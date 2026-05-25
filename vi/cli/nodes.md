---
title: Các Node
source_url: https://docs.openclaw.ai/vi/cli/nodes
scraped_at: 2026-05-25
---

# `openclaw nodes`

Quản lý các Node đã ghép đôi (thiết bị) và gọi các khả năng của Node.

Liên quan:

  * Tổng quan về Node: [Node](</vi/nodes>)
  * Camera: [Node camera](</vi/nodes/camera>)
  * Hình ảnh: [Node hình ảnh](</vi/nodes/images>)


Tùy chọn chung:

  * `--url`, `--token`, `--timeout`, `--json`


## Lệnh chung

bashCopy code
[code]
    openclaw nodes listopenclaw nodes list --connectedopenclaw nodes list --last-connected 24hopenclaw nodes pendingopenclaw nodes approve <requestId>openclaw nodes reject <requestId>openclaw nodes remove --node <id|name|ip>openclaw nodes rename --node <id|name|ip> --name <displayName>openclaw nodes statusopenclaw nodes status --connectedopenclaw nodes status --last-connected 24h
[/code]

`nodes list` in các bảng đang chờ/đã ghép đôi. Các hàng đã ghép đôi bao gồm thời gian kể từ lần kết nối gần nhất (Lần kết nối gần nhất). Dùng `--connected` để chỉ hiển thị các Node hiện đang kết nối. Dùng `--last-connected <duration>` để lọc các Node đã kết nối trong một khoảng thời gian (ví dụ: `24h`, `7d`). Dùng `nodes remove --node <id|name|ip>` để xóa bản ghi ghép đôi Node cũ do Gateway sở hữu.

Lưu ý phê duyệt:

  * `openclaw nodes pending` chỉ cần phạm vi ghép đôi.
  * `gateway.nodes.pairing.autoApproveCidrs` có thể bỏ qua bước đang chờ chỉ đối với việc ghép đôi thiết bị `role: node` lần đầu, được tin cậy rõ ràng. Tính năng này tắt theo mặc định và không phê duyệt các lần nâng cấp.
  * `openclaw nodes approve <requestId>` kế thừa các yêu cầu phạm vi bổ sung từ yêu cầu đang chờ: 
    * yêu cầu không có lệnh: chỉ ghép đôi
    * lệnh Node không phải exec: ghép đôi + ghi
    * `system.run` / `system.run.prepare` / `system.which`: ghép đôi + admin


## Gọi

bashCopy code
[code]
    openclaw nodes invoke --node <id|name|ip> --command <command> --params <json>
[/code]

Cờ gọi:

  * `--params <json>`: chuỗi đối tượng JSON (mặc định `{}`).
  * `--invoke-timeout <ms>`: thời gian chờ gọi Node (mặc định `15000`).
  * `--idempotency-key <key>`: khóa idempotency tùy chọn.
  * `system.run` và `system.run.prepare` bị chặn ở đây; dùng công cụ `exec` với `host=node` để thực thi shell.


Để thực thi shell trên một Node, hãy dùng công cụ `exec` với `host=node` thay vì `openclaw nodes run`. CLI `nodes` hiện tập trung vào khả năng: RPC trực tiếp qua `nodes invoke`, cùng với ghép đôi, camera, màn hình, vị trí, Canvas và thông báo. Các lệnh Canvas được triển khai bởi Plugin Canvas thử nghiệm đi kèm; lõi giữ một móc tương thích để chúng vẫn nằm dưới `openclaw nodes canvas`.

## Liên quan

  * [Tham chiếu CLI](</vi/cli>)
  * [Node](</vi/nodes>)


Was this useful?YesNo