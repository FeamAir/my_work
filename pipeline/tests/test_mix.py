"""Тесты сведения (assemble.py по mix_plan.md), плана сборки (sound_plan.py) и SFX v3.

    python3 -m unittest pipeline.tests.test_mix -v
Тесты с ffmpeg пропускаются, если его нет в PATH. Сети не нужно.
"""
from __future__ import annotations

import io
import json
import os
import shutil
import subprocess
import tempfile
import unittest
import warnings
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

from pipeline import assemble, costs, elevenlabs_client, sound_plan

HAVE_FFMPEG = bool(shutil.which("ffmpeg") and shutil.which("ffprobe"))
ROOT = Path(__file__).resolve().parents[2]


class FakeResp:
    def __init__(self, content=b"ID3"):
        self.status_code, self.content, self.headers, self.text = 200, content, {}, ""


# ================================================================ assemble ===

class TestMixMath(unittest.TestCase):
    def test_lra_target(self):
        self.assertEqual(assemble.lra_target(5.0), 11.0)     # min 11
        self.assertEqual(assemble.lra_target(10.0), 11.0)
        self.assertEqual(assemble.lra_target(15.3), 16.3)    # пример из mix_plan.md §5
        self.assertEqual(assemble.lra_target(25.0), 20.0)    # не больше 20

    def test_pan(self):
        self.assertEqual(assemble.pan_position("C"), 0.0)
        self.assertAlmostEqual(assemble.pan_position("L30"), -0.3)
        self.assertAlmostEqual(assemble.pan_position("r30"), 0.3)
        self.assertIsNone(assemble.pan_position("stereo"))
        self.assertEqual(assemble.pan_position(-2), -1.0)
        with self.assertRaises(assemble.AssembleError):
            assemble.pan_position("X5")
        # закон mix_plan.md: R30 = 0.35/0.65, центр 0.5/0.5 (scale=1); scale=2 — центр как у DX
        self.assertEqual(assemble.pan_gains(0.3, scale=1.0), (0.35, 0.65))
        self.assertEqual(assemble.pan_gains(-0.3, scale=1.0), (0.65, 0.35))
        self.assertEqual(assemble.pan_gains(0.0, scale=2.0), (1.0, 1.0))

    def test_clip_gain(self):
        self.assertEqual(assemble.clip_gain(-16, -24.0, -10.0, 2.0), (8.0, "lufs"))
        self.assertEqual(assemble.clip_gain(-18, -70.0, -18.1, 0.3), (12.1, "peak"))   # < 0.4 с
        self.assertEqual(assemble.clip_gain(-18, float("-inf"), -12.0, 2.0), (6.0, "peak"))
        self.assertEqual(assemble.clip_gain(-18, float("-inf"), float("-inf"), 2.0), (0.0, "none"))

    def test_parsers(self):
        err = ("[Parsed_loudnorm_0 @ 0x1] \n{\n\t\"input_i\" : \"-21.75\",\n\t\"input_tp\" : \"-18.06\",\n"
               "\t\"input_lra\" : \"3.10\",\n\t\"input_thresh\" : \"-31.75\",\n"
               "\t\"normalization_type\" : \"dynamic\",\n\t\"target_offset\" : \"0.05\"\n}\n"
               "[Parsed_ebur128_0 @ 0x2] Summary:\n\n  Integrated loudness:\n    I:         -21.2 LUFS\n"
               "    Threshold: -31.3 LUFS\n\n  Loudness range:\n    LRA:         3.0 LU\n"
               "    Threshold:   0.0 LUFS\n\n  True peak:\n    Peak:      -17.5 dBFS\n")
        ln = assemble.parse_loudnorm_json(err)
        eb = assemble.parse_ebur128(err)
        self.assertEqual(ln["input_i"], "-21.75")
        self.assertEqual((eb["I"], eb["thresh"], eb["LRA"], eb["peak"]), (-21.2, -31.3, 3.0, -17.5))
        m = assemble.master_measurement(ln, eb)
        self.assertEqual(m["input_i"], "-21.20")          # приоритет ebur128
        self.assertEqual(m["input_thresh"], "-31.30")
        self.assertEqual(m["input_tp"], "-17.50")         # худший из двух
        self.assertEqual(m["input_lra"], "3.10")
        self.assertEqual(m["loudnorm_input_i"], "-21.75")
        with self.assertRaises(assemble.AssembleError):
            assemble.parse_loudnorm_json("no json here")


def _gen(args: list[str]) -> None:
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *args], check=True)


@unittest.skipUnless(HAVE_FFMPEG, "нужен ffmpeg")
class TestAssemblePlan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        d = cls.d = Path(cls.tmp.name)
        _gen(["-f", "lavfi", "-i", "testsrc=size=320x240:rate=24:duration=3", "-pix_fmt", "yuv420p",
              str(d / "a.mp4")])
        _gen(["-f", "lavfi", "-i", "sine=frequency=440:duration=1", "-ac", "1", str(d / "dx.wav")])
        _gen(["-f", "lavfi", "-i", "sine=frequency=220:duration=2", "-ac", "2", str(d / "mus.wav")])
        _gen(["-f", "lavfi", "-i", "anoisesrc=duration=1:amplitude=0.1", str(d / "amb.wav")])
        _gen(["-f", "lavfi", "-i", "sine=frequency=1000:duration=0.5", str(d / "fx.wav")])

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def spec(self, **kw):
        s = {"output": "out.mp4", "clips": [{"path": "a.mp4"}, {"path": "a.mp4", "duration": 2}],
             "tracks": [
                 {"id": "dx1", "type": "dialog", "path": "dx.wav", "start": 0.5},
                 {"id": "mus1", "stem": "mus", "path": "mus.wav", "start": 0, "loop": True, "fade_out": 2},
                 {"id": "amb1", "stem": "amb", "path": "amb.wav", "start": 0, "end": 4, "loop": True},
                 {"id": "fx1", "stem": "fx", "path": "fx.wav", "start": 4.0, "pan": "L30", "gain_db": -3,
                  "target_lufs": -20},
                 {"id": "late", "stem": "fx", "path": "fx.wav", "start": 99},
             ]}
        s.update(kw)
        return s

    def test_plan_timeline(self):
        plan = assemble.build_plan(self.spec(), self.d)
        self.assertEqual(plan.duration, 5.0)
        ids = {i.id: i for i in plan.items}
        self.assertNotIn("late", ids)
        self.assertTrue(any("late" in w for w in plan.warnings))
        self.assertEqual(ids["dx1"].stem, "dx")
        self.assertEqual(ids["dx1"].target_lufs, -16.0)
        self.assertEqual(ids["mus1"].length, 5.0)     # петля до конца серии
        self.assertEqual(ids["amb1"].length, 4.0)     # до end
        self.assertEqual(ids["fx1"].length, 0.5)      # не длиннее файла
        self.assertEqual(ids["amb1"].target_lufs, -32.0)
        self.assertEqual(plan.master["I"], -14.0)
        self.assertEqual(plan.master["TP"], -1.0)

    def test_commands_follow_mix_plan(self):
        plan = assemble.build_plan(self.spec(), self.d)
        dx = next(i for i in plan.items if i.id == "dx1")
        norm = " ".join(assemble.cmd_normalize(dx, -3.5))
        for frag in ("highpass=f=80", "acompressor=threshold=-20dB:ratio=2.5", "volume=-3.50dB",
                     "alimiter=limit=0.708", "afade=t=in:d=0.005", "pcm_s24le", "-ac 1"):
            self.assertIn(frag, norm)
        stem_dx = " ".join(assemble.cmd_stem(plan, "dx"))
        self.assertIn("adelay=500:all=1,asetpts=N/SR/TB", stem_dx)
        self.assertIn("pan=stereo|c0=c0|c1=c0", stem_dx)
        self.assertIn("apad=whole_dur=5,atrim=0:5", stem_dx)
        stem_fx = " ".join(assemble.cmd_stem(plan, "fx"))
        self.assertIn("pan=stereo|c0=1.3*c0|c1=0.7*c0", stem_fx)   # L30, scale 2
        self.assertIn("volume=-3.00dB", stem_fx)
        stem_amb = " ".join(assemble.cmd_stem(plan, "amb"))
        self.assertIn("aloop=loop=-1:size=2e9,atrim=0:4", stem_amb)
        premix = " ".join(assemble.cmd_premix(plan, ["dx", "fx", "amb", "mus"]))
        self.assertIn("sidechaincompress=threshold=0.063:ratio=4:attack=40:release=600", premix)
        self.assertIn("sidechaincompress=threshold=0.1:ratio=1.5:attack=80:release=900", premix)
        self.assertIn("amix=inputs=4:normalize=0", premix)
        self.assertIn("mus_ducked.wav", premix)
        p2 = " ".join(assemble.cmd_master_pass2(plan, {k: "-20" for k in
                      ("input_i", "input_tp", "input_lra", "input_thresh", "target_offset")}, "16.3"))
        self.assertIn("loudnorm=I=-14:TP=-1:LRA=16.3", p2)
        self.assertIn("linear=true", p2)
        self.assertIn("aresample=48000", p2)
        mux = " ".join(assemble.cmd_mux(plan, plan.work / "master.wav"))
        self.assertIn("-c:v copy", mux)
        self.assertIn("-b:a 320k", mux)

    def test_ducking_off_and_overrides(self):
        plan = assemble.build_plan(self.spec(ducking={"mus": {"threshold": 0.04}, "amb": False}), self.d)
        premix = " ".join(assemble.cmd_premix(plan, ["dx", "amb", "mus"]))
        self.assertIn("threshold=0.04", premix)
        self.assertEqual(premix.count("sidechaincompress"), 1)
        plan = assemble.build_plan(self.spec(duck_music=False), self.d)
        self.assertNotIn("sidechaincompress", " ".join(assemble.cmd_premix(plan, ["dx", "mus"])))

    def test_dry_run_runs_nothing(self):
        (self.d / "spec.json").write_text(json.dumps(self.spec()), encoding="utf-8")
        buf = io.StringIO()
        with redirect_stdout(buf), mock.patch.object(assemble, "_run") as run:
            out = assemble.assemble(self.d / "spec.json", dry_run=True)
        run.assert_not_called()
        text = buf.getvalue()
        for stage in ("# 0. video", "# 1. normalize dx1", "# 2. stem amb", "# 3. premix",
                      "# 4. master, проход 1", "# 4. master, проход 2", "# 5. mux", "# 6. control"):
            self.assertIn(stage, text)
        self.assertEqual(out.name, "out.mp4")
        self.assertFalse((self.d / "out.mp4").exists())

    def test_missing_file(self):
        s = self.spec()
        s["tracks"].append({"stem": "fx", "path": "nope.wav", "start": 1})
        with self.assertRaises(assemble.AssembleError):
            assemble.build_plan(s, self.d)
        with self.assertRaises(assemble.AssembleError):
            assemble.build_plan(self.spec(tracks=[{"stem": "xyz", "path": "fx.wav"}]), self.d)


