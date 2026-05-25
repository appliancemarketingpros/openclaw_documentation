---
title: Gateway trên macOS
source_url: https://docs.openclaw.ai/vi/platforms/mac/bundled-gateway
scraped_at: 2026-05-25
---

OpenClaw.app không còn đóng gói kèm Node/Bun hoặc runtime Gateway. Ứng dụng macOS yêu cầu cài đặt CLI `openclaw` **bên ngoài** , không khởi chạy Gateway dưới dạng tiến trình con, và quản lý một dịch vụ launchd theo từng người dùng để giữ Gateway đang chạy (hoặc gắn vào một Gateway cục bộ hiện có nếu đã có Gateway đang chạy).

## Cài đặt CLI (bắt buộc cho chế độ cục bộ)

Node 24 là runtime mặc định trên Mac. Node 22 LTS, hiện là `22.16+`, vẫn hoạt động để tương thích. Sau đó cài đặt `openclaw` toàn cục:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

Nút **Cài đặt CLI** của ứng dụng macOS chạy cùng luồng cài đặt toàn cục mà ứng dụng dùng nội bộ: ưu tiên npm trước, sau đó pnpm, rồi bun nếu đó là trình quản lý gói duy nhất được phát hiện. Node vẫn là runtime Gateway được khuyến nghị.

## Launchd (Gateway dưới dạng LaunchAgent)

Nhãn:

  * `ai.openclaw.gateway` (hoặc `ai.openclaw.<profile>`; `com.openclaw.*` cũ có thể vẫn còn)


Vị trí plist (theo từng người dùng):

  * `~/Library/LaunchAgents/ai.openclaw.gateway.plist` (hoặc `~/Library/LaunchAgents/ai.openclaw.<profile>.plist`)


Trình quản lý:

  * Ứng dụng macOS sở hữu việc cài đặt/cập nhật LaunchAgent trong chế độ Cục bộ.
  * CLI cũng có thể cài đặt nó: `openclaw gateway install`.


Hành vi:

  * "OpenClaw Active" bật/tắt LaunchAgent.
  * Thoát ứng dụng **không** dừng gateway (launchd giữ nó hoạt động).
  * Nếu một Gateway đã chạy trên cổng đã cấu hình, ứng dụng sẽ gắn vào Gateway đó thay vì khởi động một Gateway mới.


Ghi nhật ký:

  * stdout/err của launchd: `/tmp/openclaw/openclaw-gateway.log`


## Tương thích phiên bản

Ứng dụng macOS kiểm tra phiên bản gateway so với phiên bản của chính nó. Nếu chúng không tương thích, hãy cập nhật CLI toàn cục để khớp với phiên bản ứng dụng.

## Kiểm tra smoke

bashCopy code
[code]
    openclaw --version OPENCLAW_SKIP_CHANNELS=1 \OPENCLAW_SKIP_CANVAS_HOST=1 \openclaw gateway --port 18999 --bind loopback
[/code]

Sau đó:

bashCopy code
[code]
    openclaw gateway call health --url ws://127.0.0.1:18999 --timeout 3000
[/code]

## Liên quan

  * [ứng dụng macOS](</vi/platforms/macos>)
  * [Runbook Gateway](</vi/gateway>)


Was this useful?YesNo