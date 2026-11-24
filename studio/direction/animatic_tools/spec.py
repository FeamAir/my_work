#!/usr/bin/env python3
"""S01E01 animatic, step 6: assembly spec for pipeline/assemble.py + subtitles + final overlay pass.

  python3 -I spec.py build      # -> output/S01E01/animatic/spec/S01E01_animatic_v1.json + .srt
  python3 -I spec.py assemble   # pipeline.assemble -> S01E01_animatic_v1_raw.mp4 (720p, -14 LUFS, -1 dBTP)
  python3 -I spec.py overlay    # timecode, DRAFT mark, subtitles (video re-encode, audio copied) -> S01E01_animatic_v1.mp4

Sound placement is placeholder (animatic.md step 1/5): VO on dx, ambiences per scene (looped), key SFX and
synth tones at their shots, temp music pads labelled on screen. Lullaby five notes only in Sc 1 and Sc 3
(Sc 20: stone tone only, no melody, per lullaby.md §6).
"""
import json
import os
import re
import subprocess
import sys

ROOT = "/home/user/my_work"
sys.path.insert(0, ROOT)
A = f"{ROOT}/output/S01E01/animatic"
SPEC = f"{A}/spec/S01E01_animatic_v1.json"
SRT = f"{A}/spec/S01E01_animatic_v1.srt"
RAW = f"{A}/S01E01_animatic_v1_raw.mp4"
FINAL = f"{A}/S01E01_animatic_v1.mp4"
SFX, SYN, VO = f"{A}/audio/sfx", f"{A}/audio/synth", f"{A}/vo"

# ambience per scene: (first shot, last shot or None=scene end, sfx id, gain_db)
AMB = [
    ("sc01-sh010", "sc01-sh090", "amb_flood-night-street", 0), ("sc01-sh100", "sc01-sh100", "amb_underwater", -2),
    ("sc01-sh110", None, "amb_flood-night-street", -4),
    ("sc02-sh010", None, "amb_lows-dawn-ebb", 0), ("sc02-sh010", None, "amb_treadmill-pump", -12),
    ("sc03-sh010", "sc03-sh050", "amb_lows-dawn-ebb", 0), ("sc03-sh060", None, "amb_sump-pool", 0),
    ("sc04-sh010", None, "amb_lows-house-interior", 0), ("sc06-sh010", None, "amb_treadmill-pump", 0),
    ("sc08-sh010", None, "amb_spire-stair", 0), ("sc09-sh010", "sc09-sh050", "amb_harbour", 0),
    ("sc09-sh170", None, "amb_harbour", -8), ("sc09-sh100", "sc09-sh160", "amb_lows-dusk-tide", -6),
    ("sc13-sh010", None, "amb_counting-hall", 0), ("sc10-sh010", None, "amb_tithe-hall", 0),
    ("sc14-sh010", None, "amb_counting-hall", 0), ("sc11-sh010", None, "amb_tithe-hall", 0),
    ("sc15-sh010", None, "amb_counting-hall", 0), ("sc15a-sh010", None, "amb_lows-dusk-tide", 0),
    ("sc12-sh010", "sc12-sh240", "amb_tithe-hall", -3), ("sc12-sh250", None, "amb_tithe-hall-empty", 0),
    ("sc16-sh010", "sc16-sh160", "amb_counting-hall", -2), ("sc16-sh170", None, "amb_mids-gate-dusk", -3),
    ("sc17-sh010", None, "amb_relay-room", 0), ("sc18-sh010", None, "amb_mids-gate-dusk", 0),
    ("sc19-sh010", "sc19-sh200", "amb_lows-dusk-tide", 0), ("sc19-sh210", None, "amb_lows-dusk-tide", 4),
    ("sc20-sh010", "sc20-sh230", "amb_lows-house-interior", -6),
]
# events: (shot, file (sfx id or synth/...), offset s, gain_db, stem)
EV = [
    ("sc01-sh010", "sfx_whistles-alarm", 0, 0, "fx"), ("sc01-sh040", "walla_flood-crowd", 0, -4, "fx"),
    ("sc01-sh050", "sfx_gate-bar-drag", 0, 0, "fx"), ("sc01-sh080", "sfx_gate-bar-drag", -0.5, 2, "fx"),
    ("sc01-sh090", "sfx_fists-iron-gate", 0, 0, "fx"), ("sc01-sh130", "sfx_rowboat-oars", 0, -3, "fx"),
    ("sc01-sh100", "synth/lullaby_woman_v1", 2.0, -2, "mus"), ("sc01-sh120", "synth/lullaby_woman_v1", 0, -7, "mus"),
    ("sc01-sh140", "synth/lullaby_woman_v1", 0, -12, "mus"), ("sc01-sh140", "synth/lullaby_baby2_v1", 4.6, -6, "mus"),
    ("sc02-sh020", "foley_knock-doorpost", 0, 0, "foley"), ("sc02-sh040", "foley_chain-box", 1.0, 0, "foley"),
    ("sc02-sh150", "synth/spire_flat_v1", 0, -6, "fx"), ("sc02-sh190", "foley_ladder", 0, 0, "foley"),
    ("sc03-sh020", "foley_mud-steps", 0, 0, "foley"), ("sc03-sh140", "foley_rope-creak", 0, 0, "foley"),
    ("sc03-sh150", "sfx_rake-snag", 0, 0, "fx"), ("sc03-sh180", "synth/hum_pell3_v1", 0.2, -4, "mus"),
    ("sc03-sh200", "synth/spire_flat_v1", 0, -8, "fx"), ("sc03-sh220", "synth/stone_tone_6s_v1", 0, 0, "fx"),
    ("sc03-sh230", "sfx_ripple-tremble", 0, -4, "fx"), ("sc03-sh360", "sfx_reed-whistle", 0.5, -6, "fx"),
    ("sc04-sh130", "synth/spire_flat_v1", 0, -8, "fx"), ("sc04-sh190", "foley_net-chest", 0, 0, "foley"),
    ("sc04-sh210", "foley_ladder", 0, 0, "foley"), ("sc04-sh260", "foley_page-turn", 1.5, 0, "foley"),
    ("sc05-sh010", "foley_page-turn", 0, 0, "foley"),
    ("sc06-sh020", "sfx_reed-whistle", 2.0, 0, "fx"), ("sc06-sh040", "sfx_reed-whistle", 0, 0, "fx"),
    ("sc06-sh130", "sfx_reed-whistle", 0, 2, "fx"),
    ("sc07-sh020", "foley_parchment", 0, -2, "foley"), ("sc07-sh060", "foley_parchment", 1, -2, "foley"),
    ("sc08-sh070", "synth/fork_c5_v1", 0, 0, "fx"),
    ("sc09-sh030", "synth/ione_c5_v1", 1.0, -2, "mus"), ("sc09-sh040", "synth/spire_hum_c2c3_v1", 0, -2, "fx"),
    ("sc10-sh010", "foley_parchment", 2, -6, "foley"),
    ("sc11-sh020", "foley_staff-strike", 0.3, 0, "foley"), ("sc11-sh080", "foley_silver-cup", 0.5, 0, "foley"),
    ("sc11-sh110", "walla_hall-laugh", 0, -2, "fx"), ("sc11-sh180", "foley_staff-strike", 0.2, 0, "foley"),
    ("sc14-sh180", "foley_stick-felt", 0, 0, "foley"), ("sc15-sh150", "foley_brass-clip", 0.5, 0, "foley"),
    ("sc12-sh010", "foley_parchment", 0, 0, "foley"), ("sc12-sh260", "sfx_fall-table", 0, 2, "fx"),
    ("sc12-sh320", "walla_hall-gasp", 0, 0, "fx"),
    ("sc16-sh040", "foley_bell-small", 0, 0, "fx"), ("sc16-sh050", "synth/death_tone_v1", 0, 0, "fx"),
    ("sc16-sh080", "sfx_ink-drop", 0.8, 4, "fx"), ("sc16-sh090", "synth/death_tone_v1", 0, -3, "fx"),
    ("sc16-sh170", "synth/death_tone_v1", 0, -8, "fx"),
    ("sc17-sh010", "synth/death_tone_v1", 0, -2, "fx"), ("sc18-sh010", "synth/death_tone_v1", 0, -12, "fx"),
    ("sc18-sh030", "foley_guards-file", 0, 0, "foley"), ("sc18-sh060", "sfx_gate-bar-drag", 0, 0, "fx"),
    ("sc19-sh020", "foley_knock-doorpost", 0, 0, "foley"), ("sc19-sh040", "foley_chain-box", 0, 0, "foley"),
    ("sc19-sh110", "foley_net-chest", 0, 0, "foley"), ("sc19-sh190", "synth/death_tone_v1", 0, -6, "fx"),
    ("sc19-sh190", "sfx_whistles-alarm", 1, -8, "fx"), ("sc19-sh200", "sfx_wheel-stop", 0, 0, "fx"),
    ("sc19-sh270", "foley_tin-buttons", 0, -4, "foley"),
    ("sc20-sh010", "synth/death_tone_v1", 0, -14, "fx"), ("sc20-sh080", "synth/stone_tone_12s_v1", 0, -2, "fx"),
    ("sc20-sh160", "sfx_ripple-tremble", 0, -8, "fx"), ("sc20-sh210", "sfx_reed-whistle", 0.5, -10, "fx"),
    ("sc20-sh220", "foley_ladder", 0, 0, "foley"), ("sc20-sh240", "synth/stone_tone_6s_v1", 0, -4, "fx"),
]
# temp music: (first shot, last shot, file, gain, label) — label shown on screen as [TEMP MUSIC: ...]
MUS = [
    ("sc03-sh010", "sc03-sh050", "mus_M03_lows_v1", 0, "M03 street track"),
    ("sc05-sh010", "sc05-sh090", "mus_M05_archive_v1", 0, "M05 Archive"),
    ("sc05-sh100", "sc05-sh100", "mus_TITLE_v1", 2, "T-TITLE saga theme"),
    ("sc07-sh010", "sc07-sh090", "mus_M05_archive_v1", -2, "M05 Archive part B"),
    ("sc08-sh060", "sc08-sh100", "mus_M06_pitch_v1", 0, "M06 Pitch"),
    ("sc10-sh070", "sc10-sh140", "mus_M07_corvane_v1", -2, "M07 Corvane"),
    ("sc12-sh170", "sc12-sh230", "mus_M08_held_v1", -2, "M08 held string"),
    ("sc17-sh010", "sc19-sh340", "mus_M09_clock_v1", -4, "M09 The Clock"),
]


