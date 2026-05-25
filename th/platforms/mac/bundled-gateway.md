---
title: Gateway บน macOS
source_url: https://docs.openclaw.ai/th/platforms/mac/bundled-gateway
scraped_at: 2026-05-25
---

OpenClaw.app ไม่ได้รวม Node/Bun หรือรันไทม์ Gateway มาให้อีกต่อไป แอป macOS คาดว่าจะมีการติดตั้ง CLI `openclaw` แบบ **ภายนอก** ไม่เริ่ม Gateway เป็น กระบวนการลูก และจัดการบริการ launchd รายผู้ใช้เพื่อให้ Gateway ทำงานอยู่เสมอ (หรือเชื่อมต่อกับ Gateway ภายในเครื่องที่มีอยู่แล้ว หากมีตัวหนึ่งกำลังทำงานอยู่)

## ติดตั้ง CLI (จำเป็นสำหรับโหมดภายในเครื่อง)

Node 24 เป็นรันไทม์เริ่มต้นบน Mac ส่วน Node 22 LTS ซึ่งปัจจุบันคือ `22.16+` ยังคงใช้งานได้เพื่อความเข้ากันได้ จากนั้นติดตั้ง `openclaw` แบบโกลบอล:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

ปุ่ม **ติดตั้ง CLI** ของแอป macOS จะเรียกใช้ขั้นตอนการติดตั้งแบบโกลบอลเดียวกับที่แอป ใช้ภายใน: แอปจะเลือก npm ก่อน แล้วจึงเป็น pnpm แล้วจึงเป็น bun หากนั่นเป็น ตัวจัดการแพ็กเกจเดียวที่ตรวจพบ Node ยังคงเป็นรันไทม์ Gateway ที่แนะนำ

## launchd (Gateway ในฐานะ LaunchAgent)

ป้ายกำกับ:

  * `ai.openclaw.gateway` (หรือ `ai.openclaw.<profile>`; `com.openclaw.*` แบบเดิมอาจยังคงอยู่)


ตำแหน่ง Plist (รายผู้ใช้):

  * `~/Library/LaunchAgents/ai.openclaw.gateway.plist` (หรือ `~/Library/LaunchAgents/ai.openclaw.<profile>.plist`)


ตัวจัดการ:

  * แอป macOS เป็นเจ้าของการติดตั้ง/อัปเดต LaunchAgent ในโหมดภายในเครื่อง
  * CLI ก็สามารถติดตั้งได้เช่นกัน: `openclaw gateway install`


ลักษณะการทำงาน:

  * "OpenClaw Active" เปิด/ปิดใช้งาน LaunchAgent
  * การออกจากแอป **ไม่** หยุด gateway (launchd จะคงให้ทำงานต่อ)
  * หาก Gateway กำลังทำงานอยู่แล้วบนพอร์ตที่กำหนดค่าไว้ แอปจะเชื่อมต่อกับ มันแทนที่จะเริ่มตัวใหม่


การบันทึก日志:

  * stdout/err ของ launchd: `/tmp/openclaw/openclaw-gateway.log`


## ความเข้ากันได้ของเวอร์ชัน

แอป macOS ตรวจสอบเวอร์ชัน gateway เทียบกับเวอร์ชันของตัวเอง หากทั้งสอง ไม่เข้ากัน ให้อัปเดต CLI แบบโกลบอลให้ตรงกับเวอร์ชันของแอป

## การตรวจสอบเบื้องต้น

bashCopy code
[code]
    openclaw --version OPENCLAW_SKIP_CHANNELS=1 \OPENCLAW_SKIP_CANVAS_HOST=1 \openclaw gateway --port 18999 --bind loopback
[/code]

จากนั้น:

bashCopy code
[code]
    openclaw gateway call health --url ws://127.0.0.1:18999 --timeout 3000
[/code]

## ที่เกี่ยวข้อง

  * [แอป macOS](</th/platforms/macos>)
  * [คู่มือปฏิบัติการ Gateway](</th/gateway>)


Was this useful?YesNo