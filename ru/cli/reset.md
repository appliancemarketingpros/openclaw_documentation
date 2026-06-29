---
title: Сброс
source_url: https://docs.openclaw.ai/ru/cli/reset
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw reset`

Сбрасывает локальную конфигурацию/состояние (CLI остается установленным).

Параметры:

  * `--scope <scope>`: `config`, `config+creds+sessions` или `full`
  * `--yes`: пропустить запросы подтверждения
  * `--non-interactive`: отключить запросы; требует `--scope` и `--yes`
  * `--dry-run`: вывести действия без удаления файлов


Примеры:

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

Примечания:

  * Сначала выполните `openclaw backup create`, если перед удалением локального состояния нужен снимок, который можно восстановить.
  * Если опустить `--scope`, `openclaw reset` использует интерактивный запрос, чтобы выбрать, что удалить.
  * `--non-interactive` допустим только когда заданы и `--scope`, и `--yes`.


## Связанные материалы

  * [Справочник CLI](</ru/cli>)


Was this useful?YesNo

Open issue