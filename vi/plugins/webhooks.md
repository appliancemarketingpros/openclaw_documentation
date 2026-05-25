---
title: Plugin Webhook
source_url: https://docs.openclaw.ai/vi/plugins/webhooks
scraped_at: 2026-05-25
---

Plugin Webhooks thêm các tuyến HTTP đã xác thực để liên kết tự động hóa bên ngoài với các TaskFlow OpenClaw.

Dùng Plugin này khi bạn muốn một hệ thống đáng tin cậy như Zapier, n8n, một tác vụ CI, hoặc một dịch vụ nội bộ tạo và điều khiển các TaskFlow được quản lý mà chưa cần viết Plugin tùy chỉnh.

## Nơi chạy

Plugin Webhooks chạy bên trong tiến trình Gateway.

Nếu Gateway của bạn chạy trên máy khác, hãy cài đặt và cấu hình Plugin trên máy chủ Gateway đó, rồi khởi động lại Gateway.

## Cấu hình tuyến

Đặt cấu hình trong `plugins.entries.webhooks.config`:

json5Copy code
[code]
    {  plugins: {    entries: {      webhooks: {        enabled: true,        config: {          routes: {            zapier: {              path: "/plugins/webhooks/zapier",              sessionKey: "agent:main:main",              secret: {                source: "env",                provider: "default",                id: "OPENCLAW_WEBHOOK_SECRET",              },              controllerId: "webhooks/zapier",              description: "Zapier TaskFlow bridge",            },          },        },      },    },  },}
[/code]

Các trường của tuyến:

  * `enabled`: tùy chọn, mặc định là `true`
  * `path`: tùy chọn, mặc định là `/plugins/webhooks/<routeId>`
  * `sessionKey`: phiên bắt buộc sở hữu các TaskFlow được liên kết
  * `secret`: bí mật dùng chung hoặc SecretRef bắt buộc
  * `controllerId`: id bộ điều khiển tùy chọn cho các luồng được quản lý đã tạo
  * `description`: ghi chú tùy chọn cho người vận hành


Các đầu vào `secret` được hỗ trợ:

  * Chuỗi thuần
  * SecretRef với `source: "env" | "file" | "exec"`


Nếu một tuyến dùng bí mật không thể phân giải bí mật khi khởi động, Plugin sẽ bỏ qua tuyến đó và ghi cảnh báo thay vì để lộ một endpoint bị hỏng.

## Mô hình bảo mật

Mỗi tuyến được tin cậy để hành động với quyền TaskFlow của `sessionKey` đã cấu hình.

Điều này nghĩa là tuyến có thể kiểm tra và thay đổi các TaskFlow thuộc sở hữu của phiên đó, vì vậy bạn nên:

  * Dùng một bí mật mạnh và duy nhất cho mỗi tuyến
  * Ưu tiên tham chiếu bí mật thay vì bí mật văn bản thuần nội tuyến
  * Liên kết tuyến với phiên hẹp nhất phù hợp với quy trình làm việc
  * Chỉ để lộ đường dẫn Webhook cụ thể bạn cần


Plugin áp dụng:

  * Xác thực bằng bí mật dùng chung
  * Giới hạn kích thước và thời gian chờ của thân yêu cầu
  * Giới hạn tốc độ theo cửa sổ cố định
  * Giới hạn yêu cầu đang xử lý
  * Truy cập TaskFlow gắn với chủ sở hữu thông qua `api.runtime.tasks.managedFlows.bindSession(...)`


## Định dạng yêu cầu

Gửi yêu cầu `POST` với:

  * `Content-Type: application/json`
  * `Authorization: Bearer <secret>` hoặc `x-openclaw-webhook-secret: <secret>`


Ví dụ:

bashCopy code
[code]
    curl -X POST https://gateway.example.com/plugins/webhooks/zapier \  -H 'Content-Type: application/json' \  -H 'Authorization: Bearer YOUR_SHARED_SECRET' \  -d '{"action":"create_flow","goal":"Review inbound queue"}'
[/code]

## Hành động được hỗ trợ

Plugin hiện chấp nhận các giá trị JSON `action` sau:

  * `create_flow`
  * `get_flow`
  * `list_flows`
  * `find_latest_flow`
  * `resolve_flow`
  * `get_task_summary`
  * `set_waiting`
  * `resume_flow`
  * `finish_flow`
  * `fail_flow`
  * `request_cancel`
  * `cancel_flow`
  * `run_task`


### `create_flow`

Tạo một TaskFlow được quản lý cho phiên được liên kết của tuyến.

Ví dụ:

jsonCopy code
[code]
    {  "action": "create_flow",  "goal": "Review inbound queue",  "status": "queued",  "notifyPolicy": "done_only"}
[/code]

### `run_task`

Tạo một tác vụ con được quản lý bên trong một TaskFlow được quản lý hiện có.

Các thời gian chạy được phép là:

  * `subagent`
  * `acp`


Ví dụ:

jsonCopy code
[code]
    {  "action": "run_task",  "flowId": "flow_123",  "runtime": "acp",  "childSessionKey": "agent:main:acp:worker",  "task": "Inspect the next message batch"}
[/code]

## Dạng phản hồi

Phản hồi thành công trả về:

jsonCopy code
[code]
    {  "ok": true,  "routeId": "zapier",  "result": {}}
[/code]

Yêu cầu bị từ chối trả về:

jsonCopy code
[code]
    {  "ok": false,  "routeId": "zapier",  "code": "not_found",  "error": "TaskFlow not found.",  "result": {}}
[/code]

Plugin chủ ý loại bỏ siêu dữ liệu chủ sở hữu/phiên khỏi phản hồi Webhook.

## Tài liệu liên quan

  * [SDK thời gian chạy Plugin](</vi/plugins/sdk-runtime>)
  * [Tổng quan về hook và Webhook](</vi/automation/hooks>)
  * [Webhook CLI](</vi/cli/webhooks>)


Was this useful?YesNo