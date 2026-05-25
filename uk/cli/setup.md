---
title: Налаштування
source_url: https://docs.openclaw.ai/uk/cli/setup
scraped_at: 2026-05-25
---

# `openclaw setup`

Ініціалізує базову конфігурацію та робочий простір агента. Якщо вказано будь-який прапорець онбордингу, також запускає майстер.

## Параметри

Прапорець | Опис  
---|---  
`--workspace <dir>` | Каталог робочого простору агента (типово `~/.openclaw/workspace`; зберігається як `agents.defaults.workspace`).  
`--wizard` | Запустити інтерактивний онбординг.  
`--non-interactive` | Запустити онбординг без запитів.  
`--mode <mode>` | Режим онбордингу: `local` або `remote`.  
`--import-from <provider>` | Провайдер міграції, який потрібно запустити під час онбордингу.  
`--import-source <path>` | Домашній каталог вихідного агента для `--import-from`.  
`--import-secrets` | Імпортувати підтримувані секрети під час міграції в онбордингу.  
`--remote-url <url>` | URL WebSocket віддаленого Gateway.  
`--remote-token <token>` | Токен віддаленого Gateway (необов’язково).  
  
### Автозапуск майстра

`openclaw setup` запускає майстер, коли будь-який із цих прапорців явно вказано, навіть без `--wizard`:

`--wizard`, `--non-interactive`, `--mode`, `--import-from`, `--import-source`, `--import-secrets`, `--remote-url`, `--remote-token`.

## Приклади

bashCopy code
[code]
    openclaw setupopenclaw setup --workspace ~/.openclaw/workspaceopenclaw setup --wizardopenclaw setup --wizard --import-from hermes --import-source ~/.hermesopenclaw setup --non-interactive --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
[/code]

## Примітки

  * Простий `openclaw setup` ініціалізує конфігурацію та робочий простір без запуску повного процесу онбордингу.
  * Після простого налаштування запустіть `openclaw onboard` для повного керованого процесу, `openclaw configure` для цільових змін або `openclaw channels add`, щоб додати облікові записи каналів.
  * Якщо виявлено стан Hermes, інтерактивний онбординг може автоматично запропонувати міграцію. Онбординг з імпортом потребує нового налаштування; використовуйте [Міграцію](</uk/cli/migrate>) для планів пробного запуску, резервних копій і режиму перезапису поза онбордингом.


## Пов’язане

  * [Довідник CLI](</uk/cli>)
  * [Онбординг (CLI)](</uk/start/wizard>)
  * [Початок роботи](</uk/start/getting-started>)
  * [Огляд встановлення](</uk/install>)


Was this useful?YesNo