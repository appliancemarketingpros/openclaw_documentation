---
title: Hoàn tất
source_url: https://docs.openclaw.ai/vi/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

Tạo các script tự động hoàn thành cho shell và tùy chọn cài đặt chúng vào hồ sơ shell của bạn.

## Cách sử dụng

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## Tùy chọn

  * `-s, --shell <shell>`: shell đích (`zsh`, `bash`, `powershell`, `fish`; mặc định: `zsh`)
  * `-i, --install`: cài đặt tự động hoàn thành bằng cách thêm một dòng source vào hồ sơ shell của bạn
  * `--write-state`: ghi script tự động hoàn thành vào `$OPENCLAW_STATE_DIR/completions` mà không in ra stdout
  * `-y, --yes`: bỏ qua lời nhắc xác nhận cài đặt


## Ghi chú

  * `--install` ghi một khối nhỏ "OpenClaw Completion" vào hồ sơ shell của bạn và trỏ khối đó tới script đã lưu trong bộ nhớ đệm.
  * Nếu không có `--install` hoặc `--write-state`, lệnh sẽ in script ra stdout.
  * Việc tạo tự động hoàn thành sẽ tải trước cây lệnh để bao gồm cả các lệnh con lồng nhau.


## Liên quan

  * [Tham chiếu CLI](</vi/cli>)


Was this useful?YesNo