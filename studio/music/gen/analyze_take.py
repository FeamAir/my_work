"""Free 'listening' analysis of a music take (ffmpeg + numpy only, no paid calls).

    python3 studio/music/gen/analyze_take.py TAKE.mp3 [--bar 3.0] [--sections 0,12,24,48,60,72,84,96]

Per bar (3.0 s): level, low-band (<90 Hz) level, onset density, spectral centroid.
Per section: estimated key (Krumhansl-Schmuckler), pitch-class profile with the share of the
reserved tone A-sharp (forbidden in the score), tempo estimate, low-register tonality
(strongest pitch class below 92.5 Hz and how peaked it is: a sustained drone shows up as one
pitch class dominating the sub band across a whole section).
Monophonic sections (solo cello) get a note-by-note pitch track (harmonic-product spectrum),
so the 'short note then leap up' contour can be checked. It is an aid to the ear, not a verdict.
"""
from __future__ import annotations

import argparse
import json
import subprocess

import numpy as np

SR = 22050
PCS = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
MAJ = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
MIN = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])


def load(path: str) -> np.ndarray:
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).astype(np.float64)


def stft(x: np.ndarray, n=8192, hop=2048):
    w = np.hanning(n)
    frames = [x[i:i + n] * w for i in range(0, max(len(x) - n, 1), hop)]
    S = np.abs(np.fft.rfft(np.array(frames), axis=1))
    f = np.fft.rfftfreq(n, 1 / SR)
    t = np.arange(len(frames)) * hop / SR + n / 2 / SR
    return S, f, t


def chroma(S, f, lo=80, hi=2000):
    m = (f >= lo) & (f <= hi)
    pc = np.round(12 * np.log2(f[m] / 440.0) + 9).astype(int) % 12
    C = np.zeros((S.shape[0], 12))
    for k in range(12):
        C[:, k] = (S[:, m][:, pc == k] ** 2).sum(axis=1)
    return C


def key_of(prof):
    best = None
    for r in range(12):
        for name, tpl in (("major", MAJ), ("minor", MIN)):
            c = np.corrcoef(prof, np.roll(tpl, r))[0, 1]
            if best is None or c > best[0]:
                best = (c, f"{PCS[r]} {name}")
    return best[1], round(float(best[0]), 2)


def tempo(x, t0, t1):
    seg = x[int(t0 * SR):int(t1 * SR)]
    hop = 512
    e = np.array([np.sum(seg[i:i + 1024] ** 2) for i in range(0, len(seg) - 1024, hop)])
    on = np.maximum(np.diff(np.log(e + 1e-9)), 0)
    on -= on.mean()
    ac = np.correlate(on, on, "full")[len(on) - 1:]
    fps = SR / hop
    lags = np.arange(len(ac)) / fps
    m = (lags > 60 / 200) & (lags < 60 / 50)
    if not m.any():
        return None
    bpm = 60 / lags[m][np.argmax(ac[m])]
    return round(float(bpm), 1)


def mono_pitch(x, t0, t1):
    """Dominant f0 per 0.1 s (harmonic product spectrum, 130-900 Hz), merged into notes."""
    seg = x[int(t0 * SR):int(t1 * SR)]
    n, hop = 4096, 2205
    out = []
    for i in range(0, len(seg) - n, hop):
        fr = seg[i:i + n] * np.hanning(n)
        if np.sqrt(np.mean(fr ** 2)) < 1e-3:
            out.append(None)
            continue
        sp = np.abs(np.fft.rfft(fr, 4 * n))
        hps = sp.copy()
        for h in (2, 3):
            d = sp[::h]
            hps[:len(d)] *= d
        f = np.fft.rfftfreq(4 * n, 1 / SR)
        m = (f > 130) & (f < 900)
        f0 = f[m][np.argmax(hps[m])]
        out.append(int(round(12 * np.log2(f0 / 440) + 69)))
    notes, cur, cnt = [], None, 0
    for p in out + ["end"]:
        if p == cur:
            cnt += 1
            continue
        if cur is not None and cnt >= 3:  # >= 0.3 s
            notes.append(f"{PCS[cur % 12]}{cur // 12 - 1}:{cnt / 10:.1f}s")
        cur, cnt = p, 1
    return notes


def db(v):
    return round(float(20 * np.log10(v + 1e-12)), 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("take")
    ap.add_argument("--bar", type=float, default=3.0)
    ap.add_argument("--sections", default="")
    ap.add_argument("--mono", default="", help="comma list of t0-t1 ranges for note tracking")
    a = ap.parse_args()
    x = load(a.take)
    dur = len(x) / SR
    S, f, t = stft(x)
    C = chroma(S, f)
    sub = (f > 25) & (f < 92.5)
    bars = []
    for b in range(int(np.ceil(dur / a.bar))):
        t0, t1 = b * a.bar, min((b + 1) * a.bar, dur)
        seg = x[int(t0 * SR):int(t1 * SR)]
        fm = (t >= t0) & (t < t1)
        spec = S[fm].mean(axis=0) if fm.any() else np.zeros_like(f)
        cen = float((spec * f).sum() / (spec.sum() + 1e-12))
        lowshare = float((spec[sub] ** 2).sum() / ((spec ** 2).sum() + 1e-12))
        bars.append({"bar": b + 1, "t": f"{t0:.0f}-{t1:.0f}", "rms_db": db(np.sqrt(np.mean(seg ** 2))),
                     "sub_share_db": db(np.sqrt(lowshare)), "centroid_hz": int(cen)})
    secs = [float(s) for s in a.sections.split(",")] if a.sections else [0, dur]
    sections = []
    for t0, t1 in zip(secs, secs[1:]):
        fm = (t >= t0) & (t < t1)
        prof = C[fm].sum(axis=0)
        prof = prof / (prof.sum() + 1e-12)
        k, conf = key_of(prof)
        subspec = S[fm][:, sub].mean(axis=0)
        sub_pc = np.round(12 * np.log2(f[sub] / 440.0) + 9).astype(int) % 12
        sp = np.array([(subspec[sub_pc == k2] ** 2).sum() for k2 in range(12)])
        sp = sp / (sp.sum() + 1e-12)
        top = np.argsort(prof)[::-1][:5]
        sections.append({"t": f"{t0:.0f}-{t1:.0f}", "key": k, "key_corr": conf,
                         "top_pcs": [f"{PCS[i]} {prof[i]:.2f}" for i in top],
                         "A#_share": round(float(prof[10]), 3),
                         "sub_top_pc": f"{PCS[int(np.argmax(sp))]} {sp.max():.2f}",
                         "tempo_bpm": tempo(x, t0, t1)})
    res = {"file": a.take, "duration_s": round(dur, 2),
           "last_0.5s_db": db(np.sqrt(np.mean(x[-SR // 2:] ** 2))),
           "first_0.2s_db": db(np.sqrt(np.mean(x[:SR // 5] ** 2))),
           "bars": bars, "sections": sections}
    if a.mono:
        res["notes"] = {r: mono_pitch(x, *map(float, r.split("-"))) for r in a.mono.split(",")}
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
