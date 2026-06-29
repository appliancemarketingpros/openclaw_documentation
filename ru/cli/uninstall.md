---
title: Удаление
source_url: https://docs.openclaw.ai/ru/cli/uninstall
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw uninstall`

Удаление службы Gateway и локальных данных (CLI остается).

Параметры:

  * `--service`: удалить службу Gateway
  * `--state`: удалить состояние и конфигурацию
  * `--workspace`: удалить каталоги рабочих пространств
  * `--app`: удалить приложение macOS
  * `--all`: удалить службу, состояние, рабочее пространство и приложение
  * `--yes`: пропустить запросы подтверждения
  * `--non-interactive`: отключить запросы; требует `--yes`
  * `--dry-run`: вывести действия без удаления файлов


Примеры:

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

Примечания:

  * Сначала выполните `openclaw backup create`, если хотите получить восстанавливаемый снимок перед удалением состояния или рабочих пространств.
  * `--state` сохраняет настроенные каталоги рабочих пространств, если также не выбран `--workspace`.
  * `--all` — сокращение для одновременного удаления службы, состояния, рабочего пространства и приложения.
  * `--non-interactive` требует `--yes`.


## Связанные материалы

  * [Справочник CLI](</ru/cli>)
  * [Удаление](</ru/install/uninstall>)


Was this useful?YesNo

Open issue