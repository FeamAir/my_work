# S1E01 "The Ninth Sluice" — Production Notes

Version 1.1 · 2026-11-22 · author: lead-screenwriter · companion to `beat_sheet.md` v1.1 (scene numbers are the same)
For: director · storyboard artist · VFX supervisor · composer · sound director · (marketer: §9)
Spoiler level: **safe for the production team** — this file says what must be on screen and what must not be changed; it never says why a clue matters. Where a note reads *"fixed — ask the lead"*, the reason is in the sealed file and reaches you through the keeper's extract.

Budget frame (BRIEF): cheap draft first, the expensive model once; at most three paid finals per shot, then change the approach, not the seed. Nothing below is generated before the storyboard is approved.

---

## 1. "Money" scenes — where the expensive shots go

Six scenes carry the pilot. Five need hero shots on the best model; one (Sc 16) is a signature image that is almost free. Everything else is built to be cheap (§2).

| # | Scene | Hero shots (max) | What must be right | How to keep it affordable |
|---|---|---|---|---|
| **M1** | **Sc 1 — the Night of Still Water** (1:15) | 7 images, of which **4 hero**: the cradle in the drowned street; the bar dragged shut by young hands; the baby in the lantern boat; the sleeve | Frame one decides whether a stranger keeps watching: the cradle must read in half a second on a phone. Water must move believably in the four hero shots. **No faces anywhere** | Night, rain and lantern light hide detail; the crowd is silhouettes; lanterns going out and the water over the tide-marks are static plates with animated light and a rising matte (ffmpeg). **Every plate is built to be reused in E10** (same lane, same doorpost, same gate) — the cost is shared by two episodes |
| **M2** | **Sc 3 — the pool** (0:35 of the scene) | 3: Pell leaning out over black water on the rope; the stone breaking the surface; the rings spreading across the whole pool | The rings and the low hum must land together, on 3:00. Pell's fear is a silent close-up (no lip-sync) | The rest of the scene is mid-shots on mud flats (static plates, parallax). The ring effect is one element — **build it once**: it returns in a bowl in Sc 20 and for seasons after |
| **M3** | **Sc 9 — the crown** (1:45) | 4: Ione's back in the throat of the Spire; the grooves lighting turn by turn; the harbour going from chop to glass; the masts stopping | This is the image of the series and its repeatable signature. The flattening must be a *change* seen in one continuous shot, not a cut between two states | Ione is back to camera — no face, no lip-sync. The groove-light is a mask animation over a still. The cross-cut to the roof is two static mid-shots. **Library asset:** the crown shot, the glow and the "glass" transition are reused every time a Spire is sung, all season |
| **M4** | **Sc 12 — the fall** (≈0:25 of the scene) | 3: Lucan's close-up on the cut-off line (lip-sync); the body across the table; the map sliding off and rolling shut | The fall is the one piece of physical action in the pilot: show the start and the result, not the middle (cut on the hand opening) | The reading before it is the map (inserts, tints appearing — free) and still faces. The hall afterwards is frozen — a held frame with drifting dust |
| **M5** | **Sc 20 — "It's singing back"** (≈0:30) | 3: the stone on its cord in lamplight, humming (macro); the bowl ringing; Wick's close-up (lip-sync) | The stone's look is fixed here for twelve seasons: thumbnail-sized, black, glassy, **cracked across**, on a rotted cord. Its hum is *seen* (a tremor, the rings), never a glow — glow belongs to the Spires | One room, one lamp, two children; Mags and Nan are a head and a pair of feet |
| **M6** | **Sc 16 — forty pens** (signature, cheap) | 1 wide + 2 inserts | Forty pens stopped in the air; one ink drop falling; one pen that goes on | It is a **still frame** by nature — the cheapest iconic shot in the episode. Spend on the composition, not on motion |

Also one **establishing asset** worth a top-model still: the six-second rise over Highwater in Sc 2 (three tiers, the Spires). It is the season's master wide and will be reused in every episode.

**Do not spend on:** the collector, the wheel, the Counting House rows, the Listening House, the gate — all are designed as plates with small motion.

## 2. Limited animation — scene by scene

`LA` = static keyframes with camera move, parallax, light and particles assembled in ffmpeg; `MIX` = mostly LA with one or two generated clips; `GEN` = generated motion needed.

