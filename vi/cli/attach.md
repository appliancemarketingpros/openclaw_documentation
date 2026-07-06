---
title: Đính kèm CLI
source_url: https://docs.openclaw.ai/vi/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach` khởi chạy Claude Code với một cấu hình MCP tạm thời nghiêm ngặt được liên kết với một phiên Gateway.

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

Tùy chọn:

  * `--session <key>` liên kết quyền cấp với một phiên Gateway. Mặc định là phiên chính.
  * `--ttl <ms>` yêu cầu TTL quyền cấp dương tính bằng mili giây. Gateway áp dụng mức trần riêng.
  * `--bin <path>` chọn tệp nhị phân Claude Code. Mặc định là `claude`.
  * `--print-config` ghi `.mcp.json` tạm thời, in lệnh khởi chạy và env, đồng thời giữ quyền cấp còn hiệu lực cho đến khi TTL hết hạn.


Token bearer được truyền qua biến môi trường, không phải argv. OpenClaw khởi chạy Claude Code với `--strict-mcp-config --mcp-config <path>` để các máy chủ Claude MCP trong môi trường không tham gia phiên đã gắn. Các lần khởi chạy thông thường thu hồi quyền cấp khi tiến trình Claude Code thoát.

Xem thêm: [Gateway CLI](</vi/cli/gateway>), [MCP CLI](</vi/cli/mcp>), và [ACP CLI](</vi/cli/acp>).

Was this useful?YesNo

Open issue