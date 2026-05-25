---
title: Bộ điều hợp RPC
source_url: https://docs.openclaw.ai/vi/reference/rpc
scraped_at: 2026-05-25
---

OpenClaw tích hợp các CLI bên ngoài qua JSON-RPC. Hiện nay có hai mẫu được sử dụng.

## Mẫu A: trình nền HTTP (signal-cli)

  * `signal-cli` chạy như một trình nền với JSON-RPC qua HTTP.
  * Luồng sự kiện là SSE (`/api/v1/events`).
  * Kiểm tra tình trạng: `/api/v1/check`.
  * OpenClaw sở hữu vòng đời khi `channels.signal.autoStart=true`.


Xem [Signal](</vi/channels/signal>) để biết cách thiết lập và các endpoint.

## Mẫu B: tiến trình con stdio (imsg)

  * OpenClaw sinh `imsg rpc` như một tiến trình con cho [iMessage](</vi/channels/imessage>).
  * JSON-RPC được phân tách theo dòng qua stdin/stdout (một đối tượng JSON trên mỗi dòng).
  * Không cần cổng TCP, không cần trình nền.


Các phương thức lõi được dùng:

  * `watch.subscribe` → thông báo (`method: "message"`)
  * `watch.unsubscribe`
  * `send`
  * `chats.list` (thăm dò/chẩn đoán)


Xem [iMessage](</vi/channels/imessage>) để biết cách thiết lập kế thừa và định địa chỉ (ưu tiên `chat_id`).

## Hướng dẫn adapter

  * Gateway sở hữu tiến trình (bắt đầu/dừng gắn với vòng đời nhà cung cấp).
  * Giữ cho các máy khách RPC bền bỉ: thời gian chờ, khởi động lại khi thoát.
  * Ưu tiên ID ổn định (ví dụ: `chat_id`) hơn chuỗi hiển thị.


## Liên quan

  * [Giao thức Gateway](</vi/gateway/protocol>)


Was this useful?YesNo