"""Assemble anthem v2 candidates in the generation key (F minor), 87.0 s, before anthem_finish.sh (free, r5).

Splices sit 10 ms before a downbeat attack (equal-power 10 ms crossfade), so every joint is masked by a hit:
  A = take1 s8041 [0-57.0)  + take2 s8042 (hook/answer/logo, guide strength high) [57.0-87)
  B = take1 s8041 [0-12.0)  + approved groove take s8032 [12.0-57.0) (exactly the v1a groove/theme/rise)
      + take3 s8043 (hook/answer, strength medium) [57.0-81.0) + take2 s8042 logo [81.0-87)
The horn call in the intro is lifted +4 dB after the 0:00 hit (0.6-11.85 s).
Under the hook and answer (57-81) both get the approved groove's percussive HPSS layer (s8032_P, -4 dB, moved
+25 ms onto the second-half grid) so the hall drums keep their weight (take2/3 have thin lows: <150 Hz share 9 %).

    python3 assemble_v2.py STEMDIR OUTDIR
"""
import os, sys, wave
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from a2lib import SR, load  # noqa: E402

M = "/home/user/my_work/output/music"
T1, T2, T3 = (f"{M}/lib_mus_theme-op-anthem-v2_take{i}_s804{i}.mp3" for i in (1, 2, 3))
T0 = f"{M}/lib_mus_theme-op-anthem_take2_s8032.mp3"
L = int(87.0 * SR); XF = int(0.010 * SR)


def at(x, start):  # place a (second-half) take whose t=0 is `start` s on the timeline
    y = np.zeros((L, 2)); i = int(round(start * SR)); n = min(len(x), L - i); y[i:i + n] = x[:n]; return y


def full(x):
    y = np.zeros((L, 2)); n = min(len(x), L); y[:n] = x[:n]; return y


def splice(parts):
    """parts: [(signal, t_from)], each used from t_from until the next part's t_from."""
    out = np.zeros((L, 2))
    for k, (sig, t0) in enumerate(parts):
        t1 = parts[k + 1][1] if k + 1 < len(parts) else 87.0
        g = np.zeros(L); a = int(round((t0 - 0.010) * SR)); b = int(round((t1 - 0.010) * SR))
        g[max(a, 0):b] = 1.0
        if k > 0:
            g[a:a + XF] = np.sin(np.linspace(0, np.pi / 2, XF)) ** 2
        if k + 1 < len(parts):
            g[b:b + XF] = np.cos(np.linspace(0, np.pi / 2, XF)) ** 2
        out += sig * g[:, None]
    return out


def groove_under(P, mix):
    g = np.zeros(L); t = np.arange(L) / SR
    g[(t >= 57.0) & (t < 80.6)] = 10 ** (-4 / 20)
    r = (t >= 80.6) & (t < 81.0); g[r] = 10 ** (-4 / 20) * np.linspace(1, 0, r.sum())
    d = int(0.025 * SR); Pd = np.zeros_like(P); Pd[d:] = P[:-d]
    return mix + Pd * g[:, None]


def intro_lift(y, db=4.0):
    """The horn call after the 0:00 hit sits ~8 dB under the groove (take1: M -22..-27); lift 0.45-11.95 s."""
    t = np.arange(L) / SR
    g = np.interp(t, [0, 0.35, 0.6, 11.85, 11.99, 87], [0, 0, db, db, 0, 0])
    return y * (10 ** (g / 20))[:, None]


def save(p, y):
    pk = np.abs(y).max()
    if pk > 0.98: y = y * 0.98 / pk
    w = wave.open(p, "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((y * 32767).astype("<i2").tobytes()); w.close(); print(p, f"peak {pk:.3f}")


def main():
    stems, od = sys.argv[1], sys.argv[2]; os.makedirs(od, exist_ok=True)
    t1, t0 = full(load(T1, mono=False)), full(load(T0, mono=False))
    t2, t3 = at(load(T2, mono=False), 57.0), at(load(T3, mono=False), 57.0)
    P = full(load(f"{stems}/lib_mus_theme-op-anthem_take2_s8032_P.wav", mono=False))
    A = groove_under(P, splice([(t1, 0.0), (t2, 57.0)]))
    B = groove_under(P, splice([(t1, 0.0), (t0, 12.0), (t3, 57.0), (t2, 81.0)]))
    A, B = intro_lift(A), intro_lift(B)
    save(f"{od}/anthem_v2_candA_Fm.wav", A); save(f"{od}/anthem_v2_candB_Fm.wav", B)


if __name__ == "__main__":
    main()
