#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

import os
import sys
import unittest
import importlib.util
from unittest.mock import Mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gallery_dl import extractor, config  # noqa: E402

HAS_CURL_CFFI = importlib.util.find_spec("curl_cffi") is not None


@unittest.skipUnless(HAS_CURL_CFFI, "curl_cffi not installed")
class TestFanboxSessions(unittest.TestCase):

    def setUp(self):
        config.clear()
        config.set((), "cookies", {"FANBOXSESSID": "s", "cf_clearance": "c"})

    tearDown = setUp

    def _init(self):
        ext = extractor.find("https://test.fanbox.cc/posts/1")
        ext.initialize()
        return ext

    def test_split_sessions(self):
        ext = self._init()
        # downloads use the requests session, API uses curl_cffi
        self.assertEqual(type(ext.session).__name__, "Session")
        self.assertEqual(
            type(ext.api_session).__name__, "CurlCffiSessionWrapper")
        # both jars carry the auth + CloudFlare cookies
        names = {cookie.name for cookie in ext.api_session.cookies}
        self.assertIn("FANBOXSESSID", names)
        self.assertIn("cf_clearance", names)

    def test_request_uses_api_session(self):
        ext = self._init()
        ext.api_session.request = Mock(return_value=Mock(status_code=200))
        ext.session.request = Mock(return_value=Mock(status_code=200))

        ext.request("https://api.fanbox.cc/post.info", fatal=False)

        ext.api_session.request.assert_called_once()
        ext.session.request.assert_not_called()


if __name__ == "__main__":
    unittest.main()
