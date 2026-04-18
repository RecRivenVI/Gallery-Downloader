#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

import os
import sys
import unittest
from unittest.mock import Mock, patch
from http.cookiejar import Cookie

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gallery_dl.extractor.curl_cffi_shim import (  # noqa: E402
    CurlCffiSessionWrapper,
    CurlCffiResponseWrapper,
    CookieJarWrapper,
    _DaemonThreadPoolExecutor,
    _RawProxy,
    _detach_session_threads,
    _wrap_request,
)

import curl_cffi.requests  # noqa: E402
import curl_cffi.requests.exceptions as cexc  # noqa: E402
import requests.exceptions  # noqa: E402


class TestExceptionMapping(unittest.TestCase):

    def test_exception_mapping(self):
        cases = (
            (cexc.ConnectionError,
             requests.exceptions.ConnectionError),
            (cexc.Timeout,
             requests.exceptions.Timeout),
            (cexc.ChunkedEncodingError,
             requests.exceptions.ChunkedEncodingError),
            (cexc.ContentDecodingError,
             requests.exceptions.ContentDecodingError),
            (cexc.RequestException,
             requests.exceptions.RequestException),
        )
        for cffi_exc, requests_exc in cases:
            def raise_it(e=cffi_exc):
                raise e("x")
            with self.assertRaises(requests_exc):
                _wrap_request(raise_it)

    def test_unrelated_exceptions_pass_through(self):
        def raise_val():
            raise ValueError("not curl_cffi")
        with self.assertRaises(ValueError):
            _wrap_request(raise_val)

        def raise_conn():
            raise cexc.ConnectionError("conn")
        try:
            _wrap_request(raise_conn)
        except requests.exceptions.ConnectionError as exc:
            self.assertIsInstance(
                exc.__cause__, cexc.ConnectionError)


class TestCurlCffiResponseWrapper(unittest.TestCase):

    def _make_response(self, **overrides):
        resp = Mock()
        resp.status_code = overrides.get("status_code", 200)
        resp.headers = overrides.get(
            "headers", {"content-type": "text/html"})
        resp.url = overrides.get(
            "url", "https://example.com/page")
        resp.reason = overrides.get("reason", "")
        resp.text = overrides.get("text", "hello")
        resp.content = overrides.get("content", b"hello")
        resp.encoding = overrides.get("encoding", "utf-8")
        resp.history = overrides.get("history", [])
        resp.json.return_value = overrides.get(
            "json_data", {"key": "val"})
        resp.close = Mock()
        resp.iter_content = Mock(
            return_value=iter([b"abc", b"def"]))
        return resp

    def test_passthrough(self):
        resp = self._make_response(
            status_code=404, text="nf", content=b"nf")
        w = CurlCffiResponseWrapper(resp)
        self.assertEqual(w.status_code, 404)
        self.assertEqual(w.text, "nf")
        self.assertEqual(w.content, b"nf")
        self.assertEqual(w.url, "https://example.com/page")
        self.assertEqual(w.json(), {"key": "val"})
        self.assertEqual(w.encoding, "utf-8")
        self.assertEqual(w.history, [])
        self.assertEqual(
            list(w.iter_content(chunk_size=3)), [b"abc", b"def"])
        w.close()
        resp.close.assert_called_once()

    def test_reason(self):
        # empty reason falls back to HTTP status phrases
        w = CurlCffiResponseWrapper(self._make_response(
            status_code=403, reason=""))
        self.assertEqual(w.reason, "Forbidden")

        # non-empty reason passes through unchanged
        w = CurlCffiResponseWrapper(self._make_response(
            reason="Custom"))
        self.assertEqual(w.reason, "Custom")

    def test_raw_chunked(self):
        for headers, expected in (
            ({"transfer-encoding": "chunked"}, True),
            ({"content-length": "1234"}, False),
            ({}, False),
        ):
            resp = Mock()
            resp.headers = headers
            self.assertEqual(_RawProxy(resp).chunked, expected)


