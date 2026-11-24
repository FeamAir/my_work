"""Offline tests for run_music.py gate conditions C1-C5 (no network, no paid calls).

    python3 -m unittest studio/music/gen/test_run_music.py -v
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_music as rm  # noqa: E402

PLANS = Path(__file__).resolve().parent


class FakeResp:
    def __init__(self, content=b"ID3fake", headers=None):
        self.content = content
        self.headers = headers or {"song-id": "song123", "request-id": "req1"}


class RunnerTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = Path(self.tmp.name)
        self.costs_file = d / "costs.jsonl"
        patches = [
            mock.patch.object(rm, "OUT_DIR", d),
            mock.patch.object(rm, "LEDGER", d / "ledger.jsonl"),
            mock.patch.object(rm.costs, "log_path", lambda: self.costs_file),
            mock.patch.object(rm.costs, "_check_floor", lambda *a: None),
            mock.patch.object(rm.storage, "upload", lambda *a: "ok"),
            mock.patch.object(rm.time, "sleep", lambda s: None),
            mock.patch.object(rm, "credit_usd", lambda: 0.0003),
            mock.patch.dict("os.environ", {"STUDIO_ALLOW_PAID": "1", "BUDGET_LIMIT_USD": "1000"}),
        ]
        for p in patches:
            p.start()
            self.addCleanup(p.stop)
        self.addCleanup(self.tmp.cleanup)

    def args(self, *extra):
        return rm.parse([str(PLANS / "theme_master_plan_v1.json"), "--name", "t", "--take", "1",
                         "--seed", "1", *extra])

    def costs_rows(self):
        return [json.loads(x) for x in self.costs_file.read_text().splitlines()]

    def test_c5_real_plans_carry_bans(self):
        rm.validate(json.loads((PLANS / "theme_master_plan_v1.json").read_text()))
        rm.validate(rm.resolve(json.loads((PLANS / "op_song_plan_v1.json").read_text()), "x"))
        rm.validate(json.loads((PLANS / "ending_plan_v1.json").read_text().replace("THEME", "x")))

    def test_c5_missing_ban_refused(self):
        plan = json.loads((PLANS / "theme_master_plan_v1.json").read_text())
        plan["chunks"][3]["negative_styles"].remove("modulation")
        with self.assertRaises(AssertionError):
            rm.validate(plan)

    def test_c1_paid_switch_off_refuses_before_any_call(self):
        with mock.patch.dict("os.environ", {"STUDIO_ALLOW_PAID": "0"}), \
                mock.patch.object(rm, "request") as req, mock.patch.object(rm, "credits_used") as cu:
            with self.assertRaises(rm.costs.PaidCallsDisabled):
                rm.run(self.args())
            req.assert_not_called()
            cu.assert_not_called()

    def test_c1_budget_limit_uses_credit_estimate(self):
        with mock.patch.dict("os.environ", {"BUDGET_LIMIT_USD": "1.0"}), \
                mock.patch.object(rm, "request") as req:
            with self.assertRaises(rm.costs.BudgetExceeded):  # 1.6 min x 2500 cr x $0.0003 = $1.20
                rm.run(self.args())
            req.assert_not_called()

    def test_take_limit(self):
        rm.ledger_append({"kind": "take", "name": "t", "credits": 1})
        with self.assertRaises(rm.GateRefused):
            rm.run(self.args("--max-takes", "1"))

    def test_ok_take_measured(self):
        with mock.patch.object(rm, "request", return_value=FakeResp()), \
                mock.patch.object(rm, "credits_used", side_effect=[100, 1600]):
            self.assertEqual(rm.run(self.args()), 0)
        self.assertEqual(rm.ledger_spent(), 1500)
        self.assertAlmostEqual(self.costs_rows()[0]["usd_estimate"], 0.45)

    def test_c2_error_logged_with_cost(self):
        with mock.patch.object(rm, "request", side_effect=RuntimeError("boom")), \
                mock.patch.object(rm, "credits_used", side_effect=[100, 900]):
            self.assertEqual(rm.run(self.args()), 1)
        row = self.costs_rows()[0]
        self.assertTrue(row["status"].startswith("error"))
        self.assertAlmostEqual(row["usd_estimate"], 0.24)
        self.assertEqual(rm.ledger_spent(), 800)

    def test_c3_measure_failure_books_estimate_and_stops(self):
        with mock.patch.object(rm, "request", return_value=FakeResp()), \
                mock.patch.object(rm, "credits_used", side_effect=[100] + [RuntimeError("down")] * 5):
            self.assertEqual(rm.run(self.args()), rm.EXIT_STOP)
        self.assertEqual(rm.ledger_spent(), 4000)  # 96 s at 2500 cr/min
        self.assertGreater(self.costs_rows()[0]["usd_estimate"], 0)

    def test_c4_zero_delta_books_estimate_and_stops(self):
        with mock.patch.object(rm, "request", return_value=FakeResp()), \
                mock.patch.object(rm, "credits_used", side_effect=[100] * 6):
            self.assertEqual(rm.run(self.args()), rm.EXIT_STOP)
        self.assertEqual(rm.ledger_spent(), 4000)

    def test_c4_lagging_delta_retried(self):
        with mock.patch.object(rm, "request", return_value=FakeResp()), \
                mock.patch.object(rm, "credits_used", side_effect=[100, 100, 1300]):
            self.assertEqual(rm.run(self.args()), 0)
        self.assertEqual(rm.ledger_spent(), 1200)


if __name__ == "__main__":
    unittest.main()
