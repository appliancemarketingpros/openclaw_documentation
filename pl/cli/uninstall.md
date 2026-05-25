---
title: Odinstalowanie
source_url: https://docs.openclaw.ai/pl/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

Odinstaluj usługę gateway + dane lokalne (CLI pozostaje).

Opcje:

  * `--service`: usuń usługę gateway
  * `--state`: usuń stan i konfigurację
  * `--workspace`: usuń katalogi obszaru roboczego
  * `--app`: usuń aplikację macOS
  * `--all`: usuń usługę, stan, obszar roboczy i aplikację
  * `--yes`: pomiń prośby o potwierdzenie
  * `--non-interactive`: wyłącz prompty; wymaga `--yes`
  * `--dry-run`: wypisz działania bez usuwania plików


Przykłady:

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

Uwagi:

  * Najpierw uruchom `openclaw backup create`, jeśli chcesz mieć możliwy do przywrócenia snapshot przed usunięciem stanu lub obszarów roboczych.
  * `--all` to skrót do jednoczesnego usunięcia usługi, stanu, obszaru roboczego i aplikacji.
  * `--non-interactive` wymaga `--yes`.


## Powiązane

  * [CLI reference](</pl/cli>)
  * [Uninstall](</pl/install/uninstall>)


Was this useful?YesNo