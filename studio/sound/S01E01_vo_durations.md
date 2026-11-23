# S01E01 — черновая озвучка: длительности реплик (аниматик, шаг 1)

Версия 1.0 · 2026-11-23 · звукорежиссёр · статус: **черновик для подгонки длительностей кадров** (голоса — черновой кастинг, не финал; Летописец — кандидат)

Машинный двойник: `S01E01_vo_durations.csv` (те же данные + доп. столбцы). Файлы: `output/S01E01/animatic/vo/<file>` и R2 `S01E01/animatic/vo/<file>`. Паспорт каждого дубля (voice_id, модель, seed, настройки, tts_text, расшифровка) — `output/S01E01/animatic/vo/manifest.json` (тоже в R2). Пересборка: `python3 studio/sound/tools/draft_vo.py table && python3 studio/sound/tools/durations_md.py`.

## Как читать

- **seconds** — длительность речи в файле, от первого до последнего звука (тишина по краям срезана по порогу −40 dB от пика). Это число ставится в кадр. **file_s** — полная длина файла (с хвостами ≈0,1–0,4 с).
- **shot_s** — длина кадра по раскадровке r4; **fit** — укладывается ли реплика в свой кадр. «over +N» — реплика длиннее кадра на N с: удлинить кадр, дать реплике перейти в соседний кадр (J/L-склейка) или ждать финального дубля.
- **wpm** — слов в минуту на этой длительности.
- **Модель персонажей — `eleven_v3`, stability 0.5 (Natural).** Голоса задизайнены на `eleven_ttv_v3` и на v3 звучат как на кастинге. На `eleven_v4`/`v4_turbo` те же voice_id «уезжают» вверх на 4–10 полутонов (бас Corr превращается в баритон) и читают быстрее (тяжёлые голоса — до 25 %). Прогон на `v4_turbo` сохранён как альтернатива (`alt/*_v4turbo.mp3`, столбец v4t в CSV).
- **Летописец — `eleven_multilingual_v2`**, speed 0.72 (фразы ~110 сл/мин) / 0.80 (фразы 2 и 4 Sc 5, ~120–125 сл/мин). Голос — **кандидат**, не закреплён (animatic.md §3 шаг 1). На одиночной фразе даже speed 0.70 даёт ~145 сл/мин; целевой темп набирается паузами между фразами в монтаже (карточка NARR-01). Альтернативы: `t2` (второй seed) и `v4t`.
- FIXED, `[LIPSYNC-CU]` и Летописец — по два дубля (t2 в `alt/`). Для 8 реплик основной дубль заменён лучшим по расшифровке (поле `note` в манифесте).
- Обрывы («since —», «The Seventh —», «…and the Ninth Sluice —») прочитаны до тире; точка реза — в монтаже (`emotion_markup.md` §4).
- L080 (sc15a-sh010, «…finds its level.») — хвост L079 поверх склейки, отдельного файла нет.
- Финальная озвучка — после picture lock, на модели по итогам A/B: длительности могут сместиться на ±10–15 %. Сетку строить с запасом.

## Сводка по сценам

| Сцена | Реплик | Речь, с (сумма) | Кадры с репликами, с | Реплик длиннее своего кадра | Сумма превышений, с |
|---|---|---|---|---|---|
| sc02 | 9 | 31.2 | 21.0 | 6 | 12.3 |
| sc03 | 10 | 20.5 | 27.5 | 2 | 1.9 |
| sc04 | 9 | 43.7 | 29.5 | 7 | 14.8 |
| sc05 | 6 | 33.1 | 42.5 | 0 | 0.0 |
| sc06 | 9 | 32.7 | 27.0 | 7 | 7.4 |
| sc07 | 4 | 25.5 | 23.0 | 3 | 5.3 |
| sc08 | 3 | 9.2 | 10.0 | 1 | 1.3 |
| sc09 | 3 | 5.7 | 17.0 | 0 | 0.0 |
| sc13 | 4 | 13.8 | 16.0 | 2 | 1.0 |
| sc10 | 11 | 36.6 | 36.0 | 5 | 6.0 |
| sc14 | 3 | 5.2 | 8.5 | 0 | 0.0 |
| sc11 | 2 | 12.2 | 9.0 | 1 | 6.0 |
| sc15 | 6 | 21.0 | 23.5 | 2 | 0.7 |
| sc15a | 2 | 2.5 | 4.5 | 0 | 0.0 |
| sc12 | 7 | 34.1 | 28.0 | 3 | 13.6 |
| sc17 | 2 | 3.5 | 7.0 | 0 | 0.0 |
| sc18 | 1 | 1.3 | 3.0 | 0 | 0.0 |
| sc19 | 13 | 33.8 | 43.5 | 2 | 2.4 |
| sc20 | 1 | 2.8 | 5.0 | 0 | 0.0 |
| **всего** | 105 | 368.5 | 381.5 | 41 | 72.8 |

## Все реплики (порядок монтажа)

| line | shot | TC | shot_s | персонаж | текст (EN, сценарий v1.0.2) | seconds | file_s | fit | wpm | альт. дубли, с | QA | файл |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L001 | sc02-sh030 | 1:16.5 | 3.5 | Tithe-collector | Ninth Sluice, fourth lane. Nan's house. Two months owing. | 5.52 | 5.6 | over +2.0 | 98 | v4t 5.1 | ok | `sc02-sh030_L001_V12_COLLECTOR.mp3` |
| L002 | sc02-sh040 | 1:20.0 | 2.5 | Tithe-collector | Six coppers by dusk. Or I take the nets. | 3.28 | 3.28 | over +0.8 | 165 | v4t 3.86 | ok | `sc02-sh040_L002_V12_COLLECTOR.mp3` |
| L003 | sc02-sh050 | 1:22.5 | 2.0 | Wick | Nan's drowned. | 1.28 | 2.08 | yes | 94 | v4t 1.4 | ok | `sc02-sh050_L003_V02_WICK.mp3` |
| L004 | sc02-sh060 | 1:24.5 | 2.0 | Tithe-collector | She drowned last month. | 1.38 | 2.08 | yes | 174 | v4t 1.6 | ok | `sc02-sh060_L004_V12_COLLECTOR.mp3` |
| L005 | sc02-sh070 | 1:26.5 | 2.5 | Wick | Drowned again. Took the money with her. Both times. | 4.66 | 4.72 | over +2.2 | 116 | v4t 3.9 | ok | `sc02-sh070_L005_V02_WICK.mp3` |
| L006 | sc02-sh080 | 1:29.0 | 2.5 | Nan | I'll drown you, you little eel! Get down off that bridge! | 5.36 | 5.44 | over +2.9 | 123 | v4t 4.04 | ok | `sc02-sh080_L006_V03_NAN.mp3` |
| L007 | sc02-sh100 | 1:33.0 | 1.5 | Tithe-collector | Dusk. | 0.72 | 1.2 | yes | 83 | v4t 0.84 | ok | `sc02-sh100_L007_V12_COLLECTOR.mp3` |
| L008 | sc02-sh140 | 1:41.5 | 1.5 | Wick | Six! We never found six in a week. | 2.7 | 2.72 | over +1.2 | 178 | v4t 3.38 | ok | `sc02-sh140_L008_V02_WICK.mp3` |
| L009 | sc02-sh180 | 1:52.5 | 3.0 | Pell | You want it found, you pay the mud. Mud doesn't do favours. | 6.28 | 6.4 | over +3.3 | 115 | t2 5.5, v4t 4.48 | см. QA | `sc02-sh180_L009_V01_PELL.mp3` |
| L010 | sc03-sh030 | 2:06.5 | 3.0 | Mags | Nothing left in Ninth Sluice but buttons, Pell! | 3.82 | 3.92 | over +0.8 | 126 | v4t 3.22 | ok | `sc03-sh030_L010_V11_MAGS.mp3` |
| L011 | sc03-sh040 | 2:09.5 | 2.0 | Wick | Count your own, Mags! | 1.96 | 2.08 | yes | 122 | v4t 1.84 | ok | `sc03-sh040_L011_V02_WICK.mp3` |
| L012 | sc03-sh070 | 2:18.0 | 2.5 | Wick | The old sill. Pell. You can see the stone. | 3.58 | 4.16 | over +1.1 | 151 | v4t 4.04 | см. QA | `sc03-sh070_L012_V02_WICK.mp3` |
| L013 | sc03-sh100 | 2:28.0 | 2.0 | Wick | It's only water. | 1.06 | 1.12 | yes | 170 | v4t 1.4 | ok | `sc03-sh100_L013_V02_WICK.mp3` |
| L014 | sc03-sh110 | 2:30.0 | 2.0 | Pell | Hold the rope. | 1.16 | 1.2 | yes | 155 | v4t 1.26 | ok | `sc03-sh110_L014_V01_PELL.mp3` |
| L015 | sc03-sh180 | 2:48.0 | 5.0 | Wick | Pell. Mouth. | 1.74 | 1.84 | yes | 69 | v4t 1.78 | ok | `sc03-sh180_L015_V02_WICK.mp3` |
| L016 | sc03-sh280 | 3:22.5 | 2.0 | Wick | It sang. | 1.34 | 1.84 | yes | 90 | v4t 1.1 | см. QA | `sc03-sh280_L016_V02_WICK.mp3` |
| L017 | sc03-sh290 | 3:24.5 | 5.0 | Pell | Stones don't sing. That's six coppers, that is. | 3.26 | 3.36 | yes | 147 | v4t 3.58 | ok | `sc03-sh290_L017_V01_PELL.mp3` |
| L018 | sc03-sh300 | 3:29.5 | 2.0 | Mags | What've you got, then? | 1.3 | 1.68 | yes | 185 | v4t 1.36 | см. QA | `sc03-sh300_L018_V11_MAGS.mp3` |
| L019 | sc03-sh320 | 3:33.5 | 2.0 | Pell | Buttons! | 1.26 | 1.36 | yes | 48 | v4t 1.14 | ok | `sc03-sh320_L019_V01_PELL.mp3` |
| L020 | sc04-sh040 | 4:10.0 | 3.5 | Nan | Fifteen years old and you still track silt across my floor. Sit. Eat. | 6.64 | 6.64 | over +3.1 | 117 | v4t 4.28 | ok | `sc04-sh040_L020_V03_NAN.mp3` |
| L021 | sc04-sh050 | 4:13.5 | 3.5 | Nan | And don't tell me what you found, I can see from here it was nothing. | 4.64 | 4.64 | over +1.1 | 194 | v4t 4.48 | ok | `sc04-sh050_L021_V03_NAN.mp3` |
| L022 | sc04-sh070 | 4:21.0 | 3.0 | Wick | Nan, the old sill's bare. Right down to the stone. And Pell, | 5.18 | 5.52 | over +2.2 | 139 | v4t 5.4 | см. QA | `sc04-sh070_L022_V02_WICK.mp3` |
| L023 | sc04-sh090 | 4:26.0 | 2.0 | Wick | — Pell found buttons. | 1.48 | 1.52 | yes | 122 | v4t 1.58 | см. QA | `sc04-sh090_L023_V02_WICK.mp3` |
| L024 | sc04-sh110 | 4:30.0 | 4.0 | Nan | The old sill. Bare. Not in my floods. Not in Ninth Sluice since — | 7.0 | 7.12 | over +3.0 | 111 | v4t 6.1 | ok | `sc04-sh110_L024_V03_NAN.mp3` |
| L025 | sc04-sh170 | 4:48.5 | 5.0 | Nan | Never sing, chick. Hum if you must, and only for the house. | 5.44 | 5.52 | over +0.4 | 132 | t2 5.08, v4t 4.64 | ok | `sc04-sh170_L025_V03_NAN.mp3` |
| L026 | sc04-sh200 | 4:59.0 | 4.0 | Nan | Chandler on the dike pays today. I'm back by dusk. And if that tithe-man comes early, you sit on the chest. | 8.84 | 8.88 | over +4.8 | 149 | v4t 7.54 | см. QA | `sc04-sh200_L026_V03_NAN.mp3` |
| L027 | sc04-sh230 | 5:08.5 | 2.0 | Wick | It answered you. | 2.04 | 2.16 | over +0.0 | 88 | v4t 1.42 | ok | `sc04-sh230_L027_V02_WICK.mp3` |
| L028 | sc04-sh250 | 5:14.5 | 2.5 | Pell | It's dusk's money. That's all it is. | 2.46 | 2.56 | yes | 171 | v4t 2.58 | ok | `sc04-sh250_L028_V01_PELL.mp3` |
| L029 | sc05-sh010 | 5:20.0 | 6.0 | The Chronicler | The First Voices raised the Spires. They are not heard now. | 4.5 | 4.69 | yes | 147 | t2 4.94, v4t 4.28 | ok | `sc05-sh010_L029_NARR01.mp3` |
| L030 | sc05-sh020 | 5:26.0 | 11.0 | The Chronicler | In the last year of the old kingdom, the nine warden families found Queen Neveh past reason, and her court with her. | 8.62 | 8.824 | yes | 153 | t2 7.9, v4t 7.92 | см. QA | `sc05-sh020_L030_NARR01.mp3` |
| L031 | sc05-sh060 | 5:46.0 | 5.5 | The Chronicler | She sang her city into the sea. | 3.24 | 3.251 | yes | 130 | t2 3.02, v4t 2.56 | ok | `sc05-sh060_L031_NARR01.mp3` |
| L032 | sc05-sh070 | 5:51.5 | 5.0 | The Chronicler | The Nine made their Concord on what stayed dry. | 4.18 | 4.226 | yes | 129 | t2 4.06, v4t 3.32 | ok | `sc05-sh070_L032_NARR01.mp3` |
| L033 | sc05-sh080 | 5:56.5 | 12.0 | The Chronicler | This is the three hundred and twelfth year of that Concord: three hundred and twelve years, each with its tithe, and each balance carried forward. | 9.94 | 11.239 | yes | 151 | t2 12.5, v4t 9.7 | ok | `sc05-sh080_L033_NARR01.mp3` |
| L034 | sc05-sh090 | 6:08.5 | 3.0 | The Chronicler | …and the water kept its counsel. | 2.6 | 2.833 | yes | 138 | t2 2.88, v4t 2.06 | ok | `sc05-sh090_L034_NARR01.mp3` |
| L035 | sc06-sh060 | 6:34.0 | 4.0 | Pell | Four coppers of that, if the rag-man's drunk. I want a half-walk for the other two. | 4.92 | 5.04 | over +0.9 | 220 | v4t 5.14 | ok | `sc06-sh060_L035_V01_PELL.mp3` |
| L036 | sc06-sh070 | 6:38.0 | 2.5 | Reedmaster (Corr) | No half-walks today. | 1.5 | 1.52 | yes | 160 | v4t 1.62 | ok | `sc06-sh070_L036_V10_CORR.mp3` |
| L037 | sc06-sh080 | 6:40.5 | 3.0 | Reedmaster (Corr) | Short a pin. Two wheels. Half the walks. | 3.2 | 3.2 | over +0.2 | 150 | v4t 3.88 | см. QA | `sc06-sh080_L037_V10_CORR.mp3` |
| L038 | sc06-sh090 | 6:43.5 | 3.0 | Reedmaster (Corr) | A wheel doesn't care who walks it. | 2.28 | 2.4 | yes | 184 | t2 2.36, v4t 2.32 | ok | `sc06-sh090_L038_V10_CORR.mp3` |
| L039 | sc06-sh100 | 6:46.5 | 3.0 | Reedmaster (Corr) | I've forty grown backs it doesn't care about, ahead of you. | 4.28 | 4.32 | over +1.3 | 154 | v4t 3.84 | ok | `sc06-sh100_L039_V10_CORR.mp3` |
| L040 | sc06-sh110 | 6:49.5 | 2.5 | Wick | So sing it dry. Like they do up the hill. | 3.08 | 3.12 | over +0.6 | 195 | v4t 3.0 | ok | `sc06-sh110_L040_V02_WICK.mp3` |
| L041 | sc06-sh150 | 6:58.0 | 4.5 | Reedmaster (Corr) | Reading's today. The Helm reads the map, up at the palace. Whoever reads that map decides who gets wet. | 7.84 | 7.84 | over +3.3 | 145 | v4t 7.46 | см. QA | `sc06-sh150_L041_V10_CORR.mp3` |
| L042 | sc06-sh160 | 7:02.5 | 3.0 | Reedmaster (Corr) | Come dusk we'll all know what Ninth Sluice is worth. | 3.94 | 4.0 | over +0.9 | 152 | v4t 3.44 | ok | `sc06-sh160_L042_V10_CORR.mp3` |
| L043 | sc06-sh200 | 7:12.0 | 1.5 | Reedmaster (Corr) | Listeners. | 1.66 | 1.76 | over +0.2 | 36 | v4t 0.96 | ok | `sc06-sh200_L043_V10_CORR.mp3` |
| L044 | sc07-sh020 | 7:22.5 | 6.0 | The Chronicler | The Tithe Map sets down who is sung first when the storm comes, and who after. | 6.88 | 7.245 | over +0.9 | 140 | t2 6.78, v4t 5.48 | ok | `sc07-sh020_L044_NARR01.mp3` |
| L045 | sc07-sh030 | 7:28.5 | 6.0 | The Chronicler | First Song. Second Song. Last Song. | 3.2 | 3.344 | yes | 112 | t2 3.58, v4t 4.1 | ok | `sc07-sh030_L045_NARR01.mp3` |
| L046 | sc07-sh050 | 7:38.5 | 5.0 | The Chronicler | Of the nine Spires, eight still answered. One of the eight answered badly. | 6.38 | 6.409 | over +1.4 | 122 | t2 7.76, v4t 5.66 | ok | `sc07-sh050_L046_NARR01.mp3` |
| L047 | sc07-sh060 | 7:43.5 | 6.0 | The Chronicler | By law the Helm reads the map aloud, and signs it; and the balance of that year was read on the sixth of Longdark. | 9.04 | 9.985 | over +3.0 | 159 | t2 10.34, v4t 8.04 | см. QA | `sc07-sh060_L047_NARR01.mp3` |
| L048 | sc08-sh030 | 8:06.5 | 4.0 | Choir attendant | Sing it flat for the lords, Lady Ione. They like to hear what they have paid for. | 5.34 | 5.44 | over +1.3 | 191 | v4t 4.44 | ok | `sc08-sh030_L048_V13_ATTENDANT.mp3` |
| L049 | sc08-sh040 | 8:10.5 | 3.0 | Ione | Is that what the song is for? | 1.8 | 2.24 | yes | 233 | v4t 1.64 | ok | `sc08-sh040_L049_V04_IONE.mp3` |
| L050 | sc08-sh050 | 8:13.5 | 3.0 | Choir attendant | It is what today is for. | 2.04 | 2.08 | yes | 176 | v4t 1.78 | ok | `sc08-sh050_L050_V13_ATTENDANT.mp3` |
| L051 | sc09-sh100 | 9:58.0 | 9.0 | Wick | Four. The rag-man robbed us. | 2.62 | 2.64 | yes | 137 | v4t 2.88 | см. QA | `sc09-sh100_L051_V02_WICK.mp3` |
| L052 | sc09-sh150 | 10:22.5 | 8.0 | Wick | It cares up there. | 1.46 | 2.0 | yes | 164 | v4t 1.5 | ok | `sc09-sh150_L052_V02_WICK.mp3` |
| L053 | sc09-sh150 | 10:22.5 | 8.0 | Pell | Water doesn't care who you are. | 1.62 | 1.68 | yes | 222 | t2 1.68, v4t 2.08 | ok | `sc09-sh150_L053_V01_PELL.mp3` |
| L054 | sc13-sh090 | 11:29.5 | 5.0 | Hollis | Forty-one lines. No deed-district. No street. No name against any of it. | 5.52 | 5.52 | over +0.5 | 152 | v4t 5.9 | см. QA | `sc13-sh090_L054_V05_HOLLIS.mp3` |
| L055 | sc13-sh100 | 11:34.5 | 3.0 | Hollis | And it adds. | 0.88 | 0.88 | yes | 205 | v4t 1.04 | ok | `sc13-sh100_L055_V05_HOLLIS.mp3` |
| L056 | sc13-sh120 | 11:40.5 | 5.0 | Hollis | A column that adds on the first cast is either honest or very well made. Again. | 5.52 | 5.52 | over +0.5 | 174 | v4t 5.14 | ok | `sc13-sh120_L056_V05_HOLLIS.mp3` |
| L057 | sc13-sh160 | 11:55.0 | 3.0 | Hollis | Not yet reconciled. | 1.9 | 2.08 | yes | 95 | v4t 1.84 | ok | `sc13-sh160_L057_V05_HOLLIS.mp3` |
| L058 | sc10-sh100 | 12:41.5 | 4.0 | Ruel | And that girl of yours? Still climbing my rigging when the watch isn't looking? | 4.48 | 4.56 | over +0.5 | 187 | v4t 4.26 | ok | `sc10-sh100_L058_V06_RUEL.mp3` |
| L059 | sc10-sh170 | 13:05.0 | 4.0 | Ruel | Pumps for the low sluices. It's all written down. You need only say yes. | 5.52 | 5.52 | over +1.5 | 152 | v4t 4.78 | ok | `sc10-sh170_L059_V06_RUEL.mp3` |
| L060 | sc10-sh190 | 13:12.0 | 3.5 | Lucan (the Helm) | You will have my answer when I have read. | 2.94 | 3.04 | yes | 184 | v4t 2.84 | ok | `sc10-sh190_L060_V07_LUCAN.mp3` |
| L061 | sc10-sh200 | 13:15.5 | 2.5 | Ruel | I know what you'll read. | 1.26 | 1.28 | yes | 238 | v4t 1.26 | ok | `sc10-sh200_L061_V06_RUEL.mp3` |
| L062 | sc10-sh210 | 13:18.0 | 2.5 | Ruel | Read it differently. | 1.58 | 1.6 | yes | 114 | v4t 1.28 | ok | `sc10-sh210_L062_V06_RUEL.mp3` |
| L063 | sc10-sh220 | 13:20.5 | 3.5 | Lucan (the Helm) | It is drawn, Ruel. I only read it. | 3.96 | 4.0 | over +0.5 | 121 | v4t 4.14 | ok | `sc10-sh220_L063_V07_LUCAN.mp3` |
| L064 | sc10-sh230 | 13:24.0 | 3.0 | Ruel | People live down there, old friend. | 2.04 | 2.08 | yes | 176 | v4t 2.38 | ok | `sc10-sh230_L064_V06_RUEL.mp3` |
| L065 | sc10-sh240 | 13:27.0 | 3.0 | Lucan (the Helm) | And you will lose this one. | 2.32 | 2.4 | yes | 155 | v4t 1.94 | ok | `sc10-sh240_L065_V07_LUCAN.mp3` |
| L066 | sc10-sh260 | 13:33.0 | 3.0 | Ruel | We go under and come up. | 1.98 | 2.08 | yes | 182 | t2 1.84, v4t 2.08 | ok | `sc10-sh260_L066_V06_RUEL.mp3` |
| L067 | sc10-sh310 | 13:49.0 | 3.0 | Ione | Helm. The Cantor's word: the water lies flat. | 3.94 | 4.0 | over +0.9 | 122 | v4t 4.52 | ok | `sc10-sh310_L067_V04_IONE.mp3` |
| L068 | sc10-sh360 | 14:03.0 | 4.0 | Ruel | Ione Ilvane. You've flattened my harbour. My captains will be bored. | 6.62 | 6.72 | over +2.6 | 100 | v4t 5.54 | см. QA | `sc10-sh360_L068_V06_RUEL.mp3` |
| L069 | sc14-sh120 | 14:50.0 | 2.5 | Clerk at the next desk | Yes, Kett? | 1.88 | 2.0 | yes | 64 | v4t 0.92 | см. QA | `sc14-sh120_L069_V16_CLERK.mp3` |
| L070 | sc14-sh140 | 14:56.0 | 3.0 | Hollis | The damp. It's getting into the paper. | 1.84 | 1.84 | yes | 228 | v4t 1.92 | ok | `sc14-sh140_L070_V05_HOLLIS.mp3` |
| L071 | sc14-sh160 | 15:02.0 | 3.0 | Clerk at the next desk | It gets into everything. | 1.52 | 1.52 | yes | 158 | v4t 1.78 | ok | `sc14-sh160_L071_V16_CLERK.mp3` |
| L072 | sc11-sh030 | 15:20.0 | 4.0 | Steward | The tithe cup. First the taster. Then the Helm. Then the guest of the reading. | 10.02 | 10.08 | over +6.0 | 90 | v4t 6.5 | ok | `sc11-sh030_L072_V17_STEWARD.mp3` |
| L073 | sc11-sh100 | 15:45.0 | 5.0 | Ruel | I don't drink before a storm. | 2.22 | 2.4 | yes | 162 | t2 1.98, v4t 2.32 | ok | `sc11-sh100_L073_V06_RUEL.mp3` |
| L074 | sc15-sh090 | 16:40.0 | 3.5 | Ursel | Mr Kett. You have cast it twice. | 3.52 | 3.52 | over +0.0 | 119 | v4t 3.32 | см. QA | `sc15-sh090_L074_V08_URSEL.mp3` |
| L075 | sc15-sh110 | 16:46.5 | 5.0 | Hollis | It balances, Dame Lantry. I can make it balance. What it is | 4.68 | 4.88 | yes | 154 | v4t 6.04 | ok | `sc15-sh110_L075_V05_HOLLIS.mp3` |
| L076 | sc15-sh120 | 16:51.5 | 3.0 | Hollis | is not yet reconciled. | 2.46 | 2.56 | yes | 98 | v4t 2.42 | ok | `sc15-sh120_L076_V05_HOLLIS.mp3` |
| L077 | sc15-sh140 | 16:57.5 | 3.5 | Ursel | Then you have done exactly what was asked, Hollis. | 4.18 | 4.24 | over +0.7 | 129 | v4t 3.56 | см. QA | `sc15-sh140_L077_V08_URSEL.mp3` |
| L078 | sc15-sh170 | 17:07.5 | 5.0 | Ursel | A clerk who is trusted gets a clip. | 3.5 | 3.52 | yes | 137 | t2 3.4, v4t 2.92 | ok | `sc15-sh170_L078_V08_URSEL.mp3` |
| L079 | sc15-sh190 | 17:15.5 | 3.5 | Ursel | All water finds its level. | 2.64 | 5.04 | yes | 114 | t2 2.66, v4t 2.3 | ok | `sc15-sh190_L079_V08_URSEL.mp3` |
| L080 | sc15a-sh010 | 17:44.0 | 4.0 | Ursel | …finds its level. |  |  |  |  |  |  | `— (tail of L079 (sc15-sh190) running over the cut into sc15a-sh010; no separate read)` |
| L081 | sc15a-sh070 | 18:05.0 | 2.5 | Wick | She said dusk. | 1.28 | 1.28 | yes | 141 | v4t 1.54 | ok | `sc15a-sh070_L081_V02_WICK.mp3` |
| L082 | sc15a-sh080 | 18:07.5 | 2.0 | Pell | So did he. | 1.2 | 1.2 | yes | 150 | v4t 0.94 | ok | `sc15a-sh080_L082_V01_PELL.mp3` |
| L083 | sc12-sh050 | 18:39.0 | 4.0 | Lucan (the Helm) | First Song. The Steps. The harbour and the roads. The First Sluice, through the Fourth. | 8.9 | 8.96 | over +4.9 | 101 | v4t 7.6 | см. QA | `sc12-sh050_L083_V07_LUCAN.mp3` |
| L084 | sc12-sh100 | 18:55.0 | 4.5 | Lucan (the Helm) | Second Song. The Mids, dike to dike. The Fifth Sluice. The Sixth. The Seventh — | 9.26 | 9.28 | over +4.8 | 91 | v4t 8.58 | см. QA | `sc12-sh100_L084_V07_LUCAN.mp3` |
| L085 | sc12-sh140 | 19:08.5 | 3.0 | Lucan (the Helm) | — the Seventh. | 1.38 | 1.84 | yes | 87 | v4t 1.92 | ok | `sc12-sh140_L085_V07_LUCAN.mp3` |
| L086 | sc12-sh180 | 19:20.5 | 5.0 | Lucan (the Helm) | Last Song. The Eighth Sluice. The Tenth. The Eleventh. The Twelfth. | 8.9 | 8.96 | over +3.9 | 74 | v4t 4.26 | ok | `sc12-sh180_L086_V07_LUCAN.mp3` |
| L087 | sc12-sh230 | 19:37.0 | 5.0 | Lucan (the Helm) | …and the Ninth Sluice — | 1.88 | 3.28 | yes | 128 | t2 2.92, v4t 2.36 | ok | `sc12-sh230_L087_V07_LUCAN.mp3` |
| L088 | sc12-sh300 | 20:04.0 | 3.0 | Ruel | Lucan. | 0.98 | 1.52 | yes | 61 | v4t 0.9 | ok | `sc12-sh300_L088_V06_RUEL.mp3` |
| L089 | sc12-sh310 | 20:07.0 | 3.5 | Ruel | A physician! His own physician, now! | 2.82 | 2.96 | yes | 128 | v4t 3.04 | ok | `sc12-sh310_L089_V06_RUEL.mp3` |
| L090 | sc17-sh060 | 22:12.0 | 3.0 | Relay-keeper | The tone came very quickly, my lord. | 1.74 | 1.84 | yes | 241 | v4t 2.26 | ok | `sc17-sh060_L090_V14_RELAYKEEPER.mp3` |
| L091 | sc17-sh090 | 22:21.5 | 4.0 | Lord of the Relay (Odo) | Nothing unheard. | 1.76 | 1.76 | yes | 68 | t2 1.68, v4t 1.7 | ok | `sc17-sh090_L091_V09_ODO.mp3` |
| L092 | sc18-sh100 | 23:12.0 | 3.0 | Rusk guard | Thirty days of this, then. | 1.26 | 1.36 | yes | 238 | v4t 1.78 | см. QA | `sc18-sh100_L092_V15_GUARD.mp3` |
| L093 | sc19-sh030 | 23:29.0 | 3.0 | Tithe-collector | Dusk. | 0.68 | 1.2 | yes | 88 | v4t 0.82 | ok | `sc19-sh030_L093_V12_COLLECTOR.mp3` |
| L094 | sc19-sh060 | 23:37.0 | 2.0 | Tithe-collector | Four. | 0.44 | 0.64 | yes | 136 | v4t 0.58 | ok | `sc19-sh060_L094_V12_COLLECTOR.mp3` |
| L095 | sc19-sh070 | 23:39.0 | 3.0 | Pell | Four now. Two when my nan's back. | 2.16 | 2.16 | yes | 194 | v4t 2.46 | см. QA | `sc19-sh070_L095_V01_PELL.mp3` |
| L096 | sc19-sh080 | 23:42.0 | 2.0 | Tithe-collector | Two now. | 0.5 | 1.04 | yes | 240 | v4t 0.74 | ok | `sc19-sh080_L096_V12_COLLECTOR.mp3` |
| L097 | sc19-sh120 | 23:54.0 | 2.5 | Wick | She said sit on it. | 1.68 | 1.76 | yes | 179 | v4t 1.8 | ok | `sc19-sh120_L097_V02_WICK.mp3` |
| L098 | sc19-sh130 | 23:56.5 | 2.5 | Tithe-collector | Off the chest, girl. | 1.36 | 2.24 | yes | 176 | v4t 1.92 | ok | `sc19-sh130_L098_V12_COLLECTOR.mp3` |
| L099 | sc19-sh170 | 24:08.0 | 3.0 | Pell | Wait. I can pay. | 1.72 | 1.76 | yes | 140 | v4t 1.68 | ok | `sc19-sh170_L099_V01_PELL.mp3` |
| L100 | sc19-sh230 | 24:24.5 | 2.5 | Tithe-collector | Three long. | 1.02 | 1.12 | yes | 118 | v4t 1.32 | ok | `sc19-sh230_L100_V12_COLLECTOR.mp3` |
| L101 | sc19-sh240 | 24:27.0 | 3.5 | Tithe-collector | That's the Helm. The Helm's dead. | 2.96 | 2.96 | yes | 122 | v4t 2.68 | ok | `sc19-sh240_L101_V12_COLLECTOR.mp3` |
| L102 | sc19-sh260 | 24:33.0 | 2.5 | Tithe-collector | Keep your nets. Tonight. | 2.46 | 2.56 | yes | 98 | v4t 2.08 | ok | `sc19-sh260_L102_V12_COLLECTOR.mp3` |
| L103 | sc19-sh300 | 24:46.5 | 3.0 | Wick | Pell. Who reads the map now? | 2.42 | 2.56 | yes | 149 | v4t 2.62 | ok | `sc19-sh300_L103_V02_WICK.mp3` |
| L104 | sc19-sh320 | 24:52.5 | 5.5 | The Chronicler | Helm Lucan Dask died on the sixth of Longdark, with the Tithe Map unsigned. | 7.92 | 7.941 | over +2.4 | 106 | t2 7.3, v4t 5.58 | ok | `sc19-sh320_L104_NARR01.mp3` |
| L105 | sc19-sh330 | 24:58.0 | 8.5 | The Chronicler | By law a Helm is chosen on the Still Days. There were thirty days, and a debt carried forward. | 8.52 | 8.545 | over +0.0 | 134 | t2 8.8, v4t 7.08 | ok | `sc19-sh330_L105_NARR01.mp3` |
| L106 | sc20-sh190 | 26:20.0 | 5.0 | Wick | Pell… it's singing back. | 2.82 | 2.96 | yes | 85 | t2 2.42, v4t 2.5 | см. QA | `sc20-sh190_L106_V02_WICK.mp3` |

## QA: автоматическая расшифровка (speech-to-text) расходится с текстом

Расшифровка — подсказка, а не истина: британское написание (favours/harbour/dike), цифры (41/30) и редкие имена STT часто «нормализует». Ниже — все расхождения основного дубля; содержательные отмечены в отчёте звукорежиссёра.

| line | персонаж | текст | STT услышал |
|---|---|---|---|
| L009 | Pell | You want it found, you pay the mud. Mud doesn't do favours. | You want it found, you pay the mud. Mud doesn't do favors |
| L012 | Wick | The old sill. Pell. You can see the stone. | The old sill, Pel. You can see the stone |
| L016 | Wick | It sang. | It's saying |
| L018 | Mags | What've you got, then? | What you got then? |
| L022 | Wick | Nan, the old sill's bare. Right down to the stone. And Pell, | Nan, the old sills bear right down to the stone. And Pel |
| L023 | Wick | — Pell found buttons. | El found buttons |
| L026 | Nan | Chandler on the dike pays today. I'm back by dusk. And if that tithe-man comes early, you sit on the chest. | Chandler on the dike pays today. I'm back by dusk, and if that tires man comes early, you sit on the chest |
| L030 | The Chronicler | In the last year of the old kingdom, the nine warden families found Queen Neveh past reason, and her court with her. | In the last year of the Old Kingdom, the nine Warden families found Queen Neve past reason and her court with her. |
| L037 | Reedmaster (Corr) | Short a pin. Two wheels. Half the walks. | Shorter pin, two wheels, half the walks |
| L041 | Reedmaster (Corr) | Reading's today. The Helm reads the map, up at the palace. Whoever reads that map decides who gets wet. | Readings today. The helm reads the map up at the palace. Whoever reads that map decides who gets wet |
| L047 | The Chronicler | By law the Helm reads the map aloud, and signs it; and the balance of that year was read on the sixth of Longdark. | By law, the helm reads the map aloud and signs it, and the balance of that year was read on the sixth of Long Dark. |
| L051 | Wick | Four. The rag-man robbed us. | Four, the Ragman robbed us |
| L054 | Hollis | Forty-one lines. No deed-district. No street. No name against any of it. | 41 lines no deed district no street no name against any of it |
| L068 | Ruel | Ione Ilvane. You've flattened my harbour. My captains will be bored. | Ione Ilvene, you flattened my harbor. My captains will be bored |
| L069 | Clerk at the next desk | Yes, Kett? | Yes, Cat? |
| L074 | Ursel | Mr Kett. You have cast it twice. | Mr. Ket, you have cashed it twice |
| L077 | Ursel | Then you have done exactly what was asked, Hollis. | Then you have done exactly what was asked, Tallis |
| L083 | Lucan (the Helm) | First Song. The Steps. The harbour and the roads. The First Sluice, through the Fourth. | First song, the steps, the harbor and the roads, the first sluice through the fourth |
| L084 | Lucan (the Helm) | Second Song. The Mids, dike to dike. The Fifth Sluice. The Sixth. The Seventh — | Second song. The mids, dyke to dyke. The fifth sluice, the sixth, the seventh |
| L092 | Rusk guard | Thirty days of this, then. | 30 days of this then |
| L095 | Pell | Four now. Two when my nan's back. | Four now. Two when Manon's back |
| L106 | Wick | Pell… it's singing back. | Oh, it's singing back |
