# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import adultphotosets


__tests__ = (
{
    "#url"     : "https://adultphotosets.best/softcore-photo-sets/188185-nucosplay-sunako-k-breathtaking-sunako-k-is-an-extra-slutty-night-elf-62-images-set.html",
    "#category": ("", "adultphotosets", "gallery"),
    "#class"   : adultphotosets.AdultphotosetsGalleryExtractor,
    "#range"   : "1-3",
    "#results" : (
        "https://imx.to/i/6krfdv",
        "https://imx.to/i/6krff9",
        "https://imx.to/i/6krfgd",
    ),

    "comments"  : int,
    "count"     : 62,
    "date"      : "dt:2026-01-07 00:00:00",
    "gallery_id": 188185,
    "num"       : range(1, 3),
    "section"   : "softcore-photo-sets",
    "slug"      : "nucosplay-sunako-k-breathtaking-sunako-k-is-an-extra-slutty-night-elf-62-images-set",
    "tags"      : ["NuCosplay", "Sunako K"],
    "title"     : "NuCosplay Sunako K - Breathtaking Sunako K Is An Extra Slutty Night Elf 62 images set",
    "uploader"  : "AdultPhotoSets",
    "views"     : int,
},

{
    "#url"     : "https://adultphotosets.best/hardcore-photo-sets/147049-nucosplay-eva-barbie-ginger-hero-eva-barbie-versus-big-veiny-cock-153-images-set.html",
    "#comment" : "VIPR image hosts",
    "#category": ("", "adultphotosets", "gallery"),
    "#class"   : adultphotosets.AdultphotosetsGalleryExtractor,
    "#range"   : "1-3",
    "#results" : (
        "https://vipr.im/u0porhe5poi5",
        "https://vipr.im/ix6ih61h2zya",
        "https://vipr.im/wunb9qepjhci",
    ),

    "count"     : 153,
    "date"      : "dt:2025-01-25 00:00:00",
    "gallery_id": 147049,
    "num"       : range(1, 3),
    "section"   : "hardcore-photo-sets",
    "tags"      : ["NuCosplay", "Eva Barbie"],
    "uploader"  : "AdultPhotoSets",
},

{
    "#url"     : "https://adultphotosets.best/hardcore-photo-sets/57264-bbcpie-scarlett-skies-bbc-rebound-50x-1500px-27-aug-2022.html",
    "#comment" : "ImageTwist image hosts",
    "#category": ("", "adultphotosets", "gallery"),
    "#class"   : adultphotosets.AdultphotosetsGalleryExtractor,
    "#range"   : "1-3",
    "#results" : (
        "https://imagetwist.com/m29xu70gd8cd/3dt7mr.jpg",
        "https://imagetwist.com/hnls31np33lx/3dt7mt.jpg",
        "https://imagetwist.com/9mr59j6jnsb7/3dt7mu.jpg",
    ),

    "count"     : 50,
    "date"      : "dt:2022-08-27 00:00:00",
    "gallery_id": 57264,
    "num"       : range(1, 3),
    "section"   : "hardcore-photo-sets",
    "tags"      : ["BBCPie", "Scarlett Skies"],
    "uploader"  : "AdultPhotoSets",
},

{
    "#url"     : "https://adultphotosets.best/13-teamskeet-charlie-red-the-hitchhiker-09112020-216x.html",
    "#comment" : "legacy root-level gallery",
    "#category": ("", "adultphotosets", "gallery"),
    "#class"   : adultphotosets.AdultphotosetsGalleryExtractor,
    "#range"   : "1-3",
    "#pattern" : r"https://imx\.to/i/\w+",
    "#count"   : 3,

    "count"     : 216,
    "gallery_id": 13,
    "num"       : range(1, 3),
    "section"   : "",
},

{
    "#url"     : "https://adultphotosets.best/tags/NuCosplay/",
    "#category": ("", "adultphotosets", "tag"),
    "#class"   : adultphotosets.AdultphotosetsTagExtractor,
    "#pattern" : adultphotosets.AdultphotosetsGalleryExtractor.pattern,
    "#range"   : "1-20",
    "#count"   : 20,
},

{
    "#url"     : "https://adultphotosets.best/softcore-photo-sets/",
    "#category": ("", "adultphotosets", "category"),
    "#class"   : adultphotosets.AdultphotosetsCategoryExtractor,
    "#pattern" : adultphotosets.AdultphotosetsGalleryExtractor.pattern,
    "#range"   : "1-10",
    "#count"   : 10,
},

{
    "#url"     : "https://adultphotosets.best/",
    "#category": ("", "adultphotosets", "home"),
    "#class"   : adultphotosets.AdultphotosetsHomeExtractor,
    "#pattern" : adultphotosets.AdultphotosetsGalleryExtractor.pattern,
    "#range"   : "1-10",
    "#count"   : 10,
},

)
