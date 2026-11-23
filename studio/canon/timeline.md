# Timeline

Canon: v0.7 · Status: **approved** (foundation r2, approved by the director 2026-11-22; v0.7: love-line events EV-0276…0280 and EV-0340…0347, episode records S06E02 and S10E06, from `studio/story/romance_lines.md` §7, DEC-73; transfer by lore-keeper)

Source: `studio/story/` r2 (series_bible, houses_overview, cast_overview, saga_arc, season01_outline, franchise) and `studio/story/sealed/master_mystery.md` (sealed parts only in `sealed/`).

Eras, events (before and during the saga) and the in-world dates of episodes.

## Date format

`ERA YYYY[-MM[-DD]]` - e.g. `CY 312`, `CY 312-10`, `CY 312-10-06` (= Longdark 6, CY 312). `~` = about (±1 year). `?` = unknown. Months: `world.md` §4 (month 11 = the Still Days, 5 days).
Public dating of anything before OS 1 stays `?` in-world ("in the Builders' Age"); the canon stores the scholars' date.

## 1. Eras

```canon
id: ERA-BA
type: era
canon: approved
abbr: BA
name: Builders' Age
abs_start: 0
```

```canon
id: ERA-OS
type: era
canon: approved
abbr: OS
name: Old Song
abs_start: 400
ended_by: EV-0100
```

```canon
id: ERA-CY
type: era
canon: approved
abbr: CY
name: Concord Year
abs_start: 1100
ended_by: EV-0332
```

```canon
id: ERA-SY
type: era
canon: approved
abbr: SY
name: Sovereign Years
abs_start: 1425
```

- **BA** - scholars' reckoning, counted from the first known Spire; reserved for prequels (abs 0-399).
- **OS** - reckoning of the Tide-Kings; OS 1 = first Keeper; ended by the Breaking (EV-0100), OS 700.
- **CY** - Concord Year; CY 1 = first year of the Concord; the saga opens in **CY 312**; ended by Maren's coronation (EV-0332) on the Still Days of CY 325.
- **SY** - Sovereign Years, SY 1 = CY 326 (SEC-022; announced on screen S09E12).
- A fifth era ("the Year of Many Voices") begins after S12; it is decided (DEC-13), but its start and the epilogue year are restricted until S12 (`sealed/`).

## 2. Events

ID ranges (from `franchise.md` §3): EV-0001-0049 Builders' Age (P1) · EV-0050-0099 OS 380-420 (P2) · EV-0100-0149 OS 690-CY 1 (P3) · EV-0150-0199 CY 136-141 (P4) · EV-0200-0249 CY 295-296 (P5) · **EV-0250-0299 other pre-saga history (keeper)** · EV-0300+ the saga. Prequel events are recorded as ordinary events; their prequel is named in the prose.

Each event's prose gives the public version first and then the truth, naming the secret. Restricted truths are only referenced (`sealed/`).

```canon
id: EV-0001
type: event
canon: approved
name: The first Spire grows at Lirenne
date: BA 1
date_end: BA 60
place: PL-0062
secrets: [SEC-014]
```

Public: "The Builders raised the Spires and vanished" (dated `?` in-world). Truth: SEC-014 (sealed). Prequel slot P1.

```canon
id: EV-0002
type: event
canon: approved
name: The nine Spires raised
date: BA 1
date_end: ~BA 390
place: PL-0003
secrets: [SEC-014]
```

Public: "the Builders' Age - unknown". Origin of the Still Days. Prequel P1.

```canon
id: EV-0050
type: event
canon: approved
name: The first Keeper of Lirenne
date: OS 1
place: PL-0061
houses: [HS-008]
```

The Chronicle calls every Keeper a "Tide-King" from this date.

```canon
id: EV-0051
type: event
canon: approved
name: The Crowning of the Keepers
date: ~OS 380
date_end: ~OS 420
place: PL-0061
houses: [HS-008]
```

The Keepership becomes hereditary in House Ashare (Keeper Isembar); nine warden families (six Spire-wardens, three sword-families) are sworn to it (DEC-01). Prequel P2.

```canon
id: EV-0052
type: event
canon: approved
name: The founding of the Cantor schools
date: OS 600
date_end: OS 699
houses: [HS-003]
secrets: [SEC-005]
```

Public: a holy reform. Truth: the warden families train solo Cantors to sing Spires without crowds ("the solo heresy").

```canon
id: EV-0100
type: event
canon: approved
name: The Breaking
date: OS 700-11
place: PL-0061
houses: [HS-008, HS-003, HS-001]
participants: [CH-0031]
killed: [CH-0030]
secrets: [SEC-003, SEC-025, SEC-027]
```

Public: Queen Neveh went mad and sang Lirenne into the sea; the nine warden families (six Spire-wardens, three sword-families) rose, killed her and founded the Concord. Truth (SEC-003): the Nine, led by Ilvane with Corvane ships at sea, massacred the people's chorus on the steps of the Lirenne Spire during the Still Days; ~40,000 dead; Oshra escaped by reed boat carrying the last verse and a spiral shell. The last hour: sealed. Ends the Old Song era. Prequel P3. Open wording for the Corvane admiral (DEC-14): Tolvar Corvane (CH-0203) "held the harbour; came ashore when the city fell".

```canon
id: EV-0101
type: event
canon: approved
name: The founding of the Concord
date: CY 1
houses: [HS-001, HS-002, HS-003, HS-004, HS-005, HS-009, HS-010, HS-011, HS-012, HS-090]
secrets: [SEC-005]
```

The nine warden families found the Concord - six Spire-wardens (Corvane - Sentinel; Dask - Sheaf; Ilvane - Pale and Bell/Choir; Quell - Storm; Harrow - Hill/Crown and Sluice; Vanth - Falls) and three sword families (Rusk, Moll, Ostry); "the Nine" are families, not Spires, which is why there are eight voices in CY 1 (DEC-01); the Hush Law (RULE-006); the Choir founded as a solo order; the songblood doctrine; the Gleaners begin. Spires: Crown to the Helm's office, Choir to the Choir; Rusk, Moll, Ostry are "sword houses" without a Spire.

```canon
id: EV-0102
type: event
canon: approved
name: The founding of the Quiet
date: CY 1
place: PL-0007
houses: [HS-094]
participants: [CH-0031]
secrets: [SEC-003, SEC-025]
```

Oshra founds the Quiet in the Highwater reed-slums. Details: sealed.

```canon
id: EV-0150
type: event
canon: approved
name: The Vanth Treason
date: CY 138
date_end: CY 141
place: PL-0046
houses: [HS-012, HS-091]
secrets: [SEC-008]
```

Public: "Vanth was attainted for selling the Stair." Truth (SEC-008): Vanth sang the Falls Spire less to let the Aun reach the uplands and traded with the Ossari. Vanth "river book" kept by Kadu's family. Prequel P4.

```canon
id: EV-0151
type: event
canon: approved
name: The First Upland War
date: CY 141
place: PL-0046
houses: [HS-004, HS-012, HS-003, HS-091]
secrets: [SEC-008]
```

Rusk, with Ilvane backing, destroys Vanth and takes the Stair and the Falls Spire.

```canon
id: EV-0200
type: event
canon: approved
name: The Night of Still Water
date: CY 295-11
place: PL-0008
houses: [HS-007, HS-006, HS-004, HS-092, HS-090]
participants: [CH-0004, CH-0005, CH-0023, CH-0056, CH-0002]
secrets: [SEC-004, SEC-009]
```

