"""Build studio/sound/S01E01_vo_durations.md from the CSV twin and the VO manifest (offline)."""
import csv, collections, json
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
rows = list(csv.DictReader((REPO / "studio/sound/S01E01_vo_durations.csv").open(encoding="utf-8")))
man = json.loads((REPO / "output/S01E01/animatic/vo/manifest.json").read_text(encoding="utf-8"))
qa = {v["line_id"]: v for k, v in man.items() if v["kind"] == "main"}
ORDER = ["sc02", "sc03", "sc04", "sc05", "sc06", "sc07", "sc08", "sc09", "sc13", "sc10", "sc14", "sc11", "sc15",
         "sc15a", "sc12", "sc17", "sc18", "sc19", "sc20"]
by = collections.defaultdict(list)
for r in rows:
    by[r["shot_id"].split("-")[0]].append(r)
HEAD = (REPO / "studio/sound/tools/durations_head.md").read_text(encoding="utf-8")
L = [HEAD, "## Сводка по сценам\n",
     "| Сцена | Реплик | Речь, с (сумма) | Кадры с репликами, с | Реплик длиннее своего кадра | Сумма превышений, с |",
     "|---|---|---|---|---|---|"]
tot = [0, 0.0, 0.0, 0, 0.0]
for sc in ORDER:
    rs = [r for r in by[sc] if r["seconds"]]
    if not rs:
        continue
    sp = sum(float(r["seconds"]) for r in rs)
    shots = {r["shot_id"]: float(r["shot_dur_s"]) for r in rs}
    over = [float(r["seconds"]) - float(r["shot_dur_s"]) for r in rs if r["fits_shot"] != "yes"]
    L.append(f"| {sc} | {len(rs)} | {sp:.1f} | {sum(shots.values()):.1f} | {len(over)} | {sum(over):.1f} |")
    for i, x in enumerate((len(rs), sp, sum(shots.values()), len(over), sum(over))):
        tot[i] += x
L.append(f"| **всего** | {tot[0]} | {tot[1]:.1f} | {tot[2]:.1f} | {tot[3]} | {tot[4]:.1f} |\n")
L += ["## Все реплики (порядок монтажа)\n",
      "| line | shot | TC | shot_s | персонаж | текст (EN, сценарий v1.0.2) | seconds | file_s | fit | wpm | альт. дубли, с | QA | файл |",
      "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
flags = []
for sc in ORDER:
    for r in by[sc]:
        alt = [f"{k} {r[c]}" for k, c in (("t2", "alt_t2_s"), ("v4t", "alt_v4turbo_s")) if r.get(c)]
        e = qa.get(r["line_id"], {})
        q = e.get("qa", "")
        if q and q != "ok":
            flags.append((r["line_id"], r["character"], r["text"], e.get("stt", "")))
        fn = r["file"].split("/")[-1] if r["file"] else "— (" + r["note"] + ")"
        L.append(f"| {r['line_id']} | {r['shot_id']} | {r['shot_tc']} | {r['shot_dur_s']} | {r['character']} | "
                 f"{r['text'].replace('|', '/')} | {r['seconds']} | {r['file_seconds']} | {r['fits_shot']} | {r['wpm']} | "
                 f"{', '.join(alt)} | {'ok' if q == 'ok' else ('см. QA' if q else '')} | `{fn}` |")
L += ["", "## QA: автоматическая расшифровка (speech-to-text) расходится с текстом\n",
      "Расшифровка — подсказка, а не истина: британское написание (favours/harbour/dike), цифры (41/30) и редкие имена STT часто «нормализует». Ниже — все расхождения основного дубля; содержательные отмечены в отчёте звукорежиссёра.\n",
      "| line | персонаж | текст | STT услышал |", "|---|---|---|---|"]
for lid, ch, t, s in flags:
    L.append(f"| {lid} | {ch} | {t} | {s} |")
(REPO / "studio/sound/S01E01_vo_durations.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print(len(rows), "rows,", len(flags), "flags")
