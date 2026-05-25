---
title: Tình trạng hoạt động
source_url: https://docs.openclaw.ai/vi/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

Lấy tình trạng từ Gateway đang chạy.

## Tùy chọn

Cờ | Mặc định | Mô tả  
---|---|---  
`--json` | `false` | In JSON máy có thể đọc được thay vì văn bản.  
`--timeout <ms>` | `10000` | Thời gian chờ kết nối tính bằng mili giây.  
`--verbose` | `false` | Ghi log chi tiết. Buộc thăm dò trực tiếp và mở rộng đầu ra theo từng tác tử.  
`--debug` | `false` | Bí danh cho `--verbose`.  
  
Ví dụ:

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

Ghi chú:

  * `openclaw health` mặc định yêu cầu Gateway đang chạy cung cấp ảnh chụp nhanh tình trạng. Khi Gateway đã có ảnh chụp nhanh được lưu trong bộ nhớ đệm còn mới, nó có thể trả về payload đã lưu trong bộ nhớ đệm đó và làm mới trong nền.
  * `--verbose` buộc thăm dò trực tiếp, in chi tiết kết nối Gateway và mở rộng đầu ra dễ đọc cho người dùng trên tất cả tài khoản và tác tử đã cấu hình.
  * Đầu ra bao gồm kho lưu trữ phiên theo từng tác tử khi nhiều tác tử được cấu hình.


## Liên quan

  * [Tham chiếu CLI](</vi/cli>)
  * [Tình trạng Gateway](</vi/gateway/health>)


Was this useful?YesNo