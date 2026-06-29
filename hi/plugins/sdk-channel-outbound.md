---
title: चैनल आउटबाउंड API
source_url: https://docs.openclaw.ai/hi/plugins/sdk-channel-outbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Channel plugins को outbound संदेश व्यवहार `openclaw/plugin-sdk/channel-outbound` से expose करना चाहिए। receive/context/dispatch orchestration के लिए `openclaw/plugin-sdk/channel-inbound` का उपयोग करें।

Core queueing, durability, generic retry policy, hooks, receipts, और shared `message` tool का मालिक है। Plugin native send/edit/delete calls, target normalization, platform threading, selected quotes, notification flags, account state, और platform-specific side effects का मालिक है।

## Adapter

अधिकांश plugins एक `message` adapter परिभाषित करते हैं:

tsCopy code
[code]
       defineChannelMessageAdapter,  createMessageReceiptFromOutboundResults,} from "openclaw/plugin-sdk/channel-outbound"; export const demoMessageAdapter = defineChannelMessageAdapter({  id: "demo",  durableFinal: {    capabilities: {      text: true,      replyTo: true,      thread: true,      messageSendingHooks: true,    },  },  send: {    text: async ({ cfg, to, text, accountId, replyToId, threadId, signal }) => {      const sent = await sendDemoMessage({        cfg,        to,        text,        accountId: accountId ?? undefined,        replyToId: replyToId ?? undefined,        threadId: threadId == null ? undefined : String(threadId),        signal,      });       return {        receipt: createMessageReceiptFromOutboundResults({          results: [{ channel: "demo", messageId: sent.id, conversationId: to }],          kind: "text",          threadId: threadId == null ? undefined : String(threadId),          replyToId: replyToId ?? undefined,        }),      };    },  },});
[/code]

केवल वही capabilities घोषित करें जिन्हें native transport वास्तव में सुरक्षित रखता है। इस subpath से export किए गए contract helpers के साथ प्रत्येक घोषित send, receipt, live-preview, और receive-ack capability को cover करें।

## मौजूदा Outbound Adapters

यदि channel में पहले से compatible `outbound` adapter है, तो send code की duplicate copy बनाने के बजाय message adapter derive करें:

tsCopy code
[code]
     export const messageAdapter = createChannelMessageAdapterFromOutbound({  id: "demo",  outbound,  durableFinal: {    capabilities: {      text: true,      media: true,    },  },});
[/code]

## Durable Sends

Runtime send helpers भी `channel-outbound` पर रहते हैं:

  * `sendDurableMessageBatch(...)`
  * `withDurableMessageSendContext(...)`
  * `deliverInboundReplyWithMessageSendContext(...)`
  * draft streaming/progress helpers जैसे `resolveChannelDraftStreamingChunking(...)`


`sendDurableMessageBatch(...)` एक स्पष्ट outcome लौटाता है:

  * `sent`: कम से कम एक visible platform message deliver हुआ।
  * `suppressed`: किसी भी platform message को missing नहीं माना जाना चाहिए।
  * `partial_failed`: बाद का payload या side effect fail होने से पहले कम से कम एक platform message deliver हुआ।
  * `failed`: कोई platform receipt produce नहीं हुआ।


जब कोई batch sent, suppressed, और failed payloads को mix करता है, तो `payloadOutcomes` का उपयोग करें। खाली legacy direct-delivery result से hook cancellation infer न करें।

## Compatibility Dispatch

Inbound reply dispatch को `channel-inbound` से `dispatchChannelInboundReply(...)` के जरिए assemble करना चाहिए। platform delivery को delivery adapter में रखें; message adapters, durable sends, receipts, live preview, और reply pipeline options के लिए `channel-outbound` का उपयोग करें।

Was this useful?YesNo

Open issue