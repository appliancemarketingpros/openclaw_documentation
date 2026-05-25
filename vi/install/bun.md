---
title: Bun (thử nghiệm)
source_url: https://docs.openclaw.ai/vi/install/bun
scraped_at: 2026-05-25
---

Bun là một môi trường chạy cục bộ tùy chọn để chạy TypeScript trực tiếp (`bun run ...`, `bun --watch ...`). Trình quản lý gói mặc định vẫn là `pnpm`, được hỗ trợ đầy đủ và được công cụ tài liệu sử dụng. Bun không thể dùng `pnpm-lock.yaml` và sẽ bỏ qua tệp này.

## Cài đặt

* ### Cài đặt các phần phụ thuộc

shCopy code
[code]
    bun install
[/code]

`bun.lock` / `bun.lockb` được gitignore, nên không gây thay đổi trong repo. Để bỏ qua hoàn toàn việc ghi lockfile:

shCopy code
[code]
    bun install --no-save
[/code]

* ### Build và kiểm thử

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## Tập lệnh vòng đời

Bun chặn các tập lệnh vòng đời của phần phụ thuộc trừ khi được tin cậy rõ ràng. Với repo này, các tập lệnh thường bị chặn là không bắt buộc:

  * `baileys` `preinstall` \-- kiểm tra phiên bản chính của Node >= 20 (OpenClaw mặc định dùng Node 24 và vẫn hỗ trợ Node 22 LTS, hiện là `22.16+`)
  * `protobufjs` `postinstall` \-- phát cảnh báo về các lược đồ phiên bản không tương thích (không có tạo tác build)


Nếu bạn gặp sự cố runtime cần các tập lệnh này, hãy tin cậy chúng rõ ràng:

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## Lưu ý

Một số tập lệnh vẫn hardcode pnpm (ví dụ `docs:build`, `ui:*`, `protocol:check`). Tạm thời hãy chạy các tập lệnh đó qua pnpm.

## Liên quan

  * [Tổng quan cài đặt](</vi/install>)
  * [Node.js](</vi/install/node>)
  * [Cập nhật](</vi/install/updating>)


Was this useful?YesNo