---
title: Nhật ký
source_url: https://docs.openclaw.ai/vi/cli/logs
scraped_at: 2026-05-25
---

# `openclaw logs`

Theo dõi phần cuối nhật ký tệp Gateway qua RPC (hoạt động ở chế độ từ xa).

Liên quan:

  * Tổng quan về ghi nhật ký: [Ghi nhật ký](</vi/logging>)
  * CLI Gateway: [gateway](</vi/cli/gateway>)


## Tùy chọn

  * `--limit <n>`: số dòng nhật ký tối đa cần trả về (mặc định `200`)
  * `--max-bytes <n>`: số byte tối đa cần đọc từ tệp nhật ký (mặc định `250000`)
  * `--follow`: theo dõi luồng nhật ký
  * `--interval <ms>`: khoảng thời gian thăm dò khi đang theo dõi (mặc định `1000`)
  * `--json`: xuất các sự kiện JSON được phân tách theo dòng
  * `--plain`: đầu ra văn bản thuần không có định dạng kiểu
  * `--no-color`: tắt màu ANSI
  * `--local-time`: hiển thị dấu thời gian theo múi giờ cục bộ của bạn


## Tùy chọn RPC Gateway dùng chung

`openclaw logs` cũng chấp nhận các cờ máy khách Gateway tiêu chuẩn:

  * `--url <url>`: URL WebSocket của Gateway
  * `--token <token>`: token Gateway
  * `--timeout <ms>`: thời gian chờ tính bằng ms (mặc định `30000`)
  * `--expect-final`: chờ phản hồi cuối cùng khi lệnh gọi Gateway được hỗ trợ bởi agent


Khi bạn truyền `--url`, CLI không tự động áp dụng thông tin đăng nhập từ cấu hình hoặc môi trường. Hãy thêm `--token` rõ ràng nếu Gateway đích yêu cầu xác thực.

## Ví dụ

bashCopy code
[code]
    openclaw logsopenclaw logs --followopenclaw logs --follow --interval 2000openclaw logs --limit 500 --max-bytes 500000openclaw logs --jsonopenclaw logs --plainopenclaw logs --no-coloropenclaw logs --limit 500openclaw logs --local-timeopenclaw logs --follow --local-timeopenclaw logs --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
[/code]

## Ghi chú

  * Dùng `--local-time` để hiển thị dấu thời gian theo múi giờ cục bộ của bạn.
  * Nếu Gateway local loopback ngầm định yêu cầu ghép đôi, đóng trong khi kết nối, hoặc hết thời gian chờ trước khi `logs.tail` trả lời, `openclaw logs` sẽ tự động chuyển sang nhật ký tệp Gateway đã cấu hình. Các đích `--url` rõ ràng không dùng cơ chế dự phòng này.
  * Khi dùng `--follow`, các lần ngắt kết nối gateway tạm thời (WebSocket đóng, hết thời gian chờ, rớt kết nối) sẽ kích hoạt tự động kết nối lại với backoff theo cấp số nhân (tối đa 8 lần thử lại, giới hạn 30 giây giữa các lần thử). Một cảnh báo được in ra stderr ở mỗi lần thử lại, và thông báo `[logs] gateway reconnected` được in sau khi một lần thăm dò thành công. Ở chế độ `--json`, cả cảnh báo thử lại và chuyển tiếp kết nối lại đều được phát ra dưới dạng bản ghi `{"type":"notice"}` trên stderr. Các lỗi không thể khôi phục (lỗi xác thực, cấu hình sai) vẫn thoát ngay lập tức.


## Liên quan

  * [Tài liệu tham chiếu CLI](</vi/cli>)
  * [Ghi nhật ký Gateway](</vi/gateway/logging>)


Was this useful?YesNo