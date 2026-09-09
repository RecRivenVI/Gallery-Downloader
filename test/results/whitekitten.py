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
    "#results" : "https://dql0sduktnnev.cloudfront.net/media/80a7593df984a341e580c0ecb0e1f2cc3b756f7ad92e262f786a75ce1bdd0568.avif",

    "id"            : 1042,
    "rating"        : "safe",
    "date"          : "dt:2020-12-17 00:28:59",
    "date_updated"  : "type:datetime",
    "count"         : 1,
    "tags_artist"   : ["clarabelle_crow"],
    "tags_character": ["lori_meyers"],
    "tags_copyright": ["night_in_the_woods"],
    "tags_species"  : ["mouse"],
    "tags_uncategorized": ["color", "not_whitekitten"],
    "tags"          : list,
    "uploader"      : {
        "id"      : 36,
        "roles"   : ["user"],
        "username": "ddd",
    },
},

{
    "#url"     : "https://whitekitten.art/posts/1675",
    "#comment" : "multi-file post",
    "#category": ("booru", "whitekitten", "post"),
    "#class"   : whitekitten.WhitekittenPostExtractor,
    "#results" : (
        "https://dql0sduktnnev.cloudfront.net/media/b89628854b2deea4e71d386d73cc40f584699aa99228be843721c7b71009b4c6.avif",
        "https://dql0sduktnnev.cloudfront.net/media/101d0835582598b131f99c1204ff085f82615896152ebf9d4d8171409ed2657f.avif",
    ),

    "children"       : [],
    "count"          : 2,
    "createdAt"      : "2024-11-20T22:48:42.513Z",
    "date"           : "dt:2024-11-20 22:48:42",
    "date_updated"   : "dt:2026-04-25 19:25:43",
    "description"    : None,
    "descriptionHtml": None,
    "extension"      : "avif",
    "favoriteCount"  : 1,
    "filename"       : {
        "b89628854b2deea4e71d386d73cc40f584699aa99228be843721c7b71009b4c6",
        "101d0835582598b131f99c1204ff085f82615896152ebf9d4d8171409ed2657f",
    },
    "hasCustomThumbnail": False,
    "icameCount"     : int,
    "id"             : 1675,
    "isFavorited"    : False,
    "nextId"         : 1674,
    "num"            : range(1, 3),
    "parentId"       : None,
    "prevId"         : 1677,
    "rating"         : "safe",
    "score"          : range(3, 30),
    "sourceUrls"     : None,
    "tags_artist"    : ["yonell"],
    "tags_character" : ["emmett_stone"],
    "updatedAt"      : "2026-04-25T19:25:43.297Z",
    "userScore"      : None,
    "visibility"     : "public",
    "tags"           : [
        "bird",
        "color",
        "emmett_stone",
        "inks",
        "male",
        "oc_[whitekitten]",
        "peacock",
        "yonell",
    ],
    "tags_species"   : [
        "bird",
        "peacock",
    ],
    "tags_uncategorized": [
        "color",
        "inks",
        "male",
        "oc_[whitekitten]",
    ],
    "file"           : dict,
    "uploader"       : {
        "avatarUrl": "https://dql0sduktnnev.cloudfront.net/avatars/1.webp",
        "id"       : 1,
        "roles"    : ["owner"],
        "username" : "whitekitten",
    },
},

{
    "#url"     : "https://whitekitten.art/?q=copyright%3Anight_in_the_woods",
    "#category": ("booru", "whitekitten", "tag"),
    "#class"   : whitekitten.WhitekittenTagExtractor,
    "#pattern" : r"https://\w+\.cloudfront\.net/media/[0-9a-f]+\.\w+",
    "#count"   : range(5, 500),

    "search_tags": "copyright:night_in_the_woods",
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
