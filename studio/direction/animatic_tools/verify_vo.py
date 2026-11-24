#!/usr/bin/env python3
"""Animatic audio acceptance (QA A1-A5 method, made strict): every VO line in the spec is audible at the expected
level in the FINAL file, and the dx stem is on the picture's timeline.

  ANIM_V=v3 python3 -I verify_vo.py            # -> output/S01E01/animatic/spec/S01E01_animatic_v3_vo_check.json

Per line (window = spec start .. start + duration):
  * final mp4: RMS of the window (dBFS) and peak; pass if RMS >= median(all lines) - 6 dB and peak >= -30 dBFS;
  * stem_dx.wav: the line is really there (window RMS >= 20 dB above the 0.5 s just before it, or the window before
    is itself speech) — catches a shifted/short stem like v2's (72.7 s early, 1217.05 s long);
  * stem lengths == picture length;
  * digital silence (< -80 dBFS over 0.5 s) anywhere in the final outside the planned black (last 1.0 s).
Exit code 1 on any failure.
"""
import json
import os
import subprocess
import sys

import numpy as np

A = "/home/user/my_work/output/S01E01/animatic"
VER = os.environ.get("ANIM_V", "v3")
SR = 16000


def load(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32)


def db(x):
    return float(20 * np.log10(np.sqrt(np.mean(np.square(x, dtype=np.float64))) + 1e-9)) if len(x) else -200.0


def pk(x):
    return float(20 * np.log10(np.max(np.abs(x)) + 1e-9)) if len(x) else -200.0


def main():
    spec = json.load(open(f"{A}/spec/S01E01_animatic_{VER}.json"))
    D = spec["meta"]["total_s"]
    work = f"{A}/S01E01_animatic_{VER}_raw_work"
    final = f"{A}/S01E01_animatic_{VER}.mp4"
    fails = []
    stems = {}
    for f in sorted(os.listdir(work)):
        if f.startswith("stem_") or f.endswith("_ducked.wav"):
            d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                      f"{work}/{f}"], capture_output=True, text=True).stdout)
            stems[f] = d
            if abs(d - D) > 0.05:
                fails.append(f"{f}: {d:.3f} s, picture {D:.3f} s")
    x, dx = load(final), load(f"{work}/stem_dx.wav")
    rows = []
    for t in spec["tracks"]:
        if t["stem"] != "dx":
            continue
        a, b = int(t["start"] * SR), int((t["start"] + t["duration"]) * SR)
        pre = dx[max(0, a - SR // 2):a]
        r = dict(id=t["id"], start=t["start"], dur=t["duration"], final_rms=round(db(x[a:b]), 1),
                 final_peak=round(pk(x[a:b]), 1), dx_rms=round(db(dx[a:b]), 1), dx_pre=round(db(pre), 1))
        rows.append(r)
    med = float(np.median([r["final_rms"] for r in rows]))
    for r in rows:
        r["vs_median"] = round(r["final_rms"] - med, 1)
        ok_level = r["vs_median"] >= -6.0 and r["final_peak"] >= -30.0
        ok_stem = r["dx_rms"] > -50 and (r["dx_rms"] - r["dx_pre"] >= 20 or r["dx_pre"] > -50)
        r["ok"] = bool(ok_level and ok_stem)
        if not r["ok"]:
            fails.append(f"{r['id']} @ {r['start']:.2f}: final RMS {r['final_rms']} ({r['vs_median']:+.1f} vs median), "
                         f"peak {r['final_peak']}, stem {r['dx_rms']} (pre {r['dx_pre']})")
    # digital silence outside the planned 1-s black at the end
    n = SR // 2
    zero = []
    for i in range(0, int((D - 1.0) * SR) - n, n):
        if pk(x[i:i + n]) < -80:
            zero.append(round(i / SR, 1))
    if zero:
        fails.append(f"digital silence windows (0.5 s) at {zero[:20]}{' …' if len(zero) > 20 else ''}")
    rep = dict(file=final, picture_s=D, lines=len(rows), median_rms_dbfs=round(med, 1),
               worst=sorted(rows, key=lambda r: r["vs_median"])[:5], stems=stems, zero_windows=zero,
               failures=fails, passed=not fails, rows=rows)
    out = f"{A}/spec/S01E01_animatic_{VER}_vo_check.json"
    json.dump(rep, open(out, "w"), indent=1)
    print(json.dumps({k: rep[k] for k in ("lines", "median_rms_dbfs", "worst", "stems", "failures", "passed")},
                     indent=1))
    sys.exit(0 if rep["passed"] else 1)


if __name__ == "__main__":
    main()
