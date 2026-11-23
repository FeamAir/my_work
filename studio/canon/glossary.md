# Glossary and pronunciation

Canon: v0.2 · Status: **draft** (respellings proposed by the keeper; to be confirmed by the lead screenwriter and tested with the TTS voice) (foundation r2, approved by the director 2026-11-22; transfer by lore-keeper)

Every name spoken on screen has one entry. Voice synthesis reads `say` (stressed syllable in CAPS); subtitles and on-screen text use `term`. Entries for restricted names are in `sealed/`.

## Fields

```canon-template
id: TERM-NNNN
type: term
canon: draft
term:          # exact spelling, as in subtitles
say:           # respelling for TTS, stressed syllable in CAPS
ipa:           # optional
kind:          # person | house | place | title | word | phrase | object
ref:           # CH-/HS-/PL-/… id this term names
meaning:       # for invented words
```

## Naming rules

1. **No two important names start with the same 3 letters** within one region or house generation; avoid names differing by one letter. Known exceptions in the foundation are listed in the keeper's report 2026-11-22-r2 (Corr/Corvane, Marl/Maren, Lantern/Lantry; Quire = Choir by sound).
2. Each culture has its own sound palette (below).
3. No names from existing well-known works, no real historical figures, no real brands.
4. Spelling must be pronounceable by an English TTS voice from the respelling alone; test the `say` line before approval.
5. Titles and forms of address are entries too.

## Sound palettes by culture

| Culture / region | Sounds / syllables | Example | Avoid |
|---|---|---|---|
| Concord nobility | two syllables, consonant-heavy | Corvane, Fennick, Garrick | soft -eh endings |
| old Ashare / Lirenne | soft vowels, -eh, -enne, -ra | Neveh, Lirenne, Oshra | hard stops |
| Ossari | ts / k / d + open vowels | Tsura, Kadu, Esk | Concord two-syllable surnames |
| the Shoals | j / r sailors' names | Jaro | — |
| Lowfolk | one-syllable given names; surname = their sluice ("Pell of the Ninth") | Pell, Wick, Nan, Liss, Dov, Mags | (exceptions in the foundation: Lio, Orrie - see report) |

## Entries

### People

```canon
id: TERM-0001
type: term
canon: draft
term: Pell
say: PEL
kind: person
ref: CH-0001
```

```canon
id: TERM-0002
type: term
canon: draft
term: Ione Ilvane
say: eye-OH-nee IL-vayn
kind: person
ref: CH-0002
```

```canon
id: TERM-0003
type: term
canon: draft
term: Hollis Kett
say: HOL-iss KET
kind: person
ref: CH-0003
```

```canon
id: TERM-0004
type: term
canon: draft
term: Kes Mabry
say: KESS MAY-bree
kind: person
ref: CH-0004
```

```canon
id: TERM-0005
type: term
canon: draft
term: Ruel Corvane
say: ROO-el kor-VAYN
kind: person
ref: CH-0005
```

```canon
id: TERM-0006
type: term
canon: draft
term: Maren Corvane
say: MAR-en kor-VAYN
kind: person
ref: CH-0006
```

```canon
id: TERM-0007
type: term
canon: draft
term: Wick
say: WIK
kind: person
ref: CH-0007
```

```canon
id: TERM-0008
type: term
canon: draft
term: Odo Fennick
say: OH-doh FEN-ik
kind: person
ref: CH-0010
```

```canon
id: TERM-0009
type: term
canon: draft
term: Ursel Lantry
say: UR-sel LAN-tree
kind: person
ref: CH-0011
```

```canon
id: TERM-0010
type: term
canon: draft
term: Vesna Ilvane
say: VEZ-nah IL-vayn
kind: person
ref: CH-0012
```

```canon
id: TERM-0011
type: term
canon: draft
term: Tsura Den
say: TSOO-rah DEN
kind: person
ref: CH-0013
```

```canon
id: TERM-0012
type: term
canon: draft
term: Mother Silt
say: MUH-ther SILT
kind: person
ref: CH-0014
```

```canon
id: TERM-0013
type: term
canon: draft
term: Nan Oshra
say: NAN OSH-rah
kind: person
ref: CH-0015
```

```canon
id: TERM-0014
type: term
canon: draft
term: Lucan Dask
say: LOO-kan DASK
kind: person
ref: CH-0016
```

```canon
id: TERM-0015
type: term
canon: draft
term: Garrick Dask
say: GARR-ik DASK
kind: person
ref: CH-0017
```

```canon
id: TERM-0016
type: term
canon: draft
term: Brenna Rusk
say: BREN-ah RUSK
kind: person
ref: CH-0018
```

```canon
id: TERM-0017
type: term
canon: draft
term: Jaro Quell
say: JAH-roh KWEL
kind: person
ref: CH-0019
```

```canon
id: TERM-0018
type: term
canon: draft
term: Aurin Ilvane
say: OR-in IL-vayn
kind: person
ref: CH-0020
```

```canon
id: TERM-0019
type: term
canon: draft
term: Cressa Ilvane
say: KRESS-ah IL-vayn
kind: person
ref: CH-0021
```

```canon
id: TERM-0020
type: term
canon: draft
term: Brother Elm
say: BRUH-ther ELM
kind: person
ref: CH-0022
```

```canon
id: TERM-0021
type: term
canon: draft
term: Liss
say: LISS
kind: person
ref: CH-0023
```

```canon
id: TERM-0022
type: term
canon: draft
term: Dov
say: DAHV
kind: person
ref: CH-0024
```

```canon
id: TERM-0023
type: term
canon: draft
term: Teodor Kett
say: TAY-oh-dor KET
kind: person
ref: CH-0025
```

```canon
id: TERM-0024
type: term
canon: draft
term: Neveh Ashare
say: NEH-veh ah-SHAH-reh
kind: person
ref: CH-0030
```

```canon
id: TERM-0025
type: term
canon: draft
term: Oshra
say: OSH-rah
kind: person
ref: CH-0031
```

```canon
id: TERM-0026
type: term
canon: draft
term: Esk
say: ESK
kind: person
ref: CH-0040
```

```canon
id: TERM-0027
type: term
canon: draft
term: Dorran Strand
say: DOR-an STRAND
kind: person
ref: CH-0041
```

```canon
id: TERM-0028
type: term
canon: draft
term: Zev Fennick
say: ZEV FEN-ik
kind: person
ref: CH-0042
```

```canon
id: TERM-0029
type: term
canon: draft
term: Lio
say: LEE-oh
kind: person
ref: CH-0043
```

```canon
id: TERM-0030
type: term
canon: draft
term: Nell Tern
say: NEL TURN
kind: person
ref: CH-0044
```

```canon
id: TERM-0031
type: term
canon: draft
term: Daro Vey
say: DAH-roh VAY
kind: person
ref: CH-0045
```

```canon
id: TERM-0032
type: term
canon: draft
term: Tibb
say: TIB
kind: person
ref: CH-0046
```

```canon
id: TERM-0033
type: term
canon: draft
term: Kadu
say: KAH-doo
kind: person
ref: CH-0047
```

```canon
id: TERM-0034
type: term
canon: draft
term: Corr
say: KOR
kind: person
ref: CH-0048
```

```canon
id: TERM-0035
type: term
canon: draft
term: Mags
say: MAGZ
kind: person
ref: CH-0049
```

```canon
id: TERM-0036
type: term
canon: draft
term: Sister Marl
say: SIS-ter MARL
kind: person
ref: CH-0050
```

```canon
id: TERM-0037
type: term
canon: draft
term: Doctor Ambry
say: DOK-ter AM-bree
kind: person
ref: CH-0051
```

```canon
id: TERM-0038
type: term
canon: draft
term: Bede Lark
say: BEED LARK
kind: person
ref: CH-0052
```

```canon
id: TERM-0039
type: term
canon: draft
term: Captain Fitch
say: KAP-tin FITCH
kind: person
ref: CH-0053
```

```canon
id: TERM-0040
type: term
canon: draft
term: Widow Pruitt
say: WID-oh PROO-it
kind: person
ref: CH-0054
```

```canon
id: TERM-0041
type: term
canon: draft
term: Fossett
say: FOSS-et
kind: person
ref: CH-0055
```

```canon
id: TERM-0042
type: term
canon: draft
term: Sister Venn
say: SIS-ter VEN
kind: person
ref: CH-0056
```

```canon
id: TERM-0043
type: term
canon: draft
term: Cantor Sabin
say: KAN-tor SAY-bin
kind: person
ref: CH-0057
```

```canon
id: TERM-0044
type: term
canon: draft
term: Ysa Corvane
say: EE-sah kor-VAYN
kind: person
ref: CH-0058
```

```canon
id: TERM-0045
type: term
canon: draft
term: Rook Danner
say: ROOK DAN-er
kind: person
ref: CH-0059
```

```canon
id: TERM-0046
type: term
canon: draft
term: Archivist Ferro
say: AR-kiv-ist FERR-oh
kind: person
ref: CH-0060
```

```canon
id: TERM-0047
type: term
canon: draft
term: Piers Lantry
say: PEERZ LAN-tree
kind: person
ref: CH-0061
```

```canon
id: TERM-0048
type: term
canon: draft
term: Ottar
say: OT-ar
kind: person
ref: CH-0062
```

```canon
id: TERM-0049
type: term
canon: draft
term: Juno Brisk
say: JOO-noh BRISK
kind: person
ref: CH-0063
```

```canon
id: TERM-0050
type: term
canon: draft
term: Patch
say: PATCH
kind: person
ref: CH-0064
```

```canon
id: TERM-0051
type: term
canon: draft
term: Saltwife Orrie
say: SALT-wife OR-ee
kind: person
ref: CH-0065
```

```canon
id: TERM-0052
type: term
canon: draft
term: Sal Tern
say: SAL TURN
kind: person
ref: CH-0067
```

```canon
id: TERM-0053
type: term
canon: draft
term: Ilse Ilvane
say: IL-seh IL-vayn
kind: person
ref: CH-0068
```

### Houses and powers

```canon
id: TERM-0054
type: term
canon: draft
term: House Corvane
say: HOWSS kor-VAYN
kind: house
ref: HS-001
```

```canon
id: TERM-0055
type: term
canon: draft
term: House Dask
say: HOWSS DASK
kind: house
ref: HS-002
```

```canon
id: TERM-0056
type: term
canon: draft
term: House Ilvane
say: HOWSS IL-vayn
kind: house
ref: HS-003
```