Public: "The Sluice Spire faltered, and the sea came" - an act of the sea; ~6,000 dead. Truth: Lantry ("Account Five", precursor of Account Nine) paid for the Sluice Spire's retuning to be delayed; the Pumpwrights' yearly breakage had stopped the pumps that week (precedent of SEC-028); Kes (17) shut the evacuation gate on her captain's order (SEC-009); young Captain Ruel Corvane rescued hundreds by boat. Prequel P5.

```canon
id: EV-0201
type: event
canon: approved
name: The gleaning of Ama
date: CY 295-11
place: PL-0008
houses: [HS-090]
participants: [CH-0056, CH-0002, CH-0023]
secrets: [SEC-004]
```

In a rescue boat Sister Venn hears baby Ama sing back Liss's lullaby, takes her "to a physician" and tells Liss she died; Ama is installed as Cressa's daughter Ione. Who arranged it: sealed.

```canon
id: EV-0203
type: event
canon: approved
name: The Dry Charter
date: CY 295
date_end: CY 296
place: PL-0011
houses: [HS-007]
participants: [CH-0025, CH-0011]
secrets: [SEC-006]
```

Clerk Teodor Kett forges the charter transferring the deeds of drowned Ninth Sluice to Lantry.

```canon
id: EV-0204
type: event
canon: approved
name: Death of Teodor Kett
date: CY 296
houses: [HS-007]
killed: [CH-0025]
secrets: [SEC-006]
```

Public: "drowned" (cause not given; believed drunk). Truth: drowned on Ursel's order "on a dry night"; she takes Hollis (10) as charity apprentice.

```canon
id: EV-0205
type: event
canon: approved
name: Elm gleaned
date: CY 296
houses: [HS-094, HS-090]
participants: [CH-0022]
secrets: [SEC-012]
```

The Quiet put six-year-old Elm, taught the lullaby as a baby, in a Gleaner's path - a plant inside the Choir.

```canon
id: EV-0250
type: event
canon: approved
name: Dask conquer Moll
date: CY 88
place: PL-0038
houses: [HS-002, HS-010, HS-017, HS-018]
participants: [CH-0275]
killed: [CH-0275]
secrets: [SEC-034]
```

```canon
id: EV-0251
type: event
canon: approved
name: Ostry absorbed by Corvane
date: ~CY 120
place: PL-0032
houses: [HS-001, HS-011, HS-027]
participants: [CH-0279, CH-0204]
killed: [CH-0278]
secrets: [SEC-035]
```

By marriage.

```canon
id: EV-0252
type: event
canon: approved
name: The Lantry Counting House founded
date: CY 220
place: PL-0011
houses: [HS-007]
```

```canon
id: EV-0253
type: event
canon: approved
name: House Harrow dies out; Fennick raised
date: CY 251
houses: [HS-009, HS-006, HS-007, HS-013, HS-014]
killed: [CH-0270]
participants: [CH-0250]
```

Sluice Spire to Fennick; Fennick raised to great house. Vote 5-3: both Harrow voices are cast by Harrow's stewards, the Fennicks, "stewards of the dying" (DEC-06).

```canon
id: EV-0254
type: event
canon: approved
name: The Purchased Seat
date: CY 252
place: PL-0010
houses: [HS-007, HS-009]
secrets: [SEC-036]
participants: [CH-0261]
```

Lantry buys Harrow's Conclave vote. Vote 5-2: the Hill Voice is the matter voted on and is empty; Corvane and Quell against (DEC-06).

```canon
id: EV-0256
type: event
canon: approved
name: Vesna's Great Song
date: CY 272-09
participants: [CH-0012]
houses: [HS-090]
```

Against the Mistcall storm; Vesna goes mute (forty years before the saga). What followed for her: sealed.

```canon
id: EV-0257
type: event
canon: approved
name: Death of Ilse Ilvane
date: CY 294-04
place: PL-0040
houses: [HS-003]
killed: [CH-0068]
secrets: [SEC-004]
```

Cressa's daughter dies at two months; buried secretly at Pale Crag. Not known publicly.

```canon
id: EV-0260
type: event
canon: approved
name: Death of Dov
date: CY 302
place: PL-0008
killed: [CH-0024]
```

A true treadmill accident.

```canon
id: EV-0261
type: event
canon: approved
name: The drowning of Liss
date: CY 305
place: PL-0020
houses: [HS-090]
killed: [CH-0023]
secrets: [SEC-012, SEC-027]
```

Public: "drowned" - in a year with no flood. Truth (SEC-012): after she found Sister Venn and demanded her daughter back, Choir men drowned her on the First Cantor's order. Nan takes Pell (8) and Wick (4). Further: sealed.

```canon
id: EV-0262
type: event
canon: approved
name: The leak sold twice
date: CY 312
houses: [HS-006, HS-007, HS-001]
participants: [CH-0052, CH-0005, CH-0011]
secrets: [SEC-001, SEC-013]
```

Relay-keeper Bede Lark sells the news that Helm Lucan will sign a Tithe Map letting Ninth Sluice go - first to Ruel, then to Ursel. Ursel orders every Corvane draft filed in Account Nine's file.

```canon
id: EV-0263
type: event
canon: approved
name: Ruel's sight-draft to Sister Marl
date: CY 312-10-04
houses: [HS-001, HS-007]
participants: [CH-0005, CH-0050]
secrets: [SEC-001]
```

Forty marks on the Corvane refit credit, "by the Lord Admiral's own hand" - the proof of S01E11.

```canon
id: EV-0300
type: event
canon: approved
name: Death of Helm Lucan Dask
date: CY 312-10-06
episode: S01E01
place: PL-0009
houses: [HS-002]
participants: [CH-0005, CH-0002, CH-0063]
killed: [CH-0016]
secrets: [SEC-001]
```

Collapses reading the Tithe Map on the words "...and the Ninth Sluice-". Public: natural death; then "Fennick did it".

```canon
id: EV-0301
type: event
canon: approved
name: Death of Sister Marl
date: CY 312-10
episode: S01E07
houses: [HS-090]
killed: [CH-0050]
secrets: [SEC-023]
```

Found dead with a Corvane silver mark in her fist.

```canon
id: EV-0302
type: event
canon: approved
name: Ruel stabbed on the Steps
date: CY 312-11-01
episode: S01E08
place: PL-0005
houses: [HS-001]
participants: [CH-0005, CH-0004]
secrets: [SEC-013]
```

Night procession; Kes kills the masked assassin; a Quell token falls from his hand (red herring).

```canon
id: EV-0303
type: event
canon: approved
name: Death of Ruel Corvane
date: CY 312-11-02
episode: S01E09
place: PL-0018
houses: [HS-001]
participants: [CH-0006, CH-0002, CH-0058]
killed: [CH-0005]
```

Aboard the *Patient Gull*. Last words: "Forgive what I did for them."

```canon
id: EV-0304
type: event
canon: approved
name: The skipped retuning
date: CY 312-11-03
episode: S01E09
place: PL-0016
houses: [HS-006, HS-007, HS-090]
participants: [CH-0057]
secrets: [SEC-015]
```

On the third Still Day the Sluice Spire falls silent at dusk for its retuning and the retuning song never comes (DEC-04). Public: an old Spire failing.

