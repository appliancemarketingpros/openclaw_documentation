---
title: Northflank
source_url: https://docs.openclaw.ai/vi/install/northflank
scraped_at: 2026-05-25
---

# Northflank

Triển khai OpenClaw trên Northflank bằng mẫu một cú nhấp và truy cập thông qua Control UI trên web. Đây là lộ trình "không cần terminal trên máy chủ" dễ nhất: Northflank chạy Gateway cho bạn.

## Cách bắt đầu

  1. Nhấp vào [Triển khai OpenClaw](<https://northflank.com/stacks/deploy-openclaw>) để mở mẫu.
  2. Tạo [tài khoản trên Northflank](<https://app.northflank.com/signup>) nếu bạn chưa có.
  3. Nhấp vào **Triển khai OpenClaw ngay**.
  4. Đặt biến môi trường bắt buộc: `OPENCLAW_GATEWAY_TOKEN` (dùng một giá trị ngẫu nhiên mạnh).
  5. Nhấp vào **Triển khai ngăn xếp** để build và chạy mẫu OpenClaw.
  6. Chờ quá trình triển khai hoàn tất, sau đó nhấp vào **Xem tài nguyên**.
  7. Mở dịch vụ OpenClaw.
  8. Mở URL OpenClaw công khai tại `/openclaw` và kết nối bằng bí mật dùng chung đã cấu hình. Mẫu này dùng `OPENCLAW_GATEWAY_TOKEN` theo mặc định; nếu bạn thay thế bằng xác thực mật khẩu, hãy dùng mật khẩu đó thay thế.


## Bạn nhận được gì

  * OpenClaw Gateway + Control UI được lưu trữ
  * Lưu trữ bền vững thông qua Northflank Volume (`/data`) để `openclaw.json`, `auth-profiles.json` theo từng agent, trạng thái kênh/nhà cung cấp, phiên và workspace vẫn tồn tại sau các lần triển khai lại


## Kết nối một kênh

Dùng Control UI tại `/openclaw` hoặc chạy `openclaw onboard` qua SSH để xem hướng dẫn thiết lập kênh:

  * [Telegram](</vi/channels/telegram>) (nhanh nhất — chỉ cần token bot)
  * [Discord](</vi/channels/discord>)
  * [Tất cả kênh](</vi/channels>)


## Bước tiếp theo

  * Thiết lập các kênh nhắn tin: [Kênh](</vi/channels>)
  * Cấu hình Gateway: [Cấu hình Gateway](</vi/gateway/configuration>)
  * Luôn cập nhật OpenClaw: [Cập nhật](</vi/install/updating>)


Was this useful?YesNo