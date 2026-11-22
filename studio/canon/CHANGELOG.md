# Canon changelog

One line per change. Newest on top. Format: `vX.Y · date · proposed by · record(s) · change`.

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
