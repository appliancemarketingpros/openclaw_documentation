---
title: Отправка агентом
source_url: https://docs.openclaw.ai/ru/tools/agent-send
scraped_at: 2026-06-29
---

CapabilitiesAgent coordination

`openclaw agent` запускает один ход агента из командной строки без необходимости во входящем сообщении чата. Используйте его для скриптовых рабочих процессов, тестирования и программной доставки.

## Быстрый старт

* ### Run a simple agent turn

bashCopy code
[code]
    openclaw agent --agent main --message "What is the weather today?"
[/code]

Это отправляет сообщение через Gateway и выводит ответ.

* ### Send a multiline prompt from a file

bashCopy code
[code]
    openclaw agent --agent ops --message-file ./task.md
[/code]

Это считывает допустимый файл UTF-8 как тело сообщения агента.

* ### Target a specific agent or session

bashCopy code
[code]
    # Target a specific agentopenclaw agent --agent ops --message "Summarize logs" # Target a phone number (derives session key)openclaw agent --to +15555550123 --message "Status update" # Reuse an existing sessionopenclaw agent --session-id abc123 --message "Continue the task" # Target an exact session keyopenclaw agent --session-key agent:ops:incident-42 --message "Summarize status"
[/code]

* ### Deliver the reply to a channel

bashCopy code
[code]
    # Deliver to WhatsApp (default channel)openclaw agent --to +15555550123 --message "Report ready" --deliver # Deliver to Slackopenclaw agent --agent ops --message "Generate report" \  --deliver --reply-channel slack --reply-to "#reports"
[/code]

## Флаги

Флаг | Описание  
---|---  
`--message \<text\>` | Встроенное сообщение для отправки  
`--message-file \<path\>` | Считать сообщение из допустимого файла UTF-8  
`--to \<dest\>` | Вывести ключ сеанса из целевого адресата (телефон, id чата)  
`--session-key \<key\>` | Использовать явный ключ сеанса  
`--agent \<id\>` | Направить в настроенного агента (использует его сеанс `main`)  
`--session-id \<id\>` | Повторно использовать существующий сеанс по id  
`--local` | Принудительно использовать локальную встроенную среду выполнения (без Gateway)  
`--deliver` | Отправить ответ в канал чата  
`--channel \<name\>` | Канал доставки (whatsapp, telegram, discord, slack и т. д.)  
`--reply-to \<target\>` | Переопределение цели доставки  
`--reply-channel \<name\>` | Переопределение канала доставки  
`--reply-account \<id\>` | Переопределение id учетной записи доставки  
`--thinking \<level\>` | Задать уровень thinking для выбранного профиля модели  
`--verbose \<on|full|off\>` | Задать уровень подробности  
`--timeout \<seconds\>` | Переопределить тайм-аут агента  
`--json` | Вывести структурированный JSON  
  
## Поведение

  * По умолчанию CLI работает **через Gateway**. Добавьте `--local`, чтобы принудительно использовать встроенную среду выполнения на текущей машине.
  * Передайте ровно один из параметров: `--message` или `--message-file`. Сообщения из файла сохраняют многострочное содержимое после удаления необязательной UTF-8 BOM.
  * Если Gateway недоступен, CLI **возвращается** к локальному встроенному запуску.
  * Выбор сеанса: `--to` выводит ключ сеанса (целевые группы/каналы сохраняют изоляцию; прямые чаты сворачиваются в `main`).
  * `--session-key` выбирает явный ключ. Ключи с префиксом агента должны использовать `agent:<agent-id>:<session-key>`, а `--agent` должен совпадать с этим id агента, когда указаны оба параметра. Простые ключи без sentinel ограничиваются областью `--agent`, когда он указан; например, `--agent ops --session-key incident-42` направляет в `agent:ops:incident-42`. Без `--agent` простые ключи без sentinel ограничиваются областью настроенного агента по умолчанию. Литералы `global` и `unknown` остаются без области только когда `--agent` не указан; в этом случае встроенный fallback и владение хранилищем используют настроенного агента по умолчанию.
  * Флаги thinking и verbose сохраняются в хранилище сеанса.
  * Вывод: по умолчанию простой текст или `--json` для структурированной полезной нагрузки и метаданных.
  * С `--json --deliver` JSON включает статус доставки для отправленных, подавленных, частичных и неудачных отправок. См. [статус доставки JSON](</ru/cli/agent#json-delivery-status>).


## Примеры

bashCopy code
[code]
    # Simple turn with JSON outputopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --json # Turn with thinking levelopenclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium # Multiline prompt from a fileopenclaw agent --agent ops --message-file ./task.md # Exact session keyopenclaw agent --session-key agent:ops:incident-42 --message "Summarize status" # Legacy key scoped to an agentopenclaw agent --agent ops --session-key incident-42 --message "Summarize status" # Deliver to a different channel than the sessionopenclaw agent --agent ops --message "Alert" --deliver --reply-channel telegram --reply-to "@admin"
[/code]

## Связанные материалы

[**Agent CLI reference** Полный справочник флагов и параметров `openclaw agent`. ](</ru/cli/agent>) [**Sub-agents** Фоновый запуск субагентов. ](</ru/tools/subagents>) [**Sessions** Как работают ключи сеансов и как `--to`, `--agent` и `--session-id` разрешают их. ](</ru/concepts/session>) [**Slash commands** Собственный каталог команд, используемый внутри сеансов агента. ](</ru/tools/slash-commands>)

Was this useful?YesNo

Open issue