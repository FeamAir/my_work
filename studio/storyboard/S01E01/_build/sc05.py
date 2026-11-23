from lib import S

W = '{CHRONICLE}'

SCENE = dict(
    title='SC 5 — Гобелен «Разлом» · титр', short='Гобелен + титр',
    start=320, length=60.5,
    loc='гобелен в PL-0013 (только детали, комнату не видим) — панели E-06',
    time='вне времени (Летопись)',
    chars='только тканые фигуры; Летописец [VO]',
    axis='плоская ткань, ось не задействована; камера — только движение по плите. Внутри ткани ничего не движется',
    water='тканое море: панель 1 — под башней; панель 6 — море встаёт за Королевой',
    light='ровный свет на ткани (модуль CHRONICLE); STYLE_BASE не добавляется; негатив + «anime character, cel shading, 3D»',
    accent='выцветший индиго / марена ткани', mood='архив, сухо',
    mode='LA only', vertical='—',
    notes=[
        'Шесть панелей в порядке выдержки; спирали бордюра — по солнцу (по часовой от центра наружу, как видит зритель). Жемчужина (панель 3) и кулак (панель 4) — разные кадры, без сплит-скрина.',
        'Панели 3, 4 и 6 — только внутри серии (не в маркетинге до S10E10).',
        'Склейка по форме sc04-sh260 (камень) → sh010 (тканая башня). Жемчужина — через две панели (sh030).',
        'Текст Летописца — слово в слово (выдержка §2). Решение режиссёра r4 по хронометражу: фраза 2 целиком под панелью 2 (11 с); панели 3–5 молчат по 3 с; фраза 4 делится по своей точке на два кадра — «The Nine made their Concord on what stayed dry.» под наездом на девять знамён (повтор плиты панели 2, $0) и остаток под отъездом от всего гобелена (12 с); титр 9 с (3 такта темы) вместо 12. Темп Летописца: фразы 1, 3, 5 — ~110 сл/мин, фразы 2 и 4 — ~120–125 сл/мин (сухо, без ускорения на цифрах). Сцена 60,5 с (+6,5 с), разница снята в Sc 6–8; Корона по-прежнему 9:04.',
        'Внутри ткани ничего не движется; допустим только слой пыли в свете перед тканью (L-07, малая плотность) на панелях 1, 2, 6 — чтобы 40 с LA не читались как слайд-шоу.',
        'Титр HOLLOWSTONE 6:11.5–6:20.5 поверх тканой башни; бейдж AI — только с этого момента, мелко в углу.',
    ],
    checks=['Последний кадр титра → склейка по форме на ступицу колеса sc06-sh010 (центр кадра).'],
)

SHOTS = [
    S(6, 'панель 1', 'вертикальная панорама вниз', 'Чёрная башня в нитках поднимается из тканого моря; камера спускается к подножию: Королева поёт, венец из раковины, жемчуг и бирюза; за ней толпы, ряд за рядом, маленькие рты открыты. В бордюре спирали — все по солнцу', 'SFX: сухо переворачивается страница. MUSIC: M05 Archive. CHRONICLER [VO] FIXED: «The First Voices raised the Spires. They are not heard now.»', 'A', 'L-03 (вниз по высокой плите) + L-07 (пыль перед тканью)', 'E-06 панель 1',
      W + '. Tall panel: a black tower woven in thread rising from a stylised woven sea; at its foot a queen in pearl and teal robes with a spiral-shell circlet stands singing with her right hand raised, and behind her great crowds of common people with open mouths, rows upon rows; a border of small spiral shells turning clockwise from the centre outward.',
      '', 'вниз по башне', refplate=True, nochar=True),
    S(11, 'панель 2', 'панорама слева направо', 'Девять знамён на берегу; девять семей под ними, лицом к башне', 'CHRONICLER [VO] FIXED: «In the last year of the old kingdom, the nine warden families found Queen Neveh past reason, and her court with her.»', 'A', 'L-02 (ease, медленнее: 11 с) + L-07 (пыль перед тканью)', 'E-06 панель 2',
      W + '. Wide panel: nine noble figures in a row on a shore under nine tall vertical banners with a slanted cut at the bottom, each with a flat simple emblem, raising their hands in an oath, facing a black tower; no weapons.',
      '', 'слева направо', refplate=True, nochar=True, key='panel2'),
    S(3, 'панель 3', 'медленный наезд', 'Крупно в ткани: поющая рука Королевы. На ней — чёрная жемчужина', '— (без стинга)', 'A', 'L-01 0.05', 'E-06 панель 3',
      W + '. Close woven detail: a raised woman\'s open hand with a ring bearing one black pearl, a sleeve of pearl and teal.',
      '', '—', refplate=True, nochar=True),
    S(3, 'панель 4', 'панорама вправо', 'Следующая панель: девочка-служанка, наполовину за колонной. Коса слева. Спиральная раковина прижата к груди одной рукой. Другая рука — сжатый кулак', '—', 'A', 'L-02 (малая)', 'E-06 панель 4',
      W + '. Panel: a slight servant girl half hidden behind a pillar, one long braid on her own left side, holding a spiral seashell against her chest with one arm, her other hand clenched in a closed fist.',
      '', '—', refplate=True, nochar=True),
    S(3, 'панель 5', 'панорама вправо', 'Парус с бакланом поперёк устья гавани. Корабли в море', '—', 'A', 'L-02', 'E-06 панель 5',
      W + '. Panel: ships out at sea across a harbour mouth, the largest sail bearing a black diving cormorant, no shore, no people ashore.',
      '', '—', refplate=True, nochar=True),
    S(5.5, 'панель 6', 'медленный подъём', 'Королева одна на венце башни, маленькая, поёт. Внизу толпа из панели 1 лежит: маленькие фигуры в ткани. За ней встаёт море', 'CHRONICLER [VO] FIXED [ECHO]: «She sang her city into the sea.»', 'A', 'L-03 (вверх, медленно) + L-07 (пыль перед тканью)', 'E-06 панель 6',
      W + '. Tall panel: a queen alone at the very top of a tall black tower, singing, nobody beside her; far below at the foot of the tower the crowd lies fallen, stylised and still; the sea rising up behind her.',
      '', 'вверх к Королеве', refplate=True, nochar=True, key='panel6'),
    S(5, 'панель 2', 'медленный наезд', 'Снова девять знамён на берегу — медленный наезд к середине ряда, все девять знамён остаются в кадре', 'CHRONICLER [VO] FIXED [ECHO] (начало фразы 4): «The Nine made their Concord on what stayed dry.»', 'A', 'L-01 0.08 по плите панели 2', 'E-06 панель 2', '', '', 'к центру ряда', reuse='panel2'),
    S(12, 'весь гобелен', 'отъезд', 'Камера отъезжает, пока шесть панелей не становятся одной тусклой тканью', 'CHRONICLER [VO] FIXED [ECHO] (конец фразы 4): «This is the three hundred and twelfth year of that Concord: three hundred and twelve years, each with its tithe, and each balance carried forward.»', 'A', 'L-01 отъезд 0.5 по сборной плите (6 панелей, монтаж)', 'E-06 панели 1–6',
      '— (сборная плита из шести утверждённых панелей, без генерации)', '', '—', refplate=True, nochar=True),
    S(3, 'панель 6', 'наезд', 'Чёрная башня последней панели заполняет кадр', 'CHRONICLER [VO] FIXED: «…and the water kept its counsel.» (наименьшая пауза перед)', 'A', 'L-01 наезд 0.3', 'E-06 панель 6', '', '', 'башня по центру', reuse='panel6'),
    S(9, 'титр', 'статика', 'ТИТР: HOLLOWSTONE поверх тканой башни (6:11.5–6:20.5). Последний кадр — склейка на ступицу колеса', 'MUSIC: T-TITLE — тема саги, первое проведение, 9 с (3 такта; перенарезка композитора)', 'A', 'L-01 0.02 + титр (монтаж)', 'E-06 панель 6', '', '', 'центр кадра (= ступица sc06)', reuse='panel6'),
]
