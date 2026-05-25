---
title: Flagi diagnostyczne
source_url: https://docs.openclaw.ai/pl/diagnostics/flags
scraped_at: 2026-05-25
---

Flagi diagnostyczne pozwalają włączać ukierunkowane logi debugowania bez włączania szczegółowego logowania wszędzie. Flagi są opcjonalne i nie mają wpływu, chyba że dany podsystem je sprawdza.

## Jak to działa

  * Flagi to ciągi znaków (bez rozróżniania wielkości liter).
  * Flagi można włączyć w konfiguracji lub przez nadpisanie zmienną środowiskową.
  * Obsługiwane są symbole wieloznaczne: 
    * `telegram.*` pasuje do `telegram.http`
    * `*` włącza wszystkie flagi


## Włączanie przez konfigurację

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http"]  }}
[/code]

Wiele flag:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http", "brave.http", "gateway.*"]  }}
[/code]

Uruchom ponownie Gateway po zmianie flag.

## Nadpisanie zmienną środowiskową (jednorazowe)

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=telegram.http,telegram.payload
[/code]

Wyłączenie wszystkich flag:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=0
[/code]

## Artefakty osi czasu

Flaga `timeline` zapisuje ustrukturyzowane zdarzenia czasowe uruchamiania i działania dla zewnętrznych narzędzi QA:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=timeline \OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=/tmp/openclaw-timeline.jsonl \openclaw gateway run
[/code]

Możesz też włączyć ją w konfiguracji:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["timeline"]  }}
[/code]

Ścieżka pliku osi czasu nadal pochodzi z `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH`. Gdy `timeline` jest włączona tylko z konfiguracji, najwcześniejsze zakresy ładowania konfiguracji nie są emitowane, ponieważ OpenClaw nie odczytał jeszcze konfiguracji; kolejne zakresy uruchamiania używają flagi z konfiguracji.

`OPENCLAW_DIAGNOSTICS=1`, `OPENCLAW_DIAGNOSTICS=all` oraz `OPENCLAW_DIAGNOSTICS=*` również włączają oś czasu, ponieważ włączają każdą flagę diagnostyczną. Użyj `timeline`, gdy potrzebujesz tylko artefaktu czasowego JSONL.

Rekordy osi czasu używają koperty `openclaw.diagnostics.v1`. Zdarzenia mogą zawierać identyfikatory procesów, nazwy faz, nazwy zakresów, czasy trwania, identyfikatory pluginów, liczby zależności, próbki opóźnień pętli zdarzeń, nazwy operacji dostawców, stan zakończenia procesów potomnych oraz nazwy/komunikaty błędów uruchamiania. Traktuj pliki osi czasu jako lokalne artefakty diagnostyczne; przejrzyj je przed udostępnieniem poza swoją maszynę.

## Gdzie trafiają logi

Flagi emitują logi do standardowego pliku logu diagnostycznego. Domyślnie:

CodeCopy code
[code]
    /tmp/openclaw/openclaw-YYYY-MM-DD.log
[/code]

Jeśli ustawisz `logging.file`, użyj zamiast tego tej ścieżki. Logi są w formacie JSONL (jeden obiekt JSON na wiersz). Redakcja nadal obowiązuje zgodnie z `logging.redactSensitive`.

## Wyodrębnianie logów

Wybierz najnowszy plik logu:

bashCopy code
[code]
    ls -t /tmp/openclaw/openclaw-*.log | head -n 1
[/code]

Filtruj diagnostykę HTTP Telegram:

bashCopy code
[code]
    rg "telegram http error" /tmp/openclaw/openclaw-*.log
[/code]

Filtruj diagnostykę HTTP Brave Search:

bashCopy code
[code]
    rg "brave http" /tmp/openclaw/openclaw-*.log
[/code]

Albo śledź log podczas odtwarzania problemu:

bashCopy code
[code]
    tail -f /tmp/openclaw/openclaw-$(date +%F).log | rg "telegram http error"
[/code]

W przypadku zdalnych Gateway możesz też użyć `openclaw logs --follow` (zobacz [/cli/logs](</pl/cli/logs>)).

## Uwagi

  * Jeśli `logging.level` jest ustawiony wyżej niż `warn`, te logi mogą zostać wyciszone. Domyślne `info` jest odpowiednie.
  * `brave.http` loguje adresy URL/parametry zapytań żądań Brave Search, status/czas odpowiedzi oraz zdarzenia trafienia/pominięcia/zapisu w pamięci podręcznej. Nie loguje kluczy API ani treści odpowiedzi, ale zapytania wyszukiwania mogą być wrażliwe.
  * Flagi można bezpiecznie pozostawić włączone; wpływają tylko na objętość logów konkretnego podsystemu.
  * Użyj [/logging](</pl/logging>), aby zmienić miejsca docelowe logów, poziomy i redakcję.


## Powiązane

  * [Diagnostyka Gateway](</pl/gateway/diagnostics>)
  * [Rozwiązywanie problemów z Gateway](</pl/gateway/troubleshooting>)


Was this useful?YesNo