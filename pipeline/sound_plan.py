"""План сборки серии: таблица звуков + шот-лист → JSON для pipeline.assemble.

Форматы входа:
  * таблица звуков — studio/sound/sfx_music_workflow.md §2
    (| ID | Сцена/кадр | Таймкод (старт) | Синхро-точка | Тип | Описание (RU) | Промпт (EN) | Длит., с |
     Loop | prompt_influence | Громкость, LUFS | Панорама | Библиотека | Статус |);
    необязательная колонка «Таймкод (конец)» / «Конец» задаёт конец звука явно;
  * шот-лист — studio/direction/shotlist_template.md
    (| № | Сцена | Длит. | План | Камера | Действие | Реплика / звук | … | Статус |).

Что делает:
  * клипы — по строкам шот-листа (№ = scYY-shZZZ), путь <clips-dir>/<pattern>, длина = «Длит.»;
  * таймлайн кадров → проверка таймкодов звуков (кадр, синхро-точка), подстановка старта, если
    таймкод не указан;
  * звуки → дорожки assemble.py: Тип → стем (AMB→amb, HARD/DES→fx, FOLEY→foley, MUS→mus,
    STING→sting, VOX/DX→dx), «Громкость, LUFS» → target_lufs, «Панорама» → pan, Loop → loop;
  * длина петель эмбиента — до конца сцены (по шот-листу) или до следующего эмбиента другой сцены
    + 0,5 с; музыка — до старта следующего трека + 1,5 с (кроссфейд), фейды по mix_plan.md §3.4;
  * реплики: строки DX/VOX таблицы; если их нет — из колонки «Реплика / звук» шот-листа
    (старт = начало кадра + --dx-offset, файл <audio-dir>/<epNN>_dx_<кадр>_<n>.wav) с пометкой;
  * файлы: <audio-dir>/<ID>.wav|.mp3, <audio-dir>/<ID>_*.wav, или имя из колонки «Библиотека»
    в <library-dir>; .wav предпочтительнее .mp3;
  * в JSON также кладётся список generation — что сгенерировать в ElevenLabs (Библиотека = new).

CLI:
    python3 -m pipeline.sound_plan --sound-table studio/sound/ep01_sound_table.md \\
        --shotlist studio/direction/ep01_shotlist.md --out output/ep01/assemble.json
    python3 -m pipeline.assemble output/ep01/assemble.json --dry-run
Выход 0 — план построен (предупреждения в stderr и в поле warnings), 2 — ошибки (--strict: и
предупреждения о ненайденных файлах).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from .assemble import AssembleError, pan_position
from .elevenlabs_client import DEFAULT_MUSIC_MODEL as MUSIC_MODEL
from .elevenlabs_client import DEFAULT_SFX_MODEL as SFX_MODEL

TYPE_TO_STEM = {"AMB": "amb", "HARD": "fx", "DES": "fx", "SFX": "fx", "FX": "fx", "FOLEY": "foley",
                "MUS": "mus", "STING": "sting", "VOX": "dx", "DX": "dx"}
MUS_FADE_IN, MUS_FADE_OUT, MUS_FADE_OUT_LAST, MUS_XFADE = 1.0, 2.5, 4.0, 1.5
AMB_FADE_IN, AMB_FADE_OUT, AMB_XFADE = 0.5, 0.5, 0.5
DX_OFFSET = 0.3
AUDIO_EXT = (".wav", ".mp3", ".flac", ".m4a")


class PlanError(ValueError):
    pass


# ================================================================ markdown ===

def _cells(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    # экранированный \| внутри ячейки не считается разделителем
    parts = re.split(r"(?<!\\)\|", s)
    return [p.strip().replace("\\|", "|") for p in parts]


def _is_sep(line: str) -> bool:
    return bool(re.fullmatch(r"\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*", line))


def md_tables(text: str) -> list[tuple[list[str], list[tuple[int, list[str]]]]]:
    """Все таблицы Markdown вне блоков ```: [(заголовок, [(номер строки, ячейки)])]."""
    tables = []
    lines = text.splitlines()
    in_code = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith("```"):
            in_code = not in_code
            i += 1
            continue
        if not in_code and line.lstrip().startswith("|") and i + 1 < len(lines) and _is_sep(lines[i + 1]):
            header = _cells(line)
            rows = []
            j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                rows.append((j + 1, _cells(lines[j])))
                j += 1
            tables.append((header, rows))
            i = j
            continue
        i += 1
    return tables


def _strip_md(s: str) -> str:
    """Снять обёртку `…` / **…** со всей ячейки (внутренние — не трогать)."""
    s = s.strip()
    for mark in ("**", "`"):
        if len(s) > 2 * len(mark) and s.startswith(mark) and s.endswith(mark) and mark not in s[len(mark):-len(mark)]:
            s = s[len(mark):-len(mark)].strip()
    return s


# ================================================================ values ===

_TC_RE = re.compile(r"(?:(\d+):)?(\d{1,2}):(\d{1,2}(?:[.,]\d+)?)|(\d+(?:[.,]\d+)?)\s*(?:с|s|сек)\b")


def parse_tc(s: str | None) -> tuple[float | None, bool]:
    """'00:07.500' → 7.5; 'TC≈01:02.5' → (62.5, True); '—' → (None, False). Возвращает (сек, оценочный)."""
    if s is None:
        return None, False
    s = _strip_md(s)
    approx = "≈" in s or s.upper().startswith("TC~")
    m = _TC_RE.search(s)
    if not m:
        return None, approx
    if m.group(4) is not None:
        return float(m.group(4).replace(",", ".")), approx
    h = int(m.group(1)) if m.group(1) else 0
    mm, ss = int(m.group(2)), float(m.group(3).replace(",", "."))
    if m.group(1) is None:   # ММ:СС.мс
        return mm * 60 + ss, approx
    return h * 3600 + mm * 60 + ss, approx


