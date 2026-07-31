# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import dcinside


__tests__ = (
{
    "#url"     : "https://gall.dcinside.com/mgallery/board/view?id=projectmx&no=14994409",
    "#class"   : dcinside.DcinsideGalleryExtractor,
    "#results" : (
        "https://dcimg1.dcinside.com/viewimage.php?id=3dafdf2ce0d12cab76&no=24b0d769e1d32ca73de885fa1bd62531058478fac3157bc024e4bab3a06677d6d31d4957ed12b900e4a4ff1ad5734a6e5c0f5d163c4901cdb8e4f7c6616fd39a3109f70107",
        "https://dcimg1.dcinside.com/viewimage.php?id=3dafdf2ce0d12cab76&no=24b0d769e1d32ca73de885fa1bd62531058478fac3157bc024e4bab3a06677d6d31d4957ed12b900e4a4ff1ad5734a6e5c0f5d163c4901cdb8e1f3926f6ad29a25dea500f8",
    ),

    "comments"    : range(25, 50),
    "content"     : "5일페 ［난선생님에게아무것도아니야사라져도누구도신경쓰지않을거야그렇지만날계속봐줬으면좋겠...］부스에 굿즈로 나가는 친구들입니다타이밍 좋게 게임에도 실장되어서 너무 기쁘네요^_^",
    "count"       : 2,
    "date"        : "dt:2025-04-22 14:37:57",
    "display_name": "메홍챠",
    "extension"   : "jpg",
    "hash"        : {
        "2caed427f6d63cb16aa8c5b158c12a3a1ad241f0fad285a362abf5ad4a",
        "2caed427f6d63cb16aa8c5b132f5020e75544ba9563d9cf99c8ea652d451ad6b3b1a",
    },
    "id"          : 14994409,
    "num"         : {1, 2},
    "title"       : "지뢰계 히카리/노조미 그림그렸어요 - 블루 아카이브 마이너 갤러리",
    "username"    : "wd3h8jz2hdnf",
    "views"       : range(5600, 9000),
},

{
    "#url"     : "https://gall.dcinside.com/mgallery/board/view?id=projectmx&no=18786425",
    "#class"   : dcinside.DcinsideGalleryExtractor,
    "#results" : "https://dcimg4.dcinside.co.kr/viewimage.php?id=3dafdf2ce0d12cab76&no=24b0d769e1d32ca73de785fa11d028311db29c13695a307ccacdd430f4f615f7eb84edfc6b29cdec230edf23c04e256cf557c84ded177ace55d1c855695cabfe62ae3774f6f10737fe8eb97661d41b7132dc",

    "comments"    : range(15, 50),
    "content"     : "호시노",
    "count"       : 1,
    "date"        : "dt:2026-07-11 05:40:41",
    "display_name": "유람",
    "extension"   : "jpg",
    "hash"        : "7cea8875b2866fff3ae68fe0449f3433a1b3fa7f1a302c6695f8b3906777b0",
    "id"          : 18786425,
    "num"         : 1,
    "title"       : "으헤으헤으헤으헤으헤으헤 - 블루 아카이브 마이너 갤러리",
    "username"    : "chinese5249",
    "views"       : range(3500, 9000),
},

{
    "#url"     : "https://gallog.dcinside.com/chinese5249",
    "#class"   : dcinside.DcinsideUserExtractor,
    "#pattern" : dcinside.DcinsideGalleryExtractor.pattern,
    "#count"   : 51,
},

{
    "#url"     : "https://gallog.dcinside.com/chinese5249/posting",
    "#class"   : dcinside.DcinsideUserExtractor,
},

{
    "#url"     : "https://gallog.dcinside.com/chinese5249/posting/index?cno=5",
    "#class"   : dcinside.DcinsideUserExtractor,
    "#results" : (
        "https://gall.dcinside.com/mgallery/board/view?id=stellive&no=4925219",
        "https://gall.dcinside.com/mgallery/board/view?id=stellive&no=4802116",
        "https://gall.dcinside.com/mgallery/board/view?id=stellive&no=4797792",
    ),
},

)
