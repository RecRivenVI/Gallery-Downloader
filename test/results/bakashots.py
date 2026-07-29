# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import bakashots


__tests__ = (
{
    "#url"     : "https://compare.bakashots.me/compare.php?setId=6275",
    "#class"   : bakashots.BakashotsComparisonExtractor,
    "#results" : (
        "https://compare.bakashots.me/eqCeOxHtilLxTYF4LS",
        "https://compare.bakashots.me/eqCfOxHtilUwiRZtpc=",
    ),

    "comparison_id": 41330,
    "count"        : 2,
    "date"         : "dt:2026-07-03 13:47:20",
    "extension"    : "png",
    "group_name"   : {"DBNL", "Blu-Flash"},
    "width"        : {640, 768},
    "height"       : {480, 576},
    "num"          : range(1, 2),
    "set_id"       : 6275,
    "title"        : "Comparing Dragon Ball Z - Side Story - The Plan To Eradicate The Saiyan",
    "url"          : str,
},

{
    "#url"     : "https://compare.bakashots.me/search.php?searchTherms=high",
    "#class"   : bakashots.BakashotsSearchExtractor,
    "#pattern" : bakashots.BakashotsComparisonExtractor.pattern,
    "#count"   : 12,
},

{
    "#url"     : "https://compare.bakashots.me/search.php?searchTherms=Z&page=2",
    "#class"   : bakashots.BakashotsSearchExtractor,
    "#pattern" : bakashots.BakashotsComparisonExtractor.pattern,
    "#count"   : 30,
},

)
