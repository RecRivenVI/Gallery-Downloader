# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import xenforo


__tests__ = (
{
    "#url"     : "https://thirsthub.cc/threads/dakota-skye.12684/#post-616958",
    "#category": ("xenforo", "thirsthub", "post"),
    "#class"   : xenforo.XenforoPostExtractor,
},

{
    "#url"     : "https://thirsthub.cc/threads/mariangel.2/",
    "#category": ("xenforo", "thirsthub", "thread"),
    "#class"   : xenforo.XenforoThreadExtractor,
},

{
    "#url"     : "https://thirsthub.cc/forums/the-museum.72/",
    "#category": ("xenforo", "thirsthub", "forum"),
    "#class"   : xenforo.XenforoForumExtractor,
},

)