```canon
id: EV-0305
type: event
canon: approved
name: The Still Days flood of Ninth Sluice
date: CY 312-11-03
episode: S01E10
place: PL-0008
houses: [HS-092, HS-004, HS-090]
participants: [CH-0001, CH-0007, CH-0015, CH-0002, CH-0004, CH-0048, CH-0046]
killed: [CH-0049, CH-0057, CH-0067]
secrets: [SEC-002, SEC-009, SEC-017b, SEC-028]
```

~2,000 dead; the Spire was already failing (two voices and a mute since the summer), so the sea comes in within hours on the storm tide (RULE-003, DEC-05). Sal Tern drowns (CH-0067). Pumps jammed (SEC-028); Kes opens the gate; Pell saves baby Tibb; Ione's Great Song with Pell's hum holds the Spire - Ione loses her voice.

```canon
id: EV-0306
type: event
canon: approved
name: Odo Fennick elected Helm by the Sunken Vote
date: CY 312-11-05
episode: S01E12
place: PL-0010
houses: [HS-001, HS-002, HS-003, HS-004, HS-005, HS-006, HS-007, HS-090]
participants: [CH-0010, CH-0006, CH-0012, CH-0020, CH-0017, CH-0018, CH-0019, CH-0011]
```

4-4 (Corvane, Quell, Ilvane, Rusk vs Fennick, Lantry, the Choir, Dask); the First Cantor casts the Sunken Vote. Ninth Sluice declared reclaimed land. Maren refuses to swear and sails; Kes demoted and sent to the Stair.

```canon
id: EV-0307
type: event
canon: approved
name: Death of Nan Oshra
date: CY 313
episode: S02E08
houses: [HS-006]
killed: [CH-0015]
```

Killed by Fennick's Listeners. Last words: "It's not in the blood. It's in the mouth."

```canon
id: EV-0308
type: event
canon: approved
name: The Battle of the Sluice Gates
date: CY 313
episode: S02E11
place: PL-0026
houses: [HS-001, HS-005, HS-006, HS-002, HS-007]
participants: [CH-0006, CH-0019, CH-0058]
```

Maren loses three ways: Ysa opens Gullmouth to Fennick, Dask barges block the canal, her guns fall silent early (padded powder accounts).

```canon
id: EV-0310
type: event
canon: approved
name: The Sunken Spire stirs
date: CY 313-09
episode: S03E10
place: PL-0062
houses: [HS-094]
participants: [CH-0001]
secrets: [SEC-002, SEC-025]
```

Pell sings the lullaby from the Sunken Spire's crown at low tide; the dead Spire stirs; the Quiet elders cover her mouth.

```canon
id: EV-0311
type: event
canon: approved
name: The Battle of the Stair
date: CY 313-09
episode: S03E10
place: PL-0046
houses: [HS-004, HS-091]
participants: [CH-0004, CH-0013, CH-0040, CH-0047, CH-0062]
killed: [CH-0018]
```

S03E10-E11. Pike squares, cannon in the rain, kites and gliders; the Ossari fire Rusk's own powder. Brenna dies holding the gate; the Stair and the Falls Spire fall.

```canon
id: EV-0313
type: event
canon: approved
name: The weir at the falls
date: CY 314
place: PL-0049
houses: [HS-091]
```

The Ossari silence the captured Falls Spire and build a weir; upland wells rise, the Aun drops, the Dask polders crack.

```canon
id: EV-0315
type: event
canon: approved
name: The breach of the weir
date: CY 314-11-03
episode: S04E11
place: PL-0049
houses: [HS-091, HS-002]
secrets: [SEC-024]
```

In the last dark hour before dawn on the third Still Day the weir goes; the bore does not tie up at night or wait at locks: it passes the Polders by mid-morning and reaches Highwater by late afternoon, while the Crown Spire is silent in mid-retuning and the Sluice Spire is about to follow (DEC-17). S4E11 line: *"A barge sleeps at night and waits at every lock. Water does neither."* Public: "The weir at the falls was breached, and the Dry Queen did not deny it." Truth: SEC-024 (sealed).

```canon
id: EV-0316
type: event
canon: approved
name: The duet at the Crown Spire
date: CY 314-11-03
episode: S04E11
place: PL-0014
participants: [CH-0001]
killed: [CH-0002]
secrets: [SEC-021]
```

Evening of the third Still Day (DEC-17). Mute Ione sings the Crown Spire on breath alone with Pell (high part + low note) and sings out; the duet holds the wave.

```canon
id: EV-0317
type: event
canon: approved
name: The Weir Terms
date: CY 314-11-05
episode: S04E12
houses: [HS-091, HS-006]
participants: [CH-0013]
```

Still 4-5 (S4E12). The Ossari keep the rim; the Falls Spire is sung only half the year. The Terms hold seven years (CY 315-321); Maren breaks them in CY 322 (S7) (DEC-08). Text: `houses/HS-091-ossari.md`.

```canon
id: EV-0318
type: event
canon: approved
name: Publication of the Gleaner rolls
date: CY 320
episode: S05E06
houses: [HS-003, HS-090]
participants: [CH-0021]
secrets: [SEC-005]
```

Cressa publishes Ione's journal, the Gleaner rolls and Silt's ledger.

```canon
id: EV-0319
type: event
canon: approved
name: The Night of a Thousand Voices
date: CY 320-11-03
episode: S05E11
place: PL-0008
houses: [HS-092, HS-006]
participants: [CH-0001, CH-0003, CH-0048, CH-0041, CH-0053, CH-0007]
killed: [CH-0010]
secrets: [SEC-028, SEC-021]
```

The night of Still 3, CY 320 - the Sluice Spire silent for its retuning, twenty-five years to the night after Still Water (DEC-07). Begins at the tide-post; thousands sing the Sluice Spire in a storm; the Listeners fire; Hollis kills Odo; the Pumpwrights' barges hold the water (Corr's price). Hundreds of singers dead.

```canon
id: EV-0320
type: event
canon: approved
name: The Counting House fire
date: CY 321
episode: S06E09
place: PL-0011
houses: [HS-007]
participants: [CH-0003, CH-0042]
```

Bank run and fire; Hollis presumed dead; Zev is the last man seen going in.

```canon
id: EV-0321
type: event
canon: approved
name: Death of Ursel Lantry
date: CY 321
episode: S06E10
houses: [HS-007]
killed: [CH-0011]
```

Dies when the bank falls.

```canon
id: EV-0322
type: event
canon: approved
name: The Battle of the Shoals
date: CY 321
episode: S06E11
place: PL-0055
houses: [HS-005, HS-095]
participants: [CH-0019, CH-0059]
```

A mercenary fleet changes sides mid-battle when its notes become worthless.

```canon
id: EV-0323
type: event
canon: approved
name: Maren elected Helm
date: CY 321-11
episode: S06E12
place: PL-0010
houses: [HS-001]
participants: [CH-0006, CH-0001]
```

With the votes Pell bought by a promise - repeal of the Hush Law ("in Highwater"). She puts on her father's ring.

```canon
id: EV-0324
type: event
canon: approved
name: Murder of Cressa Ilvane
date: CY 321
episode: S06E12
houses: [HS-090, HS-003]
killed: [CH-0021]
```

Murdered by the Choir.

```canon
id: EV-0325
type: event
canon: approved
name: The half-repeal of the Hush Law
date: CY 322
episode: S07E01
place: PL-0022
houses: [HS-001]
participants: [CH-0006]
```

