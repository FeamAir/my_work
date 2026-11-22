# «Песня кита»: звуковой дизайн

Версия 1.0 от 2026-11-22. Автор: звукорежиссёр.
Источник: `studio/story/bible.md` (раздел «Бумажный кит») и `ep01_script.md`, сцены 3 и 6.
Статус: план (без генерации).

## 1. Что нужно

Голос кита — главная звуковая подпись сериала. Он звучит в каждой серии, в нескольких состояниях. По сценарию: «протяжный низкий звук — китовая песня, смешанная с шелестом сотен страниц».

| Версия | Где в пилоте | Характер | Длительность |
|---|---|---|---|
| **Тревожная** (`alarm`) | sc03, первое появление кита, ≈ 1:05.5 | огромная, низкая, давит; зов вверх, который не находит разрешения; шелест сотен страниц нарастает, как шквал | 7 с |
| **Мягкая** (`soft`) | sc06, после доставки письма, ≈ 2:22.5 | тише, выше, «благодарит»; зов вниз, как выдох; шелест — как ветер в листах книги | 5 с |

Резерв для следующих серий (из того же набора слоёв, в пилоте не нужны): `dim` — тусклый, глухой (письмо отвергнуто, серия 4); `final` — длинная светлая версия на рассвете (серия 8).

## 2. Решение

**Собираем из слоёв, которые генерируются отдельно.** Не генерируем одним промптом.

| Слой | Чем генерируем | Зачем |
|---|---|---|
| W1 «Голос» — протяжный китовый зов | ElevenLabs **SFX** (`eleven_text_to_sound_v3`) | органика, «живое существо» |
| W2 «Бумага» — шелест сотен страниц | ElevenLabs **SFX** | то, что делает кита бумажным; главное отличие от обычного кита |
| W3 «Тон» — тянущийся музыкальный тон в тональности сериала | ElevenLabs **Music** (`force_instrumental: true`) | связывает голос кита с музыкой: кит «поёт в ре» |
| W4 «Масса» — инфранизкое давление (только `alarm`) | ElevenLabs **SFX** | размер 60 м; ощущается телом, на телефоне не слышно — это нормально |
| W5 «Искра» — тихий звон и шорох (только `soft`) | ElevenLabs **SFX** | связь со звуком янтарного шва |

Почему не одним промптом:
1. **Контроль.** Один промпт «китовая песня с шелестом бумаги» даёт случайный баланс: либо кит, либо бумага. Слоями можно менять пропорцию в сведении без перегенерации.
2. **Две версии из одних слоёв.** `alarm` и `soft` различаются обработкой и балансом, а не случайностью генерации. Поэтому зритель слышит одного и того же кита в разных состояниях. Это и делает звук лейтмотивом.
3. **Тональность.** Только слой W3 из Music API гарантированно музыкальный. Слой W1 подстраиваем по высоте к ре (D) питч-шифтом (`rubberband` в ffmpeg есть, проверено), и голос кита ложится на тему и лейтмотивы без диссонанса.
4. **Почему не всё через Music.** Music строит музыкальную форму: ритм, гармонию, иногда мелодию. Для голоса существа это лишнее и плохо управляется.

**Контрольный вариант (дёшево, один раз):** попробовать единый SFX-промпт (раздел 4.3). Если он вдруг звучит лучше сборки, берём его как W1+W2, а W3/W4 добавляем сверху.

## 3. Музыкальная привязка

