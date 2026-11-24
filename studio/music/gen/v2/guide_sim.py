"""Per-half-bar chroma similarity (250-1200 Hz) of a take vs the call guide, per section (free).
python3 guide_sim.py TAKE.mp3 [GUIDE.wav]"""
import sys, os, numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from a2lib import load, chroma
t = load(sys.argv[1]); g = load(sys.argv[2] if len(sys.argv) > 2 else "/home/user/my_work/output/music/guide/anthem_v2_call_guide_Fm.wav")
o = 0.03
for name, a, b in (("intro", 0, 12), ("hook", 57, 69), ("answer", 69, 81), ("logo", 81, 84)):
    s = []
    for k in range(int((b - a) / 1.5)):
        t0 = a + o + 1.5 * k
        A, B = chroma(t, t0, t0 + 1.5, 250, 1200), chroma(g, t0, t0 + 1.5, 250, 1200)
        s.append(float(np.dot(A, B) / np.linalg.norm(A) / np.linalg.norm(B)))
    print(f"{name:6s} mean {np.mean(s):.2f} | " + " ".join(f"{v:.2f}" for v in s))
