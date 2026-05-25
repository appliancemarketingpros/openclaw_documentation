---
title: Thư mục
source_url: https://docs.openclaw.ai/vi/cli/directory
scraped_at: 2026-05-25
---

# `openclaw directory`

Tra cứu thư mục cho các kênh hỗ trợ tính năng này (liên hệ/đồng cấp, nhóm và "tôi").

## Cờ chung

  * `--channel <name>`: id/bí danh kênh (bắt buộc khi nhiều kênh được cấu hình; tự động khi chỉ có một kênh được cấu hình)
  * `--account <id>`: id tài khoản (mặc định: mặc định của kênh)
  * `--json`: xuất JSON


## Ghi chú

  * `directory` nhằm giúp bạn tìm các ID có thể dán vào lệnh khác (đặc biệt là `openclaw message send --target ...`).
  * Với nhiều kênh, kết quả dựa trên cấu hình (danh sách cho phép / nhóm đã cấu hình) thay vì một thư mục nhà cung cấp trực tiếp.
  * Các Plugin kênh đã cài đặt vẫn có thể không hỗ trợ thư mục; trong trường hợp đó, lệnh sẽ báo thao tác thư mục không được hỗ trợ thay vì cài đặt lại Plugin.
  * Đầu ra mặc định là `id` (và đôi khi là `name`) được phân tách bằng tab; dùng `--json` để viết script.


## Sử dụng kết quả với `message send`

bashCopy code
[code]
    openclaw directory peers list --channel slack --query "U0"openclaw message send --channel slack --target user:U012ABCDEF --message "hello"
[/code]

## Định dạng ID (theo kênh)

  * WhatsApp: `+15551234567` (DM), `1234567890-1234567890@g.us` (nhóm), `120363123456789@newsletter` (đích gửi đi của Kênh/Bản tin)
  * Telegram: `@username` hoặc id cuộc trò chuyện dạng số; nhóm là các id dạng số
  * Slack: `user:U…` và `channel:C…`
  * Discord: `user:<id>` và `channel:<id>`
  * Matrix (Plugin): `user:@user:server`, `room:!roomId:server`, hoặc `#alias:server`
  * Microsoft Teams (Plugin): `user:<id>` và `conversation:<id>`
  * Zalo (Plugin): id người dùng (Bot API)
  * Zalo Personal / `zalouser` (Plugin): id luồng (DM/nhóm) từ `zca` (`me`, `friend list`, `group list`)


## Bản thân ("tôi")

bashCopy code
[code]
    openclaw directory self --channel zalouser
[/code]

## Đồng cấp (liên hệ/người dùng)

bashCopy code
[code]
    openclaw directory peers list --channel zalouseropenclaw directory peers list --channel zalouser --query "name"openclaw directory peers list --channel zalouser --limit 50
[/code]

## Nhóm

bashCopy code
[code]
    openclaw directory groups list --channel zalouseropenclaw directory groups list --channel zalouser --query "work"openclaw directory groups members --channel zalouser --group-id <id>
[/code]

## Liên quan

  * [Tham chiếu CLI](</vi/cli>)


Was this useful?YesNo