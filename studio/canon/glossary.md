# Glossary and pronunciation

Canon: v0.1 · Status: **empty**.

Every name that is spoken on screen — characters, houses, places, titles, invented words — has one entry. Voice synthesis (ElevenLabs) reads the `say` respelling; subtitles and on-screen text use `term`.

## Fields

```canon-template
id: TERM-NNNN
type: term
canon: draft
term:          # exact spelling, as in subtitles
say:           # respelling for TTS, stressed syllable in CAPS: "TAM-sin VAR-nel"
ipa:           # optional, /ˈtæmsɪn ˈvɑːrnəl/
kind:          # person | house | place | title | word | phrase | object
ref:           # CH-/HS-/PL-/… id this term names (empty for common words)
meaning:       # for invented words
```

## Naming rules

1. **No two important names start with the same 3 letters** within one region or house generation; avoid names differing by one letter (viewers and TTS confuse them).
2. Each culture/region has its own sound palette (listed below once the world exists) so viewers can tell origins by ear.
3. No names from existing well-known works, no real historical figures, no real brands.
4. Spelling must be pronounceable by an English TTS voice from the respelling alone; test the `say` line before approval.
5. Titles and forms of address (Lord, Warden, …) are entries too.

## Sound palettes by culture

| Culture / region | Sounds / syllables | Example pattern | Avoid |
|---|---|---|---|
| | | | |

## Entries

_(empty)_

---

## EXAMPLE (placeholder, not canon)

```canon
id: TERM-EX-0001
type: term
canon: draft
example: true
term: Tamsin Varnel
say: TAM-sin VAR-nel
ipa: /ˈtæmsɪn ˈvɑːrnəl/
kind: person
ref: CH-EX-0003
```

```canon
id: TERM-EX-0002
type: term
canon: draft
example: true
term: Greyhold
say: GRAY-hold
kind: place
ref: PL-EX-0002
```

```canon
id: TERM-EX-0003
type: term
canon: draft
example: true
term: Oren Varnel
say: OR-en VAR-nel
kind: person
ref: CH-EX-0001
```

```canon
id: TERM-EX-0004
type: term
canon: draft
example: true
term: Ilsa Varnel
say: IL-sah VAR-nel
kind: person
ref: CH-EX-0002
```

```canon
id: TERM-EX-0005
type: term
canon: draft
example: true
term: Brannoch Hale
say: BRAN-ock HAIL
kind: person
ref: CH-EX-0004
```

```canon
id: TERM-EX-0006
type: term
canon: draft
example: true
term: House Varnel
say: HOWSS VAR-nel
kind: house
ref: HS-EX-001
```

```canon
id: TERM-EX-0007
type: term
canon: draft
example: true
term: Saltmere
say: SALT-meer
kind: place
ref: PL-EX-0001
```
