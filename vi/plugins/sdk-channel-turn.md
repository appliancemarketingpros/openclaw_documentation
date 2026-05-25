---
title: Lõi lượt kênh
source_url: https://docs.openclaw.ai/vi/plugins/sdk-channel-turn
scraped_at: 2026-05-25
---

Máy trạng thái lượt kênh là máy trạng thái đầu vào dùng chung, biến một sự kiện nền tảng đã chuẩn hóa thành một lượt agent. Các Plugin kênh cung cấp thông tin nền tảng và callback phân phối. Phần lõi sở hữu việc điều phối: tiếp nhận, phân loại, kiểm tra trước, phân giải, ủy quyền, lắp ráp, ghi nhận, điều phối và hoàn tất.

Dùng phần này khi Plugin của bạn nằm trên đường xử lý nóng của tin nhắn đến. Với các sự kiện không phải tin nhắn (lệnh slash, modal, tương tác nút, sự kiện vòng đời, reaction, trạng thái thoại), hãy giữ chúng cục bộ trong Plugin. Kernel chỉ sở hữu các sự kiện có thể trở thành một lượt văn bản của agent.

## Vì sao cần kernel dùng chung

Các Plugin kênh lặp lại cùng một luồng đầu vào: chuẩn hóa, định tuyến, chặn cổng, dựng ngữ cảnh, ghi metadata phiên, điều phối lượt agent, hoàn tất trạng thái phân phối. Nếu không có kernel dùng chung, thay đổi đối với kiểm soát mention, phản hồi hiển thị chỉ dành cho công cụ, metadata phiên, lịch sử đang chờ hoặc hoàn tất điều phối phải được áp dụng riêng cho từng kênh.

Kernel cố ý tách riêng bốn khái niệm:

  * `ConversationFacts`: tin nhắn đến từ đâu
  * `RouteFacts`: agent và phiên nào nên xử lý tin nhắn đó
  * `ReplyPlanFacts`: phản hồi hiển thị nên đi đến đâu
  * `MessageFacts`: agent nên thấy nội dung và ngữ cảnh bổ sung nào


DM Slack, chủ đề Telegram, luồng Matrix và phiên chủ đề Feishu đều phân biệt các phần này trong thực tế. Xem chúng như một mã định danh duy nhất sẽ gây lệch dần theo thời gian.

## Vòng đời giai đoạn

Kernel chạy cùng một pipeline cố định bất kể kênh:

  1. `ingest` \-- adapter chuyển một sự kiện nền tảng thô thành `NormalizedTurnInput`
  2. `classify` \-- adapter khai báo liệu sự kiện này có thể bắt đầu một lượt agent hay không
  3. `preflight` \-- adapter xử lý khử trùng lặp, tự vọng lại, cấp nước dữ liệu, debounce, giải mã, điền trước một phần fact
  4. `resolve` \-- adapter trả về một lượt đã lắp ráp đầy đủ (định tuyến, kế hoạch phản hồi, tin nhắn, phân phối)
  5. `authorize` \-- chính sách DM, nhóm, mention và lệnh được áp dụng lên các fact đã lắp ráp
  6. `assemble` \-- `FinalizedMsgContext` được dựng từ các fact thông qua `buildContext`
  7. `record` \-- metadata phiên đầu vào và tuyến cuối cùng được lưu bền
  8. `dispatch` \-- lượt agent được thực thi thông qua bộ điều phối khối có đệm
  9. `finalize` \-- adapter `onFinalize` chạy ngay cả khi điều phối gặp lỗi


Mỗi giai đoạn phát ra một sự kiện nhật ký có cấu trúc khi callback `log` được cung cấp. Xem Khả năng quan sát.

## Loại tiếp nhận

Kernel không ném lỗi khi một lượt bị chặn. Nó trả về một `ChannelTurnAdmission`:

Loại | Khi nào  
---|---  
`dispatch` | Lượt được tiếp nhận. Lượt agent chạy và đường phản hồi hiển thị được thực thi.  
`observeOnly` | Lượt chạy từ đầu đến cuối nhưng adapter phân phối không gửi gì hiển thị. Dùng cho agent quan sát phát sóng và các luồng đa agent thụ động khác.  
`handled` | Một sự kiện nền tảng đã được xử lý cục bộ (vòng đời, reaction, nút, modal). Kernel bỏ qua điều phối.  
`drop` | Đường bỏ qua. Tùy chọn `recordHistory: true` giữ tin nhắn trong lịch sử nhóm đang chờ để lần mention sau có ngữ cảnh.  
  
