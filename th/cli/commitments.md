---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/th/cli/commitments
scraped_at: 2026-05-25
---

แสดงรายการและจัดการข้อผูกพันในการติดตามผลที่อนุมานได้

ข้อผูกพันคือความจำสำหรับการติดตามผลแบบเลือกใช้เองและมีอายุสั้น ซึ่งสร้างจาก บริบทของการสนทนา ดู [ข้อผูกพันที่อนุมานได้](</th/concepts/commitments>) สำหรับ คู่มือแนวคิด

เมื่อไม่มีคำสั่งย่อย `openclaw commitments` จะแสดงรายการข้อผูกพันที่รอดำเนินการ

## การใช้งาน

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## ตัวเลือก

  * `--all`: แสดงทุกสถานะแทนที่จะแสดงเฉพาะข้อผูกพันที่รอดำเนินการ
  * `--agent <id>`: กรองให้เหลือ agent id เดียว
  * `--status <status>`: กรองตามสถานะ ค่า: `pending`, `sent`, `dismissed`, `snoozed` หรือ `expired`
  * `--json`: ส่งออก JSON ที่เครื่องอ่านได้


## ตัวอย่าง

แสดงรายการข้อผูกพันที่รอดำเนินการ:

bashCopy code
[code]
    openclaw commitments
[/code]

แสดงรายการข้อผูกพันที่จัดเก็บไว้ทั้งหมด:

bashCopy code
[code]
    openclaw commitments --all
[/code]

กรองให้เหลือ agent เดียว:

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

ค้นหาข้อผูกพันที่เลื่อนการแจ้งเตือน:

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

ยกเลิกข้อผูกพันหนึ่งรายการขึ้นไป:

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

ส่งออกเป็น JSON:

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## เอาต์พุต

เอาต์พุตแบบข้อความประกอบด้วย:

  * id ของข้อผูกพัน
  * สถานะ
  * ชนิด
  * เวลาถึงกำหนดที่เร็วที่สุด
  * ขอบเขต
  * ข้อความเช็กอินที่แนะนำ


เอาต์พุต JSON ยังมีเส้นทางของที่จัดเก็บข้อผูกพันและระเบียนที่จัดเก็บไว้แบบเต็ม

## ที่เกี่ยวข้อง

  * [ข้อผูกพันที่อนุมานได้](</th/concepts/commitments>)
  * [ภาพรวมหน่วยความจำ](</th/concepts/memory>)
  * [Heartbeat](</th/gateway/heartbeat>)
  * [งานตามกำหนดเวลา](</th/automation/cron-jobs>)


Was this useful?YesNo