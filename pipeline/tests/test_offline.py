"""Офлайн-тесты пайплайна: без сети и без настоящих ключей (HTTP замокан).

    python3 -m unittest pipeline.tests.test_offline -v
"""
from __future__ import annotations

import datetime as dt
import json
import os
import tempfile
import unittest
import wave
from pathlib import Path
from unittest import mock

from pipeline import config, costs, elevenlabs_client, fal_client, storage

AK, SK = "AKIAIOSFODNN7EXAMPLE", "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
NOW = dt.datetime(2013, 5, 24, tzinfo=dt.timezone.utc)


class FakeResp:
    def __init__(self, status=200, js=None, content=b"", headers=None):
        self.status_code, self._js, self.content = status, js, content
        self.headers = headers or {}
        self.text = json.dumps(js) if js is not None else ""

    def json(self):
        return self._js


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.env = mock.patch.dict(os.environ, {
            "OUTPUT_DIR": self.tmp.name, "FAL_KEY": "test-fal-key-123456",
            "ELEVENLABS_API_KEY": "test-el-key-123456", "R2_ACCOUNT_ID": "acct",
            "R2_ACCESS_KEY_ID": AK, "R2_SECRET_ACCESS_KEY": SK,
            "BUDGET_LIMIT_USD": "1.00", "STUDIO_ALLOW_PAID": "1"})
        self.env.start()

    def tearDown(self):
        self.env.stop()
        self.tmp.cleanup()


class TestConfig(Base):
    def test_missing_key_message(self):
        with mock.patch.dict(os.environ, {"R2_SECRET_ACCESS_KEY": ""}):
            with self.assertRaises(config.MissingConfigError) as cm:
                config.get("R2_SECRET_ACCESS_KEY")
            self.assertIn("R2_SECRET_ACCESS_KEY", str(cm.exception))
            self.assertIn(".env.example", str(cm.exception))

    def test_require_lists_all(self):
        with mock.patch.dict(os.environ, {"R2_SECRET_ACCESS_KEY": "", "ELEVENLABS_API_KEY": ""}):
            with self.assertRaises(config.MissingConfigError) as cm:
                config.require("R2_SECRET_ACCESS_KEY", "ELEVENLABS_API_KEY")
            self.assertIn("R2_SECRET_ACCESS_KEY", str(cm.exception))
            self.assertIn("ELEVENLABS_API_KEY", str(cm.exception))

    def test_mask_hides_secret(self):
        self.assertNotIn("secretvalue", config.mask("supersecretvalue99"))

    def test_env_parser(self):
        p = Path(self.tmp.name) / ".env"
        p.write_text('# c\nA=1\nexport B="two words"\nC=x # comment\nD=\n', encoding="utf-8")
        self.assertEqual(config._parse_env_file(p), {"A": "1", "B": "two words", "C": "x", "D": ""})


class TestCosts(Base):
    def test_estimates(self):
        self.assertAlmostEqual(costs.estimate("kling-2.5-turbo-pro", 5), 0.35)
        self.assertAlmostEqual(costs.estimate("kling-3-pro", 10), 1.40)
        self.assertAlmostEqual(costs.estimate("minimax-h3-max-turbo", 6), 0.09)
        self.assertAlmostEqual(costs.estimate("nano-banana", 1), 0.04)
        self.assertAlmostEqual(costs.estimate("nano-banana-2", 2), 0.16)

    def test_budget_and_log(self):
        costs.guard("kling-3-pro", 5)  # 0.70 <= 1.00
        costs.log("kling-3-pro", 5, provider="fal")
        with self.assertRaises(costs.BudgetExceeded):
            costs.guard("kling-2.5-turbo-pro", 5)  # 0.70 + 0.35 > 1.00
        costs.log("nano-banana", 1, provider="fal", status="error: X")  # ошибки не стоят денег
        self.assertAlmostEqual(costs.total_spent(), 0.70)
        rows = costs.read_log()
        self.assertEqual(len(rows), 2)
        self.assertTrue((Path(self.tmp.name) / "costs.jsonl").is_file())

    def test_paid_disabled(self):
        with mock.patch.dict(os.environ, {"STUDIO_ALLOW_PAID": "0"}):
            with self.assertRaises(costs.PaidCallsDisabled):
                costs.guard("nano-banana", 1)


