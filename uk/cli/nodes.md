---
title: Вузли
source_url: https://docs.openclaw.ai/uk/cli/nodes
scraped_at: 2026-05-25
---

# `openclaw nodes`

Керуйте спареними вузлами (пристроями) та викликайте можливості вузлів.

Пов’язане:

  * Огляд вузлів: [Вузли](</uk/nodes>)
  * Камера: [Вузли камер](</uk/nodes/camera>)
  * Зображення: [Вузли зображень](</uk/nodes/images>)


Поширені параметри:

  * `--url`, `--token`, `--timeout`, `--json`


## Поширені команди

bashCopy code
[code]
    openclaw nodes listopenclaw nodes list --connectedopenclaw nodes list --last-connected 24hopenclaw nodes pendingopenclaw nodes approve <requestId>openclaw nodes reject <requestId>openclaw nodes remove --node <id|name|ip>openclaw nodes rename --node <id|name|ip> --name <displayName>openclaw nodes statusopenclaw nodes status --connectedopenclaw nodes status --last-connected 24h
[/code]

`nodes list` виводить таблиці очікуваних/спарених вузлів. Рядки спарених вузлів містять вік останнього підключення (Last Connect). Використовуйте `--connected`, щоб показувати лише вузли, підключені зараз. Використовуйте `--last-connected <duration>`, щоб відфільтрувати вузли, які підключалися протягом певної тривалості (наприклад, `24h`, `7d`). Використовуйте `nodes remove --node <id|name|ip>`, щоб видалити застарілий запис спарення вузла, яким володіє Gateway.

Примітка щодо схвалення:

  * `openclaw nodes pending` потребує лише області спарення.
  * `gateway.nodes.pairing.autoApproveCidrs` може пропустити крок очікування лише для явно довіреного першого спарення пристрою `role: node`. За замовчуванням це вимкнено й не схвалює оновлення.
  * `openclaw nodes approve <requestId>` успадковує додаткові вимоги до області від очікуваного запиту: 
    * запит без команди: лише спарення
    * команди вузла без виконання: спарення + запис
    * `system.run` / `system.run.prepare` / `system.which`: спарення + адміністратор


## Виклик

bashCopy code
[code]
    openclaw nodes invoke --node <id|name|ip> --command <command> --params <json>
[/code]

Прапорці виклику:

  * `--params <json>`: рядок JSON-об’єкта (за замовчуванням `{}`).
  * `--invoke-timeout <ms>`: час очікування виклику вузла (за замовчуванням `15000`).
  * `--idempotency-key <key>`: необов’язковий ключ ідемпотентності.
  * `system.run` і `system.run.prepare` тут заблоковані; для виконання команд оболонки використовуйте інструмент `exec` із `host=node`.


Для виконання команд оболонки на вузлі використовуйте інструмент `exec` із `host=node` замість `openclaw nodes run`. CLI `nodes` тепер зосереджений на можливостях: прямий RPC через `nodes invoke`, а також спарення, камера, екран, місцезнаходження, Canvas і сповіщення. Команди Canvas реалізовані вбудованим експериментальним Plugin Canvas; ядро зберігає гачок сумісності, тому вони залишаються в `openclaw nodes canvas`.

## Пов’язане

  * [Довідник CLI](</uk/cli>)
  * [Вузли](</uk/nodes>)


Was this useful?YesNo