@unittest.skipUnless(HAVE_FFMPEG, "нужен ffmpeg")
class TestStemTimeline(unittest.TestCase):
    """Регрессия S01E01 v2 (QA A1–A5): DX-клипы с trim_start > 0 стоят точно на своих таймкодах,
    стем ровно D секунд (раньше adelay терял ведущую тишину и стем уезжал/укорачивался)."""

    def test_trimmed_dx_items_land_on_timecode(self):
        import numpy as np
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i",
                            "sine=f=440:d=2:r=48000", "-c:a", "pcm_s24le", str(d / "v.wav")], check=True)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i",
                            "color=c=black:s=64x64:r=24:d=8", "-pix_fmt", "yuv420p", str(d / "v.mp4")], check=True)
            spec = {"output": "out.mp4", "width": 64, "height": 64, "fps": 24,
                    "clips": [{"path": "v.mp4", "duration": 8}],
                    "tracks": [{"id": "a", "stem": "dx", "path": "v.wav", "start": 2.5, "trim_start": 0.05,
                                "duration": 1.0},
                               {"id": "b", "stem": "dx", "path": "v.wav", "start": 6.0, "trim_start": 0.0137,
                                "duration": 1.0}]}
            plan = assemble.build_plan(spec, d)
            (plan.work / "clips").mkdir(parents=True)
            for it in plan.items:
                subprocess.run(assemble.cmd_normalize(it, 0.0), check=True, capture_output=True)
            subprocess.run(assemble.cmd_stem(plan, "dx"), check=True, capture_output=True)
            raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(plan.work / "stem_dx.wav"),
                                  "-f", "f32le", "-ac", "1", "-"], capture_output=True, check=True).stdout
            x = np.frombuffer(raw, np.float32)
            self.assertAlmostEqual(len(x) / 48000, 8.0, places=2)
            nz = np.nonzero(np.abs(x) > 1e-3)[0]
            onsets = [nz[0]] + [nz[i + 1] for i in np.nonzero(np.diff(nz) > 4800)[0]]
            self.assertEqual(len(onsets), 2)
            self.assertAlmostEqual(onsets[0] / 48000, 2.5, delta=0.005)
            self.assertAlmostEqual(onsets[1] / 48000, 6.0, delta=0.005)


@unittest.skipUnless(HAVE_FFMPEG, "нужен ffmpeg")
class TestSelftest(unittest.TestCase):
    def test_selftest_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            res = assemble.selftest(tmp)
        self.assertTrue(res["passed"], res)
        self.assertLessEqual(abs(res["master_I"] + 14), 1.0)
        self.assertLessEqual(res["master_TP"], -1.0)


# ============================================================== sound_plan ===

SOUND_TABLE = """# Звуки серии EP01

| ID | Сцена/кадр | Таймкод (старт) | Синхро-точка | Тип | Описание (RU) | Промпт (EN) | Длит., с | Loop | prompt_influence | Громкость, LUFS | Панорама | Библиотека | Статус |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ep01_amb_001 | sc01 | 00:00.000 | — | AMB | Город | City ambience, no music | 30 | да | 0.35 | −32 | stereo | new | план |
| ep01_mus_001 | sc01 | 00:00.000 | — | MUS | Тема | Calm piano | 20 | нет | — | −18 | stereo | new | план |
| ep01_foley_001 | sc01/sh020 | 00:04.500 | — | FOLEY | Шаги | Footsteps on wood | 2 | нет | 0.6 | −26 | L30 | new | утверждено |
| ep01_hard_001 | sc01/sh030 | 00:09.200 | удар 00:09.40 | HARD | Дверь | Door slam | 1.5 | нет | 0.6 | −22…−16 | R30 | lib_hard_door_v1 | утверждено |
| ep01_amb_002 | sc02 | 00:12.500 | — | AMB | Комната | Quiet room tone | 30 | да | 0.3 | −34 | stereo | new | план |
| ep01_mus_002 | sc02 | TC≈00:14.0 | — | MUS | Угроза | Tense strings | 30 | нет | — | −18 | stereo | new | план |
| ep01_des_001 | sc02/sh010 | 00:30.000 | вспышка 00:02.00 | DES | Вспышка | Magic flash | 3 | нет | 0.5 | −20 | X9 | new | план |
| ep01_zzz_001 | sc02 | 00:14.000 | — | ZZZ | ? | ? | 1 | нет | — | −20 | C | new | план |
"""

SHOTLIST = """# EP01

| № | Сцена | Длит. | План | Камера | Действие | Реплика / звук | Промпт ключевого кадра | Промпт движения | Модель | Статус |
|---|---|---|---|---|---|---|---|---|---|---|
| sc01-sh010 | 01 | 4 с | WS | static | Улица | Шумы города; музыка: тема | `kf` | `mv` | NB | план |
| sc01-sh020 | 01 | 5 с | MS | static | Идёт | Шаги | `kf` | `mv` | NB | план |
| sc01-sh030 | 01 | 4 с | MCU | static | Говорит | Мира (тихо): «Ну вот.»<br>Кай: «Пора.» | `kf` | `mv` | NB | план |
| sc02-sh010 | 02 | 3,5 с | WS | static | Комната | — | `kf` | `mv` | NB | план |
| sc02-sh020 | 02 | 5 | CU | static | Взгляд | Кай: «Кто здесь?» | `kf` | `mv` | NB | план |
| | | | | | | | | | | план |
"""


