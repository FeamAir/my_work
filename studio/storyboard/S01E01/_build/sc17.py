from lib import S

D = 'dusk light from a narrow window, a single warm oil lamp, cold grey stone'

SCENE = dict(
    title='SC 17 — Город слышит: Ступени', short='Ретрансляция',
    start=1314, length=45,
    loc='PL-0012 Дом Слушания, комната ретрансляции (D-12 R1/R2; DUSK + лампа)',
    time='сумерки',
    chars='{ODO} CH-0010 (без имени вслух) · смотритель ретрансляции (спина, C-08 №1)',
    axis='стена клеток фронтально (R1); Одо в центре комнаты, смотрит на стену (влево), смотритель у его правого локтя (справа, спиной). Брошь «заячье ухо» — на ПРАВОМ вороте Одо (слева в кадре анфас)',
    water='—',
    light='узкое окно с сумерками + одна масляная лампа; камни чёрные, блики дрожат, без свечения',
    accent='серно-жёлтая подкладка Фенника (мелко)', mood='спокойствие хозяина',
    mode='LA', vertical='—',
    notes=[
        'Одо одет полностью — для улицы и для совета, свиток совета под мышкой.',
        'Музыка: с этой сцены до конца sc19 — тихий пульс M09, не в низком регистре; один удар пропущен, когда камень остановлен.',
        'Камень останавливается мгновенно, посреди звона; остальные звенят вокруг пробела.',
    ],
    checks=['Склейка по форме: остановленный камень (sh130) → железный засов (sc18).'],
)

SHOTS = [
    S(5, 'WS', 'фронтально (R1), статика', 'Стена маленьких клеток от пола до балки, в каждой камень — все звенят: три тона, пауза, три тона. Воздух дрожит', 'SFX: тон смерти стеной. MUSIC: M09 пульс входит', 'A', 'VFX-RELAY-SHIMMER (на каждом камне, со сдвигом фаз) + L-01 0.02', 'D-12 R1 DUSK; E-11',
      'Dusk, frontal wide shot of a narrow tall stone relay room: one whole wall is a grid of small wrought-iron cradles each holding a dark glassy faceted stone, a keeper\'s slanted desk with a logbook, pigeon-hole slots full of paper slips, a narrow window with dusk light, one oil lamp. No people. The stones do not glow. ' + D,
      '', 'стена фронтально', nochar=True, key='wall'),
    S(3, 'insert', 'eye-level, статика', 'Клетки дрожат от звука; блики', 'SFX: звон', 'B', 'резерв: VFX-RELAY-SHIMMER + L-05 1 px', 'E-11',
      'Dusk, insert of several small wrought-iron cradles on a wall, each holding a dark faceted glassy stone, lamplight glinting on the facets. The stones do not glow. ' + D,
      'static camera; the small iron cradles rattle and tremble from the sound, the stones shiver in them, glints of lamplight jump on the facets. The stones do not glow.', '—', nochar=True, key='cages'),
    S(4, 'MS', 'eye-level, статика', 'Посреди всего этого маленький человек — как у себя в гостиной: худой, бритая голова, бледный. Сланец с серной подкладкой; серебряная брошь «заячье ухо» на правом вороте. Одет полностью, свиток совета под мышкой', 'SFX: звон', 'A', 'L-12 (моргание)', 'CH-0010; D-12 R1',
      'Dusk, medium shot of {ODO} standing in the middle of a stone room before a wall of caged stones, three-quarter view facing left, fully dressed for the street, a rolled council scroll under his left arm, hands otherwise hidden in his sleeves, half-lidded calm. ' + D,
      '', 'смотрит влево (на стену)', key='odo'),
    S(3, 'insert', 'eye-level, статика', 'Свиток совета под мышкой; брошь-ухо на правом вороте', '—', 'A', 'L-01 0.03', 'CH-0010',
      'Dusk, insert: a rolled council scroll tucked under the arm of a slate-grey robe with sulphur-yellow lining at the cuff, a small silver brooch shaped like an upright hare\'s ear on the collar. ' + D,
      '', '—'),
    S(3, 'MS', 'сзади, статика', 'Смотритель ретрансляции (спина) мнётся у его локтя', '—', 'A', 'L-12', 'C-08 №1',
      'Dusk, medium shot from behind of a relay-keeper in a slate-grey coat with yellow lining standing at someone\'s elbow, a small tone-fork on a cord, head bowed. ' + D,
      '', 'спиной; справа от Одо', l12=1, key='keeper'),
    S(3, 'MS', 'eye-level, статика', 'Одо слушает', 'KEEPER [OS] (неуверенно): «The tone came very quickly, my lord.»', 'A', 'L-12', 'CH-0010', '', '', 'смотрит влево', reuse='odo'),
    S(4, 'MCU', 'eye-level, статика', 'Маленький человек рассматривает стену камней, как рассматривают класс детей', '—', 'A', 'L-12 (полуприкрытые веки)', 'CH-0010',
      'Dusk, medium close-up of {ODO}, three-quarter view facing left, heavy-lidded pale grey eyes half closed, head tilted a little, a harmless faint smile. ' + D,
      '', 'смотрит влево', key='odo_mcu'),
    S(2.5, 'insert', 'сзади, статика', 'Руки смотрителя мнут рукав', '—', 'A', 'L-12', 'C-08 №1', '', '', '—', reuse='keeper', l12=1),
    S(4, 'MCU', 'eye-level, статика', 'Одо, мягко, почти шёпотом, очень медленно', 'THE LORD OF THE RELAY [MS] (мягко, почти шёпот; придворные гласные) FIXED: «Nothing unheard.»', 'A', 'L-12 (рот едва) + L-01 0.05 (EMO-PUSH)', 'CH-0010', '', '', 'смотрит влево', reuse='odo_mcu', l12=1),
    S(3.5, 'insert', 'eye-level, статика', 'Он кладёт один палец на ближний камень', '—', 'C', 'резерв: два кадра', 'CH-0010; E-11',
      'Dusk, insert: a pale slender hand emerging from a slate-grey sleeve with sulphur-yellow lining, one finger reaching toward a dark faceted stone in a wrought-iron cradle. ' + D,
      'static camera; the finger touches the stone and rests on it. Hand keeps five fingers.', 'рука справа'),
    S(3, 'insert', 'eye-level, статика', 'Он замолкает посреди звона. Остальные звенят вокруг пробела', 'SFX: этот камень — мгновенный обрыв; стена звенит дальше. MUSIC: один удар пропущен', 'A', 'VFX-RELAY-SHIMMER с обрывом на одном камне', 'E-11', '', '', '—', reuse='cages'),
    S(4, 'WS', 'фронтально, статика', 'Стена звенит вокруг пробела; Одо мал перед ней', 'SFX: звон', 'A', 'L-01 0.02 + VFX-RELAY-SHIMMER', 'D-12 R1; CH-0010', '', '', 'Одо по центру', reuse='wall'),
    S(3, 'CU', 'статика', 'Остановленный камень — неподвижен', '—', 'A', 'L-01 0.03; склейка по форме → засов sc18', 'E-11',
      'Dusk, close-up of a single dark faceted glassy stone in a wrought-iron cradle, perfectly still, lamplight on one facet. The stone does not glow. ' + D,
      '', 'горизонталь (= засов)', nochar=True),
]
