---
title: Nix
source_url: https://docs.openclaw.ai/th/install/nix
scraped_at: 2026-05-25
---

ติดตั้ง OpenClaw แบบประกาศด้วย **[nix-openclaw](<https://github.com/openclaw/nix-openclaw>)** \- โมดูล Home Manager อย่างเป็นทางการที่มาพร้อมทุกอย่างครบถ้วน

## สิ่งที่คุณจะได้

  * Gateway + แอป macOS + เครื่องมือ (whisper, spotify, cameras) -- ทั้งหมดถูกตรึงเวอร์ชันไว้
  * บริการ launchd ที่ยังทำงานต่อหลังรีบูต
  * ระบบ Plugin พร้อมการกำหนดค่าแบบประกาศ
  * ย้อนกลับได้ทันที: `home-manager switch --rollback`


## เริ่มต้นอย่างรวดเร็ว

* ### ติดตั้ง Determinate Nix

หากยังไม่ได้ติดตั้ง Nix ให้ทำตามคำแนะนำของ [ตัวติดตั้ง Determinate Nix](<https://github.com/DeterminateSystems/nix-installer>)

* ### สร้าง flake ภายในเครื่อง

ใช้เทมเพลตแบบ agent-first จากรีโป nix-openclaw:

bashCopy code
[code]
    mkdir -p ~/code/openclaw-local# Copy templates/agent-first/flake.nix from the nix-openclaw repo
[/code]

* ### กำหนดค่าความลับ

ตั้งค่าโทเค็นบอทรับส่งข้อความและคีย์ API ของผู้ให้บริการโมเดล ไฟล์ข้อความธรรมดาที่ `~/.secrets/` ใช้งานได้ดี

* ### กรอก placeholder ในเทมเพลตและสลับใช้งาน

bashCopy code
[code]
    home-manager switch
[/code]

* ### ตรวจสอบ

ยืนยันว่าบริการ launchd กำลังทำงานและบอทของคุณตอบกลับข้อความ

ดู [README ของ nix-openclaw](<https://github.com/openclaw/nix-openclaw>) สำหรับตัวเลือกโมดูลและตัวอย่างทั้งหมด

## พฤติกรรม runtime ของโหมด Nix

เมื่อมีการตั้งค่า `OPENCLAW_NIX_MODE=1` (อัตโนมัติเมื่อใช้ nix-openclaw) OpenClaw จะเข้าสู่โหมดกำหนดแน่นอนสำหรับการติดตั้งที่จัดการด้วย Nix แพ็กเกจ Nix อื่นสามารถตั้งค่าโหมดเดียวกันได้เช่นกัน; nix-openclaw คือข้อมูลอ้างอิงอย่างเป็นทางการ

คุณยังสามารถตั้งค่าด้วยตนเองได้:

bashCopy code
[code]
    export OPENCLAW_NIX_MODE=1
[/code]

บน macOS แอป GUI จะไม่รับตัวแปรสภาพแวดล้อมของเชลล์โดยอัตโนมัติ ให้เปิดใช้โหมด Nix ผ่าน defaults แทน:

bashCopy code
[code]
    defaults write ai.openclaw.mac openclaw.nixMode -bool true
[/code]

### สิ่งที่เปลี่ยนในโหมด Nix

  * โฟลว์ติดตั้งอัตโนมัติและแก้ไขตัวเองถูกปิดใช้งาน
  * `openclaw.json` จะถูกถือว่าเปลี่ยนแปลงไม่ได้ ค่าเริ่มต้นที่ได้จากการเริ่มทำงานจะคงอยู่เฉพาะใน runtime และตัวเขียนค่ากำหนด เช่น setup, onboarding, `openclaw update` ที่แก้ไขค่า, การติดตั้ง/อัปเดต/ถอนการติดตั้ง/เปิดใช้ Plugin, `doctor --fix`, `doctor --generate-gateway-token` และ `openclaw config set` จะปฏิเสธการแก้ไขไฟล์
  * Agent ควรแก้ไขซอร์ส Nix แทน สำหรับ nix-openclaw ให้ใช้ [Quick Start](<https://github.com/openclaw/nix-openclaw#quick-start>) แบบ agent-first และตั้งค่าคอนฟิกใต้ `programs.openclaw.config` หรือ `instances.<name>.config`
  * dependency ที่ขาดหายจะแสดงข้อความแก้ไขเฉพาะ Nix
  * UI แสดงแบนเนอร์โหมด Nix แบบอ่านอย่างเดียว


### พาธของคอนฟิกและสถานะ

OpenClaw อ่านคอนฟิก JSON5 จาก `OPENCLAW_CONFIG_PATH` และเก็บข้อมูลที่เปลี่ยนแปลงได้ใน `OPENCLAW_STATE_DIR` เมื่อทำงานภายใต้ Nix ให้ตั้งค่าเหล่านี้อย่างชัดเจนไปยังตำแหน่งที่จัดการด้วย Nix เพื่อให้สถานะ runtime และคอนฟิกไม่อยู่ใน store ที่เปลี่ยนแปลงไม่ได้

ตัวแปร | ค่าเริ่มต้น  
---|---  
`OPENCLAW_HOME` | `HOME` / `USERPROFILE` / `os.homedir()`  
`OPENCLAW_STATE_DIR` | `~/.openclaw`  
`OPENCLAW_CONFIG_PATH` | `$OPENCLAW_STATE_DIR/openclaw.json`  
  
### การค้นหา PATH ของบริการ

บริการ Gateway ของ launchd/systemd จะค้นหาไบนารีใน Nix profile โดยอัตโนมัติ เพื่อให้ plugins และเครื่องมือที่เรียกใช้งาน executable ที่ติดตั้งผ่าน `nix` ด้วยเชลล์ทำงานได้โดยไม่ต้อง ตั้งค่า PATH ด้วยตนเอง:

  * เมื่อมีการตั้งค่า `NIX_PROFILES` ทุก entry จะถูกเพิ่มลงใน PATH ของบริการตาม ลำดับความสำคัญจากขวาไปซ้าย (ตรงกับลำดับความสำคัญของ Nix shell - ขวาสุดชนะ)
  * เมื่อไม่ได้ตั้งค่า `NIX_PROFILES` จะเพิ่ม `~/.nix-profile/bin` เป็น fallback


สิ่งนี้ใช้กับสภาพแวดล้อมบริการทั้ง macOS launchd และ Linux systemd

## ที่เกี่ยวข้อง

[**nix-openclaw** โมดูล Home Manager ที่เป็นแหล่งข้อมูลหลักและคู่มือการตั้งค่าเต็มรูปแบบ ](<https://github.com/openclaw/nix-openclaw>) [**ตัวช่วยตั้งค่า** คำแนะนำการตั้งค่า CLI แบบไม่ใช้ Nix ](</th/start/wizard>) [**Docker** การตั้งค่าแบบคอนเทนเนอร์เป็นทางเลือกที่ไม่ใช้ Nix ](</th/install/docker>) [**การอัปเดต** การอัปเดตการติดตั้งที่จัดการด้วย Home Manager ควบคู่กับแพ็กเกจ ](</th/install/updating>)

Was this useful?YesNo