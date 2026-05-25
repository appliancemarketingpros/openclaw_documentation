---
title: Надсилання агентом
source_url: https://docs.openclaw.ai/uk/tools/agent-send
scraped_at: 2026-05-25
---

`openclaw agent` запускає один хід агента з командного рядка без потреби у вхідному повідомленні чату. Використовуйте це для скриптованих робочих процесів, тестування та програмної доставки.

## Швидкий старт

* ### Run a simple agent turn

bashCopy code
[code]
    openclaw agent --message "What is the weather today?"
[/code]

Це надсилає повідомлення через Gateway і виводить відповідь.

* ### Target a specific agent or session

bashCopy code
[code]
    # Target a specific agentopenclaw agent --agent ops --message "Summarize logs" # Target a phone number (derives session key)openclaw agent --to +15555550123 --message "Status update" # Reuse an existing sessionopenclaw agent --session-id abc123 --message "Continue the task"
[/code]

* ### Deliver the reply to a channel

bashCopy code
[code]
    # Deliver to WhatsApp (default channel)openclaw agent --to +15555550123 --message "Report ready" --deliver # Deliver to Slackopenclaw agent --agent ops --message "Generate report" \  --deliver --reply-channel slack --reply-to "#reports"
[/code]

## Прапорці

Прапорець | Опис  
---|---  
`--message \<text\>` | Повідомлення для надсилання (обов’язково)  
`--to \<dest\>` | Вивести ключ сесії з цілі (телефон, id чату)  
`--agent \<id\>` | Націлитися на налаштованого агента (використовує його сесію `main`)  
`--session-id \<id\>` | Повторно використати наявну сесію за id  
`--local` | Примусово використати локальне вбудоване середовище виконання (оминути Gateway)  
`--deliver` | Надіслати відповідь у канал чату  
`--channel \<name\>` | Канал доставки (whatsapp, telegram, discord, slack тощо)  
`--reply-to \<target\>` | Перевизначення цілі доставки  
`--reply-channel \<name\>` | Перевизначення каналу доставки  
`--reply-account \<id\>` | Перевизначення id облікового запису доставки  
`--thinking \<level\>` | Установити рівень мислення для вибраного профілю моделі  
`--verbose \<on|full|off\>` | Установити рівень докладності  
`--timeout \<seconds\>` | Перевизначити час очікування агента  
`--json` | Вивести структурований JSON  
  
## Поведінка

  * За замовчуванням CLI працює **через Gateway**. Додайте `--local`, щоб примусово використати вбудоване середовище виконання на поточній машині.
  * Якщо Gateway недоступний, CLI **повертається** до локального вбудованого запуску.
  * Вибір сесії: `--to` виводить ключ сесії (цілі груп/каналів зберігають ізоляцію; прямі чати згортаються до `main`).
  * Прапорці мислення й докладності зберігаються в сховищі сесії.
  * Виведення: за замовчуванням звичайний текст або `--json` для структурованого корисного навантаження + метаданих.
  * З `--json --deliver` JSON містить статус доставки для надісланих, приглушених, часткових і невдалих надсилань. Див. [статус доставки JSON](</uk/cli/agent#json-delivery-status>).


## Приклади

bashCopy code
[code]
    # Simple turn with JSON outputopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --json # Turn with thinking levelopenclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium # Deliver to a different channel than the sessionopenclaw agent --agent ops --message "Alert" --deliver --reply-channel telegram --reply-to "@admin"
[/code]

## Пов’язане

[**Agent CLI reference** Повний довідник прапорців і параметрів `openclaw agent`. ](</uk/cli/agent>) [**Sub-agents** Запуск фонових під-агентів. ](</uk/tools/subagents>) [**Sessions** Як працюють ключі сесій і як `--to`, `--agent` та `--session-id` їх визначають. ](</uk/concepts/session>) [**Slash commands** Власний каталог команд, що використовується всередині сесій агентів. ](</uk/tools/slash-commands>)

Was this useful?YesNo