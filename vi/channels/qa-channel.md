---
title: Kênh QA
source_url: https://docs.openclaw.ai/vi/channels/qa-channel
scraped_at: 2026-05-25
---

`qa-channel` là phương thức truyền tải thông điệp tổng hợp được đóng gói sẵn cho QA tự động của OpenClaw. Đây không phải là kênh sản xuất - nó tồn tại để kiểm thử cùng ranh giới Plugin kênh mà các phương thức truyền tải thật sử dụng, đồng thời giữ trạng thái xác định và có thể kiểm tra đầy đủ.

## Chức năng

  * Ngữ pháp mục tiêu kiểu Slack: 
    * `dm:<user>`
    * `channel:<room>`
    * `group:<room>`
    * `thread:<room>/<thread>`
  * Các cuộc trò chuyện `channel:` và `group:` dùng chung được hiển thị cho agent dưới dạng lượt phòng nhóm/kênh, nên chúng kiểm thử cùng chính sách định tuyến trả lời hiển thị và công cụ thông điệp được Discord, Slack, Telegram và các phương thức truyền tải tương tự sử dụng.
  * Bus tổng hợp dựa trên HTTP để chèn thông điệp đến, ghi lại bản chép lời đi, tạo luồng, phản ứng, chỉnh sửa, xóa và các hành động tìm kiếm/đọc.
  * Trình chạy tự kiểm tra phía host ghi báo cáo Markdown vào `.artifacts/qa-e2e/`.


## Cấu hình

jsonCopy code
[code]
    {  "channels": {    "qa-channel": {      "baseUrl": "http://127.0.0.1:43123",      "botUserId": "openclaw",      "botDisplayName": "OpenClaw QA",      "allowFrom": ["*"],      "pollTimeoutMs": 1000    }  }}
[/code]

Khóa tài khoản:

  * `enabled` \- công tắc chính cho tài khoản này.
  * `name` \- nhãn hiển thị tùy chọn.
  * `baseUrl` \- URL bus tổng hợp.
  * `botUserId` \- id người dùng bot kiểu Matrix được dùng trong ngữ pháp mục tiêu.
  * `botDisplayName` \- tên hiển thị cho thông điệp đi.
  * `pollTimeoutMs` \- khoảng chờ long-poll. Số nguyên từ 100 đến 30000.
  * `allowFrom` \- danh sách cho phép người gửi (id người dùng hoặc `"*"`). Tin nhắn trực tiếp và chính sách nhóm trong danh sách cho phép đều dùng các id người gửi tổng hợp này.
  * `groupPolicy` \- chính sách phòng dùng chung: `"open"` (mặc định), `"allowlist"`, hoặc `"disabled"`.
  * `groupAllowFrom` \- danh sách cho phép người gửi trong phòng dùng chung, tùy chọn. Khi bị bỏ qua dưới `"allowlist"`, QA Channel sẽ dùng lại `allowFrom`.
  * `groups.<room>.requireMention` \- yêu cầu nhắc đến bot trước khi trả lời trong một phòng nhóm/kênh cụ thể. `groups."*"` đặt giá trị mặc định.
  * `defaultTo` \- mục tiêu dự phòng khi không có mục tiêu nào được cung cấp.
  * `actions.messages` / `actions.reactions` / `actions.search` / `actions.threads` \- kiểm soát công cụ theo từng hành động.


Khóa đa tài khoản ở cấp cao nhất:

  * `accounts` \- bản ghi các ghi đè theo từng tài khoản được đặt tên, khóa theo id tài khoản.
  * `defaultAccount` \- id tài khoản ưu tiên khi có nhiều tài khoản được cấu hình.


## Trình chạy

Tự kiểm tra phía host (ghi báo cáo Markdown dưới `.artifacts/qa-e2e/`):

bashCopy code
[code]
    pnpm qa:e2e
[/code]

Lệnh này định tuyến qua `qa-lab`, khởi động bus QA trong repo, khởi động lát runtime `qa-channel` được đóng gói sẵn, và chạy một bài tự kiểm tra xác định.

Bộ kịch bản đầy đủ dựa trên repo:

bashCopy code
[code]
    pnpm openclaw qa suite
[/code]

Chạy các kịch bản song song trên làn QA gateway. Xem [Tổng quan QA](</vi/concepts/qa-e2e-automation>) để biết các kịch bản, hồ sơ và chế độ nhà cung cấp.

Trang QA dựa trên Docker (gateway + giao diện trình gỡ lỗi QA Lab trong một stack):

bashCopy code
[code]
    pnpm qa:lab:up
[/code]

Xây dựng trang QA, khởi động gateway dựa trên Docker + stack QA Lab và in URL QA Lab. Từ đó, bạn có thể chọn kịch bản, chọn làn mô hình, khởi chạy từng lượt chạy riêng lẻ và xem kết quả trực tiếp. Trình gỡ lỗi QA Lab tách biệt với gói Control UI được phát hành.

## Liên quan

  * [Tổng quan QA](</vi/concepts/qa-e2e-automation>) \- toàn bộ stack, bộ điều hợp truyền tải, biên soạn kịch bản
  * [Matrix QA](</vi/concepts/qa-matrix>) \- ví dụ về trình chạy truyền tải trực tiếp điều khiển một kênh thật
  * [Ghép nối](</vi/channels/pairing>)
  * [Nhóm](</vi/channels/groups>)
  * [Tổng quan kênh](</vi/channels>)


Was this useful?YesNo