# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import bilibili


__tests__ = (
{
    "#url"  : "https://www.bilibili.com/opus/988425412565532689",
    "#class": bilibili.BilibiliArticleExtractor,
    "#exception": "HttpError",
    "#results": (
        "http://i0.hdslb.com/bfs/new_dyn/311264c4dcf45261f7d7a7fe451b05b9405279279.png",
        "http://i0.hdslb.com/bfs/new_dyn/b60d8bc6996529613d617443a12c0a93405279279.png",
        "http://i0.hdslb.com/bfs/new_dyn/d4494543210d9eee5310e11dc62581e4405279279.png",
        "http://i0.hdslb.com/bfs/new_dyn/45268e63086b2d99811b2e6490130937405279279.png",
    ),

    "count"    : 4,
    "detail"   : dict,
    "extension": "png",
    "filename" : str,
    "height"   : 800,
    "id"       : "988425412565532689",
    "isClient" : False,
    "isPreview": False,
    "num"      : range(1, 4),
    "size"     : float,
    "theme"    : str,
    "themeMode": "light",
    "url"      : str,
    "username" : "平平出击",
    "width"    : 800,
},

{
    "#url"    : "https://www.bilibili.com/opus/977981688469520405",
    "#comment": "'module_top' file (#6687)",
    "#class"  : bilibili.BilibiliArticleExtractor,
    "#results": (
        "http://i0.hdslb.com/bfs/new_dyn/c74018e8272c56a6c28a1a1dc3c586311242656443.jpg",
    ),

    "content"  : ['月饼节到了，中秋快乐哦', '[龙年]'],
    "count"    : 1,
    "filename" : "c74018e8272c56a6c28a1a1dc3c586311242656443",
    "extension": "jpg",
    "width"    : 712,
    "height"   : 1068,
    "size"     : 115.80999755859375,
    "id"       : "977981688469520405",
    "title"    : "",
    "date"     : "dt:2024-09-17 03:08:26",
    "username" : "诗月饼",
},

{
    "#url"     : "https://www.bilibili.com/opus/1047501858770255875",
    "#comment" : "blocked/paid article (#7880)",
    "#class"   : bilibili.BilibiliArticleExtractor,
    "#count"   : 0,
    "#log"     : """\
1047501858770255875: Blocked Article
乌龙茶专属动态
加入当前UP主的6元档包月充电即可解锁观看\
""",
},

{
    "#url"     : "https://www.bilibili.com/opus/1154738799821979656",
    "#comment" : "livephoto (#8860)",
    "#class"   : bilibili.BilibiliArticleExtractor,
    "#results" : (
        "http://i0.hdslb.com/bfs/new_dyn/live_958a5cffe9177b196ada011867abd0a031968078.jpg",
        "https://i0.hdslb.com/bfs/dyn_video/_000003lud8wlka5eq2kxctgfx3fwo3b-1-152111110022.mp4",
    ),

    "content"     : ["太热了"],
    "extension"   : {"jpg", "mp4"},
    "date"        : "dt:2026-01-06 10:56:18",
    "width"       : 4096,
    "height"      : 3072,
    "id"          : "1154738799821979656",
    "suffix"      : {"", "l"},
    "isPreview"   : False,
    "live_url"    : "https://i0.hdslb.com/bfs/dyn_video/_000003lud8wlka5eq2kxctgfx3fwo3b-1-152111110022.mp4",
    "modern"      : True,
    "theme"       : "light",
    "themeMode"   : "light",
    "title"       : "",
    "user_id"     : 31968078,
    "username"    : "粽子淞",
},

{
    "#url"     : "https://www.bilibili.com/opus/1172711958019833880",
    "#class"   : bilibili.BilibiliArticleExtractor,
    "#count"   : 5,

    "content"  : ["*实际上是二月初的了但是现在才发:D"],
    "count"    : 5,
    "extension": "jpg",
    "id"       : "1172711958019833880",
    "suffix"   : "",
    "user_id"  : 3546898287823414,
    "username" : "锦鲤的重度依赖",
},

{
    "#url"     : "https://www.bilibili.com/opus/1214068919693738001",
    "#comment" : "'title' metadata",
    "#class"   : bilibili.BilibiliArticleExtractor,
    "#results" : (
        "http://i0.hdslb.com/bfs/new_dyn/9f0541646d1af7aa44b3fdda78cc284126089098.png",
        "http://i0.hdslb.com/bfs/new_dyn/fded8c1239fc5a024c2c3f8f1fc6da8926089098.jpg",
        "http://i0.hdslb.com/bfs/new_dyn/0278f2af582592c35fe452ccf44086a626089098.png",
        "http://i0.hdslb.com/bfs/new_dyn/d3f10e7d775b7bf4ad06084356185ef026089098.png",
        "http://i0.hdslb.com/bfs/new_dyn/56caf539db42cef0f3638185bc8fa5af26089098.png",
        "http://i0.hdslb.com/bfs/new_dyn/c37f0e997574a35c30afac7fb237e1c526089098.jpg",
        "http://i0.hdslb.com/bfs/new_dyn/a74094d76ec52ec657f56c4f2cf492a026089098.jpg",
    ),

    "content" : ["分享图片"],
    "count"   : 7,
    "date"    : "dt:2026-06-15 08:07:28",
    "id"      : "1214068919693738001",
    "tags"    : [],
    "title"   : "阶段性总结",
    "user_id" : 26089098,
    "username": "loooongm",
},

{
    "#url"     : "https://www.bilibili.com/opus/708027931618705409",
    "#comment" : "'rich' content with emoji",
    "#class"   : bilibili.BilibiliArticleExtractor,
    "#results" : "https://i0.hdslb.com/bfs/new_dyn/7ffb3e7f162503edc8a60316c5767ff26782661.jpg",

    "date"    : "dt:2022-09-20 15:49:59",
    "title"   : "",
    "user_id" : 6782661,
    "username": "箱学不动",
    "content" : [
        "二十天了！真没想到还能坚持",
        "[跪了]",
        " 之后会每五天发布一次动态",
    ],
},

{
    "#url"     : "https://www.bilibili.com/opus/958931227880980488",
    "#comment" : "'topic' metadata",
    "#class"   : bilibili.BilibiliArticleExtractor,
    "#results" : "http://i0.hdslb.com/bfs/new_dyn/29a796880f6502c13f6c7cd904fe0c241805430.jpg",

    "topic"    : "绝区零绘画",
    "topic_id" : "40061",
    "topic_url": "https://m.bilibili.com/topic-detail?topic_id=40061&topic_name=%E7%BB%9D%E5%8C%BA%E9%9B%B6%E7%BB%98%E7%94%BB",
},

{
    "#url"    : "https://space.bilibili.com/405279279/article",
    "#class"  : bilibili.BilibiliUserArticlesExtractor,
    "#pattern": bilibili.BilibiliArticleExtractor.pattern,
    "#count"  : range(50, 100),
},

{
    "#url"    : "https://space.bilibili.com/405279279/upload/opus",
    "#class"  : bilibili.BilibiliUserArticlesExtractor,
},

{
    "#url"    : "https://space.bilibili.com/405279279/dynamic",
    "#class"  : bilibili.BilibiliUserArticlesExtractor,
},

{
    "#url"    : "https://space.bilibili.com/405279279/favlist?fid=opus",
    "#class"  : bilibili.BilibiliUserArticlesFavoriteExtractor,
    "#auth"   : True,
},

)
