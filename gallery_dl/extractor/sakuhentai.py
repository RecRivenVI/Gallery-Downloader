# -*- coding: utf-8 -*-

# Copyright 2026 Shinei Nouzen
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://www.sakuhentai.net/"""

import re
from .common import GalleryExtractor
from .. import text


class SakuhentaiGalleryExtractor(GalleryExtractor):
    """Extractor for image galleries from sakuhentai.net"""
    category = "sakuhentai"
    root = "https://www.sakuhentai.net"
    pattern = r"(?:https?://)?(?:www\.)?sakuhentai\.net/([^/?&#]+)/?$"
    example = "https://www.sakuhentai.net/GALLERY-SLUG/"

    def __init__(self, match):
        self.slug = match[1]
        url = f"{self.root}/{self.slug}/"
        GalleryExtractor.__init__(self, match, url)

    def metadata(self, page):
        gallery_id = text.parse_int(text.extr(page, "?p=", "'"))
        extr = text.extract_from(page)
        return {
            "gallery_id": gallery_id,
            "title"     : text.unescape(extr("entry-title\">", "</h1>")),
            "anime"     : text.unescape(extr(
                "cat-serie\"><h2 title=\"", "\">")),
            "character" : text.unescape(extr(
                "cat-character\"><h2 title=\"", "\">")),
            "artist"    : text.unescape(extr(
                "support-artist\"><h2 title=\"", "\">")),
        }

    def images(self, page):
        blob = text.extr(page, "let pages = [", "];")
        for url in re.findall(r'"(https?://[^"]+)"', blob):
            yield url, None
