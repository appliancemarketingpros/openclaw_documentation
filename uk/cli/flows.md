---
title: Потоки (переспрямування)
source_url: https://docs.openclaw.ai/uk/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

Команди верхнього рівня `openclaw flows` немає. Постійна перевірка TaskFlow розташована в `openclaw tasks flow`.

## Підкоманди

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Підкоманда | Опис | Аргументи / параметри  
---|---|---  
`list` | Показати відстежувані TaskFlows. | `--json` машиночитаний вивід; фільтр `--status <name>` (див. значення статусів нижче).  
`show` | Показати один TaskFlow. | `<lookup>` — ідентифікатор потоку або ключ власника; `--json` машиночитаний вивід.  
`cancel` | Скасувати запущений TaskFlow. | `<lookup>` — ідентифікатор потоку або ключ власника.  
  
`<lookup>` приймає або ідентифікатор потоку (повернений `list` / `show`), або ключ власника потоку (стабільний ідентифікатор, який підсистема-власник використовує для відстеження потоку).

### Значення фільтра статусу

`--status` у `list` приймає одне з таких значень:

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## Приклади

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

Повний опис концепцій TaskFlow і створення див. у [TaskFlow](</uk/automation/taskflow>). Батьківську команду `tasks` див. у [довіднику CLI для tasks](</uk/cli/tasks>).

## Пов’язане

  * [Довідник CLI](</uk/cli>)
  * [Автоматизація](</uk/automation>)
  * [TaskFlow](</uk/automation/taskflow>)


Was this useful?YesNo