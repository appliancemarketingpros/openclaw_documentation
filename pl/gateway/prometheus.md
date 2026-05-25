---
title: Metryki Prometheus
source_url: https://docs.openclaw.ai/pl/gateway/prometheus
scraped_at: 2026-05-25
---

OpenClaw może udostępniać metryki diagnostyczne przez oficjalny Plugin `diagnostics-prometheus`. Nasłuchuje zaufanej diagnostyki wewnętrznej i renderuje tekstowy punkt końcowy Prometheus pod adresem:

textCopy code
[code]
    GET /api/diagnostics/prometheus
[/code]

Typ zawartości to `text/plain; version=0.0.4; charset=utf-8`, czyli standardowy format ekspozycji Prometheus.

Informacje o śladach, logach, wypychaniu OTLP i atrybutach semantycznych OpenTelemetry GenAI znajdziesz w sekcji [eksport OpenTelemetry](</pl/gateway/opentelemetry>).

## Szybki start

* ### Zainstaluj Plugin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/diagnostics-prometheus
[/code]

* ### Włącz Plugin

### Konfiguracja

json5Copy code
[code]
    {  plugins: {    allow: ["diagnostics-prometheus"],    entries: {      "diagnostics-prometheus": { enabled: true },    },  },  diagnostics: {    enabled: true,  },}
[/code]

### CLI

bashCopy code
[code]
    openclaw plugins enable diagnostics-prometheus
[/code]

* ### Uruchom ponownie Gateway

Trasa HTTP jest rejestrowana przy uruchamianiu Plugin, więc po włączeniu wykonaj przeładowanie.

* ### Zbieraj chronioną trasę

Wyślij to samo uwierzytelnianie Gateway, którego używają klienci operatora:

bashCopy code
[code]
    curl -H "Authorization: Bearer $OPENCLAW_GATEWAY_TOKEN" \  http://127.0.0.1:18789/api/diagnostics/prometheus
[/code]

* ### Podłącz Prometheus

yamlCopy code
[code]
    # prometheus.ymlscrape_configs:  - job_name: openclaw    scrape_interval: 30s    metrics_path: /api/diagnostics/prometheus    authorization:      credentials_file: /etc/prometheus/openclaw-gateway-token    static_configs:      - targets: ["openclaw-gateway:18789"]
[/code]

## Eksportowane metryki

Metryka | Typ | Etykiety  
---|---|---  
`openclaw_run_completed_total` | counter | `channel`, `model`, `outcome`, `provider`, `trigger`  
`openclaw_run_duration_seconds` | histogram | `channel`, `model`, `outcome`, `provider`, `trigger`  
`openclaw_model_call_total` | counter | `api`, `error_category`, `model`, `outcome`, `provider`, `transport`  
`openclaw_model_call_duration_seconds` | histogram | `api`, `error_category`, `model`, `outcome`, `provider`, `transport`  
`openclaw_model_tokens_total` | counter | `agent`, `channel`, `model`, `provider`, `token_type`  
`openclaw_gen_ai_client_token_usage` | histogram | `model`, `provider`, `token_type`  
`openclaw_model_cost_usd_total` | counter | `agent`, `channel`, `model`, `provider`  
`openclaw_tool_execution_total` | counter | `error_category`, `outcome`, `params_kind`, `tool`  
`openclaw_tool_execution_duration_seconds` | histogram | `error_category`, `outcome`, `params_kind`, `tool`  
`openclaw_harness_run_total` | counter | `channel`, `error_category`, `harness`, `model`, `outcome`, `phase`, `plugin`, `provider`  
`openclaw_harness_run_duration_seconds` | histogram | `channel`, `error_category`, `harness`, `model`, `outcome`, `phase`, `plugin`, `provider`  
`openclaw_message_processed_total` | counter | `channel`, `outcome`, `reason`  
`openclaw_message_processed_duration_seconds` | histogram | `channel`, `outcome`, `reason`  
`openclaw_message_delivery_started_total` | counter | `channel`, `delivery_kind`  
`openclaw_message_delivery_total` | counter | `channel`, `delivery_kind`, `error_category`, `outcome`  
`openclaw_message_delivery_duration_seconds` | histogram | `channel`, `delivery_kind`, `error_category`, `outcome`  
`openclaw_talk_event_total` | counter | `brain`, `event_type`, `mode`, `provider`, `transport`  
`openclaw_talk_event_duration_seconds` | histogram | `brain`, `event_type`, `mode`, `provider`, `transport`  
`openclaw_talk_audio_bytes` | histogram | `brain`, `event_type`, `mode`, `provider`, `transport`  
`openclaw_queue_lane_size` | gauge | `lane`  
`openclaw_queue_lane_wait_seconds` | histogram | `lane`  
`openclaw_session_state_total` | counter | `reason`, `state`  
`openclaw_session_queue_depth` | gauge | `state`  
`openclaw_session_recovery_total` | counter | `action`, `active_work_kind`, `state`, `status`  
`openclaw_session_recovery_age_seconds` | histogram | `action`, `active_work_kind`, `state`, `status`  
`openclaw_memory_bytes` | gauge | `kind`  
`openclaw_memory_rss_bytes` | histogram | brak  
`openclaw_memory_pressure_total` | counter | `level`, `reason`  
`openclaw_telemetry_exporter_total` | counter | `exporter`, `reason`, `signal`, `status`  
`openclaw_prometheus_series_dropped_total` | counter | brak  
  
## Zasady etykiet

Ograniczone etykiety o niskiej krotności

Etykiety Prometheus pozostają ograniczone i mają niską krotność. Eksporter nie emituje surowych identyfikatorów diagnostycznych, takich jak `runId`, `sessionKey`, `sessionId`, `callId`, `toolCallId`, identyfikatory wiadomości, identyfikatory czatów ani identyfikatory żądań dostawcy.

Wartości etykiet są redagowane i muszą być zgodne z polityką znaków o niskiej krotności OpenClaw. Wartości, które nie spełniają tej polityki, są zastępowane przez `unknown`, `other` lub `none`, zależnie od metryki.

Limit serii i rozliczanie przepełnienia

Eksporter ogranicza przechowywane w pamięci szeregi czasowe do **2048** serii łącznie dla liczników, wskaźników i histogramów. Nowe serie powyżej tego limitu są odrzucane, a `openclaw_prometheus_series_dropped_total` zwiększa się o jeden za każdym razem.

Traktuj ten licznik jako twardy sygnał, że atrybut po stronie źródła przecieka wartości o wysokiej kardynalności. Eksporter nigdy nie podnosi limitu automatycznie; jeśli licznik rośnie, napraw źródło zamiast wyłączać limit.

Co nigdy nie pojawia się w wyjściu Prometheus

  * tekst promptu, tekst odpowiedzi, dane wejściowe narzędzi, dane wyjściowe narzędzi, prompty systemowe
  * transkrypcje rozmów, ładunki audio, identyfikatory połączeń, identyfikatory pokoi, tokeny przekazania, identyfikatory tur i surowe identyfikatory sesji
  * surowe identyfikatory żądań dostawcy (tylko ograniczone hashe, tam gdzie mają zastosowanie, w spanach — nigdy w metrykach)
  * klucze sesji i identyfikatory sesji
  * nazwy hostów, ścieżki plików, wartości sekretów


## Przepisy PromQL

promqlCopy code
[code]
    # Tokens per minute, split by providersum by (provider) (rate(openclaw_model_tokens_total[1m])) # Spend (USD) over the last hour, by modelsum by (model) (increase(openclaw_model_cost_usd_total[1h])) # 95th percentile model run durationhistogram_quantile(  0.95,  sum by (le, provider, model)    (rate(openclaw_run_duration_seconds_bucket[5m]))) # Queue wait time SLO (95p under 2s)histogram_quantile(  0.95,  sum by (le, lane) (rate(openclaw_queue_lane_wait_seconds_bucket[5m]))) < 2 # Dropped Prometheus series (cardinality alarm)increase(openclaw_prometheus_series_dropped_total[15m]) > 0
[/code]

## Wybór między eksportem Prometheus a OpenTelemetry

OpenClaw obsługuje obie powierzchnie niezależnie. Możesz uruchomić jedną, obie albo żadną.

### diagnostics-prometheus

  * Model **pull** : Prometheus odczytuje `/api/diagnostics/prometheus`.
  * Nie wymaga zewnętrznego kolektora.
  * Uwierzytelnianie odbywa się przez normalne uwierzytelnianie Gateway.
  * Powierzchnia obejmuje tylko metryki (bez śladów ani dzienników).
  * Najlepsze dla stosów już ustandaryzowanych na Prometheus + Grafana.


### diagnostics-otel

  * Model **push** : OpenClaw wysyła OTLP/HTTP do kolektora lub backendu zgodnego z OTLP.
  * Powierzchnia obejmuje metryki, ślady i dzienniki.
  * Łączy się z Prometheus przez OpenTelemetry Collector (eksporter `prometheus` lub `prometheusremotewrite`), gdy potrzebujesz obu.
  * Pełny katalog znajdziesz w [eksporcie OpenTelemetry](</pl/gateway/opentelemetry>).


## Rozwiązywanie problemów

Pusta treść odpowiedzi

  * Sprawdź `diagnostics.enabled: true` w konfiguracji.
  * Potwierdź, że Plugin jest włączony i załadowany za pomocą `openclaw plugins list --enabled`.
  * Wygeneruj trochę ruchu; liczniki i histogramy emitują wiersze dopiero po co najmniej jednym zdarzeniu.

401 / brak autoryzacji

Endpoint wymaga zakresu operatora Gateway (`auth: "gateway"` z `gatewayRuntimeScopeSurface: "trusted-operator"`). Użyj tego samego tokenu lub hasła, którego Prometheus używa dla dowolnej innej trasy operatora Gateway. Nie ma publicznego trybu bez uwierzytelniania.

`openclaw_prometheus_series_dropped_total` rośnie

Nowy atrybut przekracza limit **2048** serii. Sprawdź ostatnie metryki pod kątem etykiety o niespodziewanie wysokiej kardynalności i napraw ją u źródła. Eksporter celowo odrzuca nowe serie zamiast po cichu przepisywać etykiety.

Prometheus pokazuje nieaktualne serie po restarcie

Plugin przechowuje stan wyłącznie w pamięci. Po restarcie Gateway liczniki resetują się do zera, a wskaźniki wznawiają pracę od następnej zgłoszonej wartości. Użyj PromQL `rate()` i `increase()`, aby czysto obsługiwać resety.

## Powiązane

  * [Eksport diagnostyki](</pl/gateway/diagnostics>) — lokalne archiwum ZIP z diagnostyką dla pakietów wsparcia
  * [Kondycja i gotowość](</pl/gateway/health>) — sondy `/healthz` i `/readyz`
  * [Logowanie](</pl/logging>) — logowanie oparte na plikach
  * [Eksport OpenTelemetry](</pl/gateway/opentelemetry>) — wysyłanie OTLP dla śladów, metryk i logów


Was this useful?YesNo