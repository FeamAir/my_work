# Secrets registry

Canon: v0.4 · Status: **approved** (foundation r2, approved by the director 2026-11-22; transfer by lore-keeper)

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
| SEC-030 | The saltpeter sold twice | season | S01E04 | S03E11 | sealed | here (draft) |
| SEC-031 | The wreckers' wages | season | S01E04 | open (DEC-37) | sealed | here (draft) |
| SEC-033 | The Lows-born hunter | episode | S01E02 | S05E12 | sealed | here (draft) |
| SEC-034 | The Broken Dike | season | — | open (DEC-38) | sealed | here (draft) |
| SEC-035 | The fog on the Ostry bar | episode | — | open (DEC-37) | sealed | here (draft) |
| SEC-036 | Harrow's deathbed will | season | — | open (DEC-39) | sealed | here (draft) |
| SEC-037 | The map before the map | episode | S01E01 | S02E06 | sealed | here (draft) |
| SEC-038 | The pilots' night | episode | — | open (DEC-41) | sealed | here (draft) |
| SEC-039 | The Goat Stair | season | — | open (DEC-40) | sealed | here (draft) |
| SEC-040 | Retired codebooks | episode | S01E07 | open (DEC-37) | sealed | here (draft) |
| SEC-041 | The walkers' union | season | S01E05 | open (DEC-37) | sealed | here (draft) |
| SEC-042 | Two retainers | episode | S02E02 | S06E11 | sealed | here (draft) |
| SEC-043 | Ferro's bindings | episode | — | open (DEC-37) | sealed | here (draft) |
| SEC-044 | Ottar's tongue | episode | — | open (DEC-37) | sealed | here (draft) |
| SEC-045 | One copper | episode | S01E02 | open (DEC-45) | sealed | here (draft) |

## Restricted secrets - what may be shared

Answers are in `sealed/sealed.md` (readers: lead-screenwriter, lore-keeper, studio director). Production constraints below are safe for helpers, the director and the composer.

