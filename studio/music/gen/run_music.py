"""Composer's ElevenLabs Music runner (one take per call).

    STUDIO_ALLOW_PAID=1 BUDGET_LIMIT_USD=60 \
    python3 studio/music/gen/run_music.py PLAN.json --name theme-master --take 1 --seed 8011 \
        [--theme-id SONG_ID] [--cap 20000] [--max-takes 2] [--rate 2500] [--dry-run]

What it does:
  * validates the plan against the /v1/music schema (checked against api.elevenlabs.io/openapi.json
    2026-11-24): 1-30 chunks, each 3000-120000 ms, text <= 6132 chars, <= 30 lines of <= 200 chars,
    condition_strength inside conditioning_ref (low|medium|high|xhigh), conditioning range <= 30 s;
    every chunk must carry the studio bans (modulation / key change, F-sharp major, drone / pedal);
  * substitutes the THEME placeholder with --theme-id (refuses to send an unresolved placeholder);
  * GATES (gate-music-2026-11-24, C1-C5):
      C1 pipeline.costs.guard() before the POST (STUDIO_ALLOW_PAID, BUDGET_LIMIT_USD, balance floor)
         plus the same budget check with the credit-based worst-case USD estimate;
      C2 an error is logged with the measured (or, if unmeasurable, the estimated) cost, not $0;
      C3 a measurement failure after a successful POST still writes the ledger row and the costs
         row with the pre-call estimate, and the run stops (exit 3);
      C4 a measured credit delta <= 0 after an OK take (lag, cycle reset) is re-read 4x15 s, then
         recorded as the estimate and the run stops (exit 3);
      C5 the prompt bans are enforced by validate();
    plus a HARD CREDIT CAP on the session ledger output/music/gen_ledger.jsonl and a per-name take
    limit (--max-takes);
  * POST /v1/music, model music_v2_5, store_for_inpainting=true, seed fixed; saves the song-id header;
  * uploads the take to R2 (music/S01/takes/...) via pipeline.storage.
--dry-run: validation + cap check + guard report + free subscription read only. No paid call.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from pipeline import config, costs, storage  # noqa: E402
from pipeline.net import request  # noqa: E402

API = "https://api.elevenlabs.io"
MODEL = "music_v2_5"
ENDPOINT = "/v1/music"
SERVICE = "elevenlabs-music"
OUT_DIR = ROOT / "output" / "music"
LEDGER = OUT_DIR / "gen_ledger.jsonl"
R2_PREFIX = "music/S01/takes"
# Worst-case planning rate until the first take is measured (third-party figures: ~900 cr/min).
WORST_CASE_CREDITS_PER_MIN = 2500
STRENGTHS = {"low", "medium", "high", "xhigh"}
# Studio bans every chunk must carry (main_theme.md §2, opening_song.md §1.1 items 2-3, gate C5).
REQUIRED_BANS = ("key change", "modulation", "F-sharp major chord", "low drone", "pedal tone")
EXIT_STOP = 3  # take saved and recorded, but the cap went blind: a human looks before the next take


class GateRefused(SystemExit):
    pass


def validate(plan: dict) -> float:
    chunks = plan.get("chunks")
    assert isinstance(chunks, list) and 1 <= len(chunks) <= 30, "1-30 chunks"
    total = 0
    for i, c in enumerate(chunks):
        d = c["duration_ms"]
        assert 3000 <= d <= 120000, f"chunk {i}: duration {d}"
        assert len(c["text"]) <= 6132, f"chunk {i}: text too long"
        lines = c["text"].split("\n")
        assert len(lines) <= 30 and all(len(x) <= 200 for x in lines), f"chunk {i}: lines"
        assert len(c.get("positive_styles", [])) <= 50 and len(c.get("negative_styles", [])) <= 50
        assert c.get("context_adherence", "high") in {"low", "medium", "high"}
        assert "condition_strength" not in c, f"chunk {i}: condition_strength must sit in conditioning_ref"
        neg = {s.lower() for s in c.get("negative_styles", [])}
        missing = [b for b in REQUIRED_BANS if b.lower() not in neg]
        assert not missing, f"chunk {i}: missing studio bans {missing}"
        ref = c.get("conditioning_ref")
        if ref:
            r = ref["range"]
            assert 0 < r["end_ms"] - r["start_ms"] <= 30000, f"chunk {i}: ref range"
            assert ref.get("condition_strength", "medium") in STRENGTHS
            assert ref["song_id"] not in {"THEME", "SKETCH"}, f"chunk {i}: unresolved {ref['song_id']}"
        total += d
    return total / 1000


def resolve(plan: dict, theme_id: str | None) -> dict:
    plan = copy.deepcopy(plan)
    for c in plan["chunks"]:
        ref = c.get("conditioning_ref")
        if ref and ref["song_id"] == "THEME":
            if not theme_id:
                raise SystemExit("plan needs --theme-id (song_id of the approved theme master)")
            ref["song_id"] = theme_id
    return plan


def credits_used() -> int:
    r = request("GET", API + "/v1/user/subscription", service="elevenlabs.info",
                headers={"xi-api-key": config.get("ELEVENLABS_API_KEY")})
    return int(r.json()["character_count"])


def ledger_rows() -> list[dict]:
    if not LEDGER.exists():
        return []
    return [json.loads(x) for x in LEDGER.read_text().splitlines() if x.strip()]


def ledger_spent() -> int:
    return sum(int(r.get("credits", 0)) for r in ledger_rows())


def takes_used(name: str) -> int:
    return sum(1 for r in ledger_rows() if r.get("name") == name and r.get("kind", "take") == "take")


def ledger_append(row: dict) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    row = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"), **row}
    with LEDGER.open("a") as f:
        f.write(json.dumps(row) + "\n")


def credit_usd() -> float:
    return costs._elevenlabs_credit_usd()


def preflight(secs: float, est_credits: float, a) -> None:
    """All refusals before money moves (cap, take limit, C1)."""
    spent = ledger_spent()
    print(f"{secs:.1f} s, est <= {est_credits:.0f} cr; ledger spent {spent} / cap {a.cap}; "
          f"takes for '{a.name}': {takes_used(a.name)} / {a.max_takes}")
    if spent + est_credits > a.cap:
        raise GateRefused("REFUSED: credit cap would be exceeded")
    if takes_used(a.name) >= a.max_takes:
        raise GateRefused(f"REFUSED: take limit {a.max_takes} reached for '{a.name}'")
    est_usd = est_credits * credit_usd()
    # C1: the studio guard (STUDIO_ALLOW_PAID, BUDGET_LIMIT_USD with the per-minute price, floor)
    costs.guard(SERVICE, secs / 60)
    # ...and the same budget check with the credit-based worst case, which is the larger figure.
    limit = config.budget_limit_usd()
    if limit is not None and costs.total_spent() + est_usd > limit:
        raise costs.BudgetExceeded(f"credit-based estimate ${est_usd:.2f} would pass BUDGET_LIMIT_USD ${limit:.2f}")
    costs._check_floor(SERVICE, est_usd)
    print(f"guard OK: est ${est_usd:.2f}, spent ${costs.total_spent():.2f}, limit {limit}")


def measure(before: int | None, retries: int = 4, wait: float = 15.0) -> tuple[int | None, str]:
    """Credit delta since `before`. Returns (credits or None, note). Never raises."""
    if before is None:
        return None, "no baseline"
    delta, note = None, ""
    for i in range(retries + 1):
        try:
            delta = credits_used() - before
        except Exception as e:  # noqa: BLE001
            note = f"measure failed: {type(e).__name__}: {e}"
            delta = None
        if delta is not None and delta > 0:
            return delta, "measured"
        if i < retries:
            time.sleep(wait)
    return (delta if delta is not None and delta > 0 else None), note or f"delta {delta} <= 0"


def run(a) -> int:
    plan = resolve(json.loads(Path(a.plan).read_text()), a.theme_id)
    secs = validate(plan)
    est = secs / 60 * a.rate
    print(f"plan {a.plan}")
    if a.dry_run:
        try:
            preflight(secs, est, a)
        except (GateRefused, costs.PaidCallsDisabled, costs.BudgetExceeded, costs.BalanceFloorReached) as e:
            print(f"dry run: a real run would be refused: {e}")
        print(f"account credits used so far: {credits_used()}")
        print("dry run: no paid call")
        return 0
    preflight(secs, est, a)
    before = credits_used()
    print(f"account credits used so far: {before}")

    body = {"model_id": MODEL, "composition_plan": plan, "seed": a.seed, "store_for_inpainting": True}
    stem = f"lib_mus_{a.name}_take{a.take}_s{a.seed}"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"{stem}.mp3"
    base = {"kind": "take", "name": a.name, "take": stem, "plan": a.plan, "seed": a.seed, "seconds": secs}
    try:
        resp = request("POST", API + ENDPOINT, service="elevenlabs.music", retries=1,
                       headers={"xi-api-key": config.get("ELEVENLABS_API_KEY"),
                                "Content-Type": "application/json", "Accept": "audio/mpeg"},
                       params={"output_format": "mp3_48000_192"}, json=body, timeout=(10, 900))
    except Exception as e:  # C2
        err = f"{type(e).__name__}: {str(e)[:300]}"
        traceback.print_exc()
        credits, note = measure(before, retries=1)
        if credits is None:
            try:  # a readable zero delta on a failed call means "not charged"
                credits, note = max(credits_used() - before, 0), "measured (failed call)"
            except Exception as me:  # noqa: BLE001  unknown whether charged: book the estimate
                credits, note = int(round(est)), f"estimate ({type(me).__name__})"
        ledger_append({**base, "credits": credits, "credits_source": note, "status": "error", "error": err})
        costs.log(SERVICE, secs / 60, provider="elevenlabs", endpoint=ENDPOINT,
                  status=f"error: {err[:120]}", usd=credits * credit_usd(),
                  extra={"credits": credits, "credits_source": note, "take": stem})
        print(f"ERROR logged: {err}; booked {credits} cr ({note})", file=sys.stderr)
        return 1

    out.write_bytes(resp.content)
    song_id = resp.headers.get("song-id")
    credits, note = measure(before)  # C3 + C4: never raises, retries a lagging delta
    stop = credits is None
    if stop:
        credits, note = int(round(est)), f"estimate ({note})"
    # Ledger row first, so the cap never goes blind (C3).
    ledger_append({**base, "credits": credits, "credits_source": note, "song_id": song_id,
                   "file": str(out), "status": "ok"})
    costs.log(SERVICE, secs / 60, provider="elevenlabs", endpoint=ENDPOINT,
              request_id=resp.headers.get("request-id"), usd=credits * credit_usd(),
              extra={"model_id": MODEL, "seed": a.seed, "seconds": secs, "credits": credits,
                     "credits_source": note, "song_id": song_id, "take": stem, "plan": a.plan})
    key = f"{R2_PREFIX}/{out.name}"
    try:
        storage.upload(str(out), key)
        r2 = key
    except Exception as e:  # noqa: BLE001  storage failure must not lose the take record
        r2 = f"upload failed: {type(e).__name__}: {e}"
    ledger_append({"kind": "upload", "name": a.name, "take": stem, "credits": 0, "r2": r2})
    print(json.dumps({"take": stem, "song_id": song_id, "credits": credits, "credits_source": note,
                      "usd": round(credits * credit_usd(), 4), "file": str(out), "r2": r2}, indent=1))
    if stop:
        print("STOP: credit delta not measurable; the estimate was booked. Check billing before the "
              "next take (gate C3/C4).", file=sys.stderr)
        return EXIT_STOP
    return 0


def parse(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--name", required=True)
    ap.add_argument("--take", type=int, required=True)
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--theme-id")
    ap.add_argument("--cap", type=int, default=20000)
    ap.add_argument("--max-takes", type=int, default=2)
    ap.add_argument("--rate", type=float, default=WORST_CASE_CREDITS_PER_MIN,
                    help="credits/min used for the pre-call estimate (set from the first measured take x1.1)")
    ap.add_argument("--dry-run", action="store_true")
    return ap.parse_args(argv)


def main(argv=None) -> None:
    sys.exit(run(parse(argv)))


if __name__ == "__main__":
    main()
