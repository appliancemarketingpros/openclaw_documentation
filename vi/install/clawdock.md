---
title: ClawDock
source_url: https://docs.openclaw.ai/vi/install/clawdock
scraped_at: 2026-05-25
---

ClawDock là một lớp shell-helper nhỏ cho các bản cài đặt OpenClaw dựa trên Docker.

Nó cung cấp các lệnh ngắn như `clawdock-start`, `clawdock-dashboard` và `clawdock-fix-token` thay cho các lệnh gọi `docker compose ...` dài hơn.

Nếu bạn chưa thiết lập Docker, hãy bắt đầu với [Docker](</vi/install/docker>).

## Cài đặt

Dùng đường dẫn helper chuẩn:

bashCopy code
[code]
    mkdir -p ~/.clawdock && curl -sL https://raw.githubusercontent.com/openclaw/openclaw/main/scripts/clawdock/clawdock-helpers.sh -o ~/.clawdock/clawdock-helpers.shecho 'source ~/.clawdock/clawdock-helpers.sh' >> ~/.zshrc && source ~/.zshrc
[/code]

Nếu trước đây bạn đã cài đặt ClawDock từ `scripts/shell-helpers/clawdock-helpers.sh`, hãy cài đặt lại từ đường dẫn mới `scripts/clawdock/clawdock-helpers.sh`. Đường dẫn GitHub raw cũ đã bị gỡ bỏ.

## Những gì bạn nhận được

### Thao tác cơ bản

Lệnh | Mô tả  
---|---  
`clawdock-start` | Khởi động Gateway  
`clawdock-stop` | Dừng Gateway  
`clawdock-restart` | Khởi động lại Gateway  
`clawdock-status` | Kiểm tra trạng thái container  
`clawdock-logs` | Theo dõi nhật ký Gateway  
  
### Truy cập container

Lệnh | Mô tả  
---|---  
`clawdock-shell` | Mở một shell bên trong container Gateway  
`clawdock-cli <command>` | Chạy các lệnh OpenClaw CLI trong Docker  
`clawdock-exec <command>` | Thực thi một lệnh bất kỳ trong container  
  
### Giao diện web và ghép nối

Lệnh | Mô tả  
---|---  
`clawdock-dashboard` | Mở URL Control UI  
`clawdock-devices` | Liệt kê các yêu cầu ghép nối thiết bị đang chờ  
`clawdock-approve <id>` | Phê duyệt một yêu cầu ghép nối  
  
### Thiết lập và bảo trì

Lệnh | Mô tả  
---|---  
`clawdock-fix-token` | Cấu hình token Gateway bên trong container  
`clawdock-update` | Pull, dựng lại và khởi động lại  
`clawdock-rebuild` | Chỉ dựng lại image Docker  
`clawdock-clean` | Xóa container và volume  
  
### Tiện ích

Lệnh | Mô tả  
---|---  
`clawdock-health` | Chạy kiểm tra tình trạng Gateway  
`clawdock-token` | In token Gateway  
`clawdock-cd` | Chuyển đến thư mục dự án OpenClaw  
`clawdock-config` | Mở `~/.openclaw`  
`clawdock-show-config` | In các tệp cấu hình với các giá trị đã được che  
`clawdock-workspace` | Mở thư mục workspace  
  
## Luồng lần đầu

bashCopy code
[code]
    clawdock-startclawdock-fix-tokenclawdock-dashboard
[/code]

Nếu trình duyệt báo rằng cần ghép nối:

bashCopy code
[code]
    clawdock-devicesclawdock-approve <request-id>
[/code]

## Cấu hình và bí mật

ClawDock hoạt động với cùng cách tách cấu hình Docker được mô tả trong [Docker](</vi/install/docker>):

  * `<project>/.env` cho các giá trị riêng của Docker như tên image, cổng và token Gateway
  * `~/.openclaw/.env` cho khóa provider dựa trên env và token bot
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` cho xác thực OAuth/API-key của provider đã lưu
  * `~/.openclaw/openclaw.json` cho cấu hình hành vi


Dùng `clawdock-show-config` khi bạn muốn nhanh chóng kiểm tra các tệp `.env` và `openclaw.json`. Lệnh này che các giá trị `.env` trong đầu ra được in.

## Liên quan

[**Docker** Bản cài đặt Docker chuẩn cho OpenClaw. ](</vi/install/docker>) [**Docker VM runtime** Runtime VM do Docker quản lý để cô lập được tăng cường. ](</vi/install/docker-vm-runtime>) [**Updating** Cập nhật gói OpenClaw và các dịch vụ được quản lý. ](</vi/install/updating>)

Was this useful?YesNo