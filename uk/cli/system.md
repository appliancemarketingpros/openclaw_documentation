---
title: Система
source_url: https://docs.openclaw.ai/uk/cli/system
scraped_at: 2026-05-25
---

# `openclaw system`

Допоміжні засоби системного рівня для Gateway: ставте системні події в чергу, керуйте Heartbeat і переглядайте присутність.

Усі підкоманди `system` використовують RPC Gateway і приймають спільні клієнтські прапорці:

  * `--url <url>`
  * `--token <token>`
  * `--timeout <ms>`
  * `--expect-final`


## Поширені команди

bashCopy code
[code]
    openclaw system event --text "Check for urgent follow-ups" --mode nowopenclaw system event --text "Check for urgent follow-ups" --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"openclaw system heartbeat enableopenclaw system heartbeat lastopenclaw system presence
[/code]

## `system event`

Типово ставить системну подію в чергу в **головному** сеансі. Наступний Heartbeat вставить її в запит як рядок `System:`. Використовуйте `--mode now`, щоб запустити Heartbeat негайно; `next-heartbeat` чекає наступного запланованого такту.

Передайте `--session-key`, щоб націлитися на певний сеанс (наприклад, щоб передати завершення асинхронного завдання назад у канал, який його запустив).

> **Виняток синхронізації з`--session-key`:** коли вказано `--session-key`, `--mode next-heartbeat` згортається до негайного цільового пробудження замість очікування наступного запланованого такту. Цільові пробудження використовують намір Heartbeat `immediate`, тому вони обходять перевірку runner на ще не наставший час, яка інакше відклала б (і фактично відкинула б) пробудження з наміром `event`. Якщо потрібна відкладена доставка, не вказуйте `--session-key`, щоб подія потрапила в головний сеанс і пішла з наступним регулярним Heartbeat.

Прапорці:

  * `--text <text>`: обов’язковий текст системної події.
  * `--mode <mode>`: `now` або `next-heartbeat` (типово).
  * `--session-key <sessionKey>`: необов’язково; націлює на певний сеанс агента замість головного сеансу агента. Ключі, які не належать визначеному агенту, повертаються до головного сеансу агента.
  * `--json`: вивід, придатний для машинного читання.
  * `--url`, `--token`, `--timeout`, `--expect-final`: спільні прапорці RPC Gateway.


## `system heartbeat last|enable|disable`

Елементи керування Heartbeat:

  * `last`: показує останню подію Heartbeat.
  * `enable`: знову вмикає Heartbeat (використовуйте це, якщо його було вимкнено).
  * `disable`: призупиняє Heartbeat.


Прапорці:

  * `--json`: вивід, придатний для машинного читання.
  * `--url`, `--token`, `--timeout`, `--expect-final`: спільні прапорці RPC Gateway.


## `system presence`

Перелічує поточні записи системної присутності, про які знає Gateway (вузли, екземпляри та подібні рядки стану).

Прапорці:

  * `--json`: вивід, придатний для машинного читання.
  * `--url`, `--token`, `--timeout`, `--expect-final`: спільні прапорці RPC Gateway.


## Примітки

  * Потребує запущеного Gateway, доступного з вашої поточної конфігурації (локальної або віддаленої).
  * Системні події є тимчасовими й не зберігаються між перезапусками.


## Пов’язане

  * [Довідник CLI](</uk/cli>)


Was this useful?YesNo