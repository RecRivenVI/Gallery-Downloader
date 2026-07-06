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
    "count"      : 2,
    "num"        : range(1, 2),
    "date"       : "type:datetime",
    "description": str,
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
    "filename"   : "OiX1obv1Krd1OyNxSO426642zxEaeiurOq258kM2Ph8BMzBa3lig8md4VSWS",
    "id"         : "2682502",
    "page_url"   : "https://artfight.net/attack/2682502.first-attack",
    "title"      : "First attack!",
    "type"       : "attack",
    "from"       : "miss_samychan",
    "to"         : "Halo-Cat",
    "team"       : "Wither",
},

{
    "#url"     : "https://artfight.net/character/6115296.enmity",
    "#class"   : artfight.ArtfightPostExtractor,
    "#auth"    : True,
    "#results" : "https://images.artfight.net/character/Awe14ZLbMHQOvJwhfdEh5BCNYSrbjk4rLNvF0giQbpF2X3hJtAOXWjNzDCcP.png?t=1782352571",

    "artist"     : "Speidurr",
    "date"       : "dt:2025-06-02 00:45:02",
    "description": str,
    "extension"  : "png",
    "filename"   : "Awe14ZLbMHQOvJwhfdEh5BCNYSrbjk4rLNvF0giQbpF2X3hJtAOXWjNzDCcP",
    "id"         : "6115296",
    "page_url"   : "https://artfight.net/character/6115296.enmity",
    "title"      : "Enmity",
    "type"       : "character",
    "username"   : "",
},

{
    "#url"     : "https://artfight.net/character/5905928.halley",
    "#class"   : artfight.ArtfightPostExtractor,
    "#auth"    : True,
    "#results" : (
        "https://images.artfight.net/character/iToglUEYrnGJMPPq3EBjbCEMmKbMRRST8z3MWmKX9g4ivRCQPo7LxpJQpvQp.png?t=1777692659",
        "https://images.artfight.net/character/STpsFbPXKTfEvy76UlHm3tZg3L4QPANpp7fNfdYJK6JetGkzWXohqz0Er4wS.png?t=1777692659",
        "https://images.artfight.net/character/3B3gEk0prQpIowfOsKamX84HQElminjwAkTTxP1I7YFx4negB7Rokhm1bJ5M.png?t=1777692659",
        "https://images.artfight.net/character/I3jl4smOf9GPVvkFQp4cnLcxj1Lv701bEbR3Jg1pgQfgol3aLVckaJPEW9No.png?t=1777692659",
        "https://images.artfight.net/character/wKhlNfiIzoMraKs35mLQlffWQE4mKHT9vsy2HVQ2nRlK8tkXguZswPeCBXKc.png?t=1777692659",
        "https://images.artfight.net/character/xQDW9cO1hYi2nEgjehuPeAv16RDgaejTaBRGvmMM2r0fvuZLJAbeXF00Krxi.png?t=1779106433",
    ),

    "artist"     : "magikind",
    "count"      : 6,
    "num"        : range(1, 6),
    "date"       : "dt:2025-05-11 11:49:26",
    "extension"  : "png",
    "id"         : "5905928",
    "page_url"   : "https://artfight.net/character/5905928.halley",
    "title"      : "[★] Halley",
    "type"       : "character",
    "tags"       : [
        "alien",
        "star",
        "space",
        "modern",
        "galaxy",
    ],
},

)
