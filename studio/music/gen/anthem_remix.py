"""OP anthem lift (free, r4): harmonic/percussive split (soft-mask median HPSS, stereo, 48 kHz) and a remix
with time-varying gains, so the 0:57.0 hook lifts instead of deflating:
  * rise 45.0-55.5: harmonic layer starts 1.5 dB down and climbs to 0 (crescendo contrast);
  * 'breath' 56.40-57.0: harmonic layer -4 dB (the drums-only pre-hit, picture: flashes + 9 frames of black);
  * hook 57.0-69.0: harmonic +2.5 dB, presence 1.2-3.5 kHz +2 dB on it (horns/trumpets forward); attack 30 ms;
  * answer 69.0-81.0: harmonic +2.0 dB, presence +1.5 dB; back to 0 dB over 81.0-82.0.
H + P with all gains at 0 dB rebuilds the input exactly (masks sum to 1).
    python3 anthem_remix.py IN.wav OUT.wav [--hook-db 2.5] [--breath-db -4]"""
import argparse, wave, numpy as np
from scipy.signal import stft, istft
from scipy.ndimage import median_filter
ap = argparse.ArgumentParser(); ap.add_argument("i"); ap.add_argument("o")
ap.add_argument("--hook-db", type=float, default=2.5); ap.add_argument("--answer-db", type=float, default=2.0)
ap.add_argument("--breath-db", type=float, default=-4.0); ap.add_argument("--rise-db", type=float, default=-1.5)
a = ap.parse_args()
w = wave.open(a.i); sr = w.getframerate(); ch = w.getnchannels(); sw = w.getsampwidth()
raw = w.readframes(w.getnframes()); w.close()
x = (np.frombuffer(raw, "<i2").astype(float) / 32768 if sw == 2 else
     (np.frombuffer(raw, np.uint8).reshape(-1, 3) @ np.array([1, 256, 65536])).astype(float)).reshape(-1, ch)
if sw == 3: x = np.where(x >= 2**23, x - 2**24, x) / 2**23
N, HOP = 4096, 1024
def env(points, t):  # piecewise-linear dB curve
    tt, vv = zip(*points); return np.interp(t, tt, vv)
out = np.zeros_like(x)
for c in range(ch):
    f, t, Z = stft(x[:, c], sr, nperseg=N, noverlap=N - HOP)
    M = np.abs(Z) ** 2
    Hm = median_filter(M, size=(1, 17)); Pm = median_filter(M, size=(17, 1))
    mask = Hm ** 2 / (Hm ** 2 + Pm ** 2 + 1e-30)
    H, P = Z * mask, Z * (1 - mask)
    hd = env([(0, 0), (45.0, 0), (45.03, a.rise_db), (55.5, 0), (56.40, 0), (56.47, a.breath_db), (57.0, a.breath_db),
              (57.03, a.hook_db), (69.0, a.hook_db), (69.3, a.answer_db), (81.0, a.answer_db), (82.0, 0), (999, 0)], t)
    pres = env([(0, 0), (56.97, 0), (57.0, 2.0), (69.0, 2.0), (69.3, 1.5), (81.0, 1.5), (82.0, 0), (999, 0)], t)
    band = ((f >= 1200) & (f <= 3500)).astype(float)[:, None]
    gH = 10 ** ((hd[None, :] + band * pres[None, :]) / 20)
    _, y = istft(H * gH + P, sr, nperseg=N, noverlap=N - HOP)
    out[:, c] = y[:len(x)] if len(y) >= len(x) else np.pad(y, (0, len(x) - len(y)))
pk = np.abs(out).max()
if pk > 0.98: out *= 0.98 / pk
w = wave.open(a.o, "wb"); w.setnchannels(ch); w.setsampwidth(2); w.setframerate(sr)
w.writeframes((out * 32767).astype("<i2").tobytes()); w.close(); print("ok", a.o, f"peak {pk:.3f}")
