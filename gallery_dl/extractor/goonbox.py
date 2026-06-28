# -*- coding: utf-8 -*-

# Copyright 2026 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://goonbox.cr/"""

from .common import Extractor, Message
from .. import text

BASE_PATTERN = r"(?:https?://)?(?:www\.)?goonbox\.cr"


class GoonboxExtractor(Extractor):
    """Base class for goonbox extractors"""
    category = "goonbox"
    root = "https://goonbox.cr"
    directory_fmt = ("{category}",
                     "{album[title]|''}{album[encoded_id]:? (/)/}")
    filename_fmt = "{filename} ({encoded_id}).{extension}"
    archive_fmt = "{encoded_id}"

    def items(self):
        for img in self.images():
            try:
                url = img["original_url"]
            except Exception:
                continue

            img["date"] = self.parse_datetime_iso(
                img.get("created_at"))
            img["date_updated"] = self.parse_datetime_iso(
                img.get("updated_at"))

            if name := img.get("original_filename"):
                text.nameext_from_name(name, img)
                if not img["extension"]:
                    img["extension"] = text.ext_from_url(url)
            else:
                text.nameext_from_url(url, img)

            yield Message.Directory, "", img
            yield Message.Url, url, img


class GoonboxImageExtractor(GoonboxExtractor):
    subcategory = "image"
    pattern = BASE_PATTERN + r"/img/([^/?#]+)"
    example = "https://goonbox.cr/img/ID"

    def images(self):
        url = f"{self.root}/api/images/{self.groups[0]}"
        return (self.request_json(url)["image"],)


class GoonboxAlbumExtractor(GoonboxExtractor):
    subcategory = "album"
    pattern = BASE_PATTERN + r"/a/([^/?#]+)"
    example = "https://goonbox.cr/a/ID"

    def images(self):
        url = f"{self.root}/api/albums/{self.groups[0]}"
        params = {"page": 1}

        while True:
            data = self.request_json(url, params=params)

            if "album" in data:
                self.kwdict["album"] = data["album"]
            yield from data["images"]

            try:
                pgn = data["pagination"]
                if pgn["current_page"] == pgn["last_page"]:
                    break
            except Exception:
                break
            params["page"] += 1
