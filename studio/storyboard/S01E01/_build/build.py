#!/usr/bin/env python3
"""Build the S01E01 storyboard markdown from scene modules.

Run:  python3 -I build.py   (from any directory; paths are absolute)
Writes sc*.md and index.md one level up. No network, no paid calls.
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

ORDER = ['sc01', 'sc02', 'sc03', 'sc04', 'sc05', 'sc06', 'sc07', 'sc08', 'sc09',
         'sc13', 'sc10', 'sc14', 'sc11', 'sc15', 'sc15a', 'sc12', 'sc16', 'sc17',
         'sc18', 'sc19', 'sc20']
SCRIPT_TOTAL = 26 * 60 + 39  # 1599 s, script v1.0.1

# prices, model_choice.md v2.0 §1
NB, NB2, MM_S, K25_S, K3_S, LIP_S = 0.04, 0.08, 0.015, 0.07, 0.14, 0.20
DEFAULT_CLIP = {'B': 6, 'C': 5, 'D': 5, 'E': 5}
VFX_IDS = (['1' + c for c in 'ABCDEFGHIJK'] + ['E-1'] + ['3' + c for c in 'ABCDEF'] +
           ['9' + c for c in 'ABCDEFGHIJKL'] + ['12' + c for c in 'ABCDE'] +
           ['16' + c for c in 'ABCD'] + ['20' + c for c in 'ABCDEFGH'])


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def tc(t):
    m = int(t // 60)
    s = t - m * 60
    return f"{m}:{s:04.1f}"


def esc(x):
    return (x or '—').replace('|', '/').replace('\n', ' ')


def clip_len(s):
    return s.clip or DEFAULT_CLIP.get(s.cls, 0)


def model_str(s, ids):
    pre = ''
    if s.reuse:
        pre = f"kf = {ids[s.reuse]} · "
    if s.clipreuse:
        return pre + f"клип = {ids[s.clipreuse]} (другой отрезок того же дубля)"
    c = clip_len(s)
    img = 'NB edit' if s.nochar else 'NB2 edit'
    if s.cls == 'A':
        if s.refplate:
            return pre + 'плита из референсов → ffmpeg LA'
        if s.nochar:
            return pre + 'NB t2i (аниматик = финал) → ffmpeg LA'
        return pre + 'NB (аним.) → NB2 edit → ffmpeg LA'
    if s.cls == 'B':
        return pre + f"NB (аним.) → {img} → MiniMax H3 {c} с"
    if s.cls == 'C':
        return pre + f"NB (аним.) → {img} → MM черн. → Kling 2.5 TP {c} с"
    if s.cls == 'D':
        return pre + f"NB (аним.) → NB2 edit (start/end) → MM×2 черн. → Kling 3 Pro {c} с"
    if s.cls == 'E':
        return pre + 'NB (аним.) → NB2 edit, рот закрыт → Kling 2.5 TP 5 с → липсинк'
    return pre


def costs(s):
    """expected and ceiling cost, $; split into (anim, final_img, video)."""
    anim = 0.0 if (s.reuse or s.refplate) else 1.3 * NB
    if s.reuse or s.refplate:
        img = 0.0
    elif s.nochar and s.cls == 'A':
        img = 0.0
    elif s.nochar:
        img = 2 * NB
    else:
        img = 2 * NB2
    img += s.l12 * (NB if s.nochar else NB2)
    c = clip_len(s)
    vid = vmax = 0.0
    if not s.clipreuse:
        if s.cls == 'B':
            vid, vmax = 1.5 * MM_S * c, 5 * MM_S * c
        elif s.cls == 'C':
            d = MM_S * max(c, 6)
            vid, vmax = d + 2 * K25_S * c, d + 5 * K25_S * c
        elif s.cls == 'D':
            d = 2 * MM_S * max(c, 6)
            vid, vmax = d + 2.5 * K3_S * c, d + 5 * K3_S * c
        elif s.cls == 'E':
            vid, vmax = 2 * (K25_S * 5 + LIP_S * 5), 5 * (K25_S * 5 + LIP_S * 5)
    return anim, img, vid, anim + img * 1.5 + vmax


def main():
    scenes = []
    for name in ORDER:
        m = load(name)
        scenes.append((name, m.SCENE, m.SHOTS))

    errors, warns = [], []
    t = 0.0
    seq = []
    for name, sc, shots in scenes:
        if abs(t - sc['start']) > 0.01:
            errors.append(f"{name}: start {sc['start']} != running {t}")
        keys = {}
        for i, s in enumerate(shots):
            s.id = f"{name}-sh{(i + 1) * 10:03d}"
            s.scene = name
            s.tc = t
            t += s.dur
            if s.key:
                keys[s.key] = s.id
            seq.append(s)
        sc['_keys'] = keys
        total = sum(s.dur for s in shots)
        sc['_total'] = total
        if abs(total - sc['length']) > 0.01:
            errors.append(f"{name}: sum {total} != length {sc['length']}")
    allkeys = {}
    for name, sc, shots in scenes:
        for k, v in sc['_keys'].items():
            allkeys[k] = v
    for s in seq:
        for attr in ('reuse', 'clipreuse'):
            k = getattr(s, attr)
            if k and k not in allkeys:
                errors.append(f"{s.id}: unknown {attr} key {k}")

    # rules
    lips = [s for s in seq if s.cls == 'E']
    if len(lips) > 5:
        errors.append(f"LIPSYNC-CU: {len(lips)} > 5")
    for s in seq:
        st = bool(s.tags & {'stone', 'cord'})
        if st and 'ring' in s.tags:
            errors.append(f"{s.id}: stone/cord and ring in one shot")
        if 'E-01' in s.refs and ('E-02' in s.refs or 'CH-0005' in s.refs):
            errors.append(f"{s.id}: E-01 with E-02/Ruel in one generation")
        if s.cls in 'BCDE' and not s.clipreuse and s.dur > clip_len(s) + 1.01:
            warns.append(f"{s.id}: {s.dur} с в монтаже > клип {clip_len(s)} с")
    for a, b in zip(seq, seq[1:]):
        if (a.tags & {'stone', 'cord'} and 'ring' in b.tags) or ('ring' in a.tags and b.tags & {'stone', 'cord'}):
            errors.append(f"adjacent stone/ring: {a.id} -> {b.id}")
    scene_tags = []
    for name, sc, shots in scenes:
        tg = set()
        for s in shots:
            tg |= s.tags
        scene_tags.append((name, tg))
    for (n1, t1), (n2, t2) in zip(scene_tags, scene_tags[1:]):
        if (t1 & {'stone', 'cord'} and 'ring' in t2) or ('ring' in t1 and t2 & {'stone', 'cord'}):
            errors.append(f"adjacent scenes stone/ring: {n1} -> {n2}")
    found = {}
    for s in seq:
        if s.vfx:
            for v in s.vfx.split('+'):
                found.setdefault(v.strip(), []).append(s.id)
    missing = [v for v in VFX_IDS if v not in found]
    if missing:
        errors.append(f"VFX IDs missing: {missing}")

    # write scenes
    for name, sc, shots in scenes:
        write_scene(name, sc, shots, allkeys)
    write_index(scenes, seq, found, errors, warns, allkeys)
    print('shots', len(seq), 'total', t, 'errors', len(errors), 'warns', len(warns))
    for e in errors:
        print('ERROR', e)
    for w in warns:
        print('WARN', w)


def write_scene(name, sc, shots, ids):
    L = []
    L.append(f"# S01E01 · {sc['title']}\n")
    L.append(f"Версия 1.0 · 2026-11-22 · раскадровщик · статус: **план, на утверждение режиссёру** · основа: `script.md` v1.0.1\n")
    L.append('```')
    L.append(f"Эпизод: S01E01 · Сцена: {name} · Локация: {sc['loc']} · Время суток: {sc['time']}")
    L.append(f"Персонажи: {sc['chars']}")
    L.append(f"Ось 180° / кто слева-справа: {sc['axis']}")
    L.append(f"Сторона воды / география: {sc['water']}")
    L.append(f"Свет: {sc['light']}")
    L.append(f"Акцент: {sc['accent']} · Настроение: {sc['mood']}")
    L.append(f"Режим: {sc['mode']} · Вертикальные нарезки: {sc.get('vertical', '—')}")
    L.append(f"Хронометраж: {tc(sc['start'])}–{tc(sc['start'] + sc['length'])} · {sc['length']:g} с · кадров: {len(shots)}")
    L.append('```\n')
    if sc.get('notes'):
        L.append('**Постановка и правила сцены**\n')
        for n in sc['notes']:
            L.append(f"- {n}")
        L.append('')
    L.append('## Кадры\n')
    L.append('| № | ТК | Длит. | План | Ракурс / движение | Действие | Реплика / звук (подача) | Кл. | LA | Модель черн. → финал | Карта направления | VFX / V | Статус |')
    L.append('|---|---|---|---|---|---|---|---|---|---|---|---|---|')
    for s in shots:
        vv = ' · '.join(x for x in (s.vfx and f"VFX {s.vfx}", s.v) if x) or '—'
        L.append(f"| {s.id} | {tc(s.tc)} | {s.dur:g} с | {esc(s.plan)} | {esc(s.cam)} | {esc(s.act)} | {esc(s.line)} | {s.cls} | {esc(s.la)} | {esc(model_str(s, ids))} | {esc(s.dirn)} | {vv} | план |")
    L.append('\n## Промпты и референсы\n')
    L.append('`{ID}` раскрывается в ID-блок из `art/pilot_references.md`; модули `{LOWS_DAWN}` и др. — `visual_bible.md` §10.2; STYLE_BASE, негатив и базовый промпт движения добавляются автоматически (`visual_bible.md` §10.1, §10.3, §10.4). Надписи (IX, цифры, ACCOUNT NINE, титры) — только наложением в монтаже.\n')
    L.append('| № | Референсы (ID) | Промпт ключевого кадра (EN) | Промпт движения (EN) |')
    L.append('|---|---|---|---|')
    for s in shots:
        if s.reuse and not s.kf:
            kf = f"= keyframe {ids[s.reuse]}"
        else:
            kf = s.kf
        mot = s.mot
        if s.cls == 'A' and not mot:
            mot = f"— (LA: {s.la})"
        L.append(f"| {s.id} | {esc(s.refs)} | {esc(kf)} | {esc(mot)} |")
    if sc.get('checks'):
        L.append('\n## Связность\n')
        for n in sc['checks']:
            L.append(f"- {n}")
    L.append('')
    with open(os.path.join(OUT, name + '.md'), 'w') as f:
        f.write('\n'.join(L))


def write_index(scenes, seq, found, errors, warns, ids):
    L = []
    L.append('# S01E01 «The Ninth Sluice» — раскадровка, сводка\n')
    L.append('Версия 1.0 · 2026-11-22 · раскадровщик · статус: **план, на утверждение режиссёру** · основа: `story/episodes/S01E01/script.md` v1.0.1\n')
    L.append('Файлы сцен: `sc01.md` … `sc20.md` (порядок монтажа ниже). Генератор: `_build/build.py` (данные кадров — `_build/sc*.py`; пересборка `python3 -I _build/build.py`, без сети). Генерация не запускалась, $0 потрачено.\n')
    total = sum(s.dur for s in seq)
    L.append('## 1. Хронометраж\n')
    L.append(f"- Сумма кадров: **{tc(total)}** ({total:g} с). Сценарий v1.0.1: 26:39 (1599 с). Расхождение: **{total - SCRIPT_TOTAL:+g} с**.")
    L.append(f"- Кадров: **{len(seq)}**, средняя длина кадра **{total / len(seq):.2f} с** (ориентир библии — 3,5 с).")
    L.append('- Не входит: эндинг (главная тема, 1:36 по cue sheet) и превью E2 (≈20 с) — не раскадрованы, см. вопросы в отчёте.\n')
    L.append('## 2. Кадры по сценам и классам\n')
    L.append('| Порядок | Сцена | ТК | Длит. | Кадров | A | B | C | D | E | Ожидаемо, $ |')
    L.append('|---|---|---|---|---|---|---|---|---|---|---|')
    tot = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    sums = [0, 0, 0, 0]
    for i, (name, sc, shots) in enumerate(scenes, 1):
        cnt = {k: sum(1 for s in shots if s.cls == k) for k in tot}
        for k in tot:
            tot[k] += cnt[k]
        exp = sum(sum(costs(s)[:3]) for s in shots)
        L.append(f"| {i} | [{name}]({name}.md) {sc['short']} | {tc(sc['start'])} | {sc['length']:g} с | {len(shots)} | {cnt['A']} | {cnt['B']} | {cnt['C']} | {cnt['D']} | {cnt['E']} | {exp:.2f} |")
    allexp = sum(sum(costs(s)[:3]) for s in seq)
    L.append(f"| | **Итого** | | **{total:g} с** | **{len(seq)}** | **{tot['A']}** | **{tot['B']}** | **{tot['C']}** | **{tot['D']}** | **{tot['E']}** | **{allexp:.2f}** |\n")
    dur = {k: sum(s.dur for s in seq if s.cls == k) for k in tot}
    L.append('Доля хронометража по классам: ' + ' · '.join(f"{k} {dur[k] / total * 100:.0f}% ({dur[k]:g} с)" for k in tot) + '.\n')
    # costs
    anim = sum(costs(s)[0] for s in seq)
    img = sum(costs(s)[1] for s in seq)
    vid = {k: sum(costs(s)[2] for s in seq if s.cls == k) for k in tot}
    ceil = sum(costs(s)[3] for s in seq)
    uniq = sum(1 for s in seq if not s.reuse and not s.refplate)
    finals_img = sum(1 for s in seq if not s.reuse and not s.refplate and not (s.nochar and s.cls == 'A'))
    l12 = sum(s.l12 for s in seq)
    gen = sum(1 for s in seq if s.cls in 'BCDE' and not s.clipreuse)
    L.append('## 3. Смета по `model_choice.md` v2.0 (§1 цены, §5.1 допущения)\n')
    L.append('Допущения: картинка аниматика — 1,3 попытки × NB $0.04; финальный ключевой кадр — 2 попытки (NB2 $0.08 с персонажами, NB $0.04 без); плиты класса A без персонажей идут из аниматика в финал ($0); рисунки L-12 — по одному edit на рисунок; B — 1,5 дубля MiniMax ($0.015/с); C — 1 черновик MM + 2 дубля Kling 2.5 TP ($0.07/с); D — 2 черновика MM + 2,5 дубля Kling 3 Pro ($0.14/с); E — 2 дубля Kling 2.5 TP 5 с + 2 × 5 с липсинка по $0.20/с (верхняя оценка). Повторно используемые ключевые кадры и отрезки одного клипа не тарифицируются.\n')
    L.append('| Статья | Объём | Ожидаемо, $ |')
    L.append('|---|---|---|')
    L.append(f"| Картинки аниматика | {uniq} уникальных кадров × 1,3 | {anim:.2f} |")
    L.append(f"| Финальные ключевые кадры + рисунки L-12 | {finals_img} кадров × 2 попытки + {l12} рисунков | {img:.2f} |")
    for k, label in (('B', 'B · MiniMax H3'), ('C', 'C · Kling 2.5 TP'), ('D', 'D · Kling 3 Pro'), ('E', 'E · K2.5 TP + липсинк')):
        n = sum(1 for s in seq if s.cls == k and not s.clipreuse)
        L.append(f"| {label} | {n} клипов | {vid[k]:.2f} |")
    L.append(f"| **Итого визуал раскадровки** | | **{allexp:.2f}** |")
    L.append(f"| Резерв 20% | | {allexp * 0.2:.2f} |")
    L.append(f"| **С резервом** | | **{allexp * 1.2:.2f}** |")
    L.append(f"| Потолок (все B–E по 5 дублей, картинки ×1,5) | | {ceil:.2f} |\n")
    L.append(f"Не входит: референсы (51 шт., ≈ $65 по `model_choice.md` §5.1 — смета художника), звук и музыка, эндинг и превью. Сравнение с ориентиром `model_choice.md` §5.1 (≈ $262 визуал без референсов и резерва на ~500 кадров) — в отчёте раскадровщика.\n")
    # AF list
    af = [s for s in seq if s.cls == 'A' and (s.nochar or s.refplate) and not s.reuse]
    L.append('## 4. Кадры, которые идут из аниматика напрямую в финал\n')
    L.append('Класс A без персонажей (плиты, вставки предметов, пейзажи) и плиты из листа референсов: картинка аниматика (NB) или реф-плита после приёмки помечается `animatic=final-candidate` и не перегенерируется (`model_choice.md` §3, `animatic.md` шаг 2). Кадры, переиспользующие эти плиты (`kf = …`), наследуют решение.\n')
    L.append(f"Всего: **{len(af)}** уникальных плит.\n")
    by = {}
    for s in af:
        by.setdefault(s.scene, []).append(s.id.split('-')[1] + (' (реф-плита)' if s.refplate else ''))
    for name, sc, shots in scenes:
        if name in by:
            L.append(f"- **{name}**: " + ', '.join(by[name]))
    L.append('')
    # lipsync
    L.append('## 5. Липсинк (LIPSYNC-CU) — 5 из 5\n')
    for s in seq:
        if s.cls == 'E':
            L.append(f"- {s.id} · {tc(s.tc)} · {esc(s.line)}")
    L.append('')
    L.append('## 6. Кадры спецэффектов (`vfx/pilot_vfx_shots.md`, 47 ID)\n')
    L.append('| VFX ID | Кадр(ы) раскадровки |')
    L.append('|---|---|')
    for v in VFX_IDS:
        L.append(f"| {v} | {', '.join(found.get(v, ['НЕТ']))} |")
    L.append('')
    L.append('## 7. Вертикальные нарезки (9:16, объект в центральной трети)\n')
    vs = {}
    for s in seq:
        if s.v:
            vs.setdefault(s.v, []).append(s.id)
    for k in sorted(vs):
        L.append(f"- **{k}**: {vs[k][0]} … {vs[k][-1]} ({len(vs[k])} кадров)")
    L.append('')
    L.append('## 8. Автоматические проверки генератора\n')
    L.append('- сумма длительностей каждой сцены = хронометраж сценария; старт сцены = конец предыдущей;')
    L.append('- LIPSYNC-CU ≤ 5;')
    L.append('- камень/шнурок и перстень: не в одном кадре, не в соседних кадрах, не в соседних сценах; E-01 не подаётся в одну генерацию с E-02 и листом Руэла;')
    L.append('- все 47 ID кадров спецэффектов размещены;')
    L.append('- длительность генерируемого кадра не больше длины клипа + 1 с (иначе предупреждение).\n')
    L.append(f"Результат последней сборки: ошибок **{len(errors)}**, предупреждений **{len(warns)}**.")
    for e in errors:
        L.append(f"- ОШИБКА: {e}")
    for w in warns:
        L.append(f"- предупреждение: {w}")
    L.append('')
    with open(os.path.join(OUT, 'index.md'), 'w') as f:
        f.write('\n'.join(L))


if __name__ == '__main__':
    main()
