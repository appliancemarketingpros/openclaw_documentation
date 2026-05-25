---
title: Tác nhân gửi
source_url: https://docs.openclaw.ai/vi/tools/agent-send
scraped_at: 2026-05-25
---

`openclaw agent` chạy một lượt agent duy nhất từ dòng lệnh mà không cần tin nhắn trò chuyện đến. Dùng lệnh này cho các quy trình có kịch bản, kiểm thử và gửi nội dung theo chương trình.

## Bắt đầu nhanh

* ### Chạy một lượt agent đơn giản

bashCopy code
[code]
    openclaw agent --message "What is the weather today?"
[/code]

Lệnh này gửi tin nhắn qua Gateway và in phản hồi.

* ### Nhắm đến một agent hoặc phiên cụ thể

bashCopy code
[code]
    # Target a specific agentopenclaw agent --agent ops --message "Summarize logs" # Target a phone number (derives session key)openclaw agent --to +15555550123 --message "Status update" # Reuse an existing sessionopenclaw agent --session-id abc123 --message "Continue the task"
[/code]

* ### Gửi phản hồi đến một kênh

bashCopy code
[code]
    # Deliver to WhatsApp (default channel)openclaw agent --to +15555550123 --message "Report ready" --deliver # Deliver to Slackopenclaw agent --agent ops --message "Generate report" \  --deliver --reply-channel slack --reply-to "#reports"
[/code]

## Cờ

Cờ | Mô tả  
---|---  
`--message \<text\>` | Tin nhắn cần gửi (bắt buộc)  
`--to \<dest\>` | Suy ra khóa phiên từ một mục tiêu (điện thoại, id trò chuyện)  
`--agent \<id\>` | Nhắm đến một agent đã cấu hình (dùng phiên `main` của agent đó)  
`--session-id \<id\>` | Tái sử dụng một phiên hiện có theo id  
`--local` | Buộc dùng runtime nhúng cục bộ (bỏ qua Gateway)  
`--deliver` | Gửi phản hồi đến một kênh trò chuyện  
`--channel \<name\>` | Kênh gửi (whatsapp, telegram, discord, slack, v.v.)  
`--reply-to \<target\>` | Ghi đè mục tiêu gửi  
`--reply-channel \<name\>` | Ghi đè kênh gửi  
`--reply-account \<id\>` | Ghi đè id tài khoản gửi  
`--thinking \<level\>` | Đặt mức suy luận cho hồ sơ mô hình đã chọn  
`--verbose \<on|full|off\>` | Đặt mức chi tiết  
`--timeout \<seconds\>` | Ghi đè thời gian chờ của agent  
`--json` | Xuất JSON có cấu trúc  
  
## Hành vi

  * Theo mặc định, CLI đi **qua Gateway**. Thêm `--local` để buộc dùng runtime nhúng trên máy hiện tại.
  * Nếu không thể truy cập Gateway, CLI **chuyển dự phòng** sang lượt chạy nhúng cục bộ.
  * Chọn phiên: `--to` suy ra khóa phiên (mục tiêu nhóm/kênh giữ nguyên cách ly; trò chuyện trực tiếp được gộp về `main`).
  * Các cờ suy luận và chi tiết được lưu vào kho phiên.
  * Đầu ra: mặc định là văn bản thuần, hoặc `--json` để có payload + siêu dữ liệu có cấu trúc.
  * Với `--json --deliver`, JSON bao gồm trạng thái gửi cho các lượt gửi đã gửi, bị chặn, một phần và thất bại. Xem [trạng thái gửi JSON](</vi/cli/agent#json-delivery-status>).


## Ví dụ

bashCopy code
[code]
    # Simple turn with JSON outputopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --json # Turn with thinking levelopenclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium # Deliver to a different channel than the sessionopenclaw agent --agent ops --message "Alert" --deliver --reply-channel telegram --reply-to "@admin"
[/code]

## Liên quan

[**Tham chiếu CLI cho agent** Tham chiếu đầy đủ về cờ và tùy chọn của `openclaw agent`. ](</vi/cli/agent>) [**Agent phụ** Khởi tạo agent phụ chạy nền. ](</vi/tools/subagents>) [**Phiên** Cách khóa phiên hoạt động và cách `--to`, `--agent`, và `--session-id` phân giải chúng. ](</vi/concepts/session>) [**Lệnh dấu gạch chéo** Danh mục lệnh gốc được dùng bên trong các phiên agent. ](</vi/tools/slash-commands>)

Was this useful?YesNo