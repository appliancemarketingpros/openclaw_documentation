---
title: Đăng nhập bằng trình duyệt
source_url: https://docs.openclaw.ai/vi/tools/browser-login
scraped_at: 2026-05-25
---

## Đăng nhập thủ công (khuyến nghị)

Khi một trang web yêu cầu đăng nhập, **hãy đăng nhập thủ công** trong hồ sơ trình duyệt **máy chủ** (trình duyệt openclaw).

**Không** cung cấp thông tin đăng nhập của bạn cho mô hình. Đăng nhập tự động thường kích hoạt các cơ chế chống bot và có thể khóa tài khoản.

Quay lại tài liệu chính về trình duyệt: [Trình duyệt](</vi/tools/browser>).

## Hồ sơ Chrome nào được sử dụng?

OpenClaw điều khiển một **hồ sơ Chrome chuyên dụng** (tên là `openclaw`, giao diện có sắc cam). Hồ sơ này tách biệt với hồ sơ trình duyệt hằng ngày của bạn.

Đối với các lệnh gọi công cụ trình duyệt của agent:

  * Lựa chọn mặc định: agent nên dùng trình duyệt `openclaw` cô lập của nó.
  * Chỉ dùng `profile="user"` khi các phiên đã đăng nhập hiện có là quan trọng và người dùng đang ở máy tính để nhấp/phê duyệt bất kỳ lời nhắc đính kèm nào.
  * Nếu bạn có nhiều hồ sơ trình duyệt người dùng, hãy chỉ định hồ sơ một cách rõ ràng thay vì đoán.


Hai cách dễ dàng để truy cập:

  1. **Yêu cầu agent mở trình duyệt** rồi tự bạn đăng nhập.
  2. **Mở qua CLI** :

bashCopy code
[code]
    openclaw browser startopenclaw browser open https://x.com
[/code]

Nếu bạn có nhiều hồ sơ, truyền `--browser-profile <name>` (mặc định là `openclaw`).

## X/Twitter: luồng khuyến nghị

  * **Đọc/tìm kiếm/chuỗi thảo luận:** dùng trình duyệt **máy chủ** (đăng nhập thủ công).
  * **Đăng cập nhật:** dùng trình duyệt **máy chủ** (đăng nhập thủ công).


## Sandboxing + quyền truy cập trình duyệt máy chủ

Các phiên trình duyệt sandbox **có nhiều khả năng hơn** kích hoạt phát hiện bot. Với X/Twitter (và các trang web nghiêm ngặt khác), hãy ưu tiên trình duyệt **máy chủ**.

Nếu agent đang ở trong sandbox, công cụ trình duyệt mặc định dùng sandbox. Để cho phép điều khiển máy chủ:

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main",        browser: {          allowHostControl: true,        },      },    },  },}
[/code]

Sau đó tự mở trình duyệt máy chủ (các lệnh gọi CLI luôn chạy trên trình duyệt máy chủ):

bashCopy code
[code]
    openclaw browser open https://x.com --browser-profile openclaw
[/code]

Các lệnh gọi công cụ `browser` của agent sau đó có thể nhắm tới máy chủ sau khi đặt `sandbox.browser.allowHostControl: true`. Ngoài ra, hãy tắt sandboxing cho agent đăng cập nhật.

## Liên quan

  * [Trình duyệt](</vi/tools/browser>)
  * [Khắc phục sự cố Browser trên Linux](</vi/tools/browser-linux-troubleshooting>)
  * [Khắc phục sự cố Browser WSL2](</vi/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo