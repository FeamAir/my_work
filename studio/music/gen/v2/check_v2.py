"""Delivery check for anthem v2 (free, r5): duration, LUFS-I, true peak, hits vs the picture grid (frames 1369/1657/
1981 at 24 fps, tolerance +-1 frame), 0:00 attack (momentary in first 0.5 s), logo tail, melody tracking.
    python3 check_v2.py FILE.mp3 [--json]"""
import sys, os, json, subprocess, numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from a2lib import *
p = sys.argv[1]; x = load(p)
I, TP = lufs_tp(p)
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True).stdout)
res = {"file": os.path.basename(p), "duration_s": round(dur, 3), "LUFS_I": I, "TP_dBTP": TP, "hits": {}}
for k, tgt in HITS.items():
    t, j = onset_near(x, tgt, 0.12, 0.15)
    fr = t * FPS
    res["hits"][k] = {"target_s": round(tgt, 3), "onset_s": round(t, 3), "delta_ms": round((t - tgt) * 1000),
                      "delta_frames": round(fr - round(tgt * FPS), 2), "ok": abs(t - tgt) <= 1 / FPS, "jump_dB": round(j, 1)}
t0, j0 = onset_near(x, 0.0, 0.0, 0.2); res["attack_0"] = {"onset_s": round(t0, 3)}
tt, m = momentary(p)
first = m[(tt >= 0.3) & (tt <= 0.5)]  # 400 ms windows ending inside the first 0.5 s (ffmpeg stamps the window start+0.1)
res["M_first_0.5s"] = [round(v, 1) for v in first]; res["M_first_0.5s_max"] = round(float(first.max()), 1)
res["intro_ok(>=-18)"] = bool(first.max() >= -18.0)
res["M_tail"] = {f"{a:.1f}": round(b, 1) for a, b in zip(tt, m) if a in np.round(np.arange(82.5, 87.01, 0.5), 1) or abs(a - round(a * 2) / 2) < 1e-6 and 82.5 <= a <= 87}
def lvl(a, b): s = x[int(a * SR):int(b * SR)]; return round(10 * np.log10(np.mean(s ** 2) + 1e-12), 1)
res["RMS_dB"] = {"intro0-3": lvl(0, 3), "groove": lvl(12, 21), "theme": lvl(21, 45), "rise": lvl(45, 57),
                 "hook": lvl(57, 69), "answer": lvl(69, 81), "logo82.5-85.5": lvl(82.5, 85.5), "85.5-86.5": lvl(85.5, 86.5)}
print(json.dumps(res, indent=1))
for t0_, n in ((0, 4), (57, 4), (69, 4)):
    print(subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "melody_track.py"), p, str(t0_), str(n), "0.04"], capture_output=True, text=True).stdout, end="")
