---
title: Потоки (перенаправление)
source_url: https://docs.openclaw.ai/ru/cli/flows
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw tasks flow`

Команды верхнего уровня `openclaw flows` нет. Долговременная инспекция TaskFlow находится в `openclaw tasks flow`.

## Подкоманды

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Подкоманда | Описание | Аргументы / параметры  
---|---|---  
`list` | Список отслеживаемых TaskFlow. | `--json` машиночитаемый вывод; фильтр `--status <name>` (см. значения статуса ниже).  
`show` | Показать один TaskFlow. | `<lookup>` идентификатор flow или ключ владельца; `--json` машиночитаемый вывод.  
`cancel` | Отменить выполняющийся TaskFlow. | `<lookup>` идентификатор flow или ключ владельца.  
  
`<lookup>` принимает либо идентификатор flow (возвращается `list` / `show`), либо ключ владельца flow (стабильный идентификатор, который владеющая подсистема использует для отслеживания flow).

### Значения фильтра статуса

`--status` в `list` принимает одно из:

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## Примеры

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

Полное описание концепций TaskFlow и руководства по созданию см. в [TaskFlow](</ru/automation/taskflow>). О родительской команде `tasks` см. [справочник CLI tasks](</ru/cli/tasks>).

## Связанное

  * [справочник CLI](</ru/cli>)
  * [Автоматизация](</ru/automation>)
  * [TaskFlow](</ru/automation/taskflow>)


Was this useful?YesNo

Open issue