def shots():
    return json.load(open(f"{A}/spec/shots.json"))["shots"]


def srt_t(t):
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}"


def build():
    ss = shots()
    by = {s["id"]: s for s in ss}
    order = [s["id"] for s in ss]
    total = sum(s["dur"] for s in ss)

    def span(a, b):
        sa = by[a]
        if b is None:
            last = [s for s in ss if s["scene"] == sa["scene"]][-1]
        else:
            last = by[b]
        return sa["tc"], last["tc"] + last["dur"]

    # assemble.py opens every clip as a separate decoder in one filter graph: 451 inputs ran out of memory (16 GB).
    # The LA clips share codec/size/fps, so they are joined losslessly first (concat demuxer, stream copy).
    lst = f"{A}/spec/la_concat.txt"
    with open(lst, "w") as f:
        for s in ss:
            f.write(f"file '{A}/la/{s['id']}.mp4'\n")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy",
                    f"{A}/la_concat.mp4"], check=True)
    clips = [{"path": "../la_concat.mp4", "duration": round(total, 3)}]
    tracks, subs = [], []
    n = 0
    for s in ss:
        for v in s["vo"]:
            if not v.get("file"):
                continue
            n += 1
            tracks.append({"id": f"dx_{v['line']}", "stem": "dx", "path": f"../vo/{v['file']}", "start": v["start"],
                           "trim_start": max(0.0, v["ss"] - 0.05), "duration": round(v["speech"] + 0.25, 3)})
            subs.append((v["start"], v["start"] + v["speech"] + 0.3, v["text"]))
    # L080: tail of L079 again over the cut into sc15a-sh010
    l79 = next(v for v in by["sc15-sh190"]["vo"] if v["line"] == "L079")
    tracks.append({"id": "dx_L080", "stem": "dx", "path": f"../vo/{l79['file']}", "start": by["sc15a-sh010"]["tc"] + 0.3,
                   "trim_start": round(l79["ss"] + l79["speech"] - 1.25, 3), "duration": 1.35, "gain_db": -5,
                   "filter": "aecho=0.8:0.5:120:0.3"})
    subs.append((by["sc15a-sh010"]["tc"] + 0.3, by["sc15a-sh010"]["tc"] + 1.8, "…finds its level."))
    for a, b, sid, g in AMB:
        t0, t1 = span(a, b)
        tracks.append({"id": f"amb_{a}_{sid}", "stem": "amb", "path": f"../audio/sfx/{sid}.mp3", "start": round(t0, 3),
                       "duration": round(t1 - t0, 3), "loop": True, "fade_in": 0.5, "fade_out": 0.5, "gain_db": g - 2})
    # v1 mix pass 2: transient SFX normalised to -18 LUFS overshoot the master (TP +0.5, LRA 21) -> trims (dB)
    TRIM = {"sfx_rowboat-oars": -6, "sfx_fall-table": -5, "sfx_rake-snag": -6, "sfx_gate-bar-drag": -4,
            "sfx_fists-iron-gate": -4, "sfx_wheel-stop": -5, "sfx_ripple-tremble": -4}
    for shot, f, off, g, stem in EV:
        g = g + TRIM.get(f, 0) + (-2 if stem == "fx" else 0)
        path = f"../audio/{f}.wav" if f.startswith("synth/") else f"../audio/sfx/{f}.mp3"
        tracks.append({"id": f"ev_{shot}_{f.split('/')[-1]}", "stem": stem, "path": path,
                       "start": round(max(0.0, by[shot]["tc"] + off), 3), "gain_db": g})
    labels = []
    for a, b, f, g, lab in MUS:
        t0, t1 = span(a, b)
        tracks.append({"id": f"mus_{a}", "stem": "mus", "path": f"../audio/synth/{f}.wav", "start": round(t0, 3),
                       "duration": round(t1 - t0, 3), "loop": True, "fade_in": 1.0, "fade_out": 1.5, "gain_db": g})
        labels.append((t0, t1, f"TEMP MUSIC: {lab}"))
    # SDH cues from the storyboard (viewer-safe text only)
    for s in ss:
        for m in re.finditer(r"SDH \[([^\]]+)\]", s["line"] or ""):
            subs.append((s["tc"] + 0.2, s["tc"] + min(s["dur"], 3.5), f"[{m.group(1)}]"))
    subs.sort()
    with open(SRT, "w") as f:
        for i, (a, b, t) in enumerate(subs, 1):
            f.write(f"{i}\n{srt_t(a)} --> {srt_t(b)}\n{t}\n\n")
    json.dump(labels, open(f"{A}/spec/music_labels.json", "w"))
    spec = {"output": "../S01E01_animatic_v1_raw.mp4", "width": 1280, "height": 720, "fps": 24, "clips": clips,
            "tracks": tracks, "keep_clip_audio": False, "ducking": True,
            "master": {"I": -14, "TP": -1, "LRA_min": 11, "LRA_max": 20},
            "meta": {"episode": "S01E01", "version": "animatic v1", "total_s": total, "shots": len(ss)}}
    json.dump(spec, open(SPEC, "w"), indent=1, ensure_ascii=False)
    missing = [t["path"] for t in tracks if not os.path.exists(os.path.join(f"{A}/spec", t["path"]))]
    missing += [c["path"] for c in clips if not os.path.exists(os.path.join(f"{A}/spec", c["path"]))]
    print(f"spec: {len(clips)} clips, {len(tracks)} tracks ({n} VO), {len(subs)} subs, total {total:.1f}s; missing {len(missing)}")
    for m in missing[:20]:
        print("  missing", m)


