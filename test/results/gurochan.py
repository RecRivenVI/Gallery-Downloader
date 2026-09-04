# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import kokonotsuba


__tests__ = (
{
    "#url"     : "https://boards.guro.st/art/koko.php?res=7184&page=1",
    "#category": ("kokonotsuba", "gurochan", "thread"),
    "#class"   : kokonotsuba.KokonotsubaThreadExtractor,
    "#pattern" : r"https://boards\.guro\.st/art/src/\d+\.\w+",
    "#count"   : range(50, 80),
},

{
    "#url"     : "https://boards.guro.cx/art/koko.php?res=7184&page=1",
    "#category": ("kokonotsuba", "gurochan", "thread"),
    "#class"   : kokonotsuba.KokonotsubaThreadExtractor,
},

{
    "#url"     : "https://boards.guro.st/art/",
    "#category": ("kokonotsuba", "gurochan", "board"),
    "#class"   : kokonotsuba.KokonotsubaBoardExtractor,
    "#pattern" : kokonotsuba.KokonotsubaThreadExtractor.pattern,
    "#count"   : range(500, 800),
},

{
    "#url"     : "https://boards.guro.st/art/3.html",
    "#category": ("kokonotsuba", "gurochan", "board"),
    "#class"   : kokonotsuba.KokonotsubaBoardExtractor,
},

{
    "#url"     : "https://boards.guro.st/art/koko.php?page=25",
    "#category": ("kokonotsuba", "gurochan", "board"),
    "#class"   : kokonotsuba.KokonotsubaBoardExtractor,
},

{
    "#url"     : "https://boards.guro.cx/art/",
    "#category": ("kokonotsuba", "gurochan", "board"),
    "#class"   : kokonotsuba.KokonotsubaBoardExtractor,
},

)
