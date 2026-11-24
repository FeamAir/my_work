#!/usr/bin/env python3
"""S01E01 animatic v2: the 21:30 cut (studio director's decision on animatic v1, 2026-11-24).

  python3 -I cut_v2.py plan      # re-time, print per-scene table + hook check (no files written)
  python3 -I cut_v2.py write     # -> output/S01E01/animatic/spec/shots_v2.json + studio/direction/shotlists/S01E01_shotlist.md
  python3 -I cut_v2.py la        # LA render of changed / restaged shots only -> output/S01E01/animatic/la_v2/ ($0)

Rules of this cut (notes: studio/direction/S01E01_animatic_v2_notes.md):
  * No story beat, clue/plant (continuity_check.md §4), FIXED line or [ECHO] line is removed. Chronicler lines whole.
  * Existing draft VO only: a line is either kept whole or dropped with its shot (no re-generation, no mid-line edits).
  * A shot is never shorter than its kept VO needs (speech + 0.2 s lead + 0.35 s tail, step 0.25 s).
  * Silent holds are cut first; coverage that repeats a set-up (reaction re-uses, second inserts) is dropped.
No network, no paid calls.
"""
import json
import math
import os
import sys

ROOT = "/home/user/my_work"
A = f"{ROOT}/output/S01E01/animatic"
V1 = f"{A}/spec/shots.json"
V2 = f"{A}/spec/shots_v2.json"
LEAD, TAIL, GAP = 0.2, 0.35, 0.3
TARGET, HARD_MAX, HOOK_MAX = 21 * 60 + 30, 22 * 60 + 30, 180.0

