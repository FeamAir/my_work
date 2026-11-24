"""Builds the r4 OP-anthem composition plans (87.0 s = 29 bars of 3.0 s, grid of the saga OP).
Generated in F minor (the model's habit) and shifted +1 semitone to F-sharp minor afterwards, as the master.
Melody words follow the master (intro motif) and main_theme.md §2 (hook: octave leap)."""
import json, sys
BANS = ["key change", "modulation", "F-sharp major chord", "F major chord", "Picardy third", "low drone",
        "pedal tone", "sustained sub bass", "808", "vocals", "choir", "humming", "singing", "vocal chops",
        "synth pad", "EDM", "trap hi-hats", "drum machine", "electric guitar", "riser synth"]
COMMON = ["instrumental", "heroic cinematic anime main title anthem", "F minor", "80 BPM", "4/4"]
DRUMS = ["live ensemble drums in a big wooden hall: deep short kick, fat toms, foot stamps on planks, hand claps",
         "stamps on beats 1 and 3, syncopated claps, the same groove all the way"]
SECTIONS = [
 ("Intro - the call", 12000, "a bold solo French horn calls the main motif, answered by solo cello", [
   "at 0:00 one deep drum hit and a bold solo French horn call, loud and clear, middle register",
   "the call motif: a short F, a leap up a fifth to a long C, one step up to D-flat, then down by steps B-flat, A-flat, G",
   "the solo cello answers with the same motif an octave lower, then the horn repeats it once more, higher and prouder",
   "soft open fifth in the strings underneath, no percussion after the first hit"], ["drums groove", "pad"]),
 ("Groove - the Lows", 9000, "the drum groove enters, staccato strings drive", [
   *DRUMS, "staccato low strings and harp ostinato in eighth notes grouped 3+3+2",
   "short horn stabs on the offbeats echo the call", "one sharp two-finger whistle accent on the last beat", "stubborn, alive"], ["melody"]),
 ("Theme", 24000, "the full melody in unison strings and horns, with a countermelody", [
   *DRUMS, "violins, violas and French horns in unison carry the main melody, strong and singing, middle register",
   "the melody: each phrase starts with a short note and leaps up to a long note, the leap wider each time, then falls by steps",
   "a clear countermelody in the cellos and bassoons moves against it in long notes",
   "trombones give short supporting chords", "memorable, hummable, proud"], []),
 ("Rise - the Steps", 12000, "brass fanfare answers, building to the climax", [
   *DRUMS, "trumpets and horns answer with proud rising fanfare calls",
   "harmony climbs D-flat major, E-flat major, C suspended, C major", "snare drum roll and tom fill grow louder every bar",
   "the last half bar is an all-drums fill, then one breath of silence"], []),
 ("Hook - the anthem", 12000, "the climax: full orchestra plays the main melody with an octave leap on the downbeat", [
   "the biggest moment of the piece: everything enters together on the first downbeat with a huge hit",
   "the hook melody: a short C, a leap up a full octave to a long high C, then down by steps B-flat, A-flat, G and A-flat",
   "all French horns, trumpets and trombones in unison with violins, a powerful brass section anthem, played twice",
   "violins double the melody an octave higher for brightness", "a running high-string countermelody in eighth notes",
   *DRUMS, "big ensemble drums on every downbeat, cymbal crashes", "triumphant, heroic, unforgettable"], []),
 ("Answer - cadence", 12000, "the answer phrase, brass and strings, strong cadence", [
   "the answering phrase in full brass and strings rises to a high F and falls home to F",
   "trumpets play a short fanfare countermelody between the phrases", *DRUMS,
   "big ensemble drum hits every half bar", "strong final cadence in F minor"], []),
 ("Last hits", 6000, "two final tutti hits, then ring out", [
   "two huge tutti chord hits on beat 1 and beat 3 of the first bar, the second is the biggest and the last",
   "after the second hit nothing new plays: the chord rings out and decays naturally to silence",
   "F minor chord, horns on top"], ["new melody", "drum groove", "fade in"]),
]
MASTER_RANGES = [(0, 12000), (12000, 21000), (24000, 48000), (48000, 60000), (60000, 72000), (72000, 84000), (84000, 90000)]

def plan(cond=None):
    chunks = []
    for i, (name, d, line, pos, neg) in enumerate(SECTIONS):
        c = {"text": f"[{name}]\n{{instrumental, {line}}}", "duration_ms": d,
             "positive_styles": COMMON + pos, "negative_styles": neg + BANS, "context_adherence": "high"}
        if cond and cond[i]:
            s, e = MASTER_RANGES[i]
            c["conditioning_ref"] = {"song_id": "THEME", "range": {"start_ms": s, "end_ms": e}, "condition_strength": cond[i]}
        chunks.append(c)
    return {"chunks": chunks}

json.dump(plan(), open("op_anthem_plan_v1_free.json", "w"), indent=1)
json.dump(plan(["low"] * 7), open("op_anthem_plan_v2_lowcond.json", "w"), indent=1)
print("ok")

# --- v3 (after takes 1-2): base = take 2 (song_id 2pOkETSO6yen6lzuOL7j, passed as --theme-id), keep what works,
# rewrite the rise (thin -> crescendo -> drums-only fill -> breath) and the hook (brass anthem, octave leap, biggest hit).
V3_TEXT = {
 3: ("Rise - the Steps", "the build starts thin and grows bar by bar into the climax", [
   "the first bar drops back to strings tremolo, low claps and a quiet snare roll, much thinner than before",
   "each bar adds more: horn calls, then trumpets, then trombones, a steady crescendo",
   "harmony climbs D-flat major, E-flat major, C suspended, C major", "snare roll and toms grow louder every bar",
   "the last half bar is a loud all-drums fill, then one short breath of silence before the hook"], []),
 4: ("Hook - the anthem", "the climax: the full brass section plays the main melody, louder and higher than anything before", [
   "the loudest and widest moment of the piece: every instrument enters together on the first downbeat with a huge hit",
   "the hook melody: a short C, a leap up a full octave to a long high C, then down by steps B-flat, A-flat, G and A-flat",
   "six French horns, three trumpets and trombones in unison carry the melody, bright and powerful, a heroic brass anthem",
   "violins double the melody an octave higher", "a running high-string countermelody in eighth notes",
   *DRUMS, "big ensemble drums on every downbeat, cymbal crashes", "triumphant, heroic, unforgettable"], ["quiet", "thin"]),
}
V3_COND = ["medium", "medium", "medium", None, None, "low", "medium"]
T2_RANGES = [(0, 12000), (12000, 21000), (21000, 45000), (45000, 57000), (57000, 69000), (69000, 81000), (81000, 87000)]

def plan_v3():
    p = plan()
    for i, c in enumerate(p["chunks"]):
        if i in V3_TEXT:
            name, line, pos, neg = V3_TEXT[i]
            c["text"] = f"[{name}]\n{{instrumental, {line}}}"
            c["positive_styles"] = COMMON + pos
            c["negative_styles"] = neg + BANS
        if V3_COND[i]:
            s, e = T2_RANGES[i]
            c["conditioning_ref"] = {"song_id": "THEME", "range": {"start_ms": s, "end_ms": e}, "condition_strength": V3_COND[i]}
    return p

json.dump(plan_v3(), open("op_anthem_plan_v3_t2base.json", "w"), indent=1)
print("v3 ok")

# --- v4 (after take 3 lost the grid without conditioning): low conditioning on the master in every chunk
# (grid + motif anchor, as take 2) + the v3 rise/hook texts.
def plan_v4():
    p = plan(["low"] * 7)
    for i, (name, line, pos, neg) in V3_TEXT.items():
        c = p["chunks"][i]
        c["text"] = f"[{name}]\n{{instrumental, {line}}}"
        c["positive_styles"] = COMMON + pos
        c["negative_styles"] = neg + BANS
    return p

json.dump(plan_v4(), open("op_anthem_plan_v4_lowcond_brass.json", "w"), indent=1)
print("v4 ok")
