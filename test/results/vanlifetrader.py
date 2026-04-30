# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import vanlifetrader


__tests__ = (
{
    "#url"     : "https://vanlifetrader.com/listing/untrapped-solutions-new-build-mercedes-sprinter-144-awd-a2738b/",
    "#category": ("", "vanlifetrader", "listing"),
    "#class"   : vanlifetrader.VanlifetraderListingExtractor,
    "#count"   : ">= 1",

    "slug"     : "untrapped-solutions-new-build-mercedes-sprinter-144-awd-a2738b",
},

{
    "#url"     : "https://vanlifetrader.com/explore/",
    "#category": ("", "vanlifetrader", "explore"),
    "#class"   : vanlifetrader.VanlifetraderExploreExtractor,
    "#pattern" : vanlifetrader.VanlifetraderListingExtractor.pattern,
    "#count"   : ">= 1",
},

)