Repealed only in Highwater, "within sight of the Crown Spire".

```canon
id: EV-0326
type: event
canon: approved
name: The Battle of the Hundred Locks
date: CY 322
episode: S07E11
place: PL-0028
houses: [HS-001, HS-091, HS-002]
killed: [CH-0004]
```

The largest land battle of the saga.

```canon
id: EV-0327
type: event
canon: approved
name: Death of Lio
date: CY 323
episode: S08E06
killed: [CH-0043]
secrets: [SEC-016]
```

Dying, he asks the crowd to raise Lirenne anyway.

```canon
id: EV-0328
type: event
canon: approved
name: Execution of Brother Elm
date: CY 323
episode: S08E09
houses: [HS-090]
killed: [CH-0022]
```

```canon
id: EV-0329
type: event
canon: approved
name: The Siege of Highwater
date: CY 323
episode: S08E10
place: PL-0004
houses: [HS-091, HS-001]
participants: [CH-0006, CH-0013]
```

S08E10-E11; ended by Maren singing two Spires against the Ossari camps - thousands drowned.

```canon
id: EV-0330
type: event
canon: approved
name: The First Raising
date: ~CY 324
episode: S09E05
place: PL-0055
houses: [HS-094, HS-093]
killed: [CH-0014]
secrets: [SEC-025, SEC-010]
```

At the lowest tide the chorus sings everything the Quiet have kept; the Sunken Spire does not rise; the Storm Spire falls dumb for an hour; the surge takes the staging camp. Maren watches from her flagship.

```canon
id: EV-0331
type: event
canon: approved
name: The Battle of the Ninth Bridge
date: ~CY 325
episode: S09E10
place: PL-0027
houses: [HS-002]
participants: [CH-0006]
killed: [CH-0007]
secrets: [SEC-010]
```

The chorus columns are cut off by the spring tide and slaughtered by Dask levies. Maren finds her old cadet cap on a dead boy.

```canon
id: EV-0332
type: event
canon: approved
name: Maren crowned Sovereign
date: CY 325-11
episode: S09E12
place: PL-0010
houses: [HS-001]
participants: [CH-0006]
secrets: [SEC-022]
```

She dissolves the Conclave and is crowned on the Still Days; the Chronicler announces a new count of years (SY 1 = CY 326). Ends the Concord Year era.

```canon
id: EV-0333
type: event
canon: approved
name: Death of Vesna Ilvane
date: SY 1
episode: S10E09
houses: [HS-090]
participants: [CH-0001, CH-0045]
killed: [CH-0012]
```

```canon
id: EV-0334
type: event
canon: approved
name: The Battle of the Polders
date: SY 1
episode: S10E11
place: PL-0035
houses: [HS-001, HS-002, HS-091]
killed: [CH-0017]
```

Maren floods the Dask polders to starve the alliance; Garrick drowns in his own fields.

```canon
id: EV-0335
type: event
canon: approved
name: Death of Jaro Quell
date: SY 2
episode: S11E08
houses: [HS-005]
killed: [CH-0019]
```

```canon
id: EV-0336
type: event
canon: approved
name: Death of Tsura Den
date: SY 2
episode: S11E10
houses: [HS-091]
killed: [CH-0013]
```

```canon
id: EV-0337
type: event
canon: approved
name: The Battle of Lirenne
date: SY 2
episode: S11E11
place: PL-0061
houses: [HS-001, HS-005, HS-091]
participants: [CH-0001]
secrets: [SEC-018]
```

S11E11-E12. The greatest naval battle while thousands sing on boats; the Sunken Spire rises.

```canon
id: EV-0338
type: event
canon: approved
name: Death of Maren Corvane
date: ~SY 3
episode: S12E11
killed: [CH-0006]
```

Exact circumstances fixed with the S12 outline (lead's open question; constraint: not by Pell's hand).

```canon
id: EV-0339
type: event
canon: approved
name: The Great Chorus
date: ~SY 3
episode: S12E12
place: PL-0003
participants: [CH-0001, CH-0042]
```

Ten thousand voices across the delta; the cost of the song shared. Pell's voice is the price.

### New events v0.7 - love lines in the saga (r7, approved DEC-73)

```canon
id: EV-0340
type: event
canon: approved
name: Bede Lark buys Sibby Roan's bond
date: TODO(DEC-78)
place: PL-0084
participants: [CH-0052, CH-0079]
secrets: [SEC-051]
```

Bought with the two sales of the leak (EV-0262): 80 marks (`world.md` §7.4). The day is open (DEC-78): `romance_lines.md` §7 says Longdark 6 ("the day the Helm dies"), but the approved S1 outline still has her on Corr's wheel in S01E07 (Longdark 25-30). Keeper's recommendation: after S01E07 and before the flood of Still 3 - Still 2, CY 312-11-02. Not shown on screen in S1; S2E4 and S2E6 pay it.

```canon
id: EV-0341
type: event
canon: approved
name: Ysa takes the packet; Jaro at the wake
date: CY 312-11-02
date_end: CY 312-11-03
episode: S01E09
place: PL-0018
houses: [HS-001, HS-005]
participants: [CH-0058, CH-0019, CH-0006]
secrets: [SEC-046, SEC-023]
```

Still 2-3. Ysa bars Jaro from the *Patient Gull* ("House only tonight, Captain-Lord."); he stands on the mole all night. She empties the cabin locker - Jaro's letters and Ruel's Longdark 5 note, tied in tarred twine - into her sleeve. At the wake he is let in last, alone, puts out the second stern lamp and takes the dead man's right hand. Chronicler: *"The Captain-Lord of the Shoals paid his respects last."*

```canon
id: EV-0342
type: event
canon: approved
name: The packet passes to Odo Fennick
date: CY 313
episode: S02E11
houses: [HS-001, HS-006, HS-005]
participants: [CH-0058, CH-0010]
secrets: [SEC-046]
```

S02E10 Ysa lays the packet before Maren with the boatswain's discharge ("There were two things to bury."); S02E11, opening Gullmouth to Fennick (EV-0308), she gives it to Odo as her pledge. The letters name the wrecker silver: from now on the Listener can unseat Jaro at any Hull Moot.

```canon
id: EV-0343
type: event
canon: approved
name: The packet passes to Zev Fennick
date: CY 320-11
episode: S05E12
houses: [HS-006]
participants: [CH-0042]
secrets: [SEC-046]
```

Still CY 320: Zev inherits the Listening House (PL-0012) after Odo's death (S05E11) and the packet with it.

```canon
id: EV-0344
type: event
canon: approved
name: The packet returned to Jaro unopened
date: CY 321
episode: S06E02
houses: [HS-006, HS-005]
participants: [CH-0042, CH-0019]
secrets: [SEC-046]
```

The first act of the new Lord Fennick. Jaro is free to back Maren in S6 and owes Zev a debt he pays at the wedding (EV-0346). In S06E08 he finds Ruel's Longdark 5 note in it (EV-0280).

```canon
id: EV-0345
type: event
canon: approved
name: Maren and Hollis - the kiss and the order
date: CY 314-11-05
episode: S04E12
participants: [CH-0006, CH-0003]
secrets: [SEC-047]
```

Still 5, CY 314, after Ione's death and the Weir Terms (EV-0317): the first kiss and, in the same scene, her order to go into Odo's treasury (DEC-52). Her way of loving, stated once.

