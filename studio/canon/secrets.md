# Secrets registry

Canon: v0.8 · Status: **approved** (foundation r2, approved by the director 2026-11-22; SEC-017a/b and SEC-030…045 approved by the lead screenwriter in r3; v0.7: SEC-046…051 and the additions to SEC-001, 006, 012, 013, 016, 023, 031 from the love lines, r7, DEC-73; v0.8: SEC-047 episodes, SEC-051 knower, Elm's partial knowledge in SEC-004/049, rename Wren Roan - r8, DEC-77…80; transfer by lore-keeper)

**Full spoilers - never use in public material before the reveal episode.**

Every hidden truth in the saga is one record. Records of **restricted** secrets (those the lead screenwriter keeps from the writer-helpers) live only in `sealed/sealed.md` (README §8a); this file lists them in the overview with the production constraints that may be shared.

## Fields

```canon-template
id: SEC-NNN
type: secret
canon: draft
title:              # short working name (internal)
tier:               # saga | season | episode
truth:              # the real fact, one sentence
cover_story:        # what people believe instead
status:             # sealed (no hints aired) | seeded (hints aired) | revealed
known_by: []        # [CH-…@origin, CH-…@S02E04]
hints: []           # episodes where clues are planted, in order
reveal:             # SxxEyy where the AUDIENCE learns the truth
reveal_steps: []    # earlier partial reveals (multi-step secrets)
public_on_reveal:   # true if the whole world learns it at reveal
min_seasons_hidden: # planned minimum gap (seasons) between first hint and reveal
depends_on: []      # SEC-… that must make sense first
related: []         # CH-/HS-/EV-/PL-/RULE- ids involved
```

Below each block: **Clues** (episode - what is shown). Full clue tables and red herrings: `studio/story/sealed/master_mystery.md` §5 (lead's file).

## Rules

1. A secret is **fair**: at least two hints before the reveal, the first at least one season earlier for `tier: saga`.
2. Hints are listed in episode order and all come before `reveal` (checked automatically).
3. `known_by` is the only place that says who knows what. A character cannot act on a secret before their `@episode`; the dead learn nothing (checked automatically). A character who only *suspects* is not listed.
4. When a character learns a secret on screen, the keeper adds `CH-…@SxxEyy` here.
5. When a hint airs: `status: seeded`; when the reveal airs: `status: revealed`, and the record becomes `locked`. Nothing has aired yet: every secret is `sealed`.
6. Secret IDs never appear in public-facing files (marketing, subtitles).
7. IDs: the lead's numbering is kept. `SEC-011` = the lead's SEC-011a (Quire); `SEC-011b` = the Chronicler. SEC-024…027 and the other restricted answers: `sealed/`.

## Overview

| ID | Title | Tier | First hint | Reveal | Status | Where |
|---|---|---|---|---|---|---|
| SEC-001 | The poisoned handshake | season | S01E01 | S01E11 | sealed | here |
| SEC-002 | The lullaby | saga | S01E01 | S03E10 | sealed | here |
| SEC-003 | The Breaking | saga | S01E01 | S05E10 | sealed | here |
| SEC-004 | Ama | saga | S01E02 | S04E10 | sealed | here |
| SEC-005 | The songblood lie | saga | S01E03 | S05E06 | sealed | here |
| SEC-006 | The forger's son | season | S01E04 | S06E08 | sealed | here |
| SEC-007 | Account Nine | season | S01E03 | S06E07 | sealed | here |
| SEC-008 | The thirst | saga | S01E12 | S07E10 | sealed | here |
| SEC-009 | The shut gate | season | S01E04 | S03E09 | sealed | here |
| SEC-010 | (restricted) | season | S01E11 | S09E11 | sealed | `sealed/` |
| SEC-011 | (restricted) | season | S06E09 | S11E06 | sealed | `sealed/` |
| SEC-011b | (restricted) | saga | S01E01 | S12E13 | sealed | `sealed/` |
| SEC-012 | The silenced mother / the Voice | season | S01E02 | S08E08 | sealed | here |
| SEC-013 | Who killed Ruel | season | S01E04 | S02E11 | sealed | here |
| SEC-014 | (restricted) | saga | S02E04 | S08E10 | sealed | `sealed/` |
| SEC-015 | The skipped song | season | S01E03 | S02E06 | sealed | here |
| SEC-016 | The Pearl Pretender | season | S06E03 | S08E06 | sealed | here |
| SEC-017 | (split: 017a / 017b, DEC-47) | — | — | — | retconned | here |
| SEC-017a | Nell is Lows-born | episode | S07E02 | S09E07 | sealed | here |
| SEC-017b | Tibb | season | S01E10 | S09E07 | sealed | here |
| SEC-018 | (restricted) | saga | S01E12 | S11E12 | sealed | `sealed/` |
| SEC-019 | Esk's mother | season | S01E12 | S07E06 | sealed | here |
| SEC-020 | (restricted) | season | S02E09 | S10E09 | sealed | `sealed/` |
| SEC-021 | (restricted) | saga | S04E11 | S10E10 | sealed | `sealed/` |
| SEC-022 | The new count of years | season | — | S09E12 | sealed | here |
| SEC-023 | Who silenced Sister Marl | season | S01E07 | S02E10 | sealed | here |
| SEC-024 | (restricted) | saga | S04E03 | S07E08 | sealed | `sealed/` |
| SEC-025 | (restricted) | saga | S01E01 | S10E10 | sealed | `sealed/` |
| SEC-026 | (restricted) | saga | S01E02 | S10E09 | sealed | `sealed/` |
| SEC-027 | (restricted) | saga | S01E01 | S12E11 | sealed | `sealed/` |
| SEC-028 | The broken pumps | season | S01E05 | S05E08 | sealed | here |
| SEC-029 | Ear-money | season | S01E05 | S04E06 | sealed | here |
| SEC-030 | The saltpeter sold twice | season | S01E04 | S03E11 | sealed | here |
| SEC-031 | The wreckers' wages | season | S01E04 | S02E09 | sealed | here |
| SEC-033 | The Lows-born hunter | episode | S01E02 | S05E12 | sealed | here |
| SEC-034 | The Broken Dike | season | — | S07E08 | sealed | here |
| SEC-035 | The fog on the Ostry bar | episode | — | S02E10 | sealed | here |
| SEC-036 | Harrow's deathbed will | season | — | S07E05 | sealed | here |
| SEC-037 | The map before the map | episode | S01E01 | S02E06 | sealed | here |
| SEC-038 | The pilots' night | episode | — | S03E02 | sealed | here |
| SEC-039 | The Goat Stair | season | — | S03E10 | sealed | here |
| SEC-040 | Retired codebooks | episode | S01E07 | S02E06 | sealed | here |
| SEC-041 | The walkers' union | season | S01E05 | S05E08 | sealed | here |
| SEC-042 | Two retainers | episode | S02E02 | S06E11 | sealed | here |
| SEC-043 | Ferro's bindings | episode | S05E03 | S05E10 | sealed | here |
| SEC-044 | Ottar's tongue | episode | S01E04 | S03E05 | sealed | here |
| SEC-045 | One copper | episode | S01E02 | S02E09 | sealed | here |
| SEC-046 | The second lamp | season | S01E01 | S01E09 | sealed | here |
| SEC-047 | The purser | saga | S01E07 | S03E06 | sealed | here (+ overlay in `sealed/`) |
| SEC-048 | The paper marriage | season | S07E03 | S12E12 | sealed | here (+ overlay in `sealed/`) |
| SEC-049 | The cut pages | season | S05E06 | S07E07 | sealed | here |
| SEC-050 | A beautiful hand | season | S01E01 | S06E08 | sealed | here |
| SEC-051 | Twice | episode | S01E07 | S02E06 | sealed | here |

SEC-032 was never issued (DEC-49: Lucan's sealed chest is already an approved fact).

## Restricted secrets - what may be shared

Answers are in `sealed/sealed.md` (readers: lead-screenwriter, lore-keeper, studio director). Production constraints below are safe for helpers, the director and the composer.

| ID | Constraint for scripts, art, music, marketing |
|---|---|
| SEC-010 | keep Maren sympathetic through S7 and arguable through S9 |
| SEC-011 | Hollis after S06E09 and Zev after S06E09 are not for helpers or marketing |
| SEC-011b | Chronicler voice design: excerpt for the sound director - `excerpts/for_sound_director.md` (v0.4, director's decision) |
| SEC-014 | no clue before S2, none explicit before S5; public material uses the official belief only |
| SEC-018 | — |
| SEC-020 | — |
| SEC-021 | — |
| SEC-024 | public line until S10: "the Dry Queen did not deny it"; dossiers name no culprit |
| SEC-025 | never in marketing, openings or previews before S10E10; the reversed lullaby in the S2 opening is the only planted audio clue (composer excerpt: `excerpts/for_composer.md`, v0.4) |
| SEC-026 | never in marketing, openings or previews before S10E10; nothing about Vesna's life before the Choir |
| SEC-027 | Ruel's ring and Pell's shard never share a frame before S12E11 (director and artist excerpt: `excerpts/for_director_and_artist.md`, v0.4) |

Open secrets with a restricted half (v0.7, r7): **SEC-047** - the open record stops at S06E09; marketing may show the line as a love story through S06E09 and as Maren's grief after it. **SEC-048** - the open record names only the public terms. The rest of both: `sealed/` §K.

---

## Records

### SEC-001 - The poisoned handshake

```canon
id: SEC-001
type: secret
canon: approved
title: The poisoned handshake
tier: season
truth: Ruel Corvane poisoned Helm Lucan Dask through a needle in his hollow black-pearl ring (poison bought from Sister Marl) to stop the Tithe Map that would let Ninth Sluice flood.
cover_story: Natural death; later 'Fennick did it'.
status: sealed
known_by: [CH-0005@origin, CH-0050@origin, CH-0058@origin, CH-0003@S01E11, CH-0006@S01E11, CH-0019@S06E08]
hints: [S01E01, S01E04, S01E06, S01E07, S01E09]
reveal: S01E11
public_on_reveal: false
related: [CH-0005, CH-0016, CH-0050, CH-0063, EV-0262, EV-0263, EV-0300, SEC-046]
```

Clues: S01E01 left-handed clasp, blood on the knuckle, "I don't drink before a storm" · S01E04 the hinged pearl; *(r7)* on the *Patient Gull* Ruel gives Jaro his right hand and keeps the ringed left behind his back · S01E06 "by the skin, not the mouth"; Juno lived · S01E07 Ruel burns one page; Marl dead with a Corvane mark · S01E09 "Forgive what I did for them." · S01E11 proof by chain (sight-draft EV-0263 + Marl + Ambry + Juno + Ione's sign for *hinge*). Becomes public in S6 *(r7: through the Account Nine file - the bank filed every Corvane draft, so publishing the bank publishes Ruel's sight-draft (EV-0263); on the eve of S06E07 Maren asks Hollis to cut that one page and he will not; SEC-047)*; Jaro learns it then and reads Ruel's unsent note of Longdark 5 (S06E08, EV-0280; SEC-046). Ruel told his sister (Longdark 5) and not his lover. Red herrings: the death-tone "too fast"; Garrick inherits.

### SEC-002 - The lullaby

```canon
id: SEC-002
type: secret
canon: approved
title: The lullaby
tier: saga
truth: Nan's five-note lullaby is the Low Note - the missing low part of every Spire's song; Pell carries it.
cover_story: A Lows cradle song.
status: sealed
known_by: [CH-0015@origin, CH-0065@origin, CH-0001@S03E10]
hints: [S01E01, S01E05, S01E10, S01E12, S02E03, S02E08, S03E04]
reveal: S03E10
public_on_reveal: false
min_seasons_hidden: 1
related: [CH-0001, CH-0015, HS-094, EV-0310, RULE-004]
```

Clues: S01E01 the shard hums back (only Wick sees) and rings a note no relay uses · S01E05 the Sluice Spire steadies for three seconds · S01E10 the low hum joins Ione's Great Song · S01E12 the Sunken Spire's crown rings faintly · S02E03 Nan: "Not there. Never there." · S02E08 "It's not in the blood. It's in the mouth." · S2 opening: the lullaby reversed under the strings · S03E04 the Quiet whistle the five notes as a password. Why no relay stone ever answered: RULE-004 prose.

### SEC-003 - The Breaking

```canon
id: SEC-003
type: secret
canon: approved
title: The Breaking
tier: saga
truth: In OS 700 the Nine warden families (led by Ilvane, with Corvane ships sealing the harbour) massacred the people's chorus at Lirenne during the Still Days; that broke the Spire and drowned the city; Neveh was not mad; the people used to sing the Spires together, and the Hush Law exists to stop that; Oshra, Neveh's servant and Pell's ancestress, escaped carrying the last verse, and her line keeps it in the Quiet.
cover_story: The Sunken Queen went mad and sang her city into the sea.
status: sealed
known_by: [CH-0015@origin, CH-0065@origin, CH-0060@origin, CH-0001@S05E10]
hints: [S01E01, S01E02, S01E08, S02E05, S03E04, S03E06, S04E07, S05E03]
reveal: S05E10
public_on_reveal: false
min_seasons_hidden: 1
related: [CH-0030, CH-0031, HS-008, HS-003, HS-001, EV-0100, RULE-006]
```

Clues: S01E01 tapestry: crowds behind the Queen, a servant girl with a **left braid**, a cormorant sail blocking the harbour · S01E02 "Oshra - an old Lows name, it means nothing" · S01E08 hands over mouths in the Still Days rite · S02E05 a rack of Ilvane "spears of the Breaking" · S03E04 "one of Oshra's daughters" · S03E06 bones in rows on the Lirenne shore, hands over mouths · S04E07 Elm translates "what was needed" as "what was holy" · S05E03 Ferro: the Chronicle of OS 700 was written in CY 40. The Lows learn it S05E11. Also reveals Maren's ancestor (Corvane ships, S05E10).

### SEC-004 - Ama

```canon
id: SEC-004
type: secret
canon: approved
title: Ama
tier: saga
truth: Ione is Ama, elder daughter of Liss and Dov of Ninth Sluice (born CY 294-03), Pell's sister, taken as a baby by Sister Venn on the Night of Still Water and installed as Cressa Ilvane's daughter; her silver hair is a rinse.
cover_story: Ione is Cressa Ilvane's daughter, born Mistcall CY 294.
status: sealed
known_by: [CH-0012@origin, CH-0056@origin, CH-0020@origin, CH-0021@origin, CH-0002@S04E10, CH-0001@S04E10]
hints: [S01E02, S01E03, S01E05, S02E05, S02E10, S03E07, S03E12, S04E04]
reveal: S04E10
public_on_reveal: false
min_seasons_hidden: 1
related: [CH-0002, CH-0023, CH-0024, CH-0056, CH-0068, EV-0201]
```

Clues: S01E02 "I had a sister. The water took her before I was born." · S01E03 the Cantor's rinse · S01E05 Ione hums two notes back · S02E05 infant grave dated Reedmonth CY 294 · S02E10 Ione hums two notes in her sleep; Elm goes pale · S03E07 Gleaner ledger "Ninth Sluice, female, one year, ear true - mother Liss" · S03E12 Venn tells Ione she was gleaned; dark roots · S04E04 Nan's sketch of Liss. Ione knows she was gleaned from S03E12; the full truth S04E10. S02E10 - Elm: partial (gleaned, Lows, the lullaby; not who) - not a knower (DEC-80, r8): he does not know her name, her parents or that she has a sister; his place inside SEC-012 lets him suspect more, and no script lets him confirm, name or act on it before S04E10, where her *"You knew."* and his yes mean exactly this.

### SEC-005 - The songblood lie

```canon
id: SEC-005
type: secret
canon: approved
title: The songblood lie
tier: saga
truth: The ear is taught, not inherited - and only by the Low Note lullaby hummed to a child before about seven; the Steps outlawed and forgot it, so the Choir cannot breed or train its own Cantors and lives on gleaned Lows children; every year the Hush Law is enforced there are fewer ears - the hidden reason the Spires are failing now.
cover_story: The ear is in the blood (RULE-002).
status: sealed
known_by: [CH-0012@origin, CH-0021@S05E06, CH-0001@S05E06]
hints: [S01E03, S02E05, S03E07, S04E10]
reveal: S05E06
public_on_reveal: true
min_seasons_hidden: 1
related: [HS-003, HS-090, RULE-002, EV-0052, EV-0318]
```

Clues: S01E03 Lows "foundlings blessed by the Lady" among the novices · S02E05 an adult Ilvane cousin without the ear kept "for her nerves" · S03E07 the Gleaner ledger: all entries under age 7 · S04E10 Ione (Lows-born) and Pell have the ear. Published S05E06 (EV-0318) - a public scandal.

### SEC-006 - The forger's son

```canon
id: SEC-006
type: secret
canon: approved
title: The forger's son
tier: season
truth: Teodor Kett forged the Dry Charter; Ursel Lantry had him drowned in CY 296 and raised his son Hollis.
cover_story: Teodor drowned drunk.
status: sealed
known_by: [CH-0011@origin, CH-0003@S06E08]
hints: [S01E04, S01E11, S02E03, S04E06, S05E08]
reveal: S06E08
public_on_reveal: false
related: [CH-0003, CH-0011, CH-0025, EV-0203, EV-0204, EV-0276, SEC-050]
```

Clues: S01E04 "T. Kett" on the charter · S01E11 "His father had a beautiful hand." · S02E03 Pruitt: drowned "on a night without rain, in a canal knee-deep" · S04E06 Hollis's forgery mistaken for an old document - "the same hand" · S05E08 Silt sells Hollis the boatman who saw it. *(r7)* Why he forged and why she raised the boy: SEC-050 (they were lovers, CY 291-296; he forged because she asked; her kindness to Hollis was never a mask). The S04E06 "second document in his father's hand" that Hollis puts away unread is a letter that begins *"U. -"*.

### SEC-007 - Account Nine

```canon
id: SEC-007
type: secret
canon: approved
title: Account Nine
tier: season
truth: The Lantry Counting House issues dry-notes against land it expects to be let flood; about 70% of notes are unbacked by S6.
cover_story: Notes are backed by dry land.
status: sealed
known_by: [CH-0011@origin, CH-0016@origin, CH-0003@S01E06, CH-0006@S01E07, CH-0005@S01E07]
hints: [S01E03, S01E06, S02E02, S05E04, S06E04]
reveal: S06E07
public_on_reveal: true
related: [HS-007, CH-0011, CH-0003]
```

Clues: Hollis and the audience learn the Ninth Sluice part in S01E03-E06; the scale of the fraud is the S06E07 reveal. S01E03 "Account Nine closes on the third Still Day" · S02E02 Lantry notes pay Fennick's mercenaries · S05E04 note prices crash in the Lows only · S06E04 Ursel's two ledgers.

### SEC-008 - The thirst

```canon
id: SEC-008
type: secret
canon: approved
title: The thirst
tier: saga
truth: The detuned, solo-sung Spires pull river water from the uplands (mechanism: RULE-012); the Spires are why the Ossari starve; in CY 138-141 Vanth discovered it, sang the Falls Spire less and was destroyed for it.
cover_story: Upland drought is weather or divine punishment; Vanth sold the Stair.
status: sealed
known_by: [CH-0047@origin, CH-0041@S07E10, CH-0042@S07E10, CH-0006@S07E12]
hints: [S01E12, S03E05, S03E08, S05E12, S06E04, S07E03]
reveal: S07E10
public_on_reveal: true
min_seasons_hidden: 1
related: [HS-091, HS-012, HS-004, CH-0013, CH-0040, CH-0047, EV-0150, RULE-012]
```

Clues: S01E12 Ossari fires (why now?) · S03E05 "Your stones drink our rivers" - laughed at · S03E08 the falls swell with no rain when the Falls Spire is sung; Esk's knotted cord · S4 the silenced Spire and the weir confound the cause · S05E12 Tsura's letter: falls thin, Shelf wells up a hand · S06E04 upland grain futures dated by the Choir's song calendar · S07E03 Dorran's gauges · S07E10 proof: gauges + Choir song logs + the Vanth river book. The Ossari *believe* it from S3 (belief is not knowledge).

### SEC-009 - The shut gate

```canon
id: SEC-009
type: secret
canon: approved
title: The shut gate
tier: season
truth: At seventeen Kes Mabry shut the Ninth Sluice evacuation gate on her captain's order on the Night of Still Water.
cover_story: Nobody knows who shut it.
status: sealed
known_by: [CH-0004@origin, CH-0040@S03E09, CH-0001@TODO(DEC-54)]
hints: [S01E04, S01E10, S02E06]
reveal: S03E09
public_on_reveal: false
related: [CH-0004, PL-0021, EV-0200]
```

Clues: S01E04 Kes avoids looking at the gate · S01E10 she opens it: "Not twice." · S02E06 she drinks alone on the anniversary of her **first stripe** (Rains 12, CY 296, "for steadiness at the Ninth Sluice gate") - she does not drink to it, she drinks at it (DEC-16) · S03E09 confession before the battle, heard first by Esk (DEC-54). Pell learns it later from Kes herself, not before S5: `CH-0001@TODO(DEC-54)` stays until the S5 outline fixes the episode.

### SEC-012 - The silenced mother / the Voice

```canon
id: SEC-012
type: secret
canon: approved
title: The silenced mother / the Voice
tier: season
truth: Liss was drowned in CY 305 on the First Cantor's order after she found Sister Venn and demanded her daughter back; Brother Elm is a Quiet child planted in the Choir who sometimes mistranslates Vesna on purpose.
cover_story: Liss drowned; Elm is a loyal foundling.
status: sealed
known_by: [CH-0012@origin, CH-0056@origin, CH-0022@origin, CH-0045@S07E07, CH-0001@S08E08]
hints: [S01E02, S02E09, S03E07, S04E04, S04E08, S07E07]
reveal: S08E08
public_on_reveal: false
related: [CH-0012, CH-0022, CH-0023, EV-0205, EV-0261, SEC-049]
```

Clues: S01E02 Liss "drowned in a dry year"; Nan asks only *where* the shard was found and lays salt and a shell there · S02E09 Vesna signs an order while Elm says "a blessing for the sick" · S03E07 ledger "mother - silenced, CY 305" · S04E04 Nan's sketch of Liss with a small dark stone at her throat · S04E08 Elm signs a spiral to Pell · S07E07 Daro catches Elm mistranslating (he knows only the Voice part from here) *(r7: and finds in his cell the pages cut from Ione's journal, SEC-049 - the Choir's proof against him)*. *(r7)* Elm's place in the Choir depends on this silence - the reason he does not tell Ione what he understands at S02E10 (line L5).

### SEC-013 - Who killed Ruel

```canon
id: SEC-013
type: secret
canon: approved
title: Who killed Ruel
tier: season
truth: Ursel Lantry and Garrick Dask hired the assassin because Ruel would expose Account Nine: Orm Hask, a Moll-born pikeman of the Lantern Company, chosen and handed over by Rook Danner and paid through Garrick Dask's steward (DEC-36).
cover_story: Fennick did it; or Quell (the token).
status: sealed
known_by: [CH-0011@S01E04, CH-0017@S01E04, CH-0059@S01E08, CH-0055@S02E07, CH-0006@S02E11, CH-0003@S02E11, CH-0076@origin]
hints: [S01E04, S01E08, S01E09, S02E02, S02E06, S02E07]
reveal: S02E11
public_on_reveal: false
related: [CH-0005, CH-0011, CH-0017, CH-0059, HS-095, EV-0302, SEC-046]
```

Clues: S01E04 Garrick leaves Ursel's office by the back stair · S01E08 the Quell token (herring) · S01E09 Polder clay on the assassin's boots; *(r7)* Jaro, asked where he was on the night of Still 1: *"On a deck. Waiting on the weather."* · S02E02 Rook Danner paid in Lantry notes · S02E06 Lucan Dask's sealed chest: his will and the unsigned Tithe Map, suppressed by Garrick (DEC-49) · S02E07 Fossett's private ledger. Proof in S2 needs two paper trails added together: Danner's notes and the steward's purse (DEC-36). *(r7)* The Quell frame holds for a season because Jaro's alibi cannot be spoken: he was waiting on the *Patient Gull* under the second lamp (SEC-046). The audience knows it from S01E08-E09; the Ring does not.

### SEC-015 - The skipped song

```canon
id: SEC-015
type: secret
canon: approved
title: The skipped song
tier: season
truth: Ursel Lantry bribed Fennick's steward to have Cantor Sabin skip the Still Day retuning of the Sluice Spire in CY 312; Odo did not know.
cover_story: An old Spire failing.
status: sealed
known_by: [CH-0011@S01E03, CH-0057@S01E09, CH-0003@S02E06]
hints: [S01E03, S01E09, S01E10]
reveal: S02E06
public_on_reveal: false
related: [CH-0011, CH-0057, CH-0010, EV-0304]
```

Clues: S01E03 "Account Nine closes on the third Still Day" · S01E09 Sabin's new purse · S01E10 Sabin sings late and sings out · S02E06 Hollis matches the purse's notes to Fennick's steward.

### SEC-016 - The Pearl Pretender

```canon
id: SEC-016
type: secret
canon: approved
title: The Pearl Pretender
tier: season
truth: Lio is not of Ashare blood; Quell salvage-brokers and Piers Lantry made his claim up to sell Lirenne salvage bonds as the dry-notes begin to crack (from S6E5, DEC-18); the fraud splits the Lows' vote (giving Maren the Helm) and makes raising Lirenne a money interest; Lio himself believes it.
cover_story: Last heir of the Tide-Kings.
status: sealed
known_by: [CH-0061@S06E01, CH-0060@S06E10, CH-0019@S07E05, CH-0001@S08E06]
hints: [S06E03, S06E05, S06E10, S07E05]
reveal: S08E06
public_on_reveal: true
related: [CH-0043, CH-0061, HS-005, HS-008, EV-0327]
```

Clues: S06E03 Lio draws the spiral counter-clockwise (Ashare spirals turn sunwise) · S06E05 Piers sells "Lirenne bonds" the day after Lio's first speech; *(r7)* S06E05-E06 the brokers script a betrothal, "the Pearl and the Singer", to bring the Hum under the bonds - Lio means it, Pell refuses him in public (deepens the split of the Lows' vote) · S06E10 his pearl is a Quell trade pearl - Ferro: "A Keeper's pearl is black, and hollow." · S07E05 Jaro's laugh. *(r7)* S08E04-E06: Lio's brokers sell the Pell-Esk kite-code to the Dry Palace watch; dying (S08E06) Lio tells Pell what he sold. Who exposes the Pretender in public at S08E06 is open for the S8 outline (lead's question, `romance_lines.md` §8).

### SEC-017 - Tibb (split, DEC-47)

```canon
id: SEC-017
type: secret
canon: retconned
title: Tibb
tier: season
truth: Split by the lead screenwriter (DEC-47, r3) into SEC-017a (Nell Tern is Lows-born) and SEC-017b (Tibb is Sal Tern's daughter); kept for history.
cover_story: A foundling.
status: sealed
known_by: []
hints: [S01E10, S07E02, S08E04]
reveal: S09E07
public_on_reveal: false
related: [SEC-017a, SEC-017b]
```

Retconned in v0.4: the ID stays retired; records link SEC-017a / SEC-017b.

### SEC-017a - Nell is Lows-born

```canon
id: SEC-017a
type: secret
canon: approved
title: Nell is Lows-born
tier: episode
truth: Nell Tern, Maren's midshipwoman, is secretly Lows-born; Sal Tern of the Ninth is her younger sister.
cover_story: A Mids-born naval officer.
status: sealed
known_by: [CH-0044@origin, CH-0067@origin, CH-0001@S09E07]
hints: [S07E02, S08E04]
reveal: S09E07
public_on_reveal: false
related: [CH-0044, CH-0067]
```

Clues: S07E02 Nell whistles a Lows tune · S08E04 Nell at a Lows grave "Sal". (DEC-47.)

### SEC-017b - Tibb is Sal Tern's daughter

```canon
id: SEC-017b
type: secret
canon: approved
title: Tibb
tier: season
truth: Tibb is the daughter of Sal Tern, Nell Tern's drowned younger sister.
cover_story: A foundling.
status: sealed
known_by: [CH-0044@S09E07, CH-0001@S09E07]
hints: [S01E10, S08E04]
reveal: S09E07
public_on_reveal: false
related: [CH-0046, CH-0044, CH-0067, EV-0305]
```

Clues: S01E10 the cradle tied with a navy knot · S08E04 Nell at a Lows grave "Sal" (the name). Function: Nell saves Tibb, not Wick, at the Ninth Bridge, and her testimony delivers a restricted secret. Both halves reach the audience in S09E07 (DEC-47).

### SEC-019 - Esk's mother

```canon
id: SEC-019
type: secret
canon: approved
title: Esk's mother
tier: season
truth: Esk is Tsura Den's son by Akko of Kitsa, her glider-captain companion killed in the Rim Skirmish (CY 309); he was given as hostage that season under the name of her nephew (DEC-20, DEC-33).
cover_story: Her nephew.
status: sealed
known_by: [CH-0013@origin, CH-0040@origin, CH-0071@origin]
hints: [S01E12, S03E03, S04E09]
reveal: S07E06
public_on_reveal: false
related: [CH-0040, CH-0013, CH-0078]
```

Clues: S01E12 Esk's kite-signal "mother" (subtitled "home") · S03E03 Tsura's same left-ear ring · S04E09 Tsura risks a truce for "a nephew".

### SEC-022 - The new count of years

```canon
id: SEC-022
type: secret
canon: approved
title: The new count of years
tier: season
truth: At her coronation on the Still Days of CY 325 Maren proclaims the Sovereign Years (SY 1 = CY 326).
cover_story: -
status: sealed
known_by: [CH-0006@S09E12]
reveal: S09E12
public_on_reveal: true
related: [CH-0006, ERA-SY, EV-0332]
```

Clues: Tier not set by the lead ("—"); recorded as season. Planting: era stamps on every date from S1; echoes S06E12, S08E11.

### SEC-023 - Who silenced Sister Marl

```canon
id: SEC-023
type: secret
canon: approved
title: Who silenced Sister Marl
tier: season
truth: Lady Ysa Corvane had the apothecary killed to bury her brother's crime, which she has known since Longdark 5 (CY 312); it is also why she later sells Gullmouth - she judges that Maren will ruin the house the way Ruel did.
cover_story: Fennick's Listeners killed her and planted the Corvane coin.
status: sealed
known_by: [CH-0058@origin, CH-0006@S02E10]
hints: [S01E07, S01E09, S01E11, S02E04]
reveal: S02E10
public_on_reveal: false
related: [CH-0058, CH-0050, EV-0301, EV-0308, EV-0341, SEC-046]
```

Clues: S01E07 Corvane coin in Marl's fist · S01E09 Ysa arrives a day before the Relay could have called her; *(r7)* she empties the cabin locker - a packet in tarred twine goes into her sleeve (double reading: first as evidence of the poison, truly SEC-046) · S01E11 her unspoken "condition": Ysa confirms - and keeps the seal (DEC-03) · S02E04 her boatswain pays for a Choir funeral · S02E10 "I have been burying your father for a year." *(r7: she lays down two things - the boatswain's discharge and the packet: "There were two things to bury.")*

### SEC-028 - The broken pumps

```canon
id: SEC-028
type: secret
canon: approved
title: The broken pumps
tier: season
truth: The Pumpwrights' Guild saws pump axle-pins before every Still Days to sell new pumps; in CY 312 that breakage stopped Ninth Sluice's three treadmill pumps on the flood night and doubled the dead; Corr kept the sawn pin; Dorran Strand's faith in a world without songs is built on that guilt.
cover_story: Old pumps fail.
status: sealed
known_by: [CH-0041@origin, CH-0048@S01E10]
hints: [S01E05, S01E10, S02E04, S05E03]
reveal: S05E08
public_on_reveal: false
related: [HS-092, CH-0041, CH-0048, EV-0305, EV-0319]
```

Clues: S01E05 Corr: "They always break the week before the Still. Funny, that." · S01E10 jammed wheels; Corr pockets the sawn pin · S02E04 "relief pumps" sold at Fennick's expense · S05E03 Dorran cannot look at a treadmill · S05E08 the pin on Dorran's desk. Not public: Corr trades silence for the Guild's barges on the Night of a Thousand Voices.

### SEC-029 - Ear-money

```canon
id: SEC-029
type: secret
canon: approved
title: Ear-money
tier: season
truth: Gleaners are paid by the head; Sister Venn's novices pad their count with children who have no ear and sell the returned ones as debt-walkers through an Undertow under-boss; Mother Silt's purge of that trade in S4 produces the ledger that proves gleaning wholesale.
cover_story: Returned children ran away.
status: sealed
known_by: [CH-0014@S04E06, CH-0073@origin, CH-0077@origin]
hints: [S01E05, S03E07, S04E02]
reveal: S04E06
public_on_reveal: false
related: [HS-090, HS-093, CH-0056, CH-0014, CH-0064]
```

Clues: S01E05 the Gleaner novice counting coins · S03E07 a price column in the Gleaner ledger · S04E02 Patch and other debt-walkers all "came back from the robes" · S04E06 Silt drowns her under-boss in his own account book. Public in S5 (with SEC-005).

---

## New secrets v0.3 (approved v0.4)

Status: **approved** by the lead screenwriter in r3 (numbers, tiers and reveals: DEC-37, DEC-38…41, DEC-45). Final numbers given by the keeper: writer-characters' SEC-030 and SEC-031 kept; their SEC-032 (Lucan's chest) is **not issued** - the chest's content is already an approved fact (CH-0016, `world.md` §6) and its wording is DEC-49; writer-houses' candidates SEC-C01...C07 became SEC-034...040; the writer-characters minor secrets became SEC-033 and SEC-041...045. None touches the origin of a main hero or a restricted answer.

### SEC-030 - The saltpeter sold twice

```canon
id: SEC-030
type: secret
canon: approved
title: The saltpeter sold twice
tier: season
truth: Lady Brenna Rusk began selling Rusk powder back up the escarpment through Clan Tekka (the envoy Itsek) to pay her pikes when the Helm's contracts were late (from about CY 302); her Captain-Quartermasters (House Grell) made it a business and sell the upland saltpeter twice (the gate book and the cliff book); at the Battle of the Stair the Ossari fire Rusk powder.
cover_story: Saltpeter lost to damp; the Stair keeps honest stores.
status: sealed
known_by: [CH-0018@origin, CH-0072@origin]
hints: [S01E04]
reveal: S03E11
public_on_reveal: false
related: [CH-0018, CH-0072, CH-0004, HS-004, HS-026, HS-091, EV-0311]
```

Source: writer-characters SEC-030 (Brenna, Itsek) + writer-houses scheme "saltpeter sold twice" (HS-004, HS-026). The quartermasters' trade after the fall of the Stair: HS-004 dossier.

### SEC-031 - The wreckers' wages

```canon
id: SEC-031
type: secret
canon: approved
title: The wreckers' wages
tier: season
truth: Quell wrecker silver (Clan Rhee's false lights) has quietly paid part of the Corvane fleet's wages and refit debt - about 30,000 marks since CY 305, never written down - which is why Jaro backs Ruel and then Maren.
cover_story: An old friendship of sailors (the Pilots' Peace).
status: sealed
known_by: [CH-0019@origin, CH-0005@origin, CH-0006@S02E09]
hints: [S01E04]
reveal: S02E09
public_on_reveal: false
related: [CH-0019, CH-0005, CH-0006, HS-005, HS-020, HS-001, EV-0277, SEC-046]
```

Source: writer-characters SEC-031 + writer-houses HS-001/HS-005 (same fact). *(r7)* The silver begins the year the liaison does (CY 305, EV-0277): the money was always the shadow of the love, and both hide behind the same sentence, "an old friendship of sailors" (SEC-046). At S02E09 Maren thinks she has understood the friendship; she learns the rest at S02E10.

### SEC-033 - The Lows-born hunter

```canon
id: SEC-033
type: secret
canon: approved
title: The Lows-born hunter
tier: episode
truth: Captain Fitch was born in the Fifth Sluice; as a boy he informed on his own lane's singers to buy his mother a room up the Steps - Pell's dream, paid the other way.
cover_story: A Mids officer with no accent.
status: sealed
known_by: [CH-0053@origin, CH-0001@S05E12]
hints: [S01E02]
reveal: S05E12
public_on_reveal: false
related: [CH-0053, CH-0001, PL-0083, EV-0319]
```

Source: writer-characters (Fitch). Hint: the only Listener who whistles like the Lows.

### SEC-034 - The Broken Dike

```canon
id: SEC-034
type: secret
canon: approved
title: The Broken Dike
tier: season
truth: In CY 87 Wardel Dask's Cantors sang the Sheaf Spire short over the Moll polders for three nights in a storm: Dask fields held and the river drowned Moll's; Moll did not cut its dikes - the first recorded letting-go of a district, 224 years before Account Nine.
cover_story: The lords of Moll cut their own dikes to drown their neighbours, and the sea drowned them instead.
status: sealed
known_by: []
hints: []
reveal: S07E08
public_on_reveal: false
related: [HS-002, HS-010, HS-017, HS-018, EV-0250, CH-0017]
```

Source: writer-houses candidate SEC-C01. Kept by the Kellow knights' clapped grievance-song and by Wardel Dask's song-log in the Barrows archive.

### SEC-035 - The fog on the Ostry bar

```canon
id: SEC-035
type: secret
canon: approved
title: The fog on the Ostry bar
tier: episode
truth: In CY 119 Wystan Corvane's escort captain lost Lord Weylin Ostry's ship on the Ostry bar on purpose; Ostry's heiress then married Wystan.
cover_story: Lost at sea in fog.
status: sealed
known_by: [CH-0058@origin, CH-0006@S02E10]
hints: []
reveal: S02E10
public_on_reveal: false
related: [HS-011, HS-027, HS-001, CH-0204, CH-0278, CH-0279, EV-0251]
```

Source: writer-houses candidate SEC-C02; a family story of the Corvane-of-the-Roads cadets. Optional colour for S2.

### SEC-036 - Harrow's deathbed will

```canon
id: SEC-036
type: secret
canon: approved
title: Harrow's deathbed will
tier: season
truth: Osbert Harrow's will of CY 247 left the Hill Voice to his natural son's line (Kilbride); the deathbed will of CY 251 that leaves it to the holder of his debts was drafted by Lantry clerks during his fever and witnessed by the Fennick Relay-Master; the Kilbrides keep a copy of the first will.
cover_story: Osbert freely bequeathed the voice to the bank.
status: sealed
known_by: []
hints: []
reveal: S07E05
public_on_reveal: false
related: [HS-009, HS-032, HS-007, HS-006, CH-0270, EV-0254]
```

Source: writer-houses candidate SEC-C03.

### SEC-037 - The map before the map

```canon
id: SEC-037
type: secret
canon: approved
title: The map before the map
tier: episode
truth: Inchley clerks of the Map Office sell drafts of the Tithe Map weeks before the reading - to the Undertow (which prices dry-pledges by them), the Cobbets and the bank; the CY 312 draft already showed Ninth Sluice let go in Inchley's hand.
cover_story: The map is secret until the Helm reads it.
status: sealed
known_by: [CH-0014@origin, CH-0011@origin]
hints: [S01E01]
reveal: S02E06
public_on_reveal: false
related: [HS-015, HS-093, HS-014, HS-007, PL-0078]
```

Source: writer-houses candidate SEC-C04. Surfaces with Lucan's chest (S02E06): Inchley draft marks beside Ursel's notes.

### SEC-038 - The pilots' night

```canon
id: SEC-038
type: secret
canon: approved
title: The pilots' night
tier: episode
truth: The night Lady Ysa opens Gullmouth, Clan Skarra pilots bring Fennick's ships over the bar, paid by Ysa through the Corvane-of-the-Roads cadets, not by Fennick; it looks like Quell's treachery.
cover_story: Quell sold Gullmouth.
status: sealed
known_by: [CH-0058@S02E10]
hints: []
reveal: S03E02
public_on_reveal: false
related: [HS-022, HS-027, CH-0058, CH-0019, EV-0308]
```

Source: writer-houses candidate SEC-C05. Timing (DEC-41): Jaro is blamed from S2E11 until S3E2; Ysa knows from S2E10.

### SEC-039 - The Goat Stair

```canon
id: SEC-039
type: secret
canon: approved
title: The Goat Stair
tier: season
truth: The Hadden family of Rimgate guides the quartermasters' back-trade up the Goat Stair, an unguarded path two miles from the Stair; whoever knows it can move men or powder past the Stair.
cover_story: The Stair is the only road up the escarpment.
status: sealed
known_by: []
hints: []
reveal: S03E10
public_on_reveal: false
related: [HS-025, HS-026, PL-0073, SEC-030]
```

Source: writer-houses candidate SEC-C06.

### SEC-040 - Retired codebooks

```canon
id: SEC-040
type: secret
canon: approved
title: Retired codebooks
tier: episode
truth: The Tennant Relay-Wardens sell retired codebooks and take a cut of their keepers' private sales; Hollis's bought codebook (S1E7) came down this chain, and Bede Lark's double sale happened on a Tennant tower.
cover_story: Codebooks are burned when retired.
status: sealed
known_by: [CH-0052@origin]
hints: [S01E07]
reveal: S02E06
public_on_reveal: false
related: [HS-030, HS-006, CH-0052, CH-0003, EV-0262]
```

Source: writer-houses candidate SEC-C07.

### SEC-041 - The walkers' union

```canon
id: SEC-041
type: secret
canon: approved
title: The walkers' union
tier: season
truth: Corr runs a secret union of the treadmill walkers under the Guild - cells by wheel, signals in a stamped rhythm (Hush-Law-legal) - that can stop every pump in Highwater.
cover_story: The walkers are unorganised debt-labour.
status: sealed
known_by: [CH-0048@origin]
hints: [S01E05, S02E04]
reveal: S05E08
public_on_reveal: false
related: [CH-0048, CH-0041, HS-092]
```

Source: writer-characters (minor) + writer-houses (HS-092). Pays S5E8 (the pin) and S6 (the strike).

### SEC-042 - Two retainers

```canon
id: SEC-042
type: secret
canon: approved
title: Two retainers
tier: episode
truth: Rook Danner holds a Lantry retainer and a Quell one and keeps both receipts.
cover_story: A mercenary loyal to his paymaster.
status: sealed
known_by: [CH-0059@origin]
hints: [S02E02]
reveal: S06E11
public_on_reveal: false
related: [CH-0059, HS-095, HS-007, HS-005, EV-0322]
```

Source: writer-characters (minor). Pays when he switches sides in the Battle of the Shoals.

### SEC-043 - Ferro's bindings

```canon
id: SEC-043
type: secret
canon: approved
title: Ferro's bindings
tier: episode
truth: Archivist Ferro has copied forbidden Ashare texts for thirty years and sewn the copies into the bindings of hymn-books.
cover_story: A harmless old archivist.
status: sealed
known_by: [CH-0060@origin]
hints: [S05E03]
reveal: S05E10
public_on_reveal: false
related: [CH-0060, HS-090, HS-008]
```

Source: writer-characters (minor).

### SEC-044 - Ottar's tongue

```canon
id: SEC-044
type: secret
canon: approved
title: Ottar's tongue
tier: episode
truth: Corporal Ottar is Ossari-born - a hostage-child raised at the Stair, Kadu's cousin - and hides his birth in the ranks; he has not spoken his own tongue in fifteen years.
cover_story: A Stair-born soldier.
status: sealed
known_by: [CH-0062@origin, CH-0018@origin, CH-0047@origin]
hints: [S01E04]
reveal: S03E05
public_on_reveal: false
related: [CH-0062, CH-0047, HS-004, HS-091]
```

Source: writer-characters (minor). The roster already says he is Ossari-born; the secret is that he hides it among Rusk soldiers.

### SEC-045 - One copper

```canon
id: SEC-045
type: secret
canon: approved
title: One copper
tier: episode
truth: In S1E2 Mags sold Silt's fence Tuck "a stone that sings back" and the lane, for one copper - nothing about where it was found; that is how the Listeners learned the lane, not just the relay log.
cover_story: The Listeners traced the stone by the relay log.
status: sealed
known_by: [CH-0049@S01E02, CH-0074@S01E02, CH-0001@S02E09]
hints: [S01E02]
reveal: S02E09
public_on_reveal: false
related: [CH-0049, CH-0074, CH-0053, CH-0001]
```

Source: writer-characters (minor). Pell learns it in S2E9, the episode after Nan's death (DEC-45).

## New secrets v0.7 - the love lines (r7, approved)

Source: `studio/story/romance_lines.md` §7 (lead screenwriter, r7; approved DEC-73). Numbers SEC-046…051 proposed by the lead are **confirmed** by the keeper (no clash; SEC-032 stays unissued). Restricted halves (SEC-047 after S06E09, the terms of SEC-048, the price of S10 in SEC-046) are in `sealed/sealed.md` §K only. Age gate (DEC-71): every pair below is 18+ by birth year at the moment of its relation (validator check).

### SEC-046 - The second lamp

```canon
id: SEC-046
type: secret
canon: approved
title: The second lamp
tier: season
truth: Ruel Corvane and Jaro Quell were lovers from CY 305 until Ruel's death; the Quell wrecker silver (SEC-031) followed the love; the signal was a second stern lamp on the Patient Gull (one lamp - the Admiral is aboard; two - come).
cover_story: An old friendship of sailors.
status: sealed
known_by: [CH-0005@origin, CH-0019@origin, CH-0058@origin, CH-0006@S02E10, CH-0010@S02E11, CH-0042@S05E12]
hints: [S01E01, S01E04, S01E06, S01E08]
reveal: S01E09
public_on_reveal: false
related: [CH-0005, CH-0019, CH-0058, CH-0006, CH-0010, CH-0042, EV-0277, EV-0280, EV-0341, EV-0342, SEC-031, SEC-013, SEC-023]
```

Why hidden: a Captain-Lord can be deposed by three clans of five at any Hull Moot, and clan silver spent on a lover's fleet is a deposing matter; a candidate for Helm whose swing vote shares his cabin hands his rival a challenge. No letters signed, no shared roof. Hidden for votes, never for shame (`romance_lines.md` §0.6).
Clues: S01E01 *(director's decision r7, background seed)* Sc 12 - when the hall runs to the dying Helm, one figure in the sea-green Quell block stands still and looks at Ruel (from behind, no name, no line, no reference sheet) · S01E04 the second stern lamp is hung; *"I'm loyal to whoever pays and respects me, Admiral. You're halfway there."*; Ruel gives the right hand, keeps the ringed left behind his back; Ione sees two lamps from the quay · S01E06 the corridor: *"You were very good in there. Very ready." - "A storm is coming. Be ready too."* · S01E08 two lamps lit as the procession sets out, a man in a green sash waiting at the rail, back to us · **S01E09 reveal (audience only)**: Ysa bars Jaro (*"House only tonight, Captain-Lord."*), takes the packet in tarred twine; at the wake Jaro, let in last and alone, puts out the second lamp and takes the dead man's right hand; Chronicler: *"The Captain-Lord of the Shoals paid his respects last."* (the record states the fact, never the cause). Echoes: S01E12 Jaro's vote, *"Calm is bought. This one was paid for."*; Quell hulls astern of the fleet.
After S1 (consequences): S02E10 Ysa lays the packet before Maren - *"There were two things to bury."* · S02E11 Ysa gives the packet to Odo as her pledge for Gullmouth: from now on the Listener can unseat Jaro at any moot (cause of "trades with both sides", S3-S5) · S05E12 Zev inherits it and S06E02 sends it back **unopened** - Zev is listed as a knower at the lead's instruction: he knows *that* the packet is the Captain-Lord's letters and what hold it gives, not what they say · S06E08 Jaro finds Ruel's unsent note of Longdark 5 in it (EV-0280) · S07E03 Jaro witnesses the Helm's wedding and does not object (his debt to Zev) · S09E05 the break · S10 the price of his neutrality: `sealed/` §K · S11E08 dies. Objects: the second lamp and the packet - `world.md` §6.

### SEC-047 - The purser

```canon
id: SEC-047
type: secret
canon: approved
title: The purser
tier: saga
truth: Maren Corvane and Hollis Kett love each other from S2 and are lovers from S04E12; she trusts his columns before she trusts him, and each time she must choose between him and the name she chooses the name.
cover_story: The Admiral's purser; later Odo's treasury secretary.
status: sealed
known_by: [CH-0003@S02E11, CH-0006@S02E11, CH-0044@S03E06, CH-0019@S04E12]
hints: [S01E07, S01E11, S02E11]
reveal: S03E06
public_on_reveal: false
min_seasons_hidden: 1
related: [CH-0003, CH-0006, CH-0044, CH-0019, EV-0345, SEC-001, SEC-010]
```

Why hidden: the heir (later head) of Corvane and a charity clerk of the bank, then a fugitive, then her spy in the enemy's treasury - each of his positions is one in which a known tie to her would kill him. Never public before S06E09.
Clues and beats: S01E07 seed (not a romantic beat): she checks his sum and finds nothing to correct - *"You could sell this to Fennick for a house on the Steps." - "I would have to keep the house dry."* · S01E11 seed: he gives her the page - *"You could have burned it." - "Twice, by now."* · S2 the proofs travel by Undertow boat as ledger entries; the entries grow a second column that is not accounts · S02E11 his letter with the names of her father's killers - the first letter with no columns (both knowers from here) · **S03E06 (audience reveal; DEC-77, r8)** purser of Corvane; he proves the powder fraud on the Whitlow flag-captains, her mother's kin, on paper, and she strikes their flags on a clerk's word (DEC-81: dismissed, nobody dies); the fleet learns the purser has the Admiral's ear and Nell Tern learns why (knower @S03E06) · S04E12 the first kiss and, in the same scene, the order to go into Odo's treasury (EV-0345) · **S04E12** (DEC-77) Jaro, at the Weir Terms, sees the purser leave the Admiral's cabin and reads it at a glance - he kept a second lamp for seven years; he says nothing. From here he holds the one fact that could buy back his own letters from the Listener (SEC-046, S2E11 → S5E12) and through the five-year skip he does not sell it: the first proof of "one thing he will not sell, found again". What he works out in S5 is for the S5 outline · S5 they meet rarely and badly; S05E11 he kills Odo; S05E12 *"I never asked you." - "No. You never do."* · S06E07 she asks him to cut one page (the sight-draft) and he will not - SEC-001 becomes public by the hand of the man who loves her · S06E09 the fire; their last words were a quarrel · S06E12 she puts on her father's ring. **After S06E09: `sealed/` §K only.** Marketing: the line may be shown as a love story through S06E09 and as Maren's grief after it.

### SEC-048 - The paper marriage

```canon
id: SEC-048
type: secret
canon: approved
title: The paper marriage
tier: season
truth: The Corvane-Fennick marriage contract of CY 322 between Helm Maren Corvane and Lord Zev Fennick has terms beyond the public ones.
cover_story: A marriage of peace that closes the Helm's War on paper.
status: sealed
known_by: [CH-0006@S07E03, CH-0042@S07E03]
hints: [S07E03, S09E12, S11E06]
reveal: S12E12
public_on_reveal: false
related: [CH-0006, CH-0042, HS-001, HS-006, EV-0346]
```

Public terms: Corvane and Fennick, enemies since CY 251, close the Helm's War on paper; the **Relay** is sworn to the Helm for her wars and stays in Fennick's keeping; the consort keeps the Listening House and the Hearings; they do not share a roof. Both are honest with each other about what this is - two people who each lost a father to the chair. Betrothal S07E02, marriage S07E03 in the Ring, without a song; Jaro stands witness for the bride. Consequences on screen: the Relay obeys the Helm through the war (the reason "the Relay in the Sovereign's hands", S11); S07E04-E05 the consort, as Master of the Hearings, rules against his wife's convenience in the Kilbride suit; S09E12 the Sovereign has a consort and **no heir** - the regime's open flaw through S10-S12; the heir-presumptive is the cadet line, Corvane of the Roads (HS-027); S12 the consort opens the Relay to the Great Chorus. The marriage is never a love; it ends with her death (S12E11); Zev survives. The terms: `sealed/` §K.

### SEC-049 - The cut pages

```canon
id: SEC-049
type: secret
canon: approved
title: The cut pages
tier: season
truth: Before Ione's journal reached Cressa for publication, Brother Elm cut out the pages that name him and kept them, unable to burn her handwriting.
cover_story: The published journal is complete.
status: sealed
known_by: [CH-0022@S05E06, CH-0045@S07E07]
hints: [S05E06]
reveal: S07E07
public_on_reveal: false
related: [CH-0022, CH-0002, CH-0021, CH-0045, EV-0318, EV-0328, SEC-012]
```

Line L5 (Elm and Ione): S01E11 seed - the first sign he teaches her is her own name, and the Voice does not speak aloud once · S2 sign lessons (she is 19); a language with words only the two of them use · S02E10 she hums two notes in her sleep and he goes pale: from that night he understands what she is and does not tell her, because his place in the Choir depends on silence (SEC-012) (S02E10 - Elm: partial (gleaned, Lows, the lullaby; not who); not a knower of SEC-004, DEC-80) · S3 he carries her journal out past the Pale Crag wardens · S04E08 the break-out; the spiral to Pell · S04E10 she signs *"You knew. Since the two notes."*; he signs yes; forehead to forehead, her hand closed over his signing hand · S04E11 she dies · S05E06 he cuts the pages, then leaks the journal to Cressa · S07E07 Daro finds the pages in his cell - the Choir's proof against him is her love of him, in her own hand · S08E09 executed; the Choir as a body holds the pages from his trial (no single knower recorded); his last words are the first sentence he speaks aloud as himself (fixed line to be written with the S8 outline). Journal and pages custody: `world.md` §6.

### SEC-050 - A beautiful hand

```canon
id: SEC-050
type: secret
canon: approved
title: A beautiful hand
tier: season
truth: Ursel Lantry and Teodor Kett were lovers from her widowhood in CY 291 until his death in CY 296; he forged the Dry Charter because she asked, and the brass ledger-clip she gave Hollis was his father's.
cover_story: Benefactress and ward.
status: sealed
known_by: [CH-0011@origin, CH-0025@origin, CH-0003@S06E08]
hints: [S01E01, S01E11, S04E06]
reveal: S06E08
public_on_reveal: false
related: [CH-0011, CH-0025, CH-0003, EV-0276, EV-0203, EV-0204, SEC-006]
```

A year after the forgery the bank needed the forger gone, and she chose the bank (SEC-006). She raised his son and has been kind to him every day since: the kindness was never a mask. Clues (no extra screen time): S01E01 the clip from her sleeve - he picks it up "as one picks up something warm" (the pilot's existing direction) · S01E11 *"His father had a beautiful hand."* - her fingers go to the empty sleeve the clip came from · S04E06 the second document in his father's hand that Hollis puts away unread is a letter that begins *"U. -"* · S06E08 reveal (Ursel's POV season). Function: Ursel chose the bank over Teodor, as Ruel chose "them" over telling Jaro and Maren chooses the name over Hollis. The clip's provenance is not spoken before S06E08 (custody: `world.md` §6).

### SEC-051 - Twice

```canon
id: SEC-051
type: secret
canon: approved
title: Twice
tier: episode
truth: Bede Lark sold the Tithe Map leak twice, to Ruel and to Ursel, because one sale was half the price of a debt-walker's bond and two bought Wren Roan off the treadmill.
cover_story: A keeper's greed.
status: sealed
known_by: [CH-0052@origin, CH-0079@S02E04, CH-0003@S02E06]
hints: [S01E07, S02E04]
reveal: S02E06
public_on_reveal: false
related: [CH-0052, CH-0079, CH-0003, CH-0048, PL-0084, EV-0262, EV-0278, EV-0279, EV-0340, SEC-001, SEC-013]
```

Wren Roan (CH-0079) has walked off her dead husband's debt on Corr's wheel at the Ninth Sluice treadmill pump since CY 306 (EV-0278); Bede has saved for her since CY 308 (EV-0279). Price: `world.md` §7.4 (keeper's figure, v0.7: the buy-out of her bond 80 marks; each sale of the leak 40). Clues: S01E07 counting Hollis's coin he says he sold "the same news, twice"; asked why, he nods at the treadmill across the canal - *one sale is half a walker's bond; two is a woman off the wheel* (Wren: a back on Corr's wheel, no face) · S02E04 the line's second beat (content with the S2 outline; `romance_lines.md` §6) · S02E06 Hollis proves that the double sale caused both murders of S1; Bede must choose between the woman and the confession. The day Bede buys the bond: **Still 2, CY 312-11-02** (EV-0340, DEC-78, r8) - the day the Lord Admiral dies. From CY 312-11-02 she knows of the purchase, not of the money (partial, not a knower); she learns the source in **S02E04** (`CH-0079@S02E04`), before Hollis proves it in S02E06, so that Bede chooses between the woman and the confession in front of someone who already knows. The smallest love in the city sets off both murders of S1.

### Additions to approved secrets (folded in v0.4)

The v0.3 `amend` blocks (new knowers: Dakka Den in SEC-019; Gant and Novice Sedge in SEC-029; Orm Hask in SEC-013) were approved in r3 and folded into the records above.


Dakka Den, the official mother (writer-characters).


Gant (the buyer) and Novice Sedge (the seller), writer-characters.


Orm Hask, the assassin (writer-characters); who he worked for is DEC-36.

## EXAMPLE (placeholder, not canon)

```canon
id: SEC-EX-001
type: secret
canon: draft
example: true
title: The heron's true father
tier: season
truth: Tamsin is the daughter of Brannoch Hale, and Oren Varnel was drowned by Brannoch on purpose.
cover_story: Tamsin is Oren's daughter; Oren drowned by accident at low tide.
status: seeded
known_by: [CH-EX-0004@origin, CH-EX-0002@origin, CH-EX-0003@S01E02]
hints: [S01E01]
reveal: S01E02
public_on_reveal: false
min_seasons_hidden: 0
related: [CH-EX-0001, CH-EX-0003, CH-EX-0004, EV-EX-0002]
```

Clues (EXAMPLE):

| Episode | Clue |
|---|---|
| S01E01 | Brannoch's scar on the right palm matches Tamsin's salt-burn birthmark. |
