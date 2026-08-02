# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import sofurry


__tests__ = (
{
    "#url"     : "https://sofurry.com/s/nKr2zXXm",
    "#class"   : sofurry.SofurrySubmissionExtractor,
},

{
    "#url"     : "https://sofurry.com/s/nKr2Edjm",
    "#class"   : sofurry.SofurrySubmissionExtractor,
},

{
    "#url"     : "https://sofurry.com/u/zummeng/gallery",
    "#class"   : sofurry.SofurryGalleryExtractor,
},

)
