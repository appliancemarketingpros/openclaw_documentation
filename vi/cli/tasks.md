---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/vi/cli/tasks
scraped_at: 2026-05-25
---

Kiểm tra các tác vụ nền bền vững và trạng thái Task Flow. Khi không có lệnh con, `openclaw tasks` tương đương với `openclaw tasks list`.

Xem [Tác vụ nền](</vi/automation/tasks>) để biết vòng đời và mô hình phân phối.

## Cách sử dụng

bashCopy code
[code]
    openclaw tasksopenclaw tasks listopenclaw tasks list --runtime acpopenclaw tasks list --status runningopenclaw tasks show <lookup>openclaw tasks notify <lookup> state_changesopenclaw tasks cancel <lookup>openclaw tasks auditopenclaw tasks maintenanceopenclaw tasks maintenance --applyopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## Tùy chọn gốc

  * `--json`: xuất JSON.
  * `--runtime <name>`: lọc theo loại: `subagent`, `acp`, `cron`, hoặc `cli`.
  * `--status <name>`: lọc theo trạng thái: `queued`, `running`, `succeeded`, `failed`, `timed_out`, `cancelled`, hoặc `lost`.


## Lệnh con

### `list`

bashCopy code
[code]
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
[/code]

Liệt kê các tác vụ nền được theo dõi, mới nhất trước.

### `show`

bashCopy code
[code]
    openclaw tasks show <lookup> [--json]
[/code]

Hiển thị một tác vụ theo ID tác vụ, ID lượt chạy, hoặc khóa phiên.

### `notify`

bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

Thay đổi chính sách thông báo cho một tác vụ đang chạy.

### `cancel`

bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

Hủy một tác vụ nền đang chạy.

### `audit`

bashCopy code
[code]
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
[/code]

Hiển thị các bản ghi tác vụ và Task Flow đã cũ, bị mất, phân phối thất bại, hoặc không nhất quán theo cách khác. Các tác vụ bị mất được giữ lại cho đến `cleanupAfter` là cảnh báo; các tác vụ bị mất đã hết hạn hoặc không được đóng dấu là lỗi.

### `maintenance`

bashCopy code
[code]
    openclaw tasks maintenance [--apply] [--json]
[/code]

Xem trước hoặc áp dụng việc đối chiếu tác vụ và Task Flow, đóng dấu dọn dẹp, cắt tỉa, và dọn dẹp sổ đăng ký phiên chạy cron đã cũ. Đối với các tác vụ cron, quá trình đối chiếu dùng nhật ký lượt chạy/trạng thái công việc đã lưu trước khi đánh dấu một tác vụ hoạt động cũ là `lost`, nên các lượt chạy cron đã hoàn tất không trở thành lỗi kiểm tra giả chỉ vì trạng thái runtime Gateway trong bộ nhớ đã biến mất. Kiểm tra CLI ngoại tuyến không có thẩm quyền đối với tập công việc cron đang hoạt động cục bộ theo tiến trình của Gateway. Các tác vụ CLI có ID lượt chạy/ID nguồn được đánh dấu là `lost` khi ngữ cảnh lượt chạy Gateway trực tiếp của chúng đã biến mất, ngay cả khi vẫn còn một hàng phiên con cũ. Khi được áp dụng, bảo trì cũng cắt tỉa các hàng sổ đăng ký phiên `cron:<jobId>:run:<uuid>` cũ hơn 7 ngày trong khi vẫn giữ nguyên các công việc cron hiện đang chạy và không chạm vào các hàng phiên không phải cron.

### `flow`

bashCopy code
[code]
    openclaw tasks flow list [--status <name>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Kiểm tra hoặc hủy trạng thái Task Flow bền vững trong sổ cái tác vụ.

## Liên quan

  * [Tham chiếu CLI](</vi/cli>)
  * [Tác vụ nền](</vi/automation/tasks>)


Was this useful?YesNo