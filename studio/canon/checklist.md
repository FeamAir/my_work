# Canon review checklist

Used by the keeper for every script, outline, character/house proposal and storyboard before it is approved. Result: **ACCEPTED** or a numbered list of conflicts (each: where in the material, which canon record, what to change).

Write at the top of the review: material, version, canon version checked against (`Canon: vX.Y`).

## 0. Automatic pass

- [ ] `python3 studio/canon/tools/validate.py` — 0 errors on the current canon (with the proposed changes applied in draft).
- [ ] `--cast SxxEyy <all CH ids in the episode>` — nobody dead, unborn, missing or captive appears unless the script means it (flashback, vision, corpse, rumour).
- [ ] For each POV character: `--knows CH-… SxxEyy` printed and kept next to the script.
- [ ] `--age Sxx <ids>` (v0.7, DEC-71) for every pair that carries a romantic beat in the season: all `ok`; nobody marked `romance: never`.
- [ ] `--todo`: the script depends on no TODO stub; every `draft` record or `amend` field the script uses is listed for the lead (README §4, §6a); open DEC items that block the season (`decisions_for_lead.md`) are closed. Since v0.4 all 64 DEC items are ruled (`studio/story/decisions_resolved.md`); three stubs stay by design (DEC-32 Quell after SY 2, DEC-33 name of Dakka's husband, DEC-54 the S5 episode in which Pell learns SEC-009). v0.7: two keeper's questions with stubs, DEC-77 and DEC-78 - **ruled in r8 and closed in v0.8** (SEC-047 reveal S03E06, Nell @S03E06, Jaro @S04E12; EV-0340 Still 2, CY 312-11-02; SEC-051 Wren @S02E04); the stub count is back to the three kept by design.

## 1. Identity and names

- [ ] Every named character, house, place, title is in the canon (has an ID) or is listed as a **new** proposal.
- [ ] Spelling matches `glossary.md` exactly (also in on-screen text and subtitles).
- [ ] Forms of address fit rank and relationship (lord/lady, titles after a change of status, nicknames only between those who use them).
- [ ] No new name clashes with an existing one (same first 3 letters, one-letter difference, same name without epithet); listed exceptions only (`glossary.md` naming rule 1, DEC-57/58).
- [ ] No names or elements recognisable from other works or real people.

## 2. Time, dates, ages

- [ ] The episode's in-world dates match `timeline.md` (or the proposal adds them).
- [ ] Every age said aloud or implied ("you were a babe when…") matches birth dates at the episode date.
- [ ] Elapsed time is consistent: travel, pregnancies, healing of wounds, seasons and weather, moon/festivals from the calendar.
- [ ] "Years ago" references match event dates; nobody remembers an event that happened before they were born (unless told by someone — then who?).
- [ ] Flashbacks are marked and their dates fit the timeline.

## 3. Where everyone is

- [ ] Each character's location at the start of the episode = location at the end of their last appearance (or the travel is shown/explained).
- [ ] Travel times are possible (`world.md` travel table); no one is in two places at once across parallel storylines.
- [ ] Armies: size, position and speed are consistent with earlier episodes and with the battle that follows.
- [ ] Captives are still captive, exiles are still away, unless the change is shown.

## 4. Who knows what

- [ ] No character acts on, hints at, or reacts to a secret before their `known_by` episode in `secrets.md`.
- [ ] Restricted secrets (`sealed/`): checked by the keeper only; findings about them go to the lead screenwriter, never into a helper-facing review.
- [ ] When a character learns something on screen, the proposal adds `CH-…@SxxEyy` to the secret.
- [ ] Rumours vs knowledge: a character may *suspect* (note it), but not *know* without a source.
- [ ] Letters, messengers, ravens etc.: the information could physically have arrived by then.
- [ ] No hint in the episode reveals a secret earlier than its planned `reveal`; hints planted are added to `hints`.
- [ ] Red herrings do not contradict the truth (re-watch test: the truth explains every clue).

## 5. Life and death

- [ ] The dead do not speak or act (except flashback, vision, recording, impostor — each must be explicit and, if an impostor, a secret).
- [ ] Deaths on screen: `died` date, `died_at`, `status_track` and (if important) a timeline event are proposed.
- [ ] Injuries persist (scar, missing hand, limp) in later episodes and in the look notes.
- [ ] Return from apparent death is only possible from `missing`/`presumed_dead`, or via a world rule with `may_return: true`.

## 6. Houses and bloodlines

- [ ] Parentage stated in dialogue matches `father`/`mother` (public) — or deliberately matches the truth only where the secret is known to the speaker.
- [ ] Succession: who inherits follows the world's rules and the house `heads` list.
- [ ] Marriages, betrothals, alliances and enmities match house `alliances` and character relations at that date.
- [ ] Sigils, colours and words used exactly as in the house file (also for art).
- [ ] Cousins, uncles etc. named in dialogue are correct per the generated tree (`--mermaid`).

## 7. World rules

- [ ] Magic / technology used within its rules, with its cost paid on screen or later.
- [ ] No new ability appears without a rule (or a rule proposal).
- [ ] Society: laws, money, class behaviour consistent with `world.md`.

## 8. Voice and character

- [ ] Lines fit the character's voice notes (formality, catchphrases, never-says).
- [ ] Goals and fears are consistent with their arc; a change of heart is motivated on screen.
- [ ] Look notes respected: signature items, scars and their side, costume changes by season.

## 9. Brief constraints

- [ ] No romantic/sexual content involving characters under 18. **The restriction follows the character's age in the season being written** (DEC-59), not the age at the saga start. Under 18 at the saga start (CY 312): Pell 15, Wick 11, Esk 13, Zev 14, Daro 16, Lio 17, Mags 15, Patch 12, Tibb (infant). Later minors: Tibb through the whole saga (17 at the finale), Sindre Rusk (from S3, while under 18). Ione is 18, Juno Brisk 19. Check every age with `born` at the episode date.
- [ ] **Age gate for romance (v0.7, DEC-71).** A romantic beat - a kiss, a declared feeling, a held look played as romance, a courtship, a betrothal, a shared room - is allowed only in a season in which **both** characters are **18 or older by birth year**: *the year in which the season begins minus the birth year ≥ 18*; for a `~` birth count from the later year (`~CY 298` → 299). Season years: S1 CY 312 · S2 313 · S3 313 · S4 314 · S5 320 · S6 321 · S7 322 · S8 323 · S9 324 · S10 SY 1 · S11 SY 2 · S12 SY 2 (SY 1 = CY 326). Machine check: `--age Sxx IDS`; romantic relations in records carry their moment and are checked by the validator.
- [ ] First season a romantic beat is allowed (by birth year, `romance_lines.md` §1): Pell **S5** (used from S6 as the object of Lio's suit, her own feeling from S7) · Esk **S5** (used S7) · Zev **S5** (`~` birth: from the later year; married S7) · Lio **S2** (nothing romantic on screen before S6) · Ione **S1** (seed only in S1; feeling from S2) · Maren, Hollis, Elm, Jaro, Ruel and the older cast - S1. Pell and Esk never meet in S1-S4; Pell and Lio in S1 are friends of 15 and 17 and nothing else.
- [ ] **No retroactive framing:** a feeling that begins in an adult season is never dated back to childhood ("since we were children" is not a canon line); a flashback to a character under 18 is never shot or scored as romance.
- [ ] **Never romantic at any age** (`romance: never`): Wick, Tibb, Mags, Patch, Daro Vey, Sindre Rusk, Ylva Dask. **Jaro and Lio - patronage only; Kes and Esk - guardian and ward (family).**
- [ ] **Function test (DEC-72):** every love beat names the decision it causes (a vote, a betrayal, a silence, a death, a document); a beat that only decorates is cut.
- [ ] **Staging and rating:** TV 16+ - feeling, a kiss, an embrace, a closed door; the camera never goes past the door; no nudity, no bed scenes. Love is carried by objects and hands (lamp, clip, kite, packet of letters, a hand given or withheld); lip-sync close-ups are not spent on love scenes unless the line is fixed. Secrecy is never about whom one loves - only votes, seals, clans, vows and debts. The Chronicler never states a cause of love (he states the fact).
- [ ] Love-line custody and staging rules (v0.7): the second lamp, the packet in tarred twine, Ione's journal and the cut pages, the clip's first owner - `world.md` §6; Ruel gives Jaro only his **right** hand; Jaro never handles the ring.
- [ ] **Voice and direction rules of r8 (v0.8, DEC-82, DEC-87):** Jaro says "loyal" once in the saga (S01E04, fixed line, in private to Ruel) and never again; Jaro says "the Admiral" in public and never Maren's given name on screen before S06E08, and keeps nothing on paper in S2-S5; Ursel's hand to the empty sleeve twice in the saga only (S1E11, S6E8); Aurin stops stammering with Cressa from S5; Zev's stammer is "near his father", ends with his father (S5E11) and is never played as warmth in L3; Cressa never says Ilse's name in S1-S3 and once in S4 (DEC-85); Wren Roan - back only, no face, no voice in S1. **Elm's Lows street-sign** in his signing with Ione: not in S1, at most once a season from S2, and **each use is reported to the keeper**, who logs it as a clue of SEC-012. When the S2 sign list is made, private signs of L5 carry a `private: L5` note.
- [ ] Violence within TV 16+.
- [ ] Spoilers: preview / opening / ending / marketing materials use nothing from a secret whose `reveal` has not aired.
- [ ] Restricted excerpts (`excerpts/`): music, framing and voice obey the constraints given to the composer, the director and artist, and the sound director (v0.4; v0.5 additions: tapestry wording, groove turn, hands at the gate, old Cantors' black bands, marketing hum rule, Ashare theme; v0.6: Spire light and dark foot, prayer signs, compass/flag/banner/peoples, Ashare theme conditions and Sunken tone for the composer; v0.7: the pilot's Sc 12 still figure and the hand rule for the director and artist, no love cue on the five-note phrase for the composer).
- [ ] Spirals (v0.5, `world.md` §2): flat spirals clockwise from the centre outward as the viewer sees them; Spire grooves a right-hand thread (near face "/"); never fixed by mirroring.
- [ ] Spire light (v0.6, `world.md` §2, DEC-69): light comes down from the crown and goes out from the top down; the echo-shard never glows; S1-S4: no glow and no bounce-light at the foot of a sung Spire; no "low sound never lights" line anywhere. From S3: the VFX excerpt (restricted) once issued.
- [ ] Compass and heights (v0.6, DEC-65): sea and harbour west, the hill east, the Ninth south-west; Crown ~160 m, Choir ~120 m, Sluice ~90 m; light direction in the pilot's master shots.
- [ ] Flag and banners (v0.6, DEC-66): Helm's storm-grey ≠ Fennick slate; nine plain silhouettes, outline at the foot; one banner shape, round seals, no shields.
- [ ] Peoples (v0.6, `world.md` §3.5): nobody says "seven peoples"; look never proves descent or marks virtue; paleness = way of life.
- [ ] Lows prayer signs (v0.6, DEC-68): only WATER and STILL match Choir sign (small, at the waist, from S1E8); SILENCE = palm on lips; no on-screen remark on the match in S1-S4.
- [ ] Ashare (v0.6, DEC-70): no Ashare theme of any kind before S5E10; four recognisers; Sunken tone never stated in open files.
- [ ] Terms on screen and in subtitles as in `glossary.md` (e.g. *echo-shard*, never *echo-chip*; *death-tone*, TERM-0495).

## 10. Output of the review

- [ ] Conflicts listed with exact references (script scene/line ↔ canon ID and field).
- [ ] Canon change requests from the material are either accepted (logged in `CHANGELOG.md`) or rejected with a reason.
- [ ] After acceptance: new IDs created, `known_by`/`hints`/`status_track` updated, validator run again.