```canon
id: TERM-0057
type: term
canon: draft
term: House Rusk
say: HOWSS RUSK
kind: house
ref: HS-004
```

```canon
id: TERM-0058
type: term
canon: draft
term: House Quell
say: HOWSS KWEL
kind: house
ref: HS-005
```

```canon
id: TERM-0059
type: term
canon: draft
term: House Fennick
say: HOWSS FEN-ik
kind: house
ref: HS-006
```

```canon
id: TERM-0060
type: term
canon: draft
term: House Lantry
say: HOWSS LAN-tree
kind: house
ref: HS-007
```

```canon
id: TERM-0061
type: term
canon: draft
term: House Ashare
say: HOWSS ah-SHAH-reh
kind: house
ref: HS-008
```

```canon
id: TERM-0062
type: term
canon: draft
term: House Harrow
say: HOWSS HARR-oh
kind: house
ref: HS-009
```

```canon
id: TERM-0063
type: term
canon: draft
term: House Moll
say: HOWSS MOL
kind: house
ref: HS-010
```

```canon
id: TERM-0064
type: term
canon: draft
term: House Ostry
say: HOWSS OSS-tree
kind: house
ref: HS-011
```

```canon
id: TERM-0065
type: term
canon: draft
term: House Vanth
say: HOWSS VANTH
kind: house
ref: HS-012
```

```canon
id: TERM-0066
type: term
canon: draft
term: the Choir
say: thuh KWIRE
kind: house
ref: HS-090
```

```canon
id: TERM-0067
type: term
canon: draft
term: the Ossari
say: thee oh-SAH-ree
kind: house
ref: HS-091
```

```canon
id: TERM-0068
type: term
canon: draft
term: the Pumpwrights' Guild
say: thuh PUMP-rites GILD
kind: house
ref: HS-092
```

```canon
id: TERM-0069
type: term
canon: draft
term: the Undertow
say: thee UN-der-toh
kind: house
ref: HS-093
```

```canon
id: TERM-0070
type: term
canon: draft
term: the Quiet
say: thuh KWY-et
kind: house
ref: HS-094
```

```canon
id: TERM-0071
type: term
canon: draft
term: the Lantern Company
say: thuh LAN-tern KUM-puh-nee
kind: house
ref: HS-095
```

### Places

```canon
id: TERM-0072
type: term
canon: draft
term: the Concord of Tessary
say: thuh KON-kord uv TESS-uh-ree
kind: place
ref: PL-0001
```

```canon
id: TERM-0073
type: term
canon: draft
term: the Aun
say: thee AWN
kind: place
ref: PL-0002
```

```canon
id: TERM-0074
type: term
canon: draft
term: the Many Mouths
say: thuh MEN-ee MOWTHZ
kind: place
ref: PL-0003
```

```canon
id: TERM-0075
type: term
canon: draft
term: Highwater
say: HY-waw-ter
kind: place
ref: PL-0004
```

```canon
id: TERM-0076
type: term
canon: draft
term: the Steps
say: thuh STEPS
kind: place
ref: PL-0005
```

```canon
id: TERM-0077
type: term
canon: draft
term: the Mids
say: thuh MIDZ
kind: place
ref: PL-0006
```

```canon
id: TERM-0078
type: term
canon: draft
term: the Lows
say: thuh LOHZ
kind: place
ref: PL-0007
```

```canon
id: TERM-0079
type: term
canon: draft
term: Ninth Sluice
say: NYNTH SLOOSS
kind: place
ref: PL-0008
```

```canon
id: TERM-0080
type: term
canon: draft
term: the Dry Palace
say: thuh DRY PAL-iss
kind: place
ref: PL-0009
```

```canon
id: TERM-0081
type: term
canon: draft
term: the Ring
say: thuh RING
kind: place
ref: PL-0010
```

```canon
id: TERM-0082
type: term
canon: draft
term: the Lantry Counting House
say: thuh LAN-tree KOWN-ting howss
kind: place
ref: PL-0011
```

```canon
id: TERM-0083
type: term
canon: draft
term: the Listening House
say: thuh LISS-en-ing howss
kind: place
ref: PL-0012
```

```canon
id: TERM-0084
type: term
canon: draft
term: the Choir temple
say: thuh KWIRE TEM-pul
kind: place
ref: PL-0013
```

```canon
id: TERM-0085
type: term
canon: draft
term: the Crown Spire
say: thuh KROWN SPY-er
kind: place
ref: PL-0014
```

```canon
id: TERM-0086
type: term
canon: draft
term: the Choir Spire
say: thuh KWIRE SPY-er
kind: place
ref: PL-0015
```

```canon
id: TERM-0087
type: term
canon: draft
term: the Sluice Spire
say: thuh SLOOSS SPY-er
kind: place
ref: PL-0016
```

```canon
id: TERM-0088
type: term
canon: draft
term: the Ilvane townhouse
say: thee IL-vayn TOWN-howss
kind: place
ref: PL-0017
```

```canon
id: TERM-0089
type: term
canon: draft
term: Highwater harbour
say: HY-waw-ter HAR-ber
kind: place
ref: PL-0018
```

```canon
id: TERM-0090
type: term
canon: draft
term: Nan's stilt-house
say: NANZ STILT-howss
kind: place
ref: PL-0019
```

```canon
id: TERM-0091
type: term
canon: draft
term: the Ninth Sluice back-canal
say: thuh NYNTH SLOOSS BAK-kuh-nal
kind: place
ref: PL-0020
```

```canon
id: TERM-0092
type: term
canon: draft
term: the Ninth Sluice evacuation gate
say: thuh NYNTH SLOOSS ee-vak-yoo-AY-shun GAYT
kind: place
ref: PL-0021
```

```canon
id: TERM-0093
type: term
canon: draft
term: the Ninth Sluice tide-post
say: thuh NYNTH SLOOSS TYD-post
kind: place
ref: PL-0022
```

```canon
id: TERM-0094
type: term
canon: draft
term: Mother Silt's barge
say: MUH-ther SILTS BARJ
kind: place
ref: PL-0023
```

```canon
id: TERM-0095
type: term
canon: draft
term: Hollis's garret
say: HOL-iss-iz GARR-et
kind: place
ref: PL-0024
```

```canon
id: TERM-0096
type: term
canon: draft
term: the Sluice Gates
say: thuh SLOOSS GAYTS
kind: place
ref: PL-0026
```

```canon
id: TERM-0097
type: term
canon: draft
term: the Ninth Bridge
say: thuh NYNTH BRIJ
kind: place
ref: PL-0027
```

```canon
id: TERM-0098
type: term
canon: draft
term: the Hundred Locks
say: thuh HUN-dred LOKS
kind: place
ref: PL-0028
```

```canon
id: TERM-0099
type: term
canon: draft
term: Gullmouth
say: GUL-mowth
kind: place
ref: PL-0030
```

```canon
id: TERM-0100
type: term
canon: draft
term: the Sentinel Spire
say: thuh SEN-tin-el SPY-er
kind: place
ref: PL-0031
```

```canon
id: TERM-0101
type: term
canon: draft
term: the Ostry harbour-forts
say: thee OSS-tree HAR-ber-forts
kind: place
ref: PL-0032
```

```canon
id: TERM-0102
type: term
canon: draft
term: the Polders
say: thuh POHL-derz
kind: place
ref: PL-0035
```

```canon
id: TERM-0103
type: term
canon: draft
term: Dask Barrows
say: DASK BARR-ohz
kind: place
ref: PL-0036
```

```canon
id: TERM-0104
type: term
canon: draft
term: the Sheaf Spire
say: thuh SHEEF SPY-er
kind: place
ref: PL-0037
```

```canon
id: TERM-0105
type: term
canon: draft
term: the Moll polders
say: thuh MOL POHL-derz
kind: place
ref: PL-0038
```

```canon
id: TERM-0106
type: term
canon: draft
term: Pale Crag
say: PAYL KRAG
kind: place
ref: PL-0040
```

```canon
id: TERM-0107
type: term
canon: draft
term: the Pale Spire
say: thuh PAYL SPY-er
kind: place
ref: PL-0041
```

```canon
id: TERM-0108
type: term
canon: draft
term: the Red Escarpment
say: thuh RED es-KARP-ment
kind: place
ref: PL-0045
```

```canon
id: TERM-0109
type: term
canon: draft
term: the Stair
say: thuh STAIR
kind: place
ref: PL-0046
```

```canon
id: TERM-0110
type: term
canon: draft
term: the Falls Spire
say: thuh FAWLZ SPY-er
kind: place
ref: PL-0047
```

```canon
id: TERM-0111
type: term
canon: draft
term: the falls of the Aun
say: thuh FAWLZ uv thee AWN
kind: place
ref: PL-0048
```

```canon
id: TERM-0112
type: term
canon: draft
term: the weir
say: thuh WEER
kind: place
ref: PL-0049
```

```canon
id: TERM-0113
type: term
canon: draft
term: the Ossari Uplands
say: thee oh-SAH-ree UP-lundz
kind: place
ref: PL-0050
```

```canon
id: TERM-0114
type: term
canon: draft
term: the Shelf lakes
say: thuh SHELF LAYKS
kind: place
ref: PL-0051
```

```canon
id: TERM-0115
type: term
canon: draft
term: the Shoals
say: thuh SHOHLZ
kind: place
ref: PL-0055
```

```canon
id: TERM-0116
type: term
canon: draft
term: Brackwater
say: BRAK-waw-ter
kind: place
ref: PL-0056
```

```canon
id: TERM-0117
type: term
canon: draft
term: the Storm Spire
say: thuh STORM SPY-er
kind: place
ref: PL-0057
```

```canon
id: TERM-0118
type: term
canon: draft
term: the Sunk
say: thuh SUNK
kind: place
ref: PL-0060
```

```canon
id: TERM-0119
type: term
canon: draft
term: Lirenne
say: lih-REN
kind: place
ref: PL-0061
```

```canon
id: TERM-0120
type: term
canon: draft
term: the Sunken Spire
say: thuh SUNK-en SPY-er
kind: place
ref: PL-0062
```

```canon
id: TERM-0121
type: term
canon: draft
term: the Open Grey
say: thee OH-pen GRAY
kind: place
ref: PL-0065
```

### Titles, words, calendar, phrases

```canon
id: TERM-0122
type: term
canon: draft
term: Helm
say: HELM
kind: title
meaning: elected ruler of the Concord, for life
```

