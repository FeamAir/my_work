"""Anthem v2 melody guide (composer r5, free/local).

Writes the call motif as MIDI (generation key F minor; the finished anthem is shifted +1 semitone to F-sharp minor
like every take since r4), renders it with fluidsynth + FluidR3_GM, and mixes it with the HPSS stems of the
approved groove take (take2 s8032, the source of v1a) into an 87.0 s conditioning guide:

  0-12    intro: tutti hit at 0:00 + horns play the CALL (4 bars), strings under it   (take2 not used)
  12-57   groove / theme / rise: take2 unchanged (harmonic + percussive)                (grid and motif kept)
  57-69   hook: brass unison CALL + violins 8va + chords + timpani, over take2 percussive only
  69-81   answer: the CALL returns, second half climbs (E-flat octave leap) and lands open on C
  81-87   logo: hit 81.0 (C, brass C4->C5) and the biggest hit 82.5 (F minor, brass F4->F5), chord rings out

The CALL (F minor; in the final key read every note +1 semitone: C -> C-sharp etc.):
  | C4 q  C5 h.  | Bb4 e Ab4 e  G4 q  Ab4 h | C4 q  C5 q. Db5 e  C5 q | Bb4 q  Ab4 q  F4 h |
  = canon hook of main_theme.md par.2 (C#4 -> C#5 | B4 A4 G#4 A4), extended to a 4-bar sentence that lands on the tonic.

    python3 make_guide.py TAKE_H.wav TAKE_P.wav OUTDIR
"""
import os, subprocess, sys, wave
import numpy as np
import mido

sys.path.insert(0, os.path.dirname(__file__))
from a2lib import SR, load  # noqa: E402

BPM, OFFSET, LEN = 80, 0.025, 87.0          # take2's measured grid offset (beats land at +25 ms)
SF2 = "/usr/share/sounds/sf2/FluidR3_GM.sf2"
TPB = 480

# --- melody (beats from the phrase start, duration in beats, MIDI note) -------------------------
CALL = [(0, 1, 60), (1, 3, 72),
        (4, .5, 70), (4.5, .5, 68), (5, 1, 67), (6, 2, 68),
        (8, 1, 60), (9, 1.5, 72), (10.5, .5, 73), (11, 1, 72),
        (12, 1, 70), (13, 1, 68), (14, 2, 65)]
ANSWER = CALL[:6] + [(8, 1, 63), (9, 3, 75),
                     (12, .5, 73), (12.5, .5, 72), (13, 1, 70), (14, 2, 72)]
# chords: (beat, length, [notes]) - mid strings voicing; roots go to low brass / basses (never below F2 = 41)
FM, DB, EB, BBM, AB, C = [53, 56, 60], [49, 53, 56], [51, 55, 58], [53, 58, 61], [51, 56, 60], [48, 52, 55]
CALL_CH = [(0, 4, FM), (4, 1, DB), (5, 1, EB), (6, 2, FM), (8, 2, FM), (10, 2, DB), (12, 2, BBM), (14, 2, FM)]
ANS_CH = CALL_CH[:4] + [(8, 4, EB), (12, 1, DB), (13, 1, BBM), (14, 2, C)]
ROOT = {tuple(FM): 41, tuple(DB): 49, tuple(EB): 51, tuple(BBM): 46, tuple(C): 48, tuple(AB): 44}

# GM programs per channel
PROG = {0: 60, 1: 56, 2: 57, 3: 48, 4: 40, 5: 42, 6: 47, 7: 61}  # horn, trumpet, trombone, strings, violin, cello, timpani, brass sect.
DRUM = 9


class Track:
    def __init__(self):
        self.ev = []  # (abs_tick, msg)

    def note(self, ch, beat, dur, n, vel):
        t0 = int(round(beat * TPB)); t1 = int(round((beat + dur) * TPB)) - 8
        self.ev.append((t0, mido.Message("note_on", channel=ch, note=n, velocity=vel)))
        self.ev.append((max(t1, t0 + 10), mido.Message("note_off", channel=ch, note=n, velocity=0)))

    def cc(self, ch, beat, ctl, val):
        self.ev.append((int(round(beat * TPB)), mido.Message("control_change", channel=ch, control=ctl, value=val)))

    def save(self, path):
        mf = mido.MidiFile(ticks_per_beat=TPB); tr = mido.MidiTrack(); mf.tracks.append(tr)
        tr.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(BPM)))
        for ch, p in PROG.items():
            tr.append(mido.Message("program_change", channel=ch, program=p))
            tr.append(mido.Message("control_change", channel=ch, control=7, value=110))
        last = 0
        for t, m in sorted(self.ev, key=lambda e: (e[0], e[1].type == "note_on")):
            tr.append(m.copy(time=t - last)); last = t
        mf.save(path)


def bar(n):  # 1-based bar -> beat
    return (n - 1) * 4


def phrase(T, b0, mel, chords, big=True):
    s = bar(b0)
    v = 118 if big else 104
    for b, d, n in mel:
        T.note(0, s + b, d, n, v)                     # horns
        if big:
            T.note(1, s + b, d, n, v - 6)             # trumpets unison
            T.note(2, s + b, d, n - 12, v - 14)       # trombones octave below
            T.note(4, s + b, d, n + 12, v - 18)       # violins 8va
            T.note(7, s + b, d, n, v - 20)            # brass section glue
    for b, d, ch in chords:
        for n in ch:
            T.note(3, s + b, d, n, 82 if big else 70)
        r = ROOT[tuple(ch)]
        T.note(5, s + b, d, r, 88 if big else 72)      # cellos/basses root (>= F2)
        if big:
            T.note(2, s + b, d, r, 84)


