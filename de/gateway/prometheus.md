---
title: Prometheus-Metriken
source_url: https://docs.openclaw.ai/de/gateway/prometheus
scraped_at: 2026-05-25
---

OpenClaw kann Diagnosemetriken über das offizielle `diagnostics-prometheus`-Plugin bereitstellen. Es lauscht auf vertrauenswürdige interne Diagnoseereignisse und rendert einen Prometheus-Text-Endpunkt unter:

textCopy code
[code]
    GET /api/diagnostics/prometheus
[/code]

Der Inhaltstyp ist `text/plain; version=0.0.4; charset=utf-8`, das standardmäßige Prometheus-Expositionsformat.

Für Traces, Logs, OTLP-Push und semantische OpenTelemetry-GenAI-Attribute siehe [OpenTelemetry-Export](</de/gateway/opentelemetry>).

## Schnellstart

* ### Plugin installieren

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/diagnostics-prometheus
[/code]

* ### Plugin aktivieren

### Konfiguration

json5Copy code
[code]
    {  plugins: {    allow: ["diagnostics-prometheus"],    entries: {      "diagnostics-prometheus": { enabled: true },    },  },  diagnostics: {    enabled: true,  },}
[/code]

### CLI

bashCopy code
[code]
    openclaw plugins enable diagnostics-prometheus
[/code]

* ### Gateway neu starten

Die HTTP-Route wird beim Plugin-Start registriert. Laden Sie daher nach der Aktivierung neu.

* ### Geschützte Route scrapen

Senden Sie dieselbe Gateway-Authentifizierung, die Ihre Operator-Clients verwenden:

bashCopy code
[code]
    curl -H "Authorization: Bearer $OPENCLAW_GATEWAY_TOKEN" \  http://127.0.0.1:18789/api/diagnostics/prometheus
[/code]

* ### Prometheus anbinden

yamlCopy code
[code]
    # prometheus.ymlscrape_configs:  - job_name: openclaw    scrape_interval: 30s    metrics_path: /api/diagnostics/prometheus    authorization:      credentials_file: /etc/prometheus/openclaw-gateway-token    static_configs:      - targets: ["openclaw-gateway:18789"]
[/code]

## Exportierte Metriken

Metrik | Typ | Labels  
---|---|---  
`openclaw_run_completed_total` | Zähler | `channel`, `model`, `outcome`, `provider`, `trigger`  
`openclaw_run_duration_seconds` | Histogramm | `channel`, `model`, `outcome`, `provider`, `trigger`  
`openclaw_model_call_total` | Zähler | `api`, `error_category`, `model`, `outcome`, `provider`, `transport`  
`openclaw_model_call_duration_seconds` | Histogramm | `api`, `error_category`, `model`, `outcome`, `provider`, `transport`  
`openclaw_model_tokens_total` | Zähler | `agent`, `channel`, `model`, `provider`, `token_type`  
`openclaw_gen_ai_client_token_usage` | Histogramm | `model`, `provider`, `token_type`  
`openclaw_model_cost_usd_total` | Zähler | `agent`, `channel`, `model`, `provider`  
`openclaw_tool_execution_total` | Zähler | `error_category`, `outcome`, `params_kind`, `tool`  
`openclaw_tool_execution_duration_seconds` | Histogramm | `error_category`, `outcome`, `params_kind`, `tool`  
`openclaw_harness_run_total` | Zähler | `channel`, `error_category`, `harness`, `model`, `outcome`, `phase`, `plugin`, `provider`  
`openclaw_harness_run_duration_seconds` | Histogramm | `channel`, `error_category`, `harness`, `model`, `outcome`, `phase`, `plugin`, `provider`  
`openclaw_message_processed_total` | Zähler | `channel`, `outcome`, `reason`  
`openclaw_message_processed_duration_seconds` | Histogramm | `channel`, `outcome`, `reason`  
`openclaw_message_delivery_started_total` | Zähler | `channel`, `delivery_kind`  
`openclaw_message_delivery_total` | Zähler | `channel`, `delivery_kind`, `error_category`, `outcome`  
`openclaw_message_delivery_duration_seconds` | Histogramm | `channel`, `delivery_kind`, `error_category`, `outcome`  
`openclaw_talk_event_total` | Zähler | `brain`, `event_type`, `mode`, `provider`, `transport`  
`openclaw_talk_event_duration_seconds` | Histogramm | `brain`, `event_type`, `mode`, `provider`, `transport`  
`openclaw_talk_audio_bytes` | Histogramm | `brain`, `event_type`, `mode`, `provider`, `transport`  
`openclaw_queue_lane_size` | Messwert | `lane`  
`openclaw_queue_lane_wait_seconds` | Histogramm | `lane`  
`openclaw_session_state_total` | Zähler | `reason`, `state`  
`openclaw_session_queue_depth` | Messwert | `state`  
`openclaw_session_recovery_total` | Zähler | `action`, `active_work_kind`, `state`, `status`  
`openclaw_session_recovery_age_seconds` | Histogramm | `action`, `active_work_kind`, `state`, `status`  
`openclaw_memory_bytes` | Messwert | `kind`  
`openclaw_memory_rss_bytes` | Histogramm | keine  
`openclaw_memory_pressure_total` | Zähler | `level`, `reason`  
`openclaw_telemetry_exporter_total` | Zähler | `exporter`, `reason`, `signal`, `status`  
`openclaw_prometheus_series_dropped_total` | Zähler | keine  
  
## Label-Richtlinie

Begrenzte Labels mit geringer Kardinalität

Prometheus-Labels bleiben begrenzt und haben geringe Kardinalität. Der Exporter gibt keine rohen Diagnosekennungen wie `runId`, `sessionKey`, `sessionId`, `callId`, `toolCallId`, Nachrichten-IDs, Chat-IDs oder Provider-Anfrage-IDs aus.

Label-Werte werden redigiert und müssen der OpenClaw-Zeichenrichtlinie für geringe Kardinalität entsprechen. Werte, die die Richtlinie nicht erfüllen, werden je nach Metrik durch `unknown`, `other` oder `none` ersetzt.

Reihengrenze und Überlaufzählung

Der Exporter begrenzt die im Speicher behaltenen Zeitreihen auf **2048** Reihen über Counter, Gauges und Histogramme hinweg. Neue Reihen über diese Grenze hinaus werden verworfen, und `openclaw_prometheus_series_dropped_total` wird jedes Mal um eins erhöht.

Beobachten Sie diesen Counter als klares Signal dafür, dass ein vorgelagertes Attribut Werte mit hoher Kardinalität weitergibt. Der Exporter hebt die Grenze nie automatisch an; wenn sie erreicht wird, beheben Sie die Ursache, statt die Grenze zu deaktivieren.

Was nie in der Prometheus-Ausgabe erscheint

  * Prompt-Text, Antworttext, Tool-Eingaben, Tool-Ausgaben, System-Prompts
  * Talk-Transkripte, Audio-Payloads, Anruf-IDs, Raum-IDs, Handoff-Token, Turn-IDs und rohe Sitzungs-IDs
  * rohe Provider-Anfrage-IDs (nur begrenzte Hashes, wo zutreffend, auf Spans — nie auf Metriken)
  * Sitzungsschlüssel und Sitzungs-IDs
  * Hostnamen, Dateipfade, geheime Werte


## PromQL-Rezepte

promqlCopy code
[code]
    # Tokens per minute, split by providersum by (provider) (rate(openclaw_model_tokens_total[1m])) # Spend (USD) over the last hour, by modelsum by (model) (increase(openclaw_model_cost_usd_total[1h])) # 95th percentile model run durationhistogram_quantile(  0.95,  sum by (le, provider, model)    (rate(openclaw_run_duration_seconds_bucket[5m]))) # Queue wait time SLO (95p under 2s)histogram_quantile(  0.95,  sum by (le, lane) (rate(openclaw_queue_lane_wait_seconds_bucket[5m]))) < 2 # Dropped Prometheus series (cardinality alarm)increase(openclaw_prometheus_series_dropped_total[15m]) > 0
[/code]

## Auswahl zwischen Prometheus- und OpenTelemetry-Export

OpenClaw unterstützt beide Oberflächen unabhängig voneinander. Sie können eine davon, beide oder keine verwenden.

### diagnostics-prometheus

  * **Pull** -Modell: Prometheus ruft `/api/diagnostics/prometheus` ab.
  * Kein externer Collector erforderlich.
  * Authentifiziert über die normale Gateway-Authentifizierung.
  * Die Oberfläche umfasst nur Metriken (keine Traces oder Logs).
  * Am besten für Stacks geeignet, die bereits auf Prometheus + Grafana standardisiert sind.


### diagnostics-otel

  * **Push** -Modell: OpenClaw sendet OTLP/HTTP an einen Collector oder ein OTLP-kompatibles Backend.
  * Die Oberfläche umfasst Metriken, Traces und Logs.
  * Bindet Prometheus über einen OpenTelemetry Collector (`prometheus`\- oder `prometheusremotewrite`-Exporter) an, wenn Sie beides benötigen.
  * Den vollständigen Katalog finden Sie unter [OpenTelemetry-Export](</de/gateway/opentelemetry>).


## Fehlerbehebung

Leerer Antwortkörper

  * Prüfen Sie `diagnostics.enabled: true` in der Konfiguration.
  * Bestätigen Sie mit `openclaw plugins list --enabled`, dass das Plugin aktiviert und geladen ist.
  * Erzeugen Sie etwas Traffic; Counter und Histogramme geben erst nach mindestens einem Ereignis Zeilen aus.

401 / nicht autorisiert

Der Endpoint erfordert den Gateway-Operator-Scope (`auth: "gateway"` mit `gatewayRuntimeScopeSurface: "trusted-operator"`). Verwenden Sie dasselbe Token oder Passwort, das Prometheus für jede andere Gateway-Operator-Route verwendet. Es gibt keinen öffentlichen, nicht authentifizierten Modus.

`openclaw_prometheus_series_dropped_total` steigt

Ein neues Attribut überschreitet die Grenze von **2048** Reihen. Prüfen Sie aktuelle Metriken auf ein Label mit unerwartet hoher Kardinalität und beheben Sie die Ursache. Der Exporter verwirft neue Reihen absichtlich, statt Labels stillschweigend umzuschreiben.

Prometheus zeigt nach einem Neustart veraltete Reihen

Das Plugin hält den Zustand nur im Speicher. Nach einem Gateway-Neustart werden Counter auf null zurückgesetzt, und Gauges beginnen wieder mit ihrem nächsten gemeldeten Wert. Verwenden Sie PromQL `rate()` und `increase()`, um Zurücksetzungen sauber zu behandeln.

## Verwandt

  * [Diagnoseexport](</de/gateway/diagnostics>) — lokale Diagnose-ZIP-Datei für Support-Bundles
  * [Zustand und Bereitschaft](</de/gateway/health>) — Prüfungen für `/healthz` und `/readyz`
  * [Logging](</de/logging>) — dateibasiertes Logging
  * [OpenTelemetry-Export](</de/gateway/opentelemetry>) — OTLP-Push für Traces, Metriken und Logs


Was this useful?YesNo