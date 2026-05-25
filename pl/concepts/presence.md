---
title: Obecność
source_url: https://docs.openclaw.ai/pl/concepts/presence
scraped_at: 2026-05-25
---

„Obecność” w OpenClaw to lekki, best-effort widok:

  * samego **Gateway** , oraz
  * **klientów połączonych z Gateway** (aplikacja mac, WebChat, CLI itd.)


Obecność służy głównie do renderowania karty **Instancje** w aplikacji macOS oraz do zapewniania operatorowi szybkiego wglądu.

## Pola obecności (co jest wyświetlane)

Wpisy obecności to uporządkowane obiekty z polami takimi jak:

  * `instanceId` (opcjonalne, ale zdecydowanie zalecane): stabilna tożsamość klienta (zwykle `connect.client.instanceId`)
  * `host`: przyjazna dla człowieka nazwa hosta
  * `ip`: best-effort adres IP
  * `version`: ciąg wersji klienta
  * `deviceFamily` / `modelIdentifier`: wskazówki dotyczące sprzętu
  * `mode`: `ui`, `webchat`, `cli`, `backend`, `probe`, `test`, `node`, ...
  * `lastInputSeconds`: „sekundy od ostatniego wejścia użytkownika” (jeśli znane)
  * `reason`: `self`, `connect`, `node-connected`, `periodic`, ...
  * `ts`: znacznik czasu ostatniej aktualizacji (ms od epoki)


## Producenci (skąd pochodzi obecność)

Wpisy obecności są tworzone przez wiele źródeł i **scalane**.

### 1) Własny wpis Gateway

Gateway zawsze dodaje wpis „self” podczas uruchamiania, aby interfejsy użytkownika pokazywały host Gateway jeszcze przed połączeniem jakichkolwiek klientów.

### 2) Połączenie WebSocket

Każdy klient WS zaczyna od żądania `connect`. Po udanym uzgadnianiu Gateway wykonuje upsert wpisu obecności dla tego połączenia.

#### Dlaczego jednorazowe polecenia CLI się nie pojawiają

CLI często łączy się na potrzeby krótkich, jednorazowych poleceń. Aby uniknąć zaśmiecania listy Instancji, `client.mode === "cli"` **nie** jest przekształcane we wpis obecności.

### 3) Beacony `system-event`

Klienci mogą wysyłać bogatsze okresowe beacony za pomocą metody `system-event`. Aplikacja mac używa tego do zgłaszania nazwy hosta, IP oraz `lastInputSeconds`.

### 4) Połączenia Node (rola: node)

Gdy Node łączy się przez WebSocket Gateway z `role: node`, Gateway wykonuje upsert wpisu obecności dla tego Node (ten sam przepływ co dla innych klientów WS).

## Reguły scalania i deduplikacji (dlaczego `instanceId` ma znaczenie)

Wpisy obecności są przechowywane w jednej mapie w pamięci:

  * Wpisy są kluczowane według **klucza obecności**.
  * Najlepszym kluczem jest stabilny `instanceId` (z `connect.client.instanceId`), który przetrwa ponowne uruchomienia.
  * Klucze nie rozróżniają wielkości liter.


Jeśli klient ponownie połączy się bez stabilnego `instanceId`, może pojawić się jako **zduplikowany** wiersz.

## TTL i ograniczony rozmiar

Obecność jest celowo efemeryczna:

  * **TTL:** wpisy starsze niż 5 minut są przycinane
  * **Maksymalna liczba wpisów:** 200 (najstarsze są usuwane jako pierwsze)


Dzięki temu lista pozostaje świeża i unika się nieograniczonego wzrostu zużycia pamięci.

## Zastrzeżenie dotyczące połączeń zdalnych/tuneli (adresy IP loopback)

Gdy klient łączy się przez tunel SSH / lokalne przekierowanie portu, Gateway może widzieć adres zdalny jako `127.0.0.1`. Aby uniknąć nadpisywania dobrego adresu IP zgłoszonego przez klienta, zdalne adresy loopback są ignorowane.

## Konsumenci

### Karta Instancje w macOS

Aplikacja macOS renderuje wynik `system-presence` i stosuje mały wskaźnik stanu (Aktywny/Bezczynny/Nieaktualny) na podstawie wieku ostatniej aktualizacji.

## Wskazówki debugowania

  * Aby zobaczyć surową listę, wywołaj `system-presence` względem Gateway.
  * Jeśli widzisz duplikaty: 
    * potwierdź, że klienci wysyłają stabilny `client.instanceId` podczas uzgadniania
    * potwierdź, że okresowe beacony używają tego samego `instanceId`
    * sprawdź, czy wpis pochodzący z połączenia nie ma `instanceId` (duplikaty są oczekiwane)


## Powiązane

[**Wskaźniki pisania** Kiedy wskaźniki pisania są wysyłane i jak je dostrajać. ](</pl/concepts/typing-indicators>) [**Streaming i chunking** Streaming wychodzący, chunking oraz formatowanie dla poszczególnych kanałów. ](</pl/concepts/streaming>) [**Architektura Gateway** Komponenty Gateway oraz protokół WebSocket, który steruje aktualizacjami obecności. ](</pl/concepts/architecture>) [**Protokół Gateway** Protokół przewodowy dla `connect`, `system-event` i `system-presence`. ](</pl/gateway/protocol>)

Was this useful?YesNo