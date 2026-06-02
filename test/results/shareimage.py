# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import shareimage


__tests__ = (
{
    "#url"  : "https://www.share-image.com/340-amateur-set-young-girl-with-big-boobs",
    "#class": shareimage.ShareimageGalleryExtractor,
},

{
    "#url"     : "https://www.share-image.com/22836-cute-blonde-amateur-babe-shows-her-naked-body",
    "#class"   : shareimage.ShareimageGalleryExtractor,
    "#pattern" : r"https://www\.share\-image\.com/pictures/big/2026/22836/178\d+\.jpg",
    "#count"   : 68,

    "count"      : 68,
    "extension"  : "jpg",
    "filename"   : r"re:^\d+$",
    "gallery_id" : 22836,
    "gallery_url": "https://www.share-image.com/22836-cute-blonde-amateur-babe-shows-her-naked-body",
    "num"        : range(1, 68),
    "title"      : "Cute Blonde Amateur Babe shows her Naked Body",
},

)
