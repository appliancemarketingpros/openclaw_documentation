---
title: Prometheus metrikleri
source_url: https://docs.openclaw.ai/tr/gateway/prometheus
scraped_at: 2026-05-25
---

OpenClaw, tanılama metriklerini resmi `diagnostics-prometheus` Plugin'i aracılığıyla sunabilir. Güvenilen dahili tanılamaları dinler ve şu adreste Prometheus metin uç noktası oluşturur:

textCopy code
[code]
    GET /api/diagnostics/prometheus
[/code]

İçerik türü, standart Prometheus sunum biçimi olan `text/plain; version=0.0.4; charset=utf-8` değeridir.

İzler, günlükler, OTLP push ve OpenTelemetry GenAI anlamsal öznitelikleri için bkz. [OpenTelemetry dışa aktarma](</tr/gateway/opentelemetry>).

## Hızlı başlangıç

* ### Plugin'i yükleyin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/diagnostics-prometheus
[/code]

* ### Plugin'i etkinleştirin

### Yapılandırma

json5Copy code
[code]
    {  plugins: {    allow: ["diagnostics-prometheus"],    entries: {      "diagnostics-prometheus": { enabled: true },    },  },  diagnostics: {    enabled: true,  },}
[/code]

### CLI

bashCopy code
[code]
    openclaw plugins enable diagnostics-prometheus
[/code]

* ### Gateway'i yeniden başlatın

HTTP rotası Plugin başlatılırken kaydedilir, bu nedenle etkinleştirdikten sonra yeniden yükleyin.

* ### Korumalı rotayı kazıyın

Operatör istemcilerinizin kullandığı aynı gateway kimlik doğrulamasını gönderin:

bashCopy code
[code]
    curl -H "Authorization: Bearer $OPENCLAW_GATEWAY_TOKEN" \  http://127.0.0.1:18789/api/diagnostics/prometheus
[/code]

* ### Prometheus'u bağlayın

yamlCopy code
[code]
    # prometheus.ymlscrape_configs:  - job_name: openclaw    scrape_interval: 30s    metrics_path: /api/diagnostics/prometheus    authorization:      credentials_file: /etc/prometheus/openclaw-gateway-token    static_configs:      - targets: ["openclaw-gateway:18789"]
[/code]

## Dışa aktarılan metrikler

