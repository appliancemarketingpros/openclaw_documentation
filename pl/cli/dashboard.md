---
title: Panel
source_url: https://docs.openclaw.ai/pl/cli/dashboard
scraped_at: 2026-05-25
---

# `openclaw dashboard`

Otwórz Control UI przy użyciu bieżącego uwierzytelnienia.

bashCopy code
[code]
    openclaw dashboardopenclaw dashboard --no-open
[/code]

Uwagi:

  * `dashboard` rozwiązuje skonfigurowane SecretRefs `gateway.auth.token`, gdy to możliwe.
  * `dashboard` respektuje `gateway.tls.enabled`: Gateway z włączonym TLS wypisuje/otwiera adresy URL Control UI z `https://` i łączy się przez `wss://`.
  * Jeśli dostarczenie adresu URL pulpitu uwierzytelnionego tokenem przez schowek/przeglądarkę się nie powiedzie, `dashboard` rejestruje bezpieczną wskazówkę dotyczącą ręcznego uwierzytelnienia, wskazującą `OPENCLAW_GATEWAY_TOKEN`, `gateway.auth.token` oraz klucz fragmentu `token`, bez wypisywania wartości tokenu.
  * W przypadku tokenów zarządzanych przez SecretRef (rozwiązanych lub nierozwiązanych) `dashboard` wypisuje/kopiuje/otwiera adres URL bez tokenu, aby uniknąć ujawniania zewnętrznych sekretów w danych wyjściowych terminala, historii schowka lub argumentach uruchamiania przeglądarki.
  * Jeśli `gateway.auth.token` jest zarządzany przez SecretRef, ale nie został rozwiązany w tej ścieżce polecenia, polecenie wypisuje adres URL bez tokenu oraz wyraźne wskazówki naprawcze zamiast osadzać nieprawidłowy symbol zastępczy tokenu.


## Powiązane

  * [Dokumentacja CLI](</pl/cli>)
  * [Dashboard](</pl/web/dashboard>)


Was this useful?YesNo