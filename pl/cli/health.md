---
title: Kondycja
source_url: https://docs.openclaw.ai/pl/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

Pobiera stan z działającego Gateway.

## Opcje

Flaga | Domyślne | Opis  
---|---|---  
`--json` | `false` | Wypisuje JSON czytelny maszynowo zamiast tekstu.  
`--timeout <ms>` | `10000` | Limit czasu połączenia w milisekundach.  
`--verbose` | `false` | Szczegółowe logowanie. Wymusza sondowanie na żywo i rozszerza dane wyjściowe dla każdego agenta.  
`--debug` | `false` | Alias dla `--verbose`.  
  
Przykłady:

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

Uwagi:

  * Domyślnie `openclaw health` pyta działający Gateway o migawkę jego stanu. Gdy Gateway ma już świeżą migawkę w pamięci podręcznej, może zwrócić ten buforowany ładunek i odświeżyć go w tle.
  * `--verbose` wymusza sondowanie na żywo, wypisuje szczegóły połączenia z Gateway i rozszerza czytelne dla człowieka dane wyjściowe na wszystkie skonfigurowane konta i agentów.
  * Dane wyjściowe obejmują magazyny sesji dla każdego agenta, gdy skonfigurowano wielu agentów.


## Powiązane

  * [Dokumentacja CLI](</pl/cli>)
  * [Stan Gateway](</pl/gateway/health>)


Was this useful?YesNo