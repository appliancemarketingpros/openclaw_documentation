---
title: Metrik Prometheus
source_url: https://docs.openclaw.ai/id/gateway/prometheus
scraped_at: 2026-05-25
---

OpenClaw dapat mengekspos metrik diagnostik melalui Plugin resmi `diagnostics-prometheus`. Plugin ini mendengarkan diagnostik internal tepercaya dan merender endpoint teks Prometheus di:

textCopy code
[code]
    GET /api/diagnostics/prometheus
[/code]

Tipe kontennya adalah `text/plain; version=0.0.4; charset=utf-8`, format eksposisi Prometheus standar.

Untuk trace, log, push OTLP, dan atribut semantik OpenTelemetry GenAI, lihat [Ekspor OpenTelemetry](</id/gateway/opentelemetry>).

## Mulai cepat

* ### Instal Plugin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/diagnostics-prometheus
[/code]

* ### Aktifkan Plugin

### Konfigurasi

json5Copy code
[code]
    {  plugins: {    allow: ["diagnostics-prometheus"],    entries: {      "diagnostics-prometheus": { enabled: true },    },  },  diagnostics: {    enabled: true,  },}
[/code]

### CLI

bashCopy code
[code]
    openclaw plugins enable diagnostics-prometheus
[/code]

* ### Mulai ulang Gateway

Rute HTTP didaftarkan saat Plugin dimulai, jadi muat ulang setelah mengaktifkannya.

* ### Scrape rute terlindungi

Kirim autentikasi gateway yang sama yang digunakan klien operator Anda:

bashCopy code
[code]
    curl -H "Authorization: Bearer $OPENCLAW_GATEWAY_TOKEN" \  http://127.0.0.1:18789/api/diagnostics/prometheus
[/code]

* ### Hubungkan Prometheus

yamlCopy code
[code]
    # prometheus.ymlscrape_configs:  - job_name: openclaw    scrape_interval: 30s    metrics_path: /api/diagnostics/prometheus    authorization:      credentials_file: /etc/prometheus/openclaw-gateway-token    static_configs:      - targets: ["openclaw-gateway:18789"]
[/code]

## Metrik yang diekspor

Metrik | Tipe | Label  
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
`openclaw_memory_rss_bytes` | histogram | tidak ada  
`openclaw_memory_pressure_total` | counter | `level`, `reason`  
`openclaw_telemetry_exporter_total` | counter | `exporter`, `reason`, `signal`, `status`  
`openclaw_prometheus_series_dropped_total` | counter | tidak ada  
  
## Kebijakan label

Label terbatas dengan kardinalitas rendah

Label Prometheus tetap terbatas dan berkardinalitas rendah. Eksportir tidak memancarkan pengenal diagnostik mentah seperti `runId`, `sessionKey`, `sessionId`, `callId`, `toolCallId`, ID pesan, ID chat, atau ID permintaan penyedia.

Nilai label disunting dan harus cocok dengan kebijakan karakter berkardinalitas rendah OpenClaw. Nilai yang gagal memenuhi kebijakan diganti dengan `unknown`, `other`, atau `none`, bergantung pada metrik.

Batas seri dan penghitungan luapan

Pengekspor membatasi deret waktu yang disimpan dalam memori hingga **2048** seri untuk gabungan penghitung, gauge, dan histogram. Seri baru di luar batas tersebut akan dibuang, dan `openclaw_prometheus_series_dropped_total` bertambah satu setiap kali.

Pantau penghitung ini sebagai sinyal kuat bahwa atribut di hulu membocorkan nilai berkardinalitas tinggi. Pengekspor tidak pernah menaikkan batas secara otomatis; jika nilainya naik, perbaiki sumbernya alih-alih menonaktifkan batas.

Yang tidak pernah muncul dalam keluaran Prometheus

  * teks prompt, teks respons, input alat, output alat, prompt sistem
  * Transkrip Talk, payload audio, id panggilan, id ruang, token handoff, id giliran, dan id sesi mentah
  * ID permintaan penyedia mentah (hanya hash terbatas, jika berlaku, pada span — tidak pernah pada metrik)
  * kunci sesi dan ID sesi
  * nama host, jalur file, nilai rahasia