def parse_number(s: str | None) -> float | None:
    """'−32' → -32.0; '4 с' → 4.0; '−22…−16' → -19.0 (середина); '—' → None."""
    if s is None:
        return None
    s = _strip_md(s).replace("−", "-").replace("–", "-").replace(",", ".")
    nums = re.findall(r"-?\d+(?:\.\d+)?", s)
    if not nums:
        return None
    vals = [float(n) for n in nums[:2]]
    if len(vals) == 2 and ("…" in s or "..." in s or re.search(r"\d\s*-\s*-?\d", s)):
        return round(sum(vals) / 2, 2)
    return vals[0]


def parse_bool(s: str | None) -> bool:
    return _strip_md(s or "").lower() in ("да", "yes", "y", "true", "1", "+", "loop")


_SHOT_RE = re.compile(r"sc\s*(\d+)\s*[-/_ ]\s*sh\s*(\d+)", re.I)
_SCENE_RE = re.compile(r"sc\s*(\d+)", re.I)


def parse_scene_shot(s: str | None) -> tuple[int | None, int | None]:
    s = _strip_md(s or "")
    m = _SHOT_RE.search(s)
    if m:
        return int(m.group(1)), int(m.group(2))
    m = _SCENE_RE.search(s)
    return (int(m.group(1)), None) if m else (None, None)


def shot_key(scene: int, shot: int) -> str:
    return f"sc{scene:02d}-sh{shot:03d}"


# ================================================================ shotlist ===

@dataclass
class Shot:
    id: str
    scene: int
    shot: int
    duration: float
    start: float = 0.0
    dialog: list[tuple[str, str]] = field(default_factory=list)   # (персонаж, текст)
    line: int = 0

    @property
    def end(self) -> float:
        return self.start + self.duration


@dataclass
class ShotLine:
    """Строка таблицы реплик шот-листа: | TC (≈) | Кадр | Персонаж | Реплика | … |."""
    start: float
    end: float | None
    shot: str
    character: str
    text: str
    line: int


def _col(header: list[str], *keys: str, exclude: tuple[str, ...] = ()) -> int | None:
    norm = [h.lower().replace("ё", "е") for h in header]
    for key in keys:
        for i, h in enumerate(norm):
            if key in h and not any(x in h for x in exclude):
                return i
    return None


_DIALOG_RE = re.compile(r"([^:;«»<>]{1,60}?)\s*(?:\([^)]*\))?\s*:\s*«([^»]+)»")


def parse_dialog(cell: str) -> list[tuple[str, str]]:
    """'Мира (тихо, себе): «Ну вот.»<br>Кай: «Да.»' → [('Мира', 'Ну вот.'), ('Кай', 'Да.')]."""
    out = []
    for m in _DIALOG_RE.finditer(cell.replace("<br>", "; ").replace("<br/>", "; ")):
        who = re.sub(r"\(.*$", "", m.group(1)).strip(" ;,.-—")
        who = re.split(r"[;.]\s*", who)[-1].strip()
        if who.lower() in ("музыка", "шумы", "звук", "sfx", "music"):
            continue
        out.append((who, m.group(2).strip()))
    return out


def parse_shotlist(text: str) -> tuple[list[Shot], list[str]]:
    shots, _lines, warnings = parse_shotlist_full(text)
    return shots, warnings


def parse_shotlist_full(text: str) -> tuple[list[Shot], list[ShotLine], list[str]]:
    """Кадры (таблицы с колонками № и Длит.) и таблица реплик (TC, Кадр, Персонаж, Реплика), если есть."""
    shots: list[Shot] = []
    lines: list[ShotLine] = []
    warnings: list[str] = []
    for header, rows in md_tables(text):
        c_id, c_dur = _col(header, "№"), _col(header, "длит")
        c_char, c_text, c_tc = _col(header, "персонаж"), _col(header, "реплика"), _col(header, "tc", "таймкод")
        c_shot = _col(header, "кадр")
        if c_id is None and c_char is not None and c_text is not None and c_tc is not None:
            for lineno, cells in rows:
                rng = parse_tc_ranges(cells[c_tc] if c_tc < len(cells) else "")
                if not rng or rng[0][0] is None:
                    continue
                lines.append(ShotLine(start=rng[0][0], end=rng[0][1],
                                      shot=_strip_md(cells[c_shot]) if c_shot is not None and c_shot < len(cells) else "",
                                      character=_strip_md(cells[c_char]), text=_strip_md(cells[c_text]),
                                      line=lineno))
            continue
        if c_id is None or c_dur is None:
            continue
        c_dlg = _col(header, "реплика")
        for lineno, cells in rows:
            if c_id >= len(cells):
                continue
            sc, sh = parse_scene_shot(cells[c_id])
            if sc is None or sh is None:
                continue
            dur = parse_number(cells[c_dur]) if c_dur < len(cells) else None
            if not dur or dur <= 0:
                warnings.append(f"шот-лист, строка {lineno}: у кадра {cells[c_id]} нет длительности — пропущен")
                continue
            dlg = parse_dialog(cells[c_dlg]) if c_dlg is not None and c_dlg < len(cells) else []
            shots.append(Shot(id=shot_key(sc, sh), scene=sc, shot=sh, duration=dur, dialog=dlg, line=lineno))
    seen: dict[str, Shot] = {}
    uniq: list[Shot] = []
    for s in shots:
        if s.id in seen:
            warnings.append(f"шот-лист: кадр {s.id} встречается дважды (строки {seen[s.id].line} и {s.line}) "
                            f"— взят первый")
            continue
        seen[s.id] = s
        uniq.append(s)
    t = 0.0
    for s in uniq:
        s.start = round(t, 3)
        t += s.duration
    return uniq, lines, warnings


