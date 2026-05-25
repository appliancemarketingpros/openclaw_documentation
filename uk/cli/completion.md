---
title: Автодоповнення
source_url: https://docs.openclaw.ai/uk/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

Згенеруйте скрипти автодоповнення оболонки та, за бажання, встановіть їх у профіль вашої оболонки.

## Використання

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## Параметри

  * `-s, --shell <shell>`: цільова оболонка (`zsh`, `bash`, `powershell`, `fish`; типово: `zsh`)
  * `-i, --install`: встановити автодоповнення, додавши рядок source до профілю вашої оболонки
  * `--write-state`: записати скрипт(и) автодоповнення до `$OPENCLAW_STATE_DIR/completions` без виведення в stdout
  * `-y, --yes`: пропустити запити на підтвердження встановлення


## Примітки

  * `--install` записує невеликий блок "Автодоповнення OpenClaw" у профіль вашої оболонки та вказує його на кешований скрипт.
  * Без `--install` або `--write-state` команда виводить скрипт у stdout.
  * Генерація автодоповнення завчасно завантажує дерева команд, щоб були включені вкладені підкоманди.


## Пов’язане

  * [Довідка CLI](</uk/cli>)


Was this useful?YesNo