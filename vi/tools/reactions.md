---
title: Phản ứng
source_url: https://docs.openclaw.ai/vi/tools/reactions
scraped_at: 2026-05-25
---

Tác tử có thể thêm và xóa phản ứng emoji trên tin nhắn bằng công cụ `message` với hành động `react`. Hành vi phản ứng thay đổi tùy theo kênh và phương thức truyền tải.

## Cách hoạt động

jsonCopy code
[code]
    {  "action": "react",  "messageId": "msg-123",  "emoji": "thumbsup"}
[/code]

  * `emoji` là bắt buộc khi thêm phản ứng.
  * Đặt `emoji` thành chuỗi rỗng (`""`) để xóa phản ứng của bot.
  * Đặt `remove: true` để xóa một emoji cụ thể (yêu cầu `emoji` không rỗng).
  * Trên các kênh hỗ trợ phản ứng trạng thái, `trackToolCalls: true` trên một phản ứng cho phép runtime dùng tin nhắn đã được phản ứng đó cho các phản ứng tiến trình công cụ tiếp theo trong cùng lượt.


## Hành vi theo kênh

Discord và Slack

  * `emoji` rỗng sẽ xóa tất cả phản ứng của bot trên tin nhắn.
  * `remove: true` chỉ xóa emoji đã chỉ định.

Google Chat

  * `emoji` rỗng sẽ xóa phản ứng của ứng dụng trên tin nhắn.
  * `remove: true` chỉ xóa emoji đã chỉ định.

Telegram

  * `emoji` rỗng sẽ xóa phản ứng của bot.
  * `remove: true` cũng xóa phản ứng nhưng vẫn yêu cầu `emoji` không rỗng để xác thực công cụ.

WhatsApp

  * `emoji` rỗng sẽ xóa phản ứng của bot.
  * `remove: true` được ánh xạ nội bộ thành emoji rỗng (vẫn yêu cầu `emoji` trong lệnh gọi công cụ).

Zalo cá nhân (zalouser)

  * Yêu cầu `emoji` không rỗng.
  * `remove: true` xóa phản ứng emoji cụ thể đó.

Feishu/Lark

  * Dùng công cụ `feishu_reaction` với các hành động `add`, `remove` và `list`.
  * Thêm/xóa yêu cầu `emoji_type`; xóa cũng yêu cầu `reaction_id`.

Signal

  * Thông báo phản ứng đến được kiểm soát bởi `channels.signal.reactionNotifications`: `"off"` tắt chúng, `"own"` (mặc định) phát sự kiện khi người dùng phản ứng với tin nhắn của bot, và `"all"` phát sự kiện cho tất cả phản ứng.

iMessage

  * Phản ứng gửi đi là tapback của iMessage (`love`, `like`, `dislike`, `laugh`, `emphasize` và `question`).
  * Thông báo tapback đến được kiểm soát bởi `channels.imessage.reactionNotifications`: `"off"` tắt chúng, `"own"` (mặc định) phát sự kiện khi người dùng phản ứng với tin nhắn do bot soạn, và `"all"` phát sự kiện cho tất cả tapback từ người gửi được ủy quyền.


## Mức độ phản ứng

Cấu hình `reactionLevel` theo từng kênh kiểm soát phạm vi tác tử dùng phản ứng. Giá trị thường là `off`, `ack`, `minimal` hoặc `extensive`.

  * [Telegram reactionLevel](</vi/channels/telegram#reaction-notifications>) — `channels.telegram.reactionLevel`
  * [WhatsApp reactionLevel](</vi/channels/whatsapp#reaction-level>) — `channels.whatsapp.reactionLevel`


Đặt `reactionLevel` trên từng kênh để điều chỉnh mức độ chủ động của tác tử khi phản ứng với tin nhắn trên mỗi nền tảng.

## Liên quan

  * [Agent Send](</vi/tools/agent-send>) — công cụ `message` bao gồm `react`
  * [Kênh](</vi/channels>) — cấu hình dành riêng cho từng kênh


Was this useful?YesNo