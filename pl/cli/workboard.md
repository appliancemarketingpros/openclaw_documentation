---
title: CLI tablicy roboczej
source_url: https://docs.openclaw.ai/pl/cli/workboard
scraped_at: 2026-06-29
---

ReferenceCLI commands

`openclaw workboard` to powierzchnia terminalowa dla dołączonego [Plugin Workboard](</pl/plugins/workboard>). Pozwala operatorowi wyświetlać karty, tworzyć kartę, sprawdzać jedną kartę i prosić działający Gateway o przekazanie gotowej pracy do uruchomień workerów subagentów.

Włącz Plugin przed użyciem polecenia:

bashCopy code
[code]
    openclaw plugins enable workboardopenclaw gateway restart
[/code]

## Użycie

bashCopy code
[code]
    openclaw workboard list [--board <id>] [--status <status>] [--include-archived] [--json]openclaw workboard create <title...> [--notes <text>] [--status <status>] [--priority <priority>] [--agent <id>] [--board <id>] [--labels <items>] [--json]openclaw workboard show <id> [--json]openclaw workboard dispatch [--url <url>] [--token <token>] [--timeout <ms>] [--json]
[/code]

Polecenie odczytuje i zapisuje tę samą bazę SQLite należącą do Plugin, której używają dashboard i narzędzia agenta Workboard. Identyfikatory kart można przekazywać jako pełny identyfikator albo jako jednoznaczny prefiks, gdy polecenie akceptuje identyfikator karty.

## `list`

bashCopy code
[code]
    openclaw workboard listopenclaw workboard list --board default --status readyopenclaw workboard list --json
[/code]

Wyjście tekstowe jest zwięzłe:

textCopy code
[code]
    7f4a2c10  ready     high    default agent-a  Fix stale worker heartbeat
[/code]

Kolumny to prefiks identyfikatora, status, priorytet, identyfikator tablicy, opcjonalny identyfikator agenta i tytuł.

Flagi:

Flaga | Cel  
---|---  
`--board <id>` | Ogranicz wyniki do jednej przestrzeni nazw tablicy  
`--status <status>` | Ogranicz wyniki do jednego statusu Workboard  
`--include-archived` | Uwzględnij zarchiwizowane karty w zwięzłym wyjściu tekstowym  
`--json` | Wypisz pełną listę kart jako maszynowy JSON  
  
Zwięzłe wyjście tekstowe domyślnie ukrywa zarchiwizowane karty, aby CLI odpowiadało poleceniu `/workboard list`. Przekaż `--include-archived`, aby je pokazać. Wyjście JSON zachowuje pełną listę kart, w tym zarchiwizowane karty, dla istniejącej automatyzacji.

## `create`

bashCopy code
[code]
    openclaw workboard create "Fix stale worker heartbeat" --priority high --labels bug,workboardopenclaw workboard create "Write Workboard docs" --status ready --agent docs-agent --board docs --notes "Cover CLI, slash command, dispatch, and SQLite state."
[/code]

Flagi:

Flaga | Cel  
---|---  
`--notes <text>` | Początkowe notatki karty  
`--status <status>` | Początkowy status, domyślnie `todo`  
`--priority <priority>` | Priorytet, domyślnie `normal`  
`--agent <id>` | Przypisz kartę do agenta lub identyfikatora właściciela  
`--board <id>` | Zapisz kartę w przestrzeni nazw tablicy  
`--labels <items>` | Etykiety rozdzielone przecinkami  
`--json` | Wypisz utworzoną kartę jako maszynowy JSON  
  
`create` zapisuje bezpośrednio do stanu SQLite Workboard. Karta jest natychmiast widoczna na karcie Workboard w Control UI oraz dla narzędzi Workboard.

## `show`

bashCopy code
[code]
    openclaw workboard show 7f4a2c10openclaw workboard show 7f4a2c10 --json
[/code]

Wyjście tekstowe wypisuje zwięzły wiersz karty i notatki. Wyjście JSON zwraca pełny rekord karty, w tym metadane wykonania, próby, komentarze, linki, dowody, artefakty, logi workerów, stan protokołu, diagnostykę i metadane automatyzacji.

## `dispatch`

bashCopy code
[code]
    openclaw workboard dispatchopenclaw workboard dispatch --jsonopenclaw workboard dispatch --url http://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
[/code]

`dispatch` najpierw wywołuje metodę RPC działającego Gateway `workboard.cards.dispatch`. Ta ścieżka używa tego samego runtime subagentów co akcja dispatch w dashboardzie, więc gotowe karty stają się śledzonymi zadaniami uruchomieniami workerów z powiązanymi kluczami sesji. Karty z przypisanym agentem używają kluczy sesji subagentów o zakresie agenta; nieprzypisane karty zachowują klucz subagenta bez zakresu, aby skonfigurowany domyślny agent Gateway został zachowany.

Pętla dispatch:

  1. Awansuje dzieci gotowe pod względem zależności do `ready`.
  2. Blokuje wygasłe roszczenia lub uruchomienia workerów po przekroczeniu czasu.
  3. Zapisuje metadane dispatch na gotowych kartach.
  4. Wybiera małą partię nieprzypisanych gotowych kart.
  5. Obejmuje roszczeniem każdą wybraną kartę dla dyspozytora lub przypisanego agenta.
  6. Uruchamia workera subagenta z ograniczonym kontekstem karty i tokenem roszczenia karty.
  7. Zapisuje na karcie identyfikator uruchomienia workera, klucz sesji, powiązanie zadania, gdy ledger zadań Gateway je zgłosi, status wykonania i log workera.