# ============================================================== sound table ===

def parse_tc_ranges(s: str | None) -> list[tuple[float | None, float | None]]:
    """'0:04.0–0:11.3' → [(4.0, 11.3)]; '0:00–0:25.5; 1:14.5–1:35.5' → два отрезка; '00:07.5' → [(7.5, None)]."""
    out: list[tuple[float | None, float | None]] = []
    for part in re.split(r"[;\n]", _strip_md(s or "")):
        tcs = [m for m in _TC_RE.finditer(part) if m.group(4) is None]
        if not tcs:
            continue
        a, _ = parse_tc(tcs[0].group(0))
        b = parse_tc(tcs[1].group(0))[0] if len(tcs) > 1 else None
        out.append((a, b))
    return out


@dataclass
class Sound:
    id: str
    stem: str
    type: str
    scene: int | None
    shot: int | None
    start: float | None
    start_approx: bool
    end: float | None
    sync: float | None
    desc: str
    prompt: str
    gen_duration: float | None
    loop: bool
    prompt_influence: float | None
    lufs: float | None
    pan: str | None
    library: str                 # имя файла из колонки «Библиотека» ('' если нет)
    status: str
    line: int
    scope: str = ""              # new | lib | ep | ''
    ranges: list[tuple[float | None, float | None]] = field(default_factory=list)
    scenes: list[int] = field(default_factory=list)
    lufs_by_scene: dict[int, float] = field(default_factory=dict)
    character: str = ""
    tts_text: str = ""
    notes: str = ""
    reuse: list[tuple[str, float | None]] = field(default_factory=list)   # (ID исходника, старт)
    gain_db: float = 0.0
    filter: str = ""
    fade_in: float | None = None
    fade_out: float | None = None
    pan_moving: bool = False
    cut_at: float | None = None  # «обрезка в 2:45.0» — жёсткий срез


SOUND_COLS = {
    "id": (("id",), ()),
    "scene": (("сцена", "сц"), ("текст", "сценари")),
    "end": (("конец", "end"), ()),
    "start": (("таймкод", "tc"), ("конец", "end")),
    "sync": (("синхро",), ()),
    "type": (("тип",), ()),
    "desc": (("описание", "локация", "слот", "подача"), ()),
    "prompt": (("промпт", "хвост"), ("influence",)),
    "tts": (("текст для tts",), ()),
    "character": (("персонаж",), ()),
    "dur": (("длит", "генерация"), ()),
    "loop": (("loop", "петля"), ()),
    "pi": (("prompt_influence", "influence", "p_inf"), ()),
    "lufs": (("громкость", "lufs"), ()),
    "pan": (("панорама", "пан"), ()),
    "lib": (("библиотека", "библ", "файл"), ()),
    "status": (("статус",), ()),
    "notes": (("вход / выход", "прим", "вход"), ()),
}
_ID_STEM_RE = re.compile(r"(?:^|_)(dx|vox|amb|mus|music|sting|foley|hard|des|sfx)(?:_|$)", re.I)
_REF_ID_RE = re.compile(r"\b((?:lib|ep\d+)_[A-Za-z0-9_-]*[A-Za-z0-9])`?\s*(?:\((\d{1,2}:\d{2}(?:[.,]\d+)?)\))?")
_LUFS_IN_TEXT_RE = re.compile(r"([−-]\d+(?:[.,]\d+)?(?:\s*…\s*[−-]\d+(?:[.,]\d+)?)?)\s*LUFS")
_SCENE_LUFS_RE = re.compile(r"\(\s*sc(\d+)((?:/\d+)*)\s*:\s*([−-]\d+(?:[.,]\d+)?)\s*\)")
_SEC_RE = r"(\d+(?:[.,]\d+)?)\s*с\b"


def _fades_from_notes(notes: str) -> tuple[float | None, float | None, list[str]]:
    """Фейды из колонки «Вход / выход»: 'вход фейдом 1.5 с; выход — кроссфейд 1 с', 'срез 30 мс'…"""
    fin = fout = None
    flags: list[str] = []
    for part in re.split(r";", notes.replace("**", "")):
        p = part.lower()
        if "вход" in p and fin is None:
            m = re.search(r"(?:фейд\w*|с тишины)\s*" + _SEC_RE, p)
            if m:
                fin = float(m.group(1).replace(",", "."))
        m = re.search(r"(?:кроссфейд\w*|фейд-аут|выход\s+фейдом)\s*" + _SEC_RE, p)
        if m:
            fout = float(m.group(1).replace(",", "."))
        m = re.search(r"(?:срез|обрыв)[^;]*?(\d+)\s*мс", p)
        if m:
            fout = int(m.group(1)) / 1000
        elif ("обрыв" in p or "срез" in p) and fout is None:
            fout = 0.01
        if "ducking" in p and "db" in p:
            flags.append("ducking-override")
    return fin, fout, flags


