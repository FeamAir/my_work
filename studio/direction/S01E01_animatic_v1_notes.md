# S01E01 animatic v1 — director's notes (studio acceptance)

Version 1 · 2026-11-24 · author: director (режиссёр-постановщик)
File: `output/S01E01/animatic/S01E01_animatic_v1.mp4` (R2 `S01E01/animatic/S01E01_animatic_v1.mp4`), 1280×720, 24 fps.
Internal only (director + studio). Not for the investor, not for marketing.
Procedure: `animatic.md`; resume checklist: `animatic_progress.md`; tools: `animatic_tools/`; contact sheets: `animatic_contacts/`.

## 1. Runtime and structure

- **Runtime: __RUNTIME__** (451 shots, 21 scenes; timed shot list fitted to draft VO = 28:19 picture).
- Loudness: __LOUDNESS__.
- Class split (unique clips): A 312 (1158 s) · B 77 (272 s) · C 42 (174 s) · D 8 (46 s) · E 5 (26 s). 124 shots reuse another shot's key frame.
- **Format conflict, decision needed:** the saga brief targets ~20–21 min episodes; the pilot script/animatic plan was 29:05, VO-fitted picture is 28:19. Either the pilot is a double-length special (state it), or ~7–8 min must come out before picture lock. Candidates to trim (no story loss, director's view): Sc 10 (2:14) and Sc 12 (2:35) council scenes — repeated wide/OTS reuse; Sc 3 (2:04) mud-flat walk-up; Sc 9 (1:50) the two 10-s harbour hero shots could be 6 s; Sc 5 tapestry (1:01) is already tight. Needs the head writer.

| Scene | Shots | Duration (s) | Scene | Shots | Duration (s) |
|---|---|---|---|---|---|
| sc01 | 17 | 70.0 | sc11 | 18 | 63.2 |
| sc02 | 21 | 66.2 | sc12 | 39 | 155.5 |
| sc03 | 38 | 124.0 | sc13 | 18 | 77.5 |
| sc04 | 26 | 100.2 | sc14 | 18 | 60.0 |
| sc05 | 10 | 60.8 | sc15 | 26 | 92.5 |
| sc06 | 23 | 71.2 | sc15a | 10 | 35.0 |
| sc07 | 9 | 44.8 | sc16 | 19 | 75.0 |
| sc08 | 20 | 68.5 | sc17 | 13 | 45.0 |
| sc09 | 18 | 110.0 | sc18 | 12 | 45.0 |
| sc10 | 38 | 134.5 | sc19 | 34 | 109.8 |
|  |  |  | sc20 | 24 | 90.0 |

(Edit order is the episode order: … sc09, sc13, sc10, sc14, sc11, sc15, sc15a, sc12, sc16 …)

## 2. What was made (this stage)

- Frames: 327 unique key frames (`_a`), nano-banana /edit with reference sheets + STYLE_BASE; 22 accepted ref plates used directly ($0); 47 end poses (`_b`) for class C/D. On-screen text (titles, "IX", map labels, "Seventeen years later", HOLLOWSTONE) is drawtext only.
- Review: every scene contact sheet checked by eye against visual bible §11 + the concept artist's known flaws; Pell close-ups checked on a larger zoom sheet. 27 key frames + 4 end poses retaken (≤2 retries each); rejects kept in `output/S01E01/animatic/frames_rejected/`.
- Motion: all 451 shots LA in 720p (push/pull/pan/tilt/shake, rain, lantern flicker, ripple rings, C/D start→end dissolve). Tapestry panels and the wide panel strip are shown whole on a dark ground (no crop).
- MiniMax H3 Max Turbo 768P drafts for 5 class-D shots: **only sc03-sh220 is usable and is cut in**; 4 rejected (see §4).
- Sound: draft VO (dx), 43 ElevenLabs SFX/ambiences, synth placeholders (stone tone, death tone, fork, temp-music pads labelled `[TEMP MUSIC: …]` on screen). Lullaby five notes only in Sc 1 (woman + baby's two notes) and Sc 3 (Pell's three hummed notes); Sc 20 stone tone only, no melody. No other scene calls for the melody.

## 3. Scene-by-scene problems and fixes needed before finals

| Scene | Problem in the animatic | Fix before finals |
|---|---|---|
| sc01 | sh070 eyes in the gate gap read as a pasted square (3 tries; kept original). sh100 underwater frame letterboxed, cloth reads as tentacles. Cradle frames are good. | sh070: build as two layers (gate plate + separate eye CU composited in the gap). sh100: plate-only NB2 with "no letterbox" + LA. |
| sc02 | **sh050 (Wick hanging upside down) and sc04-sh180 (finger marks round Wick's mouth) were refused by the fal content checker** (child character). Placeholders = copies of sc02-sh200 / sc04-sh070. Not reworded to get round the filter. sh150 tall plate → tilt. Pell braid side flipped in sh130/sh140 (retaken; sh140 still ambiguous). | Writer/director decision: restage sh050 (e.g. Wick sitting on the rope-bridge, legs dangling) and sh180 (red cheeks / bread crumbs instead of marks) in the script, then generate normally. |
| sc03 | Pell braid flipped in several MCUs (sh110, sh180 retaken OK; sh290/sh320 wide shots ambiguous). sh130/sh150 had stray people (retaken). sh170 reflection shot draws the face above the water as well as in it. sh220 MiniMax draft good. | Finals: always add the image-relative side wording (`frames.py` `_PELL_SIDE`) to every Pell prompt, not just retakes. sh170: reflection-only composition, generate the water surface top-down. |
| sc04 | Nan's earring correct (left ear) throughout. sh180 placeholder (see sc02). sh220/sh240 braid retaken. | — |
| sc05 | Tapestry plates are final candidates; HOLLOWSTONE title drawtext over panel 6 — fine inside the episode. | Lock plates (`animatic=final-candidate`). |
| sc06 | **Corr's stump** — not reliable: sh040/sh130 retaken, sh130 still unclear which hand holds the whistle; sh190 walker hand fine. sh050 had an inset panel (retaken). | Corr needs a dedicated side-anchor test (2–3 NB2 shots) before finals; image-relative wording ("on the RIGHT side of the picture the forearm ends in a stump"). |
| sc07 | Map inserts good; no text generated. | — |
| sc08 | Ione hair silver from the roots ✓. Spiral grooves on the Spire stair: direction not checkable at thumbnail size. | Check spiral direction on every Spire frame at full size before finals (§11.3). |
| sc09 | sh030 Ione hero: MiniMax lit her up blue-white (glow) → rejected, LA used. sh060 waves→glass by dissolve reads well. sh110 tag on jacket (retaken). | sh030 → Kling 3 Pro with "no light change, she does not glow". |
| sc10 | sh130/sh180 letterbox and drawn boxes (retaken). Ruel ring on the left hand in sh290 — plausible but small. | Check ring hand at full size in finals; ring and shard never in one frame — kept (no shared frames found). |
| sc11 | OK. Lipsync CU sh100 [E] static with subtitles (as planned). | E-class pipeline. |
| sc12 | sh270 letterbox (retaken). Long scene (2:35). | Trim candidate. |
| sc13–14 | sh090 letterbox (retaken); sc14-sh180 glowing rings on the desk (retaken). Hollis's cracked lens rarely visible. | Hollis: mention the cracked lens in every MCU prompt. |
| sc15 | sh160 wrong content (retaken; clip on page reads). | — |
| sc15a | sh050 braid side retaken. | — |
| sc16 | OK. Ink-drop insert sh080 with end pose reads. | — |
| sc17 | sh020 letterbox (retaken). | — |
| sc18 | sh060/sh070 reuse the Sc 1 hands set-up: start/end dissolve is enough. | LA in finals too (no video). |
| sc19 | sh110 end pose duplicated Pell twice (retaken twice). | — |
| sc20 | sh150 hero macro: first frame was a bust (retaken to true macro ✓); **MiniMax made the stone glow orange** → rejected; end pose also glowed (retaken). sh170 glowing lines on Pell's face (retaken). | sh150 → Kling 3 Pro with "the stone stays matte black, nothing glows" + check every frame. |

**Systemic issues (all scenes):**
1. Letterbox bars / inset panels / drawn empty boxes appear in ~3% of NB frames → keep the `_ONE` wording in all final prompts.
2. Pell's braid side flips in about one in four MCUs unless the image-relative wording is used. Tag on jacket appeared once.
3. "Nothing glows" is broken by the video model far more than by stills (4/5 MiniMax drafts added glow). This confirms the video-test result and rules MiniMax out for anything with the shard, the Spire, Ione or night water.

## 4. Recommended class / model per shot type (finals)

| Class | Shots (unique clips) | Model | Note |
|---|---|---|---|
| A — still + LA | 312 | NB2 /edit key frame + ffmpeg LA | 22 ref plates already final candidates |
| B — cheap motion | 77 | **Kling 2.5 Turbo Pro** (default); MiniMax H3MT 768P only for plain character CUs with no light source, shard, Spire or water in frame | MiniMax failed glow rule 4/5 here |
| C — action | 42 | Kling 2.5 Turbo Pro, start frame (+ end frame where supported) | start/end poses from the animatic are the brief |
| D — hero | 8 | Kling 3 Pro; sc03-sh220 may stay on the MiniMax draft quality level if re-rendered at 1080 | sc01-sh050 / sc18-sh060 / sc09-sh060: LA dissolve is enough → reclassify to A/B |
| E — lipsync | 5 | Kling 2.5 TP base + lipsync model (price to verify) | |

## 5. Cost estimate for the final visual stage (verified prices, `pipeline/costs.py`)

Assumptions: Kling bills 5 s per clip ≤ 5 s, 10 s above; takes: key frames 2, B 1.5, C 2, D 2.5, E 2.

| Item | Calculation | $ |
|---|---|---|
| Key frames NB2 | 305 (327 − 22 plates) × 2 × $0.08 | 48.8 |
| End frames NB2 (C/D) | 47 × 1.5 × $0.08 | 5.6 |
| B on Kling 2.5 TP | 420 billed s × 1.5 × $0.07 | 44.1 |
| C on Kling 2.5 TP | 235 billed s × 2 × $0.07 | 32.9 |
| D on Kling 3 Pro | 55 billed s × 2.5 × $0.112 | 15.4 |
| E base clips on Kling 2.5 TP | 30 billed s × 2 × $0.07 | 4.2 |
| E lipsync | price not verified (model_choice upper bound) | ≈ 10 |
| **Total** |  | **≈ $161** |

Savings options: B on MiniMax where allowed (≈ −$10 if half of B qualifies); reclassify the 3 LA-sufficient D shots (−$4); trimming the episode to 21 min cuts every line by ~25% (≈ −$40). Upper bound with 3 takes everywhere ≈ $220.
Current fal balance ≈ $57 → the final stage needs a top-up whatever option is chosen.

## 6. Cost of this stage

See the report `studio/reports/anime-director-2026-11-24.md`.
