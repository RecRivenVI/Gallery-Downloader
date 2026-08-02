# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import leftybooru


__tests__ = (
{
    "#url"     : "https://lefty.pictures/post/view/100",
    "#category": ("shimmie2", "leftybooru", "post"),
    "#class"   : leftybooru.LeftybooruPostExtractor,
    "#results" : "https://lefty.pictures/_images/0c5838437f4c36b9cee0ee6743883089/100%20-%20100%201girls%20blonde_hair%20blue_eyes%20cap%20character%3Arodina%20character%3Arodina_%28getchan%29%20chibi%20female%20female_only%20flag%20horn%20meta%3Atransparent_background%20milestone_post%20pioneer%20red_star%20site%3Aget%20site%3Agetchan%20solo%20star%20toot%20trumpet.png",

    "date"     : "dt:2015-10-21 17:18:09",
    "duration" : "",
    "extension": "png",
    "file_url" : "https://lefty.pictures/_images/0c5838437f4c36b9cee0ee6743883089/100%20-%20100%201girls%20blonde_hair%20blue_eyes%20cap%20character%3Arodina%20character%3Arodina_%28getchan%29%20chibi%20female%20female_only%20flag%20horn%20meta%3Atransparent_background%20milestone_post%20pioneer%20red_star%20site%3Aget%20site%3Agetchan%20solo%20star%20toot%20trumpet.png",
    "filename" : "100 - 100 1girls blonde_hair blue_eyes cap character:rodina character:rodina_(getchan) chibi female female_only flag horn meta:transparent_background milestone_post pioneer red_star site:get site:getchan solo star toot trumpet",
    "height"   : 1892,
    "id"       : 100,
    "md5"      : "0c5838437f4c36b9cee0ee6743883089",
    "parent_id": None,
    "rating"   : "s",
    "score"    : "0",
    "size"     : 820224,
    "source"   : None,
    "type"     : "image/png",
    "uploader" : "moe-anarchist",
    "width"    : 1375,
    "tags"     : [
        "100",
        "1girls",
        "blonde_hair",
        "blue_eyes",
        "cap",
        "character:rodina",
        "character:rodina_(getchan)",
        "chibi",
        "female",
        "female_only",
        "flag",
        "horn",
        "meta:transparent_background",
        "milestone_post",
        "pioneer",
        "red_star",
        "site:/get/",
        "site:getchan",
        "solo",
        "star",
        "toot",
        "trumpet",
    ],
},

{
    "#url"     : "https://lefty.pictures/post/view/23042?search=meta%3Avideo",
    "#comment" : "video",
    "#category": ("shimmie2", "leftybooru", "post"),
    "#class"   : leftybooru.LeftybooruPostExtractor,
    "#results" : "https://lefty.pictures/_images/a7f4b90646a5dbf0b0a6dfab305fa5f1/23042%20-%20ant%20antz%20film%20means_of_production%20meta%3Avideo%20revolution%20worker.mp4",

    "date"     : "dt:2024-06-18 10:40:50",
    "duration" : "16s",
    "extension": "mp4",
    "file_url" : "https://lefty.pictures/_images/a7f4b90646a5dbf0b0a6dfab305fa5f1/23042%20-%20ant%20antz%20film%20means_of_production%20meta%3Avideo%20revolution%20worker.mp4",
    "filename" : "23042 - ant antz film means_of_production meta:video revolution worker",
    "height"   : 1040,
    "id"       : 23042,
    "md5"      : "a7f4b90646a5dbf0b0a6dfab305fa5f1",
    "parent_id": None,
    "rating"   : "s",
    "score"    : "0",
    "size"     : 5452595,
    "source"   : "Ants (1998)",
    "type"     : "video/mp4",
    "uploader" : "vbee",
    "width"    : 1920,
    "tags"     : [
        "ant",
        "antz",
        "film",
        "means_of_production",
        "meta:video",
        "revolution",
        "worker",
    ],
},

{
    "#url"     : "https://lefty.pictures/post/list/vodka/1",
    "#category": ("shimmie2", "leftybooru", "tag"),
    "#class"   : leftybooru.LeftybooruTagExtractor,
    "#pattern" : r"https://lefty\.pictures/_images/[0-9a-f]{32}/\d+",
    "#count"   : 52,

    "extension"  : {"jpeg", "png", "mp4", ""},
    "file_url"   : str,
    "filename"   : str,
    "height"     : int,
    "id"         : int,
    "md5"        : "hash:md5",
    "rating"     : {"s", "q", "e"},
    "search_tags": "vodka",
    "size"       : int,
    "type"       : str,
    "width"      : int,
    "tags"       : list
},

{
    "#url"     : "https://lefty.pictures/post/list/alcohol/4",
    "#category": ("shimmie2", "leftybooru", "tag"),
    "#class"   : leftybooru.LeftybooruTagExtractor,
    "#count"   : range(30, 48),
},

{
    "#url"     : "https://lefty.pictures/post/list/1",
    "#category": ("shimmie2", "leftybooru", "tag"),
    "#class"   : leftybooru.LeftybooruTagExtractor,
},

)
