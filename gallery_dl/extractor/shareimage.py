# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://www.share-image.com/"""

from .common import GalleryExtractor
from .. import text


class ShareimageGalleryExtractor(GalleryExtractor):
    """Extractor for image galleries from share-image.com"""
    category = "shareimage"
    root = "https://www.share-image.com"
    pattern = (
        r"(?:https?://)?(?:www\.)?share-image\.com"
        r"(/(\d+)[^/?#]*)(?:/?(?:[?#].*)?)?$"
    )
    example = "https://www.share-image.com/12345-gallery-title"

    def __init__(self, match):
        GalleryExtractor.__init__(self, match, self.root + match[1])

    def metadata(self, page):
        return {
            "gallery_id": text.parse_int(self.groups[1]),
            "title": text.unescape(text.extr(
                page, '<meta property="og:title" content="', '"') or ""),
        }

    def images(self, page):
        find_images = text.re(
            r'''(?s)<div[^>]+class=["'][^"']*(?<![\w-])photo-card'''
            r'''(?![\w-])[^"']*["']'''
            r'''[^>]*>.*?<a\b([^>]*)''').finditer
        find_src = text.re(
            r'''\sdata-big-src=(["'])(.*?)\1''').search

        return [
            (text.urljoin(self.root, text.unescape(match[2])), None)
            for card in find_images(page)
            if (match := find_src(card[1]))
        ]
