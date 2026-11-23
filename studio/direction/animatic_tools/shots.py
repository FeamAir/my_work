#!/usr/bin/env python3
"""S01E01 animatic, step 1: timed shot list from the storyboard data + draft VO durations.

Rule (animatic.md step 1): durations change, script text never does.
  shot_dur = max(storyboard dur, VO speech + lead + tail), rounded up to 0.25 s.
Writes:
  output/S01E01/animatic/spec/shots.json          (machine list, used by frames/la/sound/assemble)
  studio/direction/shotlists/S01E01_shotlist.md   (timed shot list, one line per shot)
No network, no paid calls.  Run: python3 -I studio/direction/animatic_tools/shots.py
"""
import csv
import json
import math
import os
import sys

ROOT = "/home/user/my_work"
SB = f"{ROOT}/studio/storyboard/S01E01/_build"
VO_DIR = f"{ROOT}/output/S01E01/animatic/vo"
SPEC = f"{ROOT}/output/S01E01/animatic/spec"
sys.path.insert(0, SB)
import build  # noqa: E402  (storyboard generator: ORDER, load)

LEAD, TAIL, GAP = 0.2, 0.35, 0.3
# Sc 11 steward: 10 s read vs 4 s shot -> the 6.5 s alt take (sound: S01E01_vo_durations.md)
VO_OVERRIDE = {"L072": "alt/sc11-sh030_L072_V17_STEWARD_v4turbo.mp3"}


def ceil_q(x, q=0.25):
    return math.ceil(x / q - 1e-9) * q


def load_vo():
    man = json.load(open(f"{VO_DIR}/manifest.json"))
    by_file = {}
    for k, v in man.items():
        by_file[k] = v
    rows = list(csv.DictReader(open(f"{ROOT}/studio/sound/S01E01_vo_durations.csv")))
    lines = {}
    for r in rows:
        lid = r["line_id"]
        f = VO_OVERRIDE.get(lid) or (r["file"].split("animatic/vo/")[-1] if "animatic/vo/" in r["file"] else "")
        m = by_file.get(f, {})
        if not f or not os.path.exists(f"{VO_DIR}/{f}"):
            lines.setdefault(r["shot_id"], []).append(dict(line=lid, char=r["character"], text=r["text"],
                                                          file=None, speech=0.0, ss=0.0, delivery=r["delivery"]))
            continue
        speech = m.get("speech_dur") or float(r["seconds"] or 0)
        lines.setdefault(r["shot_id"], []).append(dict(
            line=lid, char=r["character"], text=r["text"], file=f, speech=round(speech, 2),
            ss=m.get("speech_start", 0.0), delivery=r["delivery"]))
    return lines


def main():
    vo = load_vo()
    shots, t = [], 0.0
    keys = {}
    raw = []
    for name in build.ORDER:
        m = build.load(name)
        for i, s in enumerate(m.SHOTS):
            s.id = f"{name}-sh{(i + 1) * 10:03d}"
            s.scene = name
            if s.key:
                keys[s.key] = s.id
            raw.append((name, m.SCENE, s))
    for name, sc, s in raw:
        ls = vo.get(s.id, [])
        speech = sum(x["speech"] for x in ls) + GAP * max(0, len([x for x in ls if x["file"]]) - 1)
        need = ceil_q(speech + LEAD + TAIL) if speech else 0
        dur = max(s.dur, need)
        off = LEAD
        for x in ls:
            if not x["file"]:
                continue
            x["start"] = round(t + off, 3)
            off += x["speech"] + GAP
        shots.append(dict(
            id=s.id, scene=name, tc=round(t, 3), dur=dur, sb_dur=s.dur, cls=s.cls, plan=s.plan, cam=s.cam,
            act=s.act, line=s.line, la=s.la, refs=s.refs, kf=s.kf, mot=s.mot, dirn=s.dirn,
            reuse=keys.get(s.reuse) if s.reuse else None,
            clipreuse=keys.get(s.clipreuse) if s.clipreuse else None,
            nochar=s.nochar, refplate=s.refplate, vfx=s.vfx, v=s.v, tags=sorted(s.tags), l12=s.l12,
            note=s.note, light=sc.get("light", ""), loc=sc.get("loc", ""), vo=ls))
        t += dur
    # L080: tail of L079 heard again over the cut into sc15a-sh010 (no separate read)
    os.makedirs(SPEC, exist_ok=True)
    json.dump(dict(total=t, shots=shots), open(f"{SPEC}/shots.json", "w"), ensure_ascii=False, indent=1)
    write_md(shots, t)
    sb_total = sum(x["sb_dur"] for x in shots)
    print(f"shots {len(shots)}  storyboard {sb_total:.1f}s  timed {t:.1f}s ({fmt(t)})  +{t - sb_total:.1f}s")