# --- whole shots out (VO on them goes with them) -------------------------------------------------------------
DROP = {
    # Sc 2 — coverage
    "sc02-sh160": "return to Pell's face (re-use of sh140)",
    # Sc 3 — the walk-up (director) and the after-hook coda
    "sc03-sh020": "walk-up: Pell and Wick cross the flats (sh010 already places them)",
    "sc03-sh050": "walk-up: Pell looks ahead (sh060 shows what she sees)",
    "sc03-sh340": "Wick still watching the pool (sh250 carries it)",
    "sc03-sh370": "climb up the ladder (exit; whistle + sh380 end the scene)",
    # Sc 4
    "sc04-sh050": "L021 Nan 'And don't tell me what you found…' — comic set-up, not a plant; the Wick gag still plays",
    # Sc 6
    "sc06-sh100": "L039 Corr 'I've forty grown backs…' — the FIXED line before it (L038) stays",
    # Sc 8 — the stair
    "sc08-sh090": "second fork insert (sh080 carries it)",
    "sc08-sh110": "grooves past her (the spiral is in sh010 and sh130)",
    "sc08-sh120": "slit window",
    "sc08-sh180": "she climbs on (sh190/sh200 carry it)",
    # Sc 13
    "sc13-sh060": "light on felt (re-use of sh020)",
    "sc13-sh130": "nib back up (re-use of sh100)",
    # Sc 10 — council (director)
    "sc10-sh030": "banners detail",
    "sc10-sh060": "veiled figure — marked cuttable in the storyboard",
    "sc10-sh090": "Ruel and the door-warden (set-up for L058)",
    "sc10-sh100": "L058 Ruel 'And that girl of yours?…' — charm beat; sh120 (faces smiling) keeps 'the man you follow'",
    "sc10-sh110": "door-warden's back (pay-off of L058)",
    "sc10-sh130": "faces turn (second crowd reaction)",
    "sc10-sh280": "Lucan's face over the clasp (re-use; the clasp insert sh290 stays)",
    "sc10-sh320": "Helm nods (re-use)",
    # Sc 14
    "sc14-sh080": "two desks side by side (geography already clear from sh020/sh030)",
    "sc14-sh180": "glass of water on Hollis's desk (motif repeat)",
    # Sc 11
    "sc11-sh120": "the hall laughs (re-use; laugh is on sh110)",
    "sc11-sh130": "taster laughs (re-use)",
    "sc11-sh160": "steward takes the cup away",
    # Sc 15
    "sc15-sh050": "clerks' backs (re-use)",
    "sc15-sh200": "Hollis (re-use)",
    "sc15-sh220": "everyone writes, Hollis standing",
    # Sc 12 — council (director)
    "sc12-sh070": "colour blocks don't move (re-use)",
    "sc12-sh110": "taster with the empty cup (re-use; sh360 keeps her)",
    "sc12-sh130": "Ione watches the knuckle, second time (sh080 keeps it)",
    "sc12-sh170": "benches: nobody noticed (re-use)",
    "sc12-sh200": "steward reaches for his gloves",
    "sc12-sh390": "Ione's hand at her throat, second time (sh370 keeps it)",
    # Sc 16
    "sc16-sh020": "clerk trims a lamp wick",
    "sc16-sh160": "high desk and cage (re-use of the idea of sh110)",
    # Sc 17
    "sc17-sh080": "relay-keeper's hands (re-use)",
    # second pass (v2 had 22:53 after the first list): repeated reactions and re-used set-ups
    "sc04-sh210": "Nan's feet down the ladder (sh200 already takes her out)",
    "sc06-sh140": "Wick studies his feet (re-use of sh110)",
    "sc08-sh100": "she opens her eyes (re-use of sh080)",
    "sc08-sh150": "Ione stops (sh140 Cantor gives way → sh160 hand on the band)",
    "sc09-sh090": "Ione still singing (re-use of sh030)",
    "sc09-sh160": "two figures on the ridge (re-use of sh100)",
    "sc13-sh070": "clerks glance at the glass (sh050/sh080 carry the glass)",
    "sc13-sh140": "the same total, second insert",
    "sc10-sh160": "Lucan watches him come (re-use of sh050)",
    "sc10-sh250": "Ruel looks, then smiles (re-use; the FIXED line on sh260 plays the smile)",
    "sc10-sh370": "Ione's small bow (re-use of sh300)",
    "sc14-sh110": "Fossett looks up and smiles (same frame as sh120, which keeps the line)",
    "sc11-sh150": "Helm's hands on the case, second insert (sh140 keeps it)",
    "sc15-sh030": "Hollis straightens too (re-use)",
    "sc15-sh210": "Hollis stands a beat too long (re-use)",
    "sc15-sh250": "sleeve-guards very white (re-use)",
    "sc12-sh060": "Ruel watches the Helm's face (re-use; sh090/sh190 keep Ruel on the pale district)",
    "sc12-sh220": "old eyes on the sheet (re-use; the lip-sync CU follows)",
    "sc16-sh070": "row of raised pens from the side (sh060 carries it)",
    "sc16-sh190": "following the tone down the hill (re-use of sh180)",
    "sc19-sh050": "collector peers after the coins (re-use)",
    "sc19-sh150": "door and empty walk (sh140 carries the look)",
    "sc19-sh250": "collector looks at the box on his wrist",
    "sc19-sh310": "nobody in the lane answers (re-use; the Chronicler answers over sh320)",
    "sc20-sh060": "nobody speaks (re-use of sh010)",
    "sc20-sh100": "the search: floor",
    "sc20-sh110": "the search: lamp (re-use)",
}

# --- explicit new durations (s); everything not listed and not protected is compressed by K[scene] -----------
DUR = {
    # Sc 1 after the 0:30 hook (0:00-0:30 untouched)
    "sc01-sh110": 6, "sc01-sh120": 3, "sc01-sh130": 3, "sc01-sh170": 6,
    # Sc 2
    "sc02-sh110": 1.5, "sc02-sh130": 1.5, "sc02-sh150": 5, "sc02-sh170": 1.5, "sc02-sh190": 1.5,
    # Sc 3 before the hook
    "sc03-sh010": 2.5, "sc03-sh060": 3, "sc03-sh080": 2, "sc03-sh090": 4, "sc03-sh120": 3, "sc03-sh130": 2,
    "sc03-sh140": 2, "sc03-sh160": 3, "sc03-sh190": 2, "sc03-sh200": 2, "sc03-sh210": 1.5,
    # Sc 5 tapestry — Chronicler lines whole; title 8 s
    "sc05-sh100": 8,
    # Sc 9 — the two 10-s hero shots (director) and the 10-s fade
    "sc09-sh030": 6, "sc09-sh060": 6, "sc09-sh170": 6, "sc09-sh100": 5, "sc09-sh150": 5, "sc09-sh180": 5.5,
    # Sc 12 — the fall keeps its weight
    "sc12-sh250": 4, "sc12-sh260": 4,
    # Sc 16 — forty pens
    "sc16-sh060": 7,
    # Sc 18 — never cut; light trims only
    "sc18-sh010": 4, "sc18-sh120": 5,
}