- Тональный центр кита — **ре (D)**, как у главной темы (ре мажор, `sound_bible.md` п. 3.1).
- `alarm`: зов W1 скользит вверх и застревает на **до-диез (C#)**, на полутон ниже тоники. Слой W3 держит ре-минорную краску. Звучит неразрешённо, «тревожно». Полутоновое трение перекликается с мотивом «Тень» (L3, `leitmotifs.md`).
- `soft`: зов W1 начинается выше на 3–5 полутонов и опускается **на ре**. W3 — светлый ре мажор с добавленной ноной (D–F#–A–E). Звучит «разрешённо», как выдох.
- Подстройка W1 на слух: эталонный тон ре делаем в ffmpeg (`sine=f=73.42` — D2, `sine=f=146.83` — D3), ставим его рядом с зовом, подбираем коэффициент `rubberband=pitch=<k>`. Один полутон = ×1.0595.

## 4. Промпты

Общие параметры SFX: `model_id: eleven_text_to_sound_v3` (v2 снимается 1 марта 2027), `duration_seconds` задаём явно, 3 дубля на слой. Music: `model_id` указываем явно (`music_v2_5` или `music_v2`; `music_v1` снимается 31 января 2027), `force_instrumental: true`, минимальная длина трека 3 с.

### 4.1. Версия `alarm` (тревожная)

| Слой | API | Промпт (EN) | Длит. | prompt_influence |
|---|---|---|---|---|
| W1 | SFX | `Enormous whale call heard in open air high above a quiet town: a very long, deep, mournful moan that slowly slides upward and hangs unresolved, with a hollow, papery resonance instead of water, huge distant open-air reverb tail, no water sounds, no music` | 9 с | 0.55 |
| W2 | SFX | `Hundreds of old paper pages rustling and fluttering at once, rising like a gust from a soft whisper to a loud rushing swell and slowly settling, dry crisp paper, wide stereo, open air, no wind howl, no music` | 9 с | 0.5 |
| W3 | Music | `Instrumental sustained drone in D minor, no rhythm, no melody, no percussion. Low bowed cellos and double basses hold a deep D with a faint dissonant C-sharp shimmer from string harmonics above, slow swell in and out, dark, vast, awe-struck, cinematic.` | 9 с (`music_length_ms: 9000`) | — |
| W4 | SFX | `Very deep sub-bass rumble, slow pressure swell like something enormous passing overhead, no crack, no thunder clap, smooth and continuous` | 8 с | 0.4 |

### 4.2. Версия `soft` (мягкая)

| Слой | API | Промпт (EN) | Длит. | prompt_influence |
|---|---|---|---|---|
| W1 | SFX | `Gentle whale song heard from far above, soft and warm, a medium-low tone that sighs slowly downward and fades, tender and grateful, light papery resonance, airy open-air reverb, no water sounds, no music` | 6 с | 0.55 |
| W2 | SFX | `Soft breeze through the pages of a large old book, light paper rustle and slow page flutter, calm and gentle, close and warm, no wind howl, no music` | 6 с | 0.45 |
| W3 | Music | `Instrumental warm sustained chord in D major with an added ninth, no rhythm, no melody, no percussion. Soft high strings and a quiet glass-harmonica-like pad bloom gently and fade out. Tender, relieved, glowing.` | 6 с (`music_length_ms: 6000`) | — |
| W5 | SFX | `Delicate warm shimmer: a few soft tiny glass chimes and a faint sparkle of rustling paper, magical but subtle, short tail` | 3 с | 0.5 |

### 4.3. Контрольный единый промпт (по одному дублю на версию)
- `alarm`: `Colossal whale made of paper calling over a town at sunset: a long deep mournful whale moan blended with the rushing rustle of hundreds of paper pages, vast open-air reverb, ominous and awe-inspiring, no water, no music` — 8 с, influence 0.5.
- `soft`: `Paper whale singing softly far above: a gentle warm whale sigh blended with soft rustling pages, tender and grateful, airy reverb, no water, no music` — 6 с, influence 0.5.

## 5. Сборка (ffmpeg)

Схема одинакова для обеих версий, меняются уровни и обработка. Цепочка проверена на синтетических сигналах (ffmpeg 6.1.1): питч-шифт `rubberband`, эхо, сумма слоёв, точная обрезка, 48 кГц стерео.

```bash
# alarm: W1 опускаем примерно на 1.5 полутона (k подбирается на слух по эталонному D2)
ffmpeg -i w1.wav -i w2.wav -i w3.wav -i w4.wav -filter_complex "\
[0]rubberband=pitch=0.9178,lowpass=f=4000,aecho=0.8:0.6:140|310:0.35|0.2[a];\
[1]highpass=f=300,volume=-6dB[b];\
[2]volume=-8dB[c];\
[3]lowpass=f=120,volume=-4dB[d];\
[a][b][c][d]amix=inputs=4:normalize=0,atrim=0:7,\
afade=t=in:d=0.8,afade=t=out:st=5:d=2,aresample=48000" \
-c:a pcm_s24le lib_des_whale-song-alarm_v1.wav
```

| Параметр | `alarm` | `soft` |
|---|---|---|
| Питч W1 | вниз, к D2/C#2 | вверх на 3–5 полутонов, конец на D3 |
| Эхо W1 (`aecho`) | `0.8:0.6:140\|310:0.35\|0.2` — большое пространство | `0.8:0.5:90\|200:0.25\|0.12` — ближе и мягче |
| Фильтр W1 | lowpass 4 кГц | lowpass 6 кГц, highpass 120 Гц (без тяжести) |
| Баланс W1 / W2 / W3 / W4–W5 | 0 / −6 / −8 / −4 dB | 0 / −4 / −6 / −10 dB |
| Огибающая | вход 0.8 с, нарастание до 3 с, спад 2 с | вход 1 с, спад 2.5 с |
| Целевой уровень клипа | **−16 LUFS** (DES-акцент, на уровне диалога) | **−22 LUFS** |
| Панорама | стерео, широкая | стерео, чуть уже |

После сборки клип нормализуется к целевому уровню двухпроходным `loudnorm`, как в `mix_plan.md` (однопроходный режим уходит в dynamic — проверено). Выход `loudnorm` обязательно пересэмплировать в 48 кГц (`aresample=48000`): сам фильтр отдаёт 192 кГц.

## 6. В сведении

- Под песней кита **реплик нет** (в пилоте так и стоит). Если в будущих сериях наложится, кит приглушается на 6 dB под репликой вручную, без ducking.
- Музыка под `alarm` снимается до тянущегося тона (−6 dB к обычному уровню). Музыкальный слой W3 и так делает работу музыки.
- Перед `soft` в сцене 6 — тишина вокруг щелчка ящика (см. `ep01_sound_table.md`). Мягкая песня входит вместе со швом и переходит в главную тему (`leitmotifs.md`, «Доставка»).
- Проверка на телефонной полосе (200 Гц–8 кГц): W4 там пропадает. Кит должен остаться узнаваемым за счёт W1 и W2. Если нет — поднять W2 на 2 dB.

## 7. Файлы библиотеки

| Файл | Что |
|---|---|
| `lib_des_whale-song-alarm_v1.wav` | собранная тревожная версия, 7 с |
| `lib_des_whale-song-soft_v1.wav` | собранная мягкая версия, 5 с |
| `lib_des_whale-w1-call-alarm_v1.wav`, `..._w2-paper-alarm_v1.wav`, `..._w3-tone-alarm_v1.wav`, `..._w4-sub_v1.wav` | слои `alarm` |
| `lib_des_whale-w1-call-soft_v1.wav`, `..._w2-paper-soft_v1.wav`, `..._w3-tone-soft_v1.wav`, `..._w5-spark_v1.wav` | слои `soft` |

Слои храним отдельно: из них потом собираются `dim` и `final` без новой генерации.

## 8. Стоимость (оценка, сверить с тарифом)

SFX ≈ 40 кредитов/с при заданной длительности: слои SFX ≈ (9+9+8+6+6+3) с × 3 дубля ≈ 123 с ≈ **4 900 кредитов**. Контрольный промпт: 14 с ≈ 560 кредитов. Music: 2 трека по 6–9 с × 2 дубля, тариф уточнить. Это разовая затрата на сезон.