```canon
id: TERM-0123
type: term
canon: draft
term: Your Steadiness
say: yor STED-ee-ness
kind: title
meaning: form of address to the Helm
```

```canon
id: TERM-0124
type: term
canon: draft
term: Sovereign
say: SOV-rin
kind: title
meaning: Maren's title from S09E12
```

```canon
id: TERM-0125
type: term
canon: draft
term: Cantor
say: KAN-tor
kind: title
meaning: a singer of the Spires; priest of the Choir
```

```canon
id: TERM-0126
type: term
canon: draft
term: First Cantor
say: FURST KAN-tor
kind: title
meaning: head of the Choir
```

```canon
id: TERM-0127
type: term
canon: draft
term: Lord Admiral
say: LORD AD-mer-ul
kind: title
meaning: head of the Concord fleet
```

```canon
id: TERM-0128
type: term
canon: draft
term: Captain-Lord
say: KAP-tin LORD
kind: title
meaning: elected head of the Quell island clans
```

```canon
id: TERM-0129
type: term
canon: draft
term: Dry Queen
say: DRY KWEEN
kind: title
meaning: war-leader of the Ossari
```

```canon
id: TERM-0130
type: term
canon: draft
term: Reedmaster
say: REED-mas-ter
kind: title
meaning: boss of a treadmill gang
```

```canon
id: TERM-0131
type: term
canon: draft
term: Saltwife
say: SALT-wife
kind: title
meaning: priestess of the Lady Below
```

```canon
id: TERM-0132
type: term
canon: draft
term: Gleaner
say: GLEE-ner
kind: word
meaning: Choir child-finder
```

```canon
id: TERM-0133
type: term
canon: draft
term: Listener
say: LISS-en-er
kind: word
meaning: Fennick informer or secret policeman
```

```canon
id: TERM-0134
type: term
canon: draft
term: Conclave
say: KON-klayv
kind: word
meaning: the eight-vote council that elects the Helm (meets in the Ring)
```

```canon
id: TERM-0135
type: term
canon: draft
term: the Sunken Vote
say: thuh SUNK-en VOHT
kind: word
meaning: the ninth vote of Lirenne (RULE-009)
```

```canon
id: TERM-0136
type: term
canon: draft
term: the Purchased Seat
say: thuh PUR-chast SEET
kind: word
meaning: Lantry's vote, bought from Harrow CY 252
```

```canon
id: TERM-0137
type: term
canon: draft
term: the Relay
say: thuh REE-lay
kind: word
meaning: Spire-to-Spire tone-code network (RULE-004)
```

```canon
id: TERM-0138
type: term
canon: draft
term: the Hearings
say: thuh HEER-ingz
kind: word
meaning: the courts, run by Fennick
```

```canon
id: TERM-0139
type: term
canon: draft
term: echo-stone
say: EK-oh stohn
kind: object
meaning: chip of Spire stone used by the Relay
```

```canon
id: TERM-0140
type: term
canon: draft
term: echo-shard
say: EK-oh shard
kind: object
meaning: an unlicensed echo-stone fragment
```

```canon
id: TERM-0141
type: term
canon: draft
term: hollowstone
say: HOL-oh-stohn
kind: word
meaning: the black singing stone of the Spires
```

```canon
id: TERM-0142
type: term
canon: draft
term: Spire
say: SPY-er
kind: word
meaning: one of the nine singing towers
```

```canon
id: TERM-0143
type: term
canon: draft
term: the ear
say: thee EER
kind: word
meaning: the gift of making a Spire answer
```

```canon
id: TERM-0144
type: term
canon: draft
term: songblood
say: SONG-blud
kind: word
meaning: the belief that the ear is inherited
```

```canon
id: TERM-0145
type: term
canon: draft
term: Great Song
say: GRAYT SONG
kind: word
meaning: a song of hours against storm or breach
```

```canon
id: TERM-0146
type: term
canon: draft
term: singing out
say: SING-ing OWT
kind: phrase
meaning: death of a voiceless singer who keeps singing
```

```canon
id: TERM-0147
type: term
canon: draft
term: breath-tone
say: BRETH-tohn
kind: word
meaning: the unvoiced tone a mute Cantor can still force
```

```canon
id: TERM-0148
type: term
canon: draft
term: Low Note
say: LOH NOHT
kind: word
meaning: the lullaby's part of the Spires' song (sealed meaning: SEC-002)
```

```canon
id: TERM-0149
type: term
canon: draft
term: dry-note
say: DRY-noht
kind: object
meaning: Lantry paper money
```

```canon
id: TERM-0150
type: term
canon: draft
term: dry-tithe
say: DRY-tythe
kind: word
meaning: protection tax paid by the Lows
```

```canon
id: TERM-0151
type: term
canon: draft
term: mark
say: MARK
kind: object
meaning: silver coin
```

```canon
id: TERM-0152
type: term
canon: draft
term: Tithe Map
say: TYTHE map
kind: object
meaning: yearly plan of which districts are sung first in a storm
```

```canon
id: TERM-0153
type: term
canon: draft
term: dry-pledge
say: DRY-plej
kind: word
meaning: Undertow protection racket
```

```canon
id: TERM-0154
type: term
canon: draft
term: Account Nine
say: uh-KOWNT NYNE
kind: word
meaning: Lantry's flood-speculation account
```

```canon
id: TERM-0155
type: term
canon: draft
term: Account Five
say: uh-KOWNT FYVE
kind: word
meaning: precursor of Account Nine (CY 295)
```

```canon
id: TERM-0156
type: term
canon: draft
term: Dry Charter
say: DRY CHAR-ter
kind: object
meaning: CY 295 deed transfer of drowned Ninth Sluice
```

```canon
id: TERM-0157
type: term
canon: draft
term: Hush Law
say: HUSH LAW
kind: word
meaning: RULE-006
```

```canon
id: TERM-0158
type: term
canon: draft
term: tide-post
say: TYD-post
kind: object
meaning: punishment post of the Lows
```

```canon
id: TERM-0159
type: term
canon: draft
term: Still Days
say: STIL DAYZ
kind: word
meaning: the five retuning days at year's end (RULE-010)
```

```canon
id: TERM-0160
type: term
canon: draft
term: mudlark
say: MUD-lark
kind: word
meaning: salvager of the flooded lanes
```

```canon
id: TERM-0161
type: term
canon: draft
term: treadmill walker
say: TRED-mil WAW-ker
kind: word
meaning: pump labourer
```

```canon
id: TERM-0162
type: term
canon: draft
term: debt-walker
say: DET-waw-ker
kind: word
meaning: treadmill walker working off a debt
```

```canon
id: TERM-0163
type: term
canon: draft
term: the Lady Below
say: thuh LAY-dee bih-LOH
kind: word
meaning: Lows folk faith
```

```canon
id: TERM-0164
type: term
canon: draft
term: the Hum
say: thuh HUM
kind: word
meaning: Pell's illegal singing circles (S5)
```

```canon
id: TERM-0165
type: term
canon: draft
term: Weir Terms
say: WEER TURMZ
kind: word
meaning: the CY 314 settlement (EV-0317)
```

```canon
id: TERM-0166
type: term
canon: draft
term: Spiral Book
say: SPY-rul BOOK
kind: object
meaning: Ashare text fragment (S5)
```

```canon
id: TERM-0167
type: term
canon: draft
term: the Chronicler
say: thuh KRON-ik-ler
kind: title
meaning: the narrator
```

```canon
id: TERM-0168
type: term
canon: draft
term: The Chronicle of the Dry Years
say: thuh KRON-ik-ul uv thuh DRY YEERZ
kind: object
meaning: the official record the narrator reads
```

```canon
id: TERM-0169
type: term
canon: draft
term: Quire
say: KWIRE
kind: person
meaning: the masked forger of S9-S11 (homophone of Choir - see the keeper's report)
```

```canon
id: TERM-0170
type: term
canon: draft
term: Builders
say: BIL-derz
kind: word
meaning: the official belief about who raised the Spires
```

```canon
id: TERM-0171
type: term
canon: draft
term: First Voices
say: FURST VOY-siz
kind: word
meaning: the Choir's name for the Builders
```

```canon
id: TERM-0172
type: term
canon: draft
term: Tide-King
say: TYD-king
kind: title
meaning: Chronicle title of the Ashare Keepers
```

```canon
id: TERM-0173
type: term
canon: draft
term: Keeper
say: KEE-per
kind: title
meaning: elected and later hereditary conductor of Lirenne
```

```canon
id: TERM-0174
type: term
canon: draft
term: the Breaking
say: thuh BRAY-king
kind: word
meaning: OS 700 (EV-0100)
```

```canon
id: TERM-0175
type: term
canon: draft
term: the Night of Still Water
say: thuh NYT uv STIL WAW-ter
kind: word
meaning: CY 295 (EV-0200)
```

```canon
id: TERM-0176
type: term
canon: draft
term: the Night of a Thousand Voices
say: thuh NYT uv uh THOW-zund VOY-siz
kind: word
meaning: CY 320 (EV-0319)
```

```canon
id: TERM-0177
type: term
canon: draft
term: the First Raising
say: thuh FURST RAY-zing
kind: word
meaning: S09E05 (EV-0330)
```

```canon
id: TERM-0178
type: term
canon: draft
term: the Long Ebb
say: thuh LONG EB
kind: word
meaning: once-in-a-century storm season (S11)
```

```canon
id: TERM-0179
type: term
canon: draft
term: the Great Chorus
say: thuh GRAYT KOR-us
kind: word
meaning: S12E12 (EV-0339)
```

```canon
id: TERM-0180
type: term
canon: draft
term: the Admiral's Pearl
say: thee AD-mer-ulz PURL
kind: object
meaning: Corvane heirloom ring
```

```canon
id: TERM-0181
type: term
canon: draft
term: Patient Gull
say: PAY-shent GUL
kind: object
meaning: Corvane flagship
```

```canon
id: TERM-0182
type: term
canon: draft
term: the Wet Saints
say: thuh WET SAYNTS
kind: word
meaning: a free company
```

```canon
id: TERM-0183
type: term
canon: draft
term: Isembar Ashare
say: IZ-em-bar ah-SHAH-reh
kind: person
meaning: Keeper who crowned the Keepership (prequel P2)
ref: CH-0287
```

```canon
id: TERM-0184
type: term
canon: draft
term: Sereth Ilvane
say: SEH-reth IL-vayn
kind: person
meaning: matriarch who led the Nine in OS 700 (prequel P3)
ref: CH-0224
```

