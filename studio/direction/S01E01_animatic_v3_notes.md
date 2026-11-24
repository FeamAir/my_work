# S01E01 animatic v3: director's notes (the 19:51 cut)

Version 3 · 2026-11-24 · author: director (режиссёр-постановщик) · basis: animatic v2 + the lead writer's v3 edit decisions (`story/episodes/S01E01/continuity_check.md` §9, binding) + QA / keeper / analyst reviews of v2
File: `output/S01E01/animatic/S01E01_animatic_v3.mp4` (R2 `S01E01/animatic/S01E01_animatic_v3.mp4`), 1280×720, 24 fps, AAC 48 kHz. Internal only.
Shot list: `shotlists/S01E01_shotlist.md` (v3; v2 is in git history). Machine version: `output/S01E01/animatic/spec/shots_v3.json`. Finals rules: `S01E01_finals_checklist.md`.
Tools: `animatic_tools/cut_v3.py` (cut, re-frames, LA of changed shots), `vo_v3.py` (L014 take), `regen_v3.py` (sc20-sh010), `spec.py` (`ANIM_V=v3`), `sound.py bed`, `verify_vo.py` (audio acceptance).

## 1. Result

| | v2 | v3 |
|---|---|---|
| Runtime | 21:29.75 | **19:51.00** (§9 target 19:51.50; −0.5 s, see §3.2) |
| Shots | 386 | **366** (−21 dropped, +1 restored); 69 re-rendered, the rest re-use v2 clips |
| "The stone answers" (sc03-sh220) | 2:58.25 | **2:56.25** |
| L106 "Pell… it's singing back." | missing (−91 dB) | **19:32.70, audible** |
| VO lines in the mix | 102 placed (dx stem 72.7 s early, see §2) | **103 + L080 echo, all on their shots** |
| Loudness (final mp4) | −14.7 LUFS, −1.6 dBTP, LRA 10.9 | see §2.4 |
| Paid | $0.16 | **$0.0893** (1 TTS take + 1 NB2 /edit take) |

Scene starts (v3): Sc1 0:00 · Sc2 1:04.00 · Sc3 2:05.75 · Sc4 3:40.75 · Sc5 5:03.50 · Sc6 5:57.00 · Sc7 6:55.50 · Sc8 7:36.75 · Sc9 8:14.75 · Sc13 9:20.25 · Sc10 10:01.25 · **Sc15a-1 11:21.00** · Sc14 11:31.75 · Sc11 12:11.75 · Sc15 12:48.50 · **Sc15a-2 13:50.75** · Sc12 14:11.75 · Sc16 16:00.75 · Sc17 16:30.75 · Sc18 16:51.25 · Sc19 17:20.75 · Sc20 18:45.75 · end 19:51.00.
Against §9.7: every start from Sc4 on is 0.5 s earlier (L014 shot, §3.2); Sc14 → Sc15 are 2.5 s earlier (sc15a-sh050 stays in 15a-2, §3.3); from Sc15a-2 on it is back to −0.5 s.

## 2. Sound blockers QA A1–A5: root cause and fix

### 2.1 Root cause (in `pipeline/assemble.py`, not in the mix spec)
Every DX item is trimmed (`atrim=start=…`) and then placed on its timecode with `adelay`. In ffmpeg 6.1, `adelay` after a trimmed stream emits its leading silence with **pts = NOPTS**; `amix` drops those frames. The DX stem therefore lost the silence before its first line (L001 at 72.7 s): **the whole dialogue stem played 72.7 s early** and was 72.7 s short (1217.05 s instead of 1289.75 s). FX/AMB/MUS items are not trimmed, so their stems were right.
Consequences in v2 (and v1): every line sat 72.7 s ahead of its picture; L014/L049/L053 measured "20 dB low" only because their windows happened to fall in gaps of the shifted stem; L106 (at 1271.45 s) fell past the stem's end → missing; `amb_ducked` / `mus_ducked` are side-chained from the DX stem and were cut at 1217.05 s → the Sc 20 digital silence. Re-run of my strict check on v2: 57 of 103 lines fail the "line is in the stem at its timecode" test.

### 2.2 Fix (minimal, with test)
- `pipeline/assemble.py`: placement on the timeline is now `adelay=<ms>:all=1,asetpts=N/SR/TB` (`_place()`): the delay's silence gets real timestamps, sample-exact. Same for the CLIP stem. (A first try with `aresample=async` was exact but put each delay into one huge frame and ran out of memory on 103 inputs; the final form peaks at ~110 MB.)
- Guard: after each stem render, `run_plan` checks the stem length equals the picture length (±0.05 s) and stops with an error otherwise.
- Test: `pipeline/tests/test_mix.py::TestStemTimeline::test_trimmed_dx_items_land_on_timecode` (two trimmed DX items at 2.5 s and 6.0 s land within 5 ms; stem = 8.00 s). Command assertion updated in `test_commands_follow_mix_plan`. `python3 -m unittest pipeline.tests.test_mix`: 22 pass; the only failure is the known old `TestSoundPlanBuild::test_spec` (unrelated, listed in HANDOFF).
- **For the IT engineer / sound director:** this changes every future mix built with `assemble.py`; anything mixed before today with trimmed DX items has the same offset.

### 2.3 Other sound changes in v3 (`spec.py v3_sound()`, $0)
- Sc 20 (QA A2): death-tone through the wall at sh010 (−8 dB, low-passed) and again at sh070; the stone answers under the third tone (sh080 + 3.4 s) as a sustained bed (`synth/stone_bed_v1.wav`) that holds to sh230 — the spec's "the hum does not stop"; the house bed now runs the whole scene (stem no longer cut).
- Sc 9: the check found 2.75 s of digital silence at sh080 (v2 had it too): Ione's tone and the Crown Spire hum now hold as beds from sh030/sh040 to sh170 (near until sh100, far after), as the shot list says.
- Sc 15a-1 has its own dusk-tide bed; M07 fades on sc10-sh150 (§9.2).
- QA A7: an SDH cue never starts while a spoken line is on screen (L015 and "[she hums, three notes]" no longer stack).
- L014 new take; L058 restored (existing v2 audio).

### 2.4 Verification (ffmpeg, `animatic_tools/verify_vo.py`, result in `spec/S01E01_animatic_v3_vo_check.json`)
Per VO line, window = spec start … start + duration: RMS and peak in the **final mp4**; presence in `stem_dx.wav` at that timecode (≥ 20 dB over the 0.5 s before it); all stems = 1191.00 s; no 0.5-s window below −80 dBFS outside the planned 1-s black.
RESULT_PLACEHOLDER

## 3. §9 edits as applied

### 3.1 Cuts and trims
All rows of §9.1 and §9.2 applied exactly; `cut_v3.py` asserts every v2 duration in the tables before changing it (all matched). Dropped (21): sc08-sh130, sh190; sc13-sh030, sh040; sc10-sh140, sh380; sc11-sh070, sh170; sc16-sh030, sh090, sh100, sh150, sh170; sc17-sh020, sh050, sh070, sh120; sc18-sh020, sh040; sc20-sh020, sh040. Sound cues on dropped shots move to the next kept shot of the scene (the second round of death-tones now sits under sc16-sh110, as §9.1 asks). No VO line is cut. Each trimmed VO shot still holds its line at its v2 offset + 0.35 s (asserted).

### 3.2 L014 (§9.4)
"Hold the rope, Wick." — one ElevenLabs take (take 1 of max 3): V01_PELL `iXg6m3okqCpdUH3cAzLs`, `eleven_v3`, stability 0.5 / similarity 0.8, seed 101, tag `[whispers]`, dictionary `hollowstone_en_draft_v1` — exactly the v2 take's settings; only the text changed. File `vo/sc03-sh110_L014_V01_PELL_v3.mp3` (+ `.json` record), speech 1.04 s (v2 take 1.16 s), F0 190 Hz (v2 180 Hz); the envelope shows three phrases (hold / the rope / Wick). 31 credits ≈ $0.0093.
The writer's rule "final = max(1.75, speech + 0.55)" gives **1.75 s** (the take is shorter than the old one), so sc03-sh110 keeps its v2 length and the cut is 19:51.00, not 19:51.50. *Not checked by STT (that is another paid call) — the sound director should listen.*

