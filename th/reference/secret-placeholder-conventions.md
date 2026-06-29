---
title: หลักเกณฑ์การใช้ตัวแทนความลับ
source_url: https://docs.openclaw.ai/th/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# แบบแผนสำหรับตัวยึดตำแหน่งของความลับ

ใช้ตัวยึดตำแหน่งที่มนุษย์อ่านเข้าใจได้ แต่ไม่คล้ายกับความลับจริง

## รูปแบบที่แนะนำ

  * ควรใช้ค่าที่สื่อความหมาย เช่น `example-openai-key-not-real` หรือ `example-discord-bot-token`
  * สำหรับตัวอย่าง shell ควรใช้ `${OPENAI_API_KEY}` แทนสตริงแบบ inline ที่ดูเหมือนโทเค็น
  * ทำให้ตัวอย่างดูเป็นของปลอมอย่างชัดเจน และจำกัดตามวัตถุประสงค์ (ผู้ให้บริการ ช่องทาง ประเภทการยืนยันตัวตน)


## หลีกเลี่ยงรูปแบบเหล่านี้ในเอกสาร

  * ข้อความส่วนหัวหรือท้ายของคีย์ส่วนตัว PEM แบบตรงตัว
  * คำนำหน้าที่คล้ายข้อมูลรับรองที่ใช้งานจริง เช่น `sk-...`, `xoxb-...`, `AKIA...`
  * bearer token ที่ดูสมจริงซึ่งคัดลอกมาจากบันทึก runtime


## ตัวอย่าง

bashCopy code
[code]
    # Goodexport OPENAI_API_KEY="example-openai-key-not-real" # Better (when the doc is about env wiring)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue