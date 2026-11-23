# Canon changelog

One line per change. Newest on top. Format: `vX.Y · date · proposed by · record(s) · change`.

## v0.3 · 2026-11-22 · writer-houses + writer-characters (dossiers, draft) · merged by lore-keeper

Everything merged from the dossiers is `canon: draft` (the lead screenwriter approves); the foundation stays `approved` and unchanged. Additions to approved records are `amend` blocks (README §6); values that contradict the approved canon were **not** merged and are in `decisions_for_lead.md`.

- **decisions_for_lead.md** (new): one list of 64 decisions (DEC-01…64) - the 22 foundation issues of report r2, writer-houses Q-01…19, writer-characters' questions, and the keeper's new findings from the cross-check (11 new items, 7 items extended); 17 block season 1; restricted secrets only as "закрытая" (map in `sealed/` §H). Plus 7 questions closed by the keeper from approved canon.
- **houses/**: dossiers of HS-001…012, HS-090…093 merged below each approved record (amend: founders, heads, lands, alliances, words/sigils of the fallen houses, secrets; prose: public and true history, culture, power and money, schemes on three floors, production notes); the Ossari power (HS-091), the Guild and the Undertow (HS-092/093), free companies (HS-095), the Listeners (HS-006), the Quiet as a power (HS-094); **21 new minor houses and clans HS-013…033** (one file each). Heads after S2E11/S3E11/S10E11/S11E8: TODO stubs (DEC-30…32).
- **characters/**: dossiers of 18 main and ~33 second-circle characters merged as amend + prose (look incl. silhouette and body, voice, goals, biography, arcs); genealogy links of the main cast (parents, spouses); **7 new characters CH-0071…0077** (Dakka Den, Itsek, Gant, Nim, Ansel Fray, Orm Hask, Novice Sedge); writer-characters' CH-0070 Sal Tern = the existing CH-0067 (merged, CH-0070 never issued); **`_minor-houses.md` (new): 49 lineage records CH-0200…0287 + CH-0204 Wystan Corvane (keeper)**. Not merged (approved values kept): Ione's death day, Wick's and Silt's death years, Tibb's birth, first appearances of Maren, Cressa, Tsura, Sabin, Bede, Fossett (DEC-17, 22, 23, 24); restricted secret tags moved to `sealed/`.
- **ID conflicts resolved:** writer-characters CH-0071…0077 kept (no clash with CH-0200…0287); SEC-030, SEC-031 kept; SEC-032 not issued (DEC-49); writer-houses SEC-C01…C07 → SEC-034…040; new SEC-033, SEC-041…045; places PL-0070…0078 kept; EV-0264…0273 kept.
- **world.md**: §5a 14 new places PL-0070…0083 (the Rim, the Table House, Rimgate, the Goat Stair, the Brackwater salt pans, the Long Mole, the Concord Arsenal, the Rusk House-in-Exile, the Map Office, Hobb's Gate, Second-Fifth Sluices); §7 Power and money (Conclave procedure, the Helms CY 1-312, the Tithe Map, prices and wages, dry-notes and Account Nine in numbers, salvage bonds, the Hearings, the Still Days schedule, 24 schemes) with **10 draft laws RULE-015…024**; Spire home tones (draft); §8 Life of the Lows and the Mids.
- **timeline.md**: 12 new events EV-0264…0275 (Sunk Charter, Relay, Unison Decree, Salt War, Stair Treaty, Clerks' Ordinance, Kite War, Paper Ordinance, Exchange Panic, Rim Skirmish, Grey Cough; EV-0275 Esk's hostage-giving with date stub DEC-20); amends of EV-0250, 0251, 0253, 0254.
- **secrets.md**: 15 new secrets SEC-030, 031, 033…045 (draft; reveals open: TODO DEC-37…45); knowers added to SEC-013, SEC-019, SEC-029 (amend).
- **sealed/sealed.md**: §H - 8 draft overlays (restricted tags on CH-0013, CH-0014, CH-0044, HS-001, HS-004, HS-026, HS-091, HS-093), the keeper's check of the dossiers against the restricted file, the DEC → restricted-secret table.
- **glossary.md**: **280 new terms** TERM-0214…0493 with TTS respellings (new characters and lineages, older heads and First Cantors without IDs, Ashare rulers, houses and clans, Ossari clans, places, law/money/history words, 36 Lows and Mids slang words); refs added to Isembar and Sereth.
- **genealogy/README.md**: v0.3 trees, "where the official tree lies".
- **README**: v0.3 ID allocation (CH-0066…0099 / 0100…0199 reserved / 0200…0299 lineages, HS-013…089, PL-0070+, EV to 0275, SEC-030+, RULE-015+, TERM-0214+); `amend` blocks; §6a TODO stubs; overlay lists are added; relation kinds and classes (clerk, physician). checklist: TODO/draft line. Template: classes.
- **tools/validate.py**: `amend: true` merge (fills, narrows dates, extends lists, error on contradiction); overlays add list items; TODO stubs `TODO(DEC-NN)` checked against `decisions_for_lead.md`, counted, listed with `--todo`; no draft-reference warning for amended fields; summary shows drafts, amends, stubs.
- Validator: **955 records (621 draft, 75 amend blocks), 0 errors, 0 warnings, 19 TODO stubs**. EXAMPLE records: 23, 0 errors.

## v0.2 · 2026-11-22 · lead-screenwriter (foundation r2, approved by the director) · transfer: lore-keeper

- world.md: premise; RULE-001…011 from series_bible §5 (r2 clarifications of RULE-001 breath-tone and RULE-004 "old stones ring low"); new RULE-012 (the upstream drain, mechanism of SEC-008, not public); society, money, religion; CAL-MAIN (10×36 + 5 Still Days, 6-day week); 50 places PL-0001…0065 with hierarchy and holders; travel table; §6 custody of the saga objects (shard, ring, clip, fork, earring, cap, pin, Silt's book, Lucan's chest).
- timeline.md: eras ERA-BA (abs 0), ERA-OS (400), ERA-CY (1100), ERA-SY (1425, SY 1 = CY 326); 63 events (EV-0001…0263 before the saga, EV-0300…0339 the saga, "Still Days flood", "weir", not "dam"); S01E01…E12 with exact dates; 87 episode records S2–S12 referenced by the canon, dated by season span until each outline is approved; season overview.
- houses/: HS-001…012 (7 great, 5 extinct/fallen) and HS-090…095 non-house powers (Choir, Ossari, Pumpwrights' Guild, Undertow, the Quiet, Lantern Company) at foundation level.
- characters/: 27 main records (25 heroes of the roster + Nan, Vesna) and 26 second-circle/history records in `_minor-*.md`; new keeper records CH-0067 Sal Tern, CH-0068 Ilse Ilvane (named in the foundation).
- secrets.md: SEC-001…009, 012, 013, 015…017, 019, 022, 023, 028, 029 (r2 wordings); IDs kept; SEC-011 = lead's SEC-011a (Quire), SEC-011b = the Chronicler.
- sealed/sealed.md (new, restricted): SEC-010, 011, 011b, 014, 018, 020, 021, 024, 025, 026, 027; CH-0066 Hesh Oshra; overlays for CH-0001, 0003, 0006, 0012, 0015, 0017, 0042 and SEC-002, 003, 008; EV-0255; RULE-013, RULE-014; restricted names; pre-saga custody of the objects; Chronicler wording table.
- glossary.md: 211 terms + 2 restricted (people, houses, places, titles, words, months, weekdays, seasons, eras, phrases) with TTS respellings - `canon: draft` until the lead confirms them; sound palettes.
- README: §8a sealed facts and overlays; ID allocation (HS-090+ powers, EV ranges, SEC suffix letters); no inline comments in blocks. checklist: restricted secrets line.
- tools/validate.py: secret IDs with a letter suffix; `overlay: true` merge; refs checked for `serves`, rule `secrets`, `reveal_steps`.
- Validator: 547 records, 0 errors, 0 warnings. EXAMPLE records kept (23, 0 errors).

## v0.1 · 2026-11-22 · lore-keeper

- Canon structure created: README, templates, checklist, validator. No world content yet (waiting for the lead screenwriter). Only EXAMPLE records (`example: true`) present.
