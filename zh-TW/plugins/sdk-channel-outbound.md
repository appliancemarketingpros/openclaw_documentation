---
title: 頻道傳出 API
source_url: https://docs.openclaw.ai/zh-TW/plugins/sdk-channel-outbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Channel 外掛應從 `openclaw/plugin-sdk/channel-outbound` 暴露傳出訊息行為。使用 `openclaw/plugin-sdk/channel-inbound` 進行接收／內容脈絡／派送協調。

核心負責佇列、耐久性、通用重試政策、鉤子、回條，以及共用的 `message` 工具。外掛負責原生傳送／編輯／刪除呼叫、目標 正規化、平台執行緒、選取的引用、通知旗標、帳號 狀態，以及平台特定的副作用。

## 配接器

多數外掛會定義一個 `message` 配接器：

tsCopy code
[code]
       defineChannelMessageAdapter,  createMessageReceiptFromOutboundResults,} from "openclaw/plugin-sdk/channel-outbound"; export const demoMessageAdapter = defineChannelMessageAdapter({  id: "demo",  durableFinal: {    capabilities: {      text: true,      replyTo: true,      thread: true,      messageSendingHooks: true,    },  },  send: {    text: async ({ cfg, to, text, accountId, replyToId, threadId, signal }) => {      const sent = await sendDemoMessage({        cfg,        to,        text,        accountId: accountId ?? undefined,        replyToId: replyToId ?? undefined,        threadId: threadId == null ? undefined : String(threadId),        signal,      });       return {        receipt: createMessageReceiptFromOutboundResults({          results: [{ channel: "demo", messageId: sent.id, conversationId: to }],          kind: "text",          threadId: threadId == null ? undefined : String(threadId),          replyToId: replyToId ?? undefined,        }),      };    },  },});
[/code]

只宣告原生傳輸實際會保留的能力。對每個已宣告的 傳送、回條、即時預覽與接收確認能力，使用此子路徑匯出的 合約輔助工具涵蓋。

## 現有傳出配接器

如果通道已經有相容的 `outbound` 配接器，請衍生訊息 配接器，而不是重複傳送程式碼：

tsCopy code
[code]
     export const messageAdapter = createChannelMessageAdapterFromOutbound({  id: "demo",  outbound,  durableFinal: {    capabilities: {      text: true,      media: true,    },  },});
[/code]

## 耐久傳送

執行階段傳送輔助工具也位於 `channel-outbound`：

  * `sendDurableMessageBatch(...)`
  * `withDurableMessageSendContext(...)`
  * `deliverInboundReplyWithMessageSendContext(...)`
  * 草稿串流／進度輔助工具，例如 `resolveChannelDraftStreamingChunking(...)`


`sendDurableMessageBatch(...)` 會回傳一個明確結果：

  * `sent`：至少已送達一則可見的平台訊息。
  * `suppressed`：不應將任何平台訊息視為遺失。
  * `partial_failed`：在後續酬載或副作用失敗之前，至少已送達一則平台訊息。
  * `failed`：未產生任何平台回條。


當批次混合已傳送、已抑制與失敗的酬載時，請使用 `payloadOutcomes`。 不要從空的舊版直接傳遞結果推斷鉤子取消。

## 相容性派送

傳入回覆派送應透過 `channel-inbound` 中的 `dispatchChannelInboundReply(...)` 組裝。將平台 傳遞保留在傳遞配接器中；針對訊息配接器、耐久傳送、回條、 即時預覽與回覆管線選項，使用 `channel-outbound`。

Was this useful?YesNo

Open issue