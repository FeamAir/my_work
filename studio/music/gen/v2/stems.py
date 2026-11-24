"""Median-filter HPSS split (same method as anthem_remix.py, r4) -> IN_H.wav (harmonic) + IN_P.wav (percussive).
H + P == IN.  python3 stems.py IN.(mp3|wav) OUTDIR"""
import sys, os, wave, numpy as np
from scipy.signal import stft, istft
from scipy.ndimage import median_filter
sys.path.insert(0, os.path.dirname(__file__))
from a2lib import load, SR
src, od = sys.argv[1], sys.argv[2]; os.makedirs(od, exist_ok=True)
x = load(src, mono=False); N, HOP = 4096, 1024
H = np.zeros_like(x); P = np.zeros_like(x)
for c in range(2):
    f, t, Z = stft(x[:, c], SR, nperseg=N, noverlap=N - HOP)
    M = np.abs(Z) ** 2
    Hm = median_filter(M, size=(1, 17)); Pm = median_filter(M, size=(17, 1))
    m = Hm ** 2 / (Hm ** 2 + Pm ** 2 + 1e-30)
    for Y, msk in ((H, m), (P, 1 - m)):
        _, y = istft(Z * msk, SR, nperseg=N, noverlap=N - HOP)
        Y[:, c] = y[:len(x)] if len(y) >= len(x) else np.pad(y, (0, len(x) - len(y)))
def save(p, y):
    w = wave.open(p, "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(y, -1, 1) * 32767).astype("<i2").tobytes()); w.close()
b = os.path.splitext(os.path.basename(src))[0]
save(f"{od}/{b}_H.wav", H); save(f"{od}/{b}_P.wav", P); print("ok", od, b)
