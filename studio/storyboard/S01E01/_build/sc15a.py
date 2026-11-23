from lib import S

L = '{LOWS_DUSK}'

SCENE = dict(
    title='SC 15a — Переулок при низком солнце: она решает', short='Пелл решает',
    start=1064, length=35,
    loc='PL-0008 переулок у дома Нан (D-02 C2/C1; DUSK-переход, вода возвращается)',
    time='низкое солнце',
    chars='{PELL} CH-0001 · {COLLECTOR} B-06 (далеко) · соседка (силуэт в двери) · Уик [OS]',
    axis='как sc02 (C2, смотрим на СЗ): сборщик слева, идёт слева направо от двери к двери («четыре двери… три двери»); дорога на дамбу — справа (СВ), Нан придёт оттуда. Пелл сидит на мостках, ноги над краем, лицом к камере',
    water='прилив возвращается: язык серой воды ползёт под сваи слева направо',
    light='верхние этажи и небо золотые; переулок в тени, холодный; первые фонари справа',
    accent='янтарь первых фонарей', mood='ожидание, решение',
    mode='LA', vertical='—',
    notes=['Камень не в кадре: пальцы сжимают шнурок через плащ (sh090).'],
    checks=['Сцена со шнурком между sc15 (без перстня) и sc12 (вставок перстня нет, левая рука Руэла ниже кромки стола до падения).'],
)

SHOTS = [
    S(4, 'insert', 'низко у ила, статика', 'Прилив возвращается: под сваями язык серой воды ползёт по утреннему илу, заполняет след, следующий', 'URSEL [OS, хвост sc15]: «…finds its level.» · SFX: вода ползёт, доски', 'A', 'L-16 (кромка воды ползёт слева направо) + L-10', 'D-02; W-1',
      'Low insert at silt level between tarred stilts: a thin tongue of grey water sliding over wet mud with footprints in it, the first footprint filling, warm gold light on the pilings above. No people. ' + L,
      '', 'вода слева направо', nochar=True),
    S(4, 'WS', 'eye-level (C2), статика', 'Пластина переулка из sc02 — мокрее, с золотой кромкой. Пелл сидит на мостках, ноги свешены; тряпка открыта на колене', 'SFX: стук в дверь далеко слева; счёт колеса вдали', 'A', 'L-10 + L-01 0.02', 'D-02 C2 DUSK; CH-0001',
      'Wide shot of a narrow lane of stilt-houses at low sun: the same doorpost with tide-marks on the right, water returning under the plank-walk, gold light on upper storeys, the lane in shade; {PELL} sits on the edge of the plank-walk with her feet over the edge, an open rag on her knee. ' + L,
      '', 'Пелл по центру лицом к камере', key='lane15a'),
    S(4, 'insert', 'eye-level, статика', 'Пересчитывает четыре монеты из руки в руку. Всё ещё четыре', 'SFX: медь', 'A', 'L-12 (монеты в левой / в правой) + L-19', 'CH-0001',
      'Insert: four worn copper coins in a girl\'s mud-dark cupped hand, the other hand open below it, an open patched rag on her knee, low gold light. ' + L,
      '', '—', l12=1),
    S(3.5, 'WS', 'eye-level, статика', 'Через четыре двери — сланцево-серная табарда. Женщина без слова протягивает из двери котелок; сборщик вешает его на руку к остальным и идёт к следующей двери. Стук. Три двери', 'SFX: стук; котелки звякают', 'B', 'резерв: L-04', 'B-06; C-03 b; D-02',
      'Wide shot along a plank-walk of stilt-houses at low sun: far off, {COLLECTOR} small in frame at a doorway, a woman\'s arm handing a cooking-pot out of the door, two pots already hanging on his arm. No readable faces. ' + L,
      'static camera; he takes the pot, hangs it on his arm and walks one door closer, from left to right.', 'сборщик слева, идёт вправо'),
    S(2, 'MCU', 'eye-level, статика', 'Пелл глядит на него', '—', 'A', 'L-12 (взгляд влево)', 'CH-0001',
      'Medium close-up of {PELL} sitting on a plank-walk, head turned to the left, calculating squint, low gold light from behind. ' + L,
      '', 'смотрит влево', l12=1, key='pell15a'),
    S(3.5, 'WS', 'вдоль мостков на СВ, статика', 'Она смотрит в другую сторону, вдоль мостков к дороге на дамбу. Зажигают фонари. Маленькой сгорбленной фигуры с тюком нет', 'SFX: фонари, голоса далеко', 'A', 'L-09 (фонари загораются по очереди к камере) + L-08', 'D-02 C1 DUSK',
      'Wide view along plank-walks of a stilt town toward a brick dike road, first lanterns being lit in doorways one by one, water in the lanes, empty walkway, no one coming. ' + L,
      '', 'смотрим вправо-вглубь (СВ)', nochar=True),
    S(2.5, 'MCU', 'eye-level, статика', 'Пелл', 'WICK [OS] (из двери за ней; не шутит): «She said dusk.»', 'A', 'L-12', 'CH-0001', '', '', 'смотрит вправо', reuse='pell15a'),
    S(2, 'MCU', 'eye-level, статика', 'Пелл', 'PELL [MS]: «So did he.»', 'A', 'L-12 (рот мелко)', 'CH-0001', '', '', 'смотрит вправо', reuse='pell15a', l12=1),
    S(4.5, 'CU', 'eye-level, статика', 'Немо. Рука идёт к вороту. На этот раз она знает, что делает. Пальцы смыкаются на шнурке сквозь плащ — и не разжимаются. Камня не видно. Она решила', '—', 'B', 'резерв: L-12 (рука у ворота / пальцы сжаты)', 'CH-0001',
      'Close-up of {PELL}, her mud-dark hand at the collar of her oilskin gripping a thin cord through the cloth, the stone not visible, stubborn defiance, jaw set, eyes level, low gold rim light. ' + L,
      'static camera; her fingers slowly close tight on the cord through the cloth and stay closed; her jaw sets.', 'смотрит вправо', tags=('cord',)),
    S(5, 'EWS', 'снизу на СВ, статика', 'Вверх по холму, маленький на последнем солнце, — дворец', 'SFX: тишина переулка', 'A', 'L-01 0.03', 'D-01 A LATE-AFT',
      'View from a stilt town up a hill to the northeast: a pale granite palace on the summit small against the last gold sunlight, a dark colossal spire beside it, no glow, brick dike below in shade. No people. ' + L,
      '', 'дворец по центру', nochar=True),
]