Metrik | Tür | Etiketler  
---|---|---  
`openclaw_run_completed_total` | sayaç | `channel`, `model`, `outcome`, `provider`, `trigger`  
`openclaw_run_duration_seconds` | histogram | `channel`, `model`, `outcome`, `provider`, `trigger`  
`openclaw_model_call_total` | sayaç | `api`, `error_category`, `model`, `outcome`, `provider`, `transport`  
`openclaw_model_call_duration_seconds` | histogram | `api`, `error_category`, `model`, `outcome`, `provider`, `transport`  
`openclaw_model_tokens_total` | sayaç | `agent`, `channel`, `model`, `provider`, `token_type`  
`openclaw_gen_ai_client_token_usage` | histogram | `model`, `provider`, `token_type`  
`openclaw_model_cost_usd_total` | sayaç | `agent`, `channel`, `model`, `provider`  
`openclaw_tool_execution_total` | sayaç | `error_category`, `outcome`, `params_kind`, `tool`  
`openclaw_tool_execution_duration_seconds` | histogram | `error_category`, `outcome`, `params_kind`, `tool`  
`openclaw_harness_run_total` | sayaç | `channel`, `error_category`, `harness`, `model`, `outcome`, `phase`, `plugin`, `provider`  
`openclaw_harness_run_duration_seconds` | histogram | `channel`, `error_category`, `harness`, `model`, `outcome`, `phase`, `plugin`, `provider`  
`openclaw_message_processed_total` | sayaç | `channel`, `outcome`, `reason`  
`openclaw_message_processed_duration_seconds` | histogram | `channel`, `outcome`, `reason`  
`openclaw_message_delivery_started_total` | sayaç | `channel`, `delivery_kind`  
`openclaw_message_delivery_total` | sayaç | `channel`, `delivery_kind`, `error_category`, `outcome`  
`openclaw_message_delivery_duration_seconds` | histogram | `channel`, `delivery_kind`, `error_category`, `outcome`  
`openclaw_talk_event_total` | sayaç | `brain`, `event_type`, `mode`, `provider`, `transport`  
`openclaw_talk_event_duration_seconds` | histogram | `brain`, `event_type`, `mode`, `provider`, `transport`  
`openclaw_talk_audio_bytes` | histogram | `brain`, `event_type`, `mode`, `provider`, `transport`  
`openclaw_queue_lane_size` | gösterge | `lane`  
`openclaw_queue_lane_wait_seconds` | histogram | `lane`  
`openclaw_session_state_total` | sayaç | `reason`, `state`  
`openclaw_session_queue_depth` | gösterge | `state`  
`openclaw_session_recovery_total` | sayaç | `action`, `active_work_kind`, `state`, `status`  
`openclaw_session_recovery_age_seconds` | histogram | `action`, `active_work_kind`, `state`, `status`  
`openclaw_memory_bytes` | gösterge | `kind`  
`openclaw_memory_rss_bytes` | histogram | yok  
`openclaw_memory_pressure_total` | sayaç | `level`, `reason`  
`openclaw_telemetry_exporter_total` | sayaç | `exporter`, `reason`, `signal`, `status`  
`openclaw_prometheus_series_dropped_total` | sayaç | yok  
  
## Etiket politikası

Sınırlı, düşük kardinaliteli etiketler

Prometheus etiketleri sınırlı ve düşük kardinaliteli kalır. Dışa aktarıcı `runId`, `sessionKey`, `sessionId`, `callId`, `toolCallId`, ileti kimlikleri, sohbet kimlikleri veya sağlayıcı istek kimlikleri gibi ham tanılama tanımlayıcıları yaymaz.

Etiket değerleri redakte edilir ve OpenClaw'ın düşük kardinaliteli karakter politikasıyla eşleşmelidir. Politikayı geçemeyen değerler, metriğe bağlı olarak `unknown`, `other` veya `none` ile değiştirilir.

Seri sınırı ve taşma muhasebesi

Dışa aktarıcı, bellekte tutulan zaman serilerini sayaçlar, göstergeler ve histogramlar genelinde toplam **2048** seriyle sınırlar. Bu sınırın ötesindeki yeni seriler atılır ve her seferinde `openclaw_prometheus_series_dropped_total` bir artırılır.

Bu sayacı, yukarı akıştaki bir özniteliğin yüksek kardinaliteli değerler sızdırdığına dair kesin bir sinyal olarak izleyin. Dışa aktarıcı sınırı hiçbir zaman otomatik olarak yükseltmez; değer artıyorsa sınırı devre dışı bırakmak yerine kaynağı düzeltin.

Prometheus çıktısında hiçbir zaman görünmeyenler

  * istem metni, yanıt metni, araç girdileri, araç çıktıları, sistem istemleri
  * Konuşma dökümleri, ses yükleri, çağrı kimlikleri, oda kimlikleri, devir tokenları, tur kimlikleri ve ham oturum kimlikleri
  * ham sağlayıcı istek kimlikleri (yalnızca uygun olduğunda span’lerde sınırlı karmalar; metriklerde asla)
  * oturum anahtarları ve oturum kimlikleri
  * ana makine adları, dosya yolları, gizli değerler


## PromQL tarifleri

promqlCopy code
[code]
    # Tokens per minute, split by providersum by (provider) (rate(openclaw_model_tokens_total[1m])) # Spend (USD) over the last hour, by modelsum by (model) (increase(openclaw_model_cost_usd_total[1h])) # 95th percentile model run durationhistogram_quantile(  0.95,  sum by (le, provider, model)    (rate(openclaw_run_duration_seconds_bucket[5m]))) # Queue wait time SLO (95p under 2s)histogram_quantile(  0.95,  sum by (le, lane) (rate(openclaw_queue_lane_wait_seconds_bucket[5m]))) < 2 # Dropped Prometheus series (cardinality alarm)increase(openclaw_prometheus_series_dropped_total[15m]) > 0
[/code]

## Prometheus ve OpenTelemetry dışa aktarımı arasında seçim yapma

OpenClaw her iki yüzeyi de bağımsız olarak destekler. Birini, ikisini veya hiçbirini çalıştırabilirsiniz.

### diagnostics-prometheus

  * **Pull** modeli: Prometheus `/api/diagnostics/prometheus` adresini kazır.
  * Harici collector gerekmez.
  * Normal Gateway kimlik doğrulaması üzerinden kimliği doğrulanır.
  * Yüzey yalnızca metriklerden oluşur (iz veya günlük yoktur).
  * Prometheus + Grafana üzerinde zaten standartlaşmış yığınlar için en iyisidir.


### diagnostics-otel

  * **Push** modeli: OpenClaw OTLP/HTTP’yi bir collector’a veya OTLP uyumlu arka uca gönderir.
  * Yüzey metrikleri, izleri ve günlükleri içerir.
  * İkisine de ihtiyacınız olduğunda bir OpenTelemetry Collector (`prometheus` veya `prometheusremotewrite` dışa aktarıcısı) üzerinden Prometheus’a köprü kurar.
  * Tam katalog için [OpenTelemetry dışa aktarımı](</tr/gateway/opentelemetry>) bölümüne bakın.


## Sorun giderme

Boş yanıt gövdesi

  * Yapılandırmada `diagnostics.enabled: true` olup olmadığını kontrol edin.
  * Plugin’in etkinleştirildiğini ve `openclaw plugins list --enabled` ile yüklendiğini doğrulayın.
  * Biraz trafik oluşturun; sayaçlar ve histogramlar yalnızca en az bir olaydan sonra satır yayar.

401 / yetkisiz

Uç nokta Gateway operatör kapsamını gerektirir (`auth: "gateway"` ve `gatewayRuntimeScopeSurface: "trusted-operator"`). Prometheus’un diğer Gateway operatör rotaları için kullandığı aynı tokenı veya parolayı kullanın. Genel, kimliği doğrulanmamış bir mod yoktur.

`openclaw_prometheus_series_dropped_total` artıyor

Yeni bir öznitelik **2048** seri sınırını aşıyor. Beklenmedik derecede yüksek kardinaliteli bir etiket için son metrikleri inceleyin ve sorunu kaynağında düzeltin. Dışa aktarıcı, etiketleri sessizce yeniden yazmak yerine yeni serileri kasıtlı olarak atar.

Prometheus yeniden başlatmadan sonra eski serileri gösteriyor

Plugin durumu yalnızca bellekte tutar. Gateway yeniden başlatıldıktan sonra sayaçlar sıfırlanır ve göstergeler bir sonraki bildirilen değerlerinde yeniden başlar. Sıfırlamaları temiz şekilde ele almak için PromQL `rate()` ve `increase()` kullanın.

## İlgili

  * [Tanılama dışa aktarımı](</tr/gateway/diagnostics>) — destek paketleri için yerel tanılama ZIP dosyası
  * [Sağlık ve hazır olma](</tr/gateway/health>) — `/healthz` ve `/readyz` yoklamaları
  * [Günlük kaydı](</tr/logging>) — dosya tabanlı günlük kaydı
  * [OpenTelemetry dışa aktarımı](</tr/gateway/opentelemetry>) — izler, metrikler ve günlükler için OTLP gönderimi


Was this useful?YesNo