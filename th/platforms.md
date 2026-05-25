---
title: แพลตฟอร์ม
source_url: https://docs.openclaw.ai/th/platforms
scraped_at: 2026-05-25
---

OpenClaw core เขียนด้วย TypeScript **Node คือรันไทม์ที่แนะนำ** ไม่แนะนำให้ใช้ Bun สำหรับ Gateway — มีปัญหาที่ทราบกับช่องทาง WhatsApp และ Telegram; ดูรายละเอียดที่ [Bun (ทดลอง)](</th/install/bun>)

มีแอปคู่หูสำหรับ macOS (แอปแถบเมนู) และ Node มือถือ (iOS/Android) มีแผนสำหรับแอปคู่หูบน Windows และ Linux แต่ Gateway รองรับเต็มรูปแบบแล้วในปัจจุบัน มีแผนสำหรับแอปคู่หูแบบเนทีฟบน Windows เช่นกัน; แนะนำให้ใช้ Gateway ผ่าน WSL2

## เลือกระบบปฏิบัติการของคุณ

  * macOS: [macOS](</th/platforms/macos>)
  * iOS: [iOS](</th/platforms/ios>)
  * Android: [Android](</th/platforms/android>)
  * Windows: [Windows](</th/platforms/windows>)
  * Linux: [Linux](</th/platforms/linux>)


## VPS และโฮสติ้ง

  * ศูนย์รวม VPS: [โฮสติ้ง VPS](</th/vps>)
  * [Fly.io](<http://Fly.io>): [Fly.io](</th/install/fly>)
  * Hetzner (Docker): [Hetzner](</th/install/hetzner>)
  * GCP (Compute Engine): [GCP](</th/install/gcp>)
  * Azure (Linux VM): [Azure](</th/install/azure>)
  * exe.dev (VM + HTTPS proxy): [exe.dev](</th/install/exe-dev>)


## ลิงก์ทั่วไป

  * คู่มือการติดตั้ง: [เริ่มต้นใช้งาน](</th/start/getting-started>)
  * คู่มือปฏิบัติงาน Gateway: [Gateway](</th/gateway>)
  * การกำหนดค่า Gateway: [การกำหนดค่า](</th/gateway/configuration>)
  * สถานะบริการ: `openclaw gateway status`


## การติดตั้งบริการ Gateway (CLI)

ใช้รายการใดรายการหนึ่งต่อไปนี้ (รองรับทั้งหมด):

  * วิซาร์ด (แนะนำ): `openclaw onboard --install-daemon`
  * โดยตรง: `openclaw gateway install`
  * ขั้นตอนการกำหนดค่า: `openclaw configure` → เลือก **บริการ Gateway**
  * ซ่อมแซม/ย้ายข้อมูล: `openclaw doctor` (เสนอให้ติดตั้งหรือแก้ไขบริการ)


เป้าหมายของบริการขึ้นอยู่กับระบบปฏิบัติการ:

  * macOS: LaunchAgent (`ai.openclaw.gateway` หรือ `ai.openclaw.<profile>`; แบบเดิม `com.openclaw.*`)
  * Linux/WSL2: บริการผู้ใช้ systemd (`openclaw-gateway[-<profile>].service`)
  * Windows แบบเนทีฟ: Scheduled Task (`OpenClaw Gateway` หรือ `OpenClaw Gateway (<profile>)`) พร้อมรายการเข้าสู่ระบบในโฟลเดอร์ Startup ต่อผู้ใช้เป็นทางเลือกสำรอง หากการสร้างงานถูกปฏิเสธ


## ที่เกี่ยวข้อง

  * [ภาพรวมการติดตั้ง](</th/install>)
  * [แอป macOS](</th/platforms/macos>)
  * [แอป iOS](</th/platforms/ios>)


Was this useful?YesNo