"""Offline audio measurements for voice casting and VO timing (numpy + ffmpeg only).

    python3 -I studio/sound/tools/audio_measure.py file.mp3 [more.mp3 ...] [--words N]

Reports: raw duration, speech duration (leading/trailing silence trimmed at -40 dBFS rel. peak),
median F0 (autocorrelation, voiced frames only), F0 10–90 % range, voiced share.
These are proxies only — casting choices still need a human listen.
"""
import json, subprocess, sys
import numpy as np

SR = 16000


def load(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(SR),
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def trim_bounds(x, rel_db=-40.0, win=0.02):
    n = int(SR * win)
    if len(x) < n:
        return 0.0, len(x) / SR
    frames = x[: len(x) // n * n].reshape(-1, n)
    rms = np.sqrt((frames ** 2).mean(axis=1) + 1e-12)
    db = 20 * np.log10(rms / (rms.max() + 1e-12))
    idx = np.where(db > rel_db)[0]
    if not len(idx):
        return 0.0, 0.0
    return idx[0] * win, (idx[-1] + 1) * win


def f0_track(x, fmin=60, fmax=520, win=0.05, hop=0.01):
    n, h = int(SR * win), int(SR * hop)
    lag_min, lag_max = int(SR / fmax), int(SR / fmin)
    peak = np.abs(x).max() + 1e-9
    out = []
    for i in range(0, len(x) - n, h):
        fr = x[i:i + n] - x[i:i + n].mean()
        if np.sqrt((fr ** 2).mean()) < 0.03 * peak:
            continue
        ac = np.correlate(fr, fr, "full")[n - 1:]
        if ac[0] <= 0:
            continue
        ac = ac / ac[0] * n / (n - np.arange(n))   # unbiased: no penalty for long lags
        seg = ac[lag_min:lag_max]
        k = int(np.argmax(seg))
        if seg[k] < 0.5:
            continue
        lag = k + lag_min
        # octave-error guard: prefer half lag if nearly as strong
        if lag // 2 >= lag_min and ac[lag // 2] > 0.85 * seg[k]:
            lag //= 2
        out.append(SR / lag)
    return np.array(out)


def measure(path):
    x = load(path)
    s, e = trim_bounds(x)
    f0 = f0_track(x[int(s * SR):int(e * SR)])
    res = {"file": str(path), "dur": round(len(x) / SR, 3), "speech_start": round(float(s), 2),
           "speech_end": round(float(e), 2), "speech_dur": round(float(e - s), 2)}
    if len(f0):
        res.update(f0_med=round(float(np.median(f0)), 1), f0_p10=round(float(np.percentile(f0, 10)), 1),
                   f0_p90=round(float(np.percentile(f0, 90)), 1))
    return res


def semitones(a, b):
    return 12 * np.log2(a / b)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        print(json.dumps(measure(p)))
