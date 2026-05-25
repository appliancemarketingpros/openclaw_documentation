---
title: QR
source_url: https://docs.openclaw.ai/vi/cli/qr
scraped_at: 2026-05-25
---

# `openclaw qr`

Tạo mã QR ghép đôi thiết bị di động và mã thiết lập từ cấu hình Gateway hiện tại của bạn.

## Cách sử dụng

bashCopy code
[code]
    openclaw qropenclaw qr --setup-code-onlyopenclaw qr --jsonopenclaw qr --remoteopenclaw qr --url wss://gateway.example/ws
[/code]

## Tùy chọn

  * `--remote`: ưu tiên `gateway.remote.url`; nếu chưa đặt, `gateway.tailscale.mode=serve|funnel` vẫn có thể cung cấp URL công khai từ xa
  * `--url <url>`: ghi đè URL Gateway dùng trong payload
  * `--public-url <url>`: ghi đè URL công khai dùng trong payload
  * `--token <token>`: ghi đè token Gateway mà luồng bootstrap dùng để xác thực
  * `--password <password>`: ghi đè mật khẩu Gateway mà luồng bootstrap dùng để xác thực
  * `--setup-code-only`: chỉ in mã thiết lập
  * `--no-ascii`: bỏ qua việc hiển thị QR ASCII
  * `--json`: xuất JSON (`setupCode`, `gatewayUrl`, `auth`, `urlSource`)


## Ghi chú

  * `--token` và `--password` loại trừ lẫn nhau.
  * Bản thân mã thiết lập hiện mang một `bootstrapToken` mờ, ngắn hạn, không phải token/mật khẩu Gateway dùng chung.
  * Trong luồng bootstrap node/operator tích hợp, token node chính vẫn được lưu với `scopes: []`.
  * Nếu bàn giao bootstrap cũng cấp một token operator, token đó vẫn bị giới hạn trong danh sách cho phép bootstrap: `operator.approvals`, `operator.read`, `operator.talk.secrets`, `operator.write`.
  * Các kiểm tra phạm vi bootstrap có tiền tố vai trò. Danh sách cho phép operator đó chỉ đáp ứng các yêu cầu operator; các vai trò không phải operator vẫn cần phạm vi dưới tiền tố vai trò riêng của chúng.
  * Ghép đôi thiết bị di động sẽ đóng an toàn đối với URL Gateway `ws://` qua Tailscale/công khai. Địa chỉ LAN riêng và máy chủ Bonjour `.local` vẫn được hỗ trợ qua `ws://`, nhưng các tuyến di động Tailscale/công khai nên dùng Tailscale Serve/Funnel hoặc URL Gateway `wss://`.
  * Với `--remote`, OpenClaw yêu cầu `gateway.remote.url` hoặc `gateway.tailscale.mode=serve|funnel`.
  * Với `--remote`, nếu thông tin xác thực từ xa đang thực sự hoạt động được cấu hình dưới dạng SecretRefs và bạn không truyền `--token` hoặc `--password`, lệnh sẽ phân giải chúng từ snapshot Gateway đang hoạt động. Nếu Gateway không khả dụng, lệnh sẽ thất bại nhanh.
  * Không có `--remote`, SecretRefs xác thực Gateway cục bộ sẽ được phân giải khi không truyền ghi đè xác thực CLI: 
    * `gateway.auth.token` phân giải khi xác thực token có thể thắng (đặt rõ `gateway.auth.mode="token"` hoặc chế độ suy luận khi không có nguồn mật khẩu nào thắng).
    * `gateway.auth.password` phân giải khi xác thực mật khẩu có thể thắng (đặt rõ `gateway.auth.mode="password"` hoặc chế độ suy luận khi không có token thắng từ auth/env).
  * Nếu cả `gateway.auth.token` và `gateway.auth.password` đều được cấu hình (bao gồm SecretRefs) và `gateway.auth.mode` chưa được đặt, quá trình phân giải mã thiết lập sẽ thất bại cho đến khi chế độ được đặt rõ ràng.
  * Ghi chú về lệch phiên bản Gateway: đường dẫn lệnh này yêu cầu Gateway hỗ trợ `secrets.resolve`; các Gateway cũ hơn trả về lỗi phương thức không xác định.
  * Sau khi quét, phê duyệt ghép đôi thiết bị bằng: 
    * `openclaw devices list`
    * `openclaw devices approve <requestId>`


## Liên quan

  * [Tham chiếu CLI](</vi/cli>)
  * [Ghép đôi](</vi/cli/pairing>)


Was this useful?YesNo