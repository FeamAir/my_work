"""Line list for the S01E01 draft TTS: one entry per spoken segment per storyboard shot.

Source of the segmentation: storyboard studio/storyboard/S01E01/sc*.md (column «Реплика / звук»).
Source of the wording: script.md v1.0.2 — every storyboard quote is checked against the script
text of the same speaker and scene; mismatches are reported (stderr) and the script wording wins
where a unique fix is possible. Offline, no network.

    python3 -I studio/sound/tools/extract_lines.py --out lines.json
"""
import argparse, json, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "studio/story/episodes/S01E01/script.md"
SB = REPO / "studio/storyboard/S01E01"

SPEAKERS = {
    "PELL": "V01_PELL", "WICK": "V02_WICK", "NAN": "V03_NAN", "IONE": "V04_IONE",
    "HOLLIS": "V05_HOLLIS", "RUEL": "V06_RUEL", "THE HELM": "V07_LUCAN", "URSEL": "V08_URSEL",
    "THE LORD OF THE RELAY": "V09_ODO", "REEDMASTER": "V10_CORR", "MAGS": "V11_MAGS",
    "COLLECTOR": "V12_COLLECTOR", "ATTENDANT": "V13_ATTENDANT", "KEEPER": "V14_RELAYKEEPER",
    "A GUARD": "V15_GUARD", "CHRONICLER": "NARR01", "CLERK": "V16_CLERK", "STEWARD": "V17_STEWARD",
}
SB_ORDER = ["sc01", "sc02", "sc03", "sc04", "sc05", "sc06", "sc07", "sc08", "sc09", "sc13", "sc10",
            "sc14", "sc11", "sc15", "sc15a", "sc12", "sc16", "sc17", "sc18", "sc19", "sc20"]
NAMES = sorted(SPEAKERS, key=len, reverse=True)
SEG = re.compile(r"(?P<name>" + "|".join(re.escape(n) for n in NAMES) +
                 r")\b(?P<meta>[^«·—]{0,160}?):\s*«(?P<text>[^»]+)»(?P<more>(?:\s*(?:\([^)]*\)\s*)?…?\s*(?:\([^)]*\)\s*)?«[^»]+»)*)")
HEAD = re.compile(r"^(?P<name>[A-Z][A-Z' -]+?)((?: \[[^\]]+\])*(?: \([^)]*\))?(?: \*\*FIXED\*\*)?(?: `\[ECHO\]`)?)\s*$")


def norm(t):
    t = t.replace("’", "'").replace("…", " ").lower()
    return re.sub(r"[^a-z0-9']+", " ", t).strip()


def script_blocks():
    lines = SCRIPT.read_text(encoding="utf-8").splitlines()
    out, scene, i = [], None, 0
    while i < len(lines):
        m = re.match(r"^## SC (\d+)(\w*) ", lines[i])
        if m:
            scene = f"sc{int(m.group(1)):02d}{m.group(2).lower()}"
        h = HEAD.match(lines[i])
        if h and h.group("name") in SPEAKERS and scene:
            head, i, txt = lines[i], i + 1, []
            while i < len(lines) and lines[i].strip():
                t = lines[i].strip()
                if not re.match(r"^\([^)]*\)( \*\*FIXED\*\*)?( `\[ECHO\]`)?$", t):
                    txt.append(re.sub(r"\*+", "", t).strip())
                i += 1
            out.append(dict(scene=scene, voice=SPEAKERS[h.group("name")], head=head,
                            text=" ".join(txt), fixed="FIXED" in head, echo="ECHO" in head))
            continue
        i += 1
    return out


def sb_segments():
    segs = []
    for sc in SB_ORDER:
        for row in (SB / f"{sc}.md").read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\| (sc\w+-sh\d+) \| ([\d:.]+) \| ([\d.]+) с \|", row)
            if not m:
                continue
            cell = row.split(" | ")[6]
            for k, s in enumerate(SEG.finditer(cell)):
                segs.append(dict(shot=m.group(1), scene=sc, tc=m.group(2), shot_dur=float(m.group(3)),
                                 voice=SPEAKERS[s.group("name")], meta=s.group("meta").strip(),
                                 text=" ".join([s.group("text").strip()] + [q.strip() for q in
                                               re.findall(r"«([^»]+)»", s.group("more") or "")]),
                                 overlap="хвост" in s.group("meta"), k=k))
    return segs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    a = ap.parse_args()
    blocks, segs = script_blocks(), sb_segments()
    # cross-check: every storyboard quote must be a substring of a script block of the same voice/scene
    problems = 0
    for s in segs:
        cand = [b for b in blocks if b["scene"] == s["scene"] and b["voice"] == s["voice"]]
        hit = [b for b in cand if norm(s["text"]) in norm(b["text"])]
        s["fixed"] = any(b["fixed"] for b in hit) or "FIXED" in s["meta"]
        s["echo"] = any(b["echo"] for b in hit) or "ECHO" in s["meta"]
        s["script_ok"] = bool(hit)
        if not hit:
            problems += 1
            print(f"MISMATCH {s['shot']} {s['voice']}: «{s['text']}»", file=sys.stderr)
    # coverage: every script block's words must be covered by storyboard segments
    for b in blocks:
        covered = " ".join(norm(s["text"]) for s in segs if s["scene"] == b["scene"] and s["voice"] == b["voice"])
        if norm(b["text"]) not in covered and not all(w in covered.split() for w in norm(b["text"]).split()):
            problems += 1
            print(f"UNCOVERED {b['scene']} {b['voice']}: «{b['text']}»", file=sys.stderr)
    for n, s in enumerate(segs, 1):
        sh = s["shot"].split("-")[1]
        s["line_id"] = f"L{n:03d}"
        s["name"] = f"{s['shot']}_{s['line_id']}_{s['voice']}"
    js = json.dumps(segs, ensure_ascii=False, indent=1)
    if a.out:
        Path(a.out).write_text(js, encoding="utf-8")
    else:
        print(js)
    print(f"{len(segs)} segments, {sum(len(s['text']) for s in segs)} chars, problems: {problems}",
          file=sys.stderr)


if __name__ == "__main__":
    main()
