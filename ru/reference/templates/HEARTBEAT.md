---
title: Шаблон HEARTBEAT.md
source_url: https://docs.openclaw.ai/ru/reference/templates/HEARTBEAT
scraped_at: 2026-06-29
---

ReferenceTemplates

# Шаблон HEARTBEAT.md

`HEARTBEAT.md` находится в рабочей области агента. Оставьте файл пустым или содержащим только Markdown-комментарии и заголовки, если хотите, чтобы OpenClaw пропускал вызовы модели Heartbeat.

Шаблон среды выполнения по умолчанию:

markdownCopy code
[code]
    # Keep this file empty (or with only comments) to skip heartbeat API calls. # Add tasks below when you want the agent to check something periodically.
[/code]

Добавляйте короткие задачи под комментариями только тогда, когда хотите, чтобы агент периодически что-то проверял. Делайте инструкции Heartbeat краткими, потому что они читаются при повторяющихся пробуждениях.

## См. также

  * [Конфигурация Heartbeat](</ru/gateway/config-agents>)


Was this useful?YesNo

Open issue