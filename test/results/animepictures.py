# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import animepictures

PATTERN = r"https://oimages\.anime-pictures\.net/[0-9a-f]{3}/[0-9a-f]{32}\.\w+"

__tests__ = (
{
    "#url"     : "https://anime-pictures.net/posts/334?by_tag=11401&lang=en",
    "#category": ("booru", "animepictures", "post"),
    "#class"   : animepictures.AnimepicturesPostExtractor,
    "#results" : "https://oimages.anime-pictures.net/8a4/8a456c87a6995228ce549b61d95f995d.jpg",

    "artefacts_degree": 13.642409481167842,
    "big_preview"     : "https://opreviews.anime-pictures.net/8a4/8a456c87a6995228ce549b61d95f995d_bp.avif",
    "date"            : "dt:2009-10-11 04:28:04",
    "datetime"        : "2009-10-11T04:28:04.090651",
    "download_count"  : 602,
    "erotics"         : 0,
    "ext"             : ".jpg",
    "extension"       : "jpg",
    "file_url"        : "334-1280x1024-fate (series)-fatestay night-studio deen-type-moon-artoria pendragon (all)-saber (fate).jpg",
    "filename"        : "8a456c87a6995228ce549b61d95f995d",
    "have_alpha"      : False,
    "height"          : 1024,
    "id"              : 334,
    "juser_id"        : 1,
    "md5"             : "8a456c87a6995228ce549b61d95f995d",
    "md5_pixels"      : "949fd3f755b0cfddd34a331cd35b6572",
    "medium_preview"  : "https://opreviews.anime-pictures.net/8a4/8a456c87a6995228ce549b61d95f995d_cp.avif",
    "pubtime"         : "2009-10-11T04:28:04.090651",
    "score"           : range(5, 8),
    "score_number"    : range(8, 20),
    "size"            : 216926,
    "small_preview"   : "https://opreviews.anime-pictures.net/8a4/8a456c87a6995228ce549b61d95f995d_sp.avif",
    "smooth_degree"   : 49.744955708964795,
    "spoiler"         : False,
    "star_it"         : False,
    "status"          : 1,
    "tags_count"      : range(20, 30),
    "tied"            : [],
    "width"           : 1280,
    "color"           : [
        124,
        148,
        206,
    ],
    "favorites_users" : list,
    "tags"            : list,
    "moderator"       : dict,
    "user"            : dict,
},

{
    "#url"     : "https://anime-pictures.net/posts?search_tag=text",
    "#category": ("booru", "animepictures", "tag"),
    "#class"   : animepictures.AnimepicturesTagExtractor,
    "#pattern" : PATTERN,
    "#range"   : "1-100",
    "#count"   : 100,

    "search_tags"     : "text",
},

{
    "#url"     : "https://anime-pictures.net/posts?page=2&search_tag=^+^&order_by=date&ldate=0&lang=en",
    "#category": ("booru", "animepictures", "tag"),
    "#class"   : animepictures.AnimepicturesTagExtractor,
    "#pattern" : PATTERN,
    "#range"   : "1-100",
    "#count"   : 100,

    "search_tags"     : "^ ^",
},

{
    "#url"     : "https://anime-pictures.net/posts?favorite_by=1&favorite_folder=default&lang=en",
    "#category": ("booru", "animepictures", "favorite"),
    "#class"   : animepictures.AnimepicturesFavoriteExtractor,
    "#pattern" : PATTERN,
    "#range"   : "1-100",
    "#count"   : 100,

    "favorite_folder": "default",
    "favorite_id"    : "1",
},

{
    "#url"     : "https://anime-pictures.net/stars?page=0&lang=en",
    "#category": ("booru", "animepictures", "stars"),
    "#class"   : animepictures.AnimepicturesStarsExtractor,
    "#pattern" : PATTERN,
    "#range"   : "1-100",
    "#count"   : 100,
    "#archive" : False,

    "score": {
        "addtime" : "iso:dt",
        "id"      : int,
        "juser_id": int,
        "post"    : int,
        "score"   : int,
    },
    "user" : dict,
},

)
