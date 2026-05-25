---
title: Видалення
source_url: https://docs.openclaw.ai/uk/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

Видалення сервісу gateway + локальних даних (CLI залишається).

Параметри:

  * `--service`: видалити сервіс gateway
  * `--state`: видалити стан і конфігурацію
  * `--workspace`: видалити каталоги робочого простору
  * `--app`: видалити застосунок macOS
  * `--all`: видалити сервіс, стан, робочий простір і застосунок
  * `--yes`: пропустити запити на підтвердження
  * `--non-interactive`: вимкнути запити; потребує `--yes`
  * `--dry-run`: вивести дії без видалення файлів


Приклади:

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

Примітки:

  * Спочатку виконайте `openclaw backup create`, якщо хочете мати відновлюваний знімок перед видаленням стану або робочих просторів.
  * `--all` — це скорочення для одночасного видалення сервісу, стану, робочого простору й застосунку.
  * `--non-interactive` потребує `--yes`.


## Пов’язане

  * [Довідка CLI](</uk/cli>)
  * [Видалення](</uk/install/uninstall>)


Was this useful?YesNo