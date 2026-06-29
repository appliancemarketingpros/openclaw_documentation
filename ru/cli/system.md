---
title: Система
source_url: https://docs.openclaw.ai/ru/cli/system
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw system`

Вспомогательные команды системного уровня для Gateway: постановка системных событий в очередь, управление Heartbeat и просмотр presence.

Все подкоманды `system` используют Gateway RPC и принимают общие флаги клиента:

  * `--url <url>`
  * `--token <token>`
  * `--timeout <ms>`
  * `--expect-final`


## Общие команды

bashCopy code
[code]
    openclaw system event --text "Check for urgent follow-ups" --mode nowopenclaw system event --text "Check for urgent follow-ups" --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"openclaw system heartbeat enableopenclaw system heartbeat lastopenclaw system presence
[/code]

## `system event`

По умолчанию ставит системное событие в очередь в **основном** сеансе. Следующий Heartbeat вставит его в prompt как строку `System:`. Используйте `--mode now`, чтобы запустить Heartbeat немедленно; `next-heartbeat` ожидает следующего запланированного тика.

Передайте `--session-key`, чтобы нацелиться на конкретный сеанс (например, чтобы передать завершение async-задачи обратно в канал, который ее запустил).

> **Исключение по времени с`--session-key`:** когда указан `--session-key`, `--mode next-heartbeat` сворачивается в немедленное целевое пробуждение вместо ожидания следующего запланированного тика. Целевые пробуждения используют intent Heartbeat `immediate`, поэтому они обходят not-due gate раннера, который иначе отложил бы (и фактически отбросил) пробуждение с intent `event`. Если нужна отложенная доставка, не указывайте `--session-key`, чтобы событие попало в основной сеанс и было доставлено со следующим регулярным Heartbeat.

Флаги:

  * `--text <text>`: обязательный текст системного события.
  * `--mode <mode>`: `now` или `next-heartbeat` (по умолчанию).
  * `--session-key <sessionKey>`: необязательно; нацелиться на конкретный сеанс агента вместо основного сеанса агента. Ключи, которые не принадлежат разрешенному агенту, откатываются к основному сеансу агента.
  * `--json`: машиночитаемый вывод.
  * `--url`, `--token`, `--timeout`, `--expect-final`: общие флаги Gateway RPC.


## `system heartbeat last|enable|disable`

Управление Heartbeat:

  * `last`: показать последнее событие Heartbeat.
  * `enable`: снова включить Heartbeat (используйте это, если он был отключен).
  * `disable`: приостановить Heartbeat.


Флаги:

  * `--json`: машиночитаемый вывод.
  * `--url`, `--token`, `--timeout`, `--expect-final`: общие флаги Gateway RPC.


## `system presence`

Выводит текущие записи system presence, о которых знает Gateway (узлы, экземпляры и похожие строки статуса).

Флаги:

  * `--json`: машиночитаемый вывод.
  * `--url`, `--token`, `--timeout`, `--expect-final`: общие флаги Gateway RPC.


## Примечания

  * Требуется запущенный Gateway, доступный по вашей текущей конфигурации (локальной или удаленной).
  * Системные события эфемерны и не сохраняются между перезапусками.


## Связанные материалы

  * [Справочник CLI](</ru/cli>)


Was this useful?YesNo

Open issue