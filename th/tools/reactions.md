---
title: ปฏิกิริยา
source_url: https://docs.openclaw.ai/th/tools/reactions
scraped_at: 2026-05-25
---

เอเจนต์สามารถเพิ่มและลบปฏิกิริยาอีโมจิบนข้อความได้โดยใช้เครื่องมือ `message` พร้อมแอ็กชัน `react` พฤติกรรมของปฏิกิริยาแตกต่างกันไปตามแชนเนลและทรานสปอร์ต

## วิธีทำงาน

jsonCopy code
[code]
    {  "action": "react",  "messageId": "msg-123",  "emoji": "thumbsup"}
[/code]

  * ต้องระบุ `emoji` เมื่อเพิ่มปฏิกิริยา
  * ตั้งค่า `emoji` เป็นสตริงว่าง (`""`) เพื่อลบปฏิกิริยาของบอต
  * ตั้งค่า `remove: true` เพื่อลบอีโมจิที่ระบุ (ต้องมี `emoji` ที่ไม่ว่าง)
  * บนแชนเนลที่รองรับปฏิกิริยาสถานะ การตั้งค่า `trackToolCalls: true` บน ปฏิกิริยาจะทำให้รันไทม์ใช้ข้อความที่มีปฏิกิริยานั้นสำหรับปฏิกิริยาความคืบหน้า ของเครื่องมือที่ตามมาในเทิร์นเดียวกัน


## พฤติกรรมของแชนเนล

Discord และ Slack

  * `emoji` ว่างจะลบปฏิกิริยาทั้งหมดของบอตบนข้อความ
  * `remove: true` จะลบเฉพาะอีโมจิที่ระบุ

Google Chat

  * `emoji` ว่างจะลบปฏิกิริยาของแอปบนข้อความ
  * `remove: true` จะลบเฉพาะอีโมจิที่ระบุ

Telegram

  * `emoji` ว่างจะลบปฏิกิริยาของบอต
  * `remove: true` จะลบปฏิกิริยาด้วย แต่ยังต้องมี `emoji` ที่ไม่ว่างสำหรับการตรวจสอบความถูกต้องของเครื่องมือ

WhatsApp

  * `emoji` ว่างจะลบปฏิกิริยาของบอต
  * `remove: true` จะถูกแมปเป็นอีโมจิว่างภายใน (ยังต้องมี `emoji` ในการเรียกใช้เครื่องมือ)

Zalo Personal (zalouser)

  * ต้องมี `emoji` ที่ไม่ว่าง
  * `remove: true` จะลบปฏิกิริยาอีโมจินั้นโดยเฉพาะ

Feishu/Lark

  * ใช้เครื่องมือ `feishu_reaction` พร้อมแอ็กชัน `add`, `remove` และ `list`
  * การเพิ่ม/ลบต้องมี `emoji_type`; การลบต้องมี `reaction_id` ด้วย

Signal

  * การแจ้งเตือนปฏิกิริยาขาเข้าควบคุมโดย `channels.signal.reactionNotifications`: `"off"` จะปิดใช้งาน, `"own"` (ค่าเริ่มต้น) จะปล่อยเหตุการณ์เมื่อผู้ใช้ตอบสนองต่อข้อความของบอต และ `"all"` จะปล่อยเหตุการณ์สำหรับปฏิกิริยาทั้งหมด

iMessage

  * ปฏิกิริยาขาออกคือ iMessage tapbacks (`love`, `like`, `dislike`, `laugh`, `emphasize` และ `question`)
  * การแจ้งเตือน tapback ขาเข้าควบคุมโดย `channels.imessage.reactionNotifications`: `"off"` จะปิดใช้งาน, `"own"` (ค่าเริ่มต้น) จะปล่อยเหตุการณ์เมื่อผู้ใช้ตอบสนองต่อข้อความที่บอตเป็นผู้เขียน และ `"all"` จะปล่อยเหตุการณ์สำหรับ tapback ทั้งหมดจากผู้ส่งที่ได้รับอนุญาต


## ระดับปฏิกิริยา

การกำหนดค่า `reactionLevel` รายแชนเนลควบคุมว่าเอเจนต์ใช้ปฏิกิริยากว้างเพียงใด โดยทั่วไปค่าคือ `off`, `ack`, `minimal` หรือ `extensive`

  * [Telegram reactionLevel](</th/channels/telegram#reaction-notifications>) — `channels.telegram.reactionLevel`
  * [WhatsApp reactionLevel](</th/channels/whatsapp#reaction-level>) — `channels.whatsapp.reactionLevel`


ตั้งค่า `reactionLevel` บนแชนเนลแต่ละรายการเพื่อปรับว่าเอเจนต์ตอบสนองต่อข้อความบนแต่ละแพลตฟอร์มอย่างกระตือรือร้นเพียงใด

## ที่เกี่ยวข้อง

  * [Agent Send](</th/tools/agent-send>) — เครื่องมือ `message` ที่มี `react`
  * [แชนเนล](</th/channels>) — การกำหนดค่าเฉพาะแชนเนล


Was this useful?YesNo