## Resep PromQL

promqlCopy code
[code]
    # Tokens per minute, split by providersum by (provider) (rate(openclaw_model_tokens_total[1m])) # Spend (USD) over the last hour, by modelsum by (model) (increase(openclaw_model_cost_usd_total[1h])) # 95th percentile model run durationhistogram_quantile(  0.95,  sum by (le, provider, model)    (rate(openclaw_run_duration_seconds_bucket[5m]))) # Queue wait time SLO (95p under 2s)histogram_quantile(  0.95,  sum by (le, lane) (rate(openclaw_queue_lane_wait_seconds_bucket[5m]))) < 2 # Dropped Prometheus series (cardinality alarm)increase(openclaw_prometheus_series_dropped_total[15m]) > 0
[/code]

## Memilih antara ekspor Prometheus dan OpenTelemetry

OpenClaw mendukung kedua permukaan secara independen. Anda dapat menjalankan salah satu, keduanya, atau tidak keduanya.

### diagnostics-prometheus

  * Model **tarik** : Prometheus mengambil `/api/diagnostics/prometheus`.
  * Tidak memerlukan kolektor eksternal.
  * Diautentikasi melalui autentikasi Gateway normal.
  * Permukaan hanya berupa metrik (tanpa trace atau log).
  * Paling cocok untuk stack yang sudah distandarkan pada Prometheus + Grafana.


### diagnostics-otel

  * Model **dorong** : OpenClaw mengirim OTLP/HTTP ke kolektor atau backend yang kompatibel dengan OTLP.
  * Permukaan mencakup metrik, trace, dan log.
  * Menjembatani ke Prometheus melalui OpenTelemetry Collector (pengekspor `prometheus` atau `prometheusremotewrite`) saat Anda membutuhkan keduanya.
  * Lihat [ekspor OpenTelemetry](</id/gateway/opentelemetry>) untuk katalog lengkap.


## Pemecahan masalah

Isi respons kosong

  * Periksa `diagnostics.enabled: true` dalam konfigurasi.
  * Pastikan Plugin diaktifkan dan dimuat dengan `openclaw plugins list --enabled`.
  * Buat sejumlah traffic; penghitung dan histogram hanya memancarkan baris setelah setidaknya satu peristiwa.

401 / tidak terotorisasi

Endpoint memerlukan cakupan operator Gateway (`auth: "gateway"` dengan `gatewayRuntimeScopeSurface: "trusted-operator"`). Gunakan token atau kata sandi yang sama yang digunakan Prometheus untuk rute operator Gateway lainnya. Tidak ada mode publik tanpa autentikasi.

`openclaw_prometheus_series_dropped_total` meningkat

Atribut baru melebihi batas **2048** seri. Periksa metrik terbaru untuk label dengan kardinalitas tinggi yang tidak terduga dan perbaiki di sumbernya. Pengekspor sengaja membuang seri baru alih-alih diam-diam menulis ulang label.

Prometheus menampilkan seri basi setelah mulai ulang

Plugin hanya menyimpan status dalam memori. Setelah Gateway dimulai ulang, penghitung diatur ulang ke nol dan gauge dimulai ulang pada nilai berikutnya yang dilaporkan. Gunakan PromQL `rate()` dan `increase()` untuk menangani pengaturan ulang dengan bersih.

## Terkait

  * [Ekspor diagnostik](</id/gateway/diagnostics>) — berkas zip diagnostik lokal untuk bundel dukungan
  * [Kesehatan dan kesiapan](</id/gateway/health>) — probe `/healthz` dan `/readyz`
  * [Pencatatan log](</id/logging>) — pencatatan log berbasis file
  * [Ekspor OpenTelemetry](</id/gateway/opentelemetry>) — push OTLP untuk trace, metrik, dan log


Was this useful?YesNo