---
title: แฟล็กการวินิจฉัย
source_url: https://docs.openclaw.ai/th/diagnostics/flags
scraped_at: 2026-05-25
---

แฟล็กการวินิจฉัยช่วยให้คุณเปิดใช้บันทึกดีบักแบบเจาะจงได้โดยไม่ต้องเปิดการบันทึกแบบละเอียดทุกส่วน แฟล็กเป็นแบบเลือกเปิดใช้ และจะไม่มีผลเว้นแต่ระบบย่อยจะตรวจสอบแฟล็กนั้น

## วิธีการทำงาน

  * แฟล็กเป็นสตริง (ไม่คำนึงถึงตัวพิมพ์เล็ก-ใหญ่)
  * คุณสามารถเปิดใช้แฟล็กใน config หรือผ่าน env override ได้
  * รองรับ wildcard: 
    * `telegram.*` ตรงกับ `telegram.http`
    * `*` เปิดใช้แฟล็กทั้งหมด


## เปิดใช้ผ่าน config

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http"]  }}
[/code]

หลายแฟล็ก:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http", "brave.http", "gateway.*"]  }}
[/code]

รีสตาร์ท Gateway หลังจากเปลี่ยนแฟล็ก

## Env override (ใช้ครั้งเดียว)

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=telegram.http,telegram.payload
[/code]

ปิดใช้แฟล็กทั้งหมด:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=0
[/code]

## อาร์ติแฟกต์ Timeline

แฟล็ก `timeline` จะเขียนอีเวนต์เวลาของการเริ่มต้นและรันไทม์แบบมีโครงสร้างสำหรับ harness QA ภายนอก:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=timeline \OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=/tmp/openclaw-timeline.jsonl \openclaw gateway run
[/code]

คุณยังสามารถเปิดใช้ใน config ได้ด้วย:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["timeline"]  }}
[/code]

พาธไฟล์ timeline ยังคงมาจาก `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH` เมื่อเปิดใช้ `timeline` จาก config เท่านั้น span ช่วงโหลด config แรกสุดจะไม่ถูกส่งออก เพราะ OpenClaw ยังไม่ได้อ่าน config; span การเริ่มต้นถัดมาจะใช้แฟล็กจาก config

`OPENCLAW_DIAGNOSTICS=1`, `OPENCLAW_DIAGNOSTICS=all` และ `OPENCLAW_DIAGNOSTICS=*` จะเปิดใช้ timeline ด้วย เพราะค่าเหล่านี้เปิดใช้ แฟล็กการวินิจฉัยทุกตัว ควรใช้ `timeline` เมื่อคุณต้องการเฉพาะอาร์ติแฟกต์เวลารูปแบบ JSONL

ระเบียน timeline ใช้ envelope `openclaw.diagnostics.v1` อีเวนต์อาจมี รหัสโปรเซส ชื่อเฟส ชื่อ span ระยะเวลา รหัส Plugin จำนวน dependency ตัวอย่างความหน่วงของ event loop ชื่อการทำงานของ provider สถานะการออกของ child process และชื่อ/ข้อความข้อผิดพลาดตอนเริ่มต้น ให้ถือไฟล์ timeline เป็นอาร์ติแฟกต์การวินิจฉัยในเครื่อง; ตรวจสอบก่อนแชร์ออกนอกเครื่องของคุณ

## บันทึกไปอยู่ที่ไหน

แฟล็กจะส่งบันทึกไปยังไฟล์บันทึกการวินิจฉัยมาตรฐาน โดยค่าเริ่มต้น:

CodeCopy code
[code]
    /tmp/openclaw/openclaw-YYYY-MM-DD.log
[/code]

หากคุณตั้งค่า `logging.file` ให้ใช้พาธนั้นแทน บันทึกเป็น JSONL (หนึ่งออบเจ็กต์ JSON ต่อบรรทัด) การปกปิดยังคงใช้ตาม `logging.redactSensitive`

## ดึงบันทึก

เลือกไฟล์บันทึกล่าสุด:

bashCopy code
[code]
    ls -t /tmp/openclaw/openclaw-*.log | head -n 1
[/code]

กรองการวินิจฉัย HTTP ของ Telegram:

bashCopy code
[code]
    rg "telegram http error" /tmp/openclaw/openclaw-*.log
[/code]

กรองการวินิจฉัย HTTP ของ Brave Search:

bashCopy code
[code]
    rg "brave http" /tmp/openclaw/openclaw-*.log
[/code]

หรือ tail ขณะทำซ้ำปัญหา:

bashCopy code
[code]
    tail -f /tmp/openclaw/openclaw-$(date +%F).log | rg "telegram http error"
[/code]

สำหรับ Gateway ระยะไกล คุณยังสามารถใช้ `openclaw logs --follow` ได้ด้วย (ดู [/cli/logs](</th/cli/logs>))

## หมายเหตุ

  * หากตั้งค่า `logging.level` ไว้สูงกว่า `warn` บันทึกเหล่านี้อาจถูกระงับ ค่าเริ่มต้น `info` ใช้ได้
  * `brave.http` บันทึก URL/พารามิเตอร์ query ของคำขอ Brave Search สถานะ/เวลาการตอบกลับ และอีเวนต์ cache hit/miss/write โดยจะไม่บันทึก API keys หรือเนื้อหาการตอบกลับ แต่ query การค้นหาอาจมีข้อมูลละเอียดอ่อน
  * สามารถเปิดแฟล็กทิ้งไว้ได้อย่างปลอดภัย; แฟล็กมีผลเฉพาะปริมาณบันทึกของระบบย่อยที่ระบุเท่านั้น
  * ใช้ [/logging](</th/logging>) เพื่อเปลี่ยนปลายทาง ระดับ และการปกปิดของบันทึก


## ที่เกี่ยวข้อง

  * [การวินิจฉัย Gateway](</th/gateway/diagnostics>)
  * [การแก้ไขปัญหา Gateway](</th/gateway/troubleshooting>)


Was this useful?YesNo