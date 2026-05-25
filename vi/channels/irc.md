---
title: IRC
source_url: https://docs.openclaw.ai/vi/channels/irc
scraped_at: 2026-05-25
---

Sử dụng IRC khi bạn muốn dùng OpenClaw trong các kênh cổ điển (`#room`) và tin nhắn trực tiếp. IRC được cung cấp dưới dạng Plugin tích hợp, nhưng được cấu hình trong cấu hình chính bên dưới `channels.irc`.

## Bắt đầu nhanh

  1. Bật cấu hình IRC trong `~/.openclaw/openclaw.json`.
  2. Thiết lập ít nhất:

json5Copy code
[code]
    {  channels: {    irc: {      enabled: true,      host: "irc.example.com",      port: 6697,      tls: true,      nick: "openclaw-bot",      channels: ["#openclaw"],    },  },}
[/code]

Nên dùng một máy chủ IRC riêng cho việc phối hợp bot. Nếu bạn chủ ý dùng một mạng IRC công khai, các lựa chọn phổ biến gồm Libera.Chat, OFTC và Snoonet. Tránh các kênh công khai dễ đoán cho lưu lượng backchannel của bot hoặc swarm.

  3. Khởi động/khởi động lại Gateway:

bashCopy code
[code]
    openclaw gateway run
[/code]

## Mặc định bảo mật

  * IRC dùng socket TCP/TLS thô bên ngoài định tuyến forward proxy do operator của OpenClaw quản lý. Trong các triển khai yêu cầu toàn bộ lưu lượng đi ra đi qua forward proxy đó, đặt `channels.irc.enabled=false` trừ khi lưu lượng IRC trực tiếp được phê duyệt rõ ràng.
  * `channels.irc.dmPolicy` mặc định là `"pairing"`.
  * `channels.irc.groupPolicy` mặc định là `"allowlist"`.
  * Với `groupPolicy="allowlist"`, đặt `channels.irc.groups` để định nghĩa các kênh được phép.
  * Dùng TLS (`channels.irc.tls=true`) trừ khi bạn chủ ý chấp nhận truyền tải văn bản thuần.


## Kiểm soát truy cập

Có hai "cổng" riêng biệt cho kênh IRC:

  1. **Truy cập kênh** (`groupPolicy` \+ `groups`): bot có chấp nhận tin nhắn từ một kênh hay không.
  2. **Truy cập người gửi** (`groupAllowFrom` / `groups["#channel"].allowFrom` theo từng kênh): ai được phép kích hoạt bot bên trong kênh đó.


Khóa cấu hình:

  * Allowlist DM (quyền truy cập người gửi DM): `channels.irc.allowFrom`
  * Allowlist người gửi nhóm (quyền truy cập người gửi kênh): `channels.irc.groupAllowFrom`
  * Điều khiển theo từng kênh (quy tắc kênh + người gửi + nhắc tên): `channels.irc.groups["#channel"]`
  * `channels.irc.groupPolicy="open"` cho phép các kênh chưa cấu hình (**mặc định vẫn bị chặn bởi yêu cầu nhắc tên**)


Các mục allowlist nên dùng danh tính người gửi ổn định (`nick!user@host`). Khớp nick trần có thể thay đổi và chỉ được bật khi `channels.irc.dangerouslyAllowNameMatching: true`.

### Lỗi thường gặp: `allowFrom` dành cho DM, không phải kênh

Nếu bạn thấy log như:

  * `irc: drop group sender alice!ident@host (policy=allowlist)`


...điều đó nghĩa là người gửi không được phép đối với tin nhắn **nhóm/kênh**. Sửa bằng một trong hai cách:

  * đặt `channels.irc.groupAllowFrom` (toàn cục cho tất cả kênh), hoặc
  * đặt allowlist người gửi theo từng kênh: `channels.irc.groups["#channel"].allowFrom`


Ví dụ (cho phép bất kỳ ai trong `#tuirc-dev` nói chuyện với bot):

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "allowlist",      groups: {        "#tuirc-dev": { allowFrom: ["*"] },      },    },  },}
[/code]

## Kích hoạt trả lời (nhắc tên)

Ngay cả khi một kênh được phép (qua `groupPolicy` \+ `groups`) và người gửi được phép, OpenClaw mặc định dùng **cổng nhắc tên** trong ngữ cảnh nhóm.

Điều đó nghĩa là bạn có thể thấy log như `drop channel … (missing-mention)` trừ khi tin nhắn chứa mẫu nhắc tên khớp với bot.

Để bot trả lời trong một kênh IRC **mà không cần nhắc tên** , hãy tắt cổng nhắc tên cho kênh đó:

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "allowlist",      groups: {        "#tuirc-dev": {          requireMention: false,          allowFrom: ["*"],        },      },    },  },}
[/code]

