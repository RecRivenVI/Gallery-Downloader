# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import mangayi


__tests__ = (
{
    "#url"     : "https://mangayi.com/read/ancient-animals/chapter/58/",
    "#class"   : mangayi.MangayiChapterExtractor,
    "#pattern" : r"https://scp\.keterfoundation\.com/image/ancient\-animals/chapter\-58/\d+\.jpg",
    "#count"   : 44,

    "chapter"      : 58,
    "chapter_minor": "",
    "count"        : 44,
    "date"         : "dt:2026-08-11 00:00:00",
    "extension"    : "jpg",
    "filename"     : str,
    "lang"         : "en",
    "manga"        : "Ancient Animals",
    "page"         : range(1, 44),
    "title"        : "Ep. 58 - Protect the Lake (16)",
    "volume"       : 0,
},

{
    "#url"     : "https://mangayi.com/read/blue-lock/chapter/346-2/",
    "#class"   : mangayi.MangayiChapterExtractor,
    "#results" : (
        "https://scp.keterfoundation.com/image/blue-lock/chapter-346-2/1.jpg",
        "https://scp.keterfoundation.com/image/blue-lock/chapter-346-2/2.jpg",
        "https://scp.keterfoundation.com/image/blue-lock/chapter-346-2/3.jpg",
        "https://scp.keterfoundation.com/image/blue-lock/chapter-346-2/4.jpg",
        "https://scp.keterfoundation.com/image/blue-lock/chapter-346-2/5.jpg",
        "https://scp.keterfoundation.com/image/blue-lock/chapter-346-2/6.jpg",
        "https://scp.keterfoundation.com/image/blue-lock/chapter-346-2/7.jpg",
        "https://scp.keterfoundation.com/image/blue-lock/chapter-346-2/8.jpg",
    ),

    "chapter"      : 346,
    "chapter_minor": ".2",
    "count"        : 8,
    "date"         : "dt:2026-05-19 00:00:00",
    "extension"    : "jpg",
    "filename"     : str,
    "lang"         : "en",
    "manga"        : "Blue Lock",
    "page"         : range(1, 8),
    "title"        : "Full Belt (2)",
    "volume"       : 0,
},

{
    "#url"     : "https://mangayi.com/read/eleceed/",
    "#class"   : mangayi.MangayiMangaExtractor,
    "#pattern" : mangayi.MangayiChapterExtractor.pattern,
    "#count"   : 415,

    "chapter"      : int,
    "chapter_minor": "",
    "lang"         : "en",
    "manga"        : "Eleceed",
    "title"        : str,
},

)
