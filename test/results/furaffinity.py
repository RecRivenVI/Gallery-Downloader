# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import furaffinity


__tests__ = (
{
    "#url"     : "https://www.furaffinity.net/gallery/mirlinthloth/",
    "#class"   : furaffinity.FuraffinityGalleryExtractor,
    "#pattern" : r"https://d\d?\.f(uraffinity|acdn)\.net/art/mirlinthloth/\d+/\d+.\w+\.\w+",
    "#range"   : "45-50",
    "#count"   : 6,
},

{
    "#url"     : "https://www.furaffinity.net/gallery/markrun15/folder/173240/Inanimate/?",
    "#class"   : furaffinity.FuraffinityFolderExtractor,
    "#range"   : "46-50",
    "#urla"    : (
        "https://d.furaffinity.net/art/markrun15/1598704240/1598704240.markrun15_20200829_dusknoir_flat3.jpg",
        "https://d.furaffinity.net/art/markrun15/1598704109/1598704109.markrun15_20200829_dusknoir_flat1.jpg",
        "https://d.furaffinity.net/art/markrun15/1588674514/1588674514.markrun15_20200504_cubemorgana.jpg",
        "https://d.furaffinity.net/art/markrun15/1588501280/1588501280.markrun15_20200427_inanimate_animal3.jpg",
        "https://d.furaffinity.net/art/markrun15/1588501161/1588501161.markrun15_20200427_inanimate_animal.jpg",
    ),

    "folder_id"  : "173240",
    "folder_name": "Inanimate",
},

{
    "#url"     : "https://www.furaffinity.net/scraps/mirlinthloth/",
    "#class"   : furaffinity.FuraffinityScrapsExtractor,
    "#pattern" : r"https://d\d?\.f(uraffinity|acdn)\.net/art/[^/]+(/stories)?/\d+/\d+.\w+.",
    "#count"   : ">= 3",
},

{
    "#url"     : "https://www.furaffinity.net/favorites/mirlinthloth/",
    "#class"   : furaffinity.FuraffinityFavoriteExtractor,
    "#pattern" : r"https://d\d?\.f(uraffinity|acdn)\.net/art/[^/]+/\d+/\d+.\w+\.\w+",
    "#range"   : "45-50",
    "#count"   : 6,

    "favorite_id": int,
},

{
    "#url"     : "https://www.furaffinity.net/favorites/mirlinthloth/46682246/next?",
    "#comment" : "custom start location",
    "#class"   : furaffinity.FuraffinityFavoriteExtractor,
    "#auth"    : False,
    "#range"   : "1-3",
    "#results" : (
        "https://d.furaffinity.net/art/kacey/1263424668/1263424668.kacey_mine.jpg",
        "https://d.furaffinity.net/art/leomon32/1254250660/1254250660.leomon32_high_in_the_sky.jpg",
        "https://d.furaffinity.net/art/firefoxzero/1262442028/1262442028.firefoxzero_resolute_model_4.png",
    ),
},

{
    "#url"     : "https://www.furaffinity.net/search/?q=cute",
    "#class"   : furaffinity.FuraffinitySearchExtractor,
    "#pattern" : r"https://d\d?\.f(uraffinity|acdn)\.net/art/[^/]+/\d+/\d+.\w+\.\w+",
    "#range"   : "45-50",
    "#count"   : 6,
},

{
    "#url"     : "https://www.furaffinity.net/search/?q=leaf&range=1day",
    "#comment" : "first page of search results (#2402)",
    "#class"   : furaffinity.FuraffinitySearchExtractor,
    "#range"   : "1-3",
    "#count"   : 3,
},

{
    "#url"     : "https://www.furaffinity.net/view/21835115/",
    "#class"   : furaffinity.FuraffinityPostExtractor,
    "#pattern" : r"https://d\d*\.f(uraffinity|acdn)\.net/(download/)?art/mirlinthloth/music/1488278723/1480267446.mirlinthloth_dj_fennmink_-_bude_s_4_ever\.mp3",

    "artist"     : "mirlinthloth",
    "artist_url" : "mirlinthloth",
    "date"       : "dt:2016-11-27 17:24:06",
    "description": "A Song made playing the game Cosmic DJ.",
    "extension"  : "mp3",
    "filename"   : r"re:\d+\.\w+_dj_fennmink_-_bude_s_4_ever",
    "id"         : 21835115,
    "tags"       : list,
    "title"      : "Bude's 4 Ever",
    "url"        : r"re:https://d\d?\.f(uraffinity|acdn)\.net/art",
    "user"       : "mirlinthloth",
    "views"      : int,
    "favorites"  : int,
    "comments"   : int,
    "rating"     : "General",
    "fa_category": "Music",
    "theme"      : "All",
    "species"    : "Unspecified / Any",
    "gender"     : "Any",
    "width"      : 120,
    "height"     : 120,
    "scraps"     : False,
},

{
    "#url"     : "https://www.furaffinity.net/view/42166511/",
    "#comment" : "'external' option (#1492)",
    "#class"   : furaffinity.FuraffinityPostExtractor,
    "#options" : {"external": True},
    "#pattern" : r"https://d\d*\.f(uraffinity|acdn)\.net/|http://www\.postybirb\.com",
    "#count"   : 2,
},

{
    "#url"     : "https://www.furaffinity.net/view/45331225/",
    "#comment" : "no tags (#2277)",
    "#class"   : furaffinity.FuraffinityPostExtractor,

    "artist"     : "Kota_Remminders",
    "artist_url" : "kotaremminders",
    "date"       : "dt:2022-01-03 17:49:33",
    "fa_category": "Adoptables",
    "filename"   : "1641232173.kotaremminders_chidopts1",
    "gender"     : "Any",
    "height"     : 905,
    "id"         : 45331225,
    "rating"     : "General",
    "species"    : "Unspecified / Any",
    "tags"       : [],
    "theme"      : "All",
    "title"      : "REMINDER",
    "width"      : 1280,
},

{
    "#url"     : "https://www.furaffinity.net/view/22964019/",
    "#comment" : "get thumbnails for posts (#1284)",
    "#class"   : furaffinity.FuraffinityPostExtractor,

    "artist"      : "Dwale",
    "artist_url"  : "dwale",
    "date"        : "dt:2017-03-21 14:21:29",
    "fa_category" : "Poetry",
    "filename"    : "1490106089.dwale_poem_for_children",
    "folders"     : [],
    "height"      : 50,
    "id"          : 22964019,
    "rating"      : "General",
    "title"       : "Poem for Children Wishing to Summon Evil Spirits",
    "thumbnail"   : "https://t.furaffinity.net/22964019@600-1490106089.jpg",
    "width"       : 50,
},

{
    "#url"     : "https://www.furaffinity.net/view/34260156/",
    "#comment" : "list gallery folders for image",
    "#class"   : furaffinity.FuraffinityPostExtractor,

    "artist"      : "dbd",
    "artist_url"  : "dbd",
    "date"        : "dt:2019-12-17 22:52:01",
    "fa_category" : "All",
    "filename"    : "1576623121.dbd_patreoncustom-wdg13-web",
    "folders"     : ["By Year - 2019",
                     "Custom Character Folder - All Custom Characters",
                     "Custom Character Folder - Other Ungulates",
                     "Custom Character Folder - Female",
                     "Custom Character Folder - Patreon Supported Custom Characters"],
    "id"          : 34260156,
    "rating"      : "General",
    "title"       : "Patreon Custom Deer",
    "thumbnail"   : "https://t.furaffinity.net/34260156@600-1576623121.jpg",
    "width"       : 488,
    "height"      : 900,
    "scraps"      : False,
},

{
    "#url"     : "https://www.furaffinity.net/view/4919026/",
    "#comment" : "'scraps' metadata (#7015)",
    "#class"   : furaffinity.FuraffinityPostExtractor,
    "#auth"    : False,

    "id"         : 4919026,
    "scraps"     : True,
    "title"      : "Loth Color Test",
    "rating"     : "General",
    "theme"      : "Fantasy",
    "species"    : "Dragon (Other)",
    "gender"     : "Multiple characters",
    "width"      : 600,
    "height"     : 777,
    "user"       : "mirlinthloth",
    "date"       : "dt:2010-12-10 01:47:23",
    "description": "I think this is the first coloring for Loth that I did, I loved the goofy expression so I kept it.",
    "folders": [
        "Mirlinth Loth",
        "Akiric Works",
    ],
},

{
    "#url"     : "https://www.furaffinity.net/view/46163989/",
    "#comment" : "display names (#7115 #7123)",
    "#class"   : furaffinity.FuraffinityPostExtractor,

    "artist"    : "Pickra the magical feline",
    "artist_url": "pickra",
    "user"      : "pickra",
},

{
    "#url"     : "https://www.furaffinity.net/view/57587562",
    "#comment" : "login required",
    "#class"   : furaffinity.FuraffinityPostExtractor,
    "#count"   : 0,
},

{
    "#url"     : "https://furaffinity.net/view/21835115/",
    "#class"   : furaffinity.FuraffinityPostExtractor,
},

{
    "#url"     : "https://fxfuraffinity.net/view/21835115/",
    "#class"   : furaffinity.FuraffinityPostExtractor,
},

{
    "#url"     : "https://xfuraffinity.net/view/21835115/",
    "#class"   : furaffinity.FuraffinityPostExtractor,
},

{
    "#url"     : "https://fxraffinity.net/view/21835115/",
    "#class"   : furaffinity.FuraffinityPostExtractor,
},

{
    "#url"     : "https://sfw.furaffinity.net/view/21835115/",
    "#class"   : furaffinity.FuraffinityPostExtractor,
},

{
    "#url"     : "https://www.furaffinity.net/full/21835115/",
    "#class"   : furaffinity.FuraffinityPostExtractor,
},

{
    "#url"     : "https://www.furaffinity.net/view/30599265/",
    "#comment" : "'Image Not Found' (#195)",
    "#class"   : furaffinity.FuraffinityPostExtractor,
},

{
    "#url"     : "https://www.furaffinity.net/user/mirlinthloth/",
    "#class"   : furaffinity.FuraffinityUserExtractor,
    "#pattern" : "/gallery/mirlinthloth/$",
},

{
    "#url"     : "https://www.furaffinity.net/user/mirlinthloth/",
    "#class"   : furaffinity.FuraffinityUserExtractor,
    "#options" : {"include": "all"},
    "#pattern" : "/(gallery|scraps|favorites)/mirlinthloth/$",
    "#count"   : 3,
},

{
    "#url"     : "https://www.furaffinity.net/watchlist/by/mirlinthloth/",
    "#class"   : furaffinity.FuraffinityFollowingExtractor,
    "#pattern" : furaffinity.FuraffinityUserExtractor.pattern,
    "#range"   : "176-225",
    "#count"   : 50,
},

{
    "#url"     : "https://www.furaffinity.net/msg/submissions",
    "#class"   : furaffinity.FuraffinitySubmissionsExtractor,
    "#auth"    : True,
    "#pattern" : r"https://d\d?\.f(uraffinity|acdn)\.net/art/mirlinthloth/\d+/\d+.\w+\.\w+",
    "#range"   : "45-50",
    "#count"   : 6,
},

{
    "#url"     : "https://www.furaffinity.net/msg/submissions/new~56789000@48/",
    "#class"   : furaffinity.FuraffinitySubmissionsExtractor,
    "#auth"    : True,
},

{
    "#url"     : "https://www.furaffinity.net/journal/10144860/",
    "#class"   : furaffinity.FuraffinityJournalExtractor,
    "#results" : """\
text:Another fantasy themed pack is done, be sure to check it out:<br />
<br />
<a class="auto_link " href="https://www.furaffinity.net/view/46139064/"title="https://www.furaffinity.net/view/46139064/" >https://www.furaffinity.net/view/46139064/</a><br />
<br />
An interesting addition on this pack was the outfits. While testing it very interesting combinations with other props were possible since i separated many parts of the costumes. I hope you all find it useful for your needs. For now i'll focus on other future packs, i want to make another hybrid soon, and i also had the tigers to think about. So while i think about all of that, go and have some fun with the models.<br />
<br />
You all take care out there! See ya soon!\
""",

    "artist"    : "petruz",
    "artist_url": "petruz",
    "date"      : "dt:2022-02-27 00:59:17",
    "extension" : "htm",
    "id"        : 10144860,
    "rating"    : "General",
    "title"     : "Another Dragonlord follower...",
    "user"      : "petruz",
    "comments"  : [
        {
            "date": "dt:2022-02-27 05:00:52",
            "id"  : "58977165",
            "text": "Ooh😲",
            "user": "bedford95",
        },
        {
            "date": "dt:2022-02-28 03:04:06",
            "id"  : "58980942",
            "user": "thelight777",
            "text": str,
        },
        {
            "date": "dt:2022-02-28 10:43:46",
            "id"  : "58981829",
            "text": "clothes pack, ever?",
            "user": "whitevixenrae",
        },
    ],
},

{
    "#url"     : "https://www.furaffinity.net/journals/destellanova/",
    "#class"   : furaffinity.FuraffinityJournalsExtractor,
    "#pattern" : r'text:<b class="bbcode bbcode_b">Bastion of the Plains .+',
    "#count"   : 1,

    "artist"    : "destellanova",
    "artist_url": "destellanova",
    "date"      : "dt:2026-03-08 14:41:11",
    "extension" : "htm",
    "id"        : 11321698,
    "rating"    : "General",
    "title"     : "(C|L)oredump [0x00]: OCs",
    "user"      : "destellanova",
    "comments"  : [
        {
            "date": "dt:2026-03-08 14:42:38",
            "id"  : "61505820",
            "text": "Howdy ;0",
            "user": "lulor",
        },
        {
            "date": "dt:2026-03-08 14:54:17",
            "id"  : "61505830",
            "text": "Hi <3",
            "user": "destellanova",
        },
        {
            "date": "dt:2026-03-08 15:00:02",
            "id"  : "61505837",
            "user": "lulor",
            "text": """\
OH NOW THERES LORE GHFBFNF
looks like I just said ‘hi’ to a lore post lol\
""",
        },
        {
            "date": "dt:2026-03-08 15:03:41",
            "id"  : "61505841",
            "user": "lulor",
            "text": """\
Okay now that I’ve read I’m very interested… I already thought your sona (who I assume is Stella) was very cute and pretty, but now that I know she’s part mimic, I just wanna know more and see more about her >;0
And maybe give a fluffy hug because dying repeatedly can’t be good on the psyche -v-‘
You wanna chat on discord or something maybe? :3c @ Uberfighter\
""",
        },
    ],
},

)
