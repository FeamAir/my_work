# План сведения и финальной сборки (ffmpeg)

Версия 0.1 от 2026-11-22. Автор: звукорежиссёр.
Целевые уровни — из `sound_bible.md`, раздел 5. Все команды ниже проверены на ffmpeg 6.1.1 на синтетических сигналах (тон, шум): синтаксис рабочий, итог мастера I = −14,0 LUFS. Параметры ducking откалиброваны на тестовом тоне и **требуют подстройки на первой реальной серии** (речь динамичнее тона).
Требование: ffmpeg ≥ 5.0 (нужны `amix normalize=0`, `adelay ... all=1`).
Автоматизация (скрипт, который строит эти команды из таблицы звуков) — задача IT-специалиста в `pipeline/`; здесь — спецификация.

## 1. Дорожки (стемы) и порядок

| № | Стем | Содержимое | Канальность | Целевой уровень клипов | Ducking |
|---|---|---|---|---|---|
| 1 | DX | реплики персонажей (TTS), VOX голосом персонажей | моно → центр стерео | −16 LUFS на реплику | — (это управляющий сигнал) |
| 2 | FX | HARD + DES (жёсткие и дизайн-эффекты) | стерео / моно с панорамой | −22…−16 LUFS | нет |
| 3 | FOLEY | шаги, одежда, предметы | моно с панорамой | −28…−24 LUFS | нет |
| 4 | AMB | эмбиент локаций (база + детали) | стерео | −34…−30 LUFS | 3 dB под диалог |
| 5 | MUS | музыкальные треки | стерео | −18 LUFS (до ducking) | 8–10 dB под диалог |
| 6 | STING | музыкальные акценты, заставка | стерео | −18 LUFS | нет |

Порядок сборки: **нормализация клипов → сборка стемов → премикс с ducking → мастер (loudnorm, 2 прохода) → mux с видео → контроль**.

Общие параметры: 48 кГц, промежуточные файлы `pcm_s24le`, длина каждого стема = точная длина видео `D` (секунды).

```bash
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 video.mp4)   # длина серии
```

## 2. Этап 0–1. Приём и нормализация клипов

Каждый файл из ElevenLabs (MP3 44,1 кГц) → WAV 48 кГц, приведённый к целевому уровню своей категории, с микрофейдами на краях (от щелчков) и потолком пика −3 dBFS.

```bash
# norm_clip.sh in.mp3 out.wav TARGET_LUFS
in="$1"; out="$2"; target="$3"
I=$(ffmpeg -hide_banner -nostats -i "$in" -af ebur128 -f null - 2>&1 \
    | awk '/Integrated loudness:/{f=1} f&&/I:/{print $2; exit}')
gain=$(awk -v t="$target" -v i="$I" 'BEGIN{printf "%.2f", t-i}')
ffmpeg -hide_banner -loglevel error -y -i "$in" -af "\
aresample=48000,\
volume=${gain}dB,\
alimiter=limit=0.708:level=false:attack=5:release=50,\
afade=t=in:d=0.005,areverse,afade=t=in:d=0.01,areverse" \
  -c:a pcm_s24le "$out"
```

- `alimiter=limit=0.708` — потолок −3 dBFS на клип.
- `areverse … areverse` — фейд-аут 10 мс в конце клипа без знания его длины (для коротких клипов ок; для файлов > 60 с вместо этого `afade=t=out:st=<длина−0.01>:d=0.01`).
- Для очень коротких клипов (< 0,4 с) интегральная громкость измеряется ненадёжно: для них нормализуем по пику (`volume` до пика −6 dBFS) и проверяем на слух.

Обработка диалога (добавляется к цепочке DX-клипов перед `volume`):

```text
highpass=f=80,acompressor=threshold=-20dB:ratio=2.5:attack=5:release=120:makeup=2dB
```
Срез ниже 80 Гц (гул, «бубнение») и мягкая компрессия для ровной разборчивости. TTS и так чистый, тяжёлую обработку не применяем.

## 3. Этап 2. Сборка стемов

Клипы ставятся на таймлайн через `adelay` (мс от начала серии = таймкод из таблицы звуков), суммируются `amix normalize=0` (без автоматического деления громкости на число входов), дополняются тишиной до длины `D`.

### 3.1. DX (пример с двумя репликами: 00:02.000 и 00:09.500)

```bash
ffmpeg -y -i dx_001.wav -i dx_002.wav -filter_complex "\
[0:a]adelay=2000:all=1[a0];\
[1:a]adelay=9500:all=1[a1];\
[a0][a1]amix=inputs=2:normalize=0:dropout_transition=0,\
apad=whole_dur=${D},atrim=0:${D},\
pan=stereo|c0=c0|c1=c0[dx]" \
-map "[dx]" -c:a pcm_s24le stem_dx.wav
```
`pan=stereo|c0=c0|c1=c0` — моно-реплика ровно в центр. Реплики одного персонажа не должны накладываться; перекрытие реплик разных персонажей допустимо (перебивания).

