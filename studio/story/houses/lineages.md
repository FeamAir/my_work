# Lineages — the last three generations, and where the official trees lie

> **Revision r3 (lead-screenwriter, 2026-11-22 — rulings of `story/decisions_resolved.md`):** lineages **approved as a package** (DEC-27, DEC-28, DEC-29), with the renames Crispin Harrow, Tobin Moll, Pryor Ilvane (DEC-57). Heads after losses: Rusk — Sindre with Castellan Eirik (DEC-30); Corvane — Ysa as seal-holder, then Maren (DEC-31); Dask — Ylva (DEC-32). Secret numbers are final (SEC-034…036, 039).

Author: writer-houses · 2026-11-22 · brief r2 · Canon: v0.2 (IDs aligned) · status: draft
Spoiler level: **internal**.

How to use (canon rule "one fact — one place", `canon/genealogy/README.md`): parentage lives in **character** records, so the trees below are given as **minimal character stubs** (CH-0200…0287) that the keeper can move into `canon/characters/_minor-houses.md` without rewriting. Characters already owned by `writer-characters` (CH-0001…0065) are **not** written here; for them this file lists **link requests** (which `father`/`mother`/`relations` fields their records need). Older heads (before the last three generations) are names and years only, in each house dossier.

Ages at CY 312 for cast characters are from `cast_overview.md` (birth years derived: Ruel 264, Ysa 261, Maren 293, Lucan 241, Garrick 274, Vesna 239, Aurin 268, Cressa 272, Ione 294, Brenna 255, Jaro 276, Odo 257, Zev 298, Ursel 250, Piers 282).

---

## 1. Trees at a glance (official = public; true differences marked ◆)

```text
CORVANE                                   DASK
Stellan (232–290) ═ Wenna (238–305)       Bertil (214–280) ═ Rosamund (220–270)
   ├─ Ysa (261)                              ├─ Lucan (241–312) ═ Agathe (245–285), no children
   └─ Ruel (264–312) ═ Alys Whitlow*         └─ Edrin (248–301) ═ Hilde of the Reach (252–306)
         (270–300)                                 └─ Garrick (274) ═ Thyra Orsley* (280)
         └─ Maren (293)                                  └─ Ylva (301)

ILVANE                                    RUSK
Emeric (236–301) ═ Vesna (b. 239,         Bodvar (220–279) ═ Gisla (228–290)
   "daughter of Ilvane of the Crag")         ├─ Brenna (255–313) ═ Wilmot (250–300)
Tamlyn Pallis (240–298) ═ Imre (246–309)     │     └─ Ardo (278–309) ═ Dagny Hadden* (281)
   Aurin (268) ═ Cressa Pallis* (272)         │           └─ Sindre (302)  ← heir after S3 (proposal)
      ├─ Ilse (294–294)                      └─ Eirik (262)  ← castellan of the voice (proposal)
      └─ Ione (official b. 294) ◆ SEC-004

QUELL (Captain-Lords are elected)         FENNICK
Rourke of Rhee (236–289) ═ Jessamy (248–310)   Barnet (205–262)
   └─ Jaro (276)                              └─ Sefton (228–291) ═ Maud (234–280)
Jinna of Jutt (250) — deposed CY 303                └─ Odo (257) ═ Yolande (270–299)
                                                         └─ Zev (298)
LANTRY (head elected by the Table)
Hendrik (180–241) → Mattias (205–266) → Bastian (230–291)
Bastian ═ (1) Annick (232–270) → Rainer (253–302) ═ Elske (258–290) → Piers (282)
Bastian ═ (2) Ursel, née Merriden* (250) — no children; "grandmother" of Piers by marriage

ASHARE (extinct OS 700)
Taleh (~575–628) → Ulenne (~600–671) → Neveh (~648–700) ◆ SEC-003

* = proposal for writer-characters (spouse's origin family); see §4.
```

---

## 2. Character stubs (for the keeper)