def parse_sound_table(text: str) -> tuple[list[Sound], list[str]]:
    """Все таблицы с колонками ID и таймкодом (или Тип): шаблонная таблица sfx_music_workflow.md §2
    и раздельные таблицы DX / AMB / SFX / MUS, как в ep01_sound_table.md."""
    sounds: list[Sound] = []
    warnings: list[str] = []
    for header, rows in md_tables(text):
        cols = {k: _col(header, *keys, exclude=ex) for k, (keys, ex) in SOUND_COLS.items()}
        if cols["id"] is None or (cols["type"] is None and cols["start"] is None):
            continue
        header_approx = cols["start"] is not None and "≈" in header[cols["start"]]

        def cell(cells: list[str], k: str) -> str:
            i = cols[k]
            return cells[i] if i is not None and i < len(cells) else ""

        for lineno, cells in rows:
            sid = _strip_md(cell(cells, "id")).strip("`")
            if not sid or sid in ("—", "-"):
                continue
            typ = _strip_md(cell(cells, "type")).upper()
            if not typ:
                m = _ID_STEM_RE.search(sid)
                typ = m.group(1).upper() if m else ""
                typ = {"MUSIC": "MUS"}.get(typ, typ)
            loop_detail = typ in ("AMB-D", "AMB_D")
            if loop_detail:
                typ = "AMB"
            stem = TYPE_TO_STEM.get(typ)
            if not stem:
                hint = (" — огибающая громкости стема (приём) в assemble.py не поддерживается, нужна "
                        "ручная автоматизация") if typ in ("ПРИЁМ", "ПРИЕМ") else ""
                warnings.append(f"таблица звуков, строка {lineno}: {sid}: тип {typ or '?'!r} не распознан — "
                                f"пропущен{hint}")
                continue
            tc_cell = cell(cells, "start")
            ranges = parse_tc_ranges(tc_cell)
            approx = header_approx or "≈" in tc_cell
            end, _ = parse_tc(cell(cells, "end")) if cols["end"] is not None else (None, False)
            sync, _ = parse_tc(cell(cells, "sync"))
            scenes = [int(x) for x in re.findall(r"sc\s*(\d+)", cell(cells, "scene"), re.I)]
            sc, sh = parse_scene_shot(cell(cells, "scene"))
            # панорама: 'L30→C' — автопанорама не поддерживается, берём начальную позицию
            pan_raw = _strip_md(cell(cells, "pan"))
            pan_moving = "→" in pan_raw
            pan = pan_raw.split("→")[0].strip() or None
            if pan in ("—", "-"):
                pan = None
            try:
                pan_position(pan)
            except AssembleError:
                warnings.append(f"таблица звуков, строка {lineno}: {sid}: панорама {pan!r} не распознана — центр")
                pan = "C"
            # уровень: колонка LUFS или «−14 LUFS» в примечании/подаче (DX)
            lufs_cell = cell(cells, "lufs")
            lufs = parse_number(lufs_cell)
            notes = _strip_md(cell(cells, "notes"))
            if lufs is None:
                m = _LUFS_IN_TEXT_RE.search(notes + " " + cell(cells, "desc"))
                if m:
                    lufs = parse_number(m.group(1))
            by_scene: dict[int, float] = {}
            for m in _SCENE_LUFS_RE.finditer(lufs_cell):
                v = parse_number(m.group(3))
                first = int(m.group(1))
                by_scene[first] = v
                for extra in re.findall(r"/(\d+)", m.group(2)):
                    by_scene[int(extra)] = v
            # библиотека: 'lib (`lib_mus_l1-sora_v1`)' → имя файла; 'lib'/'ep'/'new' → область
            lib_cell = cell(cells, "lib")
            m = re.search(r"`([^`]+)`", lib_cell)
            library = m.group(1) if m else ""
            scope_raw = _strip_md(re.sub(r"\(.*?\)", "", lib_cell)).lower()
            if not library and scope_raw not in ("new", "lib", "ep", "", "—", "-"):
                library, scope_raw = _strip_md(lib_cell), "lib"
            prompt = _strip_md(cell(cells, "prompt"))
            snd = Sound(
                id=sid, stem=stem, type=typ, scene=sc, shot=sh,
                start=ranges[0][0] if ranges else None, start_approx=approx,
                end=end if end is not None else (ranges[0][1] if len(ranges) == 1 else None),
                sync=sync, desc=_strip_md(cell(cells, "desc")), prompt=prompt.strip("`"),
                gen_duration=parse_number(cell(cells, "dur")),
                loop=parse_bool(cell(cells, "loop")) and not loop_detail,
                prompt_influence=parse_number(cell(cells, "pi")), lufs=lufs, pan=pan, library=library,
                status=_strip_md(cell(cells, "status")).lower(), line=lineno, scope=scope_raw,
                ranges=ranges, scenes=scenes, lufs_by_scene=by_scene,
                character=_strip_md(cell(cells, "character")), tts_text=_strip_md(cell(cells, "tts")),
                notes=notes, pan_moving=pan_moving)
            # переиспользование: '= ep01_sfx_13 (…, −4 dB)', '= ep01_sfx_16 (2:37.0) + ep01_sfx_17 (2:39.6)'
            if prompt.startswith("="):
                for rm in _REF_ID_RE.finditer(prompt):
                    snd.reuse.append((rm.group(1), parse_tc(rm.group(2))[0] if rm.group(2) else None))
                g = re.search(r"([−-]\d+(?:[.,]\d+)?)\s*dB", prompt)
                if g:
                    snd.gain_db = parse_number(g.group(1))
                lp = re.search(r"lowpass\s*(\d+)\s*Гц", prompt, re.I)
                hp = re.search(r"highpass\s*(\d+)\s*Гц", prompt, re.I)
                snd.filter = ",".join(f"{n}=f={v.group(1)}" for n, v in (("lowpass", lp), ("highpass", hp)) if v)
                cut = re.search(r"обрезка\s+в\s+(\d{1,2}:\d{2}(?:[.,]\d+)?)", prompt)
                if cut:
                    snd.cut_at = parse_tc(cut.group(1))[0]
                    snd.fade_out = 0.01
                if not snd.reuse:
                    warnings.append(f"{sid}: «{prompt[:40]}…» — не найден ID исходника для переиспользования")
            if stem == "mus" or "вход" in notes.lower():
                fin, fout, flags = _fades_from_notes(notes)
                snd.fade_in = fin if fin is not None else snd.fade_in
                snd.fade_out = fout if fout is not None else snd.fade_out
                if "ducking-override" in flags:
                    warnings.append(f"{sid}: особая глубина ducking для одного трека — assemble.py приглушает "
                                    f"стем MUS целиком; нужен отдельный стем или ручная правка")
            if pan_moving:
                warnings.append(f"{sid}: автопанорама {pan_raw!r} не поддерживается — взята начальная позиция {pan}")
            if len(ranges) > 1 and (sync is not None):
                warnings.append(f"{sid}: несколько отрезков и синхро-точка — синхро проверяется по первому")
            sounds.append(snd)
    ids: dict[str, int] = {}
    for s in sounds:
        if s.id in ids:
            warnings.append(f"таблица звуков: ID {s.id} повторяется (строки {ids[s.id]} и {s.line})")
        ids.setdefault(s.id, s.line)
    return sounds, warnings


