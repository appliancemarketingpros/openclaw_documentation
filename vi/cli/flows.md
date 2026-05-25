---
title: Luồng (chuyển hướng)
source_url: https://docs.openclaw.ai/vi/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

Không có lệnh cấp cao nhất `openclaw flows`. Việc kiểm tra TaskFlow bền vững nằm trong `openclaw tasks flow`.

## Lệnh con

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Lệnh con | Mô tả | Đối số / tùy chọn  
---|---|---  
`list` | Liệt kê các TaskFlow được theo dõi. | Đầu ra `--json` máy có thể đọc; bộ lọc `--status <name>` (xem các giá trị trạng thái bên dưới).  
`show` | Hiển thị một TaskFlow. | `<lookup>` id flow hoặc khóa chủ sở hữu; đầu ra `--json` máy có thể đọc.  
`cancel` | Hủy một TaskFlow đang chạy. | `<lookup>` id flow hoặc khóa chủ sở hữu.  
  
`<lookup>` chấp nhận id flow (được trả về bởi `list` / `show`) hoặc khóa chủ sở hữu của flow (định danh ổn định mà hệ thống con sở hữu dùng để theo dõi flow).

### Giá trị bộ lọc trạng thái

`--status` trên `list` chấp nhận một trong các giá trị sau:

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## Ví dụ

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

Để xem đầy đủ các khái niệm TaskFlow và cách biên soạn, hãy xem [TaskFlow](</vi/automation/taskflow>). Để biết lệnh mẹ `tasks`, hãy xem [tham chiếu CLI tasks](</vi/cli/tasks>).

## Liên quan

  * [Tham chiếu CLI](</vi/cli>)
  * [Tự động hóa](</vi/automation>)
  * [TaskFlow](</vi/automation/taskflow>)


Was this useful?YesNo