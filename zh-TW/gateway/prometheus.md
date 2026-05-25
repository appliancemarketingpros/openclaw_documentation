---
title: Prometheus 指標
source_url: https://docs.openclaw.ai/zh-TW/gateway/prometheus
scraped_at: 2026-05-25
---

OpenClaw 可以透過官方的 `diagnostics-prometheus` Plugin 公開診斷指標。它會監聽受信任的內部診斷，並在以下位置呈現 Prometheus 文字端點：

textCopy code
[code]
    GET /api/diagnostics/prometheus
[/code]

內容類型是 `text/plain; version=0.0.4; charset=utf-8`，也就是標準的 Prometheus exposition 格式。

如需追蹤、日誌、OTLP 推送，以及 OpenTelemetry GenAI 語意屬性，請參閱 [OpenTelemetry 匯出](</zh-TW/gateway/opentelemetry>)。

## 快速開始

* ### 安裝 Plugin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/diagnostics-prometheus
[/code]

* ### 啟用 Plugin

### 設定

json5Copy code
[code]
    {  plugins: {    allow: ["diagnostics-prometheus"],    entries: {      "diagnostics-prometheus": { enabled: true },    },  },  diagnostics: {    enabled: true,  },}
[/code]

### CLI

bashCopy code
[code]
    openclaw plugins enable diagnostics-prometheus
[/code]

* ### 重新啟動 Gateway

HTTP 路由會在 Plugin 啟動時註冊，因此啟用後請重新載入。

* ### 抓取受保護的路由

傳送與你的操作員用戶端相同的 Gateway 驗證：

bashCopy code
[code]
    curl -H "Authorization: Bearer $OPENCLAW_GATEWAY_TOKEN" \  http://127.0.0.1:18789/api/diagnostics/prometheus
[/code]

* ### 接上 Prometheus

yamlCopy code
[code]
    # prometheus.ymlscrape_configs:  - job_name: openclaw    scrape_interval: 30s    metrics_path: /api/diagnostics/prometheus    authorization:      credentials_file: /etc/prometheus/openclaw-gateway-token    static_configs:      - targets: ["openclaw-gateway:18789"]
[/code]

## 匯出的指標

指標 | 類型 | 標籤  
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
`openclaw_memory_rss_bytes` | histogram | 無  
`openclaw_memory_pressure_total` | counter | `level`, `reason`  
`openclaw_telemetry_exporter_total` | counter | `exporter`, `reason`, `signal`, `status`  
`openclaw_prometheus_series_dropped_total` | counter | 無  
  
## 標籤政策

有界、低基數標籤

Prometheus 標籤會維持有界且低基數。匯出器不會發出原始診斷識別碼，例如 `runId`、`sessionKey`、`sessionId`、`callId`、`toolCallId`、訊息 ID、聊天 ID，或供應商請求 ID。

標籤值會被遮罩，且必須符合 OpenClaw 的低基數字元政策。不符合政策的值會依指標替換為 `unknown`、`other` 或 `none`。

序列上限與溢位計算

匯出器在記憶體中保留的時間序列總數上限為 **2048** 個，包含計數器、量表與直方圖。超過該上限的新序列會被捨棄，且 `openclaw_prometheus_series_dropped_total` 每次都會遞增一。

請將此計數器視為上游屬性正在洩漏高基數值的明確訊號。匯出器不會自動提高上限；如果它持續上升，請修正來源，而不是停用上限。

Prometheus 輸出中絕不會出現的內容

  * 提示文字、回應文字、工具輸入、工具輸出、系統提示
  * Talk 逐字稿、音訊酬載、通話 ID、房間 ID、交接權杖、回合 ID，以及原始工作階段 ID
  * 原始提供者請求 ID（僅在適用時於 span 上使用有界雜湊，絕不出現在 metrics 上）
  * 工作階段金鑰與工作階段 ID
  * 主機名稱、檔案路徑、祕密值


## PromQL 配方

promqlCopy code
[code]
    # Tokens per minute, split by providersum by (provider) (rate(openclaw_model_tokens_total[1m])) # Spend (USD) over the last hour, by modelsum by (model) (increase(openclaw_model_cost_usd_total[1h])) # 95th percentile model run durationhistogram_quantile(  0.95,  sum by (le, provider, model)    (rate(openclaw_run_duration_seconds_bucket[5m]))) # Queue wait time SLO (95p under 2s)histogram_quantile(  0.95,  sum by (le, lane) (rate(openclaw_queue_lane_wait_seconds_bucket[5m]))) < 2 # Dropped Prometheus series (cardinality alarm)increase(openclaw_prometheus_series_dropped_total[15m]) > 0
[/code]

## 在 Prometheus 與 OpenTelemetry 匯出之間選擇

OpenClaw 獨立支援這兩種介面。你可以執行其中一種、兩者都執行，或兩者都不執行。

### diagnostics-prometheus

  * **拉取** 模型：Prometheus 擷取 `/api/diagnostics/prometheus`。
  * 不需要外部收集器。
  * 透過一般 Gateway 驗證進行驗證。
  * 介面僅包含 metrics（不含 traces 或 logs）。
  * 最適合已標準化使用 Prometheus + Grafana 的技術棧。


### diagnostics-otel

  * **推送** 模型：OpenClaw 將 OTLP/HTTP 傳送至收集器或 OTLP 相容後端。
  * 介面包含 metrics、traces 與 logs。
  * 當你同時需要兩者時，可透過 OpenTelemetry Collector（`prometheus` 或 `prometheusremotewrite` 匯出器）橋接至 Prometheus。
  * 完整目錄請參閱 [OpenTelemetry 匯出](</zh-TW/gateway/opentelemetry>)。


## 疑難排解

空白回應主體

  * 檢查設定中的 `diagnostics.enabled: true`。
  * 使用 `openclaw plugins list --enabled` 確認 Plugin 已啟用並載入。
  * 產生一些流量；計數器與直方圖只會在至少發生一次事件後輸出行。

401 / 未授權

端點需要 Gateway 操作者範圍（`auth: "gateway"` 搭配 `gatewayRuntimeScopeSurface: "trusted-operator"`）。請使用 Prometheus 用於任何其他 Gateway 操作者路由的相同權杖或密碼。沒有公開的未驗證模式。

`openclaw_prometheus_series_dropped_total` 正在上升

有新的屬性超過 **2048** 個序列的上限。檢查近期 metrics 中是否有非預期的高基數標籤，並在來源修正。匯出器會刻意捨棄新序列，而不是默默重寫標籤。

重新啟動後 Prometheus 顯示過期序列

Plugin 只在記憶體中保留狀態。Gateway 重新啟動後，計數器會重設為零，量表會在下一次回報值時重新開始。使用 PromQL `rate()` 與 `increase()` 來乾淨地處理重設。

## 相關內容

  * [診斷匯出](</zh-TW/gateway/diagnostics>) — 用於支援套件的本機診斷 ZIP 檔
  * [健康狀態與就緒狀態](</zh-TW/gateway/health>) — `/healthz` 和 `/readyz` 探針
  * [記錄](</zh-TW/logging>) — 以檔案為基礎的記錄
  * [OpenTelemetry 匯出](</zh-TW/gateway/opentelemetry>) — 用於追蹤資料、指標和日誌的 OTLP 推送


Was this useful?YesNo