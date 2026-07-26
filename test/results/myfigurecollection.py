# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import myfigurecollection


__tests__ = (
{
    "#url"     : "https://myfigurecollection.net/item/1836466",
    "#class"   : myfigurecollection.MyfigurecollectionItemExtractor,
    "#results" : "https://static.myfigurecollection.net/upload/items/2/1836466-bb830.jpg",

    "Category"      : ["Misc"],
    "artist"        : ["Azuma Kaya (Illustrator)"],
    "character"     : ["Gene Walker"],
    "company"       : ["DMM.com (Manufacturer)"],
    "count"         : 1,
    "dimensions"    : "W= 39 mm (1.52in)    H= 100 mm (3.9in)",
    "extension"     : "jpg",
    "filename"      : "1836466-bb830",
    "height"        : 586,
    "id"            : "1836466",
    "material"      : ["Acrylic"],
    "num"           : 1,
    "origin"        : ["Shinai naru Gene e"],
    "post_url"      : "https://myfigurecollection.net/item/1836466",
    "release"       : ["2023-08: 650 JPY (Prize (Japan))"],
    "title"         : "",
    "title_html"    : "Shinai naru Gene e - Gene Walker - Acrylic Stand  (Prize B-2) - Azuma Kaya Sensei Scratch - DMM Scratch (DMM.com)",
    "various"       : "",
    "width"         : 586,
    "classification": [
        "Acrylic Stand (Prize B-2) (Type)",
        "DMM Scratch (Product line)",
        "Azuma Kaya Sensei Scratch (Series)",
    ],
    "tags"          : [
        "2023",
        "acrylic stand",
        "acrylic",
        "azuma kaya sensei scratch",
        "azuma kaya",
        "dmm.com",
        "dmm scratch",
        "jean walker",
        "shinai naru jean e",
    ],
},

{
    "#url"     : "https://myfigurecollection.net/item/161669",
    "#class"   : myfigurecollection.MyfigurecollectionItemExtractor,
    "#results" : "https://static.myfigurecollection.net/upload/items/2/161669-f06f9.jpg",

    "Category"      : ["Music"],
    "character"     : (),
    "classification": ["Original Soundtrack (Type)"],
    "company"       : ["Aniplex (Publisher)"],
    "count"         : 1,
    "dimensions"    : "",
    "extension"     : "jpg",
    "filename"      : "161669-f06f9",
    "height"        : 360,
    "id"            : "161669",
    "material"      : "",
    "num"           : 1,
    "origin"        : ["City Hunter"],
    "post_url"      : "https://myfigurecollection.net/item/161669",
    "release"       : ["2005-21-12: 3,500 JPY (Standard (Japan))"],
    "title"         : "City Hunter Sound Collection X -Theme Songs-",
    "title_html"    : "Ann Lewis - AURA - Fence of Defense - GWINKO - Humming Bird - Kaneko Mika - Kohiruimaki Kahoru - Komuro Tetsuya - Konta - NAHO - Oginome Youko - Ohsawa Yoshiyuki - Okamura Yasuyuki - PSY･S - SEX MACHINEGUNS - Suzuki Kiyomi - Takahashi Mariko - TM NETWORK - Yano Tatsumi - City Hunter - Original Soundtrack - City Hunter Sound Collection X -Theme Songs- (Aniplex)",
    "various"       : "22 tracks, 2 discs, 00:01:35",
    "width"         : 360,
    "artist"        : [
        "Ann Lewis",
        "AURA",
        "Fence of Defense",
        "GWINKO",
        "Humming Bird",
        "Kaneko Mika",
        "Kohiruimaki Kahoru",
        "Komuro Tetsuya",
        "Konta",
        "NAHO",
        "Oginome Youko",
        "Ohsawa Yoshiyuki",
        "Okamura Yasuyuki",
        "PSY･S",
        "SEX MACHINEGUNS",
        "Suzuki Kiyomi",
        "Takahashi Mariko",
        "TM NETWORK",
        "Yano Tatsumi (Performers)",
    ],
    "tags"          : [
        "2005",
        "aniplex",
        "ann lewis",
        "aura",
        "city hunter",
        "fence of defense",
        "gwinko",
        "humming bird",
        "kaneko mika",
        "kohiruimaki kahoru",
        "komuro tetsuya",
        "konta",
        "naho",
        "oginome youko",
        "ohsawa yoshiyuki",
        "okamura yasuyuki",
        "original soundtrack",
        "psy･s",
        "sex machineguns",
        "suzuki kiyomi",
        "takahashi mariko",
        "tm network",
        "yano tatsumi",
    ],
},

{
    "#url"     : "https://myfigurecollection.net/item/98662",
    "#class"   : myfigurecollection.MyfigurecollectionItemExtractor,
    "#pattern" : r"https://static\.myfigurecollection\.net/upload/(item|picture)s/2.+",
    "#count"   : 33,

    "Category"      : ["Action/Dolls"],
    "classification": ["Nendoroid (#240) (Product line)"],
    "company"       : ["Good Smile Company (Manufacturer)"],
    "count"         : 33,
    "dimensions"    : "H= 100 mm (3.9in)",
    "extension"     : {"jpg", "jpeg"},
    "filename"      : str,
    "height"        : range(200, 3000),
    "id"            : "98662",
    "num"           : range(1, 33),
    "origin"        : ["Guilty Crown"],
    "post_url"      : "https://myfigurecollection.net/item/98662",
    "release"       : ["2012-17-07: 3,619 JPY (Standard (Japan))"],
    "title"         : "",
    "title_html"    : "Guilty Crown - Fyu-Neru - Yuzuriha Inori - Nendoroid  (#240) (Good Smile Company)",
    "various"       : "Warning: a counterfeit version of this item exists.",
    "width"         : range(200, 3000),
    "artist"        : [
        "Maruhige",
        "Nendoron (Sculptors)",
    ],
    "character"     : [
        "Fyu-Neru",
        ",",
        "Yuzuriha Inori",
    ],
    "material"      : [
        "ABS",
        "PVC",
    ],
    "tags"          : [
        "2012",
        "abs",
        "amber eyes",
        "black thighhighs",
        "cat's cradle",
        "chibi",
        "detached sleeves",
        "eyes shut",
        "female",
        "female nendoroid",
        "fingerless gloves",
        "fyu-neru",
        "gloves",
        "good smile company",
        "gradient",
        "gradient clothes",
        "guilty crown",
        "gun",
        "hagoromo",
        "long sleeves",
        "maruhige",
        "midriff",
        "nendoroid",
        "nendoron",
        "no bra",
        "orange gloves",
        "pink and orange",
        "pink hair",
        "pvc",
        "red and orange",
        "red and pink",
        "red eyes",
        "red outfit",
        "thighhighs",
        "twintails",
        "weapon",
        "yuzuriha inori",
    ],
},

{
    "#url"     : "https://myfigurecollection.net/item/2827622",
    "#comment" : "'Canceled' release",
    "#class"   : myfigurecollection.MyfigurecollectionItemExtractor,
    "#results" : (
        "https://static.myfigurecollection.net/upload/items/2/2827622-b2f90.jpg",
        "https://static.myfigurecollection.net/upload/pictures/2025/05/18/4411213.png",
    ),

    "Category"      : ["Hanged up"],
    "artist"        : ["Shiratama Yupina (Illustrator)"],
    "character"     : ["Henya the Genius"],
    "company"       : ["Fourthwall (Manufacturer)"],
    "count"         : 2,
    "dimensions"    : "W= 110 mm (4.29in)    L= 15 mm (0.59in)    H= 80 mm (3.12in)",
    "id"            : "2827622",
    "material"      : "",
    "origin"        : ["VShojo"],
    "post_url"      : "https://myfigurecollection.net/item/2827622",
    "release"       : ["Canceled"],
    "title_html"    : "VShojo - Henya the Genius - Henya Bunniversary - Pass Case (Fourthwall)",
    "classification": [
        "Pass Case (Type)",
        "Henya Bunniversary (Product line)",
    ],
    "tags"          : [
        "canceled",
        "fourthwall",
        "goods",
        "henya bunniversary",
        "henya the genius",
        "pass case",
        "shiratama yupina",
        "virtual youtuber",
        "vshojo",
    ],
},

{
    "#url"     : "https://myfigurecollection.net/item/3011848",
    "#comment" : "'release' entry without price value (#294)",
    "#class"   : myfigurecollection.MyfigurecollectionItemExtractor,
    "#results" : (
        "https://static.myfigurecollection.net/upload/items/2/3011848-1ed07.jpg",
        "https://static.myfigurecollection.net/upload/pictures/2026/02/26/4761389.jpeg",
        "https://static.myfigurecollection.net/upload/pictures/2026/01/29/4717685.jpeg",
        "https://static.myfigurecollection.net/upload/pictures/2026/01/29/4717686.jpeg",
        "https://static.myfigurecollection.net/upload/pictures/2026/01/29/4717687.jpeg",
        "https://static.myfigurecollection.net/upload/pictures/2026/01/29/4717688.jpeg",
        "https://static.myfigurecollection.net/upload/pictures/2026/01/29/4717689.jpeg",
    ),

    "Category"      : ["Prepainted"],
    "artist"        : [],
    "character"     : ["Amaori Renako"],
    "classification": ["Trio-Try-iT Figure (Product line)"],
    "company"       : ["FuRyu (Manufacturer)"],
    "count"         : 7,
    "dimensions"    : "H= 180 mm (7.02in)",
    "extension"     : {"jpg", "jpeg"},
    "filename"      : str,
    "width"         : int,
    "height"        : int,
    "id"            : "3011848",
    "material"      : ["ABS", "PVC"],
    "num"           : range(1, 7),
    "origin"        : ["Watashi ga Koibito ni Nareru Wakenaijan, Muri Muri! (*Muri Janakatta!?)"],
    "post_url"      : "https://myfigurecollection.net/item/3011848",
    "release"       : ["2026-02 (Prize (Japan))"],
    "tags"          : list,
    "title"         : "",
    "title_html"    : "Watashi ga Koibito ni Nareru Wakenaijan, Muri Muri! (*Muri Janakatta!?) - Amaori Renako - Trio-Try-iT Figure (FuRyu)",
    "various"       : "",
},

{
    "#url"     : "https://myfigurecollection.net/picture/717980",
    "#class"   : myfigurecollection.MyfigurecollectionPictureExtractor,
    "#results" : "https://static.myfigurecollection.net/upload/pictures/2013/05/31/717980.jpeg",

    "date"       : "dt:2013-05-31 03:26:01",
    "extension"  : "jpeg",
    "filename"   : "717980",
    "height"     : 2048,
    "id"         : "717980",
    "post_url"   : "https://myfigurecollection.net/picture/717980",
    "size"       : 1346560,
    "title"      : "New day",
    "url"        : "https://static.myfigurecollection.net/upload/pictures/2013/05/31/717980.jpeg",
    "user"       : "anhxtan",
    "width"      : 1365,
    "description": """\
I was very nervous when trying to keep Miku and her wings on the air. She can falling down any time, and my face will turn green for sure.<br />
Luckily it was not happened ^^&quot; and the final result seemed not bad. This is <a href="https://myfigurecollection.net/blog/8391" title="https://myfigurecollection.net/blog/8391" class="internal-link">how did i pose her in the air</a><br />
<br />
Today is the last day of May and Miku is wishing the best thing to you all.\
""",
    "Category"   : [
        "Figures",
        "Lighting",
    ],
    "tags"       : [
        "ageta yukiwo",
        "aiyoku no eustia",
        "august",
        "cheerful japan!",
        "crypton future media",
        "eustia astraea",
        "fyu-neru",
        "good smile company",
        "guilty crown",
        "hatsune miku",
        "kotobukiya",
        "maruhige",
        "nendoroid",
        "nendoron",
        "nitroplus",
        "shiina mayuri",
        "steins;gate",
        "takaku & takeshi",
        "vocaloid",
        "yuzuriha inori",
    ],
},

{
    "#url"     : "https://myfigurecollection.net/profile/AliceM",
    "#class"   : myfigurecollection.MyfigurecollectionUserExtractor,
    "#options" : {"include": "all"},
    "#results" : (
        "https://myfigurecollection.net/profile/AliceM/collection/",
        "https://myfigurecollection.net/profile/AliceM/pictures/",
    )
},

{
    "#url"     : "https://myfigurecollection.net/profile/anhxtan/collection/",
    "#class"   : myfigurecollection.MyfigurecollectionUserCollectionExtractor,
    "#pattern" : myfigurecollection.MyfigurecollectionItemExtractor.pattern,
    "#count"   : range(60, 80),
},

{
    "#url"     : "https://myfigurecollection.net/?mode=view&username=AliceM&tab=collection&status=2&current=keywords&rootId=-1&categoryId=-1&output=2&sort=category&order=asc&_tb=user&page=1",
    "#class"   : myfigurecollection.MyfigurecollectionUserCollectionExtractor,
    "#pattern" : myfigurecollection.MyfigurecollectionItemExtractor.pattern,
    "#count"   : range(120, 150),
},

{
    "#url"     : "https://myfigurecollection.net/profile/AliceM/pictures/",
    "#class"   : myfigurecollection.MyfigurecollectionUserPicturesExtractor,
    "#pattern" : myfigurecollection.MyfigurecollectionPictureExtractor.pattern,
    "#count"   : range(290, 320),
},

{
    "#url"     : "https://myfigurecollection.net/?mode=view&username=anhxtan&tab=pictures&current=tags&categoryId=0&albumId=-1&sort=date&order=desc&_tb=user&page=5",
    "#class"   : myfigurecollection.MyfigurecollectionUserPicturesExtractor,
    "#pattern" : myfigurecollection.MyfigurecollectionPictureExtractor.pattern,
    "#count"   : range(60, 80),
},

{
    "#url"     : "https://myfigurecollection.net/blogpost/67474",
    "#class"   : myfigurecollection.MyfigurecollectionArticleExtractor,
    "#results" : (
        "https://static.myfigurecollection.net/upload/pictures/2024/01/08/3862217.jpeg",
        "https://static.myfigurecollection.net/upload/pictures/2024/01/08/3862221.jpeg",
        "https://static.myfigurecollection.net/upload/pictures/2025/07/04/4471120.jpeg",
    ),

    "Category" : ["Tutorial"],
    "comments" : str,
    "count"    : 3,
    "date"     : "dt:2026-07-18 23:56:33",
    "extension": "jpeg",
    "filename" : str,
    "id"       : "67474",
    "likes"    : str,
    "num"      : 1,
    "post_url" : "https://myfigurecollection.net/blogpost/67474",
    "tags"     : [],
    "title"    : "Figure LED Accessory Doesn't Work? Try this!",
    "user"     : "Toraneko",
    "views"    : str,
    "body"     : """\
Light up features on figures are pretty cool. Something to really look forward to after Preordering a figure...what will it look like?...It's gonna look so cool!...I can't wait!<br />
<br />
But that anticipation can be shattered if after receiving it you plug it in and it doesn't light up. That super sucks. I know. I've been through it.<br />
<br />
The good news is, <span class="i">there is hope!</span> if you're someone suffering in silence with a &quot;broken&quot; LED feature that won't light, there is a good chance it is NOT actually broken and you'll be able to get it to work after all. Read on to find out how.  <br />
<br />
<span style="font-size:23px;line-height:37px"><span class="b">My Experience</span></span><br />
I ordered this <a href="https://myfigurecollection.net/item/2056949" title="https://myfigurecollection.net/item/2056949" class="internal-link">Tohru nightlight</a> from the Crunchroll store. As soon as I took it out of the box, I plugged it in using a USB-C power brick and cable (not included) to see what it looked like lit up. To my dismay it did not light up. So, I tried my laptop as the power source instead of the brick. Nothing. I decided to try one more thing. I have a power bank that can charge/power items via USB-C cable. Sadly nothing. Damn... I couldn't bear to live with it not working so I had to go through the hassle of contacting Crunchyroll and requesting a replacement. The process was actually easier than I expected (I didn't even have to send the first one back). A couple weeks later I received the second one. Plugged it in. Nothing. Tried my laptop. Nothing. Like...<span class="i">WAIT-a-minute</span>--WTF? What are the odds of two different figures sent at vastly different times both being defective?<br />
<br />
<span style="font-size:23px;line-height:37px"><span class="b">The Fix!</span></span><br />
So, I decided to try more power supply/cable combinations. Even though the nightlight connector was USB-C, I know how complex that protocol is, so I suspected <span class="i">maybe</span> it was something related to that? So, I went in search of the oldest cheapest standard (USB-A) brick I could find and used a USB-C to USB-A cable to make the connection. <span class="i">IT LIT RIGHT UP!</span> I snatched the first one I'd received off the shelf, unpacked it, and plugged it in to the el-cheapo setup. Same result. Lit right up. There was nothing wrong with it at all. <br />
<br />
So, what exactly is the problem? It's hard to say with 100% certainty, but all the power sources that I used were the fast-charging IQ/PD protocol type -- even the Power bank I tried as a source.  It appears the night light may not be compatible with these types of USB-C sources. Why? Well, new fast chargers handshake between the charging device and charged device to determine the best rate at which to charge. I think the figure accessory electronics are so basic that the power sources I had used couldn't even sense there was something attached, or didn't know what rate to output the power at, so they just didn't output anything. <span class="i">I know what you're thinking.</span> &quot;Fast-charging IQ/PD chargers are like the standard right now--I'm not sure I even have a plain old dumb power source around.&quot; Yup, that is a problem, and one that makes it very hard to understand why they'd produce products not compatible with the current standard in power sources.<br />
<br />
<span style="font-size:23px;line-height:37px"><span class="b">Figures Impacted (Know so Far)</span></span><br />
The following figures have LED features that are <span class="i">known</span> to be affected by what I described above. But I suspect there are more that have this same issue. <span class="i">If you know of others, please share in the comment section.</span><br />
<br />
Item: <a href="https://myfigurecollection.net/item/2056949" title="https://myfigurecollection.net/item/2056949" class="internal-link">Kobayashi-san chi no Maid Dragon S - Tohru - Q Version</a><br />
<span class="image"><img src="https://static.myfigurecollection.net/ressources/clear.png" alt="https://static.myfigurecollection.net/upload/pictures/2024/01/08/3862217.jpeg" style="width:70%" tbx-src="https://static.myfigurecollection.net/upload/pictures/2024/01/08/3862217.jpeg"/></span><br />
<br />
<br />
Item: <a href="https://myfigurecollection.net/item/2056950" title="https://myfigurecollection.net/item/2056950" class="internal-link">Kobayashi-san chi no Maid Dragon S - Kanna Kamui - Q Version</a><br />
<span class="image"><img src="https://static.myfigurecollection.net/ressources/clear.png" alt="https://static.myfigurecollection.net/upload/pictures/2024/01/08/3862221.jpeg" style="width:70%" tbx-src="https://static.myfigurecollection.net/upload/pictures/2024/01/08/3862221.jpeg"/></span><br />
<br />
<br />
Item: <a href="https://myfigurecollection.net/item/2395834" title="https://myfigurecollection.net/item/2395834" class="internal-link">Original - &quot;Rainy Day&quot; - Meeting - 1/7</a><br />
<span class="image"><img src="https://static.myfigurecollection.net/ressources/clear.png" alt="https://static.myfigurecollection.net/upload/pictures/2025/07/04/4471120.jpeg" style="width:90%" tbx-src="https://static.myfigurecollection.net/upload/pictures/2025/07/04/4471120.jpeg"/></span><br />
<br />
<br />
Anyhow, that pretty much wraps things up! I hope you learned something from this article that may help you now or possibly in the future (If you thought this article was worthwhile don't forget to click ♡ Like at the bottom of the article). <span class="i">If you have any experiences with other figures with LEDs that could also have this issue, or you found other power combinations that work, please share your experiences in the comments section.</span> Thanks for taking the time to read my article!\
""",
},

)
