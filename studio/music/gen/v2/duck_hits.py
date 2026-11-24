"""'Breath' before the picture hits (r5): duck the mix before 0:57.042 and 1:09.042 so the hit is the clear attack
on the frame (the drum layer and the generated hook otherwise blur it by 50-120 ms). In place, 24-bit wav.
    python3 duck_hits.py MIX.wav [db57=-7] [db69=-5]"""
import sys, wave, numpy as np
p = sys.argv[1]; d57 = float(sys.argv[2]) if len(sys.argv) > 2 else -7.0; d69 = float(sys.argv[3]) if len(sys.argv) > 3 else -5.0
w = wave.open(p); sr, ch, sw, n = w.getframerate(), w.getnchannels(), w.getsampwidth(), w.getnframes(); raw = w.readframes(n); w.close()
assert sw == 3
b = np.frombuffer(raw, np.uint8).reshape(-1, 3).astype(np.int32)
x = (b[:, 0] | (b[:, 1] << 8) | (b[:, 2] << 16)); x = np.where(x >= 2 ** 23, x - 2 ** 24, x).astype(float).reshape(-1, ch)
t = np.arange(len(x)) / sr; g = np.zeros(len(x))
for hit, d in ((1369 / 24, d57), (1657 / 24, d69)):
    pts = [(hit - 0.30, 0), (hit - 0.20, d), (hit - 0.012, d), (hit - 0.002, 0)]
    m = (t >= pts[0][0]) & (t <= pts[-1][0]); g[m] += np.interp(t[m], *zip(*pts))
y = x * (10 ** (g / 20))[:, None]
yi = np.clip(np.round(y), -2 ** 23, 2 ** 23 - 1).astype(np.int32).reshape(-1)
out = np.stack([yi & 255, (yi >> 8) & 255, (yi >> 16) & 255], 1).astype(np.uint8)
w = wave.open(p, "wb"); w.setnchannels(ch); w.setsampwidth(3); w.setframerate(sr); w.writeframes(out.tobytes()); w.close()
print("ducked", p)
