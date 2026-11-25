#!/usr/bin/env python3
"""Saga OP v1.2 — one verification pass ($0, ffmpeg + numpy; no API call).

    python3 -I op_saga_verify_v12.py FILE [--json OUT]

  1. format: frames / duration / fps / audio of FILE;
  2. freezedetect (d = 0.15) at n = 0.001 / 0.002 / 0.003 — only the planned black B16 (1360-1368) may show;
  3. mpdecimate with the DEFAULT parameters (hi 768, lo 320, frac 0.33) — dropped frames listed by cut; only B16 planned;
  4. shot lengths: scene changes (scdet) vs the CUTS grid; every cut of the grid must be a change, extra changes listed
     (known in-shot events: POP 493 / 1155, B15 flashes, C13 wipe);
  5. loudness: integrated LUFS, true peak, momentary (400 ms) at 0-0.5 s, 0-1.5 s, max over 0-9 s, median 12-57 s / 57-82 s;
  6. hook: mean luma (YAVG, 0-255) for each second 0-9 (target >= 70), and motion in 0-1.5 s;
  7. hits: the audio onset nearest to frames 0, 1369, 1657, 1981 (ms off the frame start);
  8. logo: frame 1980 vs 1981 change in the letter box (the logo lands on 1981) + §12 p. 7 contrast probe (frame 2028)
     + И10 jitter (phase correlation of the letter band 1990-2087).
"""
import json
import os
import re
import subprocess
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import op_saga_build_c12 as b  # noqa: E402

sa, an = b.sa, b.an
FPS, TOTAL = an.FPS, an.TOTAL
KNOWN_IN_SHOT = set(range(1332, 1360)) | {493, 1155} | set(range(1981, 1995))


def ff(args):
    return subprocess.run(["ffmpeg", "-hide_banner", *args], capture_output=True, text=True).stderr


def fmt(path):
    j = json.loads(subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-show_entries",
                                   "stream=codec_type,codec_name,width,height,r_frame_rate,avg_frame_rate,nb_read_frames,duration,sample_rate",
                                   "-of", "json", path], capture_output=True, text=True).stdout)
    return j["streams"]


def freezes(path):
    out = {}
    for n in (0.001, 0.002, 0.003):
        e = ff(["-i", path, "-vf", f"freezedetect=n={n}:d=0.15", "-an", "-f", "null", "-"])
        st = [float(x) for x in re.findall(r"freeze_start: ([\d.]+)", e)]
        en = [float(x) for x in re.findall(r"freeze_end: ([\d.]+)", e)] + [TOTAL / FPS]
        out[str(n)] = [{"from_s": a, "to_s": en[k], "cut": sa.cut_of(round(a * FPS)),
                        "planned": 1359 <= round(a * FPS) and round(en[k] * FPS) - 1 <= 1369} for k, a in enumerate(st)]
    return out


def mpdecimate(path):
    e = ff(["-i", path, "-vf", "mpdecimate,showinfo", "-an", "-f", "null", "-"])
    kept = {round(float(t) * FPS) for t in re.findall(r"pts_time:([\d.]+)", e)}
    dups = [f for f in range(TOTAL) if f not in kept]
    by = {}
    for f in dups:
        by.setdefault(sa.cut_of(f), []).append(f)
    unpl = {c: [v[0], v[-1], len(v)] for c, v in by.items() if c != "B16"}
    return {"dropped": len(dups), "by_cut": {c: [v[0], v[-1], len(v)] for c, v in by.items()}, "unplanned": unpl}


def scenes(path):
    """every grid cut must be the local peak of the frame-to-frame change (+-2 frames) and stand clear of the shot's own
    motion; A05a -> A05b (252) is one K07C piece by design (known since v1). Extra peaks (> 2.2x the local median, not on
    the grid, not a known in-shot event) are listed."""
    g = luma_frames(path, 0, TOTAL - 1)
    d = np.abs(np.diff(g, axis=0)).mean((1, 2))           # d[k]: change k -> k+1; a cut at f shows as d[f-1]
    bad, ratio = [], {}
    for c, s0, n in sa.CUTS:
        if s0 == 0:
            continue
        w = d[max(0, s0 - 3):s0 + 2]
        loc = np.median(np.concatenate([d[max(0, s0 - 6):s0 - 1], d[s0:s0 + 5]]))
        ratio[s0] = round(float(d[s0 - 1] / max(loc, 0.1)), 1)
        if s0 != 252 and (d[s0 - 1] < w.max() - 1e-6 or ratio[s0] < 1.4):
            bad.append({"cut": c, "frame": s0, "change": round(float(d[s0 - 1]), 1), "vs_local": ratio[s0]})
    grid = {s for _, s, _ in sa.CUTS}
    extra = []
    for k in range(3, len(d) - 3):
        f = k + 1
        loc = np.median(np.concatenate([d[k - 3:k], d[k + 1:k + 4]]))
        if d[k] > 2.2 * max(loc, 1.0) and d[k] >= d[k - 1] and d[k] >= d[k + 1] and f not in grid and f not in KNOWN_IN_SHOT:
            extra.append({"frame": f, "cut": sa.cut_of(f), "change": round(float(d[k]), 1), "vs_local": round(float(d[k] / max(loc, 1.0)), 1)})
    lens = {c: round(n / FPS, 3) for c, _, n in sa.CUTS}
    odd = {c: v for c, v in lens.items() if v not in (0.75, 1.5)}
    return {"shots": len(sa.CUTS), "grid_cuts_ok": len(sa.CUTS) - 1 - len(bad), "grid_cuts_not_clean": bad,
            "min_cut_vs_local": min(v for f, v in ratio.items() if f != 252), "extra_peaks_in_shot": extra,
            "lengths_not_0.75_or_1.5": odd}