```canon
id: EV-0346
type: event
canon: approved
name: Marriage of Helm Maren Corvane and Lord Zev Fennick
date: CY 322
episode: S07E03
place: PL-0010
houses: [HS-001, HS-006]
participants: [CH-0006, CH-0042, CH-0019]
secrets: [SEC-048]
```

Betrothal S07E02; married in the Ring without a song (the Hush Law is repealed only in Highwater, EV-0325, and the Helm does not sing); Jaro Quell stands witness for the bride and does not object. Closes the Helm's War on paper; Corvane and Fennick allied by marriage (HS-001, HS-006). Terms: SEC-048.

```canon
id: EV-0347
type: event
canon: approved
name: The kite correspondence across the siege lines
date: CY 322
date_end: CY 323
participants: [CH-0001, CH-0040, CH-0043]
secrets: [SEC-016]
```

Pell and Esk (line L4): from the parley over the Falls Spire (S7) to the Siege of Highwater (EV-0329, S08E02-E09) letters go by **kite-code** over the wall in plain sight of two armies - the only channel between the movement and the uplands. S08E04-E06 Lio lets his brokers sell the code to the Dry Palace watch; S08E10-E11 Pell flies a warning on the blown code and Esk's part of the camp leaves the low ground before the Spires are sung.

### New events v0.3 (approved v0.4)

Status: **approved** (lead screenwriter, r3; EV-0275 dated by DEC-20) (writer-houses `story/houses/README.md`; EV-0274 and EV-0275 added by the keeper). Keeper range EV-0250...0299.

```canon
id: EV-0264
type: event
canon: approved
name: The Sunk Charter
date: CY 3
place: PL-0060
houses: [HS-005]
participants: [CH-0243]
```

Quell is granted the salvage of the whole drowned city of Lirenne and its shallows "until the city be raised or the sea give it back". Its second edge against Article Nine of the Charter of the Ring ("whoever holds Lirenne") is what the Lirenne salvage bonds sell in S6 (SEC-016).

```canon
id: EV-0265
type: event
canon: approved
name: The Relay chartered
date: CY 9
place: PL-0004
houses: [HS-009, HS-006]
participants: [CH-0271]
```

Helm Aldous Harrow charters the Relay - echo-stone stations Spire to Spire - and gives the codebooks to his stewards, the Fennicks, hereditary Relay-Masters from now on (HS-006 `founded`).

```canon
id: EV-0266
type: event
canon: approved
name: The Unison Decree
date: CY 34
place: PL-0040
houses: [HS-090, HS-003, HS-001, HS-002, HS-005]
secrets: [SEC-005]
```

The Choir's chapter dissolves the lesser choirs (the Gullmouth harbour choir, the Barrows field-choir, the Brackwater wreck-singers): every Cantor must be trained at Pale Crag; the other houses rent Cantors from the Choir from now on. Public: a holy reform. Truth: the same act as the Cantor schools (EV-0052) - no group singing outside Ilvane's control (SEC-003, SEC-005).

```canon
id: EV-0267
type: event
canon: approved
name: The Salt War
date: CY 37
date_end: CY 40
place: PL-0056
houses: [HS-001, HS-005]
```

Admiral Brannic Corvane burns the clan fleets at the Brackwater bar. The Pilots' Peace (CY 40): Quell keeps its Spire, its salt and its calm-fee, flies the Concord flag in war and supplies every Gullmouth pilot (Clan Skarra) - the root of the Corvane-Quell "uneasy friendship".

```canon
id: EV-0268
type: event
canon: approved
name: The Stair Treaty
date: CY 142
place: PL-0046
houses: [HS-004, HS-091]
```

Peace by exhaustion after the First Upland War: the Rim stays Ossari, the escarpment is Rusk's; all upland saltpeter passes the Stair and pays Rusk a tenth (the saltpeter licence); the hostage custom of the Exchange of Sleeves begins. Rusk stops sending its own children after CY 206.

```canon
id: EV-0269
type: event
canon: approved
name: The Clerks' Ordinance
date: CY 160
place: PL-0009
houses: [HS-006]
```

