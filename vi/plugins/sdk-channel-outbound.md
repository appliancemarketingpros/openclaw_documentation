---
title: API gửi ra của kênh
source_url: https://docs.openclaw.ai/vi/plugins/sdk-channel-outbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Channel plugin nên phơi bày hành vi tin nhắn đi từ `openclaw/plugin-sdk/channel-outbound`. Dùng `openclaw/plugin-sdk/channel-inbound` cho điều phối nhận/ngữ cảnh/phân phối.

Core sở hữu việc xếp hàng, độ bền, chính sách thử lại chung, hook, biên nhận, và công cụ `message` dùng chung. Plugin sở hữu các lệnh gọi gửi/chỉnh sửa/xóa gốc, chuẩn hóa đích, luồng hội thoại theo nền tảng, trích dẫn đã chọn, cờ thông báo, trạng thái tài khoản, và các tác dụng phụ đặc thù nền tảng.

## Bộ chuyển đổi

Hầu hết Plugin định nghĩa một bộ chuyển đổi `message`:

tsCopy code
[code]
       defineChannelMessageAdapter,  createMessageReceiptFromOutboundResults,} from "openclaw/plugin-sdk/channel-outbound"; export const demoMessageAdapter = defineChannelMessageAdapter({  id: "demo",  durableFinal: {    capabilities: {      text: true,      replyTo: true,      thread: true,      messageSendingHooks: true,    },  },  send: {    text: async ({ cfg, to, text, accountId, replyToId, threadId, signal }) => {      const sent = await sendDemoMessage({        cfg,        to,        text,        accountId: accountId ?? undefined,        replyToId: replyToId ?? undefined,        threadId: threadId == null ? undefined : String(threadId),        signal,      });       return {        receipt: createMessageReceiptFromOutboundResults({          results: [{ channel: "demo", messageId: sent.id, conversationId: to }],          kind: "text",          threadId: threadId == null ? undefined : String(threadId),          replyToId: replyToId ?? undefined,        }),      };    },  },});
[/code]

Chỉ khai báo các năng lực mà transport gốc thực sự bảo toàn. Bao phủ từng năng lực gửi, biên nhận, xem trước trực tiếp, và xác nhận nhận đã khai báo bằng các helper hợp đồng được xuất từ đường dẫn con này.

## Bộ chuyển đổi gửi đi hiện có

Nếu kênh đã có bộ chuyển đổi `outbound` tương thích, hãy dẫn xuất bộ chuyển đổi tin nhắn thay vì sao chép mã gửi:

tsCopy code
[code]
     export const messageAdapter = createChannelMessageAdapterFromOutbound({  id: "demo",  outbound,  durableFinal: {    capabilities: {      text: true,      media: true,    },  },});
[/code]

## Lượt gửi bền vững

Các helper gửi runtime cũng nằm trên `channel-outbound`:

  * `sendDurableMessageBatch(...)`
  * `withDurableMessageSendContext(...)`
  * `deliverInboundReplyWithMessageSendContext(...)`
  * các helper phát trực tuyến/tiến trình bản nháp như `resolveChannelDraftStreamingChunking(...)`


`sendDurableMessageBatch(...)` trả về một kết quả tường minh:

  * `sent`: ít nhất một tin nhắn nền tảng hiển thị đã được phân phối.
  * `suppressed`: không tin nhắn nền tảng nào nên được xem là bị thiếu.
  * `partial_failed`: ít nhất một tin nhắn nền tảng đã được phân phối trước khi một payload hoặc tác dụng phụ sau đó thất bại.
  * `failed`: không biên nhận nền tảng nào được tạo ra.


Dùng `payloadOutcomes` khi một batch trộn các payload đã gửi, bị chặn, và thất bại. Không suy luận việc hủy hook từ một kết quả phân phối trực tiếp kế thừa rỗng.

## Phân phối tương thích

Phân phối trả lời đến nên được lắp ráp thông qua `dispatchChannelInboundReply(...)` từ `channel-inbound`. Giữ việc phân phối nền tảng trong bộ chuyển đổi phân phối; dùng `channel-outbound` cho bộ chuyển đổi tin nhắn, gửi bền vững, biên nhận, xem trước trực tiếp, và các tùy chọn pipeline trả lời.

Was this useful?YesNo

Open issue