def loud(path):
    e = ff(["-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"])
    I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1])
    tp = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", e)[-1])
    rows = [(float(t), float(m)) for t, m in re.findall(r"t:\s*([\d.]+)\s+TARGET.*?M:\s*(-?[\d.]+)", e)]
    t = np.array([r[0] for r in rows])
    m = np.array([r[1] for r in rows])

    def mx(a, b_):
        s = m[(t > a) & (t <= b_ + 1e-6)]
        return round(float(s.max()), 1) if len(s) else None

    def med(a, b_):
        return round(float(np.median(m[(t > a) & (t <= b_)])), 1)
    return {"integrated_LUFS": I, "true_peak_dBFS": tp, "M_max_0-0.5s": mx(0, 0.5), "M_max_0-1.5s": mx(0, 1.5),
            "M_max_0-9s": mx(0, 9), "M_median_0-9s": med(0.4, 9), "M_median_12-57s": med(12, 57), "M_median_57-82s": med(57, 82)}


def luma_frames(path, f0, f1, w=320, h=180):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", f"select='between(n\\,{f0}\\,{f1})',scale={w}:{h}",
                          "-vsync", "0", "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.float32)


def hook(path):
    e = ff(["-i", path, "-t", "9", "-vf", "signalstats,metadata=print:key=lavfi.signalstats.YAVG", "-an", "-f", "null", "-"])
    y = np.array([float(v) for v in re.findall(r"YAVG=([\d.]+)", e)])
    per_s = [round(float(y[k * FPS:(k + 1) * FPS].mean()), 1) for k in range(9)]
    g = luma_frames(path, 0, 36)
    mot = np.abs(np.diff(g, axis=0)).mean((1, 2))
    return {"YAVG_per_second_0-9": per_s, "min": min(per_s), "pass_>=70": min(per_s) >= 70,
            "motion_0-1.5s_median": round(float(np.median(mot)), 2)}


def hits(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", "24000", "-f", "f32le", "-"],
                         capture_output=True).stdout
    x = np.frombuffer(raw, np.float32)
    hop, win = 240, 1024
    n = len(x) // hop
    pad = np.pad(x, (win // 2, win // 2))
    S = np.abs(np.fft.rfft(np.stack([pad[i * hop:i * hop + win] * np.hanning(win) for i in range(n)]), axis=1))
    env = np.concatenate([[0], np.maximum(np.diff(np.log1p(S), axis=0), 0).sum(1)])
    dt = hop / 24000
    out = {}
    for f in (0, 1369, 1657, 1981):
        t = f / FPS
        a, b_ = max(0, int((t - 0.12) / dt)), int((t + 0.12) / dt)
        k = a + int(np.argmax(env[a:b_]))
        out[str(f)] = {"onset_ms_off_frame": round((k * dt - t) * 1000), "strength_vs_median": round(float(env[k] / np.median(env)), 1)}
    return out


def logo(path):
    g = luma_frames(path, 1978, 1983, 1920, 1080)
    box = (slice(430, 880), slice(330, 1590))
    d = [round(float(np.abs(g[k + 1][box] - g[k][box]).mean()), 2) for k in range(len(g) - 1)]
    return {"letter_box_change_1978-1983": dict(zip(["1979", "1980", "1981", "1982", "1983"], d)),
            "lands_on_1981": int(np.argmax(d)) + 1979 in (1981,), "probe_2028": b.probe(path), "jitter": b.jitter(path)}


def main():
    path = sys.argv[1]
    rep = {"file": path, "size_MB": round(os.path.getsize(path) / 1e6, 1), "streams": fmt(path)}
    for k, fn in (("freezedetect", freezes), ("mpdecimate_default", mpdecimate), ("shots", scenes), ("loudness", loud),
                  ("hook", hook), ("hits", hits), ("logo", logo)):
        rep[k] = fn(path)
        print(k, "done", file=sys.stderr, flush=True)
    s = json.dumps(rep, indent=1)
    if "--json" in sys.argv:
        open(sys.argv[sys.argv.index("--json") + 1], "w").write(s)
    print(s)


if __name__ == "__main__":
    main()