Wybór jest celowo konserwatywny. Jeden dispatch domyślnie uruchamia najwyżej trzech workerów, pomija zarchiwizowane lub już objęte roszczeniem karty i w jednym przebiegu uruchamia tylko jedną kartę na właściciela lub agenta. Karty już posiadane przez aktywną pracę uruchomioną lub przeglądu pozostają do późniejszego dispatch.

Jeśli uruchomienie workera nie powiedzie się po objęciu karty roszczeniem, Workboard blokuje tę kartę, czyści roszczenie i zapisuje błąd w metadanych wykonania karty oraz logu workera. Dzięki temu nieudane uruchomienia pozostają widoczne, zamiast po cichu wracać kartę do kolejki.

Jeśli nie podano jawnego celu Gateway, a lokalny Gateway jest niedostępny albo jeszcze nie udostępnia metody dispatch Workboard, CLI przechodzi awaryjnie do dispatch opartego wyłącznie na danych względem lokalnego stanu Workboard. Dispatch wyłącznie na danych nadal może awansować zależności, czyścić nieaktualne roszczenia i blokować uruchomienia po przekroczeniu czasu, ale nie uruchamia workerów. Błędy uwierzytelniania, uprawnień, walidacji oraz błędy dla jawnego celu `--url` lub `--token` są zgłaszane bezpośrednio.

Wyjście tekstowe raportuje uruchomienia workerów:

textCopy code
[code]
    dispatch complete: started=2 failures=0
[/code]

Wyjście awaryjne jest jawne:

textCopy code
[code]
    gateway unavailable; data dispatch only: promoted=1 blocked=0
[/code]

Wyjście JSON zawiera wynik dispatch. Dispatch oparty na Gateway może zawierać `started` i `startFailures`; awaryjny tryb wyłącznie na danych zawiera `gatewayUnavailable: true`. Tokeny roszczeń są redagowane z wyjścia JSON kart.

W dashboardzie ten sam wynik dispatch jest pokazany jako krótkie podsumowanie, aby operator mógł zobaczyć, ile kart uruchomiono, awansowano, zablokowano, odzyskano lub zakończyło się błędem bez otwierania szczegółów kart.

## Zgodność poleceń slash

Kanały obsługujące polecenia mogą używać odpowiadającego polecenia slash:

textCopy code
[code]
    /workboard list/workboard show 7f4a2c10/workboard create Fix stale worker heartbeat/workboard dispatch
[/code]

Dispatch z polecenia slash również używa runtime subagentów Gateway, więc zachowuje to samo roszczenie, uruchamianie workerów i obsługę błędów co dashboard oraz ścieżka Gateway w CLI.

`/workboard list` i `/workboard show` to polecenia odczytu dla autoryzowanych nadawców poleceń. `/workboard create` i `/workboard dispatch` modyfikują stan tablicy i wymagają statusu właściciela na powierzchniach czatu albo klienta Gateway z `operator.write` lub `operator.admin`.

## Uprawnienia

Ścieżka dispatch w CLI wywołuje RPC Gateway z zakresami `operator.read` i `operator.write`. Token Gateway tylko do odczytu może sprawdzać dane Workboard przez metody odczytu, ale nie może tworzyć kart ani uruchamiać workerów.

Lokalne polecenia `list`, `create` i `show` działają na lokalnym katalogu stanu OpenClaw używanym przez bieżący profil. Użyj `--dev` lub `--profile <name>` w poleceniu najwyższego poziomu `openclaw`, gdy potrzebujesz innego katalogu głównego stanu.

## Rozwiązywanie problemów

### Nie pojawiają się żadne karty

Potwierdź, że Plugin jest włączony dla tego samego profilu i katalogu głównego stanu:

bashCopy code
[code]
    openclaw plugins inspect workboard --runtime --json
[/code]

Jeśli dashboard pokazuje karty, ale CLI nie, sprawdź, czy oba polecenia używają tego samego ustawienia `--dev` lub `--profile`.

### Dispatch zgłasza tryb wyłącznie na danych

Uruchom lub zrestartuj Gateway:

bashCopy code
[code]
    openclaw gateway restartopenclaw gateway status --deep
[/code]

Następnie ponów `openclaw workboard dispatch`. Awaryjny tryb wyłącznie na danych jest przydatny do czyszczenia lokalnego stanu, ale uruchomienia workerów wymagają działającego Gateway.

### Dispatch niczego nie uruchamia

Sprawdź, czy istnieje co najmniej jedna karta `ready` bez aktywnego roszczenia:

bashCopy code
[code]
    openclaw workboard list --status ready
[/code]

Karty mogą być też pomijane, gdy ten sam właściciel ma już pracę uruchomioną lub w przeglądzie. Przenieś ukończoną pracę do `done`, zwolnij nieaktualne roszczenia przez narzędzia Workboard albo uruchom dispatch ponownie po zakończeniu aktywnego workera.

## Powiązane

  * [Plugin Workboard](</pl/plugins/workboard>)
  * [Dokumentacja CLI](</pl/cli>)
  * [Polecenia slash](</pl/tools/slash-commands>)
  * [Control UI](</pl/web/control-ui>)


Was this useful?YesNo

Open issue