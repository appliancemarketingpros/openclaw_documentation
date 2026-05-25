---
title: System
source_url: https://docs.openclaw.ai/pl/cli/system
scraped_at: 2026-05-25
---

# `openclaw system`

Pomocnicze narzędzia na poziomie systemu dla Gateway: kolejkowanie zdarzeń systemowych, sterowanie mechanizmem Heartbeat i wyświetlanie obecności.

Wszystkie podpolecenia `system` używają Gateway RPC i akceptują wspólne flagi klienta:

  * `--url <url>`
  * `--token <token>`
  * `--timeout <ms>`
  * `--expect-final`


## Typowe polecenia

bashCopy code
[code]
    openclaw system event --text "Check for urgent follow-ups" --mode nowopenclaw system event --text "Check for urgent follow-ups" --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"openclaw system heartbeat enableopenclaw system heartbeat lastopenclaw system presence
[/code]

## `system event`

Domyślnie dodaje zdarzenie systemowe do kolejki w sesji **main**. Następny Heartbeat wstrzyknie je do promptu jako wiersz `System:`. Użyj `--mode now`, aby uruchomić Heartbeat natychmiast; `next-heartbeat` czeka na następny zaplanowany takt.

Przekaż `--session-key`, aby wskazać konkretną sesję (na przykład w celu przekazania zakończenia zadania asynchronicznego z powrotem do kanału, który je uruchomił).

> **Wyjątek czasowy z`--session-key`:** gdy podano `--session-key`, `--mode next-heartbeat` jest sprowadzane do natychmiastowego, ukierunkowanego wybudzenia zamiast czekania na następny zaplanowany takt. Ukierunkowane wybudzenia używają intencji Heartbeat `immediate`, więc omijają bramkę „not-due” runnera, która w przeciwnym razie odroczyłaby (i w praktyce porzuciła) wybudzenie z intencją `event`. Jeśli chcesz opóźnionego dostarczenia, pomiń `--session-key`, aby zdarzenie trafiło do sesji main i zostało obsłużone przy następnym regularnym Heartbeat.

Flagi:

  * `--text <text>`: wymagany tekst zdarzenia systemowego.
  * `--mode <mode>`: `now` albo `next-heartbeat` (domyślnie).
  * `--session-key <sessionKey>`: opcjonalne; wskazuje konkretną sesję agenta zamiast głównej sesji agenta. Klucze, które nie należą do rozwiązanego agenta, wracają do głównej sesji agenta.
  * `--json`: wyjście czytelne maszynowo.
  * `--url`, `--token`, `--timeout`, `--expect-final`: współdzielone flagi Gateway RPC.


## `system heartbeat last|enable|disable`

Elementy sterujące Heartbeat:

  * `last`: pokaż ostatnie zdarzenie Heartbeat.
  * `enable`: ponownie włącz Heartbeat (użyj tego, jeśli były wyłączone).
  * `disable`: wstrzymaj Heartbeat.


Flagi:

  * `--json`: wyjście czytelne maszynowo.
  * `--url`, `--token`, `--timeout`, `--expect-final`: współdzielone flagi Gateway RPC.


## `system presence`

Wyświetla bieżące wpisy obecności systemu znane Gateway (węzły, instancje i podobne wiersze statusu).

Flagi:

  * `--json`: wyjście czytelne maszynowo.
  * `--url`, `--token`, `--timeout`, `--expect-final`: współdzielone flagi Gateway RPC.


## Uwagi

  * Wymaga działającego Gateway osiągalnego przez bieżącą konfigurację (lokalną lub zdalną).
  * Zdarzenia systemowe są efemeryczne i nie są zachowywane między ponownymi uruchomieniami.


## Powiązane

  * [Dokumentacja CLI](</pl/cli>)


Was this useful?YesNo