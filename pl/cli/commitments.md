---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/pl/cli/commitments
scraped_at: 2026-05-25
---

Wyświetlaj i zarządzaj wnioskowanymi zobowiązaniami do dalszych działań.

Zobowiązania to opcjonalne, krótkotrwałe wpisy pamięci dotyczące dalszych działań, tworzone z kontekstu rozmowy. Zobacz [Wnioskowane zobowiązania](</pl/concepts/commitments>), aby zapoznać się z przewodnikiem koncepcyjnym.

Bez podpolecenia `openclaw commitments` wyświetla oczekujące zobowiązania.

## Użycie

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## Opcje

  * `--all`: pokaż wszystkie statusy zamiast tylko oczekujących zobowiązań.
  * `--agent <id>`: filtruj do jednego identyfikatora agenta.
  * `--status <status>`: filtruj według statusu. Wartości: `pending`, `sent`, `dismissed`, `snoozed` lub `expired`.
  * `--json`: wyprowadź JSON czytelny maszynowo.


## Przykłady

Wyświetl oczekujące zobowiązania:

bashCopy code
[code]
    openclaw commitments
[/code]

Wyświetl każde zapisane zobowiązanie:

bashCopy code
[code]
    openclaw commitments --all
[/code]

Filtruj do jednego agenta:

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

Znajdź odłożone zobowiązania:

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

Odrzuć jedno lub więcej zobowiązań:

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

Eksportuj jako JSON:

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## Dane wyjściowe

Dane tekstowe obejmują:

  * identyfikator zobowiązania
  * status
  * typ
  * najwcześniejszy termin wykonania
  * zakres
  * sugerowany tekst kontaktu kontrolnego


Dane JSON zawierają także ścieżkę magazynu zobowiązań oraz pełne zapisane rekordy.

## Powiązane

  * [Wnioskowane zobowiązania](</pl/concepts/commitments>)
  * [Przegląd pamięci](</pl/concepts/memory>)
  * [Heartbeat](</pl/gateway/heartbeat>)
  * [Zaplanowane zadania](</pl/automation/cron-jobs>)


Was this useful?YesNo