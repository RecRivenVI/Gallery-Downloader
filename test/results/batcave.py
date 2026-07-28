# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import batcave


__tests__ = (
{
    "#url"     : "https://batcave.biz/reader/28592/199055",
    "#class"   : batcave.BatcaveIssueExtractor,
    "#auth"    : True,
    "#pattern" : r"https://img\.batcave\.biz/img/29/28592/199055/\d+\-[0-9a-f]{32}\.jpg",
    "#count"   : 29,

    "comic"       : "The Maxx (1993-1998)",
    "comic_id"    : 28592,
    "count"       : 29,
    "date"        : "dt:2023-10-18 00:00:00",
    "extension"   : "jpg",
    "filename"    : str,
    "issue"       : 25,
    "issue_id"    : 199055,
    "issue_string": "Issue #25",
    "lang"        : "en",
    "page"        : range(1, 29),
},

{
    "#url"     : "https://batcave.biz/31508-witchblade-1995-2015.html",
    "#class"   : batcave.BatcaveComicExtractor,
    "#pattern" : batcave.BatcaveIssueExtractor.pattern,
    "#auth"    : True,
    "#count"   : 189,

    "broken"  : False,
    "id"      : int,
    "pages"   : int,
    "posi"    : int,
    "title"   : str,
    "title_en": str,
},

)
