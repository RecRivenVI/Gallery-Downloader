# -*- coding: utf-8 -*-

# Copyright 2026 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://artfight.net/"""

from .common import Extractor, Message, Dispatch
from .. import text, util

BASE_PATTERN = r"(?:https?://)?(?:www\.)?artfight\.net"
USER_PATTERN = BASE_PATTERN + r"/~([^/?#]+)"


class ArtfightExtractor(Extractor):
    """Base class for artfight extractors"""
    category = "artfight"
    root = "https://artfight.net"
    cookies_domain = ".artfight.net"
    directory_fmt = ("{category}", "{artist}", "{type!c}s")
    filename_fmt = "{id}_{title}.{extension}"
    archive_fmt = "{id}"
    request_interval = (0.5, 1.5)
    tls12 = False  # CF

    def items(self):
        self.kwdict["username"] = text.unquote(self.groups[0])
        for post_url in self.posts():
            try:
                post = self._extract(post_url)
            except Exception as exc:
                self.log.traceback(exc)
                self.log.warning("Failed to process '%s' (%s: %s)",
                                 post_url, exc.__class__.__name__, exc)
                continue

            url = post["file"]
            text.nameext_from_url(url, post)
            yield Message.Directory, "", post
            yield Message.Url, url, post

    def _extract(self, url):
        html = self.request(url).text
        extr = text.extract_from(html)
        _, type, name = url.rsplit("/", 2)
        title, _, artist = extr(' title="', '"').rpartition(" by ")
        return {
            "id"    : name[:name.rfind(".")],
            "type"  : type,
            "title" : text.unescape(title),
            "artist": text.unescape(artist),
            "date"  : self.parse_datetime(
                extr(">On: </strong>", "<") or
                extr(">Created: </strong>", "<"),
                "%d %B %Y %I:%M:%S %p"),
            "file"  : text.unescape(extr('<a target="_blank" href="', '"')),
            "description": text.remove_html(extr(
                "<!-- Attack description -->", "<!--")),
            "page_url"   : url,
        }

    def _pagination(self, url, type):
        begin = f'class="profile-{type}s-body'
        end = 'class="d-flex justify-content-center'

        while True:
            page = self.request(url).text

            items = text.extr(page, begin, end)
            yield from text.extract_iter(items, '<a href="', '"')

            link = text.iextr(page, 'rel="next"', "<", ">")
            if url := text.extr(link, 'href="', '"'):
                url = text.unescape(url)
            else:
                break


class ArtfightUserExtractor(Dispatch, ArtfightExtractor):
    pattern = USER_PATTERN + "$"
    example = "https://artfight.net/~USER"

    def items(self):
        base = f"{self.root}/~{self.groups[0]}/"
        return self._dispatch_extractors((
            (ArtfightCharactersExtractor, base + "characters"),
            (ArtfightAttacksExtractor   , base + "attacks"),
            (ArtfightDefensesExtractor  , base + "defenses"),
        ), ("characters", "attacks", "defenses",))


class ArtfightCharactersExtractor(ArtfightExtractor):
    subcategory = "characters"
    directory_fmt = ("{category}", "{username}", "Characters")
    archive_fmt = "c{id}"
    pattern = USER_PATTERN + r"/characters"
    example = "https://artfight.net/~USER/characters"

    def posts(self):
        return self._pagination(
            f"{self.root}/~{self.groups[0]}/characters", "character")


class ArtfightAttacksExtractor(ArtfightExtractor):
    subcategory = "attacks"
    directory_fmt = ("{category}", "{username}", "Attacks")
    archive_fmt = "a{id}"
    pattern = USER_PATTERN + r"/attacks"
    example = "https://artfight.net/~USER/attacks"

    def posts(self):
        return self._pagination(
            f"{self.root}/~{self.groups[0]}/attacks", "attack")


class ArtfightDefensesExtractor(ArtfightExtractor):
    subcategory = "defenses"
    directory_fmt = ("{category}", "{username}" "Defenses")
    archive_fmt = "d{id}"
    pattern = USER_PATTERN + r"/defenses"
    example = "https://artfight.net/~USER/defenses"

    def posts(self):
        return self._pagination(
            f"{self.root}/~{self.groups[0]}/defenses", "defense")


class ArtfightPostExtractor(ArtfightExtractor):
    subcategory = "post"
    pattern = BASE_PATTERN + r"(/(?:character|attack)/\d+(?:\.[^/?#]+)?)"
    example = "https://artfight.net/attack/12345.SLUG"

    def posts(self):
        self.kwdict["username"] = ""
        return (self.root + self.groups[0],)


class ArtfightAssetsExtractor(ArtfightExtractor):
    subcategory = "assets"
    directory_fmt = ("{category}", "Art Assets")
    filename_fmt = "{num:>03}_{filename}.{extension}"
    archive_fmt = "art_assets/{filename}"
    pattern = BASE_PATTERN + r"/info/art-assets"
    example = "https://artfight.net/info/art-assets"

    def items(self):
        url = self.root + "/info/art-assets"
        page = self.request(url).text
        extr = text.extract_from(page)
        urls = list(util.unique(text.re(
            r'<img [^>]*src="([^"]+)').findall(page)))

        data = {
            "id"    : 0,
            "count" : len(urls),
            "title" : text.unescape(extr("<h1>", "<")),
            "date"  : self.parse_datetime(
                extr("</a></strong>, ", "<"), "%d %B %Y %I:%M:%S %p"),
            "page_url"   : url,
        }

        yield Message.Directory, "", data
        for num, url in enumerate(urls, 1):
            data["num"] = num
            data["file"] = url
            text.nameext_from_url(url, data)
            yield Message.Url, url, data
