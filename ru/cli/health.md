---
title: Состояние
source_url: https://docs.openclaw.ai/ru/cli/health
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw health`

Получает состояние от работающего Gateway.

## Параметры

Флаг | По умолчанию | Описание  
---|---|---  
`--json` | `false` | Выводит машиночитаемый JSON вместо текста.  
`--timeout <ms>` | `10000` | Тайм-аут подключения в миллисекундах.  
`--verbose` | `false` | Подробное логирование. Принудительно выполняет живую проверку и расширяет вывод по агентам.  
`--debug` | `false` | Псевдоним для `--verbose`.  
  
Примеры:

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

Примечания:

  * По умолчанию `openclaw health` запрашивает у работающего Gateway снимок его состояния. Когда у Gateway уже есть свежий кэшированный снимок, он может вернуть этот кэшированный payload и обновиться в фоновом режиме.
  * `--verbose` принудительно выполняет живую проверку, выводит сведения о подключении к Gateway и расширяет человекочитаемый вывод по всем настроенным аккаунтам и агентам.
  * Вывод включает хранилища сессий по агентам, когда настроено несколько агентов.


## Связанные материалы

  * [Справочник CLI](</ru/cli>)
  * [Состояние Gateway](</ru/gateway/health>)


Was this useful?YesNo

Open issue