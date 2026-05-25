---
title: Cuộc gọi thoại
source_url: https://docs.openclaw.ai/vi/cli/voicecall
scraped_at: 2026-05-25
---

# `openclaw voicecall`

`voicecall` là lệnh do Plugin cung cấp. Lệnh này chỉ xuất hiện khi Plugin cuộc gọi thoại được cài đặt và bật.

Khi Gateway đang chạy, các lệnh vận hành (`call`, `start`, `continue`, `speak`, `dtmf`, `end`, `status`) được định tuyến đến runtime cuộc gọi thoại của Gateway đó. Nếu không thể kết nối đến Gateway nào, chúng sẽ chuyển sang runtime CLI độc lập.

## Lệnh con

bashCopy code
[code]
    openclaw voicecall setup    [--json]openclaw voicecall smoke    [-t <phone>] [--message <text>] [--mode <m>] [--yes] [--json]openclaw voicecall call     -m <text> [-t <phone>] [--mode <m>]openclaw voicecall start    --to <phone> [--message <text>] [--mode <m>]openclaw voicecall continue --call-id <id> --message <text>openclaw voicecall speak    --call-id <id> --message <text>openclaw voicecall dtmf     --call-id <id> --digits <digits>openclaw voicecall end      --call-id <id>openclaw voicecall status   [--call-id <id>] [--json]openclaw voicecall tail     [--file <path>] [--since <n>] [--poll <ms>]openclaw voicecall latency  [--file <path>] [--last <n>]openclaw voicecall expose   [--mode <m>] [--path <p>] [--port <port>] [--serve-path <p>]
[/code]

Lệnh con | Mô tả  
---|---  
`setup` | Hiển thị các bước kiểm tra mức sẵn sàng của nhà cung cấp và Webhook.  
`smoke` | Chạy kiểm tra mức sẵn sàng; chỉ thực hiện cuộc gọi thử nghiệm trực tiếp với `--yes`.  
`call` | Khởi tạo cuộc gọi thoại đi.  
`start` | Bí danh cho `call` với `--to` bắt buộc và `--message` tùy chọn.  
`continue` | Phát một thông điệp và chờ phản hồi tiếp theo.  
`speak` | Phát một thông điệp mà không chờ phản hồi.  
`dtmf` | Gửi chữ số DTMF đến một cuộc gọi đang hoạt động.  
`end` | Gác máy một cuộc gọi đang hoạt động.  
`status` | Kiểm tra các cuộc gọi đang hoạt động (hoặc một cuộc gọi theo `--call-id`).  
`tail` | Theo dõi `calls.jsonl` (hữu ích trong khi kiểm thử nhà cung cấp).  
`latency` | Tóm tắt chỉ số độ trễ lượt từ `calls.jsonl`.  
`expose` | Bật/tắt Tailscale serve/funnel cho điểm cuối Webhook.  
  
## Thiết lập và smoke

### `setup`

Mặc định in các bước kiểm tra mức sẵn sàng ở dạng người đọc được. Truyền `--json` cho script.

bashCopy code
[code]
    openclaw voicecall setupopenclaw voicecall setup --json
[/code]

### `smoke`

Chạy cùng các bước kiểm tra mức sẵn sàng. Lệnh này sẽ không thực hiện cuộc gọi điện thoại thật trừ khi có cả `--to` và `--yes`.

Cờ | Mặc định | Mô tả  
---|---|---  
`-t, --to <phone>` | (không có) | Số điện thoại để gọi cho smoke trực tiếp.  
`--message <text>` | `OpenClaw voice call smoke test.` | Thông điệp sẽ phát trong cuộc gọi smoke.  
`--mode <mode>` | `notify` | Chế độ gọi: `notify` hoặc `conversation`.  
`--yes` | `false` | Thực sự thực hiện cuộc gọi đi trực tiếp.  
`--json` | `false` | In JSON cho máy đọc.  
bashCopy code
[code]
    openclaw voicecall smokeopenclaw voicecall smoke --to "+15555550123"        # dry runopenclaw voicecall smoke --to "+15555550123" --yes  # live notify call
[/code]

## Vòng đời cuộc gọi

### `call`

Khởi tạo cuộc gọi thoại đi.

Cờ | Bắt buộc | Mặc định | Mô tả  
---|---|---|---  
`-m, --message <text>` | có | (không có) | Thông điệp sẽ phát khi cuộc gọi kết nối.  
`-t, --to <phone>` | không | config `toNumber` | Số điện thoại E.164 để gọi.  
`--mode <mode>` | không | `conversation` | Chế độ gọi: `notify` (gác máy sau thông điệp) hoặc `conversation` (giữ mở).  
bashCopy code
[code]
    openclaw voicecall call --to "+15555550123" --message "Hello"openclaw voicecall call -m "Heads up" --mode notify
[/code]

### `start`

Bí danh cho `call` với dạng cờ mặc định khác.

Cờ | Bắt buộc | Mặc định | Mô tả  
---|---|---|---  
`--to <phone>` | có | (không có) | Số điện thoại để gọi.  
`--message <text>` | không | (không có) | Thông điệp sẽ phát khi cuộc gọi kết nối.  
`--mode <mode>` | không | `conversation` | Chế độ gọi: `notify` hoặc `conversation`.  
  
### `continue`

Phát một thông điệp và chờ phản hồi.

Cờ | Bắt buộc | Mô tả  
---|---|---  
`--call-id <id>` | có | ID cuộc gọi.  
`--message <text>` | có | Thông điệp sẽ phát.  
  
### `speak`

Phát một thông điệp mà không chờ phản hồi.

Cờ | Bắt buộc | Mô tả  
---|---|---  
`--call-id <id>` | có | ID cuộc gọi.  
`--message <text>` | có | Thông điệp sẽ phát.  
  
### `dtmf`

Gửi chữ số DTMF đến một cuộc gọi đang hoạt động.

Cờ | Bắt buộc | Mô tả  
---|---|---  
`--call-id <id>` | có | ID cuộc gọi.  
`--digits <digits>` | có | Chữ số DTMF (ví dụ `ww123456#` cho thời gian chờ).  
  
### `end`

Gác máy một cuộc gọi đang hoạt động.

Cờ | Bắt buộc | Mô tả  
---|---|---  
`--call-id <id>` | có | ID cuộc gọi.  
  
### `status`

Kiểm tra các cuộc gọi đang hoạt động.

Cờ | Mặc định | Mô tả  
---|---|---  
`--call-id <id>` | (không có) | Giới hạn đầu ra ở một cuộc gọi.  
`--json` | `false` | In JSON cho máy đọc.  
bashCopy code
[code]
    openclaw voicecall statusopenclaw voicecall status --jsonopenclaw voicecall status --call-id <id>
[/code]

## Nhật ký và chỉ số

### `tail`

Theo dõi nhật ký JSONL cuộc gọi thoại. In `--since` dòng cuối cùng khi bắt đầu, sau đó stream các dòng mới khi chúng được ghi.

Cờ | Mặc định | Mô tả  
---|---|---  
`--file <path>` | được phân giải từ kho Plugin | Đường dẫn đến `calls.jsonl`.  
`--since <n>` | `25` | Số dòng cần in trước khi theo dõi.  
`--poll <ms>` | `250` (tối thiểu 50) | Khoảng thời gian poll tính bằng mili giây.  
  
### `latency`

Tóm tắt chỉ số độ trễ lượt và thời gian chờ lắng nghe từ `calls.jsonl`. Đầu ra là JSON với các bản tóm tắt `recordsScanned`, `turnLatency`, và `listenWait`.

Cờ | Mặc định | Mô tả  
---|---|---  
`--file <path>` | được phân giải từ kho Plugin | Đường dẫn đến `calls.jsonl`.  
`--last <n>` | `200` (tối thiểu 1) | Số bản ghi gần đây cần phân tích.  
  
## Phơi bày Webhook

### `expose`

Bật, tắt, hoặc thay đổi cấu hình Tailscale serve/funnel cho Webhook thoại.

Cờ | Mặc định | Mô tả  
---|---|---  
`--mode <mode>` | `funnel` | `off`, `serve` (tailnet), hoặc `funnel` (công khai).  
`--path <path>` | config `tailscale.path` hoặc `--serve-path` | Đường dẫn Tailscale cần phơi bày.  
`--port <port>` | config `serve.port` hoặc `3334` | Cổng Webhook cục bộ.  
`--serve-path <path>` | config `serve.path` hoặc `/voice/webhook` | Đường dẫn Webhook cục bộ.  
bashCopy code
[code]
    openclaw voicecall expose --mode serveopenclaw voicecall expose --mode funnelopenclaw voicecall expose --mode off
[/code]

## Liên quan

  * [Tham chiếu CLI](</vi/cli>)
  * [Plugin cuộc gọi thoại](</vi/plugins/voice-call>)


Was this useful?YesNo