---
title: เครื่องมือ apply_patch
source_url: https://docs.openclaw.ai/th/tools/apply-patch
scraped_at: 2026-05-25
---

ใช้การเปลี่ยนแปลงไฟล์ด้วยรูปแบบแพตช์ที่มีโครงสร้าง เหมาะสำหรับการแก้ไขหลายไฟล์ หรือหลายฮังก์ที่การเรียก `edit` เพียงครั้งเดียวอาจเปราะบาง

เครื่องมือนี้รับสตริง `input` เดียวที่ครอบการดำเนินการกับไฟล์หนึ่งรายการขึ้นไป:

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## พารามิเตอร์

  * `input` (จำเป็น): เนื้อหาแพตช์ทั้งหมด รวมถึง `*** Begin Patch` และ `*** End Patch`


## หมายเหตุ

  * เส้นทางแพตช์รองรับเส้นทางสัมพัทธ์ (จากไดเรกทอรีเวิร์กสเปซ) และเส้นทางสัมบูรณ์
  * `tools.exec.applyPatch.workspaceOnly` มีค่าเริ่มต้นเป็น `true` (จำกัดอยู่ในเวิร์กสเปซ) ตั้งค่าเป็น `false` เฉพาะเมื่อคุณตั้งใจให้ `apply_patch` เขียน/ลบนอกไดเรกทอรีเวิร์กสเปซ
  * ใช้ `*** Move to:` ภายในฮังก์ `*** Update File:` เพื่อเปลี่ยนชื่อไฟล์
  * `*** End of File` ทำเครื่องหมายการแทรกเฉพาะ EOF เมื่อจำเป็น
  * พร้อมใช้งานตามค่าเริ่มต้นสำหรับโมเดล OpenAI และ OpenAI Codex ตั้งค่า `tools.exec.applyPatch.enabled: false` เพื่อปิดใช้งาน
  * เลือกกำหนดให้จำกัดตามโมเดลได้ผ่าน `tools.exec.applyPatch.allowModels`
  * การกำหนดค่าอยู่ภายใต้ `tools.exec` เท่านั้น


## ตัวอย่าง

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## ที่เกี่ยวข้อง

[**Diffs** ตัวดู diff แบบอ่านอย่างเดียวสำหรับการนำเสนอการเปลี่ยนแปลง ](</th/tools/diffs>) [**Exec tool** การรันคำสั่งเชลล์จาก agent ](</th/tools/exec>) [**Code execution** การวิเคราะห์ Python ระยะไกลในแซนด์บ็อกซ์ด้วย xAI ](</th/tools/code-execution>)

Was this useful?YesNo