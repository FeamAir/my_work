#!/usr/bin/env python3
"""Offline test ($0, no network): with env BUDGET_LIMIT_USD=120 the OP runner still refuses a paid call once the
step cap would be exceeded. Run: python3 -I studio/direction/opening/tools/test_op_saga_limit.py"""
import importlib.util
import json
import os
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = "/home/user/my_work"
sys.path.insert(0, ROOT)


def load_runner():
    spec = importlib.util.spec_from_file_location("op_saga_run", HERE / "op_saga_run.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    os.environ["BUDGET_LIMIT_USD"] = "120"      # the investor's env value (in this test process only)
    os.environ["STUDIO_ALLOW_PAID"] = "1"
    run = load_runner()
    from pipeline import costs, fal_client
    tmp = Path(tempfile.mkdtemp())
    log = tmp / "costs.jsonl"
    costs.log_path = lambda: log                 # fake journal, never the real one
    costs.BALANCES_PATH = tmp / "none.json"      # floor rule off for the test

    def spend(total):
        log.write_text(json.dumps({"usd_estimate": total, "provider": "fal"}) + "\n")

    fails = []

    def check(ok, msg):
        print(("ok   " if ok else "FAIL ") + msg)
        if not ok:
            fails.append(msg)

    # 1. env 120 is not refused; the step cap wins
    lim, src = run.step_limit("L", with_source=True)
    check(abs(lim - 66.03) < 1e-9 and "step L cap" in src and "120" in src, f"L effective limit {lim} [{src}]")
    for s, want in (("R", 67.35), ("N", 69.39), ("K", 84.50)):
        check(abs(run.step_limit(s) - want) < 1e-9, f"{s} effective limit {run.step_limit(s)} == {want}")
    os.environ["BUDGET_LIMIT_USD"] = "60"
    check(abs(run.step_limit("L") - 60) < 1e-9, "a lower env limit (60) still wins")
    os.environ["BUDGET_LIMIT_USD"] = "120"

    # 2. guard wrapper: refused above the cap even though env says 120
    orig = costs.guard
    run.install_step_guard(costs, 66.03)
    spend(65.99)
    try:
        costs.guard("nano-banana-2-edit", 1)
        check(False, "spent 65.99 + 0.08 > 66.03 must be refused")
    except costs.BudgetExceeded as e:
        check(True, f"refused at 65.99 + 0.08 with env=120: {e}")
    spend(65.90)
    try:
        costs.guard("nano-banana-2-edit", 1)
        check(True, "allowed at 65.90 + 0.08 <= 66.03")
    except Exception as e:
        check(False, f"65.90 + 0.08 should pass: {e}")

    # 3. through the real client path: refused before any network call
    fal_client.run = lambda *a, **k: (_ for _ in ()).throw(AssertionError("network reached"))
    spend(66.00)
    png = tmp / "ref.png"
    png.write_bytes(b"\x89PNG\r\n\x1a\n" + b"\0" * 32)
    try:
        fal_client.generate_image("x", tmp / "o.png", model="nano-banana-2", reference_images=[png])
        check(False, "fal_client.generate_image must be refused")
    except costs.BudgetExceeded:
        check(True, "fal_client.generate_image refused before the network (env=120, cap 66.03)")
    except AssertionError as e:
        check(False, str(e))

    # 4. re-installing does not stack wrappers; the original guard is kept
    run.install_step_guard(costs, 67.35)
    check(costs.guard._op_orig is orig and costs.guard._op_limit == 67.35, "re-install replaces the cap, keeps orig")
    print("RESULT:", "PASS" if not fails else f"{len(fails)} FAILED")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
