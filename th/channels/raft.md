---
title: แพ
source_url: https://docs.openclaw.ai/th/channels/raft
scraped_at: 2026-06-29
---

ChannelsDeveloper and self-hosted

Raft support เชื่อมต่อเอเจนต์ OpenClaw กับเอเจนต์ภายนอกของ Raft ผ่าน Raft CLI ภายในเครื่อง Raft ส่งคำใบ้สำหรับปลุกที่ผ่านการยืนยันตัวตนไปยัง Gateway จากนั้นเอเจนต์จะใช้ Raft CLI เพื่อตรวจสอบและส่งข้อความ

## ติดตั้ง

Raft เป็น Plugin ภายนอกอย่างเป็นทางการ ติดตั้งบนโฮสต์ Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/raftopenclaw gateway restart
[/code]

รายละเอียด: [Plugins](</th/tools/plugin>)

## ข้อกำหนดเบื้องต้น

  * เวิร์กสเปซ Raft ที่มีเอเจนต์ภายนอก
  * ติดตั้ง Raft CLI บนโฮสต์เดียวกับ OpenClaw Gateway
  * โปรไฟล์ Raft CLI ที่ลงชื่อเข้าใช้แล้วและเชื่อมโยงกับเอเจนต์ภายนอกนั้น


Plugin ไม่จัดเก็บข้อมูลรับรองของ Raft โดย Raft CLI จะเก็บการยืนยันตัวตนดังกล่าว ไว้ในโปรไฟล์ของตัวเอง

## กำหนดค่า

ตั้งค่าโปรไฟล์ใน config:

json5Copy code
[code]
    {  channels: {    raft: {      enabled: true,      profile: "openclaw",    },  },}
[/code]

สำหรับบัญชีเริ่มต้น คุณสามารถตั้งค่า `RAFT_PROFILE` ในสภาพแวดล้อมของ Gateway แทนได้:

bashCopy code
[code]
    RAFT_PROFILE=openclaw
[/code]

ใช้บัญชีที่มีชื่อเมื่อ Gateway หนึ่งตัวเชื่อมต่อกับเอเจนต์ภายนอกของ Raft มากกว่าหนึ่งตัว:

json5Copy code
[code]
    {  channels: {    raft: {      accounts: {        support: {          profile: "support-agent",        },        engineering: {          profile: "engineering-agent",        },      },    },  },}
[/code]

โฟลว์ตั้งค่าแบบโต้ตอบจะบันทึกโปรไฟล์เดียวกัน:

bashCopy code
[code]
    openclaw channels setup raft
[/code]

## วิธีการทำงาน

เมื่อ Gateway เริ่มทำงาน Plugin จะ:

  1. เปิด endpoint สำหรับปลุกแบบ HTTP ที่รับเฉพาะ loopback บนพอร์ตชั่วคราว
  2. เริ่ม `raft --profile <profile> agent bridge` พร้อม endpoint นั้นและโทเค็น ต่อโปรเซส
  3. ยอมรับเฉพาะคำใบ้สำหรับปลุกที่ผ่านการยืนยันตัวตน ไม่มีเนื้อหา และมีตัวตนสำหรับป้องกันการเล่นซ้ำจาก bridge ภายในเครื่อง
  4. ต้องมีหนึ่งใน `eventId`, `attemptId`, `messageId`, `delivery_id`, `wake_id` หรือ `id`
  5. ขจัด wake delivery ที่ลองใหม่ล่าสุดซ้ำตาม id เหตุการณ์ของ bridge รวมถึงข้ามการรีสตาร์ต Gateway
  6. ส่งคืน runtime session ที่เสถียรสำหรับ bridge ปัจจุบัน และชุด activity-drain ว่างสำหรับโปรโตคอล Raft CLI
  7. เริ่มเทิร์นเอเจนต์ OpenClaw แบบจัดลำดับหนึ่งรายการสำหรับแต่ละ wake ที่ยอมรับ


bridge เป็นเจ้าของการลองส่งซ้ำและการเชื่อมต่อใหม่ของ Raft เทิร์นของ OpenClaw จะได้รับ เฉพาะประกาศ wake ไม่ใช่สำเนาเนื้อหาข้อความ Raft โดยจะใช้ CLI เพื่ออ่านข้อความ ที่รอดำเนินการและส่งคำตอบ:

bashCopy code
[code]
    raft --profile openclaw message checkraft --profile openclaw message send
[/code]

## ตรวจสอบ

ตรวจสอบว่า OpenClaw หา CLI พบและมีโปรไฟล์ที่กำหนดค่าไว้:

bashCopy code
[code]
    openclaw channels status --probeopenclaw plugins inspect raft --runtime --json
[/code]

จากนั้นส่งข้อความไปยังเอเจนต์ภายนอกของ Raft บันทึกของ Gateway ควรแสดงว่า Raft bridge เริ่มทำงาน ตามด้วย wake ขาเข้า เอเจนต์ควรใช้โปรไฟล์ Raft ที่กำหนดค่าไว้เพื่อตรวจสอบข้อความที่รอดำเนินการ

## การแก้ไขปัญหา

ไม่มี Raft CLI

ติดตั้ง Raft CLI บนโฮสต์ Gateway และทำให้ `raft` พร้อมใช้งานบน `PATH` ของบริการ ตรวจสอบด้วย `raft --help` จากนั้นรีสตาร์ต Gateway

bridge ออกทันที

ตรวจสอบว่าโปรไฟล์ที่กำหนดค่าไว้ลงชื่อเข้าใช้แล้วและเป็นของเอเจนต์ภายนอก Raft ที่ตั้งใจไว้ เรียกใช้ `raft --profile <profile> agent bridge` โดยตรง เพื่อดูการวินิจฉัยจาก CLI

wake มาถึงแล้ว แต่ไม่มีการส่งคำตอบ Raft

นี่เป็นสิ่งที่คาดไว้เมื่อเอเจนต์ไม่ได้เรียกใช้ Raft CLI wake bridge ไม่ได้พกเนื้อหาข้อความหรือคำตอบสุดท้ายอัตโนมัติ ตรวจสอบ นโยบายเครื่องมือของเอเจนต์และให้แน่ใจว่าสามารถเรียกใช้ `raft --profile <profile> message check` และ `message send` ได้

## อ้างอิง

  * [Raft](<https://raft.build/>)
  * [เอกสาร Raft](<https://docs.raft.build/welcome/>)
  * [การผสานรวม Hermes Raft](<https://hermes-agent.nousresearch.com/docs/user-guide/messaging/raft>)


Was this useful?YesNo

Open issue