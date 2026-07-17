# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import vanlifetrader


__tests__ = (
{
    "#url"     : "https://vanlifetrader.com/listing/untrapped-solutions-new-build-mercedes-sprinter-144-awd-a2738b/",
    "#class"   : vanlifetrader.VanlifetraderListingExtractor,
    "#pattern" : r"https://vanlifetrader\.com/wp\-content/uploads/2025/08/.+",
    "#count"   : 30,

    "date"      : "dt:2026-02-14 16:31:41",
    "extension" : "jpg",
    "filename"  : str,
    "listing_id": 416977,
    "media_id"  : int,
    "num"       : range(1, 30),
    "slug"      : "untrapped-solutions-new-build-mercedes-sprinter-144-awd-a2738b",
    "title"     : "Untrapped Solutions New Build: Mercedes Sprinter 144 AWD",
},

{
    "#url"     : "https://vanlifetrader.com/explore/",
    "#class"   : vanlifetrader.VanlifetraderExploreExtractor,
    "#pattern" : vanlifetrader.VanlifetraderListingExtractor.pattern,
    "#count"   : ">= 1",
},

)
