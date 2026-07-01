# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import sakuhentai


__tests__ = (
{
    "#url"     : "https://www.sakuhentai.net/ino-yamanaka-hentai-gallery-pafupafu-boruto/",
    "#class"   : sakuhentai.SakuhentaiGalleryExtractor,
    "#pattern" : r"https://itadori\.sakuhentai\.net/animes/boruto/ino\-pafupafu\-\d{2}\.webp",
    "#count"   : 30,

    "anime"     : "Boruto",
    "artist"    : "PafuPafu",
    "character" : "Ino Yamanaka",
    "count"     : 30,
    "date"      : "dt:2026-03-19 16:24:36",
    "extension" : "webp",
    "filename"  : r"re:ino-pafupafu-\d+",
    "gallery_id": 27338,
    "num"       : range(1, 30),
    "title"     : "Ino Hentai Gallery by PafuPafu",
},

{
    "#url"     : "https://www.sakuhentai.net/hinata-hentai-gallery-onsen-eternoai-narutp/",
    "#class"   : sakuhentai.SakuhentaiGalleryExtractor,
    "#pattern" : r"https://www\.sakuhentai\.net/animes/naruto/hinata\-hentai\-onsen\-eternoai\-\d{2}\.webp",
    "#count"   : 13,

    "anime"     : "Naruto",
    "artist"    : "EternoAI",
    "character" : "Hinata Hyuga",
    "count"     : 13,
    "date"      : "dt:2024-08-15 21:42:38",
    "extension" : "webp",
    "filename"  : "hinata-hentai-onsen-eternoai-01",
    "gallery_id": 571,
    "num"       : range(1, 13),
    "title"     : "Hinata Onsen Hentai Gallery by EternoAI",
},

)