# --- untouched (hooks, protected silences, signature images, lip-sync, on-screen numbers) --------------------
PROTECT = {
    "sc01-sh010", "sc01-sh020", "sc01-sh030", "sc01-sh040", "sc01-sh050", "sc01-sh060", "sc01-sh070", "sc01-sh080",
    "sc01-sh090", "sc01-sh100", "sc01-sh140", "sc01-sh150", "sc01-sh160",
    "sc02-sh010", "sc02-sh020", "sc02-sh050", "sc02-sh200", "sc02-sh210",
    "sc03-sh170", "sc03-sh180", "sc03-sh220", "sc03-sh230",
    "sc04-sh150", "sc04-sh160", "sc04-sh170", "sc04-sh260",
    "sc05-sh040",
    "sc07-sh040", "sc07-sh070",
    "sc08-sh140", "sc08-sh160",
    "sc10-sh290", "sc10-sh330", "sc10-sh350",
    "sc11-sh100", "sc11-sh180",
    "sc13-sh150",
    "sc14-sh040", "sc14-sh050", "sc14-sh070",
    "sc15-sh150", "sc15-sh170", "sc15-sh230",
    "sc12-sh230", "sc12-sh240", "sc12-sh270", "sc12-sh280", "sc12-sh340", "sc12-sh350",
    "sc16-sh080",
    "sc18-sh060", "sc18-sh070",
    "sc19-sh190",
    "sc20-sh080", "sc20-sh150", "sc20-sh160", "sc20-sh190", "sc20-sh200", "sc20-sh220", "sc20-sh230", "sc20-sh240",
}

# per-scene compression of the remaining silent holds (VO shots are floored by their speech)
K = {"sc01": 1.0, "sc02": 1.0, "sc03": 0.8, "sc04": 0.75, "sc05": 0.8, "sc06": 0.75, "sc07": 0.75, "sc08": 0.8,
     "sc09": 0.8, "sc13": 0.7, "sc10": 0.75, "sc14": 0.75, "sc11": 0.75, "sc15": 0.75, "sc15a": 0.9, "sc12": 0.75,
     "sc16": 0.8, "sc17": 0.8, "sc18": 0.9, "sc19": 0.75, "sc20": 0.8}
FLOOR = 1.5

# restaged shots (refused by the fal content checker in v1; script change pending the lead writer's approval)
RESTAGE = {
    "sc02-sh050": "new frame: the rope-bridge over Nan's door sagging and creaking under an unseen weight; the collector "
                  "below does not look up; Wick's line is heard from above, off-screen",
    "sc02-sh070": "re-uses the new sc02-sh050 frame (Wick [OS] from the bridge; the rope sways)",
    "sc02-sh080": "re-uses the new sc02-sh050 frame, push-in to the dark doorway; Nan [OS] from inside (v1 frame with "
                  "the dangling arms retired)",
    "sc04-sh180": "new frame: insert — Nan's hand comes off and lies flat on the table, fingers trembling, beside the "
                  "net-needle; across the board Wick's bread crust lies where he dropped it",
}
REUSE_OVERRIDE = {"sc02-sh070": "sc02-sh050", "sc02-sh080": "sc02-sh050"}


def ceil_q(x, q=0.25):
    return math.ceil(x / q - 1e-9) * q


def need(s):
    ls = [v for v in s["vo"] if v.get("file")]
    if not ls:
        return 0.0
    sp = sum(v["speech"] for v in ls) + GAP * (len(ls) - 1)
    return ceil_q(sp + LEAD + TAIL)


