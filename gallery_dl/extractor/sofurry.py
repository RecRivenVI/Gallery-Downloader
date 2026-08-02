# -*- coding: utf-8 -*-

# Copyright 2026 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://sofurry.com/"""

from .common import Extractor, Message

BASE_PATTERN = r"(?:https?://)?(?:www\.)?sofurry\.com"


class SofurryExtractor(Extractor):
    """Base class for sofurry extractors"""
    category = "sofurry"
    root = "https://sofurry.com"

    def _unpack(self, pack):
        def _resolve(item):
            if isinstance(item, dict):
                return {
                    pack[int(key[1:])]: (_resolve(pack[value])
                                         if value > 0 else None)
                    for key, value in item.items()
                }
            if isinstance(item, list):
                return [
                    _resolve(pack[value]) if value > 0 else None
                    for value in item
                ]
            return item

        return _resolve(pack[0])


class SofurrySubmissionExtractor(SofurryExtractor):
    subcategory = "submission"
    directory_fmt = ("{category}", "{author[username]}")
    filename_fmt = "{date:%Y-%m-%d} {id}{title:? //}{num:? //:>02}.{extension}"
    archive_fmt = "{filename}"
    pattern = BASE_PATTERN + r"/s/([^/?#]+)"
    example = "https://sofurry.com/s/ID"

    def items(self):
        submission_id = self.groups[0]
        url = f"{self.root}/s/{submission_id}.data"
        data = self._unpack(self.request_json(url))
        submission = data["routes/submission.$id"]["data"]["submission"]

        files = submission["content"]
        submission["count"] = len(files)
        submission["date"] = self.parse_datetime_iso(submission["publishedAt"])

        yield Message.Directory, "", submission
        if self.config("original", True):
            url = f"{self.root}/api/submission-download/{submission_id}"
            submission["filename"] = submission["title"]
            submission["extension"] = \
                files[0]["extension"] if len(files) == 1 else "zip"
            yield Message.Url, url, submission
        else:
            files.sort(key=lambda f: f.get("position", 0))
            for submission["num"], file in enumerate(files, 1):
                url = file["displayUrl"]
                submission["file_id"] = file["id"]
                submission["file_title"] = file["title"]
                submission["file_description"] = file["description"]
                submission["extension"] = file["extension"]
                submission["meta"] = file["meta"]
                submission["filename"] = url[url.rfind("/")+1:]
                yield Message.Url, url, submission


class SofurryGalleryExtractor(SofurryExtractor):
    subcategory = "gallery"
    pattern = BASE_PATTERN + r"/u/([^/?#]+)/gallery"
    example = "https://sofurry.com/u/USER/gallery"

    def items(self):
        url = self.root + "/api/profile"
        params = {
            "handle": "zummeng",
            "tab": "gallery",
            "page": 0,
            "per_page": "24",
        }
        base = self.root + "/s/"
        while True:
            subs = self.request_json(url, params=params)["submissions"]

            for submission in subs["data"]:
                submission["_extractor"] = SofurrySubmissionExtractor
                yield Message.Queue, base + submission["id"], submission

            if not subs.get("hasNextPage"):
                break
            params["page"] += 1
