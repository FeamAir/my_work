"""Upload the anthem call guide to ElevenLabs (/v1/music/upload) so plans can condition on it (composer r5).

PAID: the API docs price an upload like a generation of the same length. This script uses the SAME guards as
run_music.py (it imports them, nothing is re-implemented or relaxed):
  * ledger credit cap (--cap) on output/music/gen_ledger.jsonl, worst-case estimate from --rate;
  * C1 costs.guard (STUDIO_ALLOW_PAID, BUDGET_LIMIT_USD) + the credit-based budget check + balance floor;
  * C2 errors booked with measured/estimated credits, C3/C4 measurement via run_music.measure, ledger row first.
The ledger row has kind "guide_upload" (counts toward the credit cap, not toward a take limit).

    STUDIO_ALLOW_PAID=1 python3 upload_guide.py GUIDE.mp3 --name theme-op-anthem-v2-guide --cap 20209 [--dry-run]
"""
import argparse, json, subprocess, sys, traceback
from pathlib import Path

GEN = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(GEN))
import run_music as rm  # noqa: E402
from run_music import costs, config, request, API, SERVICE  # noqa: E402

ENDPOINT = "/v1/music/upload"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file"); ap.add_argument("--name", required=True)
    ap.add_argument("--cap", type=int, default=20000)
    ap.add_argument("--rate", type=float, default=rm.WORST_CASE_CREDITS_PER_MIN)
    ap.add_argument("--max-takes", type=int, default=1)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    secs = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", a.file],
                                capture_output=True, text=True, check=True).stdout)
    est = secs / 60 * a.rate
    if any(r.get("kind") == "guide_upload" and r.get("name") == a.name and r.get("status") == "ok"
           for r in rm.ledger_rows()):
        raise SystemExit(f"REFUSED: '{a.name}' already uploaded (see ledger)")
    if a.dry_run:
        try:
            rm.preflight(secs, est, a)
        except Exception as e:  # noqa: BLE001
            print(f"dry run: a real run would be refused: {e}")
        print("dry run: no paid call"); return 0
    rm.preflight(secs, est, a)
    before = rm.credits_used()
    print(f"account credits used so far: {before}")
    base = {"kind": "guide_upload", "name": a.name, "file": a.file, "seconds": round(secs, 3)}
    try:
        with open(a.file, "rb") as fh:
            resp = request("POST", API + ENDPOINT, service="elevenlabs.music.upload", retries=1,
                           headers={"xi-api-key": config.get("ELEVENLABS_API_KEY")},
                           files={"file": (Path(a.file).name, fh, "audio/mpeg")},
                           data={"extract_composition_plan": "false"}, timeout=(10, 600))
    except Exception as e:  # C2
        err = f"{type(e).__name__}: {str(e)[:300]}"; traceback.print_exc()
        credits, note = rm.measure(before, retries=1)
        if credits is None:
            try:
                credits, note = max(rm.credits_used() - before, 0), "measured (failed call)"
            except Exception as me:  # noqa: BLE001
                credits, note = int(round(est)), f"estimate ({type(me).__name__})"
        rm.ledger_append({**base, "credits": credits, "credits_source": note, "status": "error", "error": err})
        costs.log(SERVICE, secs / 60, provider="elevenlabs", endpoint=ENDPOINT, status=f"error: {err[:120]}",
                  usd=credits * rm.credit_usd(), extra={"credits": credits, "credits_source": note, "upload": a.name})
        print(f"ERROR logged: {err}; booked {credits} cr ({note})", file=sys.stderr); return 1
    body = resp.json(); song_id = body.get("song_id")
    credits, note = rm.measure(before)
    stop = credits is None
    if stop:
        credits, note = int(round(est)), f"estimate ({note})"
    rm.ledger_append({**base, "credits": credits, "credits_source": note, "song_id": song_id, "status": "ok"})
    costs.log(SERVICE, secs / 60, provider="elevenlabs", endpoint=ENDPOINT, request_id=resp.headers.get("request-id"),
              usd=credits * rm.credit_usd(), extra={"credits": credits, "credits_source": note, "song_id": song_id,
                                                     "upload": a.name, "seconds": round(secs, 3)})
    print(json.dumps({"song_id": song_id, "credits": credits, "credits_source": note,
                      "usd": round(credits * rm.credit_usd(), 4)}, indent=1))
    return rm.EXIT_STOP if stop else 0


if __name__ == "__main__":
    sys.exit(main())
