---
title: Plugin cá nhân Zalo
source_url: https://docs.openclaw.ai/vi/plugins/zalouser
scraped_at: 2026-05-25
---

Hỗ trợ Zalo Personal cho OpenClaw thông qua một Plugin, sử dụng `zca-js` gốc để tự động hóa một tài khoản người dùng Zalo thông thường.

## Cách đặt tên

ID kênh là `zalouser` để thể hiện rõ rằng kênh này tự động hóa một **tài khoản người dùng Zalo cá nhân** (không chính thức). Chúng tôi giữ `zalo` cho khả năng tích hợp API Zalo chính thức trong tương lai.

## Nơi chạy

Plugin này chạy **bên trong tiến trình Gateway**.

Nếu bạn dùng Gateway từ xa, hãy cài đặt/cấu hình trên **máy đang chạy Gateway** , rồi khởi động lại Gateway.

Không cần tệp nhị phân CLI `zca`/`openzca` bên ngoài.

## Cài đặt

### Tùy chọn A: cài đặt từ npm

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

Dùng gói trần để theo thẻ phát hành chính thức hiện tại. Chỉ ghim một phiên bản chính xác khi bạn cần một bản cài đặt có thể tái lập.

Sau đó khởi động lại Gateway.

### Tùy chọn B: cài đặt từ thư mục cục bộ (dev)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

Sau đó khởi động lại Gateway.

## Cấu hình

Cấu hình kênh nằm dưới `channels.zalouser` (không phải `plugins.entries.*`):

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## Công cụ agent

Tên công cụ: `zalouser`

Hành động: `send`, `image`, `link`, `friends`, `groups`, `me`, `status`

Các hành động tin nhắn kênh cũng hỗ trợ `react` cho phản ứng với tin nhắn.

## Liên quan

  * [Xây dựng Plugin](</vi/plugins/building-plugins>)
  * [ClawHub](</vi/clawhub>)


Was this useful?YesNo