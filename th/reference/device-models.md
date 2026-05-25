---
title: ฐานข้อมูลรุ่นอุปกรณ์
source_url: https://docs.openclaw.ai/th/reference/device-models
scraped_at: 2026-05-25
---

แอปคู่หูบน macOS จะแสดงชื่อรุ่นอุปกรณ์ Apple ที่อ่านเข้าใจง่ายใน UI ของ **Instances** โดยแมปตัวระบุรุ่นของ Apple (เช่น `iPad16,6`, `Mac16,6`) ไปเป็นชื่อที่มนุษย์อ่านได้

การแมปนี้ถูก vendor มาเป็น JSON ภายใต้:

  * `apps/macos/Sources/OpenClaw/Resources/DeviceModels/`


## แหล่งข้อมูล

ปัจจุบันเรา vendor การแมปนี้มาจากรีโพสิตอรีที่ใช้สัญญาอนุญาต MIT:

  * `kyle-seongwoo-jun/apple-device-identifiers`


เพื่อให้บิลด์มีความกำหนดแน่นอน ไฟล์ JSON จะถูก pin ไว้กับ upstream commits ที่เฉพาะเจาะจง (บันทึกไว้ใน `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`)

## การอัปเดตฐานข้อมูล

  1. เลือก upstream commits ที่คุณต้องการ pin ไว้ (หนึ่งรายการสำหรับ iOS และหนึ่งรายการสำหรับ macOS)
  2. อัปเดต commit hashes ใน `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`
  3. ดาวน์โหลดไฟล์ JSON ใหม่ โดย pin กับ commits เหล่านั้น:

bashCopy code
[code]
    IOS_COMMIT="<commit sha for ios-device-identifiers.json>"MAC_COMMIT="<commit sha for mac-device-identifiers.json>" curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${IOS_COMMIT}/ios-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/ios-device-identifiers.json curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${MAC_COMMIT}/mac-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/mac-device-identifiers.json
[/code]

  4. ตรวจสอบให้แน่ใจว่า `apps/macos/Sources/OpenClaw/Resources/DeviceModels/LICENSE.apple-device-identifiers.txt` ยังคงตรงกับ upstream (แทนที่ไฟล์นี้หากสัญญาอนุญาตของ upstream เปลี่ยนแปลง)
  5. ตรวจสอบว่าแอป macOS บิลด์ผ่านอย่างสะอาด (ไม่มีคำเตือน):

bashCopy code
[code]
    swift build --package-path apps/macos
[/code]

## ที่เกี่ยวข้อง

  * [Nodes](</th/nodes>)
  * [Node troubleshooting](</th/nodes/troubleshooting>)


Was this useful?YesNo