### Corvane
```canon
id: CH-0203
type: character
canon: draft
name: Tolvar Corvane
epithet: the Admiral of the Breaking
house: HS-001
class: noble
role: minor
born: ~OS 660
died: CY 19
first_episode: origin
```
```canon
id: CH-0200
type: character
canon: draft
name: Stellan Corvane
house: HS-001
class: ruler
role: minor
born: CY 232
died: CY 290-09
relations: [CH-0201:spouse]
first_episode: origin
```
```canon
id: CH-0201
type: character
canon: draft
name: Wenna Corvane
house: HS-001
class: noble
role: minor
born: CY 238
died: CY 305
first_episode: origin
```
```canon
id: CH-0202
type: character
canon: draft
name: Alys Corvane
house: HS-001
class: noble
role: minor
born: CY 270
died: CY 300
first_episode: origin
```
> Wenna was born a Corvane of the Roads (HS-027); Alys a Whitlow (HS-028) — proposals, see §4. The Whitlows are an old Gullmouth family of Shoals descent, warm brown-skinned — which fits Maren's dossier ("darker than her father's, her mother's side").

### Dask
```canon
id: CH-0216
type: character
canon: draft
name: Hemmet Dask
house: HS-002
class: noble
role: minor
born: ~OS 655
died: CY 24
first_episode: origin
```
```canon
id: CH-0210
type: character
canon: draft
name: Bertil Dask
house: HS-002
class: ruler
role: minor
born: CY 214
died: CY 280
relations: [CH-0217:spouse]
first_episode: origin
```
```canon
id: CH-0217
type: character
canon: draft
name: Rosamund Dask
house: HS-002
class: noble
role: minor
born: CY 220
died: CY 270
first_episode: origin
```
```canon
id: CH-0211
type: character
canon: draft
name: Agathe Dask
house: HS-002
class: noble
role: minor
born: CY 245
died: CY 285
first_episode: origin
```
```canon
id: CH-0212
type: character
canon: draft
name: Edrin Dask
house: HS-002
class: noble
role: minor
born: CY 248
died: CY 301
father: CH-0210
mother: CH-0217
relations: [CH-0213:spouse]
first_episode: origin
```
```canon
id: CH-0213
type: character
canon: draft
name: Hilde Dask
epithet: of the Reach
house: HS-002
class: noble
role: minor
born: CY 252
died: CY 306
first_episode: origin
```
```canon
id: CH-0214
type: character
canon: draft
name: Thyra Dask
house: HS-002
class: noble
role: minor
born: CY 280
first_episode:
```
```canon
id: CH-0215
type: character
canon: draft
name: Ylva Dask
house: HS-002
class: noble
role: minor
born: CY 301
father: CH-0017
mother: CH-0214
first_episode:
```
> Hilde was born into Dask of the Reach (HS-018, Moll blood) — public. Thyra was born an Orsley (HS-031) — proposal. Ylva (11 in CY 312) is a possible Dask heir after Garrick drowns (S10E11); no plot is assigned to her here.

