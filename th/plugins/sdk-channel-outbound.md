---
title: API ขาออกของช่องทาง
source_url: https://docs.openclaw.ai/th/plugins/sdk-channel-outbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Channel Plugin ควรเปิดเผยพฤติกรรมข้อความขาออกจาก `openclaw/plugin-sdk/channel-outbound` ใช้ `openclaw/plugin-sdk/channel-inbound` สำหรับการจัดการ receive/context/dispatch

Core เป็นเจ้าของคิว ความทนทาน นโยบาย retry ทั่วไป hooks receipts และเครื่องมือ `message` ที่ใช้ร่วมกัน ส่วน Plugin เป็นเจ้าของการเรียก native send/edit/delete, การทำให้ target เป็นรูปแบบมาตรฐาน, platform threading, quotes ที่เลือก, notification flags, สถานะบัญชี และ side effects เฉพาะแพลตฟอร์ม

## อะแดปเตอร์

Plugin ส่วนใหญ่กำหนดอะแดปเตอร์ `message` หนึ่งตัว:

tsCopy code
[code]
       defineChannelMessageAdapter,  createMessageReceiptFromOutboundResults,} from "openclaw/plugin-sdk/channel-outbound"; export const demoMessageAdapter = defineChannelMessageAdapter({  id: "demo",  durableFinal: {    capabilities: {      text: true,      replyTo: true,      thread: true,      messageSendingHooks: true,    },  },  send: {    text: async ({ cfg, to, text, accountId, replyToId, threadId, signal }) => {      const sent = await sendDemoMessage({        cfg,        to,        text,        accountId: accountId ?? undefined,        replyToId: replyToId ?? undefined,        threadId: threadId == null ? undefined : String(threadId),        signal,      });       return {        receipt: createMessageReceiptFromOutboundResults({          results: [{ channel: "demo", messageId: sent.id, conversationId: to }],          kind: "text",          threadId: threadId == null ? undefined : String(threadId),          replyToId: replyToId ?? undefined,        }),      };    },  },});
[/code]

ประกาศเฉพาะความสามารถที่ native transport รักษาไว้จริงเท่านั้น ครอบคลุมความสามารถของ send, receipt, live-preview และ receive-ack แต่ละรายการที่ประกาศไว้ด้วย contract helpers ที่ export จาก subpath นี้

## อะแดปเตอร์ขาออกที่มีอยู่

ถ้า channel มีอะแดปเตอร์ `outbound` ที่เข้ากันได้อยู่แล้ว ให้ derive message adapter แทนการทำซ้ำโค้ด send:

tsCopy code
[code]
     export const messageAdapter = createChannelMessageAdapterFromOutbound({  id: "demo",  outbound,  durableFinal: {    capabilities: {      text: true,      media: true,    },  },});
[/code]

## การส่งแบบทนทาน

runtime send helpers อยู่บน `channel-outbound` เช่นกัน:

  * `sendDurableMessageBatch(...)`
  * `withDurableMessageSendContext(...)`
  * `deliverInboundReplyWithMessageSendContext(...)`
  * draft streaming/progress helpers เช่น `resolveChannelDraftStreamingChunking(...)`


`sendDurableMessageBatch(...)` คืน outcome ที่ชัดเจนหนึ่งรายการ:

  * `sent`: มีข้อความแพลตฟอร์มที่มองเห็นได้อย่างน้อยหนึ่งข้อความถูกส่งแล้ว
  * `suppressed`: ไม่ควรถือว่าข้อความแพลตฟอร์มใด ๆ หายไป
  * `partial_failed`: มีข้อความแพลตฟอร์มอย่างน้อยหนึ่งข้อความถูกส่งก่อนที่ payload หรือ side effect ภายหลังจะล้มเหลว
  * `failed`: ไม่มี platform receipt ถูกสร้างขึ้น


ใช้ `payloadOutcomes` เมื่อ batch ผสม payload ที่ส่งแล้ว ถูก suppress และล้มเหลว อย่าอนุมาน hook cancellation จากผลลัพธ์ legacy direct-delivery ที่ว่างเปล่า

## Compatibility Dispatch

Inbound reply dispatch ควรถูกประกอบผ่าน `dispatchChannelInboundReply(...)` จาก `channel-inbound` เก็บ platform delivery ไว้ใน delivery adapter; ใช้ `channel-outbound` สำหรับ message adapters, durable sends, receipts, live preview และตัวเลือก reply pipeline

Was this useful?YesNo

Open issue