Hoặc để cho phép **tất cả** kênh IRC (không có allowlist theo từng kênh) và vẫn trả lời mà không cần nhắc tên:

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "open",      groups: {        "*": { requireMention: false, allowFrom: ["*"] },      },    },  },}
[/code]

## Ghi chú bảo mật (khuyến nghị cho kênh công khai)

Nếu bạn cho phép `allowFrom: ["*"]` trong một kênh công khai, bất kỳ ai cũng có thể prompt bot. Để giảm rủi ro, hãy hạn chế công cụ cho kênh đó.

### Cùng công cụ cho mọi người trong kênh

json5Copy code
[code]
    {  channels: {    irc: {      groups: {        "#tuirc-dev": {          allowFrom: ["*"],          tools: {            deny: ["group:runtime", "group:fs", "gateway", "nodes", "cron", "browser"],          },        },      },    },  },}
[/code]

### Công cụ khác nhau theo từng người gửi (owner có nhiều quyền hơn)

Dùng `toolsBySender` để áp dụng chính sách nghiêm ngặt hơn cho `"*"` và chính sách nới lỏng hơn cho nick của bạn:

json5Copy code
[code]
    {  channels: {    irc: {      groups: {        "#tuirc-dev": {          allowFrom: ["*"],          toolsBySender: {            "*": {              deny: ["group:runtime", "group:fs", "gateway", "nodes", "cron", "browser"],            },            "id:eigen": {              deny: ["gateway", "nodes", "cron"],            },          },        },      },    },  },}
[/code]

Ghi chú:

  * Khóa `toolsBySender` nên dùng `id:` cho giá trị danh tính người gửi IRC: `id:eigen` hoặc `id:eigen!~eigen@174.127.248.171` để khớp chặt hơn.
  * Các khóa cũ không có tiền tố vẫn được chấp nhận và chỉ được khớp dưới dạng `id:`.
  * Chính sách người gửi khớp đầu tiên sẽ thắng; `"*"` là phương án dự phòng ký tự đại diện.


Để biết thêm về truy cập nhóm so với cổng nhắc tên (và cách chúng tương tác), xem: [/channels/groups](</vi/channels/groups>).

## NickServ

Để định danh với NickServ sau khi kết nối:

json5Copy code
[code]
    {  channels: {    irc: {      nickserv: {        enabled: true,        service: "NickServ",        password: "your-nickserv-password",      },    },  },}
[/code]

Đăng ký một lần tùy chọn khi kết nối:

json5Copy code
[code]
    {  channels: {    irc: {      nickserv: {        register: true,        registerEmail: "bot@example.com",      },    },  },}
[/code]

Tắt `register` sau khi nick đã được đăng ký để tránh các lần thử REGISTER lặp lại.

## Biến môi trường

Tài khoản mặc định hỗ trợ:

  * `IRC_HOST`
  * `IRC_PORT`
  * `IRC_TLS`
  * `IRC_NICK`
  * `IRC_USERNAME`
  * `IRC_REALNAME`
  * `IRC_PASSWORD`
  * `IRC_CHANNELS` (phân tách bằng dấu phẩy)
  * `IRC_NICKSERV_PASSWORD`
  * `IRC_NICKSERV_REGISTER_EMAIL`


Không thể đặt `IRC_HOST` từ `.env` của workspace; xem [Tệp `.env` của workspace](</vi/gateway/security>).

## Khắc phục sự cố

  * Nếu bot kết nối nhưng không bao giờ trả lời trong kênh, hãy xác minh `channels.irc.groups` **và** xem cổng nhắc tên có đang loại bỏ tin nhắn không (`missing-mention`). Nếu bạn muốn bot trả lời mà không cần ping, đặt `requireMention:false` cho kênh.
  * Nếu đăng nhập thất bại, hãy xác minh nick còn khả dụng và mật khẩu máy chủ.
  * Nếu TLS thất bại trên một mạng tùy chỉnh, hãy xác minh host/port và thiết lập chứng chỉ.


## Liên quan

  * [Tổng quan về kênh](</vi/channels>) — tất cả kênh được hỗ trợ
  * [Ghép cặp](</vi/channels/pairing>) — xác thực DM và luồng ghép cặp
  * [Nhóm](</vi/channels/groups>) — hành vi chat nhóm và cổng nhắc tên
  * [Định tuyến kênh](</vi/channels/channel-routing>) — định tuyến phiên cho tin nhắn
  * [Bảo mật](</vi/gateway/security>) — mô hình truy cập và gia cố bảo mật


Was this useful?YesNo