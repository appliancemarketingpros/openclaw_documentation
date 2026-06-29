---
title: API đầu vào của kênh
source_url: https://docs.openclaw.ai/vi/plugins/sdk-channel-inbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Các Plugin kênh nên mô hình hóa đường dẫn nhận bằng các danh từ đầu vào và thông điệp:

textCopy code
[code]
    platform event -> inbound facts/context -> agent reply -> message delivery
[/code]

Dùng `openclaw/plugin-sdk/channel-inbound` để chuẩn hóa sự kiện đầu vào, định dạng, gốc và điều phối. Dùng `openclaw/plugin-sdk/channel-outbound` cho hành vi gửi gốc, biên nhận, phân phối bền vững và xem trước trực tiếp.

## Trình trợ giúp cốt lõi

tsCopy code
[code]
       buildChannelInboundEventContext,  runChannelInboundEvent,  dispatchChannelInboundReply,} from "openclaw/plugin-sdk/channel-inbound";
[/code]

  * `buildChannelInboundEventContext(...)`: chiếu các dữ kiện kênh đã chuẩn hóa vào ngữ cảnh prompt/phiên. Dùng `channelContext` để truyền siêu dữ liệu người gửi/cuộc trò chuyện do kênh sở hữu tới hook Plugin `ctx.channelContext`; mở rộng `PluginHookChannelSenderContext` hoặc `PluginHookChannelChatContext` từ đường dẫn con này cho các trường dành riêng cho kênh.
  * `runChannelInboundEvent(...)`: chạy ingest, phân loại, preflight, phân giải, ghi lại, điều phối và hoàn tất cho một sự kiện nền tảng đầu vào.
  * `dispatchChannelInboundReply(...)`: ghi lại và điều phối một phản hồi đầu vào đã được lắp ráp với một adapter phân phối.


Runtime Plugin được tiêm vào cung cấp cùng các trình trợ giúp cấp cao bên dưới `runtime.channel.inbound.*` cho các kênh được đóng gói/gốc đã nhận đối tượng runtime.

tsCopy code
[code]
    await runtime.channel.inbound.run({  channel: "demo",  accountId,  raw: platformEvent,  adapter: {    ingest: normalizePlatformEvent,    resolveTurn: resolveInboundReply,  },});
[/code]

Các bộ điều phối tương thích nên lắp ráp đầu vào cho `dispatchChannelInboundReply(...)` và giữ phần phân phối nền tảng trong adapter phân phối. Các đường dẫn gửi mới nên ưu tiên adapter thông điệp và trình trợ giúp thông điệp bền vững.

## Di trú

Các bí danh runtime `runtime.channel.turn.*` cũ đã bị loại bỏ. Dùng:

  * `runtime.channel.inbound.run(...)` cho sự kiện đầu vào thô.
  * `runtime.channel.inbound.dispatchReply(...)` cho ngữ cảnh phản hồi đã lắp ráp.
  * `runtime.channel.inbound.buildContext(...)` cho payload ngữ cảnh đầu vào.
  * `runtime.channel.inbound.runPreparedReply(...)` chỉ cho các đường dẫn điều phối đã chuẩn bị do kênh sở hữu vốn đã tự lắp ráp closure điều phối của chúng.


Mã Plugin mới không nên đưa vào các API kênh đặt tên theo `turn`. Giữ từ vựng về lượt của mô hình hoặc tác tử bên trong mã tác tử/nhà cung cấp; Plugin kênh dùng các thuật ngữ đầu vào, thông điệp, phân phối và phản hồi.

Was this useful?YesNo

Open issue