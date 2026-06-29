---
title: Выполнение
source_url: https://docs.openclaw.ai/ru/cli/completion
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw completion`

Сгенерируйте скрипты автодополнения оболочки и при необходимости установите их в профиль вашей оболочки.

## Использование

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## Параметры

  * `-s, --shell <shell>`: целевая оболочка (`zsh`, `bash`, `powershell`, `fish`; по умолчанию: `zsh`)
  * `-i, --install`: установить автодополнение, добавив строку подключения в профиль вашей оболочки
  * `--write-state`: записать скрипт(ы) автодополнения в `$OPENCLAW_STATE_DIR/completions` без вывода в stdout
  * `-y, --yes`: пропустить запросы подтверждения установки


## Примечания

  * `--install` записывает небольшой блок "OpenClaw Completion" в профиль вашей оболочки и указывает его на кэшированный скрипт.
  * Без `--install` или `--write-state` команда выводит скрипт в stdout.
  * Генерация автодополнения заранее загружает деревья команд, чтобы включить вложенные подкоманды.


## Связанные материалы

  * [Справочник CLI](</ru/cli>)


Was this useful?YesNo

Open issue