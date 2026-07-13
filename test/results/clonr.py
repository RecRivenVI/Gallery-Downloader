# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import clonr


__tests__ = (
{
    "#url"     : "https://clonr.co/RF4uV43t3QgF",
    "#class"   : clonr.ClonrFolderExtractor,
    "#pattern" : (
        r"https://clonr.co/api/download/2c753d54a3f9086eb40fb8daf4e2e49.+",
        r"https://clonr.co/api/download/2c753d54a3f9086eb40fb8daf4e2e49.+",
    ),

    "audio_codec"    : {"opus", None},
    "bitrate"        : {int, None},
    "cache_id"       : "2c753d54a3f9086eb40fb8daf4e2e49e",
    "cache_state"    : "completed",
    "codec"          : {"av1", None},
    "color"          : {"HD (1-1-1)", None},
    "completed_files": 2,
    "completed_size" : 51690088,
    "count"          : 2,
    "duration_s"     : {float, None},
    "extension"      : {"m4a", "webm"},
    "failed_files"   : 0,
    "failed_size"    : 0,
    "filename"       : str,
    "fps"            : {int, None},
    "height"         : {int, None},
    "id"             : "RF4uV43t3QgF",
    "modified_at"    : int,
    "name"           : str,
    "num"            : range(1, 2),
    "paid_files"     : 0,
    "paid_size"      : 0,
    "poster"         : {str, None},
    "preview"        : {str, None},
    "size"           : int,
    "source_url"     : "https://mega.nz/folder/lIwhTLwb#Lj5UeZT-hPsQkz-UdjmAwA",
    "state"          : "done",
    "total_files"    : 2,
    "total_size"     : 51690088,
    "url"            : str,
    "width"          : {int, None},
    "zip_url"        : r"re:https://clonr.co/api/zip/2c753d54a3f9086eb40fb8daf4e2e49e/dua-lipa.zip\?s=.+",
},

)
