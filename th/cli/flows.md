---
title: โฟลว์ (เปลี่ยนเส้นทาง)
source_url: https://docs.openclaw.ai/th/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

ไม่มีคำสั่งระดับบนสุด `openclaw flows` การตรวจสอบ TaskFlow แบบคงทนอยู่ภายใต้ `openclaw tasks flow`

## คำสั่งย่อย

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

คำสั่งย่อย | คำอธิบาย | อาร์กิวเมนต์ / ตัวเลือก  
---|---|---  
`list` | แสดงรายการ TaskFlow ที่ติดตามอยู่ | เอาต์พุตที่เครื่องอ่านได้ `--json`; ตัวกรอง `--status <name>` (ดูค่าสถานะด้านล่าง)  
`show` | แสดง TaskFlow หนึ่งรายการ | id ของ flow หรือคีย์เจ้าของ `<lookup>`; เอาต์พุตที่เครื่องอ่านได้ `--json`  
`cancel` | ยกเลิก TaskFlow ที่กำลังทำงานอยู่ | id ของ flow หรือคีย์เจ้าของ `<lookup>`  
  
`<lookup>` ยอมรับได้ทั้ง id ของ flow (ที่ส่งกลับโดย `list` / `show`) หรือคีย์เจ้าของของ flow (ตัวระบุที่เสถียรซึ่งระบบย่อยที่เป็นเจ้าของใช้เพื่อติดตาม flow)

### ค่าตัวกรองสถานะ

`--status` บน `list` ยอมรับค่าใดค่าหนึ่งต่อไปนี้:

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## ตัวอย่าง

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

สำหรับแนวคิดและการเขียน TaskFlow แบบเต็ม โปรดดู [TaskFlow](</th/automation/taskflow>) สำหรับคำสั่งแม่ `tasks` โปรดดู [เอกสารอ้างอิง CLI ของ tasks](</th/cli/tasks>)

## ที่เกี่ยวข้อง

  * [เอกสารอ้างอิง CLI](</th/cli>)
  * [ระบบอัตโนมัติ](</th/automation>)
  * [TaskFlow](</th/automation/taskflow>)


Was this useful?YesNo