def fmt(t):
    return f"{int(t // 60)}:{t % 60:04.1f}"


def code(la):
    import re
    return " ".join(sorted(set(re.findall(r"L-\d\d", la or "")))) or "—"


def write_md(shots, total):
    L = []
    L.append("# S01E01 «The Ninth Sluice» — timed shot list (animatic v1)\n")
    L.append("Версия 1.0 · 2026-11-23 · режиссёр-постановщик · статус: **аниматик v1, до picture lock**\n")
    L.append("Источник: раскадровка r4 (`studio/storyboard/S01E01/_build/sc*.py`, промпты и ref-ID — там же) + черновая озвучка "
             "(`studio/sound/S01E01_vo_durations.csv`). Правило: меняются длительности, не текст. "
             f"Длительность кадра = max(раскадровка, речь + {LEAD} с до + {TAIL} с после), шаг 0,25 с. "
             "Машинная версия: `output/S01E01/animatic/spec/shots.json` (R2 `S01E01/animatic/spec/`). "
             "Генератор: `studio/direction/animatic_tools/shots.py`.\n")
    sb = sum(x["sb_dur"] for x in shots)
    L.append(f"**Итого: {len(shots)} кадров, {fmt(total)}** (раскадровка {fmt(sb)}, +{total - sb:.1f} с от озвучки). "
             "Эндинг (1:36) и превью E2 (~0:20) не раскадрованы и в аниматик не входят → с ними ≈ 29:50.\n")
    L.append("Колонки: id · ТК · длит. (раскадр.) · класс · LA · ref-ID · кадр (kf = переиспользование плиты) · реплики\n")
    cur = None
    for s in shots:
        if s["scene"] != cur:
            cur = s["scene"]
            sc = [x for x in shots if x["scene"] == cur]
            st = sum(x["dur"] for x in sc)
            sbt = sum(x["sb_dur"] for x in sc)
            L.append(f"\n## {cur} — {fmt(sc[0]['tc'])}, {st:.1f} с (раскадровка {sbt:.1f} с, {len(sc)} кадров)\n")
            L.append("| id | ТК | длит. | кл. | LA | ref | кадр | VO |")
            L.append("|---|---|---|---|---|---|---|---|")
        d = f"{s['dur']:g}" + (f" ({s['sb_dur']:g})" if s["dur"] != s["sb_dur"] else "")
        frame = ("kf=" + s["reuse"]) if s["reuse"] else ("ref-plate" if s["refplate"] else ("plate" if s["nochar"] else "new"))
        if s["cls"] in "CD" and not s["reuse"]:
            frame += " +end"
        vo = ", ".join(f"{x['line']} {x['speech']:.1f}s" for x in s["vo"]) or "—"
        refs = (s["refs"] or "—").replace("|", "/")
        L.append(f"| {s['id']} | {fmt(s['tc'])} | {d} | {s['cls']} | {code(s['la'])} | {refs} | {frame} | {vo} |")
    open(f"{ROOT}/studio/direction/shotlists/S01E01_shotlist.md", "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
