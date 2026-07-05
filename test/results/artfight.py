# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import artfight


__tests__ = (
{
    "#url"     : "https://artfight.net/~%EB%B0%94%EB%B3%B4",
    "#class"   : artfight.ArtfightUserExtractor,
    "#results" : (
        "https://artfight.net/~%EB%B0%94%EB%B3%B4/characters",
        "https://artfight.net/~%EB%B0%94%EB%B3%B4/attacks",
        "https://artfight.net/~%EB%B0%94%EB%B3%B4/defenses",
    ),
},

{
    "#url"     : "https://artfight.net/~%EB%B0%94%EB%B3%B4/attacks",
    "#class"   : artfight.ArtfightAttacksExtractor,
    "#auth"    : True,
    "#pattern" : r"https://images\.artfight\.net/attack/\w+\.(jpg|png)\?t=\d+",
    "#range"   : "1-10",
    "#count"   : 10,

    "artist"     : "바보",
    "date"       : "type:datetime",
    "description": str,
    "extension"  : {"jpg", "png"},
    "file"       : r"re:https://images.artfight.net/attack/\w+",
    "filename"   : r"re:\w+",
    "id"         : r"re:^\d+$",
    "page_url"   : r"re:https://artfight.net/attack/\d+\.\w+",
    "title"      : str,
    "type"       : "attack",
    "username"   : "바보",
},

{
    "#url"     : "https://artfight.net/~%EB%B0%94%EB%B3%B4/defenses",
    "#class"   : artfight.ArtfightDefensesExtractor,
    "#auth"    : True,
    "#pattern" : r"https://images\.artfight\.net/attack/\w+\.(jpg|png)\?t=\d+",
    "#range"   : "1-5",
    "#count"   : 5,

    "date"     : "type:datetime",
    "type"     : "attack",
    "username" : "바보",
},

{
    "#url"     : "https://artfight.net/~%EB%B0%94%EB%B3%B4/characters",
    "#class"   : artfight.ArtfightCharactersExtractor,
    "#auth"    : True,
    "#pattern" : r"https://images\.artfight\.net/character/\w+\.(jpg|png)\?t=\d+",
    "#range"   : "1-5",

    "artist"     : "바보",
    "date"       : "type:datetime",
    "description": "",
    "extension"  : {"jpg", "png"},
    "id"         : r"re:^\d+$",
    "page_url"   : r"re:https://artfight.net/character/\d+\.\w+",
    "title"      : str,
    "type"       : "character",
    "username"   : "바보",
},

{
    "#url"     : "https://artfight.net/attack/2682502.first-attack",
    "#class"   : artfight.ArtfightPostExtractor,
    "#auth"    : True,
    "#results" : "https://images.artfight.net/attack/OiX1obv1Krd1OyNxSO426642zxEaeiurOq258kM2Ph8BMzBa3lig8md4VSWS.jpeg?t=1656727443",

    "artist"     : "miss_samychan",
    "date"       : "dt:2022-07-01 20:04:02",
    "description": "",
    "extension"  : "jpeg",
    "file"       : "https://images.artfight.net/attack/OiX1obv1Krd1OyNxSO426642zxEaeiurOq258kM2Ph8BMzBa3lig8md4VSWS.jpeg?t=1656727443",
    "filename"   : "OiX1obv1Krd1OyNxSO426642zxEaeiurOq258kM2Ph8BMzBa3lig8md4VSWS",
    "id"         : "2682502",
    "page_url"   : "https://artfight.net/attack/2682502.first-attack",
    "title"      : "First attack!",
    "type"       : "attack",
    "username"   : "",
},

{
    "#url"     : "https://artfight.net/character/6115296.enmity",
    "#class"   : artfight.ArtfightPostExtractor,
    "#auth"    : True,
    "#results" : "https://images.artfight.net/character/Awe14ZLbMHQOvJwhfdEh5BCNYSrbjk4rLNvF0giQbpF2X3hJtAOXWjNzDCcP.png?t=1782352571",

    "artist"     : "Speidurr",
    "date"       : "dt:2025-06-02 00:45:02",
    "description": "",
    "extension"  : "png",
    "file"       : "https://images.artfight.net/character/Awe14ZLbMHQOvJwhfdEh5BCNYSrbjk4rLNvF0giQbpF2X3hJtAOXWjNzDCcP.png?t=1782352571",
    "filename"   : "Awe14ZLbMHQOvJwhfdEh5BCNYSrbjk4rLNvF0giQbpF2X3hJtAOXWjNzDCcP",
    "id"         : "6115296",
    "page_url"   : "https://artfight.net/character/6115296.enmity",
    "title"      : "Enmity",
    "type"       : "character",
    "username"   : "",
},

)
