---
title: อะแดปเตอร์ RPC
source_url: https://docs.openclaw.ai/th/reference/rpc
scraped_at: 2026-05-25
---

OpenClaw ผสานรวม CLI ภายนอกผ่าน JSON-RPC ปัจจุบันใช้สองรูปแบบ

## รูปแบบ A: HTTP daemon (signal-cli)

  * `signal-cli` ทำงานเป็น daemon พร้อม JSON-RPC ผ่าน HTTP
  * สตรีมเหตุการณ์คือ SSE (`/api/v1/events`)
  * Health probe: `/api/v1/check`
  * OpenClaw จัดการ lifecycle เมื่อ `channels.signal.autoStart=true`


ดู [Signal](</th/channels/signal>) สำหรับการตั้งค่าและ endpoint

## รูปแบบ B: กระบวนการลูก stdio (imsg)

  * OpenClaw spawn `imsg rpc` เป็นกระบวนการลูกสำหรับ [iMessage](</th/channels/imessage>)
  * JSON-RPC เป็นแบบคั่นบรรทัดผ่าน stdin/stdout (หนึ่ง JSON object ต่อบรรทัด)
  * ไม่มีพอร์ต TCP และไม่ต้องใช้ daemon


เมธอดหลักที่ใช้:

  * `watch.subscribe` → การแจ้งเตือน (`method: "message"`)
  * `watch.unsubscribe`
  * `send`
  * `chats.list` (probe/diagnostics)


ดู [iMessage](</th/channels/imessage>) สำหรับการตั้งค่าแบบเดิมและการระบุที่อยู่ (ควรใช้ `chat_id`)

## แนวทางสำหรับ adapter

  * Gateway เป็นเจ้าของกระบวนการ (start/stop ผูกกับ lifecycle ของ provider)
  * ทำให้ไคลเอนต์ RPC ทนทาน: timeout, รีสตาร์ตเมื่อออกจากกระบวนการ
  * ควรใช้ ID ที่เสถียร (เช่น `chat_id`) แทนสตริงที่ใช้แสดงผล


## ที่เกี่ยวข้อง

  * [โปรโตคอล Gateway](</th/gateway/protocol>)


Was this useful?YesNo