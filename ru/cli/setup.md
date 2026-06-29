---
title: Настройка
source_url: https://docs.openclaw.ai/ru/cli/setup
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw setup`

Инициализирует базовую конфигурацию и рабочую область агента. Если указан любой флаг онбординга, также запускает мастер.

## Параметры

Флаг | Описание  
---|---  
`--workspace <dir>` | Каталог рабочей области агента (по умолчанию `~/.openclaw/workspace`; сохраняется как `agents.defaults.workspace`).  
`--wizard` | Запустить интерактивный онбординг.  
`--non-interactive` | Запустить онбординг без запросов.  
`--accept-risk` | Подтвердить риск доступа агента ко всей системе; требуется с `--non-interactive`.  
`--mode <mode>` | Режим онбординга: `local` или `remote`.  
`--import-from <provider>` | Провайдер миграции, который нужно запустить во время онбординга.  
`--import-source <path>` | Домашний каталог исходного агента для `--import-from`.  
`--import-secrets` | Импортировать поддерживаемые секреты во время миграции онбординга.  
`--remote-url <url>` | URL WebSocket удаленного Gateway.  
`--remote-token <token>` | Токен удаленного Gateway (необязательно).  
  
### Автозапуск мастера

`openclaw setup` запускает мастер, когда явно указан любой из этих флагов, даже без `--wizard`:

`--wizard`, `--non-interactive`, `--accept-risk`, `--mode`, `--import-from`, `--import-source`, `--import-secrets`, `--remote-url`, `--remote-token`.

## Примеры

bashCopy code
[code]
    openclaw setupopenclaw setup --workspace ~/.openclaw/workspaceopenclaw setup --wizardopenclaw setup --wizard --import-from hermes --import-source ~/.hermesopenclaw setup --non-interactive --accept-risk --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
[/code]

## Примечания

  * Обычный `openclaw setup` инициализирует конфигурацию и рабочую область без запуска полного процесса онбординга.
  * После обычной настройки запустите `openclaw onboard` для полного пошагового пути, `openclaw configure` для точечных изменений или `openclaw channels add`, чтобы добавить учетные записи каналов.
  * Если обнаружено состояние Hermes, интерактивный онбординг может автоматически предложить миграцию. Импорт в онбординге требует свежей настройки; используйте [Миграцию](</ru/cli/migrate>) для планов пробного запуска, резервных копий и режима перезаписи вне онбординга.


## Связанные материалы

  * [Справочник CLI](</ru/cli>)
  * [Онбординг (CLI)](</ru/start/wizard>)
  * [Начало работы](</ru/start/getting-started>)
  * [Обзор установки](</ru/install>)


Was this useful?YesNo

Open issue