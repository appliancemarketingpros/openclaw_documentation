---
title: กฎการพุชของ Matrix สำหรับพรีวิวแบบเงียบ
source_url: https://docs.openclaw.ai/th/channels/matrix-push-rules
scraped_at: 2026-05-25
---

เมื่อ `channels.matrix.streaming` เป็น `"quiet"` OpenClaw จะแก้ไขอีเวนต์ตัวอย่างเดียวในตำแหน่งเดิม และทำเครื่องหมายการแก้ไขที่เสร็จสมบูรณ์ด้วยแฟล็กเนื้อหาแบบกำหนดเอง ไคลเอนต์ Matrix จะแจ้งเตือนเมื่อมีการแก้ไขสุดท้ายก็ต่อเมื่อกฎการพุชรายผู้ใช้ตรงกับแฟล็กนั้น หน้านี้มีไว้สำหรับผู้ดูแลระบบที่โฮสต์ Matrix เองและต้องการติดตั้งกฎนั้นให้กับแต่ละบัญชีผู้รับ

หากคุณต้องการเพียงพฤติกรรมการแจ้งเตือน Matrix มาตรฐาน ให้ใช้ `streaming: "partial"` หรือปิดการสตรีมไว้ ดู [การตั้งค่าช่องทาง Matrix](</th/channels/matrix#streaming-previews>)

## ข้อกำหนดเบื้องต้น

  * ผู้ใช้ผู้รับ = บุคคลที่ควรได้รับการแจ้งเตือน
  * ผู้ใช้บอต = บัญชี Matrix ของ OpenClaw ที่ส่งคำตอบ
  * ใช้ access token ของผู้ใช้ผู้รับสำหรับการเรียก API ด้านล่าง
  * จับคู่ `sender` ในกฎการพุชกับ MXID แบบเต็มของผู้ใช้บอต
  * บัญชีผู้รับต้องมี pushers ที่ทำงานได้อยู่แล้ว — กฎตัวอย่างแบบเงียบจะทำงานเฉพาะเมื่อการส่งพุช Matrix ปกติทำงานสมบูรณ์


## ขั้นตอน

* ### กำหนดค่าตัวอย่างแบบเงียบ

json5Copy code
[code]
    {channels: {matrix: {  streaming: "quiet",},},}
[/code]

* ### รับ access token ของผู้รับ

ใช้โทเค็นเซสชันไคลเอนต์ที่มีอยู่ซ้ำหากทำได้ หากต้องการออกโทเค็นใหม่:

bashCopy code
[code]
    curl -sS -X POST \"https://matrix.example.org/_matrix/client/v3/login" \-H "Content-Type: application/json" \--data '{"type": "m.login.password","identifier": { "type": "m.id.user", "user": "@alice:example.org" },"password": "REDACTED"}'
[/code]

* ### ตรวจสอบว่ามี pushers อยู่

bashCopy code
[code]
    curl -sS \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \"https://matrix.example.org/_matrix/client/v3/pushers"
[/code]

หากไม่มี pushers ส่งกลับมา ให้แก้ไขการส่งพุช Matrix ปกติสำหรับบัญชีนี้ก่อนดำเนินการต่อ

* ### ติดตั้งกฎการพุชแบบ override

OpenClaw ทำเครื่องหมายการแก้ไขตัวอย่างแบบข้อความล้วนที่เสร็จสมบูรณ์ด้วย `content["com.openclaw.finalized_preview"] = true` ติดตั้งกฎที่จับคู่เครื่องหมายนั้นพร้อมกับ MXID ของบอตในฐานะผู้ส่ง:

bashCopy code
[code]
    curl -sS -X PUT \"https://matrix.example.org/_matrix/client/v3/pushrules/global/override/openclaw-finalized-preview-botname" \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \-H "Content-Type: application/json" \--data '{"conditions": [  { "kind": "event_match", "key": "type", "pattern": "m.room.message" },  {    "kind": "event_property_is",    "key": "content.m\\.relates_to.rel_type",    "value": "m.replace"  },  {    "kind": "event_property_is",    "key": "content.com\\.openclaw\\.finalized_preview",    "value": true  },  { "kind": "event_match", "key": "sender", "pattern": "@bot:example.org" }],"actions": [  "notify",  { "set_tweak": "sound", "value": "default" },  { "set_tweak": "highlight", "value": false }]}'
[/code]

แทนที่ก่อนเรียกใช้:

  * `https://matrix.example.org`: URL ฐานของ homeserver ของคุณ
  * `$USER_ACCESS_TOKEN`: access token ของผู้ใช้ผู้รับ
  * `openclaw-finalized-preview-botname`: ID กฎที่ไม่ซ้ำกันต่อบอตต่อผู้รับ (รูปแบบ: `openclaw-finalized-preview-<botname>`)
  * `@bot:example.org`: MXID ของบอต OpenClaw ของคุณ ไม่ใช่ของผู้รับ


* ### ตรวจสอบ

bashCopy code
[code]
    curl -sS \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \"https://matrix.example.org/_matrix/client/v3/pushrules/global/override/openclaw-finalized-preview-botname"
[/code]

จากนั้นทดสอบคำตอบแบบสตรีม ในโหมดเงียบ ห้องจะแสดงตัวอย่างร่างแบบเงียบและแจ้งเตือนหนึ่งครั้งเมื่อบล็อกหรือเทิร์นเสร็จสิ้น

หากต้องการลบกฎในภายหลัง ให้ `DELETE` URL กฎเดียวกันด้วยโทเค็นของผู้รับ

## หมายเหตุสำหรับหลายบอต

กฎการพุชถูกกำหนดคีย์ด้วย `ruleId`: การเรียก `PUT` ซ้ำกับ ID เดิมจะอัปเดตกฎเดียว สำหรับบอต OpenClaw หลายตัวที่แจ้งเตือนผู้รับคนเดียวกัน ให้สร้างกฎหนึ่งรายการต่อบอตโดยใช้การจับคู่ผู้ส่งที่แตกต่างกัน

กฎ `override` ที่ผู้ใช้กำหนดใหม่จะถูกแทรกไว้ก่อนกฎระงับค่าเริ่มต้น ดังนั้นจึงไม่ต้องใช้พารามิเตอร์การจัดลำดับเพิ่มเติม กฎนี้มีผลเฉพาะกับการแก้ไขตัวอย่างแบบข้อความล้วนที่สามารถทำให้เสร็จสมบูรณ์ในตำแหน่งเดิมได้เท่านั้น ส่วน fallback สำหรับสื่อและ fallback สำหรับตัวอย่างที่ค้างเก่าใช้การส่ง Matrix ปกติ

## หมายเหตุสำหรับ homeserver

Synapse

ไม่จำเป็นต้องเปลี่ยน `homeserver.yaml` เป็นพิเศษ หากการแจ้งเตือน Matrix ปกติไปถึงผู้ใช้นี้อยู่แล้ว โทเค็นผู้รับ + การเรียก `pushrules` ด้านบนคือขั้นตอนการตั้งค่าหลัก

หากคุณเรียกใช้ Synapse หลัง reverse proxy หรือ workers ตรวจสอบให้แน่ใจว่า `/_matrix/client/.../pushrules/` ไปถึง Synapse อย่างถูกต้อง การส่งพุชจัดการโดยกระบวนการหลักหรือ `synapse.app.pusher` / workers ของ pusher ที่กำหนดค่าไว้ — ตรวจสอบให้แน่ใจว่าส่วนเหล่านั้นทำงานปกติ

กฎนี้ใช้เงื่อนไขกฎการพุช `event_property_is` (MSC3758, push rule v1.10) ซึ่งถูกเพิ่มใน Synapse ในปี 2023 Synapse รุ่นเก่ากว่ายอมรับการเรียก `PUT pushrules/...` แต่จะไม่จับคู่เงื่อนไขอย่างเงียบ ๆ — อัปเกรด Synapse หากไม่มีการแจ้งเตือนมาถึงเมื่อมีการแก้ไขตัวอย่างที่เสร็จสมบูรณ์

Tuwunel

ใช้ขั้นตอนเดียวกับ Synapse; ไม่จำเป็นต้องมีการกำหนดค่าเฉพาะของ Tuwunel สำหรับเครื่องหมายตัวอย่างที่เสร็จสมบูรณ์

หากการแจ้งเตือนหายไปขณะผู้ใช้ใช้งานบนอุปกรณ์อื่น ให้ตรวจสอบว่าเปิดใช้งาน `suppress_push_when_active` อยู่หรือไม่ Tuwunel เพิ่มตัวเลือกนี้ใน 1.4.2 (กันยายน 2025) และสามารถตั้งใจระงับการพุชไปยังอุปกรณ์อื่นขณะที่มีอุปกรณ์หนึ่งกำลังใช้งานอยู่

## ที่เกี่ยวข้อง

  * [การตั้งค่าช่องทาง Matrix](</th/channels/matrix>)
  * [แนวคิดการสตรีม](</th/concepts/streaming>)


Was this useful?YesNo