---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/th/cli/tasks
scraped_at: 2026-05-25
---

ตรวจสอบงานเบื้องหลังแบบคงทนและสถานะ Task Flow เมื่อไม่มีคำสั่งย่อย `openclaw tasks` จะเทียบเท่ากับ `openclaw tasks list`

ดู [งานเบื้องหลัง](</th/automation/tasks>) สำหรับวงจรชีวิตและโมเดลการส่งมอบ

## การใช้งาน

bashCopy code
[code]
    openclaw tasksopenclaw tasks listopenclaw tasks list --runtime acpopenclaw tasks list --status runningopenclaw tasks show <lookup>openclaw tasks notify <lookup> state_changesopenclaw tasks cancel <lookup>openclaw tasks auditopenclaw tasks maintenanceopenclaw tasks maintenance --applyopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## ตัวเลือกระดับราก

  * `--json`: ส่งออก JSON
  * `--runtime <name>`: กรองตามชนิด: `subagent`, `acp`, `cron`, หรือ `cli`
  * `--status <name>`: กรองตามสถานะ: `queued`, `running`, `succeeded`, `failed`, `timed_out`, `cancelled`, หรือ `lost`


## คำสั่งย่อย

### `list`

bashCopy code
[code]
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
[/code]

แสดงรายการงานเบื้องหลังที่ติดตามไว้ โดยรายการใหม่ที่สุดอยู่ก่อน

### `show`

bashCopy code
[code]
    openclaw tasks show <lookup> [--json]
[/code]

แสดงงานหนึ่งรายการตาม ID งาน, ID การรัน หรือคีย์เซสชัน

### `notify`

bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

เปลี่ยนนโยบายการแจ้งเตือนสำหรับงานที่กำลังทำงานอยู่

### `cancel`

bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

ยกเลิกงานเบื้องหลังที่กำลังทำงานอยู่

### `audit`

bashCopy code
[code]
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
[/code]

แสดงระเบียนงานและ Task Flow ที่ค้าง สูญหาย ส่งมอบล้มเหลว หรือไม่สอดคล้องในลักษณะอื่น งานที่สูญหายซึ่งถูกเก็บไว้จนถึง `cleanupAfter` เป็นคำเตือน ส่วนงานที่สูญหายซึ่งหมดอายุหรือไม่มีตราประทับเป็นข้อผิดพลาด

### `maintenance`

bashCopy code
[code]
    openclaw tasks maintenance [--apply] [--json]
[/code]

แสดงตัวอย่างหรือใช้การกระทบยอดงานและ Task Flow, การประทับตราการล้างข้อมูล, การตัดทิ้ง, และการล้างรีจิสทรีเซสชันการรัน Cron ที่ค้าง สำหรับงาน Cron การกระทบยอดจะใช้บันทึกการรัน/สถานะงานที่คงอยู่ก่อนทำเครื่องหมายงานที่ยังใช้งานอยู่เก่าว่า `lost` ดังนั้นการรัน Cron ที่เสร็จสิ้นแล้วจะไม่กลายเป็นข้อผิดพลาด audit เท็จ เพียงเพราะสถานะรันไทม์ Gateway ในหน่วยความจำหายไป การ audit CLI แบบออฟไลน์ ไม่ใช่แหล่งอ้างอิงเด็ดขาดสำหรับชุดงาน Cron ที่ทำงานอยู่เฉพาะกระบวนการของ Gateway งาน CLI ที่มี ID การรัน/ID แหล่งที่มาจะถูกทำเครื่องหมายว่า `lost` เมื่อบริบทการรัน Gateway ที่ยังใช้งานอยู่ หายไป แม้ว่าจะยังมีแถวเซสชันลูกเก่าอยู่ก็ตาม เมื่อใช้จริง maintenance จะตัดแถวรีจิสทรีเซสชัน `cron:<jobId>:run:<uuid>` ที่เก่ากว่า 7 วันออกด้วย โดยยังคงรักษางาน Cron ที่กำลังทำงานอยู่และปล่อย แถวเซสชันที่ไม่ใช่ Cron ไว้โดยไม่แตะต้อง

### `flow`

bashCopy code
[code]
    openclaw tasks flow list [--status <name>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

ตรวจสอบหรือยกเลิกสถานะ Task Flow แบบคงทนภายใต้บัญชีแยกประเภทงาน

## ที่เกี่ยวข้อง

  * [ข้อมูลอ้างอิง CLI](</th/cli>)
  * [งานเบื้องหลัง](</th/automation/tasks>)


Was this useful?YesNo