# =================================================================== files ===

def _version(p: Path) -> int:
    m = re.search(r"_v(\d+)$", p.stem)
    return int(m.group(1)) if m else 0


def find_audio(sound_id: str, library: str, audio_dir: Path, library_dir: Path) -> Path | None:
    """Файл звука: по имени из колонки «Библиотека» или по ID (в audio-dir и library-dir);
    точное имя, иначе <имя>_*.<ext> с максимальной версией _vN; .wav предпочтительнее."""
    names: list[tuple[Path, str]] = []
    lib = library.strip()
    if lib and lib.lower() not in ("new", "lib", "ep", "—", "-", "нет"):
        stem = Path(lib).stem if Path(lib).suffix.lower() in AUDIO_EXT else lib
        names += [(library_dir, stem), (audio_dir, stem)]
    names += [(audio_dir, sound_id), (library_dir, sound_id)]
    for d, stem in names:
        for ext in AUDIO_EXT:
            p = d / f"{stem}{ext}"
            if p.is_file():
                return p
        cands = [p for ext in AUDIO_EXT for p in d.glob(f"{stem}_*{ext}") if p.is_file()]
        if cands:
            cands.sort(key=lambda p: (_version(p), p.suffix == ".wav"), reverse=True)
            return cands[0]
    return None


# ==================================================================== plan ===

def _rel(p: Path, base: Path) -> str:
    try:
        return os.path.relpath(p.resolve(), base.resolve())
    except ValueError:
        return str(p.resolve())


def _norm_text(s: str) -> str:
    return re.sub(r"[^a-zа-я0-9]", "", s.lower().replace("ё", "е"))


@dataclass
class _Placed:
    snd: Sound
    start: float
    end: float | None
    n: int          # номер отрезка (для нескольких TC в одной строке)
    total: int


def build_spec(sounds: list[Sound], shots: list[Shot], *, episode: str, audio_dir: Path,
               library_dir: Path, clips_dir: Path, clip_pattern: str = "{shot}.mp4",
               spec_dir: Path, output: Path | None = None, dialog_from_shotlist: str = "auto",
               dx_offset: float = DX_OFFSET, approved_only: bool = False,
               shot_lines: list[ShotLine] | None = None, dx_tc_from_shotlist: bool = False
               ) -> tuple[dict, list[str]]:
    """Собрать dict для assemble.py. Возвращает (spec, предупреждения)."""
    warnings: list[str] = []
    by_key = {(s.scene, s.shot): s for s in shots}
    scenes: dict[int, tuple[float, float]] = {}
    for s in shots:
        a, b = scenes.get(s.scene, (s.start, s.end))
        scenes[s.scene] = (min(a, s.start), max(b, s.end))
    D = round(sum(s.duration for s in shots), 3) if shots else None

    def scene_at(t: float) -> int | None:
        for sc, (a, b) in scenes.items():
            if a <= t < b:
                return sc
        return None

    def find_shot(sound: Sound) -> Shot | None:
        if sound.scene is None or sound.shot is None or not shots:
            return None
        sh = by_key.get((sound.scene, sound.shot))
        if sh is None and (sound.scene, sound.shot * 10) in by_key:
            sh = by_key[(sound.scene, sound.shot * 10)]
            warnings.append(f"{sound.id}: кадр sh{sound.shot:02d} сопоставлен с {sh.id} "
                            f"(нумерация шот-листа с шагом 10)")
        if sh is None:
            warnings.append(f"{sound.id}: кадр sc{sound.scene:02d}/sh{sound.shot} не найден в шот-листе")
        return sh

    # --- клипы
    clips = []
    missing_clips = 0
    for s in shots:
        name = clip_pattern.format(shot=s.id, ep=episode, scene=f"sc{s.scene:02d}", n=s.shot)
        path = clips_dir / name
        if not path.is_file():
            missing_clips += 1
        clips.append({"path": _rel(path, spec_dir), "duration": s.duration, "shot": s.id})
    if missing_clips:
        warnings.append(f"клипов нет на диске: {missing_clips} из {len(shots)} ({clips_dir}/{clip_pattern}) — "
                        f"assemble упадёт, пока их не сгенерируют")
    if not shots:
        warnings.append("шот-лист не задан или пуст: clips = [] — assemble.py требует клипы")

    # --- реплики: сверка таймкодов с таблицей реплик шот-листа
    if shot_lines:
        used: set[int] = set()
        for snd in (x for x in sounds if x.stem == "dx" and (x.tts_text or x.character)):
            key = _norm_text(snd.tts_text or snd.desc)[:12]
            match = next((i for i, ln in enumerate(shot_lines) if i not in used and key and
                          (_norm_text(ln.text).startswith(key) or key.startswith(_norm_text(ln.text)[:12]))), None)
            if match is None:
                warnings.append(f"{snd.id}: реплика не найдена в таблице реплик шот-листа")
                continue
            used.add(match)
            ln = shot_lines[match]
            if snd.start is not None and abs(ln.start - snd.start) > 0.5:
                if dx_tc_from_shotlist:
                    warnings.append(f"{snd.id}: TC {snd.start:.1f} → {ln.start:.1f} с по шот-листу ({ln.shot})")
                    snd.ranges = [(ln.start, None)]
                    snd.start, snd.end = ln.start, None
                else:
                    warnings.append(f"{snd.id}: TC в таблице звуков {snd.start:.1f} с, в шот-листе {ln.start:.1f} с "
                                    f"({ln.shot}) — расхождение {ln.start - snd.start:+.1f} с")
        for i, ln in enumerate(shot_lines):
            if i not in used:
                warnings.append(f"реплика шот-листа {ln.start:.1f} с ({ln.character}: «{ln.text[:30]}») "
                                f"не сопоставлена со строкой DX таблицы звуков")

    # --- старты звуков
    active = [x for x in sounds if not (approved_only and x.status != "утверждено")]
    if approved_only and len(active) < len(sounds):
        warnings.append(f"--approved-only: пропущено {len(sounds) - len(active)} звуков не в статусе «утверждено»")
    placed: list[_Placed] = []
    for snd in active:
        if snd.status == "перегенерировать":
            warnings.append(f"{snd.id}: статус «перегенерировать» — файл может быть устаревшим")
        shot = find_shot(snd)
        ranges = snd.ranges or [(None, None)]
        if len(ranges) == 1:
            ranges = [(snd.start, snd.end)]
        for n, (start, end) in enumerate(ranges, 1):
            if start is None:
                if shot is not None:
                    start = shot.start
                    warnings.append(f"{snd.id}: таймкода нет — старт по началу кадра {shot.id} ({start:.3f} с)")
                elif snd.scene in scenes:
                    start = scenes[snd.scene][0]
                    warnings.append(f"{snd.id}: таймкода нет — старт по началу сцены sc{snd.scene:02d}")
                else:
                    warnings.append(f"{snd.id}: нет ни таймкода, ни кадра в шот-листе — пропущен")
                    continue
            if shot is not None and not (shot.start - 1.0 <= start <= shot.end + 0.05):
                warnings.append(f"{snd.id}: старт {start:.3f} с вне кадра {shot.id} "
                                f"({shot.start:.3f}–{shot.end:.3f} с)")
            elif shot is None and snd.scene in scenes and snd.shot is None and len(set(snd.scenes)) <= 1:
                a, b = scenes[snd.scene]
                if not (a - 1.0 <= start <= b):
                    warnings.append(f"{snd.id}: старт {start:.3f} с вне сцены sc{snd.scene:02d} ({a:.3f}–{b:.3f} с)")
            if n == 1 and snd.sync is not None:
                hi = (end if end is not None else start + (snd.gen_duration or 30))
                if not (start <= snd.sync <= hi):
                    warnings.append(f"{snd.id}: синхро-точка {snd.sync:.3f} с вне звука ({start:.3f}–{hi:.3f} с)")
            if D is not None and start >= D:
                warnings.append(f"{snd.id}: старт {start:.3f} с после конца серии по шот-листу ({D:.3f} с)")
            placed.append(_Placed(snd, start, end, n, len(ranges)))
    approx_n = sum(1 for p in placed if p.snd.start_approx)
    if approx_n:
        warnings.append(f"таймкоды оценочные (TC≈) у {approx_n} дорожек — сверить после монтажа")

    # --- реплики из шот-листа
    has_dx = any(p.snd.stem == "dx" for p in placed)
    use_shot_dialog = dialog_from_shotlist == "yes" or (dialog_from_shotlist == "auto" and not has_dx)
    dx_rows: list[dict] = []
    if use_shot_dialog:
        for shot in shots:
            for n, (who, text) in enumerate(shot.dialog, 1):
                did = f"{episode}_dx_{shot.id}_{n}"
                path = find_audio(did, "", audio_dir, library_dir)
                if path is None:
                    warnings.append(f"{did}: файла реплики нет ({audio_dir}/{did}.wav)")
                    path = audio_dir / f"{did}.wav"
                if n > 1:
                    warnings.append(f"{did}: вторая и далее реплика в кадре {shot.id} — старт тоже по началу "
                                    f"кадра, поправьте таймкод")
                dx_rows.append({"id": did, "stem": "dx", "path": _rel(path, spec_dir),
                                "start": round(shot.start + dx_offset, 3), "target_lufs": -16, "pan": "C",
                                "meta": {"character": who, "text": text, "source": "shotlist", "estimated": True}})

    # --- дорожки
    tracks: list[dict] = []
    gen: list[dict] = []
    missing_audio: list[str] = []
    placed.sort(key=lambda p: p.start)
    amb_bases = [p for p in placed if p.snd.stem == "amb" and p.snd.loop]
    mus = [p for p in placed if p.snd.stem == "mus"]
    last_scene_start = scenes[max(scenes)][0] if scenes else None
    for p in placed:
        snd, start = p.snd, p.start
        sources = snd.reuse or [(snd.id, None)]
        for k, (src_id, src_tc) in enumerate(sources):
            t_start = src_tc if src_tc is not None else start
            lib_name = snd.library if not snd.reuse else ""
            path = find_audio(src_id, lib_name, audio_dir, library_dir)
            if path is None:
                missing_audio.append(src_id)
                guess = (library_dir / f"{lib_name}.wav") if lib_name else (
                    (library_dir if src_id.startswith("lib_") or snd.scope == "lib" else audio_dir) / f"{src_id}.wav")
                path = guess
            tid = snd.id + (f"__{p.n}" if p.total > 1 else "") + (f"__{src_id}" if len(sources) > 1 else "")
            t: dict = {"id": tid, "stem": snd.stem, "path": _rel(path, spec_dir), "start": round(t_start, 3)}
            lufs = snd.lufs
            if snd.lufs_by_scene:
                sc_here = scene_at(t_start + 0.6) if scenes else None
                if sc_here in snd.lufs_by_scene:
                    lufs = snd.lufs_by_scene[sc_here]
            if lufs is not None:
                t["target_lufs"] = lufs
            if snd.pan:
                t["pan"] = snd.pan
            if snd.loop:
                t["loop"] = True
            if snd.gain_db and lufs is None:
                t["gain_db"] = snd.gain_db
            elif snd.gain_db:
                t.setdefault("meta_gain_note", f"{snd.gain_db:+g} dB из промпта не применён: уровень задан "
                                               f"колонкой LUFS ({lufs:g})")
            if snd.filter:
                t["filter"] = snd.filter
            end = p.end
            if snd.stem == "amb" and snd.loop:
                t["fade_in"], t["fade_out"] = (1.0 if t_start == 0 else AMB_FADE_IN), AMB_FADE_OUT
                if end is None and snd.scene in scenes and len(set(snd.scenes)) <= 1:
                    end = scenes[snd.scene][1]
                elif end is None:
                    nxt = next((q.start for q in amb_bases if q.start > start and q.snd.scene != snd.scene), None)
                    end = nxt + AMB_XFADE if nxt is not None else None
            elif snd.stem == "mus":
                t["fade_in"] = snd.fade_in if snd.fade_in is not None else MUS_FADE_IN
                nxt = next((q.start for q in mus if q.start > start), None)
                if end is None and nxt is not None:
                    end = nxt + MUS_XFADE
                    t["fade_out"] = snd.fade_out if snd.fade_out is not None else MUS_XFADE
                else:
                    if end is None and snd.gen_duration and not snd.loop:
                        end = start + snd.gen_duration
                    # 3–5 с — только если трек доходит до последней сцены серии (mix_plan.md §3.4)
                    reaches_last = end is None or (last_scene_start is not None and end > last_scene_start)
                    default_out = MUS_FADE_OUT_LAST if (nxt is None and reaches_last and scenes) else MUS_FADE_OUT
                    t["fade_out"] = snd.fade_out if snd.fade_out is not None else default_out
            else:
                if snd.fade_in is not None:
                    t["fade_in"] = snd.fade_in
                if snd.fade_out is not None:
                    t["fade_out"] = snd.fade_out
            if snd.stem == "dx":
                end = None           # длина реплики — по факту TTS, TC-конец в таблице оценочный
            if len(sources) > 1:
                end = None           # составной повтор: каждый исходник целиком
            if snd.cut_at is not None:
                end = snd.cut_at
            if end is not None:
                if D is not None:
                    end = min(end, D)
                if end <= t_start:
                    warnings.append(f"{tid}: конец {end:.3f} ≤ старта {t_start:.3f} — длина не ограничена")
                    end = None
                else:
                    t["end"] = round(end, 3)
            if end is not None:
                for key in ("fade_in", "fade_out"):
                    if key in t:
                        t[key] = min(t[key], round((end - t_start) / 3, 2))
            t["meta"] = {"type": snd.type, "desc": snd.desc, "status": snd.status, "line": snd.line,
                         "scene_shot": f"sc{snd.scene:02d}" + (f"/sh{snd.shot}" if snd.shot is not None else "")
                         if snd.scene is not None else None}
            if snd.character:
                t["meta"]["character"] = snd.character
            if "meta_gain_note" in t:
                t["meta"]["gain_note"] = t.pop("meta_gain_note")
            if snd.reuse:
                t["meta"]["reuse_of"] = src_id
            tracks.append(t)

        # что генерировать (одна запись на строку таблицы, а не на отрезок)
        if p.n != 1 or snd.reuse:
            continue
        if find_audio(snd.id, snd.library, audio_dir, library_dir):
            continue                     # файл уже есть — генерировать не нужно
        if snd.stem == "dx" or snd.prompt.upper().startswith("TTS"):
            g = {"id": snd.id, "kind": "tts", "character": snd.character, "text": snd.tts_text or snd.prompt,
                 "status": snd.status}
        elif snd.stem == "mus" or (snd.stem == "sting" and snd.prompt.lower().startswith("см.")):
            g = {"id": snd.id, "kind": "music", "model_id": MUSIC_MODEL, "prompt": snd.prompt,
                 "duration_seconds": snd.gen_duration, "file": snd.library or None, "status": snd.status}
        else:
            g = {"id": snd.id, "kind": "sfx", "model_id": SFX_MODEL, "prompt": snd.prompt,
                 "duration_seconds": snd.gen_duration, "loop": snd.loop,
                 "prompt_influence": snd.prompt_influence if snd.prompt_influence is not None else 0.3,
                 "status": snd.status}
            if snd.gen_duration is not None and not (0.5 <= snd.gen_duration <= 30):
                warnings.append(f"{snd.id}: длительность SFX {snd.gen_duration} с вне 0.5–30 с (лимит API)")
        if g["kind"] != "tts" and (not snd.prompt or snd.prompt.lower().startswith("см.")):
            warnings.append(f"{snd.id}: промпт — ссылка на другой документ ({snd.prompt[:50]!r}), "
                            f"генерация вручную/по нему")
            g["prompt_ref"] = True
        gen.append(g)
    if missing_audio:
        uniq = sorted(set(missing_audio))
        warnings.append(f"аудиофайл не найден: {len(uniq)} шт. ({', '.join(uniq[:6])}{' …' if len(uniq) > 6 else ''})"
                        f" — ищутся в {audio_dir} и {library_dir}")
    tracks = dx_rows + tracks

    spec = {
        "episode": episode,
        "output": _rel(output or (spec_dir / f"{episode}.mp4"), spec_dir),
        "width": 1920, "height": 1080, "fps": 24,
        "clips": clips,
        "tracks": tracks,
        "ducking": True,
        "master": {"I": -14, "TP": -1, "LRA_min": 11, "LRA_max": 20},
        "generation": gen,
        "warnings": warnings,
        "duration": D,
        "missing_audio": sorted(set(missing_audio)),
    }
    return spec, warnings


def _episode_from(*paths: Path | None) -> str:
    for p in paths:
        if p:
            m = re.search(r"ep\d+", p.name, re.I)
            if m:
                return m.group(0).lower()
    return "ep00"


def _cli() -> None:
    ap = argparse.ArgumentParser(description="Таблица звуков + шот-лист → JSON-план для pipeline.assemble")
    ap.add_argument("--sound-table", type=Path, required=True)
    ap.add_argument("--shotlist", type=Path)
    ap.add_argument("--episode", help="epNN (по умолчанию — из имени файла)")
    ap.add_argument("--audio-dir", type=Path, help="по умолчанию output/<ep>/audio")
    ap.add_argument("--library-dir", type=Path, default=Path("output/library"))
    ap.add_argument("--clips-dir", type=Path, help="по умолчанию output/<ep>/clips")
    ap.add_argument("--clip-pattern", default="{shot}.mp4",
                    help="имя файла клипа: {shot}=sc01-sh010, {ep}, {scene}, {n}")
    ap.add_argument("--out", type=Path, help="куда записать JSON (по умолчанию output/<ep>/assemble.json)")
    ap.add_argument("--output-video", type=Path, help="путь итогового mp4 (по умолчанию рядом с JSON)")
    ap.add_argument("--dialog-from-shotlist", choices=("auto", "yes", "no"), default="auto")
    ap.add_argument("--dx-offset", type=float, default=DX_OFFSET)
    ap.add_argument("--dx-tc-from-shotlist", action="store_true",
                    help="брать старт реплик из таблицы реплик шот-листа (при расхождении > 0.5 с)")
    ap.add_argument("--approved-only", action="store_true", help="только звуки в статусе «утверждено»")
    ap.add_argument("--strict", action="store_true", help="выход 2, если есть ненайденные файлы")
    ap.add_argument("--stdout", action="store_true", help="напечатать JSON вместо записи в файл")
    args = ap.parse_args()

    ep = args.episode or _episode_from(args.sound_table, args.shotlist)
    try:
        sounds, w1 = parse_sound_table(args.sound_table.read_text(encoding="utf-8"))
        shots, shot_lines, w2 = (parse_shotlist_full(args.shotlist.read_text(encoding="utf-8"))
                                 if args.shotlist else ([], [], []))
    except OSError as e:
        print(f"ОШИБКА: {e}", file=sys.stderr)
        sys.exit(2)
    if not sounds:
        print("ОШИБКА: в таблице звуков нет строк (нужны колонки ID и Тип)", file=sys.stderr)
        sys.exit(2)
    out = args.out or Path("output") / ep / "assemble.json"
    spec, w3 = build_spec(sounds, shots, episode=ep,
                          audio_dir=args.audio_dir or Path("output") / ep / "audio",
                          library_dir=args.library_dir,
                          clips_dir=args.clips_dir or Path("output") / ep / "clips",
                          clip_pattern=args.clip_pattern, spec_dir=out.parent,
                          output=args.output_video, dialog_from_shotlist=args.dialog_from_shotlist,
                          dx_offset=args.dx_offset, approved_only=args.approved_only,
                          shot_lines=shot_lines, dx_tc_from_shotlist=args.dx_tc_from_shotlist)
    warnings = w1 + w2 + w3
    spec["warnings"] = warnings
    text = json.dumps(spec, ensure_ascii=False, indent=2)
    if args.stdout:
        print(text)
    else:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        print(out)
    for w in warnings:
        print(f"ВНИМАНИЕ: {w}", file=sys.stderr)
    print(f"кадров: {len(shots)}, длительность: {spec['duration']} с, дорожек: {len(spec['tracks'])}, "
          f"к генерации: {len(spec['generation'])}, предупреждений: {len(warnings)}", file=sys.stderr)
    missing = bool(spec["missing_audio"]) or any("клипов нет" in w or "файла реплики нет" in w
                                                 for w in warnings)
    sys.exit(2 if args.strict and missing else 0)


if __name__ == "__main__":
    _cli()
