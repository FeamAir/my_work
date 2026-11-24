"""Quick take report (free): key profile, grid onsets, momentary at start/end, melody tracking of intro/hook/answer."""
import sys, os, subprocess, numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from a2lib import *
p = sys.argv[1]; x = load(p)
print("dur", round(len(x) / SR, 3))
prof = chroma(x, 0, len(x) / SR - 0.1, 150, 1500); print("key profile", top_pcs(prof, 7))
for g in [0, 12, 21, 45, 54, 57, 60, 63, 66, 69, 72, 81, 82.5]:
    t, j = onset_near(x, g, 0.12, 0.15); print(f"  grid {g:5}: onset {t:.3f} ({t - g:+.3f}) jump {j:5.1f}")
t, m = momentary(p)
print("M start", [round(v, 1) for v in m[(t >= 0.2) & (t <= 1.5)]])
print("M end  ", [(round(a, 1), round(b, 1)) for a, b in zip(t, m) if 81 <= a <= 87.1][::3])
def sec(a, b): s = x[int(a * SR):int(b * SR)]; return round(10 * np.log10(np.mean(s ** 2) + 1e-12), 1)
print("RMS dB intro0-3", sec(0, 3), "groove", sec(12, 21), "theme", sec(21, 45), "rise", sec(45, 57), "hook", sec(57, 69), "answer", sec(69, 81), "84-86", sec(84, 86))
for t0, n in ((0, 4), (57, 4), (69, 4)):
    print(subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "melody_track.py"), p, str(t0), str(n)], capture_output=True, text=True).stdout, end="")
