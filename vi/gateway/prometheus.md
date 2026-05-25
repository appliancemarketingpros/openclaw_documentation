---
title: Chỉ số Prometheus
source_url: https://docs.openclaw.ai/vi/gateway/prometheus
scraped_at: 2026-05-25
---

OpenClaw có thể công bố số liệu chẩn đoán thông qua Plugin `diagnostics-prometheus` chính thức. Plugin này lắng nghe chẩn đoán nội bộ đáng tin cậy và hiển thị một điểm cuối văn bản Prometheus tại:

textCopy code
[code]
    GET /api/diagnostics/prometheus
[/code]

Loại nội dung là `text/plain; version=0.0.4; charset=utf-8`, định dạng trình bày tiêu chuẩn của Prometheus.

Đối với dấu vết, nhật ký, đẩy OTLP và thuộc tính ngữ nghĩa OpenTelemetry GenAI, xem [xuất OpenTelemetry](</vi/gateway/opentelemetry>).

## Bắt đầu nhanh

* ### Cài đặt Plugin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/diagnostics-prometheus
[/code]

* ### Bật Plugin

### Cấu hình

json5Copy code
[code]
    {  plugins: {    allow: ["diagnostics-prometheus"],    entries: {      "diagnostics-prometheus": { enabled: true },    },  },  diagnostics: {    enabled: true,  },}
[/code]

### CLI

bashCopy code
[code]
    openclaw plugins enable diagnostics-prometheus
[/code]

* ### Khởi động lại Gateway

Tuyến HTTP được đăng ký khi Plugin khởi động, vì vậy hãy tải lại sau khi bật.

* ### Thu thập dữ liệu từ tuyến được bảo vệ

Gửi cùng thông tin xác thực Gateway mà các máy khách người vận hành của bạn dùng:

bashCopy code
[code]
    curl -H "Authorization: Bearer $OPENCLAW_GATEWAY_TOKEN" \  http://127.0.0.1:18789/api/diagnostics/prometheus
[/code]

* ### Kết nối Prometheus

yamlCopy code
[code]
    # prometheus.ymlscrape_configs:  - job_name: openclaw    scrape_interval: 30s    metrics_path: /api/diagnostics/prometheus    authorization:      credentials_file: /etc/prometheus/openclaw-gateway-token    static_configs:      - targets: ["openclaw-gateway:18789"]
[/code]

## Số liệu được xuất

Số liệu | Loại | Nhãn  
---|---|---  
`openclaw_run_completed_total` | bộ đếm | `channel`, `model`, `outcome`, `provider`, `trigger`  
`openclaw_run_duration_seconds` | biểu đồ | `channel`, `model`, `outcome`, `provider`, `trigger`  
`openclaw_model_call_total` | bộ đếm | `api`, `error_category`, `model`, `outcome`, `provider`, `transport`  
`openclaw_model_call_duration_seconds` | biểu đồ | `api`, `error_category`, `model`, `outcome`, `provider`, `transport`  
`openclaw_model_tokens_total` | bộ đếm | `agent`, `channel`, `model`, `provider`, `token_type`  
`openclaw_gen_ai_client_token_usage` | biểu đồ | `model`, `provider`, `token_type`  
`openclaw_model_cost_usd_total` | bộ đếm | `agent`, `channel`, `model`, `provider`  
`openclaw_tool_execution_total` | bộ đếm | `error_category`, `outcome`, `params_kind`, `tool`  
`openclaw_tool_execution_duration_seconds` | biểu đồ | `error_category`, `outcome`, `params_kind`, `tool`  
`openclaw_harness_run_total` | bộ đếm | `channel`, `error_category`, `harness`, `model`, `outcome`, `phase`, `plugin`, `provider`  
`openclaw_harness_run_duration_seconds` | biểu đồ | `channel`, `error_category`, `harness`, `model`, `outcome`, `phase`, `plugin`, `provider`  
`openclaw_message_processed_total` | bộ đếm | `channel`, `outcome`, `reason`  
`openclaw_message_processed_duration_seconds` | biểu đồ | `channel`, `outcome`, `reason`  
`openclaw_message_delivery_started_total` | bộ đếm | `channel`, `delivery_kind`  
`openclaw_message_delivery_total` | bộ đếm | `channel`, `delivery_kind`, `error_category`, `outcome`  
`openclaw_message_delivery_duration_seconds` | biểu đồ | `channel`, `delivery_kind`, `error_category`, `outcome`  
`openclaw_talk_event_total` | bộ đếm | `brain`, `event_type`, `mode`, `provider`, `transport`  
`openclaw_talk_event_duration_seconds` | biểu đồ | `brain`, `event_type`, `mode`, `provider`, `transport`  
`openclaw_talk_audio_bytes` | biểu đồ | `brain`, `event_type`, `mode`, `provider`, `transport`  
`openclaw_queue_lane_size` | thước đo | `lane`  
`openclaw_queue_lane_wait_seconds` | biểu đồ | `lane`  
`openclaw_session_state_total` | bộ đếm | `reason`, `state`  
`openclaw_session_queue_depth` | thước đo | `state`  
`openclaw_session_recovery_total` | bộ đếm | `action`, `active_work_kind`, `state`, `status`  
`openclaw_session_recovery_age_seconds` | biểu đồ | `action`, `active_work_kind`, `state`, `status`  
`openclaw_memory_bytes` | thước đo | `kind`  
`openclaw_memory_rss_bytes` | biểu đồ | không có  
`openclaw_memory_pressure_total` | bộ đếm | `level`, `reason`  
`openclaw_telemetry_exporter_total` | bộ đếm | `exporter`, `reason`, `signal`, `status`  
`openclaw_prometheus_series_dropped_total` | bộ đếm | không có  
  
## Chính sách nhãn

Nhãn có giới hạn, số lượng giá trị thấp

Nhãn Prometheus luôn có giới hạn và số lượng giá trị thấp. Trình xuất không phát ra các định danh chẩn đoán thô như `runId`, `sessionKey`, `sessionId`, `callId`, `toolCallId`, ID tin nhắn, ID trò chuyện hoặc ID yêu cầu của nhà cung cấp.

Giá trị nhãn được biên tập lại và phải khớp với chính sách ký tự có số lượng giá trị thấp của OpenClaw. Các giá trị không đáp ứng chính sách sẽ được thay bằng `unknown`, `other` hoặc `none`, tùy theo số liệu.

Giới hạn chuỗi và ghi nhận phần tràn

Trình xuất giới hạn số chuỗi thời gian được giữ trong bộ nhớ ở mức **2048** chuỗi, tính gộp cho counter, gauge và histogram. Các chuỗi mới vượt quá giới hạn đó sẽ bị loại bỏ, và `openclaw_prometheus_series_dropped_total` tăng thêm một mỗi lần.

Theo dõi counter này như một tín hiệu rõ ràng rằng một thuộc tính ở thượng nguồn đang rò rỉ các giá trị có độ đa dạng cao. Trình xuất không bao giờ tự động nâng giới hạn; nếu chỉ số này tăng, hãy sửa nguồn thay vì tắt giới hạn.

Những gì không bao giờ xuất hiện trong đầu ra Prometheus

  * văn bản prompt, văn bản phản hồi, đầu vào công cụ, đầu ra công cụ, system prompt
  * Bản ghi cuộc trò chuyện Talk, tải trọng âm thanh, ID cuộc gọi, ID phòng, token chuyển giao, ID lượt và ID phiên thô
  * ID yêu cầu nhà cung cấp thô (chỉ dùng hash có giới hạn, khi áp dụng, trên span — không bao giờ trên metric)
  * khóa phiên và ID phiên
  * hostname, đường dẫn tệp, giá trị bí mật


## Công thức PromQL

promqlCopy code
[code]
    # Tokens per minute, split by providersum by (provider) (rate(openclaw_model_tokens_total[1m])) # Spend (USD) over the last hour, by modelsum by (model) (increase(openclaw_model_cost_usd_total[1h])) # 95th percentile model run durationhistogram_quantile(  0.95,  sum by (le, provider, model)    (rate(openclaw_run_duration_seconds_bucket[5m]))) # Queue wait time SLO (95p under 2s)histogram_quantile(  0.95,  sum by (le, lane) (rate(openclaw_queue_lane_wait_seconds_bucket[5m]))) < 2 # Dropped Prometheus series (cardinality alarm)increase(openclaw_prometheus_series_dropped_total[15m]) > 0
[/code]

## Chọn giữa xuất Prometheus và OpenTelemetry

OpenClaw hỗ trợ độc lập cả hai bề mặt này. Bạn có thể chạy một trong hai, cả hai hoặc không chạy cái nào.

### diagnostics-prometheus

  * Mô hình **kéo** : Prometheus scrape `/api/diagnostics/prometheus`.
  * Không cần collector bên ngoài.
  * Được xác thực qua cơ chế xác thực Gateway thông thường.
  * Bề mặt chỉ có metric (không có trace hoặc log).
  * Phù hợp nhất với các stack đã chuẩn hóa trên Prometheus + Grafana.


### diagnostics-otel

  * Mô hình **đẩy** : OpenClaw gửi OTLP/HTTP tới collector hoặc backend tương thích OTLP.
  * Bề mặt bao gồm metric, trace và log.
  * Kết nối sang Prometheus thông qua OpenTelemetry Collector (trình xuất `prometheus` hoặc `prometheusremotewrite`) khi bạn cần cả hai.
  * Xem [Xuất OpenTelemetry](</vi/gateway/opentelemetry>) để biết danh mục đầy đủ.


## Khắc phục sự cố

Nội dung phản hồi trống

  * Kiểm tra `diagnostics.enabled: true` trong cấu hình.
  * Xác nhận Plugin đã được bật và tải bằng `openclaw plugins list --enabled`.
  * Tạo một ít lưu lượng; counter và histogram chỉ phát ra dòng sau khi có ít nhất một sự kiện.

401 / không được ủy quyền

Endpoint yêu cầu phạm vi điều hành Gateway (`auth: "gateway"` với `gatewayRuntimeScopeSurface: "trusted-operator"`). Dùng cùng token hoặc mật khẩu mà Prometheus dùng cho mọi route điều hành Gateway khác. Không có chế độ công khai không xác thực.

`openclaw_prometheus_series_dropped_total` đang tăng

Một thuộc tính mới đang vượt quá giới hạn **2048** chuỗi. Kiểm tra các metric gần đây để tìm một nhãn có độ đa dạng cao bất thường và sửa tại nguồn. Trình xuất cố ý loại bỏ các chuỗi mới thay vì âm thầm viết lại nhãn.

Prometheus hiển thị chuỗi cũ sau khi khởi động lại

Plugin chỉ giữ trạng thái trong bộ nhớ. Sau khi Gateway khởi động lại, counter đặt lại về 0 và gauge bắt đầu lại ở giá trị được báo cáo tiếp theo. Dùng PromQL `rate()` và `increase()` để xử lý các lần đặt lại một cách gọn gàng.

## Liên quan

  * [Xuất chẩn đoán](</vi/gateway/diagnostics>) — tệp zip chẩn đoán cục bộ cho các gói hỗ trợ
  * [Tình trạng và mức sẵn sàng](</vi/gateway/health>) — các đầu dò `/healthz` và `/readyz`
  * [Ghi nhật ký](</vi/logging>) — ghi nhật ký dựa trên tệp
  * [Xuất OpenTelemetry](</vi/gateway/opentelemetry>) — đẩy OTLP cho dấu vết, số liệu và nhật ký


Was this useful?YesNo