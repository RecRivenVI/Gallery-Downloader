# -*- coding: utf-8 -*-

# Copyright 2026 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://myfigurecollection.net/"""

from .common import Extractor, Message
from .. import text, util

BASE_PATTERN = r"(?:https?://)?(?:www\.)?myfigurecollection\.net"
USER_PATTERN = BASE_PATTERN + r"/profile/([^/?#]+)"


class MyfigurecollectionExtractor(Extractor):
    """Base class for myfigurecollection extractors"""
    category = "myfigurecollection"
    root = "https://myfigurecollection.net"


class MyfigurecollectionItemExtractor(MyfigurecollectionExtractor):
    subcategory = "item"
    directory_fmt = ("{category}", "Items")
    filename_fmt = "{id}_{num:>02}_{filename}.{extension}"
    archive_fmt = "{id}_{num}"
    pattern = BASE_PATTERN + r"/item/(\d+)"
    example = "https://myfigurecollection.net/item/12345"

    def items(self):
        item_id = self.groups[0]
        url = f"{self.root}/item/{item_id}"
        page = self.request(url).text
        extr = text.extract_from(page)

        item = {
            "id"        : item_id,
            "title_html": text.unescape(extr(
                'property="og:title" content="', '"')),
            "post_url"  : text.unescape(extr(
                'property="og:url" content="', '"')),
            "pictures"  : extr(
                'name="pictures" content="', '"'),
            "Category"  : split(extr(
                'class="data-label">Categor', "</div></div>")),
            "classification": split_meta(extr(
                'class="data-label">Classificatio', "</div></div>")),
            "title"     : rm(extr(
                'class="data-label">Title', "</div></div>")),
            "origin"    : split(extr(
                'class="data-label">Origi', "</div></div>")),
            "character" : split(extr(
                'class="data-label">Characte', "</div></div>")),
            "company"   : split_meta(extr(
                'class="data-label">Compan', "</div></div>")),
            "artist"    : split_meta(extr(
                'class="data-label">Artis', "</div></div>")),
            "release"   : self._parse_releases(extr(
                'class="data-label">Releas',
                '</div></div><div class="data-field"><div class="data-l')),
            "material"  : rm(extr(
                'abel">Materia', "</div></div>")),
            "dimensions": rm(extr(
                'abel">Dimensio', "</div></div>")),
            "various"   : rm(extr(
                'abel">Variou', "</div></div>")),
            "tags"      : text.split_html(extr(
                '<div class="object-tags">', "</section>"))[::2],
        }

        item["material"] = m.split(" , ") if (m := item["material"]) else ""

        files = util.json_loads(text.unquote(item.pop("pictures")))
        item["count"] = len(files)

        yield Message.Directory, "", item
        for item["num"], file in enumerate(files, 1):
            url = file["src"]
            item["width"] = file["w"]
            item["height"] = file["h"]
            yield Message.Url, url, text.nameext_from_url(url, item)

    def _parse_releases(self, html):
        items = html.split('<div class="data-value">')
        del items[0]

        results = []
        for item in items:
            date, pos = text.extract(item, ">", "<")
            type, pos = text.extract(item, "<em>", "<", pos)
            price, pos = text.extract(item, "<br/>", "(", pos)

            parts = date.split("/")
            try:
                date = f"{parts[2]}-{parts[1]}-{parts[0]}"
            except Exception:
                date = f"{parts[1]}-{parts[0]}"
            name = f"{date}: {price.replace('<small>', '').strip()}"
            if type:
                name = f"{name} ({type})"
            results.append(name)
        return results


def split(html):
    if not html:
        return ()
    results = text.split_html(html)
    del results[0]
    return results


def split_meta(html):
    items = html.split("<meta ")
    del items[0]

    results = []
    for item in items:
        pos = item.find("</span>")
        name = text.unescape(item[item.rfind(">", 0, pos)+1:pos])
        if role := text.extr(item, "<em>", "<"):
            name = f"{name} ({text.unescape(role)})"
        results.append(name)
    return results


def rm(html):
    return (text.unescape(text.remove_html(html[html.find(">")+1:]))
            if html else "")
