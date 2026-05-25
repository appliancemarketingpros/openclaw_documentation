---
title: Việc loại bỏ BlueBubbles và đường dẫn iMessage imsg
source_url: https://docs.openclaw.ai/vi/announcements/bluebubbles-imessage
scraped_at: 2026-05-25
---

# Loại bỏ BlueBubbles và đường dẫn imsg iMessage

OpenClaw không còn phát hành kênh BlueBubbles. Hỗ trợ iMessage hiện chạy qua Plugin `imessage` được tích hợp sẵn, Plugin này khởi động [`imsg`](<https://github.com/steipete/imsg>) cục bộ hoặc thông qua một trình bao SSH và giao tiếp JSON-RPC qua stdin/stdout.

Nếu cấu hình của bạn vẫn chứa `channels.bluebubbles`, hãy di chuyển sang `channels.imessage`. URL tài liệu cũ `/channels/bluebubbles` chuyển hướng đến [Chuyển từ BlueBubbles](</vi/channels/imessage-from-bluebubbles>), nơi có bảng chuyển đổi cấu hình đầy đủ và danh sách kiểm tra chuyển đổi.

## Những gì đã thay đổi

  * Không có máy chủ HTTP BlueBubbles, route Webhook, mật khẩu REST, hoặc runtime Plugin BlueBubbles trong đường dẫn iMessage được OpenClaw hỗ trợ.
  * OpenClaw đọc và theo dõi Messages thông qua `imsg` trên máy Mac nơi Messages.app đã đăng nhập.
  * Gửi, nhận, lịch sử và phương tiện cơ bản sử dụng các bề mặt `imsg` thông thường và quyền macOS.
  * Các thao tác nâng cao như trả lời theo chuỗi, tapback, chỉnh sửa, hoàn tác gửi, hiệu ứng, xác nhận đã đọc, chỉ báo đang nhập và quản lý nhóm yêu cầu `imsg launch` với cầu nối API riêng tư khả dụng.
  * Gateway Linux và Windows vẫn có thể dùng iMessage bằng cách đặt `channels.imessage.cliPath` thành một trình bao SSH chạy `imsg` trên máy Mac đã đăng nhập.


## Cần làm gì

  1. Cài đặt và xác minh `imsg` trên máy Mac chạy Messages:

bashCopy code
[code]brew install steipete/tap/imsgimsg --versionimsg chats --limit 3imsg rpc --help
[/code]

  2. Cấp quyền Full Disk Access và Automation cho ngữ cảnh tiến trình chạy `imsg` và OpenClaw.

  3. Chuyển đổi cấu hình cũ:

json5Copy code
[code]{  channels: {    imessage: {      enabled: true,      cliPath: "/opt/homebrew/bin/imsg",      dmPolicy: "pairing",      allowFrom: ["+15555550123"],      groupPolicy: "allowlist",      groupAllowFrom: ["+15555550123"],      groups: {        "*": { requireMention: true },      },      includeAttachments: true,    },  },}
[/code]

  4. Khởi động lại Gateway và xác minh:

bashCopy code
[code]openclaw channels status --probe
[/code]

  5. Kiểm tra DM, nhóm, tệp đính kèm và mọi thao tác API riêng tư mà bạn phụ thuộc trước khi xóa máy chủ BlueBubbles cũ.


## Ghi chú di chuyển

  * `channels.bluebubbles.serverUrl` và `channels.bluebubbles.password` không có giá trị tương đương trong iMessage.
  * `channels.bluebubbles.allowFrom`, `groupAllowFrom`, `groups`, `includeAttachments`, gốc tệp đính kèm, giới hạn kích thước phương tiện, chia nhỏ và các nút bật/tắt thao tác có giá trị tương đương trong iMessage.
  * `channels.imessage.includeAttachments` vẫn tắt theo mặc định. Đặt rõ ràng nếu bạn muốn ảnh, ghi âm, video hoặc tệp gửi đến tiếp cận tác nhân.
  * Với `groupPolicy: "allowlist"`, sao chép khối `groups` cũ, bao gồm mọi mục ký tự đại diện `"*"`. Danh sách cho phép người gửi nhóm và sổ đăng ký nhóm là các cổng riêng biệt.
  * Các liên kết ACP khớp với `channel: "bluebubbles"` phải được đổi thành `channel: "imessage"`.
  * Khóa phiên BlueBubbles cũ không trở thành khóa phiên iMessage. Phê duyệt ghép đôi được chuyển tiếp theo handle, nhưng lịch sử hội thoại dưới khóa phiên BlueBubbles thì không.


## Xem thêm

  * [Chuyển từ BlueBubbles](</vi/channels/imessage-from-bluebubbles>)
  * [iMessage](</vi/channels/imessage>)
  * [Tham chiếu cấu hình - iMessage](</vi/gateway/config-channels#imessage>)


Was this useful?YesNo