---
title: รีเซ็ต
source_url: https://docs.openclaw.ai/th/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

รีเซ็ต config/สถานะภายในเครื่อง (ยังคงติดตั้ง CLI ไว้)

ตัวเลือก:

  * `--scope <scope>`: `config`, `config+creds+sessions` หรือ `full`
  * `--yes`: ข้ามข้อความยืนยัน
  * `--non-interactive`: ปิดการถามตอบ; ต้องใช้ร่วมกับ `--scope` และ `--yes`
  * `--dry-run`: แสดงการกระทำโดยไม่ลบไฟล์


ตัวอย่าง:

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

หมายเหตุ:

  * รัน `openclaw backup create` ก่อน หากคุณต้องการ snapshot ที่กู้คืนได้ก่อนลบสถานะภายในเครื่อง
  * หากคุณไม่ระบุ `--scope`, `openclaw reset` จะใช้ prompt แบบโต้ตอบเพื่อเลือกว่าจะลบอะไร
  * `--non-interactive` ใช้ได้ก็ต่อเมื่อตั้งค่าทั้ง `--scope` และ `--yes`


## ที่เกี่ยวข้อง

  * [CLI reference](</th/cli>)


Was this useful?YesNo