Việc tiếp nhận có thể đến từ `classify` (lớp sự kiện cho biết nó không thể bắt đầu một lượt), từ `preflight` (khử trùng lặp, tự vọng lại, thiếu mention nhưng có ghi lịch sử), hoặc từ chính `resolveTurn`.

## Điểm vào

Runtime cung cấp ba điểm vào ưu tiên để adapter có thể chọn tham gia ở mức phù hợp với kênh.

typescriptCopy code
[code]
    runtime.channel.turn.run(...)             // adapter-driven full pipelineruntime.channel.turn.runAssembled(...)    // already-built context + delivery adapterruntime.channel.turn.runPrepared(...)     // channel owns dispatch; kernel runs record + finalizeruntime.channel.turn.buildContext(...)    // pure facts to FinalizedMsgContext mapping
[/code]

Hai helper runtime cũ hơn vẫn còn khả dụng để tương thích với Plugin SDK:

typescriptCopy code
[code]
    runtime.channel.turn.runResolved(...)      // deprecated compatibility alias; prefer runruntime.channel.turn.dispatchAssembled(...) // deprecated compatibility alias; prefer runAssembled
[/code]

### run

Dùng khi kênh của bạn có thể biểu diễn luồng đầu vào của nó dưới dạng `ChannelTurnAdapter&lt;TRaw&gt;`. Adapter có các callback cho `ingest`, `classify` tùy chọn, `preflight` tùy chọn, `resolveTurn` bắt buộc và `onFinalize` tùy chọn.

typescriptCopy code
[code]
    await runtime.channel.turn.run({  channel: "tlon",  accountId,  raw: platformEvent,  adapter: {    ingest(raw) {      return {        id: raw.messageId,        timestamp: raw.timestamp,        rawText: raw.body,        textForAgent: raw.body,      };    },    classify(input) {      return { kind: "message", canStartAgentTurn: input.rawText.length > 0 };    },    async preflight(input, eventClass) {      if (await isDuplicate(input.id)) {        return { admission: { kind: "drop", reason: "dedupe" } };      }      return {};    },    resolveTurn(input) {      return buildAssembledTurn(input);    },    onFinalize(result) {      clearPendingGroupHistory(result);    },  },});
[/code]

`run` là hình dạng phù hợp khi kênh có logic adapter nhỏ và hưởng lợi từ việc sở hữu vòng đời thông qua các hook.

### runAssembled

Dùng khi kênh đã phân giải định tuyến, dựng `FinalizedMsgContext`, và chỉ cần thứ tự ghi nhận, pipeline phản hồi, điều phối và hoàn tất dùng chung. Đây là hình dạng được ưu tiên cho các đường đầu vào đơn giản được đóng gói sẵn nếu không sẽ phải lặp lại mẫu `createChannelMessageReplyPipeline(...)` và `runPrepared(...)`.

typescriptCopy code
[code]
    await runtime.channel.turn.runAssembled({  cfg,  channel: "irc",  accountId,  agentId: route.agentId,  routeSessionKey: route.sessionKey,  storePath,  ctxPayload,  recordInboundSession: runtime.channel.session.recordInboundSession,  dispatchReplyWithBufferedBlockDispatcher:    runtime.channel.reply.dispatchReplyWithBufferedBlockDispatcher,  delivery: {    deliver: async (payload) => {      await sendPlatformReply(payload);    },    onError: (err, info) => {      runtime.error?.(`reply ${info.kind} failed: ${String(err)}`);    },  },});
[/code]

Chọn `runAssembled` thay vì `runPrepared` khi hành vi điều phối duy nhất do kênh sở hữu là phân phối payload cuối cùng cộng với nhập liệu tùy chọn, tùy chọn phản hồi, phân phối bền vững hoặc ghi nhật ký lỗi.

### runPrepared

Dùng khi kênh có bộ điều phối cục bộ phức tạp với bản xem trước, thử lại, chỉnh sửa hoặc khởi tạo luồng cần được kênh sở hữu. Kernel vẫn ghi nhận phiên đầu vào trước khi điều phối và đưa ra một `DispatchedChannelTurnResult` thống nhất.

typescriptCopy code
[code]
    const { dispatchResult } = await runtime.channel.turn.runPrepared({  channel: "matrix",  accountId,  routeSessionKey,  storePath,  ctxPayload,  recordInboundSession,  record: {    onRecordError,    updateLastRoute,  },  onPreDispatchFailure: async (err) => {    await stopStatusReactions();  },  runDispatch: async () => {    return await runMatrixOwnedDispatcher();  },});
[/code]

Các kênh giàu tính năng (Matrix, Mattermost, Microsoft Teams, Feishu, QQ Bot) dùng `runPrepared` vì bộ điều phối của chúng điều phối hành vi riêng theo nền tảng mà kernel không được học biết.

### buildContext

Một hàm thuần ánh xạ các gói fact thành `FinalizedMsgContext`. Dùng hàm này khi kênh của bạn tự triển khai một phần pipeline nhưng muốn hình dạng ngữ cảnh nhất quán.

typescriptCopy code
[code]
    const ctxPayload = runtime.channel.turn.buildContext({  channel: "googlechat",  accountId,  messageId,  timestamp,  from,  sender,  conversation,  route,  reply,  message,  access,  media,  supplemental,});
[/code]

`buildContext` cũng hữu ích bên trong các callback `resolveTurn` khi lắp ráp một lượt cho `run`.

## Kiểu fact

Các fact mà kernel tiêu thụ từ adapter của bạn không phụ thuộc nền tảng. Hãy chuyển các đối tượng nền tảng thành những hình dạng này trước khi đưa chúng cho kernel.

### NormalizedTurnInput

Trường | Mục đích  
---|---  
`id` | Mã định danh tin nhắn ổn định dùng cho khử trùng lặp và nhật ký  
`timestamp` | Epoch ms tùy chọn  
`rawText` | Nội dung như được nhận từ nền tảng  
`textForAgent` | Nội dung đã làm sạch tùy chọn cho agent (loại mention, cắt khoảng trắng nhập liệu)  
`textForCommands` | Nội dung tùy chọn dùng để phân tích cú pháp `/command`  
`raw` | Tham chiếu truyền qua tùy chọn cho các callback adapter cần bản gốc  
  
### ChannelEventClass

Trường | Mục đích  
---|---  
`kind` | `message`, `command`, `interaction`, `reaction`, `lifecycle`, `unknown`  
`canStartAgentTurn` | Nếu false, kernel trả về `{ kind: "handled" }`  
`requiresImmediateAck` | Gợi ý cho các adapter cần ACK trước khi điều phối  
  
### SenderFacts

Trường | Mục đích  
---|---  
`id` | Mã định danh người gửi ổn định trên nền tảng  
`name` | Tên hiển thị  
`username` | Định danh nếu khác với `name`  
`tag` | Bộ phân biệt kiểu Discord hoặc thẻ nền tảng  
`roles` | Mã định danh vai trò, dùng để khớp danh sách cho phép theo vai trò thành viên  
`isBot` | Đúng khi người gửi là bot đã biết (kernel dùng để bỏ qua)  
`isSelf` | Đúng khi người gửi là chính agent đã cấu hình  
`displayLabel` | Nhãn đã render sẵn cho văn bản phong bì  
  
### ConversationFacts

Trường | Mục đích  
---|---  
`kind` | `direct`, `group`, hoặc `channel`  
`id` | Mã định danh cuộc trò chuyện dùng để định tuyến  
`label` | Nhãn con người cho phong bì  
`spaceId` | Mã định danh không gian ngoài tùy chọn (workspace Slack, homeserver Matrix)  
`parentId` | Mã định danh cuộc trò chuyện ngoài khi đây là một luồng  
`threadId` | Mã định danh luồng khi tin nhắn này nằm trong một luồng  
`nativeChannelId` | Mã định danh kênh gốc của nền tảng khi khác với mã định tuyến  
`routePeer` | Peer dùng cho tra cứu `resolveAgentRoute`  
  
### RouteFacts

Trường | Mục đích  
---|---  
`agentId` | Agent sẽ xử lý lượt này  
`accountId` | Ghi đè tùy chọn (các kênh nhiều tài khoản)  
`routeSessionKey` | Khóa phiên dùng để định tuyến  
`dispatchSessionKey` | Khóa phiên dùng khi gửi đi nếu khác khóa định tuyến  
`persistedSessionKey` | Khóa phiên được ghi vào siêu dữ liệu phiên được lưu  
`parentSessionKey` | Phiên cha cho các phiên rẽ nhánh/theo luồng  
`modelParentSessionKey` | Phiên cha phía mô hình cho các phiên rẽ nhánh  
`mainSessionKey` | Ghim chủ sở hữu DM chính cho hội thoại trực tiếp  
`createIfMissing` | Cho phép bước ghi tạo hàng phiên bị thiếu  
  
### ReplyPlanFacts

Trường | Mục đích  
---|---  
`to` | Đích trả lời logic được ghi vào ngữ cảnh `To`  
`originatingTo` | Đích ngữ cảnh gốc (`OriginatingTo`)  
`nativeChannelId` | Id kênh gốc của nền tảng để phân phối  
`replyTarget` | Đích trả lời hiển thị cuối cùng nếu khác với `to`  
`deliveryTarget` | Ghi đè phân phối cấp thấp hơn  
`replyToId` | Id tin nhắn được trích dẫn/neo  
`replyToIdFull` | Id trích dẫn dạng đầy đủ khi nền tảng có cả hai  
`messageThreadId` | Id luồng tại thời điểm phân phối  
`threadParentId` | Id tin nhắn cha của luồng  
`sourceReplyDeliveryMode` | `thread`, `reply`, `channel`, `direct`, hoặc `none`  
  
### AccessFacts

`AccessFacts` mang các giá trị boolean mà giai đoạn ủy quyền cần. Việc khớp danh tính vẫn nằm trong kênh: kernel chỉ tiêu thụ kết quả.

Trường | Mục đích  
---|---  
`dm` | Quyết định cho phép/ghép cặp/từ chối DM và danh sách `allowFrom`  
`group` | Chính sách nhóm, cho phép định tuyến, cho phép người gửi, danh sách cho phép, yêu cầu nhắc đến  
`commands` | Ủy quyền lệnh trên các bộ ủy quyền đã cấu hình  
`mentions` | Việc phát hiện nhắc đến có khả thi hay không và agent có được nhắc đến hay không  
  
### MessageFacts

Trường | Mục đích  
---|---  
`body` | Nội dung phong bì cuối cùng (đã định dạng)  
`rawBody` | Nội dung đến dạng thô  
`bodyForAgent` | Nội dung agent nhìn thấy  
`commandBody` | Nội dung dùng để phân tích lệnh  
`envelopeFrom` | Nhãn người gửi đã kết xuất sẵn cho phong bì  
`senderLabel` | Ghi đè tùy chọn cho người gửi đã kết xuất  
`preview` | Bản xem trước ngắn đã che thông tin cho nhật ký  
`inboundHistory` | Các mục lịch sử đến gần đây khi kênh giữ một bộ đệm  
  
### SupplementalContextFacts

Ngữ cảnh bổ sung bao gồm ngữ cảnh trích dẫn, chuyển tiếp và khởi tạo luồng. Kernel áp dụng chính sách `contextVisibility` đã cấu hình. Bộ chuyển đổi kênh chỉ cung cấp các dữ kiện và cờ `senderAllowed` để chính sách liên kênh luôn nhất quán.

### InboundMediaFacts

Phương tiện được biểu diễn theo dạng dữ kiện. Việc tải xuống từ nền tảng, xác thực, chính sách SSRF, quy tắc CDN và giải mã vẫn nằm cục bộ trong kênh. Kernel ánh xạ dữ kiện vào `MediaPath`, `MediaUrl`, `MediaType`, `MediaPaths`, `MediaUrls`, `MediaTypes` và `MediaTranscribedIndexes`.

## Hợp đồng bộ chuyển đổi

