# S01E01 animatic v2: director's notes (the 21:30 cut)

Version 2 · 2026-11-24 · author: director (режиссёр-постановщик) · basis: the studio director's decisions on animatic v1
File: `output/S01E01/animatic/S01E01_animatic_v2.mp4` (R2 `S01E01/animatic/S01E01_animatic_v2.mp4`), 1280×720, 24 fps. Internal only.
Shot list: `shotlists/S01E01_shotlist.md` (v2, re-timed; cut shots are struck through with the reason). Machine version: `output/S01E01/animatic/spec/shots_v2.json`.
Tools: `animatic_tools/cut_v2.py` (cut + re-time + LA of changed shots), `animatic_tools/restage_v2.py` (the 2 restaged frames), `animatic_tools/spec.py` (`ANIM_V=v2`: build / assemble / master / overlay).

## 1. Result

| | v1 | v2 |
|---|---|---|
| Runtime | 28:18.75 | **21:29.75** (target 21:30, max 22:30) |
| Shots | 451 | 386 (65 cut, 264 re-timed or restaged, 122 untouched) |
| Hook 0:08 cradle / 0:30 five notes | ✓ / ✓ | ✓ / ✓ (0:00–0:30 untouched) |
| **"The stone answers" (sc03-sh220)** | 3:20 | **2:58.25** (the hum and SDH "[a low hum answers]" on screen at 2:58–3:01) |
| Loudness (final mp4) | −14.1 LUFS, −1.3 dBTP, LRA 21.2 | **−14.7 LUFS, −1.6 dBTP, LRA 10.9 LU** |
| Paid | — | $0.16 (2 NB2 /edit takes) |

Scene starts in v2: Sc1 0:00 · Sc2 1:06 · Sc3 2:07.8 · Sc4 3:42.8 · **Sc5 (Chronicler, title) 5:05.5** · Sc6 5:59 · Sc7 6:57.5 · Sc8 7:38.8 · Sc9 8:23.2 · Sc13 9:32.8 · Sc10 10:25.2 · Sc14 11:51.8 · Sc11 12:32.8 · Sc15 13:16.2 · Sc15a 14:20.5 · Sc12 14:53.2 · Sc16 16:46 · Sc17 17:36 · Sc18 18:11 · Sc19 18:51.5 · Sc20 20:16.5–21:29.75.
Pell's longest absence is now about 5:00 (9:2x roof → 14:20 Sc 15a); in v1 it was about 7.

| Scene | v1 s | v2 s | Δ | Scene | v1 s | v2 s | Δ |
|---|---|---|---|---|---|---|---|
| sc01 | 70.0 | 66.0 | −4.0 | sc11 | 63.2 | 43.5 | −19.8 |
| sc02 | 66.2 | 61.8 | −4.5 | sc15 | 92.5 | 64.3 | −28.3 |
| sc03 | 124.0 | 95.0 | −29.0 | sc15a | 35.0 | 32.8 | −2.3 |
| sc04 | 100.2 | 82.8 | −17.5 | sc12 | 155.5 | 112.8 | −42.8 |
| sc05 | 60.8 | 53.5 | −7.3 | sc16 | 75.0 | 50.0 | −25.0 |
| sc06 | 71.2 | 58.5 | −12.8 | sc17 | 45.0 | 35.0 | −10.0 |
| sc07 | 44.8 | 41.3 | −3.5 | sc18 | 45.0 | 40.5 | −4.5 |
| sc08 | 68.5 | 44.5 | −24.0 | sc19 | 109.8 | 85.0 | −24.8 |
| sc09 | 110.0 | 69.5 | −40.5 | sc20 | 90.0 | 73.3 | −16.8 |
| sc13 | 77.5 | 52.5 | −25.0 | | | | |
| sc10 | 134.5 | 86.5 | −48.0 | **Total** | **1698.8** | **1289.8** | **−409.0** |

(Exact per-shot values are in the shot list; the table is rounded to 0.1 s.)

## 2. How the cut was made (rules)

