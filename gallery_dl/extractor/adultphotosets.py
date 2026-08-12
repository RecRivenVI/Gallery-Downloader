# -*- coding: utf-8 -*-

# Copyright 2026 w43322

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://adultphotosets.best/"""

import re

from .common import Extractor, Message
from .. import text


BASE_PATTERN = r"(?:https?://)?(?:www\.)?adultphotosets\.best"
PHOTO_CATEGORIES = (
    "amateur-photo",
    "alternative-photo-sets",
    "artistic-photo-sets",
    "hardcore-photo-sets",
    "hentai-pictures",
    "lesbian-photo-sets",
    "softcore-photo-sets",
)
PHOTO_PATTERN = "(?:" + "|".join(PHOTO_CATEGORIES) + ")"


class AdultphotosetsExtractor(Extractor):
    """Base class for adultphotosets extractors"""
    category = "adultphotosets"
    root = "https://adultphotosets.best"
    request_interval = (0.5, 1.5)

    def items(self):
        data = {"_extractor": AdultphotosetsGalleryExtractor}
        for url in self.galleries():
            yield Message.Queue, url, data

    def _pagination(self, url):
        gallery_re = re.compile(AdultphotosetsGalleryExtractor.pattern)

        while True:
            page = self.request(url).text

            for gallery_url in text.extract_iter(
                    page, '<h2 class="title"><a href="', '"'):
                if gallery_re.match(gallery_url):
                    yield gallery_url

            nav = text.extr(page, '<span class="page_next"', '</span>')
            url = text.extr(nav, '<a href="', '"')
            if not url:
                return


class AdultphotosetsGalleryExtractor(AdultphotosetsExtractor):
    """Extractor for adultphotosets image galleries"""
    subcategory = "gallery"
    parent = True
    directory_fmt = ("{category}", "{title} ({gallery_id})")
    pattern = (BASE_PATTERN + r"(?:/(" + PHOTO_PATTERN +
               r"))?/(\d+)-([^/?#]+)\.html")
    example = "https://adultphotosets.best/hardcore-photo-sets/123-TITLE.html"

    def __init__(self, match):
        AdultphotosetsExtractor.__init__(self, match)
        self.section, self.gallery_id, self.slug = match.groups()
        self.url = match[0]

    def items(self):
        page = self.request(self.url).text
        article = text.extr(
            page, '<article class="box story fullstory">', '</article>')
        images = self.images(article)
        data = self.metadata(page, article)
        data["count"] = len(images)

        yield Message.Directory, "", data
        for data["num"], url in enumerate(images, 1):
            yield Message.Queue, url, data

    def metadata(self, page, article):
        tags = text.extr(page, '<div class="tag_list">', '</div>')

        return {
            "gallery_id": text.parse_int(self.gallery_id),
            "slug"      : self.slug,
            "section"   : self.section or "",
            "title"     : text.unescape(text.extr(
                article,
                '<h2 class="title">', '</h2>')).strip(),
            "date"      : self.parse_datetime_iso(text.extr(
                article,
                '<time datetime="', '"')),
            "uploader"  : text.unescape(text.extr(
                article,
                "onclick=\"ShowProfile('", "'")),
            "tags"      : text.split_html(tags),
            "views"     : text.parse_int(text.extr(
                article, 'title="Views: ', '"')),
            "comments"  : text.parse_int(text.extr(
                article, 'title="Comments: ', '"')),
        }

    @staticmethod
    def images(article):
        content = text.extr(article, '<div class="text">',
                            '<div class="story_tools')
        results = []
        for anchor in text.extract_iter(content, "<a ", "</a>"):
            if 'target="_blank"' in anchor and "<img " in anchor:
                url = text.extr(anchor, 'href="', '"')
                if url:
                    results.append(url)
        return results


class AdultphotosetsTagExtractor(AdultphotosetsExtractor):
    """Extractor for adultphotosets tag searches"""
    subcategory = "tag"
    pattern = BASE_PATTERN + r"/tags/([^/?#]+)"
    example = "https://adultphotosets.best/tags/TAG/"

    def galleries(self):
        tag = self.groups[0]
        self.kwdict["search_tags"] = text.unquote(tag)
        return self._pagination(f"{self.root}/tags/{tag}/")


class AdultphotosetsCategoryExtractor(AdultphotosetsExtractor):
    """Extractor for adultphotosets image categories"""
    subcategory = "category"
    pattern = BASE_PATTERN + r"/(" + PHOTO_PATTERN + r")/?$"
    example = "https://adultphotosets.best/softcore-photo-sets/"

    def galleries(self):
        section = self.groups[0]
        self.kwdict["section"] = section
        return self._pagination(f"{self.root}/{section}/")


class AdultphotosetsHomeExtractor(AdultphotosetsExtractor):
    """Extractor for the adultphotosets home listing"""
    subcategory = "home"
    pattern = BASE_PATTERN + r"/?$"
    example = "https://adultphotosets.best/"

    def galleries(self):
        return self._pagination(self.root + "/")
