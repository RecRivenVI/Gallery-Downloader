# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import fileditchfiles


__tests__ = (
{
    "#url"     : "https://fileditchfiles.st/beta16/edbb4e3dfa0b08137768/begging-emoticon-showing-clasped-hands-41405302.webp",
    "#class"   : fileditchfiles.FileditchfilesFileExtractor,
    "#pattern" : r"https://alpha\.freakingfileditch\.me/beta16/edbb4e3dfa0b08137768/begging-emoticon-showing-clasped-hands-41405302\.webp\?md5=.+&expires=\d+",

    "downloads": int,
    "id"       : "edbb4e3dfa0b08137768",
    "path"     : "/beta16/edbb4e3dfa0b08137768/begging-emoticon-showing-clasped-hands-41405302.webp",
    "size"     : 28662,
    "slug"     : "begging-emoticon-showing-clasped-hands-41405302.webp",
},

{
    "#url"     : "https://theditch.st/djfn3zqm",
    "#class"   : fileditchfiles.FileditchfilesShorturlExtractor,
    "#results" : "https://fileditchfiles.st/beta16/edbb4e3dfa0b08137768/begging-emoticon-showing-clasped-hands-41405302.webp",

    "id"       : "djfn3zqm"
},

)
