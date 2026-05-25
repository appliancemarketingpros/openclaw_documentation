---
title: Gỡ cài đặt
source_url: https://docs.openclaw.ai/vi/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

Gỡ cài đặt dịch vụ Gateway + dữ liệu cục bộ (CLI vẫn giữ nguyên).

Tùy chọn:

  * `--service`: xóa dịch vụ Gateway
  * `--state`: xóa trạng thái và cấu hình
  * `--workspace`: xóa các thư mục workspace
  * `--app`: xóa ứng dụng macOS
  * `--all`: xóa dịch vụ, trạng thái, workspace và ứng dụng
  * `--yes`: bỏ qua lời nhắc xác nhận
  * `--non-interactive`: tắt lời nhắc; yêu cầu `--yes`
  * `--dry-run`: in các hành động mà không xóa tệp


Ví dụ:

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

Ghi chú:

  * Chạy `openclaw backup create` trước nếu bạn muốn có một bản snapshot có thể khôi phục trước khi xóa trạng thái hoặc workspace.
  * `--all` là cách viết tắt để xóa dịch vụ, trạng thái, workspace và ứng dụng cùng lúc.
  * `--non-interactive` yêu cầu `--yes`.


## Liên quan

  * [Tham chiếu CLI](</vi/cli>)
  * [Gỡ cài đặt](</vi/install/uninstall>)


Was this useful?YesNo