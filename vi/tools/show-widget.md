---
title: Hiển thị tiện ích con
source_url: https://docs.openclaw.ai/vi/tools/show-widget
scraped_at: 2026-07-13
---

CapabilitiesTools

`show_widget` kết xuất nội tuyến một đoạn SVG hoặc HTML độc lập trong bản ghi cuộc trò chuyện của Control UI. Plugin Canvas đi kèm sở hữu công cụ này và lưu trữ mỗi kết quả dưới dạng tài liệu Canvas cùng nguồn.

Công cụ chỉ khả dụng khi máy khách Gateway khởi tạo khai báo khả năng `inline-widgets`. Control UI tự động khai báo khả năng này. Các lượt chạy trên kênh như Telegram và WhatsApp không nhận được `show_widget`.

Việc truyền tải khả năng áp dụng cho các phần phụ trợ mô hình nhúng, máy chủ ứng dụng Codex và dựa trên CLI. Các bên gọi MCP được xác thực bằng quyền cấp và các bên gọi trực tiếp công cụ qua HTTP vẫn mặc định từ chối vì không khai báo khả năng của máy khách.

## Sử dụng công cụ

Tác tử cung cấp hai chuỗi bắt buộc:

Tiêu đề ngắn hiển thị cùng bản xem trước nội tuyến và trong tiêu đề của tài liệu được lưu trữ.

Đoạn SVG hoặc HTML độc lập. Dữ liệu đầu vào bắt đầu bằng `<svg` sau khi loại bỏ khoảng trắng thừa sẽ được kết xuất ở chế độ SVG; mọi dữ liệu đầu vào khác được xử lý như một đoạn HTML. Độ dài tối đa: 262.144 ký tự.

Kết quả công cụ bao gồm một định danh bản xem trước Canvas, nhờ đó trò chuyện web kết xuất tiện ích trực tiếp từ lệnh gọi công cụ và khôi phục tiện ích sau khi tải lại lịch sử. Các bản ghi không kết xuất bản xem trước vẫn hiển thị đường dẫn Canvas được lưu trữ.

## Bảo mật và lưu trữ

Tài liệu tiện ích sử dụng Chính sách bảo mật nội dung nghiêm ngặt: cho phép kiểu và tập lệnh nội tuyến, hình ảnh có thể sử dụng URL `data:`, còn các yêu cầu truy xuất và tải tài nguyên bên ngoài bị chặn. Hãy đặt toàn bộ mã đánh dấu, kiểu, tập lệnh và dữ liệu hình ảnh bên trong `widget_code`.

iframe luôn bỏ qua `allow-same-origin`, ngay cả khi chế độ nhúng toàn cục của Control UI là `trusted`, vì vậy tập lệnh của tiện ích không thể đọc nguồn của ứng dụng mẹ. Máy chủ Canvas cũng phân phối tài liệu tiện ích với tiêu đề phản hồi `Content-Security-Policy: sandbox allow-scripts`, vì vậy khi mở trực tiếp URL được lưu trữ, tiện ích vẫn chạy trong một nguồn không trong suốt thay vì nguồn của Control UI. Cơ chế hộp cát của trình duyệt không ngăn tập lệnh điều hướng iframe của chính nó; chỉ kết xuất mã tiện ích mà bạn sẵn sàng thực thi trong khung cách ly đó.

iframe cũng tuân theo [`gateway.controlUi.embedSandbox`](</vi/web/control-ui#hosted-embeds>). Cấp `scripts` mặc định hỗ trợ các tiện ích tương tác trong khi vẫn duy trì khả năng cách ly nguồn.

Canvas lưu giữ tối đa 32 tiện ích cho mỗi phiên (hoặc cho mỗi tác tử khi không có phiên). Việc tạo thêm tiện ích sẽ xóa tài liệu cũ nhất trong phạm vi đó.

## Liên quan

  * [Nội dung nhúng được lưu trữ của Control UI](</vi/web/control-ui#hosted-embeds>)
  * [Plugin Canvas](</vi/plugins/reference/canvas>)
  * [Khả năng máy khách của giao thức Gateway](</vi/gateway/protocol#client-capabilities>)


Was this useful?YesNo

Open issue