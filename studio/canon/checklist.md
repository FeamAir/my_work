# Canon review checklist

Used by the keeper for every script, outline, character/house proposal and storyboard before it is approved. Result: **ACCEPTED** or a numbered list of conflicts (each: where in the material, which canon record, what to change).

Write at the top of the review: material, version, canon version checked against (`Canon: vX.Y`).

## 0. Automatic pass

- [ ] `python3 studio/canon/tools/validate.py` — 0 errors on the current canon (with the proposed changes applied in draft).
- [ ] `--cast SxxEyy <all CH ids in the episode>` — nobody dead, unborn, missing or captive appears unless the script means it (flashback, vision, corpse, rumour).
- [ ] For each POV character: `--knows CH-… SxxEyy` printed and kept next to the script.
- [ ] `--todo`: the script depends on no TODO stub; every `draft` record or `amend` field the script uses is listed for the lead (README §4, §6a); open DEC items that block the season (`decisions_for_lead.md`) are closed. Since v0.4 all 64 DEC items are ruled (`studio/story/decisions_resolved.md`); three stubs stay by design (DEC-32 Quell after SY 2, DEC-33 name of Dakka's husband, DEC-54 the S5 episode in which Pell learns SEC-009).

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
- [ ] Violence within TV 16+.
- [ ] Spoilers: preview / opening / ending / marketing materials use nothing from a secret whose `reveal` has not aired.
- [ ] Restricted excerpts (`excerpts/`): music, framing and voice obey the constraints given to the composer, the director and artist, and the sound director (v0.4; v0.5 additions: tapestry wording, groove turn, hands at the gate, old Cantors' black bands, marketing hum rule, Ashare theme).
- [ ] Spirals (v0.5, `world.md` §2): flat spirals clockwise from the centre outward as the viewer sees them; Spire grooves a right-hand thread (near face "/"); never fixed by mirroring.
- [ ] Terms on screen and in subtitles as in `glossary.md` (e.g. *echo-shard*, never *echo-chip*; *death-tone*, TERM-0495).

## 10. Output of the review

- [ ] Conflicts listed with exact references (script scene/line ↔ canon ID and field).
- [ ] Canon change requests from the material are either accepted (logged in `CHANGELOG.md`) or rejected with a reason.
- [ ] After acceptance: new IDs created, `known_by`/`hints`/`status_track` updated, validator run again.