def assemble():
    from pipeline import assemble as asm
    out, rep = asm.assemble_report(SPEC)
    print(out, json.dumps(rep, ensure_ascii=False)[:800])


def overlay():
    labels = json.load(open(f"{A}/spec/music_labels.json"))
    font = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    vf = [f"drawtext=fontfile={font}:text='%{{pts\\:hms}}':x=w-tw-14:y=10:fontsize=20:fontcolor=white:box=1:boxcolor=black@0.5:boxborderw=5",
          f"drawtext=fontfile={font}:text='ANIMATIC v1 - DRAFT':x=w-tw-14:y=h-th-12:fontsize=16:fontcolor=white@0.6"]
    for a, b, t in labels:
        vf.append(f"drawtext=fontfile={font}:text='[{t}]':x=14:y=40:fontsize=16:fontcolor=0xFFE08A:"
                  f"box=1:boxcolor=black@0.4:boxborderw=4:enable='between(t\\,{a:.2f}\\,{b:.2f})'")
    vf.append(f"subtitles={SRT}:force_style='FontName=DejaVu Sans,FontSize=20,Outline=2,MarginV=28'")
    vf.append("format=yuv420p")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", RAW, "-vf", ",".join(vf), "-c:v", "libx264", "-preset", "veryfast",
           "-crf", "23", "-af", "volume=-0.5dB", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", FINAL]
    subprocess.run(cmd, check=True)
    print(FINAL)


if __name__ == "__main__":
    {"build": build, "assemble": assemble, "overlay": overlay}[sys.argv[1]]()