1. **Kept whole:** every story beat; every plant in `story/episodes/S01E01/continuity_check.md` §4 (the stone, the cord, "six coppers", the whistle, "Whoever reads that map…" / "Who reads the map now?", Pell is fifteen (L020 kept for it), "not since—", the net-chest, the flat Sluice Spire, the fork and the throat, the knuckle and the blood, the left-hand clasp and the ring insert, the cup, Juno alive, the petition, the second sheet under the blotter, the hare's-ear pin leaving, Maren's back, ACCOUNT NINE, 1,470 / 1,740 (3 s each), "Not yet reconciled", the clip into the LEFT pocket, Ursel writing through the tone, the unsigned map, thirty days, the Sc 1 / Sc 18 hands, Mags outside the wall, the whistle in Sc 20); every FIXED and [ECHO] line; every Chronicler line in full; all five lip-sync CUs; all match cuts.
2. **Protected durations (unchanged):** 0:00–0:30 of Sc 1, the baby's two notes and the sleeve, the pool from the hum to the rings (sh170–sh230), the 3 s silence after Nan's hand, the fall and the 4 s of silence after it, the Sc 1/18 hand shots, Sc 20 from the stone in her hand to black.
3. **Cut first:** silent holds (compressed per scene to 70–90 %, never below 1.5 s or the kept speech + 0.55 s), then repeated reactions and re-used set-ups (65 shots). The cut list with a reason per shot is in `cut_v2.py` (`DROP`) and in the shot list.
4. **Director's named cuts:** Sc 10 −48 s and Sc 12 −43 s (repeated wides/OTS, the door-warden beat, second reactions, the cuttable veiled figure); Sc 3 walk-up (sh020, sh050 cut, flats and approach trimmed: −12.5 s before the hook); Sc 9 the two 10-s hero shots (sh030 Ione, sh060 harbour → glass) to 6 s each, the 10-s fade sh170 to 6 s.

### VO cuts (existing draft audio only, no re-generation, no mid-line edits)

| Line | Shot | Who | Text | Why it can go |
|---|---|---|---|---|
| L021 | sc04-sh050 | Nan | "And don't tell me what you found, I can see from here it was nothing." | comic set-up; the Wick near-blurt gag (L022/L023 + the kick) still plays |
| L039 | sc06-sh100 | Corr | "I've forty grown backs it doesn't care about, ahead of you." | the FIXED line before it (L038) carries the point |
| L058 | sc10-sh100 | Ruel | "And that girl of yours? Still climbing my rigging…" | charm beat; "the man you'd follow into a boat" stays on the faces that smile (sh120) |

All other 102 lines play as in v1 (L080 echo of L079 included). **For the sound director** (`studio/sound/S01E01_vo_plan.json` / `_durations.csv` / `_manifest.json`): mark L021, L039, L058 as "cut in v2 (picture)"; do not record them for finals unless the lead writer restores them. Files stay in `output/S01E01/animatic/vo/`.

## 3. Restaging of the two refused child shots (FOR THE LEAD WRITER'S CANON APPROVAL)

The v1 prompts were not reworded. The beats are restaged so that they read through implication, and the child is not shown in that state. The new frames were generated normally on NB2 /edit, one take each, and both were accepted.

**A. Sc 2, Wick upside down (sc02-sh050, plus sh070 and sh080 that cut with it).**
- Proposed script change, replacing "WICK drops into frame upside down, hanging by his knees from the rope-bridge over the door": *The rope-bridge over Nan's door creaks and bows under a weight we don't see. Grit and drops of water fall past the collector, who doesn't look up. WICK [OS, from above]: "Nan's drowned."*
- sh070 (L005 "Drowned again…") re-uses the same frame, with Wick still [OS] from the bridge and the rope swaying. In sh080, Nan [OS] says "Get down off that bridge!" over a push-in to the dark doorway. That line now pays the joke without the picture. The v1 sh080 frame, which showed his dangling arms, is retired so all three shots follow one consistent rule.
- Wick is first seen in sh200 ("looks at the drop, at the ladder"), the right way up. Nothing in the canon depends on seeing him hang.
- Frame: `frames/sc02-sh050_a.png` (take 1 of 1).

**B. Sc 4, after Nan's hand (sc04-sh180), replacing the finger marks around Wick's mouth.**
- Proposed script change, replacing "She takes her hand away. Marks of her fingers round his mouth. Wick is not joking": *She takes her hand away and lays it flat on the table, fingers pressed hard into the wood to stop them shaking. Beside it, the net-needle. Across the board, Wick's crust lies where he dropped it. Wick is not joking now.*
- The beat is the same: the force of the fear. It now plays on the adult's hand and on an object, with the 3-s silence before it unchanged. The shot gets an insert of Nan's hand only. Her face and Wick's are not in it.
- Frame: `frames/sc04-sh180_a.png` (take 1 of 1).

Both are marked **RESTAGE** in the shot list. Until the lead writer approves, they count as the director's proposal. The v1 placeholders are in `frames_rejected/*_v1placeholder.png`. **Canon keeper:** neither restaging changes a fact. Script wording for the two action lines is the writer's call.