### Ilvane
```canon
id: CH-0224
type: character
canon: draft
name: Sereth Ilvane
epithet: the Matriarch
house: HS-003
class: clergy
role: minor
born: ~OS 660
died: CY 14
first_episode: origin
```
```canon
id: CH-0220
type: character
canon: draft
name: Emeric Ilvane
house: HS-003
class: ruler
role: minor
born: CY 236
died: CY 301
first_episode: origin
```
```canon
id: CH-0221
type: character
canon: draft
name: Tamlyn Pallis
house: HS-029
class: noble
role: minor
born: CY 240
died: CY 298
relations: [CH-0222:spouse]
first_episode: origin
```
```canon
id: CH-0222
type: character
canon: draft
name: Imre Pallis
house: HS-029
class: noble
role: minor
born: CY 246
died: CY 309
first_episode: origin
```
> Ilse is already in canon as **CH-0068** (keeper's record, EV-0257) — no stub here. Tamlyn and Imre are **Pallis** (HS-029), the cloister stewards: Cressa's birth-house, proposal.

### Rusk
```canon
id: CH-0236
type: character
canon: draft
name: Borra Rusk
house: HS-004
class: soldier
role: minor
born: ~OS 665
died: CY 26
first_episode: origin
```
```canon
id: CH-0230
type: character
canon: draft
name: Bodvar Rusk
house: HS-004
class: ruler
role: minor
born: CY 220
died: CY 279
relations: [CH-0237:spouse]
first_episode: origin
```
```canon
id: CH-0237
type: character
canon: draft
name: Gisla Rusk
house: HS-004
class: noble
role: minor
born: CY 228
died: CY 290
first_episode: origin
```
```canon
id: CH-0231
type: character
canon: draft
name: Wilmot Rusk
house: HS-004
class: noble
role: minor
born: CY 250
died: CY 300
first_episode: origin
```
```canon
id: CH-0232
type: character
canon: draft
name: Eirik Rusk
house: HS-004
class: soldier
role: supporting
born: CY 262
father: CH-0230
mother: CH-0237
first_episode:
```
```canon
id: CH-0233
type: character
canon: draft
name: Ardo Rusk
house: HS-004
class: soldier
role: minor
born: CY 278
died: CY 309
father: CH-0231
mother: CH-0018
relations: [CH-0234:spouse]
first_episode: origin
```
```canon
id: CH-0234
type: character
canon: draft
name: Dagny Rusk
house: HS-004
class: noble
role: minor
born: CY 281
first_episode:
```
```canon
id: CH-0235
type: character
canon: draft
name: Sindre Rusk
house: HS-004
class: noble
role: supporting
born: CY 302
father: CH-0233
mother: CH-0234
first_episode:
```
> `first_episode` left empty for living stubs (Thyra, Ylva, Eirik, Dagny, Sindre, Jinna): the lead places them.
> Dagny was born a Hadden of Rimgate (HS-025; a Tekka great-grandmother) — proposal. Sindre and Eirik are **proposals** for who carries the Rusk voice in exile (S4–S12); both are designed to be shown helmeted/at a distance. Question to the lead (report Q-04).

### Quell
```canon
id: CH-0243
type: character
canon: draft
name: Reske Quell
house: HS-005
class: ruler
role: minor
born: ~OS 670
died: CY 12
first_episode: origin
```
```canon
id: CH-0240
type: character
canon: draft
name: Rourke Quell
epithet: of Rhee
house: HS-005
class: ruler
role: minor
born: CY 236
died: CY 289
relations: [CH-0241:spouse]
first_episode: origin
```
```canon
id: CH-0241
type: character
canon: draft
name: Jessamy of Rhee
house: HS-020
class: noble
role: minor
born: CY 248
died: CY 310
first_episode: origin
```
```canon
id: CH-0242
type: character
canon: draft
name: Jinna Quell
epithet: of Jutt
house: HS-005
class: ruler
role: supporting
born: CY 250
first_episode:
```

### Fennick
```canon
id: CH-0250
type: character
canon: draft
name: Barnet Fennick
house: HS-006
class: ruler
role: minor
born: CY 205
died: CY 262
first_episode: origin
```
```canon
id: CH-0251
type: character
canon: draft
name: Sefton Fennick
house: HS-006
class: ruler
role: minor
born: CY 228
died: CY 291
father: CH-0250
relations: [CH-0253:spouse]
first_episode: origin
```
```canon
id: CH-0253
type: character
canon: draft
name: Maud Fennick
house: HS-006
class: noble
role: minor
born: CY 234
died: CY 280
first_episode: origin
```
```canon
id: CH-0252
type: character
canon: draft
name: Yolande Fennick
house: HS-006
class: noble
role: minor
born: CY 270
died: CY 299
first_episode: origin
```

### Lantry
```canon
id: CH-0260
type: character
canon: draft
name: Hendrik Lantry
house: HS-007
class: merchant
role: minor
born: CY 180
died: CY 241
first_episode: origin
```
```canon
id: CH-0261
type: character
canon: draft
name: Mattias Lantry
house: HS-007
class: merchant
role: minor
born: CY 205
died: CY 266
father: CH-0260
first_episode: origin
```
```canon
id: CH-0262
type: character
canon: draft
name: Bastian Lantry
house: HS-007
class: merchant
role: minor
born: CY 230
died: CY 291
father: CH-0261
relations: [CH-0263:spouse]
first_episode: origin
```
```canon
id: CH-0263
type: character
canon: draft
name: Annick Lantry
house: HS-007
class: merchant
role: minor
born: CY 232
died: CY 270
first_episode: origin
```
```canon
id: CH-0264
type: character
canon: draft
name: Rainer Lantry
house: HS-007
class: merchant
role: minor
born: CY 253
died: CY 302
father: CH-0262
mother: CH-0263
relations: [CH-0265:spouse]
first_episode: origin
```
```canon
id: CH-0265
type: character
canon: draft
name: Elske Lantry
house: HS-007
class: merchant
role: minor
born: CY 258
died: CY 290
first_episode: origin
```

### Extinct houses (founders and last heads)
```canon
id: CH-0271
type: character
canon: draft
name: Aldous Harrow
house: HS-009
class: ruler
role: minor
born: ~OS 665
died: CY 17
first_episode: origin
```
```canon
id: CH-0270
type: character
canon: draft
name: Osbert Harrow
house: HS-009
class: ruler
role: minor
born: CY 214
died: CY 251-08
first_episode: origin
```
```canon
id: CH-0275
type: character
canon: draft
name: Rawlin Moll
house: HS-010
class: ruler
role: minor
born: CY 40
died: CY 88
first_episode: origin
```
```canon
id: CH-0276
type: character
canon: draft
name: Thessa Moll
house: HS-018
class: noble
role: minor
born: CY 70
died: CY 130
father: CH-0275
first_episode: origin
```
```canon
id: CH-0278
type: character
canon: draft
name: Weylin Ostry
house: HS-011
class: ruler
role: minor
born: CY 85
died: CY 119
first_episode: origin
```
```canon
id: CH-0279
type: character
canon: draft
name: Elowen Ostry
house: HS-001
class: noble
role: minor
born: CY 95
died: CY 150
first_episode: origin
```
```canon
id: CH-0280
type: character
canon: draft
name: Lady of Vanth (name reserved for prequel P4)
house: HS-012
class: ruler
role: minor
born: ?
died: CY 141
first_episode: origin
```

### Ashare
```canon
id: CH-0287
type: character
canon: draft
name: Isembar Ashare
house: HS-008
class: ruler
role: minor
born: ~OS 370
died: ~OS 431
first_episode: origin
```
```canon
id: CH-0285
type: character
canon: draft
name: Taleh Ashare
house: HS-008
class: ruler
role: minor
born: ~OS 575
died: OS 628
first_episode: origin
```
```canon
id: CH-0286
type: character
canon: draft
name: Ulenne Ashare
house: HS-008
class: ruler
role: minor
born: ~OS 600
died: OS 671
mother: CH-0285
first_episode: origin
```

---

## 3. Link requests for `writer-characters`' records

| Record (owner: writer-characters) | Fields this genealogy needs |
|---|---|
| CH-0005 Ruel Corvane | `father: CH-0200`, `mother: CH-0201`, `relations: [CH-0202:spouse]` |
| CH-0058 Ysa Corvane | `father: CH-0200`, `mother: CH-0201` |
| CH-0006 Maren Corvane | `father: CH-0005`, `mother: CH-0202` |
| CH-0016 Lucan Dask | `father: CH-0210`, `mother: CH-0217`, `relations: [CH-0211:spouse]` |
| CH-0017 Garrick Dask | `father: CH-0212`, `mother: CH-0213`, `relations: [CH-0214:spouse]` |
| CH-0012 Vesna Ilvane | **no parents** (official entry only: "daughter of Ilvane of the Crag", b. CY 239 — brief r2); `relations: [CH-0220:spouse]` |
| CH-0020 Aurin Ilvane | `father: CH-0220`, `mother: CH-0012`, `relations: [CH-0021:spouse]` |
| CH-0021 Cressa Ilvane | `father: CH-0221`, `mother: CH-0222` (born a Pallis, HS-029 — proposal; she keeps `house: HS-003`) |
| CH-0002 Ione Ilvane | `father: CH-0020`, `mother: CH-0021` (official); `true_father: CH-0024`, `true_mother: CH-0023`, `parentage_secret: SEC-004` |
| CH-0018 Brenna Rusk | `father: CH-0230`, `mother: CH-0237`, `relations: [CH-0231:spouse]` |
| CH-0019 Jaro Quell | `house: HS-005` (Captain-Lord, born of Clan Rhee HS-020), `father: CH-0240`, `mother: CH-0241` |
| CH-0010 Odo Fennick | `father: CH-0251`, `mother: CH-0253`, `relations: [CH-0252:spouse]` |
| CH-0042 Zev Fennick | `father: CH-0010`, `mother: CH-0252` |
| CH-0011 Ursel Lantry | `relations: [CH-0262:spouse]`; born a Merriden (HS-016) — proposal |
| CH-0061 Piers Lantry | `father: CH-0264`, `mother: CH-0265`; Ursel is his step-grandmother |
| CH-0030 Neveh Ashare | `father: CH-0286` |
| CH-0279 Elowen Ostry (mine) | needs `relations: [CH-…:spouse]` → Wystan Corvane has no ID (older generation); keeper may add one or leave the marriage as event EV-0251 only |

---

## 4. Public vs true genealogy — where the official trees lie

Only the lies listed in the brief (§4) are used for main characters. Everything marked *proposal* is new and is **not** a parentage secret — it is the official, true origin of a spouse, offered to `writer-characters` to accept or replace.

| House | Official tree says | Truth | Secret |
|---|---|---|---|
| **Corvane** | Tolvar "took from the water all that could be taken" at the Breaking; the pearl "won at Lirenne" | Tolvar's ships sealed Lirenne's harbour during the massacre. The ring's history beyond "won at Lirenne": `[SEALED — ask lead]`. **No parentage lie** in the last three generations. | SEC-003; SEC-027 (sealed) |
| | *proposal:* Maren's mother Alys was a Whitlow (the purser family) | — | makes the S2E11 powder fraud a family betrayal |
| **Dask** | Garrick's mother Hilde was "of the Reach" (Moll blood, public) | as stated. **No parentage lie.** The founding lie is the *Broken Dike* (CY 87), not a birth | SEC-034 (candidate) |
| **Ilvane** | Ione, daughter of Aurin and Cressa, born CY 294; "the songblood"; Ilvane-born Cantors in the Book of the Blood | Ione is Ama of Ninth Sluice (true parents Liss and Dov), gleaned CY 295; Cressa's own daughter Ilse died CY 294-04. Of 31 "Ilvane-born" Cantors CY 250–312, at least 19 were gleaned (names not given; never on screen as a list). Vesna: official entry only. | SEC-004, SEC-005; Vesna `[SEALED]` |
| **Fennick** | Barnet → Sefton → Odo → Zev | **true.** The lie about Fennick is political (the bought elevation of CY 251), not genealogical | — |
| **Lantry** | Piers is "Dame Ursel's grandson" | true **by marriage**: Ursel (b. 250) is Bastian's second wife; Piers (b. 282) is Bastian's grandson by his first wife Annick. Not a secret — it is why the Table, not blood, chose Ursel, and why Piers "wants out" | (arithmetic note for the lead: a blood grandson is impossible at these ages) |
| **Ashare** | the Tide-Kings from OS 1; Neveh mad; the line ended with her | Neveh was not mad (SEC-003). Keepers before ~OS 400 were elected, not all Ashare (P2 ground). Whether any Ashare child survived: `[SEALED — ask lead]`. The Pretender (S6) is false (SEC-016). | SEC-003, SEC-016 |

### Minor-house genealogy secrets (allowed: new candidates)
- **SEC-035 (Ostry):** the fog of CY 119 that made Elowen Ostry an heiress was arranged by Wystan Corvane's escort.
- **SEC-036 (Harrow/Kilbride):** Osbert Harrow's natural son (b. CY 240) was named heir of the Hill Voice in the CY 247 will; the CY 251 deathbed will replaced him with "the holder of my debts".
- **SEC-039 (Hadden):** besides the known Tekka marriage of CY 206, the Haddens guide the back-trade on the Goat Stair (a scheme, not parentage).
