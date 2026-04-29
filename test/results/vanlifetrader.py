# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import vanlifetrader


__tests__ = (
{
    "#url"     : "https://vanlifetrader.com/listing/2026-geotrek-verus-awd-afeb01/",
    "#category": ("", "vanlifetrader", "listing"),
    "#class"   : vanlifetrader.VanlifetraderListingExtractor,
    "#count"   : ">= 1",

    "slug"     : "2026-geotrek-verus-awd-afeb01",
},

{
    "#url"     : "https://vanlifetrader.com/explore/",
    "#category": ("", "vanlifetrader", "explore"),
    "#class"   : vanlifetrader.VanlifetraderExploreExtractor,
    "#pattern" : vanlifetrader.VanlifetraderListingExtractor.pattern,
    "#count"   : ">= 1",
},

)
