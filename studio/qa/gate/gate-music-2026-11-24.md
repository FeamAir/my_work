# Gate — pilot music stage (theme master + OP song "Louder Than the Tide")

Date: 2026-11-24 · gatekeeper · branch `studio-setup` @ 0c225db · no paid calls made.
Scope: composer's request to run ElevenLabs Music (`music_v2_5`): theme master ≤ 2 takes, then OP song ≤ 4 takes conditioned on the master's `song_id`; cap 25 000 credits (≈ 115 862 left on the account).
Inputs read: `music/opening_song.md` v0.3, `music/main_theme.md` v0.1, `music/gen/*` (both plans, `run_music.py`, `check_take.py`), `reports/composer-2026-11-24.md`, `story/episodes/S01E01/v4_dialogue_pass.md` §0–§4, §8.3, §9–§10, `music/leitmotifs.md` §0, `music/lullaby.md` §3, §8, `music/pilot_cue_sheet.md` v0.3, `canon/excerpts/for_composer.md` §3, `canon/secrets.md` (SEC table, incl. the uncommitted v0.9 row for SEC-011b), `canon/CHANGELOG.md` v0.9 (uncommitted, keeper's work in progress), `canon/excerpts/for_director_and_artist.md` §7 (uncommitted), `direction/S01E01_finals_checklist.md`, `status.md`, `pipeline/costs.py`, `pipeline/net.py`, `pipeline/elevenlabs_client.py`, `output/costs.jsonl`.

## Verdict

**GATE CLOSED for the OP song.**
**Theme master: GATE OPENS once C1–C5 below are done.** They are free fixes, about 30 minutes of work. No re-review is needed: the composer ticks them in the run log and runs.

The theme master is needed in every version of the pilot: as the ending, the instrumental OP and the cuts. It does not depend on the v4 lore sign-off. The song does depend on it, through its lyrics and its placement (B1, B2).

## Blockers (song only)

| # | Where | What | Owner |
|---|---|---|---|
| B1 | `canon/excerpts/for_composer.md` §3 item 8; `leitmotifs.md` §0 rule 7; `status.md` "Решения директора" (OP line) | Canon rule: "the Lows have no voice; a voice appears only when it breaks through on screen: Lio S1E2". A sung lyric in the Lows' "we" voice at 3:25 of S1E01 comes before that point. The director's 2026-11-22 decision ("song first in S1E3; E2 and pilot instrumental") was made **for exactly this reason** (`composer-2026-11-22-r2.md`, Q1), and it is still the decision on record in `status.md`. v4 is a proposal ("nothing here is in force yet"). The keeper's v0.9 rulings (uncommitted) sign the OP **visual** list but say nothing about the song's voice or its lyrics. | lore-keeper: ruling. Director: record the decision in `status.md` |
| B2 | `opening_song.md` §3, bridge, line 2: "and the water keeps its counsel"; `op_song_plan_v1.json` chunk 6 | This paraphrases the Chronicler's sign-off (TERM-0211, SEC-011b). Canon v0.9 (in progress): the record is first *heard* in S12E13, and nobody may quote the sign-off. As written, a sung voice would say the sign-off aloud in every S1 opening, and in the pilot it comes ~17 min before the Chronicle page prints it. The lyrics have **never** been reviewed by the keeper: no `lore-*` report mentions the song. Smaller items for the same review: "keep it in your chest" (it can read as closed-mouth humming, for_composer §3 item 9); and the hook's idea that a commoner's voice is set against the tide, which the keeper should check against the sealed hint plans (SEC-005 / SEC-002 area). The lyrics are baked into the audio, so any change after generation means new takes (up to ≈ 15 000 credits wasted). | lore-keeper: lyric sign-off. Composer: swap the line (e.g. a bridge without the sign-off) |
| B3 | `opening_song.md` header | No director approval of the lyrics or concept is on record. v0.2 says "текст и концепция утверждает директор", and v0.3 only changes the placement. | Director |

Lifting B1–B3 costs nothing and does not depend on the v4 cut point: the OP is 1:30.0 wherever it sits. If the keeper rules out pilot placement, the song is still the E2/E3+ OP, so the **placement** alone would not waste takes. The **lyrics** would.

## Conditions for the theme master (free, before the first paid call)

| # | Where | What | Owner |
|---|---|---|---|
| C1 | `run_music.py` main() | The runner never calls `costs.guard`. As a result, the `STUDIO_ALLOW_PAID` switch (not set in `.env`, so it defaults to off), the `BUDGET_LIMIT_USD` check and the balance floor are all bypassed. Only the private credit ledger is checked. Add `costs.guard("elevenlabs-music", secs/60)` before the POST (or at least `config.paid_calls_allowed()`). | composer / IT |
| C2 | `run_music.py` except-branch | On an error, `costs.log(... status="error")` writes `usd_estimate = 0` even when the credit delta is > 0, so a charged failure is invisible in `output/costs.jsonl`. Pass `usd=credits*rate`. | composer / IT |
| C3 | `run_music.py` after the POST | If `credits_used()` (or `storage`) raises after a successful POST, no ledger row and no costs row are written, and the cap goes blind. Write the ledger row first, using the pre-call estimate as a fallback. | composer / IT |
| C4 | `run_music.py` | The cap relies on the `character_count` delta. If that delta is ≤ 0 or lags (async billing or a cycle reset), the ledger records 0 and the cap stops working. If the measured credits are ≤ 0 after an OK take, record the estimate and stop. Also, other agents' TTS running at the same time inflates the delta; that error is in the safe direction. | composer / IT |
| C5 | `theme_master_plan_v1.json` | §1.1 items 2–3 are not fully reflected in the prompt. No chunk has "key change / modulation" or "F-sharp major chord / Picardy third" as a negative. The Rise chunk climbs to C♯ major, so the model may resolve to F♯ major, which would sound the reserved A♯. "low drone / pedal tone" is missing in Rise and Answer (Intro, Theme, Hook have it); add it there. Same edit for the OP plan before it runs: add "major chord" to the Pre-Chorus and "low drone" to Pre-Chorus and Chorus. | composer |

## Point-by-point

### 1. §1.1 rules in the plans
- No lullaby or riddle quote: nothing in either plan quotes it. "5/4 / quintuplets" are negatives only in the Groove chunks. The listening checklist covers it (composer, by ear). OK.
- Reserved tone A♯/B♭: the written harmony (F♯m, A, D, E, Bm, C♯sus4, C♯) is clean. The risk is in the prompts → **C5**.
- Drone/sub: "sub bass" is negative in every instrumental OP chunk and every theme chunk. "drone/pedal" is incomplete → **C5**. The OP has a bass guitar and a drum kit, so energy below 90 Hz is certain, and `check_take.py` reports `sub_vs_full_db` without a pass/fail threshold. `leitmotifs.md` §0 item 4 requires an 85–90 Hz high-pass on pilot music stems; `pilot_cue_sheet.md` says the ED gets 40 Hz on drums. → **F1**.
- Phone band: the range is in the prompts (alto–mezzo; melody up to F♯5), and `check_take.py` writes `_phone.wav`. OK.
- No choir/hum: "choir" is negative in every vocal chunk and "humming" in the key ones. The theme is instrumental throughout. OK.
- No house/hero themes: none are named. The listening checklist should add "no Corvane 'dive' (horn, 4th down / 6th up)". Both plans ask for horn "descending calls". → F5 (cosmetic).

### 2. Lyrics: spoilers and canon → B2
Open-canon items are fine: Hush Law, the tiers of song, "Who pays for the dry?" (Kes, S1E4). One correction for `opening_song.md` §3.1: "Calm is bought" is **Quell house words** (CH-0019, HS-020; first spoken S1E2 by Tuck, E4 by Jaro), not "девиз Низов". It is open, but the keeper should glance at it together with B2, because the S1E12 echo line belongs to SEC-046.

### 3. Runner, cap, logging
- Budget: worst case 2 × 96 s + 4 × 90 s = 9.2 min × 2 500 cr/min = **23 000 ≤ 25 000** (checked with `validate()`: 96.0 s / 90.0 s). The cap is shared across theme and song through one ledger. Overshoot is bounded by one take if the real rate is above 2 500 cr/min. After take 1, set `--rate` to the measured rate × 1.1.
- USD: `output/costs.jsonl` = $51.92 (fal $43.36, ElevenLabs $8.56) against `BUDGET_LIMIT_USD=120`. The music worst case at the default $0.0003/credit is $7.50, giving $59.42. OK. No fal calls are involved, so the fal floor is untouched.
- Duplicates: there are no `elevenlabs-music` rows in `costs.jsonl` and no `output/music/`, so nothing is duplicated.
- The two reported bugs **do not affect this run**. The runner does not use `elevenlabs_client.music()` (so `_plan_seconds`, which returns `None` for `chunks` plans, is confirmed but not used), and it calls `request(..., retries=1)`, which sends exactly one attempt. They must still be fixed by IT before any other music path is used (F6).
- The ledger lives in `output/` (gitignored): run all six takes in one environment, or copy the ledger out (F7).
- Take limits (≤ 2 / ≤ 4) are not enforced in code; they rely on the composer's discipline.

### 4. What is still unapproved
- The song: B1–B3.
- The theme: `main_theme.md` is "черновик к тесту". §7 plans a sketch → master with `conditioning_ref` on the sketch, plus a free ABC guide for the director first. The run uses the master cold. That is the director's call (≤ 2 takes), but §7 is now out of date (F3). Doing the free guide first is recommended.
- v4 itself: nothing in the theme generation depends on it.

### 5. Durations
- OP: plan 6+6+18+12+24+9+12+3 = **90.0 s** = 30 T, matching §2 and v4 §8.3 (3:25–4:55). OK.
- Theme master: **96.0 s** (7 chunks × 3 s grid). OK.
- Ending: three versions disagree, though none of this affects generation (cuts are free):
  - `pilot_cue_sheet.md` v0.3: ED = the full 1:36;
  - v4 §3.2: "start on phrase B" (= 0:36 in the master);
  - composer: 0:00 in, full 1:36, or a 60 s "no hook" cut (0:00–0:48 + 1:24–1:36).

  The composer's 0:00 in-point fits the Chronicle page best, because the quietest ≈ 20 s are under it. Phrase B at 0:36 is not the quiet part. The director picks after the master exists (F4).

## Fix before finals / cosmetic

| # | Where | What | Owner | Severity |
|---|---|---|---|---|
| F1 | `opening_song.md` §6; `check_take.py` | Add the pilot OP version with HPF 85–90 Hz (or define a pass threshold: short bass notes allowed, nothing sustained and tonal below F♯2). Without this, the sub check is not a gate. | composer | fix before final |
| F2 | `opening_song.md` §5.1–§5.3 | Still v0.2: there is a SKETCH step, and the §5.2 JSON has `condition_strength` at chunk level, which the API schema rejects. The header says the `gen/` files are authoritative. Replace it or point to them. | composer | fix before final |
| F3 | `main_theme.md` §7 | The generation order no longer matches the run (no sketch, master generated cold). | composer | fix before final |
| F4 | `pilot_cue_sheet.md` v0.3 | Still has T-TITLE, no OP and ED 1:36. Update after v4 is accepted, including the ending in-point. | composer / director | fix before final |
| F5 | `opening_song.md` §7 (director notes) vs v4 §3.3 and keeper v0.9 §7 | 1:00 "heroes together" (Pell and Ione may not share a composition); 1:09 "open chronicle / tapestry" (the Chronicle book is forbidden in the OP; tapestry panels 1, 2 and 5 only); 1:06 "hand with salt" (ask the keeper); 1:27 "episode title" vs v4 (title burned in over sc03-sh270). Also: `S01E01_finals_checklist.md` G13 says "panels 3, 4, 6 never in opening", v4 §3.3 allows 6, and the keeper v0.9 now forbids 6. Align G13 and v4. | composer / director / lead-screenwriter | fix before the OP storyboard |
| F6 | `pipeline/elevenlabs_client.py` `_plan_seconds`; `pipeline/net.py` `request(retries=0)` | Both bugs are confirmed. They are not in this run's path. | IT | fix before other music calls |
| F7 | `output/music/gen_ledger.jsonl` | The ledger is local and gitignored, so the cap resets in a new container. | composer | cosmetic |
| F8 | `op_song_plan_v1.json` chunk 2 | 6 s chunk with a 12 s `conditioning_ref` range. Confirm the API accepts a range longer than the chunk; a dry run cannot test this. | composer | cosmetic |
| F9 | `output/costs.jsonl` | ElevenLabs credit units logged: 28 972. The account reports 15 138 used this cycle. Either the logged estimates are too high or the billing cycle reset; reconcile. | IT / producer | cosmetic |
