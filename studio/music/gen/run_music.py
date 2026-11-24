"""Composer's ElevenLabs Music runner (one take per call).

    python3 studio/music/gen/run_music.py PLAN.json --name op-song --take 1 --seed 101 \
        [--theme-id SONG_ID] [--cap 25000] [--dry-run]

What it does:
  * validates the plan against the /v1/music schema (checked against api.elevenlabs.io/openapi.json
    2026-11-24): 1-30 chunks, each 3000-120000 ms, text <= 6132 chars, <= 30 lines of <= 200 chars,
    condition_strength inside conditioning_ref (low|medium|high|xhigh), conditioning range <= 30 s;
  * substitutes the THEME placeholder with --theme-id (refuses to send an unresolved placeholder);
  * HARD CAP: the session ledger output/music/gen_ledger.jsonl sums measured credits; a take is
    refused if spent + worst-case estimate would pass --cap;
  * measures the real cost as the delta of GET /v1/user/subscription character_count (free call);
  * POST /v1/music, model music_v2_5, store_for_inpainting=true, seed fixed; saves the song-id header;
  * logs to output/costs.jsonl via pipeline.costs (service elevenlabs-music, measured credits in extra)
    and uploads the take to R2 (music/S01/takes/...) via pipeline.storage.
--dry-run: validation + cap check + free subscription read only. No paid call.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from pipeline import config, costs, storage  # noqa: E402
from pipeline.net import request  # noqa: E402

API = "https://api.elevenlabs.io"
MODEL = "music_v2_5"
OUT_DIR = ROOT / "output" / "music"
LEDGER = OUT_DIR / "gen_ledger.jsonl"
R2_PREFIX = "music/S01/takes"
# Worst-case planning rate until the first take is measured (third-party figures: ~900 cr/min).
WORST_CASE_CREDITS_PER_MIN = 2500
STRENGTHS = {"low", "medium", "high", "xhigh"}


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


def ledger_spent() -> int:
    if not LEDGER.exists():
        return 0
    return sum(int(json.loads(x).get("credits", 0)) for x in LEDGER.read_text().splitlines() if x.strip())


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--name", required=True)
    ap.add_argument("--take", type=int, required=True)
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--theme-id")
    ap.add_argument("--cap", type=int, default=25000)
    ap.add_argument("--rate", type=float, default=WORST_CASE_CREDITS_PER_MIN,
                    help="credits/min used for the pre-call estimate (set from the first measured take)")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    plan = resolve(json.loads(Path(a.plan).read_text()), a.theme_id)
    secs = validate(plan)
    est = secs / 60 * a.rate
    spent = ledger_spent()
    print(f"plan {a.plan}: {secs:.1f} s, est <= {est:.0f} cr; ledger spent {spent} / cap {a.cap}")
    if spent + est > a.cap:
        raise SystemExit("REFUSED: cap would be exceeded")
    before = credits_used()
    print(f"account credits used so far: {before}")
    if a.dry_run:
        print("dry run: no paid call")
        return

    body = {"model_id": MODEL, "composition_plan": plan, "seed": a.seed, "store_for_inpainting": True}
    endpoint = "/v1/music"
    stem = f"lib_mus_{a.name}_take{a.take}_s{a.seed}"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"{stem}.mp3"
    try:
        resp = request("POST", API + endpoint, service="elevenlabs.music", retries=1,
                       headers={"xi-api-key": config.get("ELEVENLABS_API_KEY"),
                                "Content-Type": "application/json", "Accept": "audio/mpeg"},
                       params={"output_format": "mp3_48000_192"}, json=body, timeout=(10, 900))
    except Exception as e:
        after = credits_used()
        costs.log("elevenlabs-music", secs / 60, provider="elevenlabs", endpoint=endpoint,
                  status=f"error: {type(e).__name__}", extra={"credits": after - before, "take": stem})
        with LEDGER.open("a") as f:
            f.write(json.dumps({"take": stem, "credits": after - before, "status": "error"}) + "\n")
        raise
    out.write_bytes(resp.content)
    song_id = resp.headers.get("song-id")
    after = credits_used()
    credits = after - before
    usd = credits * costs._elevenlabs_credit_usd()
    costs.log("elevenlabs-music", secs / 60, provider="elevenlabs", endpoint=endpoint,
              request_id=resp.headers.get("request-id"), usd=usd,
              extra={"model_id": MODEL, "seed": a.seed, "seconds": secs, "credits": credits,
                     "song_id": song_id, "take": stem, "plan": a.plan})
    key = f"{R2_PREFIX}/{out.name}"
    try:
        storage.upload(str(out), key)
        r2 = key
    except Exception as e:  # storage failure must not lose the take record
        r2 = f"upload failed: {type(e).__name__}: {e}"
    row = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"), "take": stem,
           "plan": a.plan, "seed": a.seed, "song_id": song_id, "credits": credits,
           "seconds": secs, "file": str(out), "r2": r2, "status": "ok"}
    with LEDGER.open("a") as f:
        f.write(json.dumps(row) + "\n")
    print(json.dumps(row, indent=1))


if __name__ == "__main__":
    main()