```canon
id: TERM-0185
type: term
canon: draft
term: Builders' Age
say: BIL-derz AYJ
kind: word
ref: ERA-BA
meaning: era BA
```

```canon
id: TERM-0186
type: term
canon: draft
term: Old Song
say: OHLD SONG
kind: word
ref: ERA-OS
meaning: era OS
```

```canon
id: TERM-0187
type: term
canon: draft
term: Concord Year
say: KON-kord YEER
kind: word
ref: ERA-CY
meaning: era CY
```

```canon
id: TERM-0188
type: term
canon: draft
term: Sovereign Years
say: SOV-rin YEERZ
kind: word
ref: ERA-SY
meaning: era SY
```

```canon
id: TERM-0189
type: term
canon: draft
term: Firstwater
say: FURST-waw-ter
kind: word
meaning: month 1
```

```canon
id: TERM-0190
type: term
canon: draft
term: Rains
say: RAYNZ
kind: word
meaning: month 2
```

```canon
id: TERM-0191
type: term
canon: draft
term: Silting
say: SIL-ting
kind: word
meaning: month 3
```

```canon
id: TERM-0192
type: term
canon: draft
term: Reedmonth
say: REED-munth
kind: word
meaning: month 4
```

```canon
id: TERM-0193
type: term
canon: draft
term: Highsun
say: HY-sun
kind: word
meaning: month 5
```

```canon
id: TERM-0194
type: term
canon: draft
term: Saltdry
say: SALT-dry
kind: word
meaning: month 6
```

```canon
id: TERM-0195
type: term
canon: draft
term: Ember
say: EM-ber
kind: word
meaning: month 7 (season: the Ember)
```

```canon
id: TERM-0196
type: term
canon: draft
term: Fallow
say: FAL-oh
kind: word
meaning: month 8
```

```canon
id: TERM-0197
type: term
canon: draft
term: Mistcall
say: MIST-kawl
kind: word
meaning: month 9
```

```canon
id: TERM-0198
type: term
canon: draft
term: Longdark
say: LONG-dark
kind: word
meaning: month 10
```

```canon
id: TERM-0199
type: term
canon: draft
term: Still
say: STIL
kind: word
meaning: the 5 Still Days (month 11)
```

```canon
id: TERM-0200
type: term
canon: draft
term: Humday
say: HUM-day
kind: word
meaning: weekday 1
```

```canon
id: TERM-0201
type: term
canon: draft
term: Reedday
say: REED-day
kind: word
meaning: weekday 2
```

```canon
id: TERM-0202
type: term
canon: draft
term: Bellday
say: BEL-day
kind: word
meaning: weekday 3
```

```canon
id: TERM-0203
type: term
canon: draft
term: Drumday
say: DRUM-day
kind: word
meaning: weekday 4
```

```canon
id: TERM-0204
type: term
canon: draft
term: Hornday
say: HORN-day
kind: word
meaning: weekday 5
```

```canon
id: TERM-0205
type: term
canon: draft
term: Restday
say: REST-day
kind: word
meaning: weekday 6
```

```canon
id: TERM-0206
type: term
canon: draft
term: the Wet
say: thuh WET
kind: word
meaning: season: Firstwater-Silting
```

```canon
id: TERM-0207
type: term
canon: draft
term: the Green
say: thuh GREEN
kind: word
meaning: season: Reedmonth-Saltdry
```

```canon
id: TERM-0208
type: term
canon: draft
term: the Mist
say: thuh MIST
kind: word
meaning: season: Mistcall-Longdark
```

```canon
id: TERM-0209
type: term
canon: draft
term: Calm is bought.
say: KAHLM iz BAWT
kind: phrase
meaning: Quell words; recurring line
```

```canon
id: TERM-0210
type: term
canon: draft
term: Who pays for the dry?
say: hoo PAYZ for thuh DRY
kind: phrase
meaning: recurring line
```

```canon
id: TERM-0211
type: term
canon: draft
term: ...and the water kept its counsel.
say: and thuh WAW-ter KEPT its KOWN-sel
kind: phrase
meaning: the Chronicler's sign-off (changes only in S12E13)
```

---

## v0.3 additions (draft)

Status: **draft** (respellings proposed by writer-houses and writer-characters, normalised by the keeper; stressed syllable in CAPS; to be tested with the TTS voice). Names of older heads without a character ID are entries without `ref`; `meaning` says who they were. Name clashes against the 3-letter rule: DEC-57.

### People (v0.3)

```canon
id: TERM-0214
type: term
canon: approved
term: Sedge
say: SEJ
kind: person
ref: CH-0077
```

```canon
id: TERM-0215
type: term
canon: approved
term: Tolvar Corvane
say: TOLL-var kor-VAYN
kind: person
ref: CH-0203
```

```canon
id: TERM-0216
type: term
canon: approved
term: Stellan Corvane
say: STEL-un kor-VAYN
kind: person
ref: CH-0200
```

```canon
id: TERM-0217
type: term
canon: approved
term: Wenna Corvane
say: WEN-uh kor-VAYN
kind: person
ref: CH-0201
```

```canon
id: TERM-0218
type: term
canon: approved
term: Alys Corvane
say: AL-iss kor-VAYN
kind: person
ref: CH-0202
```

```canon
id: TERM-0219
type: term
canon: approved
term: Hemmet Dask
say: HEM-it DASK
kind: person
ref: CH-0216
```

```canon
id: TERM-0220
type: term
canon: approved
term: Bertil Dask
say: BUR-til DASK
kind: person
ref: CH-0210
```

```canon
id: TERM-0221
type: term
canon: approved
term: Rosamund Dask
say: ROZ-uh-mund DASK
kind: person
ref: CH-0217
```

```canon
id: TERM-0222
type: term
canon: approved
term: Agathe Dask
say: AG-aht DASK
kind: person
ref: CH-0211
```

```canon
id: TERM-0223
type: term
canon: approved
term: Edrin Dask
say: ED-rin DASK
kind: person
ref: CH-0212
```

```canon
id: TERM-0224
type: term
canon: approved
term: Hilde Dask
say: HIL-duh DASK
kind: person
ref: CH-0213
```

```canon
id: TERM-0225
type: term
canon: approved
term: Thyra Dask
say: THY-ruh DASK
kind: person
ref: CH-0214
```

```canon
id: TERM-0226
type: term
canon: approved
term: Ylva Dask
say: ILL-vuh DASK
kind: person
ref: CH-0215
```

```canon
id: TERM-0227
type: term
canon: approved
term: Emeric Ilvane
say: EM-er-ick IL-vayn
kind: person
ref: CH-0220
```

```canon
id: TERM-0228
type: term
canon: approved
term: Tamlyn Pallis
say: TAM-lin PAL-iss
kind: person
ref: CH-0221
```

```canon
id: TERM-0229
type: term
canon: approved
term: Imre Pallis
say: IM-ray PAL-iss
kind: person
ref: CH-0222
```

```canon
id: TERM-0230
type: term
canon: approved
term: Borra Rusk
say: BOR-uh RUSK
kind: person
ref: CH-0236
```

```canon
id: TERM-0231
type: term
canon: approved
term: Bodvar Rusk
say: BOD-var RUSK
kind: person
ref: CH-0230
```

```canon
id: TERM-0232
type: term
canon: approved
term: Gisla Rusk
say: GEES-luh RUSK
kind: person
ref: CH-0237
```

```canon
id: TERM-0233
type: term
canon: approved
term: Wilmot Rusk
say: WIL-mot RUSK
kind: person
ref: CH-0231
```

```canon
id: TERM-0234
type: term
canon: approved
term: Eirik Rusk
say: AY-rik RUSK
kind: person
ref: CH-0232
```

```canon
id: TERM-0235
type: term
canon: approved
term: Ardo Rusk
say: AR-doh RUSK
kind: person
ref: CH-0233
```

```canon
id: TERM-0236
type: term
canon: approved
term: Dagny Rusk
say: DAG-nee RUSK
kind: person
ref: CH-0234
```

```canon
id: TERM-0237
type: term
canon: approved
term: Sindre Rusk
say: SIN-dreh RUSK
kind: person
ref: CH-0235
```

```canon
id: TERM-0238
type: term
canon: approved
term: Reske Quell
say: RESK-eh KWEL
kind: person
ref: CH-0243
```

```canon
id: TERM-0239
type: term
canon: approved
term: Rourke Quell
say: RORK KWEL
kind: person
ref: CH-0240
```

```canon
id: TERM-0240
type: term
canon: approved
term: Jessamy of Rhee
say: JESS-uh-mee uv REE
kind: person
ref: CH-0241
```

```canon
id: TERM-0241
type: term
canon: approved
term: Jinna Quell
say: JIN-uh KWEL
kind: person
ref: CH-0242
```

```canon
id: TERM-0242
type: term
canon: approved
term: Barnet Fennick
say: BAR-nit FEN-ik
kind: person
ref: CH-0250
```

```canon
id: TERM-0243
type: term
canon: approved
term: Sefton Fennick
say: SEF-tun FEN-ik
kind: person
ref: CH-0251
```

```canon
id: TERM-0244
type: term
canon: approved
term: Maud Fennick
say: MAWD FEN-ik
kind: person
ref: CH-0253
```

```canon
id: TERM-0245
type: term
canon: approved
term: Yolande Fennick
say: yoh-LAND FEN-ik
kind: person
ref: CH-0252
```

```canon
id: TERM-0246
type: term
canon: approved
term: Hendrik Lantry
say: HEN-drik LAN-tree
kind: person
ref: CH-0260
```

```canon
id: TERM-0247
type: term
canon: approved
term: Mattias Lantry
say: mah-TEE-us LAN-tree
kind: person
ref: CH-0261
```

```canon
id: TERM-0248
type: term
canon: approved
term: Bastian Lantry
say: BAST-ee-un LAN-tree
kind: person
ref: CH-0262
```

```canon
id: TERM-0249
type: term
canon: approved
term: Annick Lantry
say: AN-ick LAN-tree
kind: person
ref: CH-0263
```

```canon
id: TERM-0250
type: term
canon: approved
term: Rainer Lantry
say: RY-ner LAN-tree
kind: person
ref: CH-0264
```

```canon
id: TERM-0251
type: term
canon: approved
term: Elske Lantry
say: ELS-keh LAN-tree
kind: person
ref: CH-0265
```

```canon
id: TERM-0252
type: term
canon: approved
term: Aldous Harrow
say: AWL-dus HARR-oh
kind: person
ref: CH-0271
```

