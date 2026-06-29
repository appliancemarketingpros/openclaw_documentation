---
title: Plugin Codex Supervisor
source_url: https://docs.openclaw.ai/vi/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Plugin Codex Supervisor

Giám sát các phiên app-server Codex từ OpenClaw.

## Phân phối

  * Gói: `@openclaw/codex-supervisor`
  * Tuyến cài đặt: được bao gồm trong OpenClaw


## Bề mặt

hợp đồng: công cụ

## Liệt kê phiên

`codex_sessions_list` mặc định chỉ liệt kê các phiên Codex đã được tải. Đặt `include_stored` để bao gồm lịch sử đã lưu; plugin sử dụng đường dẫn liệt kê chỉ state-DB của app-server Codex và mặc định giới hạn kết quả đã lưu ở 200. Truyền `max_stored_sessions` để giảm hoặc tăng giới hạn đó, tối đa 1000.

Was this useful?YesNo

Open issue