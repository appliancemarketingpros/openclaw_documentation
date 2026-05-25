---
title: Thiết lập
source_url: https://docs.openclaw.ai/vi/cli/setup
scraped_at: 2026-05-25
---

# `openclaw setup`

Khởi tạo cấu hình cơ sở và workspace của agent. Khi có bất kỳ cờ onboarding nào, lệnh này cũng chạy trình hướng dẫn.

## Tùy chọn

Cờ | Mô tả  
---|---  
`--workspace <dir>` | Thư mục workspace của agent (mặc định `~/.openclaw/workspace`; được lưu dưới dạng `agents.defaults.workspace`).  
`--wizard` | Chạy onboarding tương tác.  
`--non-interactive` | Chạy onboarding mà không có lời nhắc.  
`--mode <mode>` | Chế độ onboarding: `local` hoặc `remote`.  
`--import-from <provider>` | Nhà cung cấp di chuyển sẽ chạy trong quá trình onboarding.  
`--import-source <path>` | Thư mục home của agent nguồn cho `--import-from`.  
`--import-secrets` | Nhập các bí mật được hỗ trợ trong quá trình di chuyển onboarding.  
`--remote-url <url>` | URL WebSocket của Gateway từ xa.  
`--remote-token <token>` | Token Gateway từ xa (tùy chọn).  
  
### Tự động kích hoạt trình hướng dẫn

`openclaw setup` chạy trình hướng dẫn khi bất kỳ cờ nào sau đây được chỉ định rõ ràng, ngay cả khi không có `--wizard`:

`--wizard`, `--non-interactive`, `--mode`, `--import-from`, `--import-source`, `--import-secrets`, `--remote-url`, `--remote-token`.

## Ví dụ

bashCopy code
[code]
    openclaw setupopenclaw setup --workspace ~/.openclaw/workspaceopenclaw setup --wizardopenclaw setup --wizard --import-from hermes --import-source ~/.hermesopenclaw setup --non-interactive --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
[/code]

## Ghi chú

  * `openclaw setup` thuần túy khởi tạo cấu hình và workspace mà không chạy toàn bộ luồng onboarding.
  * Sau setup thuần túy, chạy `openclaw onboard` để có hành trình được hướng dẫn đầy đủ, `openclaw configure` để thay đổi có mục tiêu, hoặc `openclaw channels add` để thêm tài khoản kênh.
  * Nếu phát hiện trạng thái Hermes, onboarding tương tác có thể tự động đề xuất di chuyển. Onboarding nhập yêu cầu setup mới; sử dụng [Di chuyển](</vi/cli/migrate>) cho các kế hoạch chạy thử, bản sao lưu và chế độ ghi đè bên ngoài onboarding.


## Liên quan

  * [Tham chiếu CLI](</vi/cli>)
  * [Onboarding (CLI)](</vi/start/wizard>)
  * [Bắt đầu](</vi/start/getting-started>)
  * [Tổng quan cài đặt](</vi/install>)


Was this useful?YesNo