```canon
id: TERM-0253
type: term
canon: approved
term: Osbert Harrow
say: OZ-bert HARR-oh
kind: person
ref: CH-0270
```

```canon
id: TERM-0254
type: term
canon: approved
term: Rawlin Moll
say: RAW-lin MOL
kind: person
ref: CH-0275
```

```canon
id: TERM-0255
type: term
canon: approved
term: Thessa Moll
say: THESS-uh MOL
kind: person
ref: CH-0276
```

```canon
id: TERM-0256
type: term
canon: approved
term: Weylin Ostry
say: WAY-lin OSS-tree
kind: person
ref: CH-0278
```

```canon
id: TERM-0257
type: term
canon: approved
term: Elowen Ostry
say: EL-oh-wen OSS-tree
kind: person
ref: CH-0279
```

```canon
id: TERM-0258
type: term
canon: approved
term: the last Lady of Vanth
say: thuh LAST LAY-dee uv VANTH
kind: person
ref: CH-0280
```

```canon
id: TERM-0259
type: term
canon: approved
term: Taleh Ashare
say: TAH-leh ah-SHAH-reh
kind: person
ref: CH-0285
```

```canon
id: TERM-0260
type: term
canon: approved
term: Ulenne Ashare
say: oo-LEN ah-SHAH-reh
kind: person
ref: CH-0286
```

```canon
id: TERM-0261
type: term
canon: approved
term: Wystan Corvane
say: WISS-tun kor-VAYN
kind: person
ref: CH-0204
```

```canon
id: TERM-0262
type: term
canon: approved
term: Gant
say: GANT
kind: person
ref: CH-0073
```

```canon
id: TERM-0263
type: term
canon: approved
term: Tuck
say: TUK
kind: person
ref: CH-0074
```

```canon
id: TERM-0264
type: term
canon: approved
term: Ansel Fray
say: AN-sel FRAY
kind: person
ref: CH-0075
```

```canon
id: TERM-0265
type: term
canon: approved
term: Orm Hask
say: ORM HASK
kind: person
ref: CH-0076
```

```canon
id: TERM-0266
type: term
canon: approved
term: Dakka Den
say: DAK-ah DEN
kind: person
ref: CH-0071
```

```canon
id: TERM-0267
type: term
canon: approved
term: Itsek
say: IT-sek
kind: person
ref: CH-0072
```

```canon
id: TERM-0268
type: term
canon: approved
term: Brannic Corvane
say: BRAN-ick kor-VAYN
kind: person
meaning: head of House Corvane CY 19-44; the Salt War
```

```canon
id: TERM-0269
type: term
canon: approved
term: Edda Corvane
say: ED-uh kor-VAYN
kind: person
meaning: Lady Admiral CY 44-71; the Long Mole
```

```canon
id: TERM-0270
type: term
canon: approved
term: Galen Corvane
say: GAY-len kor-VAYN
kind: person
meaning: head CY 71-102; Helm CY 80-102
```

```canon
id: TERM-0271
type: term
canon: approved
term: Rendal Corvane
say: REN-dul kor-VAYN
kind: person
meaning: head CY 131-160, "the first of both bloods"
```

```canon
id: TERM-0272
type: term
canon: approved
term: Saffen Corvane
say: SAF-en kor-VAYN
kind: person
meaning: head CY 160-188
```

```canon
id: TERM-0273
type: term
canon: approved
term: Hallam Corvane
say: HAL-um kor-VAYN
kind: person
meaning: head CY 188-221; Helm CY 198-221
```

```canon
id: TERM-0274
type: term
canon: approved
term: Idwal Corvane
say: ID-wahl kor-VAYN
kind: person
meaning: head CY 221-247
```

```canon
id: TERM-0275
type: term
canon: approved
term: Oswin Corvane
say: OZ-win kor-VAYN
kind: person
meaning: head CY 247-266
```

```canon
id: TERM-0276
type: term
canon: approved
term: Orla Corvane
say: OR-luh kor-VAYN
kind: person
meaning: First Cantor CY 252-281
```

```canon
id: TERM-0277
type: term
canon: approved
term: Ulric Dask
say: UL-rick DASK
kind: person
meaning: head CY 24-58; Helm CY 39-58
```

```canon
id: TERM-0278
type: term
canon: approved
term: Wardel Dask
say: WAR-dul DASK
kind: person
meaning: head CY 58-93; the Furrow War
```

```canon
id: TERM-0279
type: term
canon: approved
term: Grimald Dask
say: GRIM-ald DASK
kind: person
meaning: head CY 93-126; Helm CY 102-126
```

```canon
id: TERM-0280
type: term
canon: approved
term: Ebbard Dask
say: EB-ard DASK
kind: person
meaning: head CY 126-171; Helm CY 149-171
```

```canon
id: TERM-0281
type: term
canon: approved
term: Wulfric Dask
say: WOOLF-rick DASK
kind: person
meaning: head CY 171-199
```

```canon
id: TERM-0282
type: term
canon: approved
term: Osric Dask
say: OZ-rick DASK
kind: person
meaning: head CY 199-228
```

```canon
id: TERM-0283
type: term
canon: approved
term: Stannic Dask
say: STAN-ick DASK
kind: person
meaning: head CY 228-262
```

```canon
id: TERM-0284
type: term
canon: approved
term: Idony Dask
say: ID-oh-nee DASK
kind: person
meaning: First Cantor CY 192-221
```

```canon
id: TERM-0285
type: term
canon: approved
term: Avel Ilvane
say: AV-el IL-vayn
kind: person
meaning: head CY 9-39; Helm CY 17-39
```

```canon
id: TERM-0286
type: term
canon: approved
term: Cassen Ilvane
say: KASS-en IL-vayn
kind: person
meaning: head CY 39-70
```

```canon
id: TERM-0287
type: term
canon: approved
term: Mireth Ilvane
say: MEER-eth IL-vayn
kind: person
meaning: head CY 70-101
```

```canon
id: TERM-0288
type: term
canon: approved
term: Selwyn Ilvane
say: SEL-win IL-vayn
kind: person
meaning: head CY 101-118
```

```canon
id: TERM-0289
type: term
canon: approved
term: Evander Ilvane
say: ee-VAN-der IL-vayn
kind: person
meaning: head CY 118-149; Helm CY 126-149
```

```canon
id: TERM-0290
type: term
canon: approved
term: Linnet Ilvane
say: LIN-it IL-vayn
kind: person
meaning: head CY 149-180
```

```canon
id: TERM-0291
type: term
canon: approved
term: Cyrel Ilvane
say: SEER-el IL-vayn
kind: person
meaning: head CY 180-214
```

```canon
id: TERM-0292
type: term
canon: approved
term: Belisse Ilvane
say: beh-LEESS IL-vayn
kind: person
meaning: head CY 214-240
```

```canon
id: TERM-0293
type: term
canon: approved
term: Tavian Ilvane
say: TAY-vee-un IL-vayn
kind: person
meaning: head CY 240-268; Helm CY 249-268
```

```canon
id: TERM-0294
type: term
canon: approved
term: Sorrel Ilvane
say: SOR-ul IL-vayn
kind: person
meaning: First Cantor CY 14-43
```

```canon
id: TERM-0295
type: term
canon: approved
term: Saskia Ilvane
say: SASS-kee-uh IL-vayn
kind: person
meaning: First Cantor CY 70-98
```

```canon
id: TERM-0296
type: term
canon: approved
term: Ommen Ilvane
say: OM-en IL-vayn
kind: person
meaning: First Cantor CY 98-131
```

```canon
id: TERM-0297
type: term
canon: approved
term: Pryor Ilvane
say: PRY-er IL-vayn
kind: person
meaning: First Cantor CY 131-160 (renamed from Quiller, DEC-57)
```

```canon
id: TERM-0298
type: term
canon: approved
term: Beryl Ilvane
say: BEH-ril IL-vayn
kind: person
meaning: First Cantor CY 160-192
```

```canon
id: TERM-0299
type: term
canon: approved
term: Nolwen Ilvane
say: NOLL-wen IL-vayn
kind: person
meaning: First Cantor CY 221-252
```

```canon
id: TERM-0300
type: term
canon: approved
term: Torsk Rusk
say: TORSK RUSK
kind: person
meaning: head CY 26-60
```

```canon
id: TERM-0301
type: term
canon: approved
term: Ulla Rusk
say: OOL-uh RUSK
kind: person
meaning: head CY 60-98
```

```canon
id: TERM-0302
type: term
canon: approved
term: Brodric Rusk
say: BROD-rick RUSK
kind: person
meaning: head CY 98-129
```

```canon
id: TERM-0303
type: term
canon: approved
term: Vorn Rusk
say: VORN RUSK
kind: person
meaning: head CY 129-163; stormed the Stair CY 141
```

```canon
id: TERM-0304
type: term
canon: approved
term: Ragna Rusk
say: RAG-nuh RUSK
kind: person
meaning: head CY 163-190
```

```canon
id: TERM-0305
type: term
canon: approved
term: Drust Rusk
say: DRUST RUSK
kind: person
meaning: head CY 190-216; the Kite War
```

```canon
id: TERM-0306
type: term
canon: approved
term: Inga Rusk
say: ING-uh RUSK
kind: person
meaning: head CY 216-244
```

```canon
id: TERM-0307
type: term
canon: approved
term: Jettan Quell
say: JET-un KWEL
kind: person
meaning: Captain-Lord CY 12-33 (Jutt)
```

```canon
id: TERM-0308
type: term
canon: approved
term: Skarn Quell
say: SKARN KWEL
kind: person
meaning: Captain-Lord CY 33-41 (Skarra)
```

```canon
id: TERM-0309
type: term
canon: approved
term: Raddock Quell
say: RAD-uck KWEL
kind: person
meaning: Captain-Lord CY 41-70 (Tarrow)
```

```canon
id: TERM-0310
type: term
canon: approved
term: Jusso Quell
say: JOO-soh KWEL
kind: person
meaning: Captain-Lord CY 70-96 (Tarrow)
```

```canon
id: TERM-0311
type: term
canon: approved
term: Rilla Quell
say: RIL-uh KWEL
kind: person
meaning: Captain-Lord CY 96-130 (Jutt)
```

```canon
id: TERM-0312
type: term
canon: approved
term: Murro Quell
say: MUR-oh KWEL
kind: person
meaning: Captain-Lord CY 130-155 (Tarrow)
```