def hit(T, beat, chord, root, vel=127):
    T.note(DRUM, beat, .5, 36, vel); T.note(DRUM, beat, .5, 35, vel)
    T.note(DRUM, beat, 1, 49, min(vel, 112))
    T.note(6, beat, 1, root if root >= 41 else root + 12, vel)  # timpani
    for n in chord:
        T.note(7, beat, .5, n + 12, vel - 10); T.note(3, beat, .5, n, vel - 15)
    T.note(2, beat, .5, root, vel - 10)


def build(mid_path):
    T = Track()
    # intro: hit at 0:00, horns call (solo, strong), strings p; small hit on bar 3
    hit(T, 0, FM, 41, 127)
    phrase(T, 1, CALL, CALL_CH, big=False)
    T.note(1, bar(3), 1, 60, 96); T.note(1, bar(3) + 1, 1.5, 72, 96)    # trumpet joins the 2nd leap
    hit(T, bar(3), FM, 41, 100)
    # hook (bar 20 = 57.0 s) and answer (bar 24 = 69.0 s)
    hit(T, bar(20), FM, 41, 127)
    phrase(T, 20, CALL, CALL_CH)
    hit(T, bar(24), FM, 41, 122)
    phrase(T, 24, ANSWER, ANS_CH)
    for b in range(20, 28):                           # timpani on every downbeat, softer on beat 3
        T.note(6, bar(b), 1, 41, 110); T.note(6, bar(b) + 2, 1, 48, 92)
    # logo: 81.0 hit on C (brass C4 -> C5), 82.5 biggest hit on F minor (brass F4 -> F5), ring to 86
    hit(T, bar(28), C, 48, 118)
    for ch, v in ((0, 118), (1, 112), (7, 100)):
        T.note(ch, bar(28), .5, 60, v); T.note(ch, bar(28) + .5, 1.5, 72, v)
    hit(T, bar(28) + 2, FM, 41, 127)
    for ch, v in ((0, 124), (1, 118), (7, 108)):
        T.note(ch, bar(28) + 2, .5, 65, v); T.note(ch, bar(28) + 2.5, 4.5, 77, v)
    T.note(0, bar(28) + 2.5, 4.5, 65, 110)            # horns hold F4 under the trumpets' F5
    for n in FM + [65, 68, 72]:
        T.note(3, bar(28) + 2, 5, n, 96)                # strings ring the F minor chord
    T.note(5, bar(28) + 2, 5, 41, 96); T.note(2, bar(28) + 2, 4, 53, 96)
    for k in range(6):                                  # timpani roll dying away under the chord
        T.note(6, bar(28) + 3 + k * .25, .25, 41, max(100 - 14 * k, 30))
    T.save(mid_path)


def render(mid, wav):
    subprocess.run(["fluidsynth", "-ni", "-g", "0.6", "-r", str(SR), "-F", wav, SF2, mid], check=True,
                   capture_output=True)




def gains(L, pts):
    t = np.arange(L) / SR; tt, vv = zip(*pts)
    return 10 ** (np.interp(t, tt, vv) / 20)


def main():
    hw, pw, od = sys.argv[1:4]; os.makedirs(od, exist_ok=True)
    mid, raw = f"{od}/anthem_v2_call_guide.mid", f"{od}/guide_orch_raw.wav"
    build(mid); render(mid, raw)
    L = int(LEN * SR)
    o = load(raw, mono=False)
    pad = int(OFFSET * SR)
    orch = np.zeros((L, 2)); seg = o[:L - pad]; orch[pad:pad + len(seg)] = seg
    H = load(hw, mono=False)[:L]; P = load(pw, mono=False)[:L]
    H = np.pad(H, ((0, L - len(H)), (0, 0))); P = np.pad(P, ((0, L - len(P)), (0, 0)))
    # take2 harmonic: off in the intro, full 12-56.4, off from the breath on (my orchestration owns 57-87)
    gH = gains(L, [(0, -90), (11.6, -90), (12.0, 0), (56.35, 0), (56.45, -90), (90, -90)])
    # take2 percussive: off in the intro (it holds only cello attacks there), full after, gone after 83.5
    gP = gains(L, [(0, -90), (11.6, -90), (12.0, 0), (82.4, 0), (83.6, -90), (90, -90)])
    # my orchestration: full in the intro and 56.9-87, silent 12-56.9 (no overlap with take2 harmony)
    gO = gains(L, [(0, 0), (11.9, 0), (12.02, -90), (56.85, -90), (56.95, 0), (90, 0)])
    orch_n = orch / (np.abs(orch).max() + 1e-9)
    mix = H * gH[:, None] + P * gP[:, None] * 1.0 + orch_n * gO[:, None] * 0.85
    mix *= 0.95 / np.abs(mix).max()
    out = f"{od}/anthem_v2_call_guide_Fm.wav"
    w = wave.open(out, "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix * 32767).astype("<i2").tobytes()); w.close()
    print("guide", out, mid)


if __name__ == "__main__":
    main()
