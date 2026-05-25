---
title: Khởi tạo tác nhân
source_url: https://docs.openclaw.ai/vi/start/bootstrapping
scraped_at: 2026-05-25
---

Khởi tạo ban đầu là nghi thức **chạy lần đầu** chuẩn bị không gian làm việc của tác nhân và thu thập thông tin nhận dạng. Việc này diễn ra sau quy trình thiết lập ban đầu, khi tác nhân khởi động lần đầu tiên.

## Khởi tạo ban đầu thực hiện những gì

Trong lần chạy tác nhân đầu tiên, OpenClaw khởi tạo không gian làm việc (mặc định `~/.openclaw/workspace`):

  * Tạo sẵn `AGENTS.md`, `BOOTSTRAP.md`, `IDENTITY.md`, `USER.md`.
  * Chạy một nghi thức hỏi đáp ngắn (mỗi lần một câu hỏi).
  * Ghi thông tin nhận dạng + tùy chọn vào `IDENTITY.md`, `USER.md`, `SOUL.md`.
  * Xóa `BOOTSTRAP.md` khi hoàn tất để quy trình chỉ chạy một lần.


Đối với các lượt chạy mô hình nhúng/cục bộ, OpenClaw giữ `BOOTSTRAP.md` ngoài ngữ cảnh hệ thống đặc quyền. Trong lần chạy đầu tiên tương tác chính, nó vẫn truyền nội dung tệp trong lời nhắc người dùng để các mô hình không gọi công cụ `read` một cách đáng tin cậy vẫn có thể hoàn tất nghi thức. Nếu lượt chạy hiện tại không thể truy cập an toàn vào không gian làm việc, tác nhân sẽ nhận được một ghi chú khởi tạo giới hạn thay vì một lời chào chung chung.

## Bỏ qua khởi tạo ban đầu

Để bỏ qua bước này cho một không gian làm việc đã được tạo sẵn, hãy chạy `openclaw onboard --skip-bootstrap`.

## Nơi quy trình chạy

Khởi tạo ban đầu luôn chạy trên **máy chủ Gateway**. Nếu ứng dụng macOS kết nối với một Gateway từ xa, không gian làm việc và các tệp khởi tạo ban đầu nằm trên máy từ xa đó.

## Tài liệu liên quan

  * Quy trình thiết lập ban đầu ứng dụng macOS: [Quy trình thiết lập ban đầu](</vi/start/onboarding>)
  * Bố cục không gian làm việc: [Không gian làm việc của tác nhân](</vi/concepts/agent-workspace>)


Was this useful?YesNo