| ID | Constraint for scripts, art, music, marketing |
|---|---|
| SEC-010 | keep Maren sympathetic through S7 and arguable through S9 |
| SEC-011 | Hollis after S06E09 and Zev after S06E09 are not for helpers or marketing |
| SEC-011b | Chronicler voice design: excerpt to the sound director by the director's decision |
| SEC-014 | no clue before S2, none explicit before S5; public material uses the official belief only |
| SEC-018 | — |
| SEC-020 | — |
| SEC-021 | — |
| SEC-024 | public line until S10: "the Dry Queen did not deny it"; dossiers name no culprit |
| SEC-025 | never in marketing, openings or previews before S10E10; the reversed lullaby in the S2 opening is the only planted audio clue (composer excerpt by the director's decision) |
| SEC-026 | never in marketing, openings or previews before S10E10; nothing about Vesna's life before the Choir |
| SEC-027 | Ruel's ring and Pell's shard never share a frame before S12E11 (director excerpt) |

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
known_by: [CH-0005@origin, CH-0050@origin, CH-0058@origin, CH-0003@S01E11, CH-0006@S01E11]
hints: [S01E01, S01E04, S01E06, S01E07, S01E09]
reveal: S01E11
public_on_reveal: false
related: [CH-0005, CH-0016, CH-0050, CH-0063, EV-0262, EV-0263, EV-0300]
```

Clues: S01E01 left-handed clasp, blood on the knuckle, "I don't drink before a storm" · S01E04 the hinged pearl · S01E06 "by the skin, not the mouth"; Juno lived · S01E07 Ruel burns one page; Marl dead with a Corvane mark · S01E09 "Forgive what I did for them." · S01E11 proof by chain (sight-draft EV-0263 + Marl + Ambry + Juno + Ione's sign for *hinge*). Becomes public in S6. Red herrings: the death-tone "too fast"; Garrick inherits.

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

Clues: S01E02 "I had a sister. The water took her before I was born." · S01E03 the Cantor's rinse · S01E05 Ione hums two notes back · S02E05 infant grave dated Reedmonth CY 294 · S02E10 Ione hums two notes in her sleep; Elm goes pale · S03E07 Gleaner ledger "Ninth Sluice, female, one year, ear true - mother Liss" · S03E12 Venn tells Ione she was gleaned; dark roots · S04E04 Nan's sketch of Liss. Ione knows she was gleaned from S03E12; the full truth S04E10.

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
related: [CH-0003, CH-0011, CH-0025, EV-0203, EV-0204]
```

Clues: S01E04 "T. Kett" on the charter · S01E11 "His father had a beautiful hand." · S02E03 Pruitt: drowned "on a night without rain, in a canal knee-deep" · S04E06 Hollis's forgery mistaken for an old document - "the same hand" · S05E08 Silt sells Hollis the boatman who saw it.

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

Clues: S01E04 Kes avoids looking at the gate · S01E10 she opens it: "Not twice." · S02E06 she drinks alone "on the anniversary" (see report: date conflict) · S03E09 confession to Pell before the battle.

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
related: [CH-0012, CH-0022, CH-0023, EV-0205, EV-0261]
```

Clues: S01E02 Liss "drowned in a dry year"; Nan asks only *where* the shard was found and lays salt and a shell there · S02E09 Vesna signs an order while Elm says "a blessing for the sick" · S03E07 ledger "mother - silenced, CY 305" · S04E04 Nan's sketch of Liss with a small dark stone at her throat · S04E08 Elm signs a spiral to Pell · S07E07 Daro catches Elm mistranslating (he knows only the Voice part from here).

### SEC-013 - Who killed Ruel

```canon
id: SEC-013
type: secret
canon: approved
title: Who killed Ruel
tier: season
truth: Ursel Lantry and Garrick Dask hired the assassin (a Lantern Company man) because Ruel would expose Account Nine.
cover_story: Fennick did it; or Quell (the token).
status: sealed
known_by: [CH-0011@S01E04, CH-0017@S01E04, CH-0059@S01E08, CH-0055@S02E07, CH-0006@S02E11, CH-0003@S02E11, CH-0076@origin]
hints: [S01E04, S01E08, S01E09, S02E02, S02E06, S02E07]
reveal: S02E11
public_on_reveal: false
related: [CH-0005, CH-0011, CH-0017, CH-0059, HS-095, EV-0302]
```

Clues: S01E04 Garrick leaves Ursel's office by the back stair · S01E08 the Quell token (herring) · S01E09 Polder clay on the assassin's boots · S02E02 Rook Danner paid in Lantry notes · S02E06 Lucan's sealed will: the unsigned Tithe Map in Ursel's hand, suppressed by Garrick · S02E07 Fossett's private ledger.

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
truth: Lio is not of Ashare blood; Quell salvage-brokers and Piers Lantry made his claim up to sell Lirenne salvage bonds; the fraud splits the Lows' vote (giving Maren the Helm) and makes raising Lirenne a money interest; Lio himself believes it.
cover_story: Last heir of the Tide-Kings.
status: sealed
known_by: [CH-0061@S06E01, CH-0060@S06E10, CH-0019@S07E05, CH-0001@S08E06]
hints: [S06E03, S06E05, S06E10, S07E05]
reveal: S08E06
public_on_reveal: true
related: [CH-0043, CH-0061, HS-005, HS-008, EV-0327]
```

Clues: S06E03 Lio draws the spiral counter-clockwise (Ashare spirals turn sunwise) · S06E05 Piers sells "Lirenne bonds" the day after Lio's first speech · S06E10 his pearl is a Quell trade pearl - Ferro: "A Keeper's pearl is black, and hollow." · S07E05 Jaro's laugh.

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
truth: Esk is Tsura Den's son, given as hostage under the name of her nephew.
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
related: [CH-0058, CH-0050, EV-0301, EV-0308]
```

Clues: S01E07 Corvane coin in Marl's fist · S01E09 Ysa arrives a day before the Relay could have called her · S01E11 her unspoken "condition" · S02E04 her boatswain pays for a Choir funeral · S02E10 "I have been burying your father for a year."

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

## New secrets v0.3 (draft)

Status: **draft** (the lead screenwriter approves numbering, tier and reveal: DEC-37). Final numbers given by the keeper: writer-characters' SEC-030 and SEC-031 kept; their SEC-032 (Lucan's chest) is **not issued** - the chest's content is already an approved fact (CH-0016, `world.md` §6) and its wording is DEC-49; writer-houses' candidates SEC-C01...C07 became SEC-034...040; the writer-characters minor secrets became SEC-033 and SEC-041...045. None touches the origin of a main hero or a restricted answer.

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
related: [CH-0019, CH-0005, CH-0006, HS-005, HS-020, HS-001]
```

Source: writer-characters SEC-031 + writer-houses HS-001/HS-005 (same fact).

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

Source: writer-houses candidate SEC-C05. Timing against SEC-023 (S02E10) to be fixed: DEC-41.

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
truth: In S1E2 Mags sold word of Pell's singing stone to Silt's fence Tuck for one copper; that is how the Listeners learned the lane, not just the relay log.
cover_story: The Listeners traced the stone by the relay log.
status: sealed
known_by: [CH-0049@S01E02, CH-0074@S01E02, CH-0001@S02E09]
hints: [S01E02]
reveal: S02E09
public_on_reveal: false
related: [CH-0049, CH-0074, CH-0053, CH-0001]
```

Source: writer-characters (minor). Pell learns it from Tuck in S2.

### Additions to approved secrets (draft)

`amend` blocks (README §6): new knowers proposed by the dossiers; the approved records above are unchanged.


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