The Hearings (the Concord's courts) pass from the Helm's office to the Fennick Relay-Masters; the Listeners begin as informers "so that the Hearings may hear".

```canon
id: EV-0270
type: event
canon: approved
name: The Kite War
date: CY 203
date_end: CY 206
place: PL-0070
houses: [HS-004, HS-091, HS-025]
```

The Second Upland War: Rusk takes three terrace forts on the Rim and loses two within a year; keeps Rimgate (PL-0072), given to the Hadden family, who marry into Clan Tekka. First gliders seen by Concord soldiers. Dry Queen Sotka.

```canon
id: EV-0271
type: event
canon: approved
name: The Paper Ordinance
date: CY 224
place: PL-0011
houses: [HS-007, HS-009]
secrets: [SEC-007]
```

Helm Tancred Harrow allows the Counting House to issue dry-notes, "a promise of dry ground", backed by deeds to land above the waterline (in practice: above Let Go on the Tithe Map) and countersigned by a Merriden notary.

```canon
id: EV-0272
type: event
canon: approved
name: The Exchange Panic
date: CY 268
place: PL-0030
houses: [HS-001, HS-007]
```

The Gullmouth Exchange, Corvane's own bank, fails after a false relay rumour of a lost treasure fleet; Lantry buys its paper at a fifth; Corvane borrows from Lantry from then on. Pattern (no secret of its own): the rumour was a relay message sold early - the trick Bede Lark repeats in CY 312 (EV-0262).

```canon
id: EV-0273
type: event
canon: approved
name: The Rim Skirmish
date: CY 309
place: PL-0070
houses: [HS-004, HS-091]
killed: [CH-0233]
```

Border fight on the Rim; Brenna's son Ardo Rusk is killed, and in the same fight the Kitsa glider-captain Akko (CH-0078, DEC-33). Truce follows; Esk is given as hostage the same season (EV-0275, DEC-20).

```canon
id: EV-0274
type: event
canon: approved
name: The Grey Cough
date: CY 249
date_end: CY 251
place: PL-0005
houses: [HS-009, HS-006]
participants: [CH-0270]
```

A winter lung-fever of the Steps; House Harrow dies of it (EV-0253). Fennick stewards run Harrow's estates in the dying months.

```canon
id: EV-0275
type: event
canon: approved
name: Esk given to the Stair as hostage
date: CY 309-08
place: PL-0046
houses: [HS-091, HS-004]
participants: [CH-0040, CH-0018]
secrets: [SEC-019]
```

Under the truce after the Rim Skirmish (EV-0273) the clans give Esk as hostage, "the Dry Queen's nephew" (SEC-019), in Fallow CY 309 - a hostage paid for Ardo Rusk's blood (DEC-20). Esk is 10; in S1 he has been a hostage three years. Corporal Ottar was given twelve years earlier, CY 297.

### New events v0.7 - love lines before the saga (r7, approved DEC-73)

```canon
id: EV-0276
type: event
canon: approved
name: Ursel Lantry and Teodor Kett become lovers
date: CY 291
date_end: CY 296
houses: [HS-007]
participants: [CH-0011, CH-0025]
secrets: [SEC-050]
```

From the year of her widowhood (Bastian Lantry, CH-0262, d. CY 291) until his death (EV-0204). He forges the Dry Charter (EV-0203) because she asks; a year later she chooses the bank. Not spoken before S06E08.

```canon
id: EV-0277
type: event
canon: approved
name: The liaison of Ruel Corvane and Jaro Quell begins
date: CY 305
houses: [HS-001, HS-005]
participants: [CH-0005, CH-0019]
secrets: [SEC-046, SEC-031]
```

The same year the Quell wrecker silver begins to pay the Corvane fleet (SEC-031). Ruel is a widower since CY 300 (CH-0202). Signal: a second stern lamp on the *Patient Gull*. Revealed to the audience S01E09.

```canon
id: EV-0278
type: event
canon: approved
name: Sibby Roan goes on the wheel
date: CY 306
place: PL-0084
participants: [CH-0079]
secrets: [SEC-051]
```

Her dead husband's debt is "walked" on Corr's wheel at the Ninth Sluice treadmill pump (`world.md` §8.2): a mark off the debt per walk, while the interest runs faster.

```canon
id: EV-0279
type: event
canon: approved
name: Bede Lark begins to save for Sibby's bond
date: CY 308
participants: [CH-0052]
secrets: [SEC-051]
```

A relay-keeper's savings against an 80-mark bond (`world.md` §7.4); four years are not enough - the reason he sells the leak twice in CY 312 (EV-0262).

```canon
id: EV-0280
type: event
canon: approved
name: Ruel's unsent note to Jaro
date: CY 312-10-05
houses: [HS-001]
participants: [CH-0005, CH-0058]
secrets: [SEC-046, SEC-001, SEC-023]
```

Longdark 5, the eve of the Helm's death: Ruel writes *"If I asked you to sail tomorrow and not ask why-"* and does not send it; the note goes into the cabin locker with the packet. The same day he tells his sister (Ysa "has known since Longdark 5", SEC-023). He told his sister and not his lover. Jaro reads the note in S06E08.

### Additions to approved events (folded in v0.4)

`amend` blocks (README §6) from the writer-houses dossiers; the approved records are unchanged.


The Furrow War (CY 87-88). Public: in the flood year CY 87 the Moll lords "cut their own dikes"; Dask levies march in to "rebuild the Reach"; Lord Rawlin Moll is killed at Hobb's Gate (PL-0079) in CY 88; Helm Galen Corvane sanctions the conquest; Thessa Moll marries a Dask second son (CY 89) - Dask of the Reach (HS-018). Truth: SEC-034.


Lord Weylin Ostry and his heir are lost on the Ostry bar in fog under a Corvane escort (CY 119); his sister Elowen marries Wystan Corvane (CY 120); the cadet line Corvane of the Roads (HS-027) keeps the forts. Truth: SEC-035.


Osbert Harrow, the last lord, dies childless in Fallow CY 251 of the Grey Cough (EV-0274). The Sluice Spire, the Sluice Voice and the twelve sluices' dry-tithe pass to Fennick, raised to great house in Longdark CY 251 by a Conclave vote of 5-3 (Corvane, Quell, Ilvane against; Lantry money bought Dask and the Choir). The arithmetic of that vote with Harrow's two voices vacant is DEC-06.


Osbert's last will leaves Harrow's second voice, the Hill Voice (a house's voice without a Spire since CY 1; DEC-02), "to the holder of my debts"; the Ring confirms it 5-3 (arithmetic: DEC-06). Harrow Hall becomes the Table House (PL-0071). Truth: SEC-036.

## 3. Episodes

Season 1 has exact dates (outline r2). For seasons 2-12 an episode record exists only where the canon already points to it; its dates are the **season span** from `saga_arc.md` until the season outline is approved.

```canon
id: S01E01
type: episode
canon: approved
title: The Ninth Sluice
date_start: CY 312-10-06
date_end: CY 312-10-06
pov: [CH-0001, CH-0002, CH-0003]
```

pilot ~27 min (script v1.0: 26:39 of story). *(v0.7, director's decision on r7: one background seed in Sc 12 - one figure in the sea-green Quell block stands still and looks at Ruel; from behind, no name, no line, no reference sheet; it is Jaro Quell, SEC-046 - no other change to the pilot.)* **One day** (v0.5, lead's ruling R-1, `story/episodes/S01E01/continuity_check.md` v2): Longdark 6, from the dawn ebb to dark. The tithe-reading, the Helm's fall and the death-tone fall in the late afternoon and at the evening bell of the same day.

```canon
id: S01E02
type: episode
canon: approved
title: Candidates
date_start: CY 312-10-06
date_end: CY 312-10-10
pov: [CH-0001, CH-0005, CH-0010]
```

Opens on the night of Longdark 6, in the same second as the last frame of S01E01 (the hand-off scene); the rest of the episode is Longdark 8-10 (v0.5, R-1).

```canon
id: S01E03
type: episode
canon: approved
title: The Hush Law
date_start: CY 312-10-11
date_end: CY 312-10-14
pov: [CH-0001, CH-0002, CH-0003]
```

```canon
id: S01E04
type: episode
canon: approved
title: Ledger and Lantern
date_start: CY 312-10-15
date_end: CY 312-10-18
pov: [CH-0005, CH-0004, CH-0003]
```

```canon
id: S01E05
type: episode
canon: approved
title: Mudlark
date_start: CY 312-10-19
date_end: CY 312-10-21
pov: [CH-0001, CH-0002]
```

```canon
id: S01E06
type: episode
canon: approved
title: Skin, Not Mouth
date_start: CY 312-10-22
date_end: CY 312-10-24
pov: [CH-0010, CH-0003, CH-0005]
```

```canon
id: S01E07
type: episode
canon: approved
title: Echo
date_start: CY 312-10-25
date_end: CY 312-10-30
pov: [CH-0003, CH-0001, CH-0006]
```

```canon
id: S01E08
type: episode
canon: approved
title: Still Day One
date_start: CY 312-10-31
date_end: CY 312-11-01
pov: [CH-0004, CH-0002, CH-0001]
```

Still 1 (DEC-04): Ione does not sing a retuning; she stands in the muster of Cantors at the Choir Spire as the retuning parties leave for the coast, and counts how few they are. Ruel is stabbed that night.

```canon
id: S01E09
type: episode
canon: approved
title: The Steps
date_start: CY 312-11-02
date_end: CY 312-11-03
pov: [CH-0005, CH-0006, CH-0010]
```

Still 2 → dusk of Still 3 (DEC-15): Ruel, stabbed on the night of Still 1 (S01E08), dies on Still 2; countdown line "Account Nine closes on the third Still Day"; the cliffhanger is dusk, Still 3, when the Sluice Spire falls silent.

```canon
id: S01E10
type: episode
canon: approved
title: Still Water
date_start: CY 312-11-03
date_end: CY 312-11-03
pov: [CH-0001, CH-0002, CH-0004]
```

[LONG-24]

```canon
id: S01E11
type: episode
canon: approved
title: Ink
date_start: CY 312-11-04
date_end: CY 312-11-04
pov: [CH-0003, CH-0006, CH-0002]
```

```canon
id: S01E12
type: episode
canon: approved
title: The Sunken Vote
date_start: CY 312-11-05
date_end: CY 313-01-06
pov: [CH-0010, CH-0006, CH-0001]
```

[LONG-28]; tag scene at the Stair, Firstwater 6, CY 313

```canon
id: S02E01
type: episode
canon: approved
date_start: CY 313-01-01
date_end: CY 313-06-36
```

```canon
id: S02E02
type: episode
canon: approved
date_start: CY 313-01-01
date_end: CY 313-06-36
```

```canon
id: S02E03
type: episode
canon: approved
date_start: CY 313-01-01
date_end: CY 313-06-36
```

```canon
id: S02E04
type: episode
canon: approved
date_start: CY 313-01-01
date_end: CY 313-06-36
```

```canon
id: S02E05
type: episode
canon: approved
date_start: CY 313-01-01
date_end: CY 313-06-36
```

```canon
id: S02E06
type: episode
canon: approved
date_start: CY 313-01-01
date_end: CY 313-06-36
```

```canon
id: S02E07
type: episode
canon: approved
date_start: CY 313-01-01
date_end: CY 313-06-36
```

```canon
id: S02E08
type: episode
canon: approved
date_start: CY 313-01-01
date_end: CY 313-06-36
```

```canon
id: S02E09
type: episode
canon: approved
date_start: CY 313-01-01
date_end: CY 313-06-36
```

```canon
id: S02E10
type: episode
canon: approved
date_start: CY 313-01-01
date_end: CY 313-06-36
```

```canon
id: S02E11
type: episode
canon: approved
date_start: CY 313-01-01
date_end: CY 313-06-36
```

```canon
id: S03E02
type: episode
canon: approved
date_start: CY 313-07-01
date_end: CY 314-02-36
```

```canon
id: S03E03
type: episode
canon: approved
date_start: CY 313-07-01
date_end: CY 314-02-36
```

```canon
id: S03E04
type: episode
canon: approved
date_start: CY 313-07-01
date_end: CY 314-02-36
```

```canon
id: S03E05
type: episode
canon: approved
date_start: CY 313-07-01
date_end: CY 314-02-36
```

```canon
id: S03E06
type: episode
canon: approved
date_start: CY 313-07-01
date_end: CY 314-02-36
```

```canon
id: S03E07
type: episode
canon: approved
date_start: CY 313-07-01
date_end: CY 314-02-36
```

```canon
id: S03E08
type: episode
canon: approved
date_start: CY 313-07-01
date_end: CY 314-02-36
```

```canon
id: S03E09
type: episode
canon: approved
date_start: CY 313-07-01
date_end: CY 314-02-36
```

```canon
id: S03E10
type: episode
canon: approved
date_start: CY 313-07-01
date_end: CY 314-02-36
```

```canon
id: S03E11
type: episode
canon: approved
date_start: CY 313-07-01
date_end: CY 314-02-36
```

```canon
id: S03E12
type: episode
canon: approved
date_start: CY 313-07-01
date_end: CY 314-02-36
```

```canon
id: S04E02
type: episode
canon: approved
date_start: CY 314-03-01
date_end: CY 314-11-05
```

```canon
id: S04E03
type: episode
canon: approved
date_start: CY 314-03-01
date_end: CY 314-11-05
```

```canon
id: S04E04
type: episode
canon: approved
date_start: CY 314-03-01
date_end: CY 314-11-05
```

```canon
id: S04E06
type: episode
canon: approved
date_start: CY 314-03-01
date_end: CY 314-11-05
```

```canon
id: S04E07
type: episode
canon: approved
date_start: CY 314-03-01
date_end: CY 314-11-05
```

```canon
id: S04E08
type: episode
canon: approved
date_start: CY 314-03-01
date_end: CY 314-11-05
```

```canon
id: S04E09
type: episode
canon: approved
date_start: CY 314-03-01
date_end: CY 314-11-05
```

```canon
id: S04E10
type: episode
canon: approved
date_start: CY 314-03-01
date_end: CY 314-11-05
```

```canon
id: S04E11
type: episode
canon: approved
date_start: CY 314-03-01
date_end: CY 314-11-05
```

```canon
id: S04E12
type: episode
canon: approved
date_start: CY 314-03-01
date_end: CY 314-11-05
```

```canon
id: S05E02
type: episode
canon: approved
date_start: CY 320-05-01
date_end: CY 320-11-05
```

```canon
id: S05E03
type: episode
canon: approved
date_start: CY 320-05-01
date_end: CY 320-11-05
```

```canon
id: S05E04
type: episode
canon: approved
date_start: CY 320-05-01
date_end: CY 320-11-05
```

```canon
id: S05E06
type: episode
canon: approved
date_start: CY 320-05-01
date_end: CY 320-11-05
```

```canon
id: S05E08
type: episode
canon: approved
date_start: CY 320-05-01
date_end: CY 320-11-05
```

```canon
id: S05E10
type: episode
canon: approved
date_start: CY 320-05-01
date_end: CY 320-11-05
```

```canon
id: S05E11
type: episode
canon: approved
date_start: CY 320-05-01
date_end: CY 320-11-05
```

```canon
id: S05E12
type: episode
canon: approved
date_start: CY 320-05-01
date_end: CY 320-11-05
```

```canon
id: S06E01
type: episode
canon: approved
date_start: CY 321-01-01
date_end: CY 321-11-05
```

```canon
id: S06E02
type: episode
canon: approved
date_start: CY 321-01-01
date_end: CY 321-11-05
```

(v0.7) The packet returned to Jaro unopened (EV-0344).

```canon
id: S06E03
type: episode
canon: approved
date_start: CY 321-01-01
date_end: CY 321-11-05
```

```canon
id: S06E04
type: episode
canon: approved
date_start: CY 321-01-01
date_end: CY 321-11-05
```

```canon
id: S06E05
type: episode
canon: approved
date_start: CY 321-01-01
date_end: CY 321-11-05
```

```canon
id: S06E07
type: episode
canon: approved
date_start: CY 321-01-01
date_end: CY 321-11-05
```

```canon
id: S06E08
type: episode
canon: approved
date_start: CY 321-01-01
date_end: CY 321-11-05
```

```canon
id: S06E09
type: episode
canon: approved
date_start: CY 321-01-01
date_end: CY 321-11-05
```

```canon
id: S06E10
type: episode
canon: approved
date_start: CY 321-01-01
date_end: CY 321-11-05
```

```canon
id: S06E11
type: episode
canon: approved
date_start: CY 321-01-01
date_end: CY 321-11-05
```

```canon
id: S06E12
type: episode
canon: approved
date_start: CY 321-01-01
date_end: CY 321-11-05
```

```canon
id: S07E01
type: episode
canon: approved
date_start: CY 322-01-01
date_end: CY 322-11-05
```

```canon
id: S07E02
type: episode
canon: approved
date_start: CY 322-01-01
date_end: CY 322-11-05
```

```canon
id: S07E03
type: episode
canon: approved
date_start: CY 322-01-01
date_end: CY 322-11-05
```

```canon
id: S07E05
type: episode
canon: approved
date_start: CY 322-01-01
date_end: CY 322-11-05
```

```canon
id: S07E06
type: episode
canon: approved
date_start: CY 322-01-01
date_end: CY 322-11-05
```

```canon
id: S07E07
type: episode
canon: approved
date_start: CY 322-01-01
date_end: CY 322-11-05
```

```canon
id: S07E08
type: episode
canon: approved
date_start: CY 322-01-01
date_end: CY 322-11-05
```

```canon
id: S07E10
type: episode
canon: approved
date_start: CY 322-01-01
date_end: CY 322-11-05
```

```canon
id: S07E11
type: episode
canon: approved
date_start: CY 322-01-01
date_end: CY 322-11-05
```

```canon
id: S07E12
type: episode
canon: approved
date_start: CY 322-01-01
date_end: CY 322-11-05
```

```canon
id: S08E02
type: episode
canon: approved
date_start: CY 323-01-01
date_end: CY 323-11-05
```

```canon
id: S08E03
type: episode
canon: approved
date_start: CY 323-01-01
date_end: CY 323-11-05
```

```canon
id: S08E04
type: episode
canon: approved
date_start: CY 323-01-01
date_end: CY 323-11-05
```

```canon
id: S08E06
type: episode
canon: approved
date_start: CY 323-01-01
date_end: CY 323-11-05
```

```canon
id: S08E08
type: episode
canon: approved
date_start: CY 323-01-01
date_end: CY 323-11-05
```

```canon
id: S08E09
type: episode
canon: approved
date_start: CY 323-01-01
date_end: CY 323-11-05
```

```canon
id: S08E10
type: episode
canon: approved
date_start: CY 323-01-01
date_end: CY 323-11-05
```

```canon
id: S08E11
type: episode
canon: approved
date_start: CY 323-01-01
date_end: CY 323-11-05
```

```canon
id: S09E04
type: episode
canon: approved
date_start: CY 324-01-01
date_end: CY 325-11-05
```

```canon
id: S09E05
type: episode
canon: approved
date_start: CY 324-01-01
date_end: CY 325-11-05
```

```canon
id: S09E06
type: episode
canon: approved
date_start: CY 324-01-01
date_end: CY 325-11-05
```

```canon
id: S09E07
type: episode
canon: approved
date_start: CY 324-01-01
date_end: CY 325-11-05
```

```canon
id: S09E08
type: episode
canon: approved
date_start: CY 324-01-01
date_end: CY 325-11-05
```

```canon
id: S09E10
type: episode
canon: approved
date_start: CY 324-01-01
date_end: CY 325-11-05
```

```canon
id: S09E11
type: episode
canon: approved
date_start: CY 324-01-01
date_end: CY 325-11-05
```

```canon
id: S09E12
type: episode
canon: approved
date_start: CY 324-01-01
date_end: CY 325-11-05
```

```canon
id: S10E03
type: episode
canon: approved
date_start: SY 1-01-01
date_end: SY 1-11-05
```

```canon
id: S10E05
type: episode
canon: approved
date_start: SY 1-01-01
date_end: SY 1-11-05
```

```canon
id: S10E06
type: episode
canon: approved
date_start: SY 1-01-01
date_end: SY 1-11-05
```

```canon
id: S10E09
type: episode
canon: approved
date_start: SY 1-01-01
date_end: SY 1-11-05
```

```canon
id: S10E10
type: episode
canon: approved
date_start: SY 1-01-01
date_end: SY 1-11-05
```

```canon
id: S10E11
type: episode
canon: approved
date_start: SY 1-01-01
date_end: SY 1-11-05
```

```canon
id: S11E06
type: episode
canon: approved
date_start: SY 2-01-01
date_end: SY 2-11-05
```

```canon
id: S11E08
type: episode
canon: approved
date_start: SY 2-01-01
date_end: SY 2-11-05
```

```canon
id: S11E10
type: episode
canon: approved
date_start: SY 2-01-01
date_end: SY 2-11-05
```

```canon
id: S11E11
type: episode
canon: approved
date_start: SY 2-01-01
date_end: SY 2-11-05
```

```canon
id: S11E12
type: episode
canon: approved
date_start: SY 2-01-01
date_end: SY 2-11-05
```

```canon
id: S12E11
type: episode
canon: approved
date_start: SY 2-01-01
date_end: SY 3-11-05
```

```canon
id: S12E12
type: episode
canon: approved
date_start: SY 2-01-01
date_end: SY 3-11-05
```

```canon
id: S12E13
type: episode
canon: approved
date_start: ?
```

S12E13 (epilogue): decades after S12; date restricted (DEC-13, `sealed/`).

## 4. Season overview

| Season | Title | In-world dates | Main arc | Key events | Secrets revealed |
|---|---|---|---|---|---|
| S1 | Dry Tithe | CY 312-10-06 → CY 312-11-05 (+ tag CY 313-01-06) | election | EV-0300…0306 | SEC-001 |
| S2 | The Purchased Seat | CY 313-01 → 313-06 | the Helm's War | EV-0307, EV-0308 | SEC-013, SEC-015, SEC-023 |
| S3 | The Stair | CY 313-07 → 314-02 | Ossari invasion | EV-0310, EV-0311 | SEC-002, SEC-009 |
| S4 | Still Days | CY 314-03 → 314-11-05 | occupation; the weir | EV-0313…0317 | SEC-004, SEC-029 |
| skip | — | CY 315 → CY 320 | five years | — | — |
| S5 | A Thousand Voices | CY 320-05 → 320-11 | the Hum | EV-0318, EV-0319 | SEC-003, SEC-005, SEC-028 |
| S6 | Ledger of the Drowned | CY 321 | bank crash; election | EV-0320…0324 | SEC-006, SEC-007 (+SEC-001 public) |
| S7 | Thirst | CY 322 | the water war | EV-0325, EV-0326 | SEC-008, SEC-019, SEC-024 (audience) |
| S8 | The Spiral | CY 323 | siege; the archive | EV-0327…0329 | SEC-012, SEC-014, SEC-016 |
| S9 | The Ninth Vote | CY 324 → CY 325-11-05 | the Raising; the crown | EV-0330…0332 | SEC-010, SEC-017, SEC-022 |
| S10 | Sovereign | SY 1 | tyranny | EV-0333, EV-0334 | SEC-020, SEC-021, SEC-025, SEC-026 |
| S11 | Lirenne | SY 2 | the Long Ebb | EV-0335…0337 | SEC-011, SEC-018 |
| S12 | The Low Note | SY 2 → SY 3 (13 episodes; epilogue decades later) | the Great Chorus | EV-0338, EV-0339 | SEC-027 (last step), SEC-011b |

Twelve seasons, 145 episodes (S12: 13). Running times: `studio/story/series_bible.md` §11. One time skip: S4→S5.

## EXAMPLE (placeholder, not canon)

```canon
id: ERA-EX-OT
type: era
canon: draft
example: true
abbr: OT
name: Old Tides
abs_start: 0
```

```canon
id: ERA-EX-SR
type: era
canon: draft
example: true
abbr: SR
name: Salt Reckoning
abs_start: 600
ended_by:
```

```canon
id: EV-EX-0001
type: event
canon: draft
example: true
name: Founding of House Varnel
date: SR 120
place: PL-EX-0002
houses: [HS-EX-001]
participants: [CH-EX-0001]
```

```canon
id: EV-EX-0002
type: event
canon: draft
example: true
name: The Low-Tide Drowning
date: SR 146-11-03
place: PL-EX-0002
houses: [HS-EX-001]
killed: [CH-EX-0001]
secrets: [SEC-EX-001]
episode: S01E02
flashback: true
```

Prose (EXAMPLE): Publicly, Oren Varnel drowned crossing to Greyhold. In truth — see SEC-EX-001.

```canon
id: S01E01
type: episode
canon: draft
example: true
title: Low Water
date_start: SR 162-03-01
date_end: SR 162-03-04
pov: [CH-EX-0003]
```

```canon
id: S01E02
type: episode
canon: draft
example: true
title: Salt Memory
date_start: SR 162-03-05
date_end: SR 162-03-09
pov: [CH-EX-0003]
```
