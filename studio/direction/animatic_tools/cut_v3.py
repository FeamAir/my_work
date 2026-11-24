#!/usr/bin/env python3
"""S01E01 animatic v3: the lead writer's v3 edit decisions (continuity_check.md §9, binding) applied to v2.

  python3 -I cut_v3.py plan      # print per-scene table, scene starts, checks (no files written)
  python3 -I cut_v3.py write     # -> output/S01E01/animatic/spec/shots_v3.json + studio/direction/shotlists/S01E01_shotlist.md
  python3 -I cut_v3.py la        # LA render of v3-changed shots only -> output/S01E01/animatic/la_v3/ ($0)

Basis: spec/shots_v2.json (1289.75 s). Every v2 duration named in §9 is asserted before it is changed, so a table
typo cannot silently re-time the wrong shot. "Trim" never re-times speech: each VO keeps its offset inside its
shot, and the shot must still hold offset + speech + 0.35 s.
Re-frames re-use existing frames (field `reuse`); no new frames except sc20-sh010 (regen_v3.py).
No network, no paid calls.
"""
import json
import os
import sys

ROOT = "/home/user/my_work"
A = f"{ROOT}/output/S01E01/animatic"
V1, V2, V3 = f"{A}/spec/shots.json", f"{A}/spec/shots_v2.json", f"{A}/spec/shots_v3.json"
TAIL = 0.35

# shot -> (v2 duration as in §9, v3 duration); None = drop
T = {
    # §9.1 Sc 16-18
    "sc16-sh010": (4.0, 2.5), "sc16-sh030": (2.5, None), "sc16-sh040": (2.5, 2.0), "sc16-sh050": (3.25, 3.25),
    "sc16-sh060": (7.0, 5.5), "sc16-sh080": (3.0, 3.0), "sc16-sh090": (2.5, None), "sc16-sh100": (2.5, None),
    "sc16-sh110": (4.0, 3.5), "sc16-sh120": (2.5, 2.0), "sc16-sh130": (2.5, 1.75), "sc16-sh140": (3.0, 3.0),
    "sc16-sh150": (2.5, None), "sc16-sh170": (3.25, None), "sc16-sh180": (5.0, 3.5),
    "sc17-sh010": (4.0, 3.0), "sc17-sh020": (2.5, None), "sc17-sh030": (3.25, 3.0), "sc17-sh040": (2.5, 2.0),
    "sc17-sh050": (2.5, None), "sc17-sh060": (2.5, 2.5), "sc17-sh070": (3.25, None), "sc17-sh090": (3.25, 3.0),
    "sc17-sh100": (3.0, 2.5), "sc17-sh110": (2.5, 2.5), "sc17-sh120": (3.25, None), "sc17-sh130": (2.5, 2.0),
    "sc18-sh010": (4.0, 3.0), "sc18-sh020": (2.75, None), "sc18-sh030": (3.75, 3.0), "sc18-sh040": (2.25, None),
    "sc18-sh050": (3.75, 3.0), "sc18-sh060": (5.0, 5.0), "sc18-sh070": (2.0, 2.0), "sc18-sh080": (4.25, 3.25),
    "sc18-sh090": (2.75, 2.0), "sc18-sh100": (2.75, 2.5), "sc18-sh110": (2.25, 1.75), "sc18-sh120": (5.0, 4.0),
    # §9.2 other dead zones
    "sc01-sh140": (7.0, 6.0), "sc01-sh150": (5.0, 4.0),
    "sc08-sh060": (2.0, 1.5), "sc08-sh130": (2.5, None), "sc08-sh190": (2.5, None), "sc08-sh200": (3.0, 2.0),
    "sc09-sh010": (3.25, 2.5), "sc09-sh020": (3.25, 2.5), "sc09-sh170": (6.0, 4.0), "sc09-sh180": (5.5, 5.0),
    "sc13-sh010": (4.0, 2.5), "sc13-sh020": (5.0, 3.5), "sc13-sh030": (3.0, None), "sc13-sh040": (2.25, None),
    "sc13-sh050": (3.5, 3.0), "sc13-sh080": (3.25, 3.0), "sc13-sh170": (4.0, 3.0), "sc13-sh180": (4.0, 2.5),
    "sc10-sh010": (3.0, 2.5), "sc10-sh020": (3.75, 2.5), "sc10-sh040": (2.25, 2.0), "sc10-sh050": (3.0, 2.5),
    "sc10-sh080": (3.75, 3.0), "sc10-sh120": (2.75, 2.25), "sc10-sh140": (3.0, None),
    "sc10-sh290": (2.0, 1.5), "sc10-sh330": (2.5, 1.75), "sc10-sh340": (2.25, 2.25), "sc10-sh350": (3.0, 2.5),
    "sc10-sh380": (3.5, None),
    "sc14-sh020": (2.75, 2.25), "sc14-sh030": (3.0, 2.5),
    "sc11-sh060": (2.25, 1.75), "sc11-sh070": (2.0, None), "sc11-sh090": (2.25, 1.75), "sc11-sh110": (2.75, 2.75),
    "sc11-sh140": (3.0, 2.25), "sc11-sh170": (3.0, None),
    "sc15-sh020": (2.75, 2.25), "sc15-sh060": (2.25, 1.75), "sc15-sh260": (4.25, 3.25),
    "sc15a-sh100": (4.5, 3.5),
    "sc12-sh010": (4.5, 3.0), "sc12-sh020": (4.5, 4.0), "sc12-sh040": (3.75, 2.0),
    "sc20-sh010": (5.0, 4.0), "sc20-sh020": (3.25, None), "sc20-sh030": (3.25, 3.0), "sc20-sh040": (2.5, None),
    "sc20-sh050": (3.25, 2.5), "sc20-sh070": (3.25, 3.0),
    "sc05-sh080": (10.5, 10.5),
}

