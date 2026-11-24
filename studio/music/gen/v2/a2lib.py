"""Shared helpers for the anthem v2 work (composer r5, free/local): load audio via ffmpeg, onset finder,
momentary loudness (ffmpeg ebur128), true peak / integrated LUFS, per-beat chroma."""
import re, subprocess, numpy as np
SR = 48000
FPS = 24
HITS = {"57": 1369 / FPS, "69": 1657 / FPS, "82.5": 1981 / FPS}  # 57.042, 69.042, 82.542


def load(p, mono=True, sr=SR):
    a = ["ffmpeg", "-v", "error", "-i", p, "-ar", str(sr)] + (["-ac", "1"] if mono else ["-ac", "2"]) + ["-f", "f32le", "-"]
    x = np.frombuffer(subprocess.run(a, capture_output=True, check=True).stdout, np.float32).astype(float)
    return x if mono else x.reshape(-1, 2)


def env_db(x, hop=240):
    e = np.sqrt(np.convolve(x ** 2, np.ones(hop) / hop, "same"))[::hop]
    return 20 * np.log10(e + 1e-9), SR / hop


def onset_near(x, t, lo=0.15, hi=0.20):
    """Strongest attack (smoothed rise of the 5 ms energy envelope) in [t-lo, t+hi]."""
    edb, fps = env_db(x)
    d = np.convolve(np.diff(edb, prepend=edb[0]), np.ones(3), "same")
    i0, i1 = max(int((t - lo) * fps), 1), int((t + hi) * fps)
    i = i0 + int(np.argmax(d[i0:i1]))
    pre = x[max(int((t - 0.6) * SR), 0):max(int((t - 0.1) * SR), 1)]
    jump = edb[i:i + int(0.1 * fps)].max() - 10 * np.log10(np.mean(pre ** 2) + 1e-12)
    return i / fps, float(jump)


def momentary(p):
    out = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", p, "-af",
                          "ebur128=metadata=1,ametadata=mode=print:key=lavfi.r128.M:file=-", "-f", "null", "-"],
                         capture_output=True, text=True).stdout
    t = [float(v) for v in re.findall(r"pts_time:([\d.]+)", out)]
    m = [float(v) for v in re.findall(r"lavfi.r128.M=(-?[\d.]+)", out)]
    return np.array(t), np.array(m)


def lufs_tp(p):
    e = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", p, "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1]), float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", e)[-1])


NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def chroma(x, t0, t1, fmin=150, fmax=1500, n=8192):
    w = np.hanning(n); f = np.fft.rfftfreq(n, 1 / SR)
    pc = np.round(12 * np.log2(np.maximum(f, 1) / 440) + 9).astype(int) % 12
    S = sum(np.abs(np.fft.rfft(x[i:i + n] * w)) ** 2 for i in range(int(t0 * SR), max(int(t1 * SR) - n, int(t0 * SR) + 1), 2048))
    m = (f >= fmin) & (f <= fmax)
    prof = np.array([S[m][pc[m] == k].sum() for k in range(12)])
    return prof / (prof.sum() + 1e-12)


def top_pcs(prof, k=4):
    return " ".join(f"{NAMES[i]}{prof[i]:.2f}" for i in np.argsort(prof)[::-1][:k])