```canon
id: TERM-0313
type: term
canon: approved
term: Jolle Quell
say: JOL-eh KWEL
kind: person
meaning: Captain-Lord CY 155-198; "the Pirate Helm" CY 171-198
```

```canon
id: TERM-0314
type: term
canon: approved
term: Jenner Quell
say: JEN-er KWEL
kind: person
meaning: Captain-Lord CY 198-230 (Skarra)
```

```canon
id: TERM-0315
type: term
canon: approved
term: Jassa Quell
say: JASS-uh KWEL
kind: person
meaning: Captain-Lord CY 230-259 (Jutt)
```

```canon
id: TERM-0316
type: term
canon: approved
term: Ivo Fennick
say: EE-voh FEN-ik
kind: person
meaning: first Relay-Master CY 9-40
```

```canon
id: TERM-0317
type: term
canon: approved
term: Percival Fennick
say: PUR-sih-vul FEN-ik
kind: person
meaning: Relay-Master CY 40-77
```

```canon
id: TERM-0318
type: term
canon: approved
term: Gideon Fennick
say: GID-ee-un FEN-ik
kind: person
meaning: Relay-Master CY 77-110
```

```canon
id: TERM-0319
type: term
canon: approved
term: Clement Fennick
say: KLEM-ent FEN-ik
kind: person
meaning: Relay-Master CY 110-150
```

```canon
id: TERM-0320
type: term
canon: approved
term: Hamon Fennick
say: HAY-mun FEN-ik
kind: person
meaning: Relay-Master CY 150-189; Master of the Hearings
```

```canon
id: TERM-0321
type: term
canon: approved
term: Rafe Fennick
say: RAYF FEN-ik
kind: person
meaning: head CY 189-221
```

```canon
id: TERM-0322
type: term
canon: approved
term: Nyle Fennick
say: NILE FEN-ik
kind: person
meaning: head CY 221-240
```

```canon
id: TERM-0323
type: term
canon: approved
term: Thurstan Harrow
say: THUR-stun HARR-oh
kind: person
meaning: head CY 17-52
```

```canon
id: TERM-0324
type: term
canon: approved
term: Lambert Harrow
say: LAM-bert HARR-oh
kind: person
meaning: head CY 52-80; Helm CY 58-80
```

```canon
id: TERM-0325
type: term
canon: approved
term: Baldwin Harrow
say: BAWLD-win HARR-oh
kind: person
meaning: head CY 80-118
```

```canon
id: TERM-0326
type: term
canon: approved
term: Hugo Harrow
say: HYOO-goh HARR-oh
kind: person
meaning: head CY 118-150
```

```canon
id: TERM-0327
type: term
canon: approved
term: Crispin Harrow
say: KRIS-pin HARR-oh
kind: person
meaning: head CY 150-183 (renamed from Anselm, DEC-57)
```

```canon
id: TERM-0328
type: term
canon: approved
term: Jocelyn Harrow
say: JOSS-lin HARR-oh
kind: person
meaning: head CY 183-209
```

```canon
id: TERM-0329
type: term
canon: approved
term: Tancred Harrow
say: TAN-kred HARR-oh
kind: person
meaning: head CY 209-249; Helm CY 221-249; the Paper Ordinance
```

```canon
id: TERM-0330
type: term
canon: approved
term: Tobin Moll
say: TOH-bin MOL
kind: person
meaning: head ~OS 690-CY 30 (renamed from Ancel, DEC-57)
```

```canon
id: TERM-0331
type: term
canon: approved
term: Yorath Moll
say: YOR-ath MOL
kind: person
meaning: head CY 30-61
```

```canon
id: TERM-0332
type: term
canon: approved
term: Kenver Ostry
say: KEN-ver OSS-tree
kind: person
meaning: head ~OS 695-CY 31
```

```canon
id: TERM-0333
type: term
canon: approved
term: Gwilym Ostry
say: GWIL-im OSS-tree
kind: person
meaning: head CY 31-70
```

```canon
id: TERM-0334
type: term
canon: approved
term: Callis Ostry
say: KAL-iss OSS-tree
kind: person
meaning: head CY 70-112
```

```canon
id: TERM-0335
type: term
canon: approved
term: Gethin Vanth
say: GETH-in VANTH
kind: person
meaning: head ~OS 690-CY 28
```

```canon
id: TERM-0336
type: term
canon: approved
term: Hywel Vanth
say: HUH-wel VANTH
kind: person
meaning: head CY 28-66
```

```canon
id: TERM-0337
type: term
canon: approved
term: Ithel Vanth
say: ITH-el VANTH
kind: person
meaning: head CY 66-104
```

```canon
id: TERM-0338
type: term
canon: approved
term: Tegwen Vanth
say: TEG-wen VANTH
kind: person
meaning: head CY 104-136
```

```canon
id: TERM-0339
type: term
canon: approved
term: Aleneh Ashare
say: ah-LEN-eh ah-SHAH-reh
kind: person
meaning: Tide-Queen OS 431-468
```

```canon
id: TERM-0340
type: term
canon: approved
term: Ravenne Ashare
say: rah-VEN ah-SHAH-reh
kind: person
meaning: Tide-Queen OS 468-505
```

```canon
id: TERM-0341
type: term
canon: approved
term: Obeh Ashare
say: OH-beh ah-SHAH-reh
kind: person
meaning: Tide-King OS 505-533
```

```canon
id: TERM-0342
type: term
canon: approved
term: Rinneh Ashare
say: RIN-eh ah-SHAH-reh
kind: person
meaning: Tide-Queen OS 533-571
```

```canon
id: TERM-0343
type: term
canon: approved
term: Yareh Ashare
say: YAR-eh ah-SHAH-reh
kind: person
meaning: Tide-King OS 571-600
```

```canon
id: TERM-0344
type: term
canon: approved
term: Thandry of Brackwater
say: THAN-dree uv BRAK-waw-ter
kind: person
meaning: First Cantor CY 43-70, the last wreck-singer to rise in the Choir
```

```canon
id: TERM-0345
type: term
canon: approved
term: Ekida
say: eh-KEE-dah
kind: person
meaning: Dry Queen CY 138-143
```

```canon
id: TERM-0346
type: term
canon: approved
term: Sotka
say: SOT-kah
kind: person
meaning: Dry Queen CY 202-207 (the Kite War)
```

```canon
id: TERM-0347
type: term
canon: approved
term: Akko of Kitsa
say: AH-koh uv KIT-sah
kind: person
meaning: Kitsa glider-captain, Tsura's companion, killed in the Rim Skirmish (CY 309)
ref: CH-0078
```

### Houses, clans and powers (v0.3)

```canon
id: TERM-0348
type: term
canon: approved
term: House Dunmore
say: HOWSS DUN-mor
kind: house
ref: HS-013
```

```canon
id: TERM-0349
type: term
canon: approved
term: House Cobbet
say: HOWSS KOB-it
kind: house
ref: HS-014
```

```canon
id: TERM-0350
type: term
canon: approved
term: House Inchley
say: HOWSS INCH-lee
kind: house
ref: HS-015
```

```canon
id: TERM-0351
type: term
canon: approved
term: House Merriden
say: HOWSS MEH-rih-den
kind: house
ref: HS-016
```

```canon
id: TERM-0352
type: term
canon: approved
term: House Kellow
say: HOWSS KEL-oh
kind: house
ref: HS-017
```

```canon
id: TERM-0353
type: term
canon: approved
term: House Dask of the Reach
say: HOWSS DASK uv thuh REECH
kind: house
ref: HS-018
```

```canon
id: TERM-0354
type: term
canon: approved
term: House Gillam
say: HOWSS GIL-um
kind: house
ref: HS-019
```

```canon
id: TERM-0355
type: term
canon: approved
term: Clan Rhee
say: KLAN REE
kind: house
ref: HS-020
```

```canon
id: TERM-0356
type: term
canon: approved
term: Clan Jutt
say: KLAN JUT
kind: house
ref: HS-021
```

```canon
id: TERM-0357
type: term
canon: approved
term: Clan Skarra
say: KLAN SKAR-uh
kind: house
ref: HS-022
```

```canon
id: TERM-0358
type: term
canon: approved
term: Clan Tarrow
say: KLAN TAR-oh
kind: house
ref: HS-023
```

```canon
id: TERM-0359
type: term
canon: approved
term: Clan Varra
say: KLAN VAR-uh
kind: house
ref: HS-024
```

```canon
id: TERM-0360
type: term
canon: approved
term: House Hadden
say: HOWSS HAD-en
kind: house
ref: HS-025
```

```canon
id: TERM-0361
type: term
canon: approved
term: House Grell
say: HOWSS GREL
kind: house
ref: HS-026
```

```canon
id: TERM-0362
type: term
canon: approved
term: House Corvane of the Roads
say: HOWSS kor-VAYN uv thuh ROHDZ
kind: house
ref: HS-027
```

```canon
id: TERM-0363
type: term
canon: approved
term: House Whitlow
say: HOWSS WIT-loh
kind: house
ref: HS-028
```

```canon
id: TERM-0364
type: term
canon: approved
term: House Pallis
say: HOWSS PAL-iss
kind: house
ref: HS-029
```

```canon
id: TERM-0365
type: term
canon: approved
term: House Tennant
say: HOWSS TEN-unt
kind: house
ref: HS-030
```

```canon
id: TERM-0366
type: term
canon: approved
term: House Orsley
say: HOWSS ORZ-lee
kind: house
ref: HS-031
```

```canon
id: TERM-0367
type: term
canon: approved
term: House Kilbride
say: HOWSS kil-BRIDE
kind: house
ref: HS-032
```

```canon
id: TERM-0368
type: term
canon: approved
term: House Wray
say: HOWSS RAY
kind: house
ref: HS-033
```

```canon
id: TERM-0369
type: term
canon: approved
term: Clan Den
say: KLAN DEN
kind: house
meaning: Ossari clan of the Rim; kite-masters (Tsura, Dakka)
```

```canon
id: TERM-0370
type: term
canon: approved
term: Clan Tekka
say: KLAN TEK-ah
kind: house
meaning: Ossari clan of the nitre country; saltpeter (Itsek)
```

```canon
id: TERM-0371
type: term
canon: approved
term: Clan Kitsa
say: KLAN KIT-sah
kind: house
meaning: Ossari clan of the high mesas; gliders
```

```canon
id: TERM-0372
type: term
canon: approved
term: Clan Udra
say: KLAN OO-drah
kind: house
meaning: Ossari well-keepers and knot-reckoners
```

```canon
id: TERM-0373
type: term
canon: approved
term: Clan Saktu
say: KLAN SAHK-too
kind: house
meaning: Ossari herders of the southern plateau
```

```canon
id: TERM-0374
type: term
canon: approved
term: Clan Edakka
say: KLAN eh-DAH-kah
kind: house
meaning: Ossari lake-fishers of the Shelf lakes; took in Vanth survivors (Kadu)
```

### Places (v0.3)

```canon
id: TERM-0375
type: term
canon: approved
term: the Rim
say: thuh RIM
kind: place
ref: PL-0070
```

```canon
id: TERM-0376
type: term
canon: approved
term: the Table House
say: thuh TAY-bul howss
kind: place
ref: PL-0071
```

```canon
id: TERM-0377
type: term
canon: approved
term: Rimgate
say: RIM-gayt
kind: place
ref: PL-0072
```

```canon
id: TERM-0378
type: term
canon: approved
term: the Goat Stair
say: thuh GOHT STAIR
kind: place
ref: PL-0073
```

```canon
id: TERM-0379
type: term
canon: approved
term: the Brackwater salt pans
say: thuh BRAK-waw-ter SALT panz
kind: place
ref: PL-0074
```

```canon
id: TERM-0380
type: term
canon: approved
term: the Long Mole
say: thuh LONG MOHL
kind: place
ref: PL-0075
```

```canon
id: TERM-0381
type: term
canon: approved
term: the Concord Arsenal
say: thuh KON-kord AR-sen-ul
kind: place
ref: PL-0076
```

```canon
id: TERM-0382
type: term
canon: approved
term: the Rusk House-in-Exile
say: thuh RUSK HOWSS-in-EG-zile
kind: place
ref: PL-0077
```

```canon
id: TERM-0383
type: term
canon: approved
term: the Map Office
say: thuh MAP OF-iss
kind: place
ref: PL-0078
```

```canon
id: TERM-0384
type: term
canon: approved
term: Hobb's Gate
say: HOBZ GAYT
kind: place
ref: PL-0079
```

```canon
id: TERM-0385
type: term
canon: approved
term: the Second Sluice
say: thuh SEK-und SLOOSS
kind: place
ref: PL-0080
```

```canon
id: TERM-0386
type: term
canon: approved
term: the Third Sluice
say: thuh THURD SLOOSS
kind: place
ref: PL-0081
```

```canon
id: TERM-0387
type: term
canon: approved
term: the Fourth Sluice
say: thuh FORTH SLOOSS
kind: place
ref: PL-0082
```

```canon
id: TERM-0388
type: term
canon: approved
term: the Fifth Sluice
say: thuh FIFTH SLOOSS
kind: place
ref: PL-0083
```

```canon
id: TERM-0389
type: term
canon: approved
term: the Reach
say: thuh REECH
kind: place
ref: PL-0038
meaning: local name of the Moll polders
```

### Titles, words, objects (v0.3)

```canon
id: TERM-0390
type: term
canon: approved
term: the Hill Voice
say: thuh HIL VOYSS
kind: word
ref: RULE-017
meaning: Harrow's second voice, a house's voice without a Spire; Lantry's since CY 252
```

```canon
id: TERM-0391
type: term
canon: approved
term: the Sluice Voice
say: thuh SLOOSS VOYSS
kind: word
meaning: the voice that goes with the Sluice Spire (Fennick since CY 251)
```

```canon
id: TERM-0392
type: term
canon: approved
term: the Hull Moot
say: thuh HUL MOOT
kind: word
ref: HS-005
meaning: the five Quell clan-chiefs sitting in an upturned hull; elects the Captain-Lord
```

```canon
id: TERM-0393
type: term
canon: approved
term: the Sunk Charter
say: thuh SUNK CHAR-ter
kind: object
ref: EV-0264
meaning: Quell's salvage right over Lirenne (CY 3)
```

```canon
id: TERM-0394
type: term
canon: approved
term: the Pilots' Peace
say: thuh PY-luts PEESS
kind: word
ref: EV-0267
meaning: the peace of CY 40 after the Salt War
```

```canon
id: TERM-0395
type: term
canon: approved
term: the Unison Decree
say: thee YOO-nih-sun dih-KREE
kind: word
ref: EV-0266
meaning: CY 34: all Cantors trained at Pale Crag
```

```canon
id: TERM-0396
type: term
canon: approved
term: the Exchange of Sleeves
say: thee eks-CHAYNJ uv SLEEVZ
kind: word
ref: RULE-023
meaning: the hostage custom of the Stair Treaty
```

```canon
id: TERM-0397
type: term
canon: approved
term: Sea Right
say: SEE RITE
kind: word
ref: RULE-018
meaning: Corvane house law of succession
```

```canon
id: TERM-0398
type: term
canon: approved
term: the Joining
say: thuh JOY-ning
kind: word
ref: RULE-019
meaning: Still 5: every Spire sung together at dusk
```

```canon
id: TERM-0399
type: term
canon: approved
term: the Lament for the Drowned
say: thuh luh-MENT for thuh DROWND
kind: word
ref: RULE-019
meaning: Still 4: Cantors in boats over Lirenne
```

```canon
id: TERM-0400
type: term
canon: approved
term: the Ember contracts
say: thee EM-ber KON-trakts
kind: word
ref: HS-002
meaning: Dask harvests sold forward to the bank
```

```canon
id: TERM-0401
type: term
canon: approved
term: vote-lien
say: VOHT-leen
kind: word
meaning: a Conclave voice pledged to a creditor
```

```canon
id: TERM-0402
type: term
canon: approved
term: Lirenne salvage bond
say: lih-REN SAL-vij BOND
kind: object
meaning: the S6 bond (SEC-016)
```

```canon
id: TERM-0403
type: term
canon: approved
term: the Bondholders' Council
say: thuh BOND-hohl-derz KOWN-sil
kind: word
```

```canon
id: TERM-0404
type: term
canon: approved
term: storm-berth
say: STORM-burth
kind: word
ref: PL-0075
meaning: a berth inside the Long Mole sold in storms
```

```canon
id: TERM-0405
type: term
canon: approved
term: calm-fee
say: KAHM-fee
kind: word
ref: HS-005
meaning: the toll to be sung through the Storm Spire's water
```

```canon
id: TERM-0406
type: term
canon: approved
term: priority song
say: pry-OR-ih-tee SONG
kind: word
ref: HS-090
meaning: a bought promise to be sung first
```

```canon
id: TERM-0407
type: term
canon: approved
term: first-tone
say: FURST-tohn
kind: word
ref: HS-006
meaning: relay messages an hour before the public
```

```canon
id: TERM-0408
type: term
canon: approved
term: speed fee
say: SPEED fee
kind: word
meaning: a bribe-fee to the Hearings
```

```canon
id: TERM-0409
type: term
canon: approved
term: gate book
say: GAYT book
kind: object
ref: HS-026
meaning: the quartermasters' honest ledger
```

```canon
id: TERM-0410
type: term
canon: approved
term: cliff book
say: KLIF book
kind: object
ref: HS-026
meaning: the quartermasters' real ledger
```

```canon
id: TERM-0411
type: term
canon: approved
term: the Book of Mouths
say: thuh BOOK uv MOWTHZ
kind: object
ref: HS-002
meaning: Dask's ledger of everyone who ate Dask grain on credit
```

```canon
id: TERM-0412
type: term
canon: approved
term: the Ash Roll
say: thee ASH ROHL
kind: object
ref: HS-029
meaning: the stewards' true roll of gleaned children
```

```canon
id: TERM-0413
type: term
canon: approved
term: the Book of the Blood
say: thuh BOOK uv thuh BLUD
kind: object
ref: HS-003
meaning: the Pale Crag register of Ilvane-born
```

```canon
id: TERM-0414
type: term
canon: approved
term: the Grey Hares
say: thuh GRAY HAIRZ
kind: word
ref: HS-006
meaning: Odo's household guard
```

```canon
id: TERM-0415
type: term
canon: approved
term: the White Staves
say: thuh WITE STAYVZ
kind: word
ref: HS-003
meaning: the Pale Crag cloister guard
```

```canon
id: TERM-0416
type: term
canon: approved
term: the Grey Ninth
say: thuh GRAY NYNTH
kind: word
meaning: free company of Rusk deserters
```

```canon
id: TERM-0417
type: term
canon: approved
term: the Salt Oars
say: thuh SALT ORZ
kind: word
meaning: mercenary galley fleet of the outer isles
```

```canon
id: TERM-0418
type: term
canon: approved
term: the red knot
say: thuh RED NOT
kind: word
ref: RULE-022
meaning: the mark on an Ossari well-cord
```

```canon
id: TERM-0419
type: term
canon: approved
term: kite-word
say: KITE-wurd
kind: word
ref: HS-091
meaning: the simplest set of kite signals
```

```canon
id: TERM-0420
type: term
canon: approved
term: the Sky Road
say: thuh SKY ROHD
kind: word
ref: HS-091
meaning: Ossari belief: the wind carries the names of the dead
```

```canon
id: TERM-0421
type: term
canon: approved
term: the Furrow War
say: thuh FUR-oh WOR
kind: word
ref: EV-0250
```

```canon
id: TERM-0422
type: term
canon: approved
term: the Broken Dike
say: thuh BROH-ken DYKE
kind: word
ref: SEC-034
```

```canon
id: TERM-0423
type: term
canon: approved
term: the Salt War
say: thuh SALT WOR
kind: word
ref: EV-0267
```

```canon
id: TERM-0424
type: term
canon: approved
term: the Kite War
say: thuh KITE WOR
kind: word
ref: EV-0270
```

```canon
id: TERM-0425
type: term
canon: approved
term: the Grey Cough
say: thuh GRAY KOF
kind: word
ref: EV-0274
```

```canon
id: TERM-0426
type: term
canon: approved
term: the Paper Ordinance
say: thuh PAY-per OR-dih-nunss
kind: word
ref: EV-0271
```

```canon
id: TERM-0427
type: term
canon: approved
term: the Clerks' Ordinance
say: thuh KLARKS OR-dih-nunss
kind: word
ref: EV-0269
```

```canon
id: TERM-0428
type: term
canon: approved
term: the Stair Treaty
say: thuh STAIR TREE-tee
kind: word
ref: EV-0268
```

```canon
id: TERM-0429
type: term
canon: approved
term: the Exchange Panic
say: thee eks-CHAYNJ PAN-ik
kind: word
ref: EV-0272
```