# frame changes (render frame = frames/<reuse>_a.png); "DARK" = no picture, plain dark ground
REFRAME = {
    "sc05-sh080": ("sc05-sh010", "keeper blocker 1 / §9.2: slow pull-back on tapestry panel 1 only (v2: panels 1-6 strip "
                                 "with 3 and 4 side by side)"),
    "sc05-sh100": ("DARK", "keeper item 2: HOLLOWSTONE title on plain dark, not over panel 6"),
    "sc10-sh190": ("sc10-sh230", "§9.6: L060 is Lucan's line -> Lucan MCU (H)"),
    "sc10-sh200": ("sc10-sh190", "§9.6: re-use re-pointed to the original Ruel MCU (R)"),
    "sc10-sh230": ("sc10-sh190", "§9.6: L064 is Ruel's line -> Ruel MCU (R)"),
    "sc10-sh240": ("sc10-sh230", "§9.6: re-use re-pointed to the original Lucan MCU (H)"),
    "sc11-sh060": ("sc10-sh040", "§9.5: the steward with the hare's-ear pin by the door waits with the hall"),
    "sc20-sh180": ("sc20-sh050", "analyst: v2 frame read grey-haired; Wick at the table, lamp-lit (hair brown)"),
}
# delivery marks changed by §9.6
DELIVERY = {"L060": "[MS]", "L064": "[MS]"}

# §9.5 restore: v1 shot, placed after sc10-sh080, frame = sc10-sh090 (Ruel, door-warden's back), existing L058 audio
RESTORE = {"sc10-sh100": dict(after="sc10-sh080", dur=5.25, reuse="sc10-sh090")}

# §9.4 L014 new take (studio director approved one TTS call); speech from audio_measure of the accepted take
L014 = dict(text="Hold the rope, Wick.", file="sc03-sh110_L014_V01_PELL_v3.mp3")

# §9.3 Sc 15a split. Condition checked on frames: sc15a-sh050_a.png shows a cord across the collar (net-bag cord,
# reads as "the cord") -> sh050 stays in 15a-2 before sh060; 15a-1 = sh020-sh040 (10.75 s).
SC15A_1 = ["sc15a-sh020", "sc15a-sh030", "sc15a-sh040"]
SC15A_1_AFTER = "sc10-sh360"

TARGET = 1191.0


def load():
    v1 = {s["id"]: s for s in json.load(open(V1))["shots"]}
    v2 = json.load(open(V2))["shots"]
    return v1, v2


def build():
    v1, v2 = load()
    by2 = {s["id"]: s for s in v2}
    for sid, (old, new) in T.items():
        assert sid in by2, sid
        assert abs(by2[sid]["dur"] - old) < 1e-6, (sid, by2[sid]["dur"], old)
    order = [s["id"] for s in v2 if not (s["id"] in T and T[s["id"]][1] is None)]
    for sid in SC15A_1:
        order.remove(sid)
    i = order.index(SC15A_1_AFTER) + 1
    order[i:i] = SC15A_1
    for sid, r in RESTORE.items():
        order.insert(order.index(r["after"]) + 1, sid)

    vo_meta = json.load(open(f"{A}/vo/sc03-sh110_L014_V01_PELL_v3.json"))
    out, t = [], 0.0
    for sid in order:
        if sid in RESTORE:
            s = dict(v1[sid])
            s["v1_tc"], s["v1_dur"] = s["tc"], s["dur"]
            s["v2_tc"], s["v2_dur"] = None, None
            s["reuse"] = RESTORE[sid]["reuse"]
            d = RESTORE[sid]["dur"]
            offs = [0.2 for _ in s["vo"]]
            s["v3_note"] = "RESTORED §9.5 (L058, existing v2 audio; frame re-use sc10-sh090)"
            s["la_dir"] = "la_v3"
        else:
            s = dict(by2[sid])
            s["v2_tc"], s["v2_dur"] = s["tc"], s["dur"]
            d = T[sid][1] if sid in T else s["dur"]
            offs = [round(v["start"] - s["tc"], 3) if v.get("file") else 0 for v in s["vo"]]
            s["v3_note"] = None
            changed = d != s["dur"]
            if sid in REFRAME:
                s["reuse"] = REFRAME[sid][0]
                s["v3_note"] = "RE-FRAME: " + REFRAME[sid][1]
                changed = True
            if sid == "sc05-sh080":
                s["cam_override"] = ["out", 0.3]
            if sid == "sc20-sh010":
                s["v3_note"] = "NEW FRAME: NB2 /edit take 1 + $0 hair grade (Wick read grey-haired in v2)"
                changed = True
            if sid == "sc03-sh110":
                changed = True
            s["la_dir"] = "la_v3" if changed else ("la_v2" if s.get("changed") else "la")
        vo = []
        for v, off in zip(s["vo"], offs):
            v = dict(v)
            if v.get("line") == "L014":
                v.update(text=L014["text"], file=L014["file"], speech=vo_meta["speech_dur"],
                         ss=vo_meta["speech_start"])
            if v.get("line") in DELIVERY:
                v["delivery"] = DELIVERY[v["line"]]
            if v.get("file"):
                v["start"] = round(t + off, 3)
            vo.append(v)
        if sid == "sc03-sh110":   # §9.2: final = max(1.75, speech + 0.55)
            sp = vo[0]["speech"]
            d = max(1.75, round(-(-(sp + 0.55) // 0.25) * 0.25, 2))
        for v, off in zip(vo, offs):
            if v.get("file"):
                assert off + v["speech"] + TAIL <= d + 1e-6, (sid, v["line"], off, v["speech"], d)
        s["vo"], s["tc"], s["dur"] = vo, round(t, 3), d
        s["changed"] = s["la_dir"] == "la_v3"
        out.append(s)
        t += d
    return v2, out, round(t, 3)


def fmt(t):
    return f"{int(t // 60)}:{t % 60:05.2f}"


def starts(v3):
    seen, res = set(), []
    for s in v3:
        key = s["scene"] + ("-1" if s["id"] in SC15A_1 else ("-2" if s["scene"] == "sc15a" else ""))
        if key not in seen:
            seen.add(key)
            res.append((key, s["tc"]))
    return res


def plan():
    v2, v3, total = build()
    print(f"v2 {len(v2)} shots {fmt(sum(s['dur'] for s in v2))} -> v3 {len(v3)} shots {fmt(total)} ({total:.2f}s)")
    print(" · ".join(f"{k} {fmt(t)}" for k, t in starts(v3)))
    hook = next(s["tc"] for s in v3 if s["id"] == "sc03-sh220")
    l106 = next(v["start"] for s in v3 for v in s["vo"] if v.get("line") == "L106")
    print("stone answers", fmt(hook), "| L106", fmt(l106), "| L014 shot", next(s["dur"] for s in v3 if s["id"] == "sc03-sh110"))
    nvo = sum(1 for s in v3 for v in s["vo"] if v.get("file"))
    print("VO lines", nvo)
    # no two consecutive identical frames in Sc 10 quarrel
    q = [s for s in v3 if s["id"] in ("sc10-sh170", "sc10-sh180", "sc10-sh190", "sc10-sh200", "sc10-sh210",
                                       "sc10-sh220", "sc10-sh230", "sc10-sh240", "sc10-sh260")]
    print("Sc10 frames:", [(s["id"][-5:], s["reuse"] or s["id"][-5:]) for s in q])
    return v2, v3, total


def write():
    v2, v3, total = plan()
    assert abs(total - TARGET) < 0.01, total
    dropped = [dict(id=sid, v2_dur=o, why="§9 drop") for sid, (o, n) in T.items() if n is None]
    json.dump(dict(total=total, version="v3", basis="shots_v2.json + continuity_check §9", shots=v3, dropped=dropped),
              open(V3, "w"), ensure_ascii=False, indent=1)
    write_md(v2, v3, total, dropped)
    print("wrote", V3)


def write_md(v2, v3, total, dropped):
    t2 = sum(s["dur"] for s in v2)
    L = ["# S01E01 «The Ninth Sluice» — timed shot list (animatic v3, 19:51 cut)\n",
         "Версия 3.0 · 2026-11-24 · режиссёр-постановщик · статус: **аниматик v3, кандидат в picture lock**\n",
         "Источник: v2 (`spec/shots_v2.json`, 1289.75 с) → решения главного сценариста `story/episodes/S01E01/"
         "continuity_check.md` §9 (обязательны) → `animatic_tools/cut_v3.py` → `output/S01E01/animatic/spec/shots_v3.json`. "
         "Заметки: `direction/S01E01_animatic_v3_notes.md`. Чек-лист финалов: `direction/S01E01_finals_checklist.md`.\n",
         f"**Итого: {len(v3)} кадров, {fmt(total)}** (v2: {len(v2)} кадров, {fmt(t2)}; {total - t2:+.2f} с).\n",
         "Начала сцен: " + " · ".join(f"{k} {fmt(t)}" for k, t in starts(v3)) + "\n",
         "Колонки: id · ТК v3 · длит. v3 (v2) · класс · кадр (kf = переиспользование) · реплики · примечание v3.\n"]
    cur = None
    for s in v3:
        key = s["scene"] + (" (15a-1)" if s["id"] in SC15A_1 else (" (15a-2)" if s["scene"] == "sc15a" else ""))
        if key != cur:
            cur = key
            L += [f"\n## {key} — {fmt(s['tc'])}\n", "| id | ТК | длит. | кл. | кадр | VO | v3 |", "|---|---|---|---|---|---|---|"]
        d = f"{s['dur']:g}" + (f" ({s['v2_dur']:g})" if s.get("v2_dur") not in (None, s["dur"]) else
                               (" (cut in v2)" if s.get("v2_dur") is None else ""))
        frame = "dark" if s["reuse"] == "DARK" else (("kf=" + s["reuse"]) if s["reuse"] else "own")
        vo = ", ".join(f"{v['line']} {v.get('delivery', '')} {v['speech']:.2f}s" for v in s["vo"] if v.get("file")) or "—"
        L.append(f"| {s['id']} | {fmt(s['tc'])} | {d} | {s['cls']} | {frame} | {vo} | {s.get('v3_note') or ''} |")
    L.append("\n## Убраны в v3 (§9)\n")
    L.append(", ".join(f"~~{x['id']}~~ ({x['v2_dur']:g})" for x in dropped) + "\n")
    open(f"{ROOT}/studio/direction/shotlists/S01E01_shotlist.md", "w").write("\n".join(L) + "\n")


def la():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import concurrent.futures as cf
    import la as LAmod
    LAmod.LA = f"{A}/la_v3"
    os.makedirs(LAmod.LA, exist_ok=True)
    LAmod.ensure_fx()
    v3 = json.load(open(V3))["shots"]
    todo = [s for s in v3 if s["la_dir"] == "la_v3"]
    force = bool(os.environ.get("FORCE"))
    print("LA v3 jobs", len(todo), flush=True)
    with cf.ProcessPoolExecutor(int(os.environ.get("WORKERS", "4"))) as ex:
        for sid, r in ex.map(LAmod.render, todo, [force] * len(todo)):
            if r != "skip":
                print(sid, r, flush=True)


if __name__ == "__main__":
    {"plan": plan, "write": write, "la": la}[sys.argv[1]]()
