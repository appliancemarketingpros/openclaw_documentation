---
title: Bảng điều khiển
source_url: https://docs.openclaw.ai/vi/cli/dashboard
scraped_at: 2026-05-25
---

# `openclaw dashboard`

Mở giao diện điều khiển bằng xác thực hiện tại của bạn.

bashCopy code
[code]
    openclaw dashboardopenclaw dashboard --no-open
[/code]

Ghi chú:

  * `dashboard` phân giải các SecretRefs `gateway.auth.token` đã cấu hình khi có thể.
  * `dashboard` tuân theo `gateway.tls.enabled`: các gateway đã bật TLS sẽ in/mở URL giao diện điều khiển dạng `https://` và kết nối qua `wss://`.
  * Nếu việc gửi URL dashboard đã xác thực bằng mã thông báo qua clipboard/trình duyệt thất bại, `dashboard` ghi nhật ký một gợi ý xác thực thủ công an toàn, nêu tên `OPENCLAW_GATEWAY_TOKEN`, `gateway.auth.token`, và khóa fragment `token` mà không in giá trị mã thông báo.
  * Đối với các mã thông báo do SecretRef quản lý (đã phân giải hoặc chưa phân giải), `dashboard` in/sao chép/mở một URL không chứa mã thông báo để tránh làm lộ bí mật bên ngoài trong đầu ra terminal, lịch sử clipboard hoặc đối số khởi chạy trình duyệt.
  * Nếu `gateway.auth.token` do SecretRef quản lý nhưng chưa được phân giải trong đường dẫn lệnh này, lệnh sẽ in một URL không chứa mã thông báo và hướng dẫn khắc phục rõ ràng thay vì nhúng một placeholder mã thông báo không hợp lệ.


## Liên quan

  * [Tham chiếu CLI](</vi/cli>)
  * [Dashboard](</vi/web/dashboard>)


Was this useful?YesNo