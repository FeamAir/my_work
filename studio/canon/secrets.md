# Secrets registry

Canon: v0.2 · Status: **approved** (foundation r2, approved by the director 2026-11-22; transfer by lore-keeper)

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
| SEC-017 | Tibb | season | S01E10 | S09E07 | sealed | here |
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
known_by: [CH-0004@origin, CH-0001@S03E09]
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
known_by: [CH-0011@S01E04, CH-0017@S01E04, CH-0059@S01E08, CH-0055@S02E07, CH-0006@S02E11, CH-0003@S02E11]
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

### SEC-017 - Tibb

```canon
id: SEC-017
type: secret
canon: approved
title: Tibb
tier: season
truth: Tibb is the daughter of Sal Tern, Nell Tern's drowned younger sister; Nell is secretly Lows-born.
cover_story: A foundling.
status: sealed
known_by: [CH-0044@S09E07, CH-0001@S09E07]
hints: [S01E10, S07E02, S08E04]
reveal: S09E07
public_on_reveal: false
related: [CH-0046, CH-0044, CH-0067, EV-0305]
```

Clues: S01E10 the cradle tied with a navy knot · S07E02 Nell whistles a Lows tune · S08E04 Nell at a Lows grave "Sal". Function: Nell saves Tibb, not Wick, at the Ninth Bridge, and her testimony delivers SEC-010.

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
known_by: [CH-0013@origin, CH-0040@origin]
hints: [S01E12, S03E03, S04E09]
reveal: S07E06
public_on_reveal: false
related: [CH-0040, CH-0013]
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
known_by: [CH-0014@S04E06]
hints: [S01E05, S03E07, S04E02]
reveal: S04E06
public_on_reveal: false
related: [HS-090, HS-093, CH-0056, CH-0014, CH-0064]
```

Clues: S01E05 the Gleaner novice counting coins · S03E07 a price column in the Gleaner ledger · S04E02 Patch and other debt-walkers all "came back from the robes" · S04E06 Silt drowns her under-boss in his own account book. Public in S5 (with SEC-005).

---

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
