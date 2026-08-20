# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://mangayi.com/"""

from .common import ChapterExtractor, MangaExtractor
from .. import text, util

BASE_PATTERN = r"(?:https?://)?(?:www\.)?mangayi\.com"


class MangayiBase():
    """Base class for mangayi.com extractors"""
    category = "mangayi"
    root = "https://mangayi.com"


class MangayiChapterExtractor(MangayiBase, ChapterExtractor):
    """Extractor for manga-chapters from mangayi.com"""
    pattern = BASE_PATTERN + r"(\/read\/[^/?#]+(?:\/v0*(\d+))?\/chapter\/(\d+[^/?#]*)\/)"
    example = "https://mangayi.com/read/TITLE/chapter/1/"

    def __init__(self, match):
        self.part, self.volume, self.chapter = match.groups()
        self.base = f"{self.root}{self.part}"
        ChapterExtractor.__init__(self, match, self.base)

    def get_pages_count(self, page) -> int:
        """Return the count of manga pages"""
        page_template='type="application/ld+json">{"@context":"https://schema.org","@type":"MediaGallery",'
        
        gallery, pos = text.extract(page, page_template, '</script>')
        gallery = util.json_loads('{' + gallery)

        return len(gallery['associatedMedia'])

    def get_page_json(self, page) -> dict:
        """Extract basic metadata from manga page"""
        page_template='type="application/ld+json">{"@context":"https://schema.org","@type":"ComicIssue",'
        
        page, pos = text.extract(page, page_template, '</script>')
        page = util.json_loads('{' + page)

        return page


    def metadata(self, page):
        data = self.get_page_json(page)
        chapter, dot, minor = data['issueNumber'].partition('.')
        
        return {
            "manga"         :   data['isPartOf']['name'],
            "title"         :   data['name'].split(":")[-1].lstrip(' '),
            "chapter"       :   text.parse_int(chapter),
            "chapter_minor" :   dot + minor,
            "count"         :   self.get_pages_count(page),
            "lang"          :   "en",
            "language"      :   "English"
        }


    def images(self, page):
        mediaGalleryTemplate = 'type="application/ld+json">{"@context":"https://schema.org","@type":"MediaGallery",'

        page, pos = text.extract(page, mediaGalleryTemplate, '</script>')
        page = util.json_loads('{' + page)['associatedMedia']

        for image in page:
            yield text.ensure_http_scheme(image['url']), None


class MangayiMangaExtractor(MangayiBase, MangaExtractor):
    chapterclass = MangayiChapterExtractor
    pattern = BASE_PATTERN + r"(\/read\/[^/?#]+\/)"
    example = "https://mangayi.com/read/TITLE"

    def chapters(self, page):
        chaptersTemplate='type="application/ld+json">{"@context":"https://schema.org","@type":"ItemList",'
        results = []

        manga, pos = text.extract(page, '<title>', '</title>')
        manga = manga.removesuffix(' Manga - Read Free Online | Mangayi')
        manga = text.unescape(manga)

        page, pos = text.extract(page, chaptersTemplate, '</script>')
        page = util.json_loads('{' + page)

        chapters_list = page['itemListElement']

        for ch in chapters_list:
            chapter = ch['url'].split('/')[-2]
            title = ch['name'].removeprefix(manga).lstrip()

            chapter, sep, minor = chapter.partition('-')
            
            results.append(
                (
                    ch['url'], 
                    {
                        "manga": manga,
                        "chapter": text.parse_int(chapter),
                        "chapter_minor": sep + minor,
                        "title": title,
                        "date": None,
                        "lang": "en",
                        "language": "English"
                    }
                )
            )
        return results