"""Crude predominant-pitch tracker for checking the call (free): per eighth note on the 80 BPM grid, the strongest
pitch class + octave in 250-1100 Hz via a harmonic-sum spectrum.  python3 melody_track.py FILE T0 BARS [OFFSET]"""
import sys, os, numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from a2lib import load, SR, NAMES
p, t0, bars = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]); off = float(sys.argv[4]) if len(sys.argv) > 4 else 0.025
x = load(p); n = 8192; f = np.fft.rfftfreq(n, 1 / SR); w = np.hanning(n)
cands = np.arange(55, 86)  # G3..C#6 midi
fr = 440 * 2 ** ((cands - 69) / 12)
out = []
for k in range(bars * 8):
    t = t0 + off + k * 0.375 + 0.06
    seg = x[int(t * SR):int(t * SR) + n]
    if len(seg) < n: break
    S = np.abs(np.fft.rfft(seg * w))
    def amp(fq): i = int(round(fq / (SR / n))); return S[max(i - 1, 0):i + 2].max()
    sc = [sum(amp(f0 * h) / h ** 0.5 for h in (1, 2, 3, 4)) for f0 in fr]
    m = cands[int(np.argmax(sc))]
    out.append(f"{NAMES[m % 12]}{m // 12 - 1}")
for b in range(bars):
    print(f"bar@{t0 + 3 * b:6.2f}: " + " ".join(out[b * 8:(b + 1) * 8]))
