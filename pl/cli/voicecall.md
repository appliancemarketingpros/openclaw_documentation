---
title: Połączenie głosowe
source_url: https://docs.openclaw.ai/pl/cli/voicecall
scraped_at: 2026-05-25
---

# `openclaw voicecall`

`voicecall` to polecenie dostarczane przez Plugin. Pojawia się tylko wtedy, gdy Plugin połączeń głosowych jest zainstalowany i włączony.

Gdy Gateway działa, polecenia operacyjne (`call`, `start`, `continue`, `speak`, `dtmf`, `end`, `status`) są kierowane do środowiska uruchomieniowego połączeń głosowych tego Gateway. Jeśli żaden Gateway nie jest osiągalny, używają awaryjnie samodzielnego środowiska uruchomieniowego CLI.

## Podpolecenia

bashCopy code
[code]
    openclaw voicecall setup    [--json]openclaw voicecall smoke    [-t <phone>] [--message <text>] [--mode <m>] [--yes] [--json]openclaw voicecall call     -m <text> [-t <phone>] [--mode <m>]openclaw voicecall start    --to <phone> [--message <text>] [--mode <m>]openclaw voicecall continue --call-id <id> --message <text>openclaw voicecall speak    --call-id <id> --message <text>openclaw voicecall dtmf     --call-id <id> --digits <digits>openclaw voicecall end      --call-id <id>openclaw voicecall status   [--call-id <id>] [--json]openclaw voicecall tail     [--file <path>] [--since <n>] [--poll <ms>]openclaw voicecall latency  [--file <path>] [--last <n>]openclaw voicecall expose   [--mode <m>] [--path <p>] [--port <port>] [--serve-path <p>]
[/code]

Podpolecenie | Opis  
---|---  
`setup` | Pokazuje kontrole gotowości dostawcy i Webhook.  
`smoke` | Uruchamia kontrole gotowości; wykonuje testowe połączenie na żywo tylko z `--yes`.  
`call` | Inicjuje wychodzące połączenie głosowe.  
`start` | Alias `call` z wymaganym `--to` i opcjonalnym `--message`.  
`continue` | Odtwarza komunikat i czeka na następną odpowiedź.  
`speak` | Odtwarza komunikat bez czekania na odpowiedź.  
`dtmf` | Wysyła cyfry DTMF do aktywnego połączenia.  
`end` | Rozłącza aktywne połączenie.  
`status` | Sprawdza aktywne połączenia (lub jedno przez `--call-id`).  
`tail` | Śledzi `calls.jsonl` (przydatne podczas testów dostawcy).  
`latency` | Podsumowuje metryki opóźnienia tur z `calls.jsonl`.  
`expose` | Przełącza Tailscale serve/funnel dla punktu końcowego Webhook.  
  
## Konfiguracja i smoke

### `setup`

Domyślnie wypisuje kontrole gotowości czytelne dla człowieka. Przekaż `--json` dla skryptów.

bashCopy code
[code]
    openclaw voicecall setupopenclaw voicecall setup --json
[/code]

### `smoke`

Uruchamia te same kontrole gotowości. Nie wykona prawdziwego połączenia telefonicznego, chyba że obecne są zarówno `--to`, jak i `--yes`.

Flaga | Domyślnie | Opis  
---|---|---  
`-t, --to <phone>` | (brak) | Numer telefonu do połączenia na żywo smoke.  
`--message <text>` | `OpenClaw voice call smoke test.` | Komunikat do odtworzenia podczas połączenia smoke.  
`--mode <mode>` | `notify` | Tryb połączenia: `notify` lub `conversation`.  
`--yes` | `false` | Faktycznie wykonuje wychodzące połączenie na żywo.  
`--json` | `false` | Wypisuje JSON czytelny maszynowo.  
bashCopy code
[code]
    openclaw voicecall smokeopenclaw voicecall smoke --to "+15555550123"        # dry runopenclaw voicecall smoke --to "+15555550123" --yes  # live notify call
[/code]

## Cykl życia połączenia

### `call`

Inicjuje wychodzące połączenie głosowe.

Flaga | Wymagane | Domyślnie | Opis  
---|---|---|---  
`-m, --message <text>` | tak | (brak) | Komunikat do odtworzenia po połączeniu.  
`-t, --to <phone>` | nie | config `toNumber` | Numer telefonu E.164, pod który należy zadzwonić.  
`--mode <mode>` | nie | `conversation` | Tryb połączenia: `notify` (rozłącz po komunikacie) lub `conversation` (pozostań połączony).  
bashCopy code
[code]
    openclaw voicecall call --to "+15555550123" --message "Hello"openclaw voicecall call -m "Heads up" --mode notify
[/code]

### `start`

Alias `call` z innym domyślnym kształtem flag.

Flaga | Wymagane | Domyślnie | Opis  
---|---|---|---  
`--to <phone>` | tak | (brak) | Numer telefonu do połączenia.  
`--message <text>` | nie | (brak) | Komunikat do odtworzenia po połączeniu.  
`--mode <mode>` | nie | `conversation` | Tryb połączenia: `notify` lub `conversation`.  
  
### `continue`

Odtwarza komunikat i czeka na odpowiedź.

Flaga | Wymagane | Opis  
---|---|---  
`--call-id <id>` | tak | Identyfikator połączenia.  
`--message <text>` | tak | Komunikat do odtworzenia.  
  
### `speak`

Odtwarza komunikat bez czekania na odpowiedź.

Flaga | Wymagane | Opis  
---|---|---  
`--call-id <id>` | tak | Identyfikator połączenia.  
`--message <text>` | tak | Komunikat do odtworzenia.  
  
### `dtmf`

Wysyła cyfry DTMF do aktywnego połączenia.

Flaga | Wymagane | Opis  
---|---|---  
`--call-id <id>` | tak | Identyfikator połączenia.  
`--digits <digits>` | tak | Cyfry DTMF (np. `ww123456#` dla oczekiwania).  
  
### `end`

Rozłącza aktywne połączenie.

Flaga | Wymagane | Opis  
---|---|---  
`--call-id <id>` | tak | Identyfikator połączenia.  
  
### `status`

Sprawdza aktywne połączenia.

Flaga | Domyślnie | Opis  
---|---|---  
`--call-id <id>` | (brak) | Ogranicza wynik do jednego połączenia.  
`--json` | `false` | Wypisuje JSON czytelny maszynowo.  
bashCopy code
[code]
    openclaw voicecall statusopenclaw voicecall status --jsonopenclaw voicecall status --call-id <id>
[/code]

## Logi i metryki

### `tail`

Śledzi dziennik JSONL połączeń głosowych. Przy starcie wypisuje ostatnie `--since` wierszy, a następnie strumieniuje nowe wiersze w miarę ich zapisywania.

Flaga | Domyślnie | Opis  
---|---|---  
`--file <path>` | rozwiązywane z magazynu Plugin | Ścieżka do `calls.jsonl`.  
`--since <n>` | `25` | Wiersze do wypisania przed śledzeniem.  
`--poll <ms>` | `250` (minimum 50) | Interwał odpytywania w milisekundach.  
  
### `latency`

Podsumowuje metryki opóźnienia tury i oczekiwania na nasłuch z `calls.jsonl`. Wynik to JSON z podsumowaniami `recordsScanned`, `turnLatency` i `listenWait`.

Flaga | Domyślnie | Opis  
---|---|---  
`--file <path>` | rozwiązywane z magazynu Plugin | Ścieżka do `calls.jsonl`.  
`--last <n>` | `200` (minimum 1) | Liczba ostatnich rekordów do przeanalizowania.  
  
## Udostępnianie Webhook

### `expose`

Włącza, wyłącza lub zmienia konfigurację Tailscale serve/funnel dla głosowego Webhook.

Flaga | Domyślnie | Opis  
---|---|---  
`--mode <mode>` | `funnel` | `off`, `serve` (tailnet) lub `funnel` (publiczne).  
`--path <path>` | config `tailscale.path` lub `--serve-path` | Ścieżka Tailscale do udostępnienia.  
`--port <port>` | config `serve.port` lub `3334` | Lokalny port Webhook.  
`--serve-path <path>` | config `serve.path` lub `/voice/webhook` | Lokalna ścieżka Webhook.  
bashCopy code
[code]
    openclaw voicecall expose --mode serveopenclaw voicecall expose --mode funnelopenclaw voicecall expose --mode off
[/code]

## Powiązane

  * [Referencja CLI](</pl/cli>)
  * [Plugin połączeń głosowych](</pl/plugins/voice-call>)


Was this useful?YesNo