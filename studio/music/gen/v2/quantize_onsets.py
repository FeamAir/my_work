"""Snap detected drum onsets from T0 on to the 16th-note grid (80 BPM, offset 0.04 s, the grid drum_reinforce.py
uses for its taiko hits) when within 0.10 s; merge duplicates. Keeps the picture hits 57.042 / 69.042 / 82.542 on
the frame (r5: the generated hook hits have soft lows, so the kick detector fired 85 ms late at 0:57).
    python3 quantize_onsets.py on.json [T0=56.9]"""
import json, sys
p = sys.argv[1]; T0 = float(sys.argv[2]) if len(sys.argv) > 2 else 56.9
G, OFF = 0.1875, 0.04
on = json.load(open(p)); moved = 0
for k, lst in on.items():
    out, seen = [], set()
    for ev in lst:
        t = ev[0]
        if t >= T0:
            q = round((t - OFF) / G) * G + OFF
            if abs(q - t) <= 0.10:
                moved += abs(q - t) > 0.005; t = round(q, 4)
        key = round(t, 3)
        if key in seen: continue
        seen.add(key); out.append([t] + ev[1:])
    on[k] = out
json.dump(on, open(p, "w")); print(f"quantized {moved} onsets from {T0} s")
