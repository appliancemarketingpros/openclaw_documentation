---
title: Węzły
source_url: https://docs.openclaw.ai/pl/cli/nodes
scraped_at: 2026-05-25
---

# `openclaw nodes`

Zarządzaj sparowanymi Node (urządzeniami) i wywołuj możliwości Node.

Powiązane:

  * Przegląd Node: [Node](</pl/nodes>)
  * Kamera: [Node kamery](</pl/nodes/camera>)
  * Obrazy: [Node obrazów](</pl/nodes/images>)


Typowe opcje:

  * `--url`, `--token`, `--timeout`, `--json`


## Typowe polecenia

bashCopy code
[code]
    openclaw nodes listopenclaw nodes list --connectedopenclaw nodes list --last-connected 24hopenclaw nodes pendingopenclaw nodes approve <requestId>openclaw nodes reject <requestId>openclaw nodes remove --node <id|name|ip>openclaw nodes rename --node <id|name|ip> --name <displayName>openclaw nodes statusopenclaw nodes status --connectedopenclaw nodes status --last-connected 24h
[/code]

`nodes list` wypisuje tabele oczekujących/sparowanych elementów. Sparowane wiersze zawierają wiek najnowszego połączenia (Ostatnie połączenie). Użyj `--connected`, aby pokazać tylko aktualnie połączone Node. Użyj `--last-connected <duration>`, aby odfiltrować Node, które połączyły się w podanym czasie (np. `24h`, `7d`). Użyj `nodes remove --node <id|name|ip>`, aby usunąć nieaktualny rekord parowania Node należący do Gateway.

Uwaga dotycząca zatwierdzania:

  * `openclaw nodes pending` wymaga tylko zakresu parowania.
  * `gateway.nodes.pairing.autoApproveCidrs` może pominąć krok oczekiwania tylko dla jawnie zaufanego, pierwszego parowania urządzenia `role: node`. Domyślnie jest wyłączone i nie zatwierdza uaktualnień.
  * `openclaw nodes approve <requestId>` dziedziczy dodatkowe wymagania dotyczące zakresu z oczekującego żądania: 
    * żądanie bez polecenia: tylko parowanie
    * polecenia Node inne niż exec: parowanie + zapis
    * `system.run` / `system.run.prepare` / `system.which`: parowanie + admin


## Wywoływanie

bashCopy code
[code]
    openclaw nodes invoke --node <id|name|ip> --command <command> --params <json>
[/code]

Flagi wywołania:

  * `--params <json>`: ciąg obiektu JSON (domyślnie `{}`).
  * `--invoke-timeout <ms>`: limit czasu wywołania Node (domyślnie `15000`).
  * `--idempotency-key <key>`: opcjonalny klucz idempotencji.
  * `system.run` i `system.run.prepare` są tutaj blokowane; do wykonywania poleceń powłoki użyj narzędzia `exec` z `host=node`.


Do wykonywania poleceń powłoki na Node użyj narzędzia `exec` z `host=node` zamiast `openclaw nodes run`. CLI `nodes` koncentruje się teraz na możliwościach: bezpośrednie RPC przez `nodes invoke`, a także parowanie, kamera, ekran, lokalizacja, Canvas i powiadomienia. Polecenia Canvas są implementowane przez dołączony eksperymentalny Plugin Canvas; rdzeń zachowuje hak zgodności, aby pozostały dostępne pod `openclaw nodes canvas`.

## Powiązane

  * [Dokumentacja CLI](</pl/cli>)
  * [Node](</pl/nodes>)


Was this useful?YesNo