class TestSoundPlanParsing(unittest.TestCase):
    def test_tc_and_numbers(self):
        self.assertEqual(sound_plan.parse_tc("00:07.500"), (7.5, False))
        self.assertEqual(sound_plan.parse_tc("01:02.25"), (62.25, False))
        self.assertEqual(sound_plan.parse_tc("1:00:02.5"), (3602.5, False))
        self.assertEqual(sound_plan.parse_tc("TC≈00:14,0"), (14.0, True))
        self.assertEqual(sound_plan.parse_tc("удар 00:16.10"), (16.1, False))
        self.assertEqual(sound_plan.parse_tc("—"), (None, False))
        self.assertEqual(sound_plan.parse_number("−32"), -32.0)
        self.assertEqual(sound_plan.parse_number("−22…−16"), -19.0)
        self.assertEqual(sound_plan.parse_number("3,5 с"), 3.5)
        self.assertIsNone(sound_plan.parse_number("—"))
        self.assertEqual(sound_plan.parse_scene_shot("sc03/sh05"), (3, 5))
        self.assertEqual(sound_plan.parse_scene_shot("`sc01-sh010`"), (1, 10))
        self.assertEqual(sound_plan.parse_scene_shot("sc02"), (2, None))

    def test_dialog(self):
        self.assertEqual(sound_plan.parse_dialog("Мира (тихо, себе): «Ну вот. Снова идёшь.»"),
                         [("Мира", "Ну вот. Снова идёшь.")])
        self.assertEqual(sound_plan.parse_dialog("Тиканье; Мира: «А?»<br>Кай: «Б.»"),
                         [("Мира", "А?"), ("Кай", "Б.")])
        self.assertEqual(sound_plan.parse_dialog("Тиканье часов; музыка: вступление"), [])

    def test_shotlist(self):
        shots, w = sound_plan.parse_shotlist(SHOTLIST)
        self.assertEqual([s.id for s in shots],
                         ["sc01-sh010", "sc01-sh020", "sc01-sh030", "sc02-sh010", "sc02-sh020"])
        self.assertEqual([s.start for s in shots], [0, 4, 9, 13, 16.5])
        self.assertEqual(shots[2].dialog, [("Мира", "Ну вот."), ("Кай", "Пора.")])

    def test_sound_table(self):
        sounds, w = sound_plan.parse_sound_table(SOUND_TABLE)
        self.assertEqual(len(sounds), 7)             # ZZZ пропущен
        self.assertTrue(any("ZZZ" in x for x in w))
        self.assertTrue(any("X9" in x for x in w))   # непонятная панорама → C
        hard = next(s for s in sounds if s.id == "ep01_hard_001")
        self.assertEqual((hard.stem, hard.start, hard.sync, hard.lufs, hard.pan, hard.library),
                         ("fx", 9.2, 9.4, -19.0, "R30", "lib_hard_door_v1"))
        amb = next(s for s in sounds if s.id == "ep01_amb_001")
        self.assertTrue(amb.loop)
        self.assertEqual(amb.prompt_influence, 0.35)


