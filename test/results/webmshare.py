# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import webmshare


__tests__ = (
{
    "#url"     : "https://webmshare.com/O9mWY",
    "#category": ("", "webmshare", "video"),
    "#class"   : webmshare.WebmshareVideoExtractor,

    "date"     : "dt:2022-12-04 00:00:00",
    "extension": "webm",
    "filename" : "O9mWY",
    "height"   : 568,
    "id"       : "O9mWY",
    "thumb"    : "https://s1.webmshare.com/t/O9mWY.jpg",
    "title"    : "Yeah buddy over here",
    "url"      : "https://s1.webmshare.com/O9mWY.webm",
    "views"    : int,
    "width"    : 320,
},

{
    "#url"     : "https://s1.webmshare.com/zBGAg.webm",
    "#category": ("", "webmshare", "video"),
    "#class"   : webmshare.WebmshareVideoExtractor,

    "date"  : "dt:2018-12-07 00:00:00",
    "height": 1080,
    "id"    : "zBGAg",
    "thumb" : "https://s1.webmshare.com/t/zBGAg.jpg",
    "title" : "",
    "url"   : "https://s1.webmshare.com/zBGAg.webm",
    "views" : int,
    "width" : 1920,
},

{
    "#url"     : "https://webmshare.com/play/zBGAg",
    "#category": ("", "webmshare", "video"),
    "#class"   : webmshare.WebmshareVideoExtractor,
},

{
    "#url"     : "https://webmshare.com/download-webm/zBGAg",
    "#category": ("", "webmshare", "video"),
    "#class"   : webmshare.WebmshareVideoExtractor,
},

{
    "#url"     : "https://webmshare.com/oO9Z0",
    "#comment" : "18+",
    "#class"   : webmshare.WebmshareVideoExtractor,
    "#results" : "https://s1.webmshare.com/oO9Z0.webm",

    "date"     : "dt:2026-06-22 00:00:00",
    "extension": "webm",
    "filename" : "oO9Z0",
    "height"   : 1440,
    "id"       : "oO9Z0",
    "thumb"    : "https://s1.webmshare.com/t/oO9Z0.jpg",
    "title"    : "めぐみん Bass Knight with Megumin",
    "url"      : "https://s1.webmshare.com/oO9Z0.webm",
    "views"    : int,
    "width"    : 2560,
},

{
    "#url"     : "https://webmshare.com/results?q=nature",
    "#class"   : webmshare.WebmshareSearchExtractor,
    "#results" : (
        "https://webmshare.com/VVO1v",
        "https://webmshare.com/jxa11",
        "https://webmshare.com/DeWDV",
        "https://webmshare.com/93GOD",
        "https://webmshare.com/RyoEW",
        "https://webmshare.com/3jODz",
        "https://webmshare.com/ZQ4GJ",
        "https://webmshare.com/6jLQ1",
        "https://webmshare.com/WWNwd",
    ),

    "search_tags": "nature",
},

)
