---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/uk/cli/commitments
scraped_at: 2026-05-25
---

Переглядайте й керуйте виведеними зобов’язаннями щодо подальших дій.

Зобов’язання — це короткочасні пам’ятки про подальші дії, створені з контексту розмови за явною згодою. Див. [Виведені зобов’язання](</uk/concepts/commitments>) для концептуального посібника.

Без підкоманди `openclaw commitments` показує список очікуваних зобов’язань.

## Використання

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## Параметри

  * `--all`: показати всі статуси замість лише очікуваних зобов’язань.
  * `--agent <id>`: відфільтрувати за одним ідентифікатором агента.
  * `--status <status>`: відфільтрувати за статусом. Значення: `pending`, `sent`, `dismissed`, `snoozed` або `expired`.
  * `--json`: вивести машинозчитуваний JSON.


## Приклади

Показати очікувані зобов’язання:

bashCopy code
[code]
    openclaw commitments
[/code]

Показати кожне збережене зобов’язання:

bashCopy code
[code]
    openclaw commitments --all
[/code]

Відфільтрувати за одним агентом:

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

Знайти відкладені зобов’язання:

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

Відхилити одне або кілька зобов’язань:

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

Експортувати як JSON:

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## Вивід

Текстовий вивід містить:

  * ідентифікатор зобов’язання
  * статус
  * тип
  * найраніший строк виконання
  * область дії
  * запропонований текст перевірки стану


Вивід JSON також містить шлях до сховища зобов’язань і повні збережені записи.

## Пов’язане

  * [Виведені зобов’язання](</uk/concepts/commitments>)
  * [Огляд пам’яті](</uk/concepts/memory>)
  * [Heartbeat](</uk/gateway/heartbeat>)
  * [Заплановані завдання](</uk/automation/cron-jobs>)


Was this useful?YesNo