---
title: CLI bản ghi cuộc trao đổi
source_url: https://docs.openclaw.ai/vi/cli/transcripts
scraped_at: 2026-06-29
---

Get started

# `openclaw transcripts`

Kiểm tra bản ghi được công cụ `transcripts` lõi của OpenClaw ghi lại. CLI này ở chế độ chỉ đọc; việc ghi, nhập và tóm tắt do công cụ agent và các nguồn tự khởi động đã cấu hình đảm nhiệm.

Dùng CLI khi bạn muốn tìm ghi chú hôm qua, mở tệp Markdown trong trình soạn thảo, đưa một bản ghi vào công cụ khác, hoặc gỡ lỗi xem một phiên được lưu ở đâu trên đĩa. Công cụ này không bắt đầu hoặc dừng việc ghi.

Artifact nằm trong thư mục trạng thái OpenClaw:

textCopy code
[code]
    $OPENCLAW_STATE_DIR/transcripts/YYYY-MM-DD/<session>/  metadata.json  transcript.jsonl  summary.json  summary.md
[/code]

Thư mục trạng thái mặc định là `~/.openclaw`; đặt `OPENCLAW_STATE_DIR` để dùng một thư mục khác. Thư mục ngày lấy từ thời điểm bắt đầu phiên, và thư mục phiên là một phân đoạn hệ thống tệp an toàn được suy ra từ id phiên.

## Lệnh

bashCopy code
[code]
    openclaw transcripts listopenclaw transcripts show <session>openclaw transcripts show YYYY-MM-DD/<session>openclaw transcripts path <session>openclaw transcripts path YYYY-MM-DD/<session>openclaw transcripts path <session> --diropenclaw transcripts path <session> --metadataopenclaw transcripts path <session> --transcriptopenclaw transcripts list --jsonopenclaw transcripts show <session> --jsonopenclaw transcripts path <session> --json
[/code]

  * `list`: liệt kê các phiên đã lưu, bộ chọn kèm ngày, thời điểm bắt đầu, tiêu đề và đường dẫn `summary.md`.
  * `show <session>`: in `summary.md` đã lưu.
  * `path <session>`: in đường dẫn `summary.md`.
  * `path <session> --dir`: in thư mục phiên.
  * `path <session> --metadata`: in `metadata.json`.
  * `path <session> --transcript`: in `transcript.jsonl`.
  * `--json`: in đầu ra máy đọc được.


Khi id phiên do con người đặt bị lặp qua nhiều ngày, dùng bộ chọn kèm ngày từ `list`, ví dụ `openclaw transcripts show 2026-05-22/standup`. Id phiên mặc định bao gồm dấu thời gian và hậu tố ngẫu nhiên; chỉ cấu hình id phiên cố định khi chúng là duy nhất trong ngày.

## Đầu ra

`list` in một phiên trên mỗi dòng:

textCopy code
[code]
    2026-05-22/standup  2026-05-22T09:00:00.000Z  Weekly standup  /Users/alex/.openclaw/transcripts/2026-05-22/standup/summary.md
[/code]

Đầu ra được phân tách bằng tab. Các cột là bộ chọn, thời điểm bắt đầu, tiêu đề và đường dẫn tóm tắt. Bộ chọn là giá trị an toàn nhất để truyền lại cho `show` hoặc `path`.

`list --json` in các đối tượng có:

  * `sessionId`
  * `selector`
  * `date`
  * `title`
  * `startedAt`
  * `stoppedAt`
  * `source`
  * `path`
  * `summaryPath`
  * `hasSummary`


`show --json` trả về siêu dữ liệu phiên đã lưu, bộ chọn, thư mục phiên, đường dẫn tóm tắt và văn bản Markdown tóm tắt. `path --json` trả về đường dẫn đã chọn và cho biết tệp đó có tồn tại hay không.

## Nhiều cuộc họp mỗi ngày

Transcripts nhóm các phiên theo ngày, rồi theo id phiên. Mười cuộc họp trong một ngày trở thành mười thư mục cùng cấp:

textCopy code
[code]
    ~/.openclaw/transcripts/2026-05-22/  transcript-2026-05-22T09-00-00-000Z-a1b2c3d4/  transcript-2026-05-22T10-30-00-000Z-b2c3d4e5/  standup/
[/code]

Dùng id được tạo mặc định cho hầu hết tự động hóa. Dùng id cố định như `standup` chỉ khi cùng id đó sẽ không được dùng hai lần trong cùng một ngày.

## Thiếu bản tóm tắt

Các phiên trực tiếp ghi `summary.md` khi phiên dừng. Các bản ghi được nhập sẽ ghi `summary.md` ngay sau khi nhập. Một phiên vẫn có thể xuất hiện trong `list` mà không có bản tóm tắt khi việc ghi đang hoạt động, provider gặp lỗi trong lúc dừng, hoặc siêu dữ liệu được ghi trước khi có bất kỳ lời thoại nào đến.

Dùng `path <session> --transcript` để kiểm tra bản ghi chỉ ghi thêm, và dùng hành động `summarize` của công cụ `transcripts` để tạo lại bản tóm tắt Markdown.

## Cấu hình

Việc ghi bản ghi là tùy chọn bật vì các nguồn trực tiếp có thể tham gia và ghi âm cuộc họp. Bật công cụ bằng `transcripts.enabled` cấp cao nhất:

jsonCopy code
[code]
    {  "transcripts": {    "enabled": true,    "maxUtterances": 2000  }}
[/code]

Cấu hình các nguồn tự khởi động bằng `transcripts.autoStart` trong `openclaw.json`. Mỗi mục được bật khi có mặt; bỏ qua một mục để tắt nguồn đó.

jsonCopy code
[code]
    {  "transcripts": {    "enabled": true,    "autoStart": [      {        "providerId": "discord-voice",        "guildId": "1234567890",        "channelId": "2345678901"      },      {        "providerId": "slack-huddle",        "accountId": "workspace",        "channelId": "C123"      }    ]  }}
[/code]

Was this useful?YesNo

Open issue