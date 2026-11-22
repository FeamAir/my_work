# Команда студии

| Роль | Агент | Папка | Должностная инструкция |
|---|---|---|---|
| Директор студии (ведущий) | основная сессия Claude | `studio/reports/`, `studio/status.md` | — |
| Сценарист | `screenwriter` | `studio/story/` | `.claude/agents/screenwriter.md` |
| Режиссёр-постановщик | `anime-director` | `studio/direction/` | `.claude/agents/anime-director.md` |
| IT-специалист | `it-engineer` | `pipeline/` | `.claude/agents/it-engineer.md` |
| Звукорежиссёр | `sound-director` | `studio/sound/` | `.claude/agents/sound-director.md` |

Порядок работы: директор ставит задачу → агент работает в своей папке → пишет отчёт в `studio/reports/` → директор принимает, коммитит и обновляет `studio/status.md`.

Инвестор читает `studio/status.md` и отчёты. В управлении не участвует.
