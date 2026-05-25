---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/vi/cli/commitments
scraped_at: 2026-05-25
---

Liệt kê và quản lý các cam kết theo dõi được suy luận.

Cam kết là các bộ nhớ theo dõi ngắn hạn, chỉ được tạo khi chọn tham gia từ ngữ cảnh cuộc trò chuyện. Xem [Cam kết được suy luận](</vi/concepts/commitments>) để đọc hướng dẫn khái niệm.

Khi không có lệnh con, `openclaw commitments` liệt kê các cam kết đang chờ.

## Cách sử dụng

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## Tùy chọn

  * `--all`: hiển thị tất cả trạng thái thay vì chỉ các cam kết đang chờ.
  * `--agent <id>`: lọc theo một id tác nhân.
  * `--status <status>`: lọc theo trạng thái. Giá trị: `pending`, `sent`, `dismissed`, `snoozed`, hoặc `expired`.
  * `--json`: xuất JSON máy đọc được.


## Ví dụ

Liệt kê các cam kết đang chờ:

bashCopy code
[code]
    openclaw commitments
[/code]

Liệt kê mọi cam kết đã lưu:

bashCopy code
[code]
    openclaw commitments --all
[/code]

Lọc theo một tác nhân:

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

Tìm các cam kết đã tạm hoãn:

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

Bỏ qua một hoặc nhiều cam kết:

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

Xuất dưới dạng JSON:

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## Đầu ra

Đầu ra văn bản bao gồm:

  * id cam kết
  * trạng thái
  * loại
  * thời điểm đến hạn sớm nhất
  * phạm vi
  * văn bản kiểm tra lại được đề xuất


Đầu ra JSON cũng bao gồm đường dẫn kho lưu trữ cam kết và toàn bộ bản ghi đã lưu.

## Liên quan

  * [Cam kết được suy luận](</vi/concepts/commitments>)
  * [Tổng quan về bộ nhớ](</vi/concepts/memory>)
  * [Heartbeat](</vi/gateway/heartbeat>)
  * [Tác vụ đã lên lịch](</vi/automation/cron-jobs>)


Was this useful?YesNo