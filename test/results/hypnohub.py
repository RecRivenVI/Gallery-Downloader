# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import gelbooru_v02


__tests__ = (
{
    "#url"     : "https://hypnohub.net/index.php?page=post&s=list&tags=gonoike_biwa",
    "#category": ("gelbooru_v02", "hypnohub", "tag"),
    "#class"   : gelbooru_v02.GelbooruV02TagExtractor,
    "#pattern": r"https://hypnohub.net//images/../../\w{32}.(jpg|png)",
},

{
    "#url"     : "https://hypnohub.net/index.php?page=pool&s=show&id=61",
    "#category": ("gelbooru_v02", "hypnohub", "pool"),
    "#class"   : gelbooru_v02.GelbooruV02PoolExtractor,
    "#results" : (
        "https://hypnohub.net//images/60/93/6093f0e9fbe9697b519c3a60865b4f8e.jpg",
        "https://hypnohub.net//images/40/0d/400d41d179d1b792e80d27e46b4a53a2.jpg",
        "https://hypnohub.net//images/9a/8e/9a8ed3843ce4113c03bfa9cc219b47fa.jpg",
    ),
},

{
    "#url"     : "https://hypnohub.net/index.php?page=favorites&s=view&id=43546",
    "#category": ("gelbooru_v02", "hypnohub", "favorite"),
    "#class"   : gelbooru_v02.GelbooruV02FavoriteExtractor,
    "#count"   : 3,
},

{
    "#url"     : "https://hypnohub.net/index.php?page=post&s=view&id=1439",
    "#category": ("gelbooru_v02", "hypnohub", "post"),
    "#class"   : gelbooru_v02.GelbooruV02PostExtractor,
    "#options"     : {
        "tags" : True,
        "notes": True,
    },
    "#pattern"     : r"https://hypnohub\.net//images/90/24/90245c3c5250c2a8173255d3923a010b\.jpg",
    "#sha1_content": "5987c5d2354f22e5fa9b7ee7ce4a6f7beb8b2b71",

    "tags_artist"   : "brokenteapot",
    "tags_character": "hsien-ko",
    "tags_copyright": "capcom darkstalkers",
    "tags_general"  : str,
    "tags_metadata" : "dialogue text translated",
    "notes"         : [
        {
            "body"  : "Master Master Master Master Master Master",
            "height": 83,
            "id"    : 10577,
            "width" : 129,
            "x"     : 259,
            "y"     : 20,
        },
        {
            "body"  : "Response Response Response Response Response Response",
            "height": 86,
            "id"    : 10578,
            "width" : 125,
            "x"     : 126,
            "y"     : 20,
        },
        {
            "body"  : "Obedience Obedience Obedience Obedience Obedience Obedience",
            "height": 80,
            "id"    : 10579,
            "width" : 98,
            "x"     : 20,
            "y"     : 20,
        },
    ],
},

{
    "#url"     : "https://hypnohub.net/index.php?page=post&s=view&id=168597",
    "#comment" : "'Access Restricted' (gh#9586)",
    "#category": ("gelbooru_v02", "hypnohub", "post"),
    "#class"   : gelbooru_v02.GelbooruV02PostExtractor,
    "#results"     : "https://hypnohub.net//images/02/79/0279d7acb918e80f3289c7b1c8eef8a4.png",
    "#sha1_content": "7e8f23860dad284a042161d57cf4a4f7bbff30ea",

    "file_url": "https://hypnohub.net/images/02/79/0279d7acb918e80f3289c7b1c8eef8a4.png",
    "id"      : "168597",
    "md5"     : "0279d7acb918e80f3289c7b1c8eef8a4",
},

)
