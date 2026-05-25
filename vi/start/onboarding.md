---
title: Thiết lập ban đầu (ứng dụng macOS)
source_url: https://docs.openclaw.ai/vi/start/onboarding
scraped_at: 2026-05-25
---

Tài liệu này mô tả luồng thiết lập lần chạy đầu tiên **hiện tại**. Mục tiêu là trải nghiệm "ngày 0" mượt mà: chọn nơi Gateway chạy, kết nối xác thực, chạy trình hướng dẫn và để agent tự khởi động ban đầu. Để xem tổng quan chung về các lộ trình onboarding, hãy xem [Tổng quan onboarding](</vi/start/onboarding-overview>).

* ### Phê duyệt cảnh báo macOS

![](/assets/macos-onboarding/01-macos-warning.jpeg)
* ### Phê duyệt tìm mạng cục bộ

![](/assets/macos-onboarding/02-local-networks.jpeg)
* ### Chào mừng và thông báo bảo mật

Đọc thông báo bảo mật được hiển thị và quyết định cho phù hợp ![](/assets/macos-onboarding/03-security-notice.png)

Mô hình tin cậy bảo mật:

  * Theo mặc định, OpenClaw là một agent cá nhân: một ranh giới người vận hành đáng tin cậy.
  * Các thiết lập dùng chung/nhiều người dùng yêu cầu khóa chặt (tách ranh giới tin cậy, giữ quyền truy cập công cụ ở mức tối thiểu và làm theo [Bảo mật](</vi/gateway/security>)).
  * Onboarding cục bộ hiện mặc định các cấu hình mới thành `tools.profile: "coding"` để các thiết lập cục bộ mới vẫn giữ công cụ hệ thống tệp/runtime mà không buộc dùng hồ sơ `full` không hạn chế.
  * Nếu hooks/webhooks hoặc các nguồn nội dung không đáng tin cậy khác được bật, hãy dùng một tầng mô hình hiện đại mạnh và giữ chính sách công cụ/sandboxing nghiêm ngặt.


* ### Cục bộ so với từ xa

![](/assets/macos-onboarding/04-choose-gateway.png)

**Gateway** chạy ở đâu?

  * **Máy Mac này (chỉ cục bộ):** onboarding có thể cấu hình xác thực và ghi thông tin xác thực cục bộ.
  * **Từ xa (qua SSH/Tailnet):** onboarding **không** cấu hình xác thực cục bộ; thông tin xác thực phải tồn tại trên máy chủ gateway.
  * **Cấu hình sau:** bỏ qua thiết lập và để ứng dụng chưa được cấu hình.


* ### Quyền

Chọn các quyền bạn muốn cấp cho OpenClaw ![](/assets/macos-onboarding/05-permissions.png)

Onboarding yêu cầu các quyền TCC cần thiết cho:

  * Tự động hóa (AppleScript)
  * Thông báo
  * Trợ năng
  * Ghi màn hình
  * Micrô
  * Nhận dạng giọng nói
  * Camera
  * Vị trí


* ### CLI

* ### Trò chuyện onboarding (phiên chuyên dụng)

Sau khi thiết lập, ứng dụng mở một phiên trò chuyện onboarding chuyên dụng để agent có thể tự giới thiệu và hướng dẫn các bước tiếp theo. Điều này giữ phần hướng dẫn lần chạy đầu tiên tách biệt khỏi cuộc trò chuyện thông thường của bạn. Xem [Khởi động ban đầu](</vi/start/bootstrapping>) để biết điều gì xảy ra trên máy chủ gateway trong lần chạy agent đầu tiên.

## Liên quan

  * [Tổng quan onboarding](</vi/start/onboarding-overview>)
  * [Bắt đầu](</vi/start/getting-started>)


Was this useful?YesNo