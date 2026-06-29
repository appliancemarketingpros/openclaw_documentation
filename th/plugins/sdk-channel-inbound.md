---
title: API ขาเข้าของช่องทาง
source_url: https://docs.openclaw.ai/th/plugins/sdk-channel-inbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Plugin ช่องทางควรจำลองเส้นทางการรับด้วยคำนาม inbound และ message:

textCopy code
[code]
    platform event -> inbound facts/context -> agent reply -> message delivery
[/code]

ใช้ `openclaw/plugin-sdk/channel-inbound` สำหรับการทำให้เหตุการณ์ inbound เป็นมาตรฐาน การจัดรูปแบบ ราก และการประสานงาน ใช้ `openclaw/plugin-sdk/channel-outbound` สำหรับพฤติกรรมการส่งแบบเนทีฟ ใบรับ การนำส่งที่ทนทาน และการแสดงตัวอย่างสด

## ตัวช่วยหลัก

tsCopy code
[code]
       buildChannelInboundEventContext,  runChannelInboundEvent,  dispatchChannelInboundReply,} from "openclaw/plugin-sdk/channel-inbound";
[/code]

  * `buildChannelInboundEventContext(...)`: ฉายข้อเท็จจริงของช่องทางที่ปรับเป็นมาตรฐานแล้วเข้าไปใน บริบท prompt/session ใช้ `channelContext` เพื่อส่งต่อเมตาดาต้า ผู้ส่ง/แชทที่ช่องทางเป็นเจ้าของไปยัง Plugin hook `ctx.channelContext`; ขยาย `PluginHookChannelSenderContext` หรือ `PluginHookChannelChatContext` จาก subpath นี้สำหรับฟิลด์เฉพาะช่องทาง
  * `runChannelInboundEvent(...)`: เรียก ingest, classify, preflight, resolve, record, dispatch และ finalize สำหรับเหตุการณ์แพลตฟอร์ม inbound หนึ่งรายการ
  * `dispatchChannelInboundReply(...)`: บันทึกและ dispatch การตอบกลับ inbound ที่ประกอบแล้ว ด้วยอะแดปเตอร์การนำส่ง


รันไทม์ Plugin ที่ถูกฉีดเข้ามาเปิดเผยตัวช่วยระดับสูงเดียวกันภายใต้ `runtime.channel.inbound.*` สำหรับช่องทางแบบบันเดิล/เนทีฟที่ได้รับ อ็อบเจ็กต์รันไทม์อยู่แล้ว

tsCopy code
[code]
    await runtime.channel.inbound.run({  channel: "demo",  accountId,  raw: platformEvent,  adapter: {    ingest: normalizePlatformEvent,    resolveTurn: resolveInboundReply,  },});
[/code]

ตัว dispatch เพื่อความเข้ากันได้ควรประกอบอินพุต `dispatchChannelInboundReply(...)` และเก็บการนำส่งของแพลตฟอร์มไว้ในอะแดปเตอร์การนำส่ง เส้นทางส่งใหม่ควร เลือกใช้อะแดปเตอร์ message และตัวช่วย message ที่ทนทาน

## การย้ายระบบ

นามแฝงรันไทม์ `runtime.channel.turn.*` แบบเก่าถูกนำออกแล้ว ใช้:

  * `runtime.channel.inbound.run(...)` สำหรับเหตุการณ์ inbound ดิบ
  * `runtime.channel.inbound.dispatchReply(...)` สำหรับบริบทการตอบกลับที่ประกอบแล้ว
  * `runtime.channel.inbound.buildContext(...)` สำหรับ payload บริบท inbound
  * `runtime.channel.inbound.runPreparedReply(...)` เฉพาะสำหรับเส้นทาง dispatch ที่เตรียมไว้และช่องทางเป็นเจ้าของ ซึ่งประกอบ dispatch closure ของตนเองอยู่แล้ว


โค้ด Plugin ใหม่ไม่ควรเพิ่ม API ช่องทางที่ตั้งชื่อด้วย `turn` เก็บคำศัพท์ของ model หรือ agent turn ไว้ภายในโค้ด agent/provider; Plugin ช่องทางใช้คำว่า inbound, message, delivery และ reply

Was this useful?YesNo

Open issue