Đối với `run` đầy đủ, hình dạng bộ chuyển đổi là:

typescriptCopy code
[code]
    type ChannelTurnAdapter&lt;TRaw&gt; = {  ingest(raw: TRaw): Promise&lt;NormalizedTurnInput | null&gt; | NormalizedTurnInput | null;  classify?(input: NormalizedTurnInput): Promise&lt;ChannelEventClass&gt; | ChannelEventClass;  preflight?(    input: NormalizedTurnInput,    eventClass: ChannelEventClass,  ): Promise&lt;PreflightFacts | ChannelTurnAdmission | null | undefined&gt;;  resolveTurn(    input: NormalizedTurnInput,    eventClass: ChannelEventClass,    preflight: PreflightFacts,  ): Promise&lt;ChannelTurnResolved&gt; | ChannelTurnResolved;  onFinalize?(result: ChannelTurnResult): Promise<void> | void;};
[/code]

`resolveTurn` trả về một `ChannelTurnResolved`, là một `AssembledChannelTurn` với loại admission tùy chọn. Trả về `{ admission: { kind: "observeOnly" } }` sẽ chạy lượt mà không tạo đầu ra hiển thị. Bộ chuyển đổi vẫn sở hữu callback phân phối; callback đó chỉ trở thành no-op cho lượt đó.

`onFinalize` chạy trên mọi kết quả, bao gồm cả lỗi gửi đi. Dùng nó để xóa lịch sử nhóm đang chờ, xóa phản ứng xác nhận, dừng chỉ báo trạng thái và flush trạng thái cục bộ.

## Bộ chuyển đổi phân phối

Kernel không gọi trực tiếp nền tảng. Kênh trao cho kernel một `ChannelTurnDeliveryAdapter`:

typescriptCopy code
[code]
    type ChannelTurnDeliveryAdapter = {  deliver(payload: ReplyPayload, info: ChannelDeliveryInfo): Promise&lt;ChannelDeliveryResult | void&gt;;  onError?(err: unknown, info: { kind: string }): void;  durable?: false | DurableInboundReplyDeliveryOptions;}; type ChannelDeliveryResult = {  messageIds?: string[];  receipt?: MessageReceipt;  threadId?: string;  replyToId?: string;  visibleReplySent?: boolean;};
[/code]

`deliver` được gọi một lần cho mỗi đoạn trả lời đã đệm. Trong quá trình di trú vòng đời tin nhắn, phân phối channel-turn đã lắp ráp mặc định do kênh sở hữu: trường `durable` bị bỏ qua nghĩa là kernel phải gọi trực tiếp `deliver` và không được định tuyến qua phân phối đi chung. Chỉ đặt `durable` sau khi kênh đã được kiểm tra để chứng minh đường gửi chung bảo toàn hành vi phân phối cũ, bao gồm đích trả lời/luồng, xử lý phương tiện, bộ nhớ đệm tin nhắn đã gửi/tự vọng lại, dọn dẹp trạng thái và id tin nhắn trả về. `durable: false` vẫn là cách viết tương thích cho "dùng callback do kênh sở hữu", nhưng các kênh chưa di trú không cần thêm nó. Trả về id tin nhắn nền tảng khi kênh có chúng để dispatcher có thể bảo toàn neo luồng và chỉnh sửa các đoạn sau; các đường phân phối mới hơn cũng nên trả về `receipt` để khôi phục, hoàn tất bản xem trước và triệt trùng lặp có thể rời khỏi `messageIds`. Đối với các lượt chỉ quan sát, trả về `{ visibleReplySent: false }` hoặc dùng `createNoopChannelTurnDeliveryAdapter()`.

Các kênh dùng `runPrepared` với dispatcher hoàn toàn do kênh sở hữu không có `ChannelTurnDeliveryAdapter`. Các dispatcher đó mặc định không durable. Chúng nên giữ đường phân phối trực tiếp cho đến khi chọn tham gia rõ ràng vào ngữ cảnh gửi mới với đích hoàn chỉnh, bộ chuyển đổi an toàn khi phát lại, hợp đồng biên nhận và các hook tác dụng phụ phía kênh.

