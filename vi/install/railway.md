---
title: Railway
source_url: https://docs.openclaw.ai/vi/install/railway
scraped_at: 2026-05-25
---

# Railway

Triển khai OpenClaw trên Railway bằng mẫu một cú nhấp và truy cập qua giao diện điều khiển trên web. Đây là cách dễ nhất "không cần terminal trên máy chủ": Railway chạy Gateway cho bạn.

## Danh sách kiểm tra nhanh (người dùng mới)

  1. Nhấp **Triển khai trên Railway** (bên dưới).
  2. Thêm một **Volume** được gắn tại `/data`.
  3. Đặt các **Biến** bắt buộc (ít nhất là `OPENCLAW_GATEWAY_PORT` và `OPENCLAW_GATEWAY_TOKEN`).
  4. Bật **HTTP Proxy** trên cổng `8080`.
  5. Mở `https://<your-railway-domain>/openclaw` và kết nối bằng bí mật dùng chung đã cấu hình. Mẫu này mặc định dùng `OPENCLAW_GATEWAY_TOKEN`; nếu bạn thay bằng xác thực mật khẩu, hãy dùng mật khẩu đó thay thế.


## Triển khai một cú nhấp

[ Triển khai trên Railway ](<https://railway.com/deploy/clawdbot-railway-template>)

Sau khi triển khai, tìm URL công khai của bạn trong **Railway → dịch vụ của bạn → Settings → Domains**.

Railway sẽ:

  * cấp cho bạn một miền được tạo sẵn (thường là `https://<something>.up.railway.app`), hoặc
  * dùng miền tùy chỉnh của bạn nếu bạn đã gắn một miền.


Sau đó mở:

  * `https://<your-railway-domain>/openclaw` — Giao diện điều khiển


## Bạn nhận được gì

  * OpenClaw Gateway + giao diện điều khiển được lưu trữ
  * Lưu trữ bền vững qua Railway Volume (`/data`) để `openclaw.json`, `auth-profiles.json` theo từng tác tử, trạng thái kênh/nhà cung cấp, phiên và workspace vẫn tồn tại sau các lần triển khai lại


## Cài đặt Railway bắt buộc

### Mạng công khai

Bật **HTTP Proxy** cho dịch vụ.

  * Cổng: `8080`


### Volume (bắt buộc)

Gắn một volume tại:

  * `/data`


### Biến

Đặt các biến này trên dịch vụ:

  * `OPENCLAW_GATEWAY_PORT=8080` (bắt buộc — phải khớp với cổng trong Mạng công khai)
  * `OPENCLAW_GATEWAY_TOKEN` (bắt buộc; coi như bí mật quản trị)
  * `OPENCLAW_STATE_DIR=/data/.openclaw` (khuyến nghị)
  * `OPENCLAW_WORKSPACE_DIR=/data/workspace` (khuyến nghị)


## Kết nối một kênh

Dùng giao diện điều khiển tại `/openclaw` hoặc chạy `openclaw onboard` qua shell của Railway để xem hướng dẫn thiết lập kênh:

  * [Telegram](</vi/channels/telegram>) (nhanh nhất — chỉ cần token bot)
  * [Discord](</vi/channels/discord>)
  * [Tất cả kênh](</vi/channels>)


## Sao lưu & di chuyển

Xuất trạng thái, cấu hình, hồ sơ xác thực và workspace của bạn:

bashCopy code
[code]
    openclaw backup create
[/code]

Lệnh này tạo một kho lưu trữ sao lưu có thể mang đi, gồm trạng thái OpenClaw cùng mọi workspace đã cấu hình. Xem [Sao lưu](</vi/cli/backup>) để biết chi tiết.

## Bước tiếp theo

  * Thiết lập các kênh nhắn tin: [Kênh](</vi/channels>)
  * Cấu hình Gateway: [Cấu hình Gateway](</vi/gateway/configuration>)
  * Luôn cập nhật OpenClaw: [Cập nhật](</vi/install/updating>)


Was this useful?YesNo