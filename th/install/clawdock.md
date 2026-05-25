---
title: ClawDock
source_url: https://docs.openclaw.ai/th/install/clawdock
scraped_at: 2026-05-25
---

ClawDock เป็นเลเยอร์ตัวช่วย shell ขนาดเล็กสำหรับการติดตั้ง OpenClaw แบบใช้ Docker

ช่วยให้คุณใช้คำสั่งสั้น ๆ เช่น `clawdock-start`, `clawdock-dashboard` และ `clawdock-fix-token` แทนการเรียก `docker compose ...` ที่ยาวกว่า

หากคุณยังไม่ได้ตั้งค่า Docker ให้เริ่มที่ [Docker](</th/install/docker>)

## ติดตั้ง

ใช้พาธตัวช่วยมาตรฐาน:

bashCopy code
[code]
    mkdir -p ~/.clawdock && curl -sL https://raw.githubusercontent.com/openclaw/openclaw/main/scripts/clawdock/clawdock-helpers.sh -o ~/.clawdock/clawdock-helpers.shecho 'source ~/.clawdock/clawdock-helpers.sh' >> ~/.zshrc && source ~/.zshrc
[/code]

หากก่อนหน้านี้คุณติดตั้ง ClawDock จาก `scripts/shell-helpers/clawdock-helpers.sh` ให้ติดตั้งใหม่จากพาธใหม่ `scripts/clawdock/clawdock-helpers.sh` พาธ GitHub raw เดิมถูกนำออกแล้ว

## สิ่งที่คุณจะได้

### การทำงานพื้นฐาน

คำสั่ง | คำอธิบาย  
---|---  
`clawdock-start` | เริ่ม Gateway  
`clawdock-stop` | หยุด Gateway  
`clawdock-restart` | รีสตาร์ท Gateway  
`clawdock-status` | ตรวจสอบสถานะ container  
`clawdock-logs` | ติดตาม log ของ Gateway  
  
### การเข้าถึง container

คำสั่ง | คำอธิบาย  
---|---  
`clawdock-shell` | เปิด shell ภายใน container ของ Gateway  
`clawdock-cli <command>` | เรียกใช้คำสั่ง OpenClaw CLI ใน Docker  
`clawdock-exec <command>` | ดำเนินการคำสั่งใด ๆ ภายใน container  
  
### Web UI และการจับคู่

คำสั่ง | คำอธิบาย  
---|---  
`clawdock-dashboard` | เปิด URL ของ Control UI  
`clawdock-devices` | แสดงรายการการจับคู่อุปกรณ์ที่รอดำเนินการ  
`clawdock-approve <id>` | อนุมัติคำขอจับคู่  
  
### การตั้งค่าและการบำรุงรักษา

คำสั่ง | คำอธิบาย  
---|---  
`clawdock-fix-token` | กำหนดค่า token ของ Gateway ภายใน container  
`clawdock-update` | pull, build ใหม่ และรีสตาร์ท  
`clawdock-rebuild` | build อิมเมจ Docker ใหม่เท่านั้น  
`clawdock-clean` | ลบ container และ volume  
  
### ยูทิลิตี

คำสั่ง | คำอธิบาย  
---|---  
`clawdock-health` | เรียกใช้การตรวจสุขภาพของ Gateway  
`clawdock-token` | พิมพ์ token ของ Gateway  
`clawdock-cd` | ไปยังไดเรกทอรีโปรเจกต์ OpenClaw  
`clawdock-config` | เปิด `~/.openclaw`  
`clawdock-show-config` | พิมพ์ไฟล์ config พร้อมปิดบังค่าที่ละเอียดอ่อน  
`clawdock-workspace` | เปิดไดเรกทอรี workspace  
  
## ขั้นตอนครั้งแรก

bashCopy code
[code]
    clawdock-startclawdock-fix-tokenclawdock-dashboard
[/code]

หากเบราว์เซอร์แจ้งว่าจำเป็นต้องจับคู่:

bashCopy code
[code]
    clawdock-devicesclawdock-approve <request-id>
[/code]

## Config และ secret

ClawDock ทำงานร่วมกับการแยก config ของ Docker แบบเดียวกับที่อธิบายไว้ใน [Docker](</th/install/docker>):

  * `<project>/.env` สำหรับค่าที่เฉพาะกับ Docker เช่น ชื่ออิมเมจ, port และ token ของ Gateway
  * `~/.openclaw/.env` สำหรับคีย์ผู้ให้บริการและ token ของ bot ที่อิง env
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` สำหรับ auth ของผู้ให้บริการแบบ OAuth/API-key ที่จัดเก็บไว้
  * `~/.openclaw/openclaw.json` สำหรับ config พฤติกรรม


ใช้ `clawdock-show-config` เมื่อต้องการตรวจสอบไฟล์ `.env` และ `openclaw.json` อย่างรวดเร็ว คำสั่งนี้จะปิดบังค่า `.env` ในเอาต์พุตที่พิมพ์ออกมา

## ที่เกี่ยวข้อง

[**Docker** การติดตั้ง Docker มาตรฐานสำหรับ OpenClaw ](</th/install/docker>) [**รันไทม์ Docker VM** รันไทม์ VM ที่จัดการโดย Docker สำหรับการแยกที่แข็งแกร่งขึ้น ](</th/install/docker-vm-runtime>) [**การอัปเดต** การอัปเดตแพ็กเกจ OpenClaw และบริการที่จัดการอยู่ ](</th/install/updating>)

Was this useful?YesNo