### 3.2. FX / FOLEY (панорама и уровень по месту)

```bash
ffmpeg -y -i ep01_hard_001.wav -i ep01_foley_001.wav -filter_complex "\
[0:a]adelay=15800:all=1,pan=stereo|c0=0.35*c0|c1=0.65*c0[h1];\
[1:a]adelay=7500:all=1,pan=stereo|c0=0.5*c0|c1=0.5*c0[f1];\
[h1][f1]amix=inputs=2:normalize=0:dropout_transition=0,\
apad=whole_dur=${D},atrim=0:${D}[fx]" \
-map "[fx]" -c:a pcm_s24le stem_fx.wav
```
Панорама: `0.5/0.5` — центр, `0.35/0.65` — ≈ R30, `0.65/0.35` — ≈ L30. Для стерео-исходников вместо `pan` при необходимости — `stereotools=balance_out=0.3`.
Ручная подстройка уровня отдельного эффекта по месту — `volume=-3dB` в его цепочке.

### 3.3. AMB (петля на длину сцены + переход между локациями)

Петля базы на длину сцены (сцена 1: 0–35 с, сцена 2: 34,5–80 с, кроссфейд 0,5 с с J-cut):

```bash
ffmpeg -y -i lib_amb_city-rain-night_v1.wav -i lib_amb_room-quiet_v1.wav -filter_complex "\
[0:a]aloop=loop=-1:size=2e9,atrim=0:35,\
afade=t=in:st=0:d=1,afade=t=out:st=34.5:d=0.5[s1];\
[1:a]aloop=loop=-1:size=2e9,atrim=0:45.5,\
afade=t=in:st=0:d=0.5,adelay=34500:all=1[s2];\
[s1][s2]amix=inputs=2:normalize=0:dropout_transition=0,\
apad=whole_dur=${D},atrim=0:${D}[amb]" \
-map "[amb]" -c:a pcm_s24le stem_amb.wav
```
- `aloop=loop=-1:size=2e9` + `atrim` — бесконечное повторение петли с обрезкой до нужной длины.
- Сцена 2 стартует на 0,5 с раньше смены кадра (J-cut), фейды перекрываются — получается кроссфейд.
- Детали эмбиента (one-shots) добавляются в этот же `amix` как обычные клипы через `adelay`.

### 3.4. MUS и STING

```bash
ffmpeg -y -i lib_mus_theme-sting_v1.wav -i lib_mus_l3-threat_v1.wav -filter_complex "\
[0:a]atrim=0:6,afade=t=out:st=5:d=1[m1];\
[1:a]atrim=0:40,afade=t=in:st=0:d=1.5,afade=t=out:st=37:d=3,adelay=52000:all=1[m2];\
[m1][m2]amix=inputs=2:normalize=0:dropout_transition=0,\
apad=whole_dur=${D},atrim=0:${D}[mus]" \
-map "[mus]" -c:a pcm_s24le stem_mus.wav
```
- Вход трека: фейд 0,5–1,5 с (или жёсткий вход на акценте — тогда без фейда).
- Выход: фейд 2–3 с; в последней сцене серии — 3–5 с.
- Смена трека «встык»: фейды двух треков перекрываются на 1–2 с (как в примере с эмбиентом). Если два трека идут подряд и известны оба файла — можно `acrossfade=d=1.5:c1=tri:c2=tri`.
- Стинги и заставка собираются в отдельный стем `stem_sting.wav` той же командой — они **не** приглушаются под диалог.

## 4. Этап 3. Премикс с ducking

```bash
ffmpeg -y -i stem_dx.wav -i stem_mus.wav -i stem_fx.wav -i stem_amb.wav -i stem_sting.wav \
-filter_complex "\
[0:a]asplit=3[dx][dx_sc_mus][dx_sc_amb];\
[1:a][dx_sc_mus]sidechaincompress=threshold=0.063:ratio=4:attack=40:release=600:knee=4:detection=rms:makeup=1[mus];\
[3:a][dx_sc_amb]sidechaincompress=threshold=0.1:ratio=1.5:attack=80:release=900:knee=6:detection=rms:makeup=1[amb];\
[dx][mus][2:a][amb][4:a]amix=inputs=5:normalize=0:duration=first:dropout_transition=0[premix]" \
-map "[premix]" -c:a pcm_s24le premix.wav
```

Параметры ducking:

| Стем | threshold | ratio | attack, мс | release, мс | Ожидаемое приглушение |
|---|---|---|---|---|---|
| MUS | 0.063 (≈ −24 dBFS) | 4 | 40 | 600 | ≈ 9 dB (замер на тесте) |
| AMB | 0.1 (≈ −20 dBFS) | 1.5 | 80 | 900 | ≈ 3 dB (замер на тесте) |

Калибровка на первой реальной серии: вывести только приглушённую музыку (`-map "[mus]"`) и сравнить `volumedetect` на участке с речью и без; цель 8–10 dB. Мало — понизить `threshold` (0.04) или поднять `ratio` (5–6); много или «качает» — наоборот, и/или увеличить `release` до 800 мс.

Участки без ducking (кульминация без слов, музыкальный клип): соответствующий трек кладётся в `stem_sting.wav`, а не в `stem_mus.wav`.

Если FOLEY собирается отдельным стемом — добавить его входом в `amix` (`inputs=6`).

## 5. Этап 4. Мастер: loudnorm в два прохода

Проход 1 — измерение:
```bash
ffmpeg -hide_banner -i premix.wav \
  -af loudnorm=I=-14:TP=-1:LRA=11:print_format=json -f null - 2>&1 | tail -12
```

Проход 2 — применение измеренных значений (`input_i`, `input_tp`, `input_lra`, `input_thresh`, `target_offset` из JSON):
```bash
ffmpeg -y -i premix.wav -af "\
loudnorm=I=-14:TP=-1:LRA=${LRA_T}:\
measured_I=${IN_I}:measured_TP=${IN_TP}:measured_LRA=${IN_LRA}:\
measured_thresh=${IN_THRESH}:offset=${OFFSET}:linear=true:print_format=summary,\
aresample=48000" \
-c:a pcm_s24le master.wav
```

Важно:
- `linear=true` — громкость меняется одним усилением, динамика сведения сохраняется. ffmpeg **сам переключится в динамический режим**, если измеренный LRA больше целевого или если линейное усиление пробьёт TP. Поэтому `LRA_T = max(11, measured_LRA + 1)` (но не больше 20). Проверено: при measured_LRA = 15,3 и LRA=11 режим становится `dynamic`, при LRA=16 — `linear`.
- Если и так ушло в `dynamic` из-за пиков — опустить самые громкие эффекты в премиксе на 2–3 dB и повторить, а не мириться с «качанием».
- `aresample=48000` после `loudnorm` обязателен: фильтр внутри работает на 192 кГц.

## 6. Этап 5. Сборка с видео

```bash
ffmpeg -y -i video.mp4 -i master.wav \
  -map 0:v:0 -map 1:a:0 -c:v copy \
  -c:a aac -b:a 320k -ar 48000 -ac 2 \
  -shortest -movflags +faststart episode_final.mp4
```

## 7. Этап 6. Контроль

```bash
# громкость и true peak мастера
ffmpeg -hide_banner -nostats -i episode_final.mp4 -map 0:a -af ebur128=peak=true -f null - 2>&1 | tail -12
```
Критерии приёмки:
- I = −14 ±1 LUFS, True peak ≤ −1,0 dBFS (в отчёте `ebur128` — строка «Peak»), LRA 6–11 LU (до 13 для экшена).
- Длина аудио = длина видео (±1 кадр), синхрон реплик с губами/кадрами в контрольных точках.
- Прослушивание: наушники + имитация телефона:
  ```bash
  ffplay -af "highpass=f=200,lowpass=f=8000" episode_final.mp4
  ```
- Нет щелчков на стыках, нет «дыр» эмбиента, музыка не «качает» между репликами.

## 8. Сводная таблица параметров

| Параметр | Значение |
|---|---|
| Частота / разрядность | 48 кГц / 24 бит (промежуточные), AAC 320 кбит/с (финал) |
| DX на реплику | −16 LUFS, HPF 80 Гц, компрессор 2.5:1 |
| MUS (до ducking) | −18 LUFS; ducking ≈ 9 dB |
| AMB | −32 LUFS (база); ducking ≈ 3 dB |
| FX / FOLEY | −22…−16 / −28…−24 LUFS |
| Потолок клипа | −3 dBFS (`alimiter=limit=0.708`) |
| Микрофейды клипов | 5 мс вход / 10 мс выход |
| Фейды музыки | вход 0,5–1,5 с, выход 2–3 с (финал 3–5 с) |
| Кроссфейд эмбиента | 0,3–0,5 с, J-cut 0,5–1 с |
| Мастер | `loudnorm I=-14 TP=-1 LRA=max(11, measured+1)`, 2 прохода, `linear=true` |
