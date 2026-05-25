---
title: สิทธิ์บน macOS
source_url: https://docs.openclaw.ai/th/platforms/mac/permissions
scraped_at: 2026-05-25
---

การให้สิทธิ์บน macOS มีความเปราะบาง TCC จะผูกการให้สิทธิ์เข้ากับ ลายเซ็นโค้ดของแอป, bundle identifier และ path บนดิสก์ หากสิ่งใดสิ่งหนึ่งเปลี่ยนไป macOS จะมองว่าแอปเป็นตัวใหม่ และอาจทิ้งหรือซ่อนหน้าต่างขอสิทธิ์

## ข้อกำหนดสำหรับสิทธิ์ที่เสถียร

  * path เดิม: รันแอปจากตำแหน่งคงที่ (สำหรับ OpenClaw คือ `dist/OpenClaw.app`)
  * bundle identifier เดิม: การเปลี่ยน bundle ID จะสร้างตัวตนสิทธิ์ใหม่
  * แอปที่มีลายเซ็น: บิลด์ที่ไม่ได้ลงนามหรือใช้ ad-hoc signing จะไม่คงสิทธิ์ไว้
  * ลายเซ็นสม่ำเสมอ: ใช้ใบรับรอง Apple Development หรือ Developer ID จริง เพื่อให้ลายเซ็นคงที่ข้ามการ build ใหม่


ad-hoc signatures จะสร้างตัวตนใหม่ทุกครั้งที่ build macOS จะลืม สิทธิ์เดิม และหน้าต่างขอสิทธิ์อาจหายไปทั้งหมดจนกว่าจะล้างรายการเก่าที่ค้างอยู่

## รายการตรวจสอบการกู้คืนเมื่อหน้าต่างขอสิทธิ์หายไป

  1. ปิดแอป
  2. ลบรายการของแอปใน System Settings -> Privacy & Security
  3. เปิดแอปใหม่จาก path เดิมแล้วให้สิทธิ์อีกครั้ง
  4. หากหน้าต่างยังไม่ขึ้น ให้รีเซ็ตรายการ TCC ด้วย `tccutil` แล้วลองอีกครั้ง
  5. สิทธิ์บางอย่างจะกลับมาปรากฏอีกครั้งได้ก็ต่อเมื่อรีสตาร์ต macOS แบบเต็ม


ตัวอย่างการรีเซ็ต (แทน bundle ID ตามต้องการ):

bashCopy code
[code]
    sudo tccutil reset Accessibility ai.openclaw.macsudo tccutil reset ScreenCapture ai.openclaw.macsudo tccutil reset AppleEvents
[/code]

## สิทธิ์ไฟล์และโฟลเดอร์ (Desktop/Documents/Downloads)

macOS อาจจำกัด Desktop, Documents และ Downloads สำหรับโปรเซสที่รันผ่านเทอร์มินัล/เบื้องหลังด้วย หากการอ่านไฟล์หรือการแสดงรายการไดเรกทอรีค้างอยู่ ให้ให้สิทธิ์กับ process context เดียวกับที่ทำ file operations (เช่น Terminal/iTerm, แอปที่ถูกเริ่มผ่าน LaunchAgent หรือโปรเซส SSH)

วิธีแก้ชั่วคราว: ย้ายไฟล์เข้า OpenClaw workspace (`~/.openclaw/workspace`) หากคุณต้องการหลีกเลี่ยงการให้สิทธิ์รายโฟลเดอร์

หากคุณกำลังทดสอบเรื่องสิทธิ์ ควรลงนามด้วยใบรับรองจริงเสมอ บิลด์แบบ ad-hoc ยอมรับได้เฉพาะสำหรับการรันในเครื่องอย่างรวดเร็วที่เรื่องสิทธิ์ไม่สำคัญ

## ที่เกี่ยวข้อง

  * [แอป macOS](</th/platforms/macos>)
  * [การลงนามบน macOS](</th/platforms/mac/signing>)


Was this useful?YesNo