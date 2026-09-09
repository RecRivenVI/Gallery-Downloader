# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import whitekitten


__tests__ = (
{
    "#url"     : "https://whitekitten.art/posts/1042",
    "#category": ("booru", "whitekitten", "post"),
    "#class"   : whitekitten.WhitekittenPostExtractor,
    "#count"   : 1,

    "id"              : 1042,
    "rating"          : "safe",
    "date"            : "dt:2020-12-17 00:28:59",
    "count"           : 1,
    "tags_artist"     : ["clarabelle_crow"],
    "tags_character"  : ["lori_meyers"],
    "tags_copyright"  : ["night_in_the_woods"],
    "tags_species"    : ["mouse"],
    "tags_uncategorized": list,
    "tags"            : list,
    "uploader"        : dict,
},

{
    "#url"     : "https://whitekitten.art/?q=copyright%3Anight_in_the_woods",
    "#category": ("booru", "whitekitten", "tag"),
    "#class"   : whitekitten.WhitekittenTagExtractor,
    "#pattern" : r"https://\w+\.cloudfront\.net/media/[0-9a-f]+\.\w+",
    "#count"   : range(5, 500),

    "search_tags"     : "copyright:night_in_the_woods",
},

{
    "#url"     : "https://whitekitten.art/",
    "#category": ("booru", "whitekitten", "tag"),
    "#class"   : whitekitten.WhitekittenTagExtractor,
},

{
    "#url"     : "https://whitekitten.art",
    "#category": ("booru", "whitekitten", "tag"),
    "#class"   : whitekitten.WhitekittenTagExtractor,
},
)
