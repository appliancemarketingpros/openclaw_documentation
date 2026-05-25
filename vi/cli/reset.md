---
title: Đặt lại
source_url: https://docs.openclaw.ai/vi/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

Đặt lại cấu hình/trạng thái cục bộ (giữ CLI đã cài đặt).

Tùy chọn:

  * `--scope <scope>`: `config`, `config+creds+sessions`, hoặc `full`
  * `--yes`: bỏ qua lời nhắc xác nhận
  * `--non-interactive`: tắt lời nhắc; yêu cầu `--scope` và `--yes`
  * `--dry-run`: in ra các hành động mà không xóa tệp


Ví dụ:

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

Ghi chú:

  * Chạy `openclaw backup create` trước nếu bạn muốn có một bản chụp có thể khôi phục trước khi xóa trạng thái cục bộ.
  * Nếu bạn bỏ qua `--scope`, `openclaw reset` sử dụng lời nhắc tương tác để chọn nội dung cần xóa.
  * `--non-interactive` chỉ hợp lệ khi cả `--scope` và `--yes` đều được đặt.


## Liên quan

  * [Tham chiếu CLI](</vi/cli>)


Was this useful?YesNo