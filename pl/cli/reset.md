---
title: Resetowanie
source_url: https://docs.openclaw.ai/pl/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

Resetuje lokalny stan/konfigurację (pozostawia zainstalowane CLI).

Opcje:

  * `--scope <scope>`: `config`, `config+creds+sessions` lub `full`
  * `--yes`: pomija monity o potwierdzenie
  * `--non-interactive`: wyłącza monity; wymaga `--scope` i `--yes`
  * `--dry-run`: wypisuje działania bez usuwania plików


Przykłady:

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

Uwagi:

  * Najpierw uruchom `openclaw backup create`, jeśli chcesz mieć możliwą do przywrócenia migawkę przed usunięciem stanu lokalnego.
  * Jeśli pominiesz `--scope`, `openclaw reset` użyje interaktywnego monitu do wyboru, co usunąć.
  * `--non-interactive` jest prawidłowe tylko wtedy, gdy ustawiono zarówno `--scope`, jak i `--yes`.


## Powiązane

  * [Odwołanie CLI](</pl/cli>)


Was this useful?YesNo