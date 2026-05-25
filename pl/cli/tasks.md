---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/pl/cli/tasks
scraped_at: 2026-05-25
---

Sprawdzaj trwałe zadania w tle oraz stan przepływu zadań. Bez podpolecenia `openclaw tasks` jest równoważne `openclaw tasks list`.

Zobacz [Zadania w tle](</pl/automation/tasks>), aby poznać cykl życia i model dostarczania.

## Użycie

bashCopy code
[code]
    openclaw tasksopenclaw tasks listopenclaw tasks list --runtime acpopenclaw tasks list --status runningopenclaw tasks show <lookup>openclaw tasks notify <lookup> state_changesopenclaw tasks cancel <lookup>openclaw tasks auditopenclaw tasks maintenanceopenclaw tasks maintenance --applyopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## Opcje główne

  * `--json`: wypisuje JSON.
  * `--runtime <name>`: filtruje według rodzaju: `subagent`, `acp`, `cron` lub `cli`.
  * `--status <name>`: filtruje według statusu: `queued`, `running`, `succeeded`, `failed`, `timed_out`, `cancelled` lub `lost`.


## Podpolecenia

### `list`

bashCopy code
[code]
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
[/code]

Wyświetla śledzone zadania w tle od najnowszych.

### `show`

bashCopy code
[code]
    openclaw tasks show <lookup> [--json]
[/code]

Pokazuje jedno zadanie według identyfikatora zadania, identyfikatora uruchomienia lub klucza sesji.

### `notify`

bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

Zmienia zasadę powiadomień dla uruchomionego zadania.

### `cancel`

bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

Anuluje uruchomione zadanie w tle.

### `audit`

bashCopy code
[code]
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
[/code]

Ujawnia nieaktualne, utracone, niedostarczone lub w inny sposób niespójne rekordy zadań i przepływu zadań. Utracone zadania przechowywane do `cleanupAfter` są ostrzeżeniami; wygasłe lub nieostemplowane utracone zadania są błędami.

### `maintenance`

bashCopy code
[code]
    openclaw tasks maintenance [--apply] [--json]
[/code]

Podgląda lub stosuje uzgadnianie zadań i przepływu zadań, stemplowanie czyszczenia, przycinanie oraz czyszczenie rejestru sesji nieaktualnych uruchomień Cron. W przypadku zadań Cron uzgadnianie używa utrwalonych dzienników uruchomień/stanu zadań przed oznaczeniem starego aktywnego zadania jako `lost`, dzięki czemu ukończone uruchomienia Cron nie stają się fałszywymi błędami audytu tylko dlatego, że stan środowiska wykonawczego Gateway w pamięci zniknął. Audyt CLI w trybie offline nie jest autorytatywny dla lokalnego dla procesu zestawu aktywnych zadań Cron w Gateway. Zadania CLI z identyfikatorem uruchomienia/identyfikatorem źródła są oznaczane jako `lost`, gdy ich aktywny kontekst uruchomienia Gateway zniknął, nawet jeśli pozostał stary wiersz sesji podrzędnej. Po zastosowaniu konserwacja przycina także wiersze rejestru sesji `cron:<jobId>:run:<uuid>` starsze niż 7 dni, zachowując obecnie uruchomione zadania Cron i pozostawiając wiersze sesji inne niż Cron bez zmian.

### `flow`

bashCopy code
[code]
    openclaw tasks flow list [--status <name>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Sprawdza lub anuluje trwały stan przepływu zadań w rejestrze zadań.

## Powiązane

  * [Dokumentacja CLI](</pl/cli>)
  * [Zadania w tle](</pl/automation/tasks>)


Was this useful?YesNo