class TestCookieJarWrapper(unittest.TestCase):

    def test_truthiness_and_len(self):
        cookies = curl_cffi.requests.Cookies()
        w = CookieJarWrapper(cookies)
        self.assertFalse(w)
        self.assertEqual(len(w), 0)

        cookies.set("a", "1", domain="example.com")
        cookies.set("b", "2", domain="example.com")
        self.assertTrue(w)
        self.assertEqual(len(w), 2)

    def test_iteration_yields_cookie_objects(self):
        cookies = curl_cffi.requests.Cookies()
        cookies.set("sess", "abc", domain=".example.com")
        items = list(CookieJarWrapper(cookies))
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].name, "sess")
        self.assertEqual(items[0].domain, ".example.com")
        self.assertTrue(hasattr(items[0], "expires"))

    def test_mutation(self):
        cookies = curl_cffi.requests.Cookies()
        w = CookieJarWrapper(cookies)

        cookie = Cookie(
            0, "by_object", "val", None, False,
            ".example.com", False, True,
            "/", False, False, None, False, None, None, {},
        )
        w.set_cookie(cookie)
        w.set("by_name", "val2", domain="example.com")

        self.assertEqual(cookies.get("by_object"), "val")
        self.assertEqual(cookies.get("by_name"), "val2")


class TestCurlCffiSessionWrapper(unittest.TestCase):

    def test_none_headers_stripped(self):
        session = Mock(spec=curl_cffi.requests.Session)
        session.headers = {}
        session.cookies = curl_cffi.requests.Cookies()
        resp = Mock()
        resp.status_code = 200
        resp.headers = {}
        resp.url = "https://example.com"
        resp.reason = "OK"
        resp.history = []
        session.request.return_value = resp

        wrapper = CurlCffiSessionWrapper(session=session)
        wrapper.request(
            "GET", "https://example.com",
            headers={
                "Accept": "application/json",
                "Cookie": None,
                "Origin": "https://example.com",
            },
        )
        sent = session.request.call_args.kwargs["headers"]
        self.assertEqual(sent["Accept"], "application/json")
        self.assertEqual(sent["Origin"], "https://example.com")
        self.assertNotIn("Cookie", sent)

    def test_request_translates_session_exceptions(self):
        session = Mock(spec=curl_cffi.requests.Session)
        session.headers = {}
        session.cookies = curl_cffi.requests.Cookies()
        session.request.side_effect = cexc.ConnectionError("x")

        wrapper = CurlCffiSessionWrapper(session=session)
        with self.assertRaises(
                requests.exceptions.ConnectionError):
            wrapper.request("GET", "https://example.com")

    def test_import_error_without_curl_cffi(self):
        with patch(
            "gallery_dl.extractor.curl_cffi_shim.curl_cffi",
            None,
        ):
            with self.assertRaises(ImportError) as cm:
                CurlCffiSessionWrapper()
            self.assertIn("curl_cffi", str(cm.exception))

    def test_executor_is_daemon_variant(self):
        wrapper = CurlCffiSessionWrapper(impersonate="firefox")
        try:
            self.assertIsInstance(
                wrapper._session._executor,
                _DaemonThreadPoolExecutor,
            )
        finally:
            wrapper.close()

    def test_daemon_executor_spawns_daemon_threads(self):
        executor = _DaemonThreadPoolExecutor(max_workers=1)
        try:
            executor.submit(lambda: 42).result(timeout=5)
            threads = list(executor._threads)
            self.assertEqual(len(threads), 1)
            self.assertTrue(threads[0].daemon)
        finally:
            executor.shutdown(wait=False)

    def test_detach_session_threads_clears_queue(self):
        import concurrent.futures.thread as tp
        wrapper = CurlCffiSessionWrapper(impersonate="firefox")
        try:
            wrapper._session._executor.submit(
                lambda: 42).result(timeout=5)
            workers = list(wrapper._session._executor._threads)
            self.assertTrue(
                any(t in tp._threads_queues for t in workers))

            _detach_session_threads(wrapper._session)
            self.assertFalse(
                any(t in tp._threads_queues for t in workers))
        finally:
            wrapper.close()


if __name__ == "__main__":
    unittest.main()
