#!/usr/bin/env python3
"""Saga OP v1.2 audio ($0, numpy/scipy only; no API call). From anthem v1a (output/music/lib_mus_theme-op-anthem_v1a.mp3):
  * the v1a stems by the composer's own method (gen/anthem_remix.py: soft-mask median HPSS, N=4096, hop 1024; H + P with
    unit gains rebuilds the input);
  * a HIT at 0:00: the percussive stem of the 0:57 taiko strike (57.06-58.6 s of v1a, its onset 57.11) laid at 0.00 so
    its attack lands on frame 0-1, with the harmonic stem's low band (< 220 Hz) of the same strike for body; 1.3 s decay;
  * the intro +5 dB (0-9.0 s, A01a-A04b), back to 0 dB over 9.0-12.0 s (the groove from 0:12 untouched);
  * hits 1369/1657/1981 untouched (the music after 12 s is v1a sample for sample, times a constant gain);
  * one constant gain to -14.0 LUFS integrated; a 4x oversampled look-ahead peak limiter only if the true peak > -1.2 dBTP.
    python3 -I op_saga_audio_v12.py OUT.wav [--src ANTHEM] [--no-hit] [--intro-db 0]
Parametric (coordinator 2026-11-24): a new anthem with its own 0:00 hit goes in with --src NEW --no-hit --intro-db 0
(only the -14 LUFS / TP step runs); the picture is never re-edited for it (op_saga_build_c12.py master --audio OUT.wav)."""
import json, re, subprocess, sys
import numpy as np
from scipy.signal import stft, istft, butter, sosfiltfilt, resample_poly
from scipy.ndimage import median_filter, maximum_filter1d

ROOT = "/home/user/my_work"
SRC = f"{ROOT}/output/music/lib_mus_theme-op-anthem_v1a.mp3"
SR, TOTAL = 48000, 87.0
HIT_SRC, HIT_PRE, HIT_LEN = 57.11, 0.05, 1.55        # v1a onset of the 0:57 strike; window starts 50 ms before it
INTRO_DB, INTRO_END, INTRO_BACK = 5.0, 9.0, 12.0
FADE_ST, FADE_D = 86.5, 0.5


def load(src=SRC):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-t", str(TOTAL), "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64)
    n = int(TOTAL * SR)
    return np.pad(x, ((0, max(0, n - len(x))), (0, 0)))[:n]


def hpss(seg):
    N, HOP = 4096, 1024
    H, P = np.zeros_like(seg), np.zeros_like(seg)
    for c in range(seg.shape[1]):
        f, t, Z = stft(seg[:, c], SR, nperseg=N, noverlap=N - HOP)
        M = np.abs(Z) ** 2
        Hm, Pm = median_filter(M, size=(1, 17)), median_filter(M, size=(17, 1))
        m = Hm ** 2 / (Hm ** 2 + Pm ** 2 + 1e-30)
        for Zx, dst in ((Z * m, H), (Z * (1 - m), P)):
            _, y = istft(Zx, SR, nperseg=N, noverlap=N - HOP)
            dst[:, c] = y[:len(seg)] if len(y) >= len(seg) else np.pad(y, (0, len(seg) - len(y)))
    return H, P


def lufs(x):
    p = subprocess.run(["ffmpeg", "-hide_banner", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-af", "ebur128=peak=true",
                        "-f", "null", "-"], input=x.astype(np.float32).tobytes(), capture_output=True).stderr.decode()
    i = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", p)[-1])
    tp = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", p)[-1])
    return i, tp


def true_peak_env(x, os_=4):
    up = resample_poly(x, os_, 1, axis=0)
    a = np.abs(up).max(1)
    return a.reshape(-1, os_).max(1)[:len(x)]


def limit(x, ceil_db=-1.3, look=0.004, rel=0.08):
    c = 10 ** (ceil_db / 20)
    pk = true_peak_env(x)
    g = np.minimum(1.0, c / np.maximum(pk, 1e-9))
    L = int(look * SR)
    g = -maximum_filter1d(-g, size=2 * L + 1)                   # look-ahead: the min over the window
    a = np.exp(-1 / (rel * SR))
    out = np.empty_like(g)
    cur = 1.0
    for i, v in enumerate(g):                                   # instant attack (already looked ahead), slow release
        cur = v if v < cur else v + (cur - v) * a
        out[i] = cur
    return x * out[:, None], float(out.min())


def main(dst, src=SRC, with_hit=True, intro_db=INTRO_DB):
    x = load(src)
    n = len(x)
    t = np.arange(n) / SR
    # 1. the hit at 0:00 from the v1a stems of the 0:57 strike
    a0 = int((HIT_SRC - HIT_PRE - 1.0) * SR)                   # 1 s of context before for a clean HPSS
    seg = x[a0:a0 + int((HIT_LEN + 1.0 + 1.0) * SR)]
    Hs, Ps = hpss(seg)
    s0 = int(1.0 * SR)
    m = int(HIT_LEN * SR)
    sos = butter(4, 220, "lowpass", fs=SR, output="sos")
    hit = Ps[s0:s0 + m] + 0.8 * sosfiltfilt(sos, Hs[s0:s0 + m], axis=0)
    tt = np.arange(m) / SR
    env = np.minimum(1, tt / 0.004) * np.where(tt < 0.35, 1.0, np.exp(-(tt - 0.35) / 0.32))
    hit *= env[:, None] * (1.0 if with_hit else 0.0)
    # 2. intro +5 dB, back to 0 over 9-12 s
    gdb = np.interp(t, [0, INTRO_END, INTRO_BACK, TOTAL], [intro_db, intro_db, 0, 0])
    y = x * (10 ** (gdb / 20))[:, None]
    y[:m] += hit * 1.0
    # 3. fade as the picture
    y *= np.clip((FADE_ST + FADE_D - t) / FADE_D, 0, 1)[:, None]
    # 4. constant gain to -14 LUFS, limiter only if needed, re-measure
    i, tp = lufs(y)
    y *= 10 ** ((-14.0 - i) / 20)
    i2, tp2 = lufs(y)
    gr = 1.0
    if tp2 > -1.2:
        y, gr = limit(y)
        i3, _ = lufs(y)
        y *= 10 ** ((-14.0 - i3) / 20)
        y, gr2 = limit(y)
        gr = min(gr, gr2)
    i4, tp4 = lufs(y)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_s24le", dst],
                   input=y.astype(np.float32).tobytes(), check=True)
    rep = {"integrated_LUFS": i4, "true_peak_dBFS": tp4, "limiter_min_gain_dB": round(20 * np.log10(gr), 2),
           "hit": f"v1a P+H<220Hz {HIT_SRC - HIT_PRE:.2f}-{HIT_SRC - HIT_PRE + HIT_LEN:.2f} s -> 0.00", "intro_dB": intro_db, "src": src}
    if not with_hit:
        rep["hit"] = "none (the source carries its own)"
    print(json.dumps(rep))
    return rep


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--src", default=SRC)
    ap.add_argument("--no-hit", action="store_true")
    ap.add_argument("--intro-db", type=float, default=INTRO_DB)
    a = ap.parse_args()
    main(a.out, a.src, not a.no_hit, a.intro_db)