class TestFal(Base):
    def test_image_flow(self):
        calls = []

        def fake_request(method, url, **kw):
            calls.append((method, url, kw.get("headers", {}).get("Authorization")))
            if method == "POST":
                return FakeResp(js={"request_id": "rid1",
                                    "status_url": "https://queue.fal.run/fal-ai/nano-banana/requests/rid1/status",
                                    "response_url": "https://queue.fal.run/fal-ai/nano-banana/requests/rid1"})
            if url.endswith("/status"):
                return FakeResp(js={"status": "IN_PROGRESS"} if len(calls) < 3 else {"status": "COMPLETED"})
            return FakeResp(js={"images": [{"url": "https://fal.media/x.png"}]})

        def fake_download(url, dest, **kw):
            Path(dest).write_bytes(b"png")
            return Path(dest)

        out = Path(self.tmp.name) / "img.png"
        with mock.patch.object(fal_client, "request", fake_request), \
                mock.patch.object(fal_client, "download", fake_download), \
                mock.patch.object(fal_client, "POLL_INTERVAL", 0):
            fal_client.generate_image("test", out)
        self.assertEqual(calls[0][:2], ("POST", "https://queue.fal.run/fal-ai/nano-banana"))
        self.assertEqual(calls[0][2], "Key test-fal-key-123456")
        self.assertTrue(out.is_file())
        self.assertAlmostEqual(costs.total_spent(), 0.04)

    def test_video_duration_validation(self):
        with self.assertRaises(ValueError):
            fal_client.image_to_video("https://x/y.png", "p", "o.mp4", model="kling-2.5-turbo-pro", duration=7)

    def test_video_budget_blocks_before_submit(self):
        with mock.patch.dict(os.environ, {"BUDGET_LIMIT_USD": "0.10"}), \
                mock.patch.object(fal_client, "request") as req:
            with self.assertRaises(costs.BudgetExceeded):
                fal_client.image_to_video("https://x/y.png", "p", "o.mp4", duration=5)
            req.assert_not_called()

    def test_data_uri(self):
        p = Path(self.tmp.name) / "a.png"
        p.write_bytes(b"\x89PNG")
        self.assertTrue(fal_client.to_image_url(p).startswith("data:image/png;base64,"))

    def test_app_base(self):
        self.assertEqual(fal_client._app_base("fal-ai/kling-video/v2.5-turbo/pro/image-to-video"),
                         "fal-ai/kling-video")


class TestElevenLabs(Base):
    def test_tts_wav(self):
        pcm = b"\x00\x01" * 4410
        with mock.patch.object(elevenlabs_client, "request",
                               return_value=FakeResp(content=pcm, headers={"request-id": "r"})) as req:
            out = elevenlabs_client.tts("Привет", "voice123", Path(self.tmp.name) / "l.wav")
        args, kw = req.call_args
        self.assertTrue(args[1].endswith("/v1/text-to-speech/voice123"))
        self.assertEqual(kw["params"]["output_format"], "pcm_44100")
        self.assertEqual(kw["json"]["model_id"], "eleven_multilingual_v2")
        with wave.open(str(out)) as w:
            self.assertEqual((w.getframerate(), w.getnframes()), (44100, 4410))
        self.assertEqual(costs.read_log()[0]["units"], 6)

    def test_sfx_mp3(self):
        with mock.patch.object(elevenlabs_client, "request", return_value=FakeResp(content=b"ID3")):
            out = elevenlabs_client.sfx("door slam", Path(self.tmp.name) / "s.mp3", duration_seconds=2)
        self.assertEqual(out.read_bytes(), b"ID3")


class TestStorage(Base):
    def test_sigv4_aws_vector(self):
        # Пример AWS "GET Object" из документации SigV4 для S3
        h = storage.sign_v4("GET", "examplebucket.s3.amazonaws.com", "/test.txt", {},
                            {"Range": "bytes=0-9"}, storage.EMPTY_SHA256, AK, SK, NOW,
                            region="us-east-1")
        self.assertTrue(h["authorization"].endswith(
            "Signature=f0e8bdb87c964420e857bd35b5d6ed310bd44f0170aba48dd91039c6036bdb41"))

    def test_presign_aws_vector(self):
        url = storage.presign_v4("GET", "examplebucket.s3.amazonaws.com", "/test.txt", AK, SK, NOW,
                                 expires=86400, region="us-east-1")
        self.assertIn("X-Amz-Signature=aeeed9bbccd4d02ee5c0109b86d86835f995330da4c265957d157751f604d404", url)

    def test_endpoint(self):
        self.assertEqual(storage.endpoint_url("abc"), "https://abc.r2.cloudflarestorage.com")

    @unittest.skipIf(storage.HAVE_BOTO3, "проверяется встроенный клиент")
    def test_mini_list_parses_xml(self):
        xml = (b'<?xml version="1.0"?><ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">'
               b'<Contents><Key>ep01/a.mp4</Key><Size>42</Size></Contents></ListBucketResult>')
        with mock.patch("pipeline.net.request", return_value=FakeResp(content=xml)) as req:
            objs = storage.list_objects("ep01/")
        self.assertEqual(objs, [{"key": "ep01/a.mp4", "size": 42}])
        url = req.call_args[0][1]
        self.assertTrue(url.startswith("https://acct.r2.cloudflarestorage.com/anime-studio?"))
        self.assertIn("AWS4-HMAC-SHA256", req.call_args[1]["headers"]["authorization"])


if __name__ == "__main__":
    unittest.main()