### 3.3 Sc 15a split (§9.3)
The condition was checked first: `sc15a-sh050_a.png` shows a braided cord around her collar running down the chest (her net-bag cord, but it reads as a cord at the collar). By the writer's rule **sh050 stays in 15a-2 (before sh060)** and **Sc 15a-1 = sh020, sh030, sh040 (10.75 s)** after sc10-sh360 / L068. sh020 shows only the net bag on her front, no cord at the collar. 15a-2 = sh010 (L080 echo) · sh050 · sh060 · sh070 (L081) · sh080 (L082) · sh090 · sh100 (3.5). Pell off screen (v3, from shots with her ref): 9:11.3 → 11:21.0 (2:10), 11:28.5 → 13:54.5 (2:26; 2:19 in §9.3 before the sh050 condition), 14:08.3 → Sc 19 at 17:20.8 (3:12). v2: 5:00 and 3:58.

### 3.4 Sc 10 (§9.5, §9.6)
- sc10-sh100 restored after sh080: 5.25 s, frame `sc10-sh090_a.png` (Ruel, door-warden's back), L058 `[MS]` warm. Sound director: L058 back in the manifest as "restored in v3".
- Ring insert sh290 1.5 s, blood bead sh330 1.75 s, Ione sees sh350 2.5 s, no sting; sh340 unchanged.
- Quarrel frames: sh190 = Lucan MCU (`sc10-sh230_a`), sh200 = Ruel (`sc10-sh190_a`), sh230 = Ruel (`sc10-sh190_a`), sh240 = Lucan (`sc10-sh230_a`). Sequence H, R, insert, H-OTS, R, H, two-shot; L060 and L064 marked `[MS]` in the shot data. Ring insert (10:58.25) → the Helm drinks (sc11-sh080, 12:31.75) = 93.5 s, with Sc 15a-1 and Sc 14 between.

### 3.5 Steward frame in Sc 11 (§9.5)
sc11-sh060 (1.75 s) re-uses `sc10-sh040_a.png`: the man by the door, back to camera, waiting with the hall. No action, no line. (Keeper: presence only, no new fact.)

### 3.6 Lore blocker sc05-sh080 and the title
- sc05-sh080 re-built from **tapestry panel 1 only** (`sc05-sh010_a.png`): a slow pull-back from the Queen to the whole panel over the 10.5 s of L033 (zoom 1.30 → 1.00, `cam_override` in `la.py`). Panels 3 and 4 are in no v3 frame together; the v2 strip plate is retired.
- sc05-sh100: **HOLLOWSTONE on plain dark** (no panel under it), 8 s, same type and fade. Panel 6 no longer carries the title anywhere.

### 3.7 Grey-haired Wick (analyst, v2 20:16 and 21:08)
- **sc20-sh180** (21:08 in v2): swapped to the existing `sc20-sh050_a.png` (Wick at the table, lamp-lit, hair reads brown; also loses the glowing wall lines of QA V10). $0.
- **sc20-sh010** (20:16 in v2): no existing night frame has Pell on the chest *and* Wick, so one NB2 /edit (take 1 of max 2) of the v2 frame with the Wick master + turnaround as refs: Wick's hair re-done, tuft on his right temple, glowing wall lines removed, Pell and room unchanged. The take came out ginger-orange with a lamp halo, so instead of a second paid take I pulled the hair to mouse-brown with a local $0 grade (`regen_v3.py grade`: box above the eyes only). v2 frame kept as `frames_rejected/sc20-sh010_a_v2grey.png`. $0.08.

## 4. Not done in the animatic (by instruction) → finals checklist
Corr's stump, Spire light and thread, glowing caustics, Hollis's lens, the clasp hand and sleeve, the Helm's ring, Nan's doorway, map details, banners, Mags's red rag and every other finals item from QA and the keeper are merged per shot in `S01E01_finals_checklist.md`, with the Corr method decision (stage from his left side; 3-image test before finals).

## 5. Cost of this step
ElevenLabs TTS 31 credits ≈ $0.0093 (L014, 1 take of 3 allowed) + fal NB2 /edit $0.08 (sc20-sh010, 1 take of 2 allowed) = **$0.0893**. Studio total by `output/costs.jsonl`: **$51.92** (limit for this run $55). Backed up to `studio/budget/costs.jsonl`.

## 6. Open
- QA: sound re-check of v3 (picture unchanged except the listed re-frames).
- Sound director: listen to the L014 take; L058 "restored in v3" in the manifest; for finals, limiter before loudnorm (pass 2 of the animatic master is still dynamic).
- IT engineer: review the `assemble.py` fix (§2.2); the known `test_spec` failure is unrelated.
- Studio director / investor: viewing v3 → picture lock.
