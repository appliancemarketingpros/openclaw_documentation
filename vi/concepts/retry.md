---
title: Chính sách thử lại
source_url: https://docs.openclaw.ai/vi/concepts/retry
scraped_at: 2026-05-25
---

## Mục tiêu

  * Thử lại theo từng yêu cầu HTTP, không phải theo từng luồng nhiều bước.
  * Giữ nguyên thứ tự bằng cách chỉ thử lại bước hiện tại.
  * Tránh lặp lại các thao tác không có tính idempotent.


## Mặc định

  * Số lần thử: 3
  * Giới hạn độ trễ tối đa: 30000 ms
  * Jitter: 0.1 (10 phần trăm)
  * Mặc định của nhà cung cấp: 
    * Độ trễ tối thiểu của Telegram: 400 ms
    * Độ trễ tối thiểu của Discord: 500 ms


## Hành vi

### Nhà cung cấp mô hình

  * OpenClaw để SDK của nhà cung cấp xử lý các lần thử lại ngắn thông thường.
  * Với các SDK dựa trên Stainless như Anthropic và OpenAI, các phản hồi có thể thử lại (`408`, `409`, `429`, và `5xx`) có thể bao gồm `retry-after-ms` hoặc `retry-after`. Khi thời gian chờ đó dài hơn 60 giây, OpenClaw chèn `x-should-retry: false` để SDK trả lỗi ngay lập tức và chuyển đổi dự phòng mô hình có thể chuyển sang hồ sơ xác thực khác hoặc mô hình dự phòng.
  * Ghi đè giới hạn bằng `OPENCLAW_SDK_RETRY_MAX_WAIT_SECONDS=<seconds>`. Đặt thành `0`, `false`, `off`, `none`, hoặc `disabled` để SDK tự xử lý các lần ngủ `Retry-After` dài ở bên trong.


### Discord

  * Thử lại khi gặp lỗi giới hạn tốc độ (HTTP 429), hết thời gian chờ yêu cầu, phản hồi HTTP 5xx, và các lỗi truyền tải tạm thời như lỗi tra cứu DNS, đặt lại kết nối, đóng socket, và lỗi fetch.
  * Sử dụng `retry_after` của Discord khi có, nếu không thì dùng trì hoãn lùi theo cấp số nhân.


### Telegram

  * Thử lại khi gặp lỗi tạm thời (429, hết thời gian chờ, kết nối/đặt lại/đã đóng, tạm thời không khả dụng).
  * Sử dụng `retry_after` khi có, nếu không thì dùng trì hoãn lùi theo cấp số nhân.
  * Lỗi phân tích cú pháp Markdown không được thử lại; chúng chuyển về văn bản thuần.


## Cấu hình

Đặt chính sách thử lại theo từng nhà cung cấp trong `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  channels: {    telegram: {      retry: {        attempts: 3,        minDelayMs: 400,        maxDelayMs: 30000,        jitter: 0.1,      },    },    discord: {      retry: {        attempts: 3,        minDelayMs: 500,        maxDelayMs: 30000,        jitter: 0.1,      },    },  },}
[/code]

## Ghi chú

  * Thử lại áp dụng theo từng yêu cầu (gửi tin nhắn, tải lên phương tiện, phản ứng, bình chọn, sticker).
  * Các luồng tổng hợp không thử lại những bước đã hoàn tất.


## Liên quan

  * [Chuyển đổi dự phòng mô hình](</vi/concepts/model-failover>)
  * [Hàng đợi lệnh](</vi/concepts/queue>)


Was this useful?YesNo