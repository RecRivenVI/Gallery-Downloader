# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import imagehosts


__tests__ = (
{
    "#url"     : "https://pixhost.cc/show/190/130327671_test-.png",
    "#category": ("imagehost", "pixhost", "image"),
    "#class"   : imagehosts.PixhostImageExtractor,
    "#results"      : "https://img37.pixhost.cc/images/190/130327671_test-.png",
    "#sha1_content" : "0c8768055e4e20e7c7259608b67799171b691140",

    "filename" : "test-",
    "extension": "png",
    "directory": "190",
    "token"    : "130327671",
    "post_url" : "https://pixhost.cc/show/190/130327671_test-.png",
},

{
    "#url"     : "https://pixhost.to/show/190/130327671_test-.png",
    "#category": ("imagehost", "pixhost", "image"),
    "#class"   : imagehosts.PixhostImageExtractor,
    "#results"      : "https://img37.pixhost.cc/images/190/130327671_test-.png",
    "#sha1_content" : "0c8768055e4e20e7c7259608b67799171b691140",

    "filename" : "test-",
    "extension": "png",
    "directory": "190",
    "token"    : "130327671",
    "post_url" : "https://pixhost.cc/show/190/130327671_test-.png",
},

{
    "#url"     : "https://pixhost.org/show/190/130327671_test-.png",
    "#category": ("imagehost", "pixhost", "image"),
    "#class"   : imagehosts.PixhostImageExtractor,
},

{
    "#url"     : "https://pixhost.cc/gallery/jSMFq",
    "#category": ("imagehost", "pixhost", "gallery"),
    "#class"   : imagehosts.PixhostGalleryExtractor,
    "#pattern" : imagehosts.PixhostImageExtractor.pattern,
    "#count"   : 3,
},

{
    "#url"     : "https://pixhost.to/gallery/jSMFq",
    "#category": ("imagehost", "pixhost", "gallery"),
    "#class"   : imagehosts.PixhostGalleryExtractor,
},

{
    "#url"     : "https://pixhost.org/gallery/jSMFq",
    "#category": ("imagehost", "pixhost", "gallery"),
    "#class"   : imagehosts.PixhostGalleryExtractor,
},

)
