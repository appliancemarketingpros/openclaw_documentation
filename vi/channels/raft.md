---
title: Raft
source_url: https://docs.openclaw.ai/vi/channels/raft
scraped_at: 2026-06-29
---

ChannelsDeveloper and self-hosted

Hỗ trợ Raft kết nối một tác nhân OpenClaw với Raft External Agent thông qua Raft CLI cục bộ. Raft gửi các gợi ý đánh thức đã xác thực đến Gateway. Sau đó tác nhân dùng Raft CLI để kiểm tra và gửi tin nhắn.

## Cài đặt

Raft là một Plugin bên ngoài chính thức. Cài đặt trên máy chủ Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/raftopenclaw gateway restart
[/code]

Chi tiết: [Plugin](</vi/tools/plugin>)

## Điều kiện tiên quyết

  * Một không gian làm việc Raft có External Agent.
  * Raft CLI được cài đặt trên cùng máy chủ với OpenClaw Gateway.
  * Một hồ sơ Raft CLI đã đăng nhập và được liên kết với External Agent đó.


Plugin không lưu trữ thông tin xác thực Raft. Raft CLI giữ xác thực đó trong hồ sơ riêng của nó.

## Cấu hình

Đặt hồ sơ trong cấu hình:

json5Copy code
[code]
    {  channels: {    raft: {      enabled: true,      profile: "openclaw",    },  },}
[/code]

Với tài khoản mặc định, bạn cũng có thể đặt `RAFT_PROFILE` trong môi trường Gateway:

bashCopy code
[code]
    RAFT_PROFILE=openclaw
[/code]

Dùng tài khoản có tên khi một Gateway kết nối với nhiều Raft External Agent:

json5Copy code
[code]
    {  channels: {    raft: {      accounts: {        support: {          profile: "support-agent",        },        engineering: {          profile: "engineering-agent",        },      },    },  },}
[/code]

Luồng thiết lập tương tác ghi lại cùng hồ sơ:

bashCopy code
[code]
    openclaw channels setup raft
[/code]

## Cách hoạt động

Khi Gateway khởi động, Plugin:

  1. Mở một điểm cuối HTTP đánh thức chỉ cho loopback trên một cổng tạm thời.
  2. Khởi động `raft --profile <profile> agent bridge` với điểm cuối đó và một token riêng cho từng tiến trình.
  3. Chỉ chấp nhận các gợi ý đánh thức đã xác thực, không có nội dung, có định danh chống phát lại từ cầu nối cục bộ.
  4. Yêu cầu một trong các giá trị `eventId`, `attemptId`, `messageId`, `delivery_id`, `wake_id`, hoặc `id`.
  5. Khử trùng lặp các lượt phân phối đánh thức được thử lại gần đây theo id sự kiện cầu nối, bao gồm cả sau khi Gateway khởi động lại.
  6. Trả về một phiên thời gian chạy ổn định cho cầu nối hiện tại và một lô rút hoạt động trống cho giao thức Raft CLI.
  7. Khởi động một lượt tác nhân OpenClaw được tuần tự hóa cho mỗi lần đánh thức được chấp nhận.


Cầu nối sở hữu việc thử lại và kết nối lại phân phối của Raft. Lượt OpenClaw chỉ nhận một thông báo đánh thức, không phải nội dung tin nhắn Raft được sao chép. Nó dùng CLI để đọc các tin nhắn đang chờ và gửi phản hồi:

bashCopy code
[code]
    raft --profile openclaw message checkraft --profile openclaw message send
[/code]

## Xác minh

Kiểm tra rằng OpenClaw có thể tìm thấy CLI và có hồ sơ đã cấu hình:

bashCopy code
[code]
    openclaw channels status --probeopenclaw plugins inspect raft --runtime --json
[/code]

Sau đó gửi một tin nhắn đến Raft External Agent. Nhật ký Gateway sẽ hiển thị cầu nối Raft khởi động, tiếp theo là một lần đánh thức đến. Tác nhân nên dùng hồ sơ Raft đã cấu hình để kiểm tra các tin nhắn đang chờ.

## Khắc phục sự cố

Raft CLI is missing

Cài đặt Raft CLI trên máy chủ Gateway và làm cho `raft` khả dụng trên `PATH` của dịch vụ. Xác minh bằng `raft --help`, rồi khởi động lại Gateway.

The bridge exits immediately

Xác minh hồ sơ đã cấu hình đã đăng nhập và thuộc về Raft External Agent dự kiến. Chạy trực tiếp `raft --profile <profile> agent bridge` để xem chẩn đoán của CLI.

A wake arrives but no Raft response is sent

Điều này là dự kiến khi tác nhân không gọi Raft CLI. Cầu nối đánh thức không mang nội dung tin nhắn hoặc phản hồi cuối tự động. Kiểm tra chính sách công cụ của tác nhân và đảm bảo nó có thể chạy `raft --profile <profile> message check` và `message send`.

## Tham khảo

  * [Raft](<https://raft.build/>)
  * [Tài liệu Raft](<https://docs.raft.build/welcome/>)
  * [Tích hợp Hermes Raft](<https://hermes-agent.nousresearch.com/docs/user-guide/messaging/raft>)


Was this useful?YesNo

Open issue