class TestSoundPlanBuild(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = self.d = Path(self.tmp.name)
        for sub in ("audio", "lib", "clips"):
            (d / sub).mkdir()
        (d / "audio" / "ep01_amb_001.wav").write_bytes(b"x")
        (d / "audio" / "ep01_foley_001_steps-wood_v1.wav").write_bytes(b"x")
        (d / "audio" / "ep01_foley_001_steps-wood_v2.wav").write_bytes(b"x")
        (d / "lib" / "lib_hard_door_v1.wav").write_bytes(b"x")
        (d / "clips" / "sc01-sh010.mp4").write_bytes(b"x")

    def tearDown(self):
        self.tmp.cleanup()

    def build(self, **kw):
        sounds, _ = sound_plan.parse_sound_table(SOUND_TABLE)
        shots, _ = sound_plan.parse_shotlist(SHOTLIST)
        args = dict(episode="ep01", audio_dir=self.d / "audio", library_dir=self.d / "lib",
                    clips_dir=self.d / "clips", spec_dir=self.d)
        args.update(kw)
        return sound_plan.build_spec(sounds, shots, **args)

    def test_spec(self):
        spec, w = self.build()
        self.assertEqual(spec["duration"], 21.5)
        self.assertEqual(spec["clips"][0], {"path": "clips/sc01-sh010.mp4", "duration": 4.0, "shot": "sc01-sh010"})
        self.assertTrue(any("клип sc01-sh020" in x for x in w))
        t = {x["id"]: x for x in spec["tracks"]}
        # эмбиент сцены 1 — петля до конца сцены 1 (13 с)
        self.assertEqual((t["ep01_amb_001"]["end"], t["ep01_amb_001"]["loop"]), (13.0, True))
        self.assertEqual(t["ep01_amb_001"]["path"], "audio/ep01_amb_001.wav")
        self.assertEqual(t["ep01_amb_002"]["end"], 21.5)
        # музыка 1 — до старта музыки 2 + 1.5 с кроссфейд
        self.assertEqual(t["ep01_mus_001"]["end"], 15.5)
        self.assertEqual(t["ep01_mus_001"]["fade_out"], 1.5)
        self.assertTrue(any("TC≈" in x and "ep01_mus_002" in x for x in w))
        # файл по шаблону <ID>_*_vN — берётся последняя версия; библиотека — по колонке
        self.assertEqual(t["ep01_foley_001"]["path"], "audio/ep01_foley_001_steps-wood_v2.wav")
        self.assertEqual(t["ep01_hard_001"]["path"], "lib/lib_hard_door_v1.wav")
        self.assertEqual(t["ep01_hard_001"]["target_lufs"], -19.0)
        self.assertEqual((t["ep01_hard_001"]["stem"], t["ep01_hard_001"]["pan"]), ("fx", "R30"))
        # DES: синхро-точка раньше старта и кадр sc02/sh010 не совпадает с 30 с
        self.assertTrue(any("ep01_des_001" in x and "синхро" in x for x in w))
        self.assertTrue(any("ep01_des_001" in x and "вне кадра" in x for x in w))
        # реплики из шот-листа (в таблице нет DX)
        dx = [x for x in spec["tracks"] if x["stem"] == "dx"]
        self.assertEqual([x["id"] for x in dx], ["ep01_dx_sc01-sh030_1", "ep01_dx_sc01-sh030_2",
                                                 "ep01_dx_sc02-sh020_1"])
        self.assertEqual(dx[0]["start"], 9.3)
        self.assertEqual(dx[0]["meta"]["character"], "Мира")
        # генерация: всё new, кроме реплик и библиотечного звука; SFX — модель v3
        gen = {g["id"]: g for g in spec["generation"]}
        self.assertNotIn("ep01_hard_001", gen)
        self.assertEqual(gen["ep01_amb_001"]["model_id"], "eleven_text_to_sound_v3")
        self.assertTrue(gen["ep01_amb_001"]["loop"])
        self.assertEqual(gen["ep01_mus_001"]["kind"], "music")
        self.assertEqual(spec["master"], {"I": -14, "TP": -1, "LRA_min": 11, "LRA_max": 20})

    def test_options(self):
        spec, _ = self.build(dialog_from_shotlist="no", approved_only=True)
        self.assertEqual(sorted(x["id"] for x in spec["tracks"]), ["ep01_foley_001", "ep01_hard_001"])

    def test_no_shotlist(self):
        sounds, _ = sound_plan.parse_sound_table(SOUND_TABLE)
        spec, w = sound_plan.build_spec(sounds, [], episode="ep01", audio_dir=self.d / "audio",
                                        library_dir=self.d / "lib", clips_dir=self.d / "clips",
                                        spec_dir=self.d)
        self.assertEqual(spec["clips"], [])
        self.assertTrue(any("шот-лист не задан" in x for x in w))
        t = {x["id"]: x for x in spec["tracks"]}
        self.assertEqual(t["ep01_amb_001"]["end"], 13.0)   # до следующего эмбиента + 0.5 с

    def test_templates_parse(self):
        """Примеры из шаблонов студии разбираются (если файлы на месте)."""
        wf = ROOT / "studio/sound/sfx_music_workflow.md"
        tpl = ROOT / "studio/direction/shotlist_template.md"
        if not (wf.is_file() and tpl.is_file()):
            self.skipTest("шаблонов нет")
        sounds, _ = sound_plan.parse_sound_table(wf.read_text(encoding="utf-8"))
        shots, _ = sound_plan.parse_shotlist(tpl.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(sounds), 6)
        self.assertEqual([s.id for s in shots], ["sc01-sh010", "sc01-sh020", "sc01-sh030"])
        self.assertEqual(shots[2].dialog, [("Мира", "Ну вот. Снова идёшь.")])


@unittest.skipUnless(HAVE_FFMPEG, "нужен ffmpeg")
class TestSoundPlanToAssemble(unittest.TestCase):
    """План из sound_plan принимается assemble.build_plan (на синтетических файлах)."""

    def test_end_to_end_plan(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            for sub in ("audio", "lib", "clips"):
                (d / sub).mkdir()
            shots, _ = sound_plan.parse_shotlist(SHOTLIST)
            for s in shots:
                _gen(["-f", "lavfi", "-i", f"testsrc=size=160x120:rate=24:duration={s.duration + 1}",
                      "-pix_fmt", "yuv420p", str(d / "clips" / f"{s.id}.mp4")])
            sounds, _ = sound_plan.parse_sound_table(SOUND_TABLE)
            for s in sounds:
                target = d / ("lib" if s.library.startswith("lib_") else "audio") / \
                    f"{s.library if s.library.startswith('lib_') else s.id}.wav"
                _gen(["-f", "lavfi", "-i", "sine=duration=2", str(target)])
            for sid in ("ep01_dx_sc01-sh030_1", "ep01_dx_sc01-sh030_2", "ep01_dx_sc02-sh020_1"):
                _gen(["-f", "lavfi", "-i", "sine=duration=1", str(d / "audio" / f"{sid}.wav")])
            spec, w = sound_plan.build_spec(sounds, shots, episode="ep01", audio_dir=d / "audio",
                                            library_dir=d / "lib", clips_dir=d / "clips", spec_dir=d)
            self.assertFalse([x for x in w if "не найден (" in x or "файла нет" in x], w)
            plan = assemble.build_plan(spec, d)
            self.assertEqual(plan.duration, 21.5)
            self.assertEqual(len(plan.clips), 5)
            self.assertIn("dx", {i.stem for i in plan.items})


# ============================================================ ElevenLabs ===

class TestSfxV3(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.env = mock.patch.dict(os.environ, {
            "OUTPUT_DIR": self.tmp.name, "ELEVENLABS_API_KEY": "test-el-key-123456",
            "BUDGET_LIMIT_USD": "1.00", "STUDIO_ALLOW_PAID": "1"})
        self.env.start()

    def tearDown(self):
        self.env.stop()
        self.tmp.cleanup()

    def test_default_model_v3(self):
        self.assertEqual(elevenlabs_client.DEFAULT_SFX_MODEL, "eleven_text_to_sound_v3")
        with mock.patch.object(elevenlabs_client, "request", return_value=FakeResp()) as req:
            elevenlabs_client.sfx("rain on a tin roof", Path(self.tmp.name) / "r.mp3",
                                  duration_seconds=20, loop=True, prompt_influence=0.35)
        body = req.call_args[1]["json"]
        self.assertEqual(body, {"text": "rain on a tin roof", "model_id": "eleven_text_to_sound_v3",
                                "prompt_influence": 0.35, "duration_seconds": 20, "loop": True})
        rec = costs.read_log()[-1]
        self.assertEqual(rec["units"], 800)

    def test_v2_deprecated_warning(self):
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            body = elevenlabs_client.sfx_body("door", model_id="eleven_text_to_sound_v2")
        self.assertEqual(body["model_id"], "eleven_text_to_sound_v2")
        self.assertTrue(any(issubclass(c.category, DeprecationWarning) and "2027-03-01" in str(c.message)
                            for c in caught))

    def test_validation_before_guard(self):
        with mock.patch.object(elevenlabs_client, "request") as req, \
                mock.patch.object(costs, "guard") as guard:
            for kw in ({"duration_seconds": 31}, {"duration_seconds": 0.2}, {"prompt_influence": 1.5}):
                with self.assertRaises(ValueError):
                    elevenlabs_client.sfx("x", Path(self.tmp.name) / "x.mp3", **kw)
            with self.assertRaises(ValueError):
                elevenlabs_client.sfx("  ", Path(self.tmp.name) / "x.mp3")
        req.assert_not_called()
        guard.assert_not_called()


if __name__ == "__main__":
    unittest.main()
