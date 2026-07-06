# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import shimmie2


__tests__ = (
{
    "#url"     : "https://www.prequeladventure.com/fanartbooru/post/view/9272",
    "#category": ("shimmie2", "prequelfanart", "post"),
    "#class"   : shimmie2.Shimmie2PostExtractor,
    "#results" : "https://www.prequeladventure.com/fanartbooru/_images/6868d398a2539d98cfbd07eaddf974ab/9272%20-%20argonian%20artist%3Airenewavys%20character%3AQuill-Weave.jpeg",

    "extension": "jpeg",
    "file_url" : "https://www.prequeladventure.com/fanartbooru/_images/6868d398a2539d98cfbd07eaddf974ab/9272%20-%20argonian%20artist%3Airenewavys%20character%3AQuill-Weave.jpeg",
    "filename" : "9272 - argonian artist:irenewavys character:Quill-Weave",
    "height"   : 544,
    "id"       : 9272,
    "md5"      : "6868d398a2539d98cfbd07eaddf974ab",
    "size"     : 0,
    "tags"     : "argonian artist:irenewavys character:Quill-Weave",
    "width"    : 424,
},

{
    "#url"     : "https://www.prequeladventure.com/fanartbooru/post/list/argonian/1",
    "#category": ("shimmie2", "prequelfanart", "tag"),
    "#class"   : shimmie2.Shimmie2TagExtractor,
    "#pattern" : r"https://www\.prequeladventure\.com/fanartbooru/_images/\w{32}/\d+.+",
    "#range"   : "1-100",
    "#count"   : 100,

    "extension"  : "jpg",
    "file_url"   : r"re:https://www.prequeladventure.com/fanartbooru/_images/.+",
    "filename"   : str,
    "height"     : 0,
    "id"         : int,
    "md5"        : "hash:md5",
    "search_tags": "argonian",
    "size"       : 0,
    "tags"       : str,
    "width"      : 0,
},

)
