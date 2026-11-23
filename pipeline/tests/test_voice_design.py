"""Offline tests for the Voice Design / dictionary additions of elevenlabs_client (no network)."""
import base64
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from pipeline import elevenlabs_client as el


class FakeResp:
    def __init__(self, payload=None, content=b"ID3"):
        self._p = payload or {}
        self.content = content
        self.headers = {"request-id": "r1"}

    def json(self):
        return self._p


class TestDesignBody(unittest.TestCase):
    def test_limits(self):
        ok = el.design_body("x" * 30, "y" * 120, seed=5)
        self.assertEqual(ok["model_id"], "eleven_ttv_v3")
        self.assertFalse(ok["should_enhance"])
        self.assertEqual(ok["loudness"], 0.0)
        self.assertEqual(ok["seed"], 5)
        with self.assertRaises(ValueError):
            el.design_body("short", "y" * 120)
        with self.assertRaises(ValueError):
            el.design_body("x" * 30, "too short")
        with self.assertRaises(ValueError):
            el.design_body("x" * 30, "y" * 120, model_id="eleven_v3")


class TestDesignAndTts(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.env = mock.patch.dict(os.environ, {"STUDIO_ALLOW_PAID": "1"})
        self.env.start()

    def tearDown(self):
        self.env.stop()
        self.tmp.cleanup()

    def test_design_saves_previews(self):
        payload = {"previews": [{"generated_voice_id": "g1", "audio_base_64": base64.b64encode(b"abc").decode(),
                                 "duration_secs": 1.0}]}
        with mock.patch.object(el, "request", return_value=FakeResp(payload)) as req, \
                mock.patch.object(el.costs, "log"):
            res = el.design_voice("d" * 30, "t" * 120, self.tmp.name, prefix="i1", seed=7)
        self.assertEqual(res[0]["generated_voice_id"], "g1")
        self.assertEqual(Path(res[0]["file"]).read_bytes(), b"abc")
        self.assertIn("/v1/text-to-voice/design", req.call_args.args[1])
        self.assertEqual(req.call_args.kwargs["json"]["seed"], 7)

    def test_tts_voice_settings_override_and_dictionary(self):
        with mock.patch.object(el, "request", return_value=FakeResp()) as req, mock.patch.object(el.costs, "log"):
            el.tts("Hello there", "vid", Path(self.tmp.name) / "a.mp3", model_id="eleven_v3",
                   voice_settings={"stability": 0.5}, pronunciation_dictionaries=[("d1", "v1"), ("d2", None)])
        body = req.call_args.kwargs["json"]
        self.assertEqual(body["voice_settings"], {"stability": 0.5})
        self.assertEqual(body["pronunciation_dictionary_locators"],
                         [{"pronunciation_dictionary_id": "d1", "version_id": "v1"},
                          {"pronunciation_dictionary_id": "d2"}])

    def test_half_price_v4_turbo(self):
        self.assertEqual(el.tts_credits("abcd", "eleven_v4_turbo"), 2.0)
        self.assertEqual(el.tts_credits("abcd", "eleven_v3"), 4.0)


if __name__ == "__main__":
    unittest.main()
