---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/ru/cli/commitments
scraped_at: 2026-06-29
---

ReferenceCLI commands

Список и управление выведенными последующими обязательствами.

Обязательства — это включаемые явно, краткоживущие последующие воспоминания, создаваемые из контекста разговора. См. [Выведенные обязательства](</ru/concepts/commitments>) для концептуального руководства.

Без подкоманды `openclaw commitments` выводит список ожидающих обязательств.

## Использование

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## Параметры

  * `--all`: показать все статусы, а не только ожидающие обязательства.
  * `--agent <id>`: отфильтровать по одному идентификатору агента.
  * `--status <status>`: отфильтровать по статусу. Значения: `pending`, `sent`, `dismissed`, `snoozed` или `expired`.
  * `--json`: вывести машиночитаемый JSON.


## Примеры

Вывести ожидающие обязательства:

bashCopy code
[code]
    openclaw commitments
[/code]

Вывести все сохраненные обязательства:

bashCopy code
[code]
    openclaw commitments --all
[/code]

Отфильтровать по одному агенту:

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

Найти отложенные обязательства:

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

Отклонить одно или несколько обязательств:

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

Экспортировать как JSON:

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## Вывод

Текстовый вывод включает:

  * идентификатор обязательства
  * статус
  * тип
  * самое раннее время наступления срока
  * область действия
  * предлагаемый текст проверки состояния


Вывод JSON также включает путь к хранилищу обязательств и полные сохраненные записи.

## Связанные материалы

  * [Выведенные обязательства](</ru/concepts/commitments>)
  * [Обзор памяти](</ru/concepts/memory>)
  * [Heartbeat](</ru/gateway/heartbeat>)
  * [Запланированные задачи](</ru/automation/cron-jobs>)


Was this useful?YesNo

Open issue