---
title: Dzienniki
source_url: https://docs.openclaw.ai/pl/cli/logs
scraped_at: 2026-05-25
---

# `openclaw logs`

Śledź logi plikowe Gateway przez RPC (działa w trybie zdalnym).

Powiązane:

  * Omówienie logowania: [Logowanie](</pl/logging>)
  * CLI Gateway: [gateway](</pl/cli/gateway>)


## Opcje

  * `--limit <n>`: maksymalna liczba wierszy logów do zwrócenia (domyślnie `200`)
  * `--max-bytes <n>`: maksymalna liczba bajtów do odczytania z pliku logu (domyślnie `250000`)
  * `--follow`: śledź strumień logów
  * `--interval <ms>`: interwał odpytywania podczas śledzenia (domyślnie `1000`)
  * `--json`: emituj zdarzenia JSON rozdzielane wierszami
  * `--plain`: wyjście zwykłym tekstem bez stylizowanego formatowania
  * `--no-color`: wyłącz kolory ANSI
  * `--local-time`: renderuj znaczniki czasu w lokalnej strefie czasowej


## Współdzielone opcje RPC Gateway

`openclaw logs` akceptuje także standardowe flagi klienta Gateway:

  * `--url <url>`: adres URL WebSocket Gateway
  * `--token <token>`: token Gateway
  * `--timeout <ms>`: limit czasu w ms (domyślnie `30000`)
  * `--expect-final`: czekaj na końcową odpowiedź, gdy wywołanie Gateway jest obsługiwane przez agenta


Gdy przekażesz `--url`, CLI nie stosuje automatycznie poświadczeń z konfiguracji ani środowiska. Podaj `--token` jawnie, jeśli docelowy Gateway wymaga uwierzytelnienia.

## Przykłady

bashCopy code
[code]
    openclaw logsopenclaw logs --followopenclaw logs --follow --interval 2000openclaw logs --limit 500 --max-bytes 500000openclaw logs --jsonopenclaw logs --plainopenclaw logs --no-coloropenclaw logs --limit 500openclaw logs --local-timeopenclaw logs --follow --local-timeopenclaw logs --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
[/code]

## Uwagi

  * Użyj `--local-time`, aby renderować znaczniki czasu w lokalnej strefie czasowej.
  * Jeśli niejawny lokalny local loopback Gateway poprosi o parowanie, zamknie połączenie podczas łączenia albo przekroczy limit czasu, zanim `logs.tail` odpowie, `openclaw logs` automatycznie przełączy się na skonfigurowany plik logu Gateway. Jawne cele `--url` nie używają tego mechanizmu awaryjnego.
  * Podczas używania `--follow` przejściowe rozłączenia gateway (zamknięcie WebSocket, przekroczenie limitu czasu, zerwanie połączenia) wyzwalają automatyczne ponowne połączenie z wykładniczym opóźnieniem (do 8 ponowień, z limitem 30 s między próbami). Przy każdej ponownej próbie ostrzeżenie jest wypisywane do stderr, a po udanym odpytywaniu wypisywany jest komunikat `[logs] gateway reconnected`. W trybie `--json` zarówno ostrzeżenie o ponownej próbie, jak i przejście po ponownym połączeniu są emitowane jako rekordy `{"type":"notice"}` do stderr. Błędy nienaprawialne (błąd uwierzytelniania, zła konfiguracja) nadal powodują natychmiastowe zakończenie.


## Powiązane

  * [Dokumentacja CLI](</pl/cli>)
  * [Logowanie Gateway](</pl/gateway/logging>)


Was this useful?YesNo