def retime():
    v1 = json.load(open(V1))["shots"]
    out, t = [], 0.0
    for s in v1:
        if s["id"] in DROP:
            continue
        n = need(s)
        if s["id"] in PROTECT:
            d = s["dur"]
        elif s["id"] in DUR:
            d = max(DUR[s["id"]], n)
        else:
            k = K.get(s["scene"], 1.0)
            d = max(n, min(s["dur"], FLOOR), ceil_q(s["dur"] * k))
        d = min(d, s["dur"]) if s["id"] not in DUR else d
        s2 = dict(s)
        s2["v1_tc"], s2["v1_dur"], s2["tc"], s2["dur"] = s["tc"], s["dur"], round(t, 3), d
        if s["id"] in REUSE_OVERRIDE:
            s2["reuse"] = REUSE_OVERRIDE[s["id"]]
        s2["restage"] = RESTAGE.get(s["id"])
        vo, off = [], LEAD
        for v in s["vo"]:
            v = dict(v)
            if v.get("file"):
                v["start"] = round(t + off, 3)
                off += v["speech"] + GAP
            vo.append(v)
        s2["vo"] = vo
        s2["changed"] = (d != s["dur"]) or bool(s2["restage"])
        out.append(s2)
        t += d
    return v1, out, t


def fmt(t):
    return f"{int(t // 60)}:{t % 60:04.1f}"


def report(v1, v2, total):
    by1, by2 = {}, {}
    for s in v1:
        by1.setdefault(s["scene"], []).append(s)
    for s in v2:
        by2.setdefault(s["scene"], []).append(s)
    rows = []
    for sc in by1:
        a = sum(x["dur"] for x in by1[sc])
        b = sum(x["dur"] for x in by2.get(sc, []))
        rows.append((sc, len(by1[sc]), a, len(by2.get(sc, [])), b))
    hook = next(s["tc"] for s in v2 if s["id"] == "sc03-sh220")
    return rows, hook


def plan():
    v1, v2, total = retime()
    rows, hook = report(v1, v2, total)
    for sc, n1, a, n2, b in rows:
        print(f"{sc:6} {n1:3} {a:7.2f} -> {n2:3} {b:7.2f}  ({b - a:+.2f})")
    v1t = sum(s["dur"] for s in v1)
    print(f"total {fmt(v1t)} -> {fmt(total)} ({total:.2f}s; {total - v1t:+.1f}); shots {len(v1)} -> {len(v2)}; "
          f"hook sc03-sh220 at {fmt(hook)}; target {fmt(TARGET)} max {fmt(HARD_MAX)}")
    dropped_vo = [(v["line"], v["char"], s["id"]) for s in v1 if s["id"] in DROP for v in s["vo"]]
    print("VO dropped:", dropped_vo)
    return v1, v2, total


def write():
    v1, v2, total = plan()
    assert total <= HARD_MAX, total
    hook = next(s["tc"] for s in v2 if s["id"] == "sc03-sh220")
    assert hook <= HOOK_MAX, hook
    json.dump(dict(total=total, version="v2", shots=v2,
                   dropped=[dict(id=s["id"], dur=s["dur"], why=DROP[s["id"]], vo=[v["line"] for v in s["vo"]])
                            for s in v1 if s["id"] in DROP]),
              open(V2, "w"), ensure_ascii=False, indent=1)
    write_md(v1, v2, total)
    print("wrote", V2)


def code(la):
    import re
    return " ".join(sorted(set(re.findall(r"L-\d\d", la or "")))) or "—"


def write_md(v1, v2, total):
    rows, hook = report(v1, v2, total)
    v1t = sum(s["dur"] for s in v1)
    L = ["# S01E01 «The Ninth Sluice» — timed shot list (animatic v2, 21:30 cut)\n",
         "Версия 2.0 · 2026-11-24 · режиссёр-постановщик · статус: **аниматик v2, кандидат в picture lock**\n",
         "Решение директора студии по аниматику v1: пилот — обычная серия ~21–22 мин (цель 21:30, максимум 22:30), "
         "крючок «камень отвечает» до 3:00. Источник: v1 (`spec/shots.json`, генератор `animatic_tools/shots.py`) → "
         "сокращение `animatic_tools/cut_v2.py` → машинная версия `output/S01E01/animatic/spec/shots_v2.json`. "
         "Правила: сюжетные биты, улики (continuity_check §4), FIXED и [ECHO] — не режутся; реплики — только целиком "
         "(существующая озвучка, без перегенерации); кадр не короче своей реплики. Заметки: `direction/S01E01_animatic_v2_notes.md`.\n",
         f"**Итого: {len(v2)} кадров, {fmt(total)}** (v1: {len(v1)} кадров, {fmt(v1t)}; {total - v1t:+.1f} с). "
         f"**Крючок «камень отвечает» (sc03-sh220): {fmt(hook)}.** Эндинг и превью E2 не входят.\n",
         "| Сцена | v1 кадров | v1, с | v2 кадров | v2, с | Δ, с |", "|---|---|---|---|---|---|"]
    for sc, n1, a, n2, b in rows:
        L.append(f"| {sc} | {n1} | {a:.1f} | {n2} | {b:.1f} | {b - a:+.1f} |")
    L.append(f"| **Итого** | {len(v1)} | {v1t:.1f} | {len(v2)} | {total:.1f} | {total - v1t:+.1f} |\n")
    L.append("Колонки: id · ТК v2 · длит. v2 (v1) · класс · LA · ref-ID · кадр (kf = переиспользование) · реплики. "
             "**RESTAGE** — перепостановка (ждёт одобрения главного сценариста).\n")
    by2 = {s["id"]: s for s in v2}
    cur = None
    for s in v1:
        if s["scene"] != cur:
            cur = s["scene"]
            sc2 = [x for x in v2 if x["scene"] == cur]
            L.append(f"\n## {cur} — {fmt(sc2[0]['tc'])}, {sum(x['dur'] for x in sc2):.1f} с "
                     f"(v1 {sum(x['dur'] for x in v1 if x['scene'] == cur):.1f} с), {len(sc2)} кадров\n")
            L.append("| id | ТК | длит. | кл. | LA | ref | кадр | VO |")
            L.append("|---|---|---|---|---|---|---|---|")
        if s["id"] in DROP:
            vo = ", ".join(v["line"] for v in s["vo"]) or "—"
            L.append(f"| ~~{s['id']}~~ | — | ~~{s['dur']:g}~~ | {s['cls']} | — | — | **CUT**: {DROP[s['id']]} | {vo} (cut) |")
            continue
        x = by2[s["id"]]
        d = f"{x['dur']:g}" + (f" ({s['dur']:g})" if x["dur"] != s["dur"] else "")
        frame = ("kf=" + x["reuse"]) if x["reuse"] else ("ref-plate" if s["refplate"] else ("plate" if s["nochar"] else "new"))
        if s["cls"] in "CD" and not x["reuse"]:
            frame += " +end"
        if x.get("restage"):
            frame = "**RESTAGE** " + frame + ": " + x["restage"]
        vo = ", ".join(f"{v['line']} {v['speech']:.1f}s" for v in x["vo"]) or "—"
        refs = (s["refs"] or "—").replace("|", "/")
        L.append(f"| {s['id']} | {fmt(x['tc'])} | {d} | {s['cls']} | {code(s['la'])} | {refs} | {frame} | {vo} |")
    open(f"{ROOT}/studio/direction/shotlists/S01E01_shotlist.md", "w").write("\n".join(L) + "\n")


def la():
    """Render changed / restaged shots into la_v2/ with the v1 renderer ($0). Unchanged shots keep la/<id>.mp4."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import concurrent.futures as cf
    import la as LAmod
    LAmod.LA = f"{A}/la_v2"
    os.makedirs(LAmod.LA, exist_ok=True)
    LAmod.ensure_fx()
    v2 = json.load(open(V2))["shots"]
    todo = [s for s in v2 if s["changed"]]
    only = [x for x in os.environ.get("ONLY", "").split(",") if x]
    if only:
        todo = [s for s in todo if s["id"] in only]
    force = bool(os.environ.get("FORCE"))
    print("LA v2 jobs", len(todo), flush=True)
    with cf.ProcessPoolExecutor(int(os.environ.get("WORKERS", "4"))) as ex:
        for sid, r in ex.map(LAmod.render, todo, [force] * len(todo)):
            if r != "skip":
                print(sid, r, flush=True)


if __name__ == "__main__":
    {"plan": plan, "write": write, "la": la}[sys.argv[1]]()
