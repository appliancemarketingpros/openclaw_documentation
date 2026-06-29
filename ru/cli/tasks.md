---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/ru/cli/tasks
scraped_at: 2026-06-29
---

ReferenceCLI commands

Проверяйте устойчивые фоновые задачи и состояние Task Flow. Без подкоманды `openclaw tasks` эквивалентна `openclaw tasks list`.

См. [Фоновые задачи](</ru/automation/tasks>), чтобы узнать о жизненном цикле и модели доставки.

## Использование

bashCopy code
[code]
    openclaw tasksopenclaw tasks listopenclaw tasks list --runtime acpopenclaw tasks list --status runningopenclaw tasks show <lookup>openclaw tasks notify <lookup> state_changesopenclaw tasks cancel <lookup>openclaw tasks auditopenclaw tasks maintenanceopenclaw tasks maintenance --applyopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## Корневые параметры

  * `--json`: вывод JSON.
  * `--runtime <name>`: фильтр по виду: `subagent`, `acp`, `cron` или `cli`.
  * `--status <name>`: фильтр по статусу: `queued`, `running`, `succeeded`, `failed`, `timed_out`, `cancelled` или `lost`.


## Подкоманды

### `list`

bashCopy code
[code]
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
[/code]

Перечисляет отслеживаемые фоновые задачи, начиная с самых новых.

### `show`

bashCopy code
[code]
    openclaw tasks show <lookup> [--json]
[/code]

Показывает одну задачу по ID задачи, ID запуска или ключу сессии.

### `notify`

bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

Изменяет политику уведомлений для выполняющейся задачи.

### `cancel`

bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

Отменяет выполняющуюся фоновую задачу.

### `audit`

bashCopy code
[code]
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
[/code]

Выявляет устаревшие, потерянные, не доставленные или иным образом несогласованные записи задач и Task Flow. Потерянные задачи, сохраняемые до `cleanupAfter`, считаются предупреждениями; истекшие или потерянные задачи без метки считаются ошибками.

### `maintenance`

bashCopy code
[code]
    openclaw tasks maintenance [--apply] [--json]
[/code]

Предварительно просматривает или применяет согласование задач и Task Flow, проставление меток очистки, удаление старых записей и очистку реестра сессий устаревших запусков cron. Для задач cron согласование использует сохраненные журналы запусков/состояние задания перед тем, как пометить старую активную задачу как `lost`, поэтому завершенные запуски cron не превращаются в ложные ошибки аудита только из-за того, что состояние in-memory рантайма Gateway исчезло. Офлайн-аудит CLI не является авторитетным источником для process-local набора активных cron-заданий Gateway. Задачи CLI с ID запуска/ID источника помечаются как `lost`, когда их live-контекст запуска Gateway исчез, даже если старая строка дочерней сессии остается. При применении обслуживание также удаляет из реестра сессий строки `cron:<jobId>:run:<uuid>`, которые старше 7 дней, сохраняя текущие выполняющиеся cron-задания и оставляя строки не-cron сессий без изменений.

### `flow`

bashCopy code
[code]
    openclaw tasks flow list [--status <name>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Проверяет или отменяет устойчивое состояние Task Flow в журнале задач.

## См. также

  * [Справочник CLI](</ru/cli>)
  * [Фоновые задачи](</ru/automation/tasks>)


Was this useful?YesNo

Open issue