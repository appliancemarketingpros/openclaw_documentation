---
title: Sự kiện môi trường trong phòng
source_url: https://docs.openclaw.ai/vi/channels/ambient-room-events
scraped_at: 2026-06-29
---

ChannelsConfiguration

Sự kiện phòng nền cho phép OpenClaw xử lý các cuộc trò chuyện nhóm hoặc kênh không nhắc đến tác tử dưới dạng ngữ cảnh thầm lặng. Tác tử có thể cập nhật bộ nhớ và trạng thái phiên, nhưng phòng vẫn im lặng trừ khi tác tử gọi rõ ràng công cụ `message`.

Với các cuộc trò chuyện nhóm luôn bật, đây là chế độ được khuyến nghị: kết hợp `messages.groupChat.unmentionedInbound: "room_event"` với `messages.groupChat.visibleReplies: "message_tool"`. Dùng chế độ này khi tác tử nên lắng nghe, quyết định khi nào phản hồi là hữu ích, và tránh mẫu lời nhắc cũ yêu cầu trả lời `NO_REPLY`.

Hiện được hỗ trợ: kênh guild Discord, kênh Slack và kênh riêng tư Slack, tin nhắn trực tiếp nhiều người trên Slack, và nhóm hoặc siêu nhóm Telegram. Các kênh nhóm khác giữ hành vi nhóm hiện có trừ khi trang kênh của chúng cho biết chúng hỗ trợ sự kiện phòng nền.

## Thiết lập được khuyến nghị

Đặt hành vi trò chuyện nhóm toàn cục:

json5Copy code
[code]
    {  messages: {    groupChat: {      unmentionedInbound: "room_event",      visibleReplies: "message_tool",      historyLimit: 50,    },  },}
[/code]

Sau đó cấu hình chính phòng đó là luôn bật bằng cách tắt cơ chế chặn theo lượt nhắc cho phòng đó. Kênh vẫn phải được cho phép bởi `groupPolicy` thông thường, danh sách cho phép phòng và danh sách cho phép người gửi.

Sau khi lưu cấu hình, Gateway tải nóng các thiết lập `messages`. Chỉ khởi động lại khi theo dõi tệp hoặc tải lại cấu hình bị tắt.

## Những gì thay đổi

Với `messages.groupChat.unmentionedInbound: "room_event"`:

  * tin nhắn nhóm hoặc kênh được cho phép nhưng không nhắc đến tác tử trở thành sự kiện phòng thầm lặng
  * tin nhắn có nhắc đến tác tử vẫn là yêu cầu của người dùng
  * lệnh văn bản và lệnh gốc vẫn là yêu cầu của người dùng
  * yêu cầu hủy bỏ hoặc dừng vẫn là yêu cầu của người dùng
  * tin nhắn trực tiếp vẫn là yêu cầu của người dùng


Sự kiện phòng dùng cơ chế gửi hiển thị nghiêm ngặt. Văn bản cuối cùng của trợ lý là riêng tư. Tác tử phải gọi `message(action=send)` để đăng trong phòng.

## Ví dụ Discord

json5Copy code
[code]
    {  messages: {    groupChat: {      unmentionedInbound: "room_event",      visibleReplies: "message_tool",      historyLimit: 50,    },  },  channels: {    discord: {      groupPolicy: "allowlist",      guilds: {        "&lt;DISCORD_SERVER_ID&gt;": {          requireMention: false,          users: ["&lt;YOUR_DISCORD_USER_ID&gt;"],        },      },    },  },}
[/code]

Dùng cấu hình Discord theo kênh khi chỉ một kênh nên hoạt động ở chế độ nền:

json5Copy code
[code]
    {  channels: {    discord: {      guilds: {        "&lt;DISCORD_SERVER_ID&gt;": {          channels: {            "&lt;DISCORD_CHANNEL_ID_OR_NAME&gt;": {              allow: true,              requireMention: false,            },          },        },      },    },  },}
[/code]

## Ví dụ Slack

Danh sách cho phép kênh Slack ưu tiên ID. Dùng ID kênh như `C12345678`, không dùng `#channel-name`.

json5Copy code
[code]
    {  messages: {    groupChat: {      unmentionedInbound: "room_event",      visibleReplies: "message_tool",      historyLimit: 50,    },  },  channels: {    slack: {      groupPolicy: "allowlist",      channels: {        "&lt;SLACK_CHANNEL_ID&gt;": {          allow: true,          requireMention: false,        },      },    },  },}
[/code]

## Ví dụ Telegram

Với nhóm Telegram, bot phải có khả năng nhìn thấy tin nhắn nhóm thông thường. Nếu `requireMention: false`, hãy tắt chế độ riêng tư BotFather hoặc dùng một thiết lập Telegram khác gửi toàn bộ lưu lượng nhóm đến bot.

json5Copy code
[code]
    {  messages: {    groupChat: {      unmentionedInbound: "room_event",      visibleReplies: "message_tool",      historyLimit: 50,    },  },  channels: {    telegram: {      groups: {        "&lt;TELEGRAM_GROUP_CHAT_ID&gt;": {          groupPolicy: "open",          requireMention: false,        },      },    },  },}
[/code]

ID nhóm Telegram thường là số âm như `-1001234567890`. Đọc `chat.id` từ `openclaw logs --follow`, chuyển tiếp một tin nhắn nhóm đến bot trợ giúp ID, hoặc kiểm tra Bot API `getUpdates`.

## Chính sách riêng cho tác tử

Dùng ghi đè tác tử khi nhiều tác tử dùng chung cùng một phòng nhưng chỉ một tác tử nên xem cuộc trò chuyện không nhắc đến là ngữ cảnh nền:

json5Copy code
[code]
    {  messages: {    groupChat: {      visibleReplies: "message_tool",    },  },  agents: {    list: [      {        id: "main",        groupChat: {          unmentionedInbound: "room_event",          mentionPatterns: ["@openclaw", "openclaw"],        },      },    ],  },}
[/code]

Giá trị `agents.list[].groupChat.unmentionedInbound` riêng cho tác tử ghi đè `messages.groupChat.unmentionedInbound` cho tác tử đó.

## Chế độ phản hồi hiển thị

`messages.groupChat.visibleReplies` mặc định là `"automatic"` cho các yêu cầu người dùng trong nhóm/kênh thông thường. Giữ mặc định đó khi bạn muốn văn bản cuối cùng của trợ lý được đăng hiển thị mà không cần một lệnh gọi công cụ message rõ ràng.

Với các phòng nền luôn bật, `messages.groupChat.visibleReplies: "message_tool"` vẫn được khuyến nghị, đặc biệt với các mô hình thế hệ mới nhất, đáng tin cậy khi dùng công cụ, như GPT 5.5. Chế độ này cho phép tác tử quyết định khi nào nên nói bằng cách gọi công cụ message. Nếu mô hình trả về văn bản cuối cùng mà không gọi công cụ, OpenClaw giữ văn bản cuối cùng đó ở chế độ riêng tư và ghi nhật ký siêu dữ liệu gửi bị chặn.

Sự kiện phòng vẫn nghiêm ngặt ngay cả khi các yêu cầu nhóm khác dùng phản hồi tự động. Sự kiện phòng nền không nhắc đến vẫn yêu cầu `message(action=send)` để có đầu ra hiển thị.

## Lịch sử

`messages.groupChat.historyLimit` kiểm soát mặc định lịch sử nhóm toàn cục. Kênh có thể ghi đè bằng `channels.<channel>.historyLimit`, và một số kênh cũng hỗ trợ giới hạn lịch sử theo tài khoản.

Đặt `historyLimit: 0` để tắt ngữ cảnh lịch sử nhóm.

Các kênh sự kiện phòng được hỗ trợ giữ các tin nhắn phòng nền gần đây làm ngữ cảnh. Discord giữ lịch sử sự kiện phòng cho đến khi một lần gửi Discord hiển thị thành công, để ngữ cảnh thầm lặng không bị mất trước khi gửi qua công cụ message.

## Khắc phục sự cố

Nếu phòng hiển thị trạng thái đang nhập hoặc mức sử dụng token nhưng không có tin nhắn hiển thị:

  1. Xác nhận phòng được cho phép bởi danh sách cho phép kênh và danh sách cho phép người gửi.
  2. Xác nhận `requireMention: false` được đặt ở cấp phòng bạn mong đợi.
  3. Kiểm tra xem `messages.groupChat.unmentionedInbound` hoặc ghi đè tác tử có phải là `"room_event"` hay không.
  4. Kiểm tra nhật ký để tìm siêu dữ liệu payload cuối cùng bị chặn hoặc `didSendViaMessagingTool: false`.
  5. Với yêu cầu nhóm thông thường, giữ hoặc khôi phục `messages.groupChat.visibleReplies: "automatic"` nếu bạn muốn phản hồi cuối cùng được đăng tự động. Với phòng nền dùng `message_tool`, hãy dùng mô hình/runtime gọi công cụ đáng tin cậy.


Nếu phòng nền Telegram hoàn toàn không kích hoạt, hãy kiểm tra chế độ riêng tư BotFather và xác minh Gateway đang nhận tin nhắn nhóm thông thường.

Nếu phòng nền Slack không kích hoạt, hãy xác minh khóa kênh là ID kênh Slack và ứng dụng có phạm vi `channels:history` hoặc `groups:history` bắt buộc cho loại phòng đó.

## Liên quan

  * [Nhóm](</vi/channels/groups>)
  * [Discord](</vi/channels/discord>)
  * [Slack](</vi/channels/slack>)
  * [Telegram](</vi/channels/telegram>)
  * [Khắc phục sự cố kênh](</vi/channels/troubleshooting>)
  * [Tham chiếu cấu hình kênh](</vi/gateway/config-channels>)


Was this useful?YesNo

Open issue