---
title: ถอนการติดตั้ง
source_url: https://docs.openclaw.ai/th/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

ถอนการติดตั้งบริการ gateway + ข้อมูลในเครื่อง (CLI ยังคงอยู่)

ตัวเลือก:

  * `--service`: ลบบริการ gateway
  * `--state`: ลบสถานะและคอนฟิก
  * `--workspace`: ลบไดเรกทอรี workspace
  * `--app`: ลบแอป macOS
  * `--all`: ลบบริการ สถานะ workspace และแอปทั้งหมด
  * `--yes`: ข้ามพรอมป์ยืนยัน
  * `--non-interactive`: ปิดพรอมป์; ต้องใช้ร่วมกับ `--yes`
  * `--dry-run`: แสดงการกระทำโดยยังไม่ลบไฟล์


ตัวอย่าง:

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

หมายเหตุ:

  * รัน `openclaw backup create` ก่อน หากคุณต้องการ snapshot ที่กู้คืนได้ก่อนลบสถานะหรือ workspace
  * `--all` เป็นรูปแบบย่อสำหรับการลบบริการ สถานะ workspace และแอปร่วมกัน
  * `--non-interactive` ต้องใช้ร่วมกับ `--yes`


## ที่เกี่ยวข้อง

  * [ข้อมูลอ้างอิง CLI](</th/cli>)
  * [ถอนการติดตั้ง](</th/install/uninstall>)


Was this useful?YesNo