Các helper tương thích công khai như `recordInboundSessionAndDispatchReply`, `dispatchInboundReplyWithBase` và helper DM trực tiếp phải tiếp tục bảo toàn hành vi trong quá trình di trú. Chúng không nên gọi phân phối durable chung trước các callback `deliver` hoặc `reply` do bên gọi sở hữu.

## Tùy chọn ghi

Giai đoạn ghi bọc `recordInboundSession`. Hầu hết kênh có thể dùng mặc định. Ghi đè qua `record`:

typescriptCopy code
[code]
    record: {  groupResolution,  createIfMissing: true,  updateLastRoute,  onRecordError: (err) => log.warn("record failed", err),  trackSessionMetaTask: (task) => pendingTasks.push(task),}
[/code]

Dispatcher chờ giai đoạn ghi. Nếu ghi ném lỗi, kernel chạy `onPreDispatchFailure` (khi được cung cấp cho `runPrepared`) rồi ném lại.

## Khả năng quan sát

Mỗi giai đoạn phát ra một sự kiện có cấu trúc khi callback `log` được cung cấp:

typescriptCopy code
[code]
    await runtime.channel.turn.run({  channel: "twitch",  accountId,  raw,  adapter,  log: (event) => {    runtime.log?.debug?.(`turn.${event.stage}:${event.event}`, {      channel: event.channel,      accountId: event.accountId,      messageId: event.messageId,      sessionKey: event.sessionKey,      admission: event.admission,      reason: event.reason,    });  },});
[/code]

Các giai đoạn được ghi nhật ký: `ingest`, `classify`, `preflight`, `resolve`, `authorize`, `assemble`, `record`, `dispatch`, `finalize`. Tránh ghi nhật ký nội dung thô; dùng `MessageFacts.preview` cho bản xem trước ngắn đã che thông tin.

## Những gì vẫn nằm cục bộ trong kênh

Kernel sở hữu việc điều phối. Kênh vẫn sở hữu:

  * Phương tiện vận chuyển của nền tảng (Gateway, REST, websocket, polling, webhooks)
  * Phân giải danh tính và khớp tên hiển thị
  * Lệnh gốc, lệnh slash, tự động hoàn thành, modal, nút, trạng thái giọng nói
  * Kết xuất thẻ, modal và adaptive-card
  * Xác thực phương tiện, quy tắc CDN, phương tiện được mã hóa, phiên âm
  * API chỉnh sửa, phản ứng, che nội dung và hiện diện
  * Backfill và lấy lịch sử phía nền tảng
  * Luồng ghép cặp cần xác minh đặc thù nền tảng


Nếu hai kênh bắt đầu cần cùng một helper cho một trong các phần này, hãy trích xuất một helper SDK dùng chung thay vì đẩy nó vào kernel.

## Độ ổn định

`runtime.channel.turn.*` là một phần của bề mặt runtime Plugin công khai. Các kiểu dữ kiện (`SenderFacts`, `ConversationFacts`, `RouteFacts`, `ReplyPlanFacts`, `AccessFacts`, `MessageFacts`, `SupplementalContextFacts`, `InboundMediaFacts`) và các hình dạng admission (`ChannelTurnAdmission`, `ChannelEventClass`) có thể truy cập qua `PluginRuntime` từ `openclaw/plugin-sdk/core`.

Áp dụng các quy tắc tương thích ngược: các trường dữ kiện mới là bổ sung, loại admission không bị đổi tên và tên điểm vào vẫn ổn định. Nhu cầu kênh mới yêu cầu thay đổi không mang tính bổ sung phải đi qua quy trình di trú SDK Plugin.

## Liên quan

  * [Tái cấu trúc vòng đời tin nhắn](</vi/concepts/message-lifecycle-refactor>) cho vòng đời gửi/nhận/trực tiếp đã lên kế hoạch sẽ bọc kernel này
  * [Xây dựng Plugin kênh](</vi/plugins/sdk-channel-plugins>) cho hợp đồng Plugin kênh rộng hơn
  * [Helper runtime Plugin](</vi/plugins/sdk-runtime>) cho các bề mặt `runtime.*` khác
  * [Nội bộ Plugin](</vi/plugins/architecture-internals>) cho pipeline tải và cơ chế registry


Was this useful?YesNo