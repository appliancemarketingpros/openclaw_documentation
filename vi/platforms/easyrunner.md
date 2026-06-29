---
title: EasyRunner
source_url: https://docs.openclaw.ai/vi/platforms/easyrunner
scraped_at: 2026-06-29
---

PlatformsPlatforms overview

EasyRunner có thể lưu trữ OpenClaw Gateway như một ứng dụng nhỏ được đóng gói trong container phía sau proxy Caddy của nó. Hướng dẫn này giả định một máy chủ EasyRunner chạy các ứng dụng Compose tương thích với Podman và cung cấp HTTPS thông qua Caddy.

## Trước khi bắt đầu

  * Một máy chủ EasyRunner có domain được định tuyến tới đó.
  * Một image container OpenClaw đã build hoặc đã phát hành.
  * Một volume cấu hình bền vững cho `/home/node/.openclaw`.
  * Một volume workspace bền vững cho `/workspace`.
  * Một token hoặc mật khẩu Gateway mạnh.


Giữ xác thực thiết bị được bật khi có thể. Nếu triển khai reverse proxy của bạn không thể truyền chính xác danh tính thiết bị, hãy sửa thiết lập trusted-proxy trước; chỉ dùng các bypass xác thực nguy hiểm cho mạng hoàn toàn riêng tư và do operator kiểm soát.

## Ứng dụng Compose

Tạo một ứng dụng EasyRunner với tệp Compose có dạng như sau:

yamlCopy code
[code]
    services:  openclaw:    image: ghcr.io/openclaw/openclaw:latest    restart: unless-stopped    environment:      OPENCLAW_GATEWAY_TOKEN: ${OPENCLAW_GATEWAY_TOKEN}      OPENCLAW_HOME: /home/node      OPENCLAW_STATE_DIR: /home/node/.openclaw      OPENCLAW_CONFIG_PATH: /home/node/.openclaw/openclaw.json      OPENCLAW_WORKSPACE_DIR: /workspace    volumes:      - openclaw-config:/home/node/.openclaw      - openclaw-workspace:/workspace    labels:      caddy: openclaw.example.com      caddy.reverse_proxy: "{{upstreams 1455}}"    command: ["openclaw", "gateway", "--bind", "lan", "--port", "1455"] volumes:  openclaw-config:  openclaw-workspace:
[/code]

Thay `openclaw.example.com` bằng hostname Gateway của bạn. Lưu `OPENCLAW_GATEWAY_TOKEN` trong trình quản lý secret/môi trường của EasyRunner thay vì commit nó vào định nghĩa ứng dụng.

## Cấu hình OpenClaw

Bên trong volume cấu hình bền vững, giữ Gateway chỉ có thể truy cập thông qua proxy và yêu cầu xác thực:

json5Copy code
[code]
    {  gateway: {    bind: "lan",    port: 1455,    auth: {      token: "${OPENCLAW_GATEWAY_TOKEN}",    },  },}
[/code]

Nếu Caddy kết thúc TLS cho Gateway, hãy cấu hình thiết lập trusted proxy cho đúng đường dẫn proxy thay vì tắt kiểm tra xác thực trên toàn cục. Xem [Xác thực trusted proxy](</vi/gateway/trusted-proxy-auth>).

## Xác minh

Từ workstation của bạn:

bashCopy code
[code]
    openclaw gateway probe --url https://openclaw.example.com --token <token>openclaw gateway status --url https://openclaw.example.com --token <token>
[/code]

Từ máy chủ EasyRunner, kiểm tra nhật ký ứng dụng để xác nhận Gateway đang lắng nghe và không có lỗi khởi động về SecretRef, plugin hoặc xác thực kênh.

## Cập nhật và sao lưu

  * Pull hoặc build image OpenClaw mới, sau đó redeploy ứng dụng EasyRunner.
  * Sao lưu volume `openclaw-config` trước khi cập nhật.
  * Sao lưu `openclaw-workspace` nếu agent ghi dữ liệu dự án bền vững ở đó.
  * Chạy `openclaw doctor` sau các bản cập nhật lớn để phát hiện migration cấu hình và cảnh báo dịch vụ.


## Khắc phục sự cố

  * `gateway probe` không thể kết nối: xác nhận hostname Caddy trỏ tới ứng dụng và container đang lắng nghe trên `0.0.0.0:1455`.
  * Xác thực thất bại: xoay vòng token trong secret EasyRunner và lệnh client cục bộ cùng lúc.
  * Tệp thuộc sở hữu của root sau khi khôi phục: sửa các volume đã mount để người dùng container có thể ghi vào `/home/node/.openclaw` và `/workspace`.
  * Plugin trình duyệt hoặc kênh thất bại: kiểm tra xem các binary bên ngoài cần thiết, network egress và thông tin xác thực đã mount có khả dụng bên trong container hay không.


Was this useful?YesNo

Open issue