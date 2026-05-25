---
title: Máy chủ proxy
source_url: https://docs.openclaw.ai/vi/cli/proxy
scraped_at: 2026-05-25
---

# `openclaw proxy`

Xác thực định tuyến proxy do người vận hành quản lý, hoặc chạy proxy gỡ lỗi tường minh cục bộ và kiểm tra lưu lượng đã ghi lại.

Dùng `validate` để kiểm tra sơ bộ proxy chuyển tiếp do người vận hành quản lý trước khi bật định tuyến proxy của OpenClaw. Các lệnh khác là công cụ gỡ lỗi để điều tra ở cấp truyền tải: chúng có thể khởi động proxy cục bộ, chạy lệnh con khi đã bật ghi lại, liệt kê các phiên ghi lại, truy vấn các mẫu lưu lượng phổ biến, đọc các blob đã ghi lại, và xóa sạch dữ liệu ghi lại cục bộ.

## Lệnh

bashCopy code
[code]
    openclaw proxy start [--host <host>] [--port <port>]openclaw proxy run [--host <host>] [--port <port>] -- <cmd...>openclaw proxy validate [--json] [--proxy-url <url>] [--allowed-url <url>] [--denied-url <url>] [--apns-reachable] [--apns-authority <url>] [--timeout-ms <ms>]openclaw proxy coverageopenclaw proxy sessions [--limit <count>]openclaw proxy query --preset <name> [--session <id>]openclaw proxy blob --id <blobId>openclaw proxy purge
[/code]

## Xác thực

`openclaw proxy validate` kiểm tra URL proxy do người vận hành quản lý có hiệu lực từ `--proxy-url`, cấu hình, hoặc `OPENCLAW_PROXY_URL`. Lệnh này báo cáo sự cố cấu hình khi không có proxy nào được bật và cấu hình; dùng `--proxy-url` để kiểm tra sơ bộ một lần trước khi thay đổi cấu hình. Theo mặc định, lệnh xác minh rằng một đích công khai thành công qua proxy và proxy không thể truy cập một canary loopback tạm thời. Các đích bị từ chối tùy chỉnh dùng cơ chế đóng khi lỗi: phản hồi HTTP và lỗi truyền tải mơ hồ đều thất bại trừ khi bạn có thể xác minh riêng một tín hiệu từ chối theo từng triển khai. Thêm `--apns-reachable` để cũng mở một đường hầm CONNECT HTTP/2 của APNs qua proxy và xác nhận APNs sandbox phản hồi; phép thăm dò dùng một provider token cố ý không hợp lệ, vì vậy phản hồi APNs `403 InvalidProviderToken` là tín hiệu khả năng truy cập thành công.

Tùy chọn:

  * `--json`: in JSON đọc được bởi máy.
  * `--proxy-url <url>`: xác thực URL proxy này thay vì cấu hình hoặc env.
  * `--allowed-url <url>`: thêm một đích được kỳ vọng sẽ thành công qua proxy. Lặp lại để kiểm tra nhiều đích.
  * `--denied-url <url>`: thêm một đích được kỳ vọng sẽ bị proxy chặn. Lặp lại để kiểm tra nhiều đích.
  * `--apns-reachable`: cũng xác minh HTTP/2 APNs sandbox có thể truy cập được qua proxy.
  * `--apns-authority <url>`: authority APNs để thăm dò với `--apns-reachable` (mặc định là `https://api.sandbox.push.apple.com`; production là `https://api.push.apple.com`).
  * `--timeout-ms <ms>`: thời gian chờ cho mỗi yêu cầu tính bằng mili giây.


Xem [Proxy mạng](</vi/security/network-proxy>) để biết hướng dẫn triển khai và ngữ nghĩa từ chối.

## Các preset truy vấn

`openclaw proxy query --preset <name>` chấp nhận:

  * `double-sends`
  * `retry-storms`
  * `cache-busting`
  * `ws-duplicate-frames`
  * `missing-ack`
  * `error-bursts`


## Ghi chú

  * `start` mặc định là `127.0.0.1` trừ khi đặt `--host`.
  * `run` khởi động một proxy gỡ lỗi cục bộ rồi chạy lệnh sau `--`.
  * Cơ chế chuyển tiếp upstream trực tiếp của proxy gỡ lỗi mở các socket upstream để chẩn đoán. Khi chế độ proxy do OpenClaw quản lý đang hoạt động, chuyển tiếp trực tiếp cho các yêu cầu proxy và đường hầm CONNECT bị tắt theo mặc định; chỉ đặt `OPENCLAW_DEBUG_PROXY_ALLOW_DIRECT_CONNECT_WITH_MANAGED_PROXY=1` cho chẩn đoán cục bộ đã được phê duyệt.
  * `validate` thoát với mã 1 khi cấu hình proxy hoặc kiểm tra đích thất bại.
  * Các bản ghi lại là dữ liệu gỡ lỗi cục bộ; dùng `openclaw proxy purge` khi hoàn tất.


## Liên quan

  * [Tham chiếu CLI](</vi/cli>)
  * [Proxy mạng](</vi/security/network-proxy>)
  * [Xác thực proxy tin cậy](</vi/gateway/trusted-proxy-auth>)


Was this useful?YesNo