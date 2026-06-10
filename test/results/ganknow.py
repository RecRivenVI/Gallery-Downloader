# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import ganknow


__tests__ = (
{
    "#url"     : "https://ganknow.com/kukuchi581?tab=about",
    "#category": ("", "ganknow", "user"),
    "#class"   : ganknow.GanknowUserExtractor,
    "#auth"    : "cookies",
    "#range"   : "1-3",
    "#count"   : 3,
    "#pattern" : r"https://lh3\.googleusercontent\.com/",

    "accessType": str,
    "count"     : int,
    "date"      : "type:datetime",
    "links"     : list,
    "media"     : dict,
    "media_id"  : "iso:uuid",
    "post_id"   : "iso:uuid",
    "post_url"  : r"re:https://ganknow\.com/post/[0-9a-f-]+",
    "preview"   : bool,
    "tags"      : list,
    "title"     : str,
    "type"      : "image",
    "user"      : {
        "id"      : "c0872970-df9b-4f83-b1e0-a85c3b4107fb",
        "nickname": "kukuchi581",
    },
},

{
    "#url"     : "https://ganknow.com/post/6c4ab8a6-e01d-463f-8ed5-53bead8495ee",
    "#category": ("", "ganknow", "post"),
    "#class"   : ganknow.GanknowPostExtractor,
    "#auth"    : "cookies",
    "#count"   : 1,
    "#pattern" : r"https://lh3\.googleusercontent\.com/",

    "date"    : "type:datetime",
    "media_id": "iso:uuid",
    "post_id" : "6c4ab8a6-e01d-463f-8ed5-53bead8495ee",
    "preview" : False,
    "type"    : "image",
    "user"    : {
        "id"      : "c0872970-df9b-4f83-b1e0-a85c3b4107fb",
        "nickname": "kukuchi581",
    },
},

{
    "#url"  : "https://ganknow.com/u/kukuchi581",
    "#class": ganknow.GanknowUserExtractor,
},

)
