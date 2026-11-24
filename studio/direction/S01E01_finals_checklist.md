# S01E01 — finals checklist (key frames, video, mix)

Version 1.0 · 2026-11-24 · author: director (режиссёр-постановщик) · basis: animatic v3 (19:51.00)
Sources merged: `reports/qa-animatic-v2-2026-11-24.md` (V1–V14, C1–C7, A6, A8), `reports/lore-animatic-v2-2026-11-24.md` (items 1–21), `reports/analyst-animatic-v2-2026-11-24.md` §7 (finals-only items), `continuity_check.md` §9.5–9.6, v1 notes §3 (still open).
**Binding for every finals prompt and for key-frame acceptance.** A prompt that touches a shot below must carry the listed wording; the acceptance check looks at the "check first" item before anything else and rejects the take if it fails. Shot ids are the stable shot-list ids (v3 shot list: `shotlists/S01E01_shotlist.md`). Nothing here changes timing: picture lock stays as v3.

Legend: **[B]** = blocker for that shot (do not generate without it); **[F]** = must-fix in finals; source in brackets.

## 0. Decision: Corr (CH-0048) method — signed

QA V1 / CH-0048 card: the model mirrors the amputation in every frontal portrait (4 of 4), and in v2 sc06-sh090/sh200 show the stump on the wrong arm, sh040 shows two hands.
**Decision:**
1. **Stage Corr from his LEFT side** in every shot where his arms are visible: camera on his left, the LEFT forearm (the one that ends in the wrapped stump) nearest to camera; the whistle in his RIGHT hand, on the far side or in profile. No frontal MS/MCU of Corr with both forearms visible. Prompt wording, image-relative: "seen from his left side; his LEFT forearm, nearest to the camera, ends in a stump wrapped in tarred cloth, no hand on it; the reed whistle is in his RIGHT hand on the far side".
2. **Before finals: a 3-image test** (NB2 /edit, refs = `B05_sheet_v1.png` side view + Sc 6 plate D-03), one take each, one per set-up: sh040 (MS at the wheel), sh090 (MCU, FIXED line L038), sh200 (MS with the whistle). Cost ≈ $0.24, needs the studio director's go-ahead at finals time.
3. Pass = the stump on the LEFT forearm and the whistle in the RIGHT hand in **all 3**. If one fails: that set-up goes to a masked /edit of the stump only (mask on the forearm), not to a re-roll. No paid Sc 6 Corr shot runs before the test passes.

## 1. Rules for every shot (systemic)

| # | Rule (prompt wording / check) | Source |
|---|---|---|
| G1 | **Pell:** image-relative braid wording in every Pell prompt (`frames.py` `_PELL_SIDE`): one braid on her LEFT side (picture-right when she faces us, on her back when seen from behind); in a profile facing picture-right the braid is hidden or behind. Blue tin tag on the braid tip only, never on the jacket. Check the braid side first. | QA V4/V5, v1 notes |
| G2 | **Wick:** hair warm mouse-**brown** — in night / teal-graded shots add "hair reads brown in the lamp light, not grey, not ash, not ginger". ONE tuft at his RIGHT temple (picture-left when he faces us). No cap in E1. | analyst (grey Wick), QA V6 |
| G3 | **Nothing glows:** the shard never glows (only trembling and rings on water); relay stones black; no light veins, crack lines or lightning on walls, floors or faces; night-water caustics are a soft ripple (L-10), never lines. | QA V10/V11, keeper 15, world.md |
| G4 | **Spire light (DEC-69, S1–S4):** only the Crown Spire sings; light runs top-down in the grooves from the crown; the base and the doorway at the foot stay dark, no reflected light below. | QA V8/V9, keeper 13/14 |
| G5 | **Crown Spire thread:** right-hand thread — on the near side the grooves run "/" (lower-left to upper-right). Never fix by mirroring (door, light and west move). Check at full size on every Spire frame. | keeper 11/12 |
| G6 | **Hollis:** crack in his LEFT spectacle lens in every shot where his face reads. | QA V7 |
| G7 | **Ruel:** black pearl ring on his LEFT hand only; deep-blue admiral's coat with silver braid. Ring and shard never in one frame, no split screens. | QA V2, keeper 16, §7 rule |
| G8 | **The Helm (Lucan):** no rings at all on his hands. | QA V3 |
| G9 | **Nan:** one spiral-shell earring, LEFT ear (picture-right); crooked RIGHT little finger readable in hand shots. | keeper 10 |
| G10 | **Frame hygiene:** `_ONE` wording (no letterbox, inset, drawn boxes); no extra people beyond the shot's count; heads not cut by the top edge in MS. | v1 notes, QA V5/V12/V13 |
| G11 | **Heraldry (C-06 hall, banners):** one banner shape — slanted cut, long point at the pole (DEC-66); field colours per house files (Ilvane white/pale violet, Dask ochre, Ostry dark red, Harrow white with green hill, Fennick slate and sulphur); the Choir banner = undyed linen with H-08; Ilvane hand is a RIGHT hand (thumb picture-right with palm visible); Fennick pin = ONE hare's ear (H06_brooch). | keeper 6/7/18 |
| G12 | **Nan's house location:** no open sea through the door or window at eye level — an alley, plank-walks, the dyke wall above the roofs (the Ninth lies below sea level). Sc 4 = grey morning light of the ebb; Sc 20 = night, one lamp on the right. | keeper 9, QA C1 |
| G13 | **Tapestry:** panels 3 and 4 never in one frame; panels 3, 4, 6 never in titles, opening, posters or marketing before S10E10. Fabric fills the frame (no pillarbox). | keeper 1/2, QA C5 |
| G14 | **E-shots (lip-sync):** key frame accepted only after the side checks above; then base clip, then lip-sync. | QA V6 |
| G15 | **Video model:** anything with the shard, a Spire, Ione or night water → Kling (3 Pro for D), never MiniMax (4 of 5 MiniMax drafts added glow). Motion prompt carries "nothing glows, no light change". | v1 notes |
| G16 | **Mix (finals):** limiter before loudnorm so pass 2 stays linear; ride the level jumps in Sc 15 / 15a. | QA A8, A6 |

## 2. Per-shot checklist

| Shot (v3 TC) | Must-fix for finals (prompt / acceptance) | Check first | Source |
|---|---|---|---|
| sc01-sh070 | [F] eyes in the gate gap: build as two layers (gate plate + separate eye CU composited in the gap) | no pasted square | v1 notes |
| sc01-sh100 | [F] underwater plate, no letterbox; the baby's cloth must not read as tentacles | full frame | v1 notes |
| sc02-sh130/140 | [F] Pell braid side (G1) | braid | v1 notes |
| sc02-sh200 | [F] Wick tuft on his RIGHT temple (G2) | tuft | QA V6 |
| sc03-sh110 | [F] Pell MCU, L014 now "Hold the rope, Wick." — mouth small, not looking at the water (G1) | braid | §9.4 |
| sc03-sh170 | [F] reflection-only composition (water surface from above), no second face above the water | one face | v1 notes |
| sc03-sh240 | [F] Pell profile facing picture-right: braid hidden or behind her, not on the near shoulder | braid | QA V4 |
| sc04-sh020, sh040, sh070, sh090 | [F] doorway/window: alley and dyke wall, no sea at eye level (G12) | background | keeper 9 |
| sc04-sh170 | [F] same as above + grey morning light, no pink-violet sunset sky | sky | keeper 9 |
| sc04-sh180 (RESTAGE) | [F] Nan's RIGHT hand, crooked little finger readable; no faces | finger | keeper 10 |
| sc05-sh010 (panel 1) | [F] panel 1 starts at the black tower rising from the woven sea, travel up to the Queen (plate panel0 as start) | tower first | keeper 4 |
| sc05-sh020, sh070 (panel 2) | [F] re-weave panel 2: six Spire banners in the centre, Rask and Moll left, Ostry right; Ilvane RIGHT palm with the spiral stone; fields per G11; cormorant diving into a wave; the nine figures face the tower. Paid (NB2 /edit) — needs the studio director's decision. Panel 2 is marketing-approved, so accuracy matters most here | banner order | keeper 3 |
| sc05-sh080 | [B] panel 1 only, slow pull-back (as in animatic v3); never panels 3+4 together; not for marketing | panels in frame | keeper 1, §9.2 |
| sc05-sh090 | [F] the tower fills the frame (full-frame fabric) | full frame | QA C5 |
| sc05-sh100 | [B] HOLLOWSTONE title on plain dark (v3 decision); never over panel 6 | background | keeper 2 |
| sc05 all panels | [F] fabric full-frame, no pillarbox (G13) | — | QA C5 |
| sc06-sh040, sh090, sh130, sh200 | [B] Corr from his left side, stump on the LEFT forearm, whistle in the RIGHT hand (§0); after the 3-image test only | stump | QA V1, CH-0048 |
| sc08 (stair) | [F] spiral groove direction "/" on every Spire frame (G5) | grooves | v1 notes |
| sc09-sh030 | [F] Ione hero: Kling 3 Pro, "no light change, she does not glow" | no glow | v1 notes |
| sc09-sh040, sh050, sh080 | [F] VFX pass: white-blue light in the grooves, top-down from the crown (G4); thread "/" (G5) | light direction | QA V9, keeper 11 |
| sc09-sh100 | [F] only the Crown Spire lit, base and doorway dark (no blue doorway); the other two Spires dark; Wick [MS, back to camera] talking to the coins (no 6th lip-sync) | base dark; Wick's back | QA V8/V14, keeper 14 |
| sc09-sh130 | [F] no hooded figure behind Pell (tower silhouette must not read as a person) | extra person | QA V12 |
| sc09-sh150, sh170 | [F] thread "/" (G5) | grooves | keeper 11 |
| sc10-sh040 | [F] Fennick steward: ONE-ear hare pin on the collar (H06) | pin | keeper 18 |
| sc10-sh070, sh120 | [F] hall banners per G11 (re-generate C-06 from H01–H08) | banner shape | keeper 6 |
| sc10-sh100 (restored) | [F] Ruel's charm beat, L058 `[MS]` warm; door-warden's back in the foreground; record L058 for finals | — | §9.5 |
| sc10-sh190 | [F] **description swapped:** Lucan MCU speaking L060 `[MS]` (was "Ruel listens") | speaker | §9.6 |
| sc10-sh230 | [F] **description swapped:** Ruel MCU speaking L064 `[MS]` (was Lucan) | speaker | §9.6 |
| sc10-sh290 | [B] clasp insert: Ruel's **LEFT** hand with the black pearl ring in the deep-blue sleeve with silver braid; the other hand in Lucan's sleeve; insert ≤ 1.5 s, no sting | which hand, sleeve colour | QA V2, keeper 16, §9.5 |
| sc10-sh330 | [B] the Helm's hand without any ring; the bead of blood on the knuckle | no ring | QA V3 |
| sc11-sh060 | [F] re-framed (§9.5): the Fennick steward with the one-ear pin by the door, waiting with the hall; no look, no line; banners per G11 | pin, banners | §9.5, keeper 6 |
| sc11-sh100 → sh110 | [F] the window with the harbour behind Ruel in both shots (no red interior in sh100) | background | QA C4 |
| sc12-sh010, sh020, sh100 | [F] the map: pale wash over the Ninth with IX, the empty ruled signature line; fourth legend mark covered | IX, empty line | keeper 19 |
| sc12-sh280 … sh380 | [F] hall banners per G11 | banners | keeper 6 |
| sc12-sh320 | [F] one still figure in the Quell blue-green block, back to camera, no face, no ref | — | keeper 20 |
| sc12-sh350 | [F] the hare's-ear pin readable as it leaves (half-turn or a glint) | pin | keeper 18 |
| sc13-sh010, sh180 | [F] the Spire in the bank window = D-08 look, light only in the upper turns, dark base | base dark | keeper 13 |
| sc13-sh120; sc14-sh020, sh060, sh100, sh130; sc15-sh180 | [F] Hollis's cracked LEFT lens (G6) | crack | QA V7 |
| sc15-sh170; sc15a-sh030/040 | [F] mix: Ursel's quiet line and the coppers/pots ride down to programme level | level | QA A6 |
| sc17-sh110 | [F] relay stones black, highlights only, no inner orange glow | glow | QA V11 |
| sc19-sh040 | [F] Pell near-frontal: braid on her LEFT (picture-right); head not cut by the top edge | braid | QA V5 |
| sc19-sh110 | [F] no light veins | glow | keeper 15 |
| sc19-sh200 | [F] the wheel stopping in the dark of dusk, not the bright day plate of sc06-sh020 | light | QA C2 |
| sc20-sh010 | [F] Wick's hair brown (G2); night, one lamp right | hair | analyst |
| sc20-sh070, sh080, sh120, sh160, sh180 | [F] no glowing cracks/veins; the stone's sound = rings in the bowl (sh070/sh160) and trembling dust only | glow | QA V10, keeper 15 |
| sc20-sh130, sh170 | [F] night, one lamp on the right; no violet daylight from a window or door; no sea in the doorway | light | QA C1 |
| sc20-sh150 | [F] hero macro: Kling 3 Pro, "the stone stays matte black, nothing glows"; check every frame | glow | v1 notes |
| sc20-sh180 | [F] Wick backed against the wall, looking at her hand; hair brown (G2) | hair | analyst |
| sc20-sh190 (E) | [B] Wick: tuft on his RIGHT temple, hair brown, night lamp light (not daylight); key frame not accepted otherwise | tuft, light | QA V6/C1 |
| sc20-sh200 | [F] Mags readable: the red rag in her hair, back to camera | red rag | analyst |

## 3. Not changed by this list
Timing, the cut and the VO. Items marked paid (panel 2 re-weave, C-06 re-generation, the Corr test) need the studio director's go-ahead at finals time.