## 4. Conflicts with the lead writer's rules (need the writer's ruling, not changed by me)

1. `beat_sheet.md` §3 says to "never cut anything in 0:00–5:20" and limits trims to Sc 8/13/17. The studio director's 21:30 decision overrides this. Sc 1 after 0:30 lost −4 s, Sc 2 −4.5 s, Sc 3 −29 s and Sc 4 −17.5 s, with no beat or line lost except L021. Sc 7, 15a and 18 got light hold trims only, and no shot was cut from them.
2. **The Chronicler now starts at 5:05.5.** `beat_sheet.md` says "none before 5:20" (and production notes v1.1, "never before 5:55", come from the 29-min version). The intent still holds, because he enters only after the whole cold open. The minute mark has moved because the cold open is shorter. Please restate the rule as "not before the end of Sc 4".
3. The restaging in §3.

## 5. Sound / loudness

- The assemble.py premix measured LRA 21.5 LU, so loudnorm fell back to dynamic mode (same as v1). New `spec.py master` step: one broadband compressor (3:1 under −30 dBFS, attack 20 ms, release 300 ms, +4 dB makeup) on the premix, then 2-pass loudnorm −14 LUFS / −1.5 dBTP. Result on the final mp4: **−14.7 LUFS, −1.6 dBTP, LRA 10.9 LU** (−0.6 dB of headroom kept from the v1 AAC fix). Pass 2 still ran dynamic loudnorm, because the compressed premix needed +10 dB, more than linear mode allows within the TP limit. For finals, the mix engineer should put a limiter before loudnorm so it stays linear.
- Cues on cut shots moved to the next kept shot in the scene. Ambience/music spans end on the last kept shot. No new SFX and no VO generated.
- `pipeline/assemble.py` path as in v1 (LA clips concatenated losslessly first): `la_concat_v2.mp4` = la/ (122 untouched) + la_v2/ (264 re-rendered).

## 6. Final visual stage estimate, trimmed cut (verified prices, `pipeline/costs.py`)

Assumptions as in v1: Kling bills 5 s per clip ≤ 5 s and 10 s above; takes are key frames 2, B 1.5, C 2, D 2.5, E 2. Unique clips in v2: A 256 · B 70 · C 42 · D 8 · E 5.

| Item | Calculation | $ |
|---|---|---|
| Key frames NB2 | 273 (unique frames in v2 minus 22 plates) × 2 × $0.08 | 43.7 |
| End frames NB2 (C/D) | 47 × 1.5 × $0.08 | 5.6 |
| B on Kling 2.5 TP | 370 billed s × 1.5 × $0.07 | 38.9 |
| C on Kling 2.5 TP | 235 billed s × 2 × $0.07 | 32.9 |
| D on Kling 3 Pro | 55 billed s × 2.5 × $0.112 | 15.4 |
| E base clips on Kling 2.5 TP | 30 billed s × 2 × $0.07 | 4.2 |
| E lipsync | price not verified (model_choice upper bound) | ≈ 10 |
| **Total** |  | **≈ $151** |

**Correction to the v1 notes:** I predicted that a 21-min cut would save about $40, but the real saving is only about $10. Most of the cut came out of A-class holds and shorter shots, and that does not change the per-clip Kling billing. Shots that were cut are mostly re-use frames. All C, D and E shots survive, because they are the action and the money shots.
Further savings: run every B/C/D/E shot of 6 s or less on a 5-s clip with a 1-s hold, which brings billed seconds to B 360 / C 230 / D 40 / E 25 (≈ −$6). Reclassify the 3 D shots that are LA-sufficient (≈ −$4). Use MiniMax for plain B CUs (≈ −$9). With all three, the total is about **$132**. The upper bound with 3 takes everywhere is about $205.

## 7. Cost of this step

fal $0.16 (2 × NB2 /edit, one take each; limit was 3 each). Studio total by `output/costs.jsonl`: **$51.83** (backed up to `studio/budget/costs.jsonl`). Nothing else was paid. ElevenLabs: 0 credits.

## 8. Open

- Lead writer: restaging §3, rules §4.1–4.2, and confirmation of the three VO cuts.
- Director/investor: viewing v2. If approved, this is picture lock, and the shot list status becomes `animatic-ok`.
- v1 notes §3 per-scene fixes for finals still apply (Corr side test, the Pell braid wording, no glow, sh070 eyes, etc.).
