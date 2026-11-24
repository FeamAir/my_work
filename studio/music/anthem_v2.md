# OP anthem v2: the Call (melody guide, logo sting, A/B note)

Version 1.0 · 2026-11-24 · composer (r5) · status: **two candidates, waiting for a listening test** (director / investor)

Files: `output/music/lib_mus_theme-op-anthem_v2_candA.mp3`, `…_candB.mp3` (+ `_phone.wav`),
`output/music/lib_mus_theme-op-anthem_v2_sting.mp3` / `.wav` (3.0 s). R2: `music/S01/`.
Guide: `studio/music/gen/v2/anthem_v2_call_guide.mid` (notation, generation key F minor) and the rendered guide
`output/music/guide/anthem_v2_call_guide_Fm.wav` (R2 `music/S01/guide/`).

## 1. The Call (melody guide)

Key F-sharp minor, 80 BPM, 4/4, bar = 3.0 s. Generation happens in F minor and the result is shifted up one
semitone, as it has been since r4. The notes below are in the final key.

The idea comes from the canon "growing leap" (`main_theme.md` §2): **a short low note, an octave leap up to a long
note, then a fall by steps**. The canon hook (C♯4 → C♯5 | B4 A4 G♯4 A4) becomes a 4-bar sentence that lands home:

```abc
X:1
T:The Call (OP anthem v2)
M:4/4
L:1/8
Q:1/4=80
K:F#m
"F#m"C2 c6 | "D"B A "E"G2 "F#m"A4 | "F#m"C2 c3 "D"d c2 | "Bm"B2 A2 "F#m"F4 |]
%% Answer (1:09): bars 1-2 the same, then the leap climbs to E and ends open on the dominant
"F#m"C2 c6 | "D"B A "E"G2 "F#m"A4 | "E"E2 e6 | "D"d c "Bm"B2 "C#"c4 |]
%% Logo (1:21-1:22.5): C# -> C#' on the C# chord, then the resolving leap F# -> F#' on F#m
```

- Range C♯4–E5, so it sits in the middle of the phone speaker band (director's rule). Everyone can sing the leap.
- No A♯ (reserved tone), no F♯ major or Picardy third, no drone below F♯2. The verifier shows the A♯ share at
  0.017–0.032 in the hook, answer and logo.
- Where it plays:
  - **0:00** — a tutti hit, and the horns call it right on the hit (intro, 4 bars).
  - **0:57.0** — full brass in unison, violins an octave above, timpani on downbeats (the drop).
  - **1:09.0** — it returns; the second leap climbs a tone higher and ends open.
  - **1:21.0 / 1:22.5** — the logo: two octave leaps, C♯→C♯ (question), then F♯→F♯ (answer, tonic).

## 2. Logo sting (sonic signature)

**Hit at 1:22.542** (frame 1981), with brass playing F♯4 → F♯5 over an F♯ minor chord. The chord **rings and
resolves**:
- momentary loudness stays −11.5…−14 LUFS until 85.5 s;
- then a natural ring-out of −7 dB over 85.2–86.5 s, and the existing fade 86.5–87.0.

Before (v1a), the anthem was at −38 LUFS by 84 s.

Separate file `…_v2_sting.mp3/.wav`:
- 3.0 s, cut 82.50–85.50 s of candidate A;
- hit at 0.045 s, ring, 0.9 s fade;
- −13.8 LUFS-I, true peak −3.5 dBTP.

For bumpers, socials, the platform logo and the end of trailers.

## 3. A/B: what changed against v1a

| | v1a (r4) | **cand A** | **cand B** |
|---|---|---|---|
| 0:00 | silence → cello, M −32 LUFS in the first 0.4 s | tutti hit + horn Call, M −15.9…−16.4 | same as A |
| intro 0–12 | soft cello solo | horns play the full Call (+4 dB lift after the hit) | same as A |
| groove / theme / rise 12–57 | take2 s8032 | **new take1 s8041** (one generation with the new intro; groove kept, theme close to master, not identical) | **exactly the approved v1a material** (s8032 12–57 s) |
| drop 0:57 | master motif, no octave | **the Call, octave leap**, guide strength high (take2 s8042) | **the Call**, guide strength medium (take3 s8043, a bit freer and more "played") |
| 1:09 | answer | Call returns, climbs to E (take2) | Call returns (take3) |
| logo 1:22.5 | hit, then fades to silence | hit + F♯→F♯ leap, chord rings | same as A (take2 logo) |
| hits (target 57.042 / 69.042 / 82.542) | 57.11 / 69.12 / 82.525 | **57.040 / 69.045 / 82.550** | **57.040 / 69.040 / 82.550** |
| LUFS-I / TP | −13.9 / −1.7 | −13.9 / −1.7 | −13.9 / −1.7 |

Kept in both:
- tempo 80 BPM and length 87.0 s;
- the drum-reinforcement layer from r4 (same samples and hall);
- the approved groove's percussive layer under the drop (s8032, −4 dB).

New in both:
- a 0.2 s "breath" (−7 / −5…−8 dB) right before 0:57 and 1:09, so each hit lands as the clear attack on its frame.

## 4. How it was made (reproducible, see `gen/v2/`)

1. `make_guide.py`: MIDI of the Call → fluidsynth (FluidR3_GM), mixed with the HPSS stems of take2 s8032
   (`stems.py`). The upload guide is 42 s: guide 0–12 s + 57–87 s.
2. `upload_guide.py`: guarded upload to `/v1/music/upload` (same C1–C4 guards as `run_music.py`, imported).
3. `make_v2_plans.py` + `run_music.py`:
   - plan `a`: full 87 s, take1;
   - plans `h1` / `h2`: 33 s, starting at 0:57, takes 2 and 3.

   Lesson: the first chunk follows its reference almost exactly (chroma similarity 0.98–0.99). Later chunks drift
   back to the context (0.33–0.39). So the drop got its own generation, in which it is the first chunk.
4. `assemble_v2.py` → `finish_v2.sh`:
   - `anthem_finish.sh` from r4;
   - `quantize_onsets.py`;
   - `duck_hits.py`;
   - the logo ring-out.

   Then `make_sting.sh`.
5. Checks: `check_v2.py` and `op_verify.py`.