| Sc | Mode | Notes |
|---|---|---|
| 1 | GEN (4) + LA (3) | see M1 |
| 2 | MIX | the knock and Pell's exit are generated; Wick is not shown on the bridge (v2 restage, approved 2026-11-24): the rope-bridge bows and drips over the collector, Wick `[OS]`; the city rise is a tall still with a vertical pan (also crops well for 9:16) |
| 3 | MIX | see M2; Mags is a distant figure, never closer than a full-body long shot |
| 4 | LA + 1 GEN | a table scene: hands, bread, net-needle, the chest in the corner. The one generated clip is Nan's hand going over Wick's mouth. Nan's CU is lip-sync #1 |
| 5 | **LA only** | tapestry: five panels drawn as *woven textile*, a distinct flat style (this style is also the look of all later "Chronicle" sequences). Camera moves only. No animation inside the weave |
| 6 | LA | walkers from behind in silhouette on the wheel — a looped rotation; Corr in mid-shot; the still wheel is simply a still |
| 7 | **LA only** | table-top document: tints wash in, labels appear. Hands in two shots. This map is the fans' board — legible, designed, kept as a master file and redrawn each season |
| 8 | LA + 1 GEN | the fork struck and lifted (generated, hands); the old Cantor is a robe and a hand at a throat |
| 9 | GEN | see M3 |
| 10 | MIX | the hall as colour blocks; Ruel's entrance generated (mid-shot); the clasp is two inserts (hands; the ring) and one two-shot; the bead of blood is an insert |
| 11 | LA + lip-sync #2 | cup inserts; Ruel's CU |
| 12 | MIX | see M4; lip-sync #3 |
| 13 | **LA** | rows of backs (one plate, repeated depth), pages, pen, the water-glass going still (reuses the "glass" idea in miniature) |
| 14 | **LA** | two sheets and two faces. The figures 1,470 / 1,740 must be readable on a phone for a full second each |
| 15 | LA + lip-sync #4 | Ursel barely moves by nature |
| 16 | LA | see M6 |
| 17 | LA | a wall of caged stones (one plate), Odo in mid-shot; the stones "ring" by a small shimmer and sound |
| 18 | MIX | helmets from behind; the hands on the bar is a generated insert **framed exactly as Sc 1 image 3** (fixed — same lens, same angle, same side of frame) |
| 19 | MIX | door comedy and the chest in mid-shots; the lane is lantern-lit silhouettes; Nan is a tiny figure far off |
| 20 | MIX | see M5; lip-sync #5 |

Roughly **60–65% of the running time is limited animation**. The script will be written to that proportion.

## 3. Lip-sync close-ups — budget 5

| # | Sc | Character | Line |
|---|---|---|---|
| 1 | 4 | Nan | "Never sing, chick. Hum if you must, and only for the house." |
| 2 | 11 | Ruel | "I don't drink before a storm." |
| 3 | 12 | Lucan | "…and the Ninth Sluice—" |
| 4 | 15 | Ursel | "A clerk who is trusted gets a clip." |
| 5 | 20 | Wick | "Pell… it's singing back." |

- Shots 2, 3 and 5 are **reused in later episodes** (recall montages) — archive the final clips and their keyframes.
- If the style test allows only four: #3 becomes a mid-shot over the map, the close-up goes to Lucan's hand.
- Everything else is `[VO]`, `[OS]`, `[MS]`, backs, hands, documents. **Pell and Ione have no lip-sync close-up in the pilot**; their close-ups are silent. Ione's singing is never lip-synced — always the back.
- Speech on mid-shots: keep mouths small in frame or turned three-quarters; prefer cutting to the listener.

## 4. Crowds and how to make them with AI

| Sc | Crowd | Solution |
|---|---|---|
| 1 | the lane in flood; the crowd at the gate | silhouettes against lantern light, rain, backs; hands and fists in inserts; sound does the numbers (voices without words, iron) |
| 2, 6 | treadmill walkers | from behind, one loop of a wheel with identical backs; the count in sound |
| 3 | mudlarks | four or five small figures on a mud flat, far apart |
| 10–12 | the tithe hall, eight seats | **colour, not faces**: eight blocks of house colour under eight banners (white; deep blue; rust red; sea green; slate and sulphur; black and copper; violet and linen; Dask's — per the art sheet), seen from behind or from the gallery. Only Lucan, Ruel, Ione and Juno are faces |
| 13–16 | forty clerks | one desk-row plate repeated in depth; identical ash-grey backs — sameness is the point |
| 17 | relay room | no people but two |
| 18 | Rusk guards | helmets, rust-red tabards, a file from behind |
| 19 | the lane at the death-tone | doorways with one lantern each and one figure each; no figure closer than full-body |

Rule for the episode: **no shot holds more than four readable faces.**

## 5. References to make for the pilot

Counts are for the concept artist and the director's ID-blocks (`direction/consistency.md`). Anchors: `story/characters/_anchors_matrix.md`; colours and sigils: `story/houses/art_and_music_sheet.md`.

**A. Full character sheets — 8** (turnaround, expressions, ID-block)
Pell · Wick · Nan · Ione · Ruel · Hollis · Ursel · Odo

**B. Light references — 11 (+2 optional)** (costume + one or two anchors; face only where noted)
1. Helm Lucan Dask — **face needed** (one lip-sync close-up; he is never seen again alive)
2. Juno Brisk — white coif, taster's spoon on a chain
3. Fossett — pomaded centre parting, spotless sleeve-guards (face, mid-shot)
4. Mags — red rag in black frizz, man's pocketed waistcoat (long shot and back only in E1)
5. Corr — barrel body, left hand missing, beard in one rope, reed whistle
6. the tithe-collector — slate tabard with sulphur stripe, box chained to the wrist (new, unnamed)
7. Maren — **back only**: short deep-blue jacket, umber curls tied high with a silver cord (her full sheet is due for E2)
8. Kes — **back and hands only**: rust-red tabard, shaved sides, dented half-helm with a white stripe under the left arm; plus the *young* pair of hands for Sc 1 (her full sheet is due for E2)
9. Liss — silhouette with one long left braid (Sc 1)
10. Sister Venn — a grey robed sleeve and hand (Sc 1)
11. the old Cantor on the stair — robe, black throat-band, a signing hand
12. *(optional)* Vesna — veiled, violet veil, rings on every finger of the right hand; never a face
13. *(optional)* Brother Elm — bowed, tonsure band, undyed linen

**C. Group and uniform sheets — 8**
mudlarks · treadmill walkers · Lows lane folk (CY 295 night and CY 312) · Lantry clerks · Rusk guards (helmeted) · the eight seats in the hall (one sheet: eight colour blocks, banners, stewards) · Choir robes (novice, Cantor) · Fennick men (relay-keeper; the hare's-ear pin)

**D. Locations — 12**
1. Highwater, master wide — three tiers and the Spires (PL-0004)
2. Ninth Sluice lane with Nan's doorpost and its tide-marks — **three states**: night flood CY 295, dawn ebb, dusk tide (PL-0008)
3. the evacuation gate — Lows side (CY 295) and Mids side (CY 312) (PL-0021)
4. the back-canal, the bare old sluice sill, the sump pool (PL-0020)
5. the Ninth's treadmill pump — three wheels over a sump (in PL-0008)
6. Nan's stilt-house, interior — table, net-chest, water-bowl, window (PL-0019)
7. the Map Office, table-top (PL-0078)
8. the Crown Spire — inner stair; a throat of the crown; exterior, dark and lit (PL-0014)
9. Highwater harbour from above — rough and "glass"; the *Patient Gull* at anchor (PL-0018)
10. the tithe hall of the Dry Palace — dais, map-table, tall window to the harbour, banners (PL-0009)
11. the Lantry counting hall — desk rows, high desk, the caged stone; the steps outside over the city (PL-0011)
12. the Listening House relay room — the wall of caged stones (PL-0012)

**E. Props and documents — 12** (each a clean reference; the first five are saga objects — fix them now)
1. Pell's stone on its cord 2. Ruel's black pearl ring (left hand) 3. the brass ledger-clip 4. Ione's silver tuning fork 5. the Tithe Map (master) and its small copy 6. the Breaking tapestry, five panels 7. the tithe cup 8. the collector's chained box 9. the net-chest 10. the cradle 11. a caged echo-stone 12. the two ledger sheets (ACCOUNT NINE; Fossett's 1,470 / 1,740)

**Total: 51 references (53 with the optional pair)** — 8 + 11 + 8 + 12 + 12. Of these, about 35 are reused in E2–E12 without change; the pilot pays for most of the season's reference library.

**Fixed details — do not vary (ask the lead before changing any):**
- every braid named above is on the **left**; Ruel's ring and his clasp are **left-handed**; Nan's single earring is **left**;
- the tapestry: crowds behind the Queen in panel 2 and **none** in panel 5; a black pearl on her singing hand; the girl's fist **closed**; the pearl and the fist in **different panels**; every spiral turns **sunwise**; a cormorant on the sail;
- **the stone and the ring never share a frame** — not in a cross-cut split, not in a poster, not in a thumbnail;
- the cradle in Sc 1 has **no knot** on it;
- Sc 18's hands are framed exactly as Sc 1's;
- the Tithe Map leaves the table **unsigned**;
- Nan's earring is worn and never looked at; nobody says the family's name.

## 6. Music and silence

| Moment | Sc | What |
|---|---|---|
| **The lullaby — first music of the series** | 1 (0:35) | After thirty-five seconds of water and iron with **no score at all**: a woman's unaccompanied hum, five notes, mouth closed. Then a baby's voice: the first two, imperfect. No instrument joins. This phrase must be composed and approved before anything else in the score |
| The lullaby, second use | 3 (≈2:50) | Pell: three notes of it, mouth shut, breathy, frightened — not pretty. **The stone's answer is not an instrument and not a voice**: one low sustained tone, below every other pitch in the episode, felt as much as heard |
| The lullaby, third use | 20 | No melody. The stone's low tone alone, entering under the third stroke of the death-tone, and held one second into black. The ending theme starts after that second, not on the cut |
| **Rule** | all | The five notes are heard **only** in Sc 1, 3 and 20. Not in underscore, not in the title, not as Lows colour. *Fixed — ask the lead.* Keep the low register empty everywhere else (`art_and_music_sheet.md` §5) so that the stone's note has a place nothing else has used |
| The Lows | 2, 3, 4, 6, 19 | No sung voice. Whistles (falling two-tone = Listeners; rising three = all clear), plank-stamps, the walkers' count spoken on **one pitch**, the reed whistle, buckets, water. Percussive, alive, never mournful. Wick's one sung note in Sc 4 should be startling because it is the only one |
| The Sluice Spire | 2, 4 | A Spire's hum that is audibly **flat** and thin — the viewer should feel something is off before anyone says so |
| Title | 5 | The saga theme's first statement — 12 seconds, one phrase, built so that it can open into the full opening theme at the end credits. The tapestry before it: a drone and a single plucked or bowed line, dry, "archival" |
| **Ione's song** | 9 | One sustained true tone on the Crown Spire's home pitch — a real, trained, young soprano sound, no vibrato show. The Spire's answer: a deep hum that arrives *under* her. Then the sea's noise is **taken away** — the flattening is heard as subtraction (waves, rigging, gulls fade to nothing). Score stays out until she stops |
| The hall | 10–12 | Almost no music. Room tone, cloth, the cup. A single held string from "…Last Song" onward if anything. On the fall: **silence** — not a sting |
| The Counting House | 13–15 | No music. Pens, pages, felt. It should be the quietest place in the episode — so the bell can be loud |
| **The death-tone** | 16–20 | A diegetic signal, not score: three long tones on the Crown's pitch and a rest as long as a tone, repeated; it passes from stone to stone and thins as it descends the city. In Sc 16 it is all there is. Score may enter under Sc 17–19 as a slow pulse counting — the first hint of the "clock" idea that returns each episode |
| Odo | 17 | He stops a stone with one finger: the tone in that room ends mid-ring |
| Silences to protect | — | 0:00–0:35 (no score); the pool before the hum; after Nan's hand (three seconds); the fall; the pens; the last second after the cut to black |

**House themes:** not stated in the pilot. At most a colour: Corvane's warmth under Ruel's entrance. The themes are introduced from E2, when the candidates declare.

## 7. The Chronicler

- **Heard three times only:** Sc 5 (≈55 s), Sc 7 (≈30 s), Sc 19 (≈20 s). **Never before the end of Sc 4** (2026-11-24 ruling; was "5:55" of the 29-min version; 5:05.5 in the v2 picture). Never over a character's face — only over the tapestry, the map, and the lane at dusk.
- **Voice:** old, dry, precise, faintly hoarse; a record-keeper reading entries, not a bard and not a priest. Clear consonants, every word finished. Unhurried — about 110 words a minute. No tremor of feeling at "She sang her city into the sea"; no relish at the death. He gives dates, numbers and counts with the smallest audible satisfaction.
- **Casting constraints (fixed — ask the lead):** not a bass, no "epic trailer" colour; the timbre must be one that can become **slightly hoarser** in a later season without being recast; it must be clearly distinguishable from every S1 speaking character on first hearing. Lock the voice ID at the first TTS probe and never regenerate it with different settings.
- **Text rule:** his lines are delivered exactly as scripted — no paraphrase, no trims in the edit. Lines marked `[ECHO]` are never cut.
- **Sign-off:** "…and the water kept its counsel." — one fixed reading, archived; it closes Sc 5 here and returns at the season's end.
- **Mix:** dry and close, almost no room — a man reading at a desk. A page-turn before his first word (Sc 5) and nothing else.
- Hollis's young `[VO]` in Sc 13 must not share cadence, pace or processing with the Chronicler (fixed — ask the lead).

## 8. Other notes for the director and the storyboard

- **No logo, card or title before frame one.** The first frame of the upload is the cradle. Idents and the AI badge: corner overlay or after the title (with the marketer).
- **The six-second city rise (Sc 2)** is the only establishing shot before the title; do not extend it. The world is explained by Sc 5 and Sc 7, when the viewer wants it.
- **Match cuts are structure, not decoration:** Sc 1 → 2 (the doorpost), Sc 4 → 5 (the stone → the woven tower), Sc 5 panel 5 → Sc 9 (the lone singer), Sc 1 → Sc 18 (the hands), Sc 3 → Sc 20 (the rings).
- **Time of day is a clock:** dawn ebb (Sc 2–3) → morning → noon (Sc 7) → low sun (Sc 9–15) → dusk (Sc 16–19) → dark (Sc 20). The tide is out in the morning and back in the lanes by dusk — the same lane plate, wet.
- **Sc 13 overlaps Sc 9 in time:** the Crown Spire glows in the bank's windows. One city, one hour.
- **Sign language:** one gesture only in the pilot (the old Cantor's blessing, Sc 8). It should come from the sign glossary the director is preparing, so that it stays valid later.
- **Age and content:** Pell 15, Wick 11, Mags 15, an infant. Peril by water, light and sound; no injury detail; the one death is a fall.
- **E10 reuse:** keep every Sc 1 plate, layer and camera move as a named library item — E10 restages them.

## 9. Vertical cuts (15–60 s) for Shorts / TikTok — self-contained hooks, no spoilers

Storyboard these five moments with a **9:16 safe area** (the subject centred, nothing essential in the outer thirds). Each works without context, ends on a question, and gives away no answer. End card on each: title, "Episode 1", the AI badge.

| # | Clip | Source | Length | Opens on | Ends on | On-screen text (suggestion) |
|---|---|---|---|---|---|---|
| V1 | **The cradle** | Sc 1, 0:00–0:35 | 30–35 s | the cradle afloat in a drowned street | the bar dropping; fists on the gate | *Someone shut the gate.* |
| V2 | **It hummed back** | Sc 3, the pool | 35–45 s | a girl on a rope leaning over black water; a boy: "Pell. Mouth." | the rings crossing the pool; the boy's face | *Singing is against the law here. Something just answered.* |
| V3 | **She sings. The sea lies flat.** | Sc 9 | 30–40 s | a white figure, back to us, in the throat of a black tower | the harbour turned to glass; her hand at her throat | *An empire stays dry only while its nobles sing.* |
| V4 | **Never sing** | Sc 4 | 20–25 s | a boy sings one note at a kitchen table | an old hand over his mouth; "Never sing, chick." | *The poor are forbidden to sing. Why?* |
| V5 | **Forty pens** | Sc 16 | 15–20 s | a silent hall of clerks; a stone in a cage begins to ring | every pen stopped in the air — and one still writing | *A ruler just died. One person isn't surprised.* |

Tall subjects make V1–V3 natural in 9:16: the street, the rope over the pool, the Spire.

**Do not cut for social before the episodes named:**
- anything from Sc 10–12 as a stand-alone clip (the clasp, the cup, the fall) — the hall plays only inside the episode until after E11;
- Sc 20, the last line — it is the reason to finish the pilot; usable after E2 is out;
- the Sc 1 / Sc 18 hands side by side — never as marketing;
- the baby humming back and the sleeve (Sc 1, 0:50–1:08) — keep inside the episode;
- any image that puts the stone and the ring together.
