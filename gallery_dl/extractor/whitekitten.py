# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://whitekitten.art/"""

from .booru import BooruExtractor
from .common import Message
from .. import text, dt


class WhitekittenExtractor(BooruExtractor):
    """Base class for whitekitten extractors"""
    category = "whitekitten"
    root = "https://whitekitten.art"
    per_page = 100
    filename_fmt = "{category}_{id}_{file[fileOrder]}.{extension}"
    archive_fmt = "{id}_{file[fileOrder]}"

    def _init(self):
        self.max_rating = self.config("max-rating", "explicit")

    def items(self):
        data = self.metadata()
        for post in self.posts():
            self._prepare_post(post)
            files = post.get("files") or ()
            post["count"] = len(files)
            post.update(data)

            yield Message.Directory, "", post
            for num, file in enumerate(files, 1):
                self._prepare_file(file)
                url = file["mediaUrl"]

                file_meta = dict(post)
                file_meta["num"] = num
                file_meta["file"] = file
                for key in ("width", "height", "mimeType", "fileSize",
                            "fileOrder", "tags", "tags_artist",
                            "tags_character", "tags_copyright",
                            "tags_species", "tags_uncategorized"):
                    if key in file:
                        file_meta[key] = file[key]

                if pngurl := file.get("pngUrl"):
                    file_meta["_fallback"] = iter((pngurl,))

                text.nameext_from_url(url, file_meta)
                yield Message.Url, url, file_meta

    def _pagination(self, params):
        url = self.root + "/api/posts"
        params["maxRating"] = self.max_rating
        params.setdefault("filterMode", "hidden")
        while True:
            data = self.request_json(url, params=params)["data"]
            yield from (data.get("posts") or ())
            cursor = data.get("cursor")
            if not cursor:
                return
            params["cursor"] = cursor

    def _prepare_post(self, post):
        # post-list endpoint returns summary rows without 'files'/'tags';
        # fetch detail to fill those in
        if "files" not in post:
            detail = self.request_json(
                f"{self.root}/api/posts/{post['id']}",
                params={"maxRating": self.max_rating},
            )["data"]["post"]
            post.update(detail)

        if post.get("createdAt"):
            post["date"] = dt.parse_iso(post["createdAt"])
        if post.get("updatedAt"):
            post["date_updated"] = dt.parse_iso(post["updatedAt"])

        self._split_tags(post, post.get("tags") or ())

    def _prepare_file(self, file):
        tags = list(file.get("tags") or ())
        for extra in ("inheritedTags", "impliedTags"):
            if file.get(extra):
                tags.extend(file[extra])
        seen = set()
        unique = []
        for tag in tags:
            tid = tag.get("id")
            if tid not in seen:
                seen.add(tid)
                unique.append(tag)
        self._split_tags(file, unique)

    @staticmethod
    def _split_tags(obj, tags):
        grouped = {}
        names = []
        for tag in tags:
            name = tag.get("name") or ""
            bare = name.partition(":")[2] or name
            grouped.setdefault(
                tag.get("category") or "uncategorized", []).append(bare)
            names.append(bare)
        for cat, tlist in grouped.items():
            obj["tags_" + cat] = tlist
        obj["tags"] = sorted(names)


BASE_PATTERN = WhitekittenExtractor.update({
    "whitekitten": {
        "root": "https://whitekitten.art",
        "pattern": r"whitekitten\.art",
    },
})


class WhitekittenTagExtractor(WhitekittenExtractor):
    """Extractor for whitekitten tag searches"""
    subcategory = "tag"
    directory_fmt = ("{category}", "{search_tags}")
    pattern = BASE_PATTERN + r"/?(?:\?([^#]*))?$"
    example = "https://whitekitten.art/?q=TAG"

    def metadata(self):
        return {"search_tags": self._query().get("q", "")}

    def posts(self):
        q = self._query().get("q")
        return self._pagination({"q": q} if q else {})

    def _query(self):
        return text.parse_query(self.groups[-1] or "")


class WhitekittenPostExtractor(WhitekittenExtractor):
    """Extractor for a single whitekitten post"""
    subcategory = "post"
    pattern = BASE_PATTERN + r"/posts/(\d+)"
    example = "https://whitekitten.art/posts/12345"

    def posts(self):
        url = f"{self.root}/api/posts/{self.groups[-1]}"
        params = {"maxRating": self.max_rating}
        return (self.request_json(url, params=params)["data"]["post"],)
