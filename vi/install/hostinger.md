---
title: Hostinger
source_url: https://docs.openclaw.ai/vi/install/hostinger
scraped_at: 2026-05-25
---

Chạy một OpenClaw Gateway bền vững trên [Hostinger](<https://www.hostinger.com/openclaw>) thông qua triển khai được quản lý bằng **1 cú nhấp** hoặc cài đặt trên **VPS**.

## Điều kiện tiên quyết

  * Tài khoản Hostinger ([đăng ký](<https://www.hostinger.com/openclaw>))
  * Khoảng 5-10 phút


## Tùy chọn A: OpenClaw bằng 1 cú nhấp

Cách nhanh nhất để bắt đầu. Hostinger xử lý hạ tầng, Docker và cập nhật tự động.

* ### Mua và khởi chạy

  1. Từ [trang Hostinger OpenClaw](<https://www.hostinger.com/openclaw>), chọn một gói OpenClaw được quản lý và hoàn tất thanh toán.


* ### Chọn kênh nhắn tin

Chọn một hoặc nhiều kênh để kết nối:

  * **WhatsApp** \-- quét mã QR hiển thị trong trình hướng dẫn thiết lập.
  * **Telegram** \-- dán mã thông báo bot từ [BotFather](<https://t.me/BotFather>).


* ### Hoàn tất cài đặt

Nhấp **Hoàn tất** để triển khai phiên bản. Khi đã sẵn sàng, truy cập bảng điều khiển OpenClaw từ **Tổng quan OpenClaw** trong hPanel.

## Tùy chọn B: OpenClaw trên VPS

Kiểm soát máy chủ của bạn nhiều hơn. Hostinger triển khai OpenClaw qua Docker trên VPS của bạn và bạn quản lý nó thông qua **Trình quản lý Docker** trong hPanel.

* ### Mua VPS

  1. Từ [trang Hostinger OpenClaw](<https://www.hostinger.com/openclaw>), chọn một gói OpenClaw trên VPS và hoàn tất thanh toán.


* ### Cấu hình OpenClaw

Sau khi VPS được cấp phát, hãy điền các trường cấu hình:

  * **Mã thông báo Gateway** \-- được tạo tự động; lưu lại để sử dụng sau.
  * **Số WhatsApp** \-- số của bạn kèm mã quốc gia (không bắt buộc).
  * **Mã thông báo bot Telegram** \-- từ [BotFather](<https://t.me/BotFather>) (không bắt buộc).
  * **Khóa API** \-- chỉ cần nếu bạn không chọn tín dụng AI sẵn dùng trong quá trình thanh toán.


* ### Khởi động OpenClaw

Nhấp **Triển khai**. Khi đã chạy, mở bảng điều khiển OpenClaw từ hPanel bằng cách nhấp vào **Mở**.

Nhật ký, khởi động lại và cập nhật được quản lý trực tiếp từ giao diện Trình quản lý Docker trong hPanel. Để cập nhật, nhấn **Cập nhật** trong Trình quản lý Docker và thao tác đó sẽ kéo hình ảnh mới nhất.

## Xác minh thiết lập của bạn

Gửi "Hi" tới trợ lý của bạn trên kênh bạn đã kết nối. OpenClaw sẽ trả lời và hướng dẫn bạn qua các tùy chọn ban đầu.

## Khắc phục sự cố

**Bảng điều khiển không tải** \-- Chờ vài phút để container hoàn tất cấp phát. Kiểm tra nhật ký Trình quản lý Docker trong hPanel.

**Container Docker liên tục khởi động lại** \-- Mở nhật ký Trình quản lý Docker và tìm lỗi cấu hình (thiếu mã thông báo, khóa API không hợp lệ).

**Bot Telegram không phản hồi** \-- Gửi trực tiếp tin nhắn mã ghép nối của bạn từ Telegram dưới dạng một tin nhắn bên trong cuộc trò chuyện OpenClaw để hoàn tất kết nối.

## Bước tiếp theo

  * [Kênh](</vi/channels>) \-- kết nối Telegram, WhatsApp, Discord và nhiều kênh khác
  * [Cấu hình Gateway](</vi/gateway/configuration>) \-- tất cả tùy chọn cấu hình


## Liên quan

  * [Tổng quan cài đặt](</vi/install>)
  * [Lưu trữ VPS](</vi/vps>)
  * [DigitalOcean](</vi/install/digitalocean>)


Was this useful?YesNo