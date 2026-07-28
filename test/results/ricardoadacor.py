# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import szurubooru


__tests__ = (
{
    "#url"     : "https://ricardo.adacor.org/post/4489",
    "#category": ("szurubooru", "ricardoadacor", "post"),
    "#class"   : szurubooru.SzurubooruPostExtractor,
    "#results" : "https://ricardo.adacor.org/data/posts/4489_541f218e00011d84.webm",

    "canvasHeight"   : 720,
    "canvasWidth"    : 1280,
    "checksum"       : "aeb8beef35383ce405e413b35947985100bc8902",
    "checksumMD5"    : "20649cf3b15bf76f07500fe6d6aecd77",
    "commentCount"   : 0,
    "comments"       : [],
    "contentUrl"     : "data/posts/4489_541f218e00011d84.webm",
    "creationTime"   : "2026-02-24T05:48:43.180448Z",
    "date"           : "dt:2026-02-24 05:48:43",
    "extension"      : "webm",
    "favoriteCount"  : int,
    "favoritedBy"    : list,
    "featureCount"   : 0,
    "fileSize"       : 4159673,
    "filename"       : "4489_541f218e00011d84",
    "flags"          : ["loop"],
    "hasCustomThumbnail": False,
    "id"             : 4489,
    "lastEditTime"   : "2026-04-08T04:13:42.839160Z",
    "lastFeatureTime": None,
    "mimeType"       : "video/webm",
    "noteCount"      : 0,
    "notes"          : [],
    "ownFavorite"    : False,
    "ownScore"       : 0,
    "pools"          : [],
    "relationCount"  : 0,
    "relations"      : [],
    "safety"         : "safe",
    "score"          : int,
    "source"         : None,
    "tagCount"       : range(3, 20),
    "tags"           : list,
    "tags_default"   : list,
    "tags_genre"     : list,
    "thumbnailUrl"   : "data/generated-thumbnails/4489_541f218e00011d84.jpg",
    "type"           : "video",
    "version"        : 2,
    "user"           : {
        "avatarUrl": "https://gravatar.com/avatar/989911e29cf45a3abe555908534f88a2?d=retro&s=300",
        "name"     : "admin",
    },
},

{
    "#url"     : "https://ricardo.adacor.org/posts/query=football",
    "#category": ("szurubooru", "ricardoadacor", "tag"),
    "#class"   : szurubooru.SzurubooruTagExtractor,
    "#results" : (
        "https://ricardo.adacor.org/data/posts/4489_541f218e00011d84.webm",
        "https://ricardo.adacor.org/data/posts/2800_098f379b37675567.jpg",
    ),

    "search_tags": "football",
},

)