```canon
id: TERM-0430
type: term
canon: approved
term: the Rim Skirmish
say: thuh RIM SKUR-mish
kind: word
ref: EV-0273
```

```canon
id: TERM-0431
type: term
canon: approved
term: the salt tongue
say: thuh SALT TUNG
kind: word
meaning: the sea pushing up a low river (CY 314)
```

```canon
id: TERM-0432
type: term
canon: approved
term: the Table
say: thuh TAY-bul
kind: word
ref: HS-007
meaning: the partners of the Counting House
```

```canon
id: TERM-0433
type: term
canon: approved
term: Master of the Count
say: MAS-ter uv thuh KOWNT
kind: title
ref: HS-007
meaning: head of Lantry, elected by the Table
```

```canon
id: TERM-0434
type: term
canon: approved
term: Relay-Master
say: REE-lay MAS-ter
kind: title
ref: HS-006
```

```canon
id: TERM-0435
type: term
canon: approved
term: Relay-Warden
say: REE-lay WOR-den
kind: title
ref: HS-030
```

```canon
id: TERM-0436
type: term
canon: approved
term: Captain-Quartermaster
say: KAP-tin KWOR-ter-mas-ter
kind: title
ref: HS-026
```

```canon
id: TERM-0437
type: term
canon: approved
term: Lord of the Hall
say: LORD uv thuh HAWL
kind: title
ref: HS-003
meaning: secular head of Ilvane
```

```canon
id: TERM-0438
type: term
canon: approved
term: Dikeriders
say: DYKE-ry-derz
kind: word
ref: HS-002
meaning: polder knights
```

```canon
id: TERM-0439
type: term
canon: approved
term: voice-bearer
say: VOYSS-bair-er
kind: title
ref: RULE-015
```

```canon
id: TERM-0440
type: term
canon: approved
term: Challenge of the Voice
say: CHAL-inj uv thuh VOYSS
kind: word
ref: RULE-016
```

```canon
id: TERM-0441
type: term
canon: approved
term: Challenge of Precedence
say: CHAL-inj uv PRESS-ih-dunss
kind: word
ref: RULE-016
```

```canon
id: TERM-0442
type: term
canon: approved
term: Article Nine
say: AR-tih-kul NYNE
kind: word
ref: RULE-009
meaning: the Sunken Vote clause
```

```canon
id: TERM-0443
type: term
canon: approved
term: First Song
say: FURST SONG
kind: word
ref: RULE-020
```

```canon
id: TERM-0444
type: term
canon: approved
term: Second Song
say: SEK-und SONG
kind: word
ref: RULE-020
```

```canon
id: TERM-0445
type: term
canon: approved
term: Last Song
say: LAST SONG
kind: word
ref: RULE-020
```

```canon
id: TERM-0446
type: term
canon: approved
term: Let Go
say: LET GOH
kind: word
ref: RULE-020
meaning: a district not sung
```

```canon
id: TERM-0447
type: term
canon: approved
term: lift
say: LIFT
kind: word
ref: RULE-020
meaning: a bought rise to a higher tier of song
```

```canon
id: TERM-0448
type: term
canon: approved
term: the Concord stamp
say: thuh KON-kord STAMP
kind: object
ref: PL-0076
meaning: the Arsenal ring-stamp on powder barrels
```

```canon
id: TERM-0449
type: term
canon: approved
term: the Pearl Pretender
say: thuh PURL prih-TEN-der
kind: title
ref: CH-0043
```

```canon
id: TERM-0450
type: term
canon: approved
term: Gleaner's bell
say: GLEE-nerz BEL
kind: object
ref: HS-090
meaning: silver handbell rung beside a child's ear
```

```canon
id: TERM-0451
type: term
canon: approved
term: Cantor's rinse
say: KAN-torz RINSS
kind: word
ref: HS-003
meaning: the weekly silver rinse of the Crag
```

```canon
id: TERM-0452
type: term
canon: approved
term: the Remembering
say: thuh rih-MEM-ber-ing
kind: word
meaning: Still 3 lantern rite of the Lows for the Night of Still Water
```

```canon
id: TERM-0453
type: term
canon: approved
term: whistle-chain
say: WISS-ul chayn
kind: word
meaning: the Lows' roof-to-roof whistled relay
```

```canon
id: TERM-0454
type: term
canon: approved
term: silt-bread
say: SILT-bred
kind: object
```

```canon
id: TERM-0455
type: term
canon: approved
term: tide-house
say: TYD-howss
kind: word
meaning: cheap chicory house on the dike
```

### Slang of the Lows and the Mids (v0.3; writer-characters §11)

```canon
id: TERM-0456
type: term
canon: approved
term: the White Roll
say: thuh WITE ROHL
kind: object
ref: HS-029
meaning: the Choir's public roll of foundling novices
```

```canon
id: TERM-0457
type: term
canon: approved
term: the Low Ebb Fair
say: thuh LOH EB FAIR
kind: word
meaning: mudlark fair in Ember
```

```canon
id: TERM-0458
type: term
canon: approved
term: up the Steps
say: UP thuh STEPS
kind: word
meaning: out of the Lows; to safety
```

```canon
id: TERM-0459
type: term
canon: approved
term: your dryness
say: yor DRY-ness
kind: word
meaning: mocking address for anyone from the Steps
```

```canon
id: TERM-0460
type: term
canon: approved
term: the dries
say: thuh DRIZE
kind: word
meaning: the rich (also: the dry)
```

```canon
id: TERM-0461
type: term
canon: approved
term: wet note
say: WET NOHT
kind: word
meaning: a dry-note backed by land that will flood
```

```canon
id: TERM-0462
type: term
canon: approved
term: a one-dry
say: uh wun-DRY
kind: word
meaning: a one-mark note
```

```canon
id: TERM-0463
type: term
canon: approved
term: fiver
say: FY-ver
kind: word
meaning: a five-mark note
```

```canon
id: TERM-0464
type: term
canon: approved
term: copper
say: KOP-er
kind: word
meaning: small coin; 60 to a mark
```

```canon
id: TERM-0465
type: term
canon: approved
term: to walk it off
say: too WAWK it OFF
kind: word
meaning: to work off a debt on the treadmill
```

```canon
id: TERM-0466
type: term
canon: approved
term: drowned on paper
say: DROWND on PAY-per
kind: word
meaning: officially dead, alive under another name
```

```canon
id: TERM-0467
type: term
canon: approved
term: given to the ebb
say: GIV-en too thee EB
kind: word
meaning: drowned as punishment; buried at sea
```

```canon
id: TERM-0468
type: term
canon: approved
term: gone to the Lady
say: GON too thuh LAY-dee
kind: word
meaning: drowned (polite)
```

```canon
id: TERM-0469
type: term
canon: approved
term: the Lady spat you out
say: thuh LAY-dee SPAT yoo OWT
kind: word
meaning: you were lucky to survive
```

```canon
id: TERM-0470
type: term
canon: approved
term: shell-kisser
say: SHEL-kiss-er
kind: word
meaning: Steps insult for Lady Below worshippers
```

```canon
id: TERM-0471
type: term
canon: approved
term: mud-rat
say: MUD-rat
kind: word
meaning: mudlark (insult)
```

```canon
id: TERM-0472
type: term
canon: approved
term: larker
say: LAR-ker
kind: word
meaning: mudlark (affectionate)
```

```canon
id: TERM-0473
type: term
canon: approved
term: lane
say: LAYN
kind: word
meaning: a mudlark's patch of canal
```

```canon
id: TERM-0474
type: term
canon: approved
term: house noise
say: HOWSS noyz
kind: word
meaning: humming indoors (legal grey zone)
```

```canon
id: TERM-0475
type: term
canon: approved
term: there's a whistle on
say: thairz uh WISS-ul ON
kind: word
meaning: Listeners about
```

```canon
id: TERM-0476
type: term
canon: approved
term: ears
say: EERZ
kind: word
meaning: Listeners
```

```canon
id: TERM-0477
type: term
canon: approved
term: hares
say: HAIRZ
kind: word
meaning: Listeners (from the Fennick sigil)
```

```canon
id: TERM-0478
type: term
canon: approved
term: robes
say: ROHBZ
kind: word
meaning: the Choir
```

```canon
id: TERM-0479
type: term
canon: approved
term: the bell
say: thuh BEL
kind: word
meaning: the Gleaners ("the bell came down the lane")
```

```canon
id: TERM-0480
type: term
canon: approved
term: the post
say: thuh POHST
kind: word
meaning: the tide-post
```

```canon
id: TERM-0481
type: term
canon: approved
term: post-night
say: POHST-nite
kind: word
meaning: a night on the tide-post
```

```canon
id: TERM-0482
type: term
canon: approved
term: a rung
say: uh RUNG
kind: word
meaning: a flood (floors are raised one rung per flood)
```

```canon
id: TERM-0483
type: term
canon: approved
term: sandbag money
say: SAND-bag MUN-ee
kind: word
meaning: a dry-pledge
```

```canon
id: TERM-0484
type: term
canon: approved
term: mouth
say: MOWTH
kind: word
meaning: an Undertow rumour-seller
```

```canon
id: TERM-0485
type: term
canon: approved
term: dry room
say: DRY room
kind: word
meaning: a room above the flood line
```

```canon
id: TERM-0486
type: term
canon: approved
term: clip
say: KLIP
kind: word
meaning: a trusted clerk; "he's got his clip" = promoted
```

```canon
id: TERM-0487
type: term
canon: approved
term: inkfinger
say: INK-fing-er
kind: word
meaning: clerk (Lows insult)
```

```canon
id: TERM-0488
type: term
canon: approved
term: still-mouthed
say: STIL-mowthd
kind: word
meaning: silent out of fear
```

```canon
id: TERM-0489
type: term
canon: approved
term: tide-turned
say: TYD-turnd
kind: word
meaning: betrayed; a turncoat
```

```canon
id: TERM-0490
type: term
canon: approved
term: Ninther
say: NYNE-ther
kind: word
meaning: someone from the Ninth Sluice
```

```canon
id: TERM-0491
type: term
canon: approved
term: duck
say: DUK
kind: word
meaning: Lows endearment
```

```canon
id: TERM-0492
type: term
canon: approved
term: chick
say: CHIK
kind: word
meaning: Lows endearment
```

```canon
id: TERM-0493
type: term
canon: approved
term: columns!
say: KOL-umz
kind: word
meaning: clerk's oath (Hollis)
```

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
