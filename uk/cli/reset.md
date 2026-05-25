---
title: Reset
source_url: https://docs.openclaw.ai/uk/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

Скидання локальної конфігурації/стану (CLI залишається встановленим).

Параметри:

  * `--scope <scope>`: `config`, `config+creds+sessions` або `full`
  * `--yes`: пропустити запити на підтвердження
  * `--non-interactive`: вимкнути запити; потребує `--scope` і `--yes`
  * `--dry-run`: вивести дії без видалення файлів


Приклади:

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

Примітки:

  * Спочатку виконайте `openclaw backup create`, якщо хочете мати відновлюваний знімок перед видаленням локального стану.
  * Якщо не вказати `--scope`, `openclaw reset` використає інтерактивний запит, щоб вибрати, що видаляти.
  * `--non-interactive` є чинним лише тоді, коли встановлено і `--scope`, і `--yes`.


## Пов’язане

  * [Довідка CLI](</uk/cli>)


Was this useful?YesNo