#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gallery_dl.extractor import shareimage  # noqa E402


class TestShareimageGalleryExtractor(unittest.TestCase):

    def test_images(self):
        extr = shareimage.ShareimageGalleryExtractor.from_url(
            "https://www.share-image.com/340-example")
        page = """
        <div class="photo-card">
            <a href="/ignored" data-big-src="https://img.example/01.jpg">
                <img src="/thumb-01.jpg">
            </a>
            <a data-big-src="https://img.example/ignored.jpg"></a>
        </div>
        <div class="photo-card featured">
            <span>caption</span>
            <a data-big-src="/images/02.png" href="/view/2"></a>
        </div>
        <div class="not-photo-card">
            <a data-big-src="https://img.example/ignored.png"></a>
        </div>
        """

        self.assertEqual(extr.images(page), [
            ("https://img.example/01.jpg", None),
            ("https://www.share-image.com/images/02.png", None),
        ])

    def test_metadata(self):
        extr = shareimage.ShareimageGalleryExtractor.from_url(
            "https://www.share-image.com/340-example")
        page = '<meta property="og:title" content="Example &amp; Gallery">'

        self.assertEqual(extr.metadata(page), {
            "gallery_id": 340,
            "title": "Example & Gallery",
        })


if __name__ == "__main__":
    unittest.main()
