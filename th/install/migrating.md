---
title: คู่มือการย้ายข้อมูล
source_url: https://docs.openclaw.ai/th/install/migrating
scraped_at: 2026-05-25
---

OpenClaw รองรับเส้นทางการย้ายข้อมูลสามแบบ: นำเข้าจากระบบเอเจนต์อื่น ย้ายการติดตั้งที่มีอยู่ไปยังเครื่องใหม่ และอัปเกรด Plugin แบบแทนที่เดิม

## นำเข้าจากระบบเอเจนต์อื่น

ใช้ผู้ให้บริการการย้ายข้อมูลที่รวมมาให้เพื่อนำคำสั่ง, เซิร์ฟเวอร์ MCP, skills, การตั้งค่าโมเดล และ API keys (แบบเลือกเปิดใช้) เข้ามาใน OpenClaw แผนจะแสดงตัวอย่างก่อนมีการเปลี่ยนแปลงใดๆ ความลับจะถูกปกปิดในรายงาน และการใช้แผนจะมีข้อมูลสำรองที่ผ่านการยืนยันรองรับ

[**Migrating from Claude** นำเข้าสถานะของ Claude Code และ Claude Desktop รวมถึง `CLAUDE.md`, เซิร์ฟเวอร์ MCP, skills และคำสั่งของโปรเจ็กต์ ](</th/install/migrating-claude>) [**Migrating from Hermes** นำเข้าการตั้งค่า Hermes, providers, เซิร์ฟเวอร์ MCP, memory, skills และคีย์ `.env` ที่รองรับ ](</th/install/migrating-hermes>)

จุดเข้าใช้งาน CLI คือ [`openclaw migrate`](</th/cli/migrate>) Onboarding ยังสามารถเสนอการย้ายข้อมูลได้เมื่อพบแหล่งที่มาที่รู้จัก (`openclaw onboard --flow import`)

## ย้าย OpenClaw ไปยังเครื่องใหม่

คัดลอก **ไดเรกทอรีสถานะ** (`~/.openclaw/` โดยค่าเริ่มต้น) และ **workspace** ของคุณเพื่อคงไว้ซึ่ง:

  * **การตั้งค่า** — `openclaw.json` และการตั้งค่า Gateway ทั้งหมด
  * **การยืนยันตัวตน** — `auth-profiles.json` รายเอเจนต์ (API keys รวมถึง OAuth) พร้อมสถานะของช่องทางหรือ provider ใดๆ ภายใต้ `credentials/`
  * **เซสชัน** — ประวัติการสนทนาและสถานะเอเจนต์
  * **สถานะช่องทาง** — การเข้าสู่ระบบ WhatsApp, เซสชัน Telegram และสิ่งที่คล้ายกัน
  * **ไฟล์ workspace** — `MEMORY.md`, `USER.md`, skills และ prompts


### ขั้นตอนการย้ายข้อมูล

* ### Stop the gateway and back up

บนเครื่อง **เก่า** ให้หยุด Gateway เพื่อไม่ให้ไฟล์เปลี่ยนระหว่างการคัดลอก จากนั้นเก็บถาวร:

bashCopy code
[code]
    openclaw gateway stopcd ~tar -czf openclaw-state.tgz .openclaw
[/code]

หากคุณใช้หลายโปรไฟล์ (เช่น `~/.openclaw-work`) ให้เก็บถาวรแต่ละโปรไฟล์แยกกัน

* ### Install OpenClaw on the new machine

[ติดตั้ง](</th/install>) CLI (และ Node หากจำเป็น) บนเครื่องใหม่ ไม่เป็นไรหาก onboarding สร้าง `~/.openclaw/` ใหม่ คุณจะเขียนทับในขั้นตอนถัดไป

* ### Copy state directory and workspace

โอนย้ายไฟล์เก็บถาวรผ่าน `scp`, `rsync -a` หรือไดรฟ์ภายนอก แล้วแตกไฟล์:

bashCopy code
[code]
    cd ~tar -xzf openclaw-state.tgz
[/code]

ตรวจสอบให้แน่ใจว่าได้รวมไดเรกทอรีที่ซ่อนไว้แล้ว และความเป็นเจ้าของไฟล์ตรงกับผู้ใช้ที่จะเรียกใช้ Gateway

* ### รัน doctor และตรวจสอบ

บนเครื่องใหม่ ให้รัน [Doctor](</th/gateway/doctor>) เพื่อใช้การย้ายข้อมูลการกำหนดค่าและซ่อมแซมบริการ:

bashCopy code
[code]
    openclaw doctoropenclaw gateway restartopenclaw status
[/code]

หาก Telegram หรือ Discord ใช้ค่า env fallback เริ่มต้น (`TELEGRAM_BOT_TOKEN` หรือ `DISCORD_BOT_TOKEN`) ให้ตรวจสอบว่า state-dir `.env` ที่ย้ายข้อมูลมาแล้วมีคีย์เหล่านั้นโดยไม่พิมพ์ค่าลับออกมา:

bashCopy code
[code]
    awk -F= '/^(TELEGRAM_BOT_TOKEN|DISCORD_BOT_TOKEN)=/ { print $1 "=present" }' ~/.openclaw/.env
[/code]

`openclaw doctor` ยังเตือนเมื่อบัญชี Telegram หรือ Discord เริ่มต้นที่เปิดใช้งานไม่มีโทเค็นที่กำหนดค่าไว้ และตัวแปร env ที่ตรงกันไม่พร้อมใช้งานสำหรับกระบวนการ doctor

### ข้อผิดพลาดที่พบบ่อย

โปรไฟล์หรือ state-dir ไม่ตรงกัน

หาก gateway เก่าใช้ `--profile` หรือ `OPENCLAW_STATE_DIR` แต่ gateway ใหม่ไม่ได้ใช้ แชนเนลจะแสดงเหมือนออกจากระบบแล้วและเซสชันจะว่างเปล่า ให้เริ่ม gateway ด้วยโปรไฟล์หรือ state-dir **เดียวกัน** ที่คุณย้ายข้อมูลมา จากนั้นรัน `openclaw doctor` อีกครั้ง

คัดลอกเฉพาะ openclaw.json

ไฟล์กำหนดค่าเพียงอย่างเดียวไม่เพียงพอ โปรไฟล์การยืนยันตัวตนของโมเดลอยู่ภายใต้ `agents/<agentId>/agent/auth-profiles.json` และสถานะของแชนเนลกับผู้ให้บริการอยู่ภายใต้ `credentials/` ให้ย้ายข้อมูลไดเรกทอรีสถานะ **ทั้งหมด** เสมอ

สิทธิ์และความเป็นเจ้าของ

หากคุณคัดลอกในฐานะ root หรือเปลี่ยนผู้ใช้ gateway อาจอ่านข้อมูลประจำตัวไม่สำเร็จ ตรวจสอบให้แน่ใจว่าไดเรกทอรีสถานะและ workspace เป็นของผู้ใช้ที่รัน gateway

โหมดรีโมต

หาก UI ของคุณชี้ไปที่ gateway **รีโมต** โฮสต์รีโมตจะเป็นเจ้าของเซสชันและ workspace ให้ย้ายข้อมูลโฮสต์ gateway เอง ไม่ใช่แล็ปท็อปเครื่องโลคัลของคุณ ดู [FAQ](</th/help/faq#where-things-live-on-disk>)

ความลับในข้อมูลสำรอง

ไดเรกทอรีสถานะมีโปรไฟล์การยืนยันตัวตน ข้อมูลประจำตัวของแชนเนล และสถานะอื่นของผู้ให้บริการ จัดเก็บข้อมูลสำรองแบบเข้ารหัส หลีกเลี่ยงช่องทางถ่ายโอนที่ไม่ปลอดภัย และหมุนเวียนคีย์หากคุณสงสัยว่ามีการเปิดเผย

### เช็กลิสต์การตรวจสอบ

บนเครื่องใหม่ ให้ยืนยันว่า:

  * [ ] `openclaw status` แสดงว่า gateway กำลังทำงาน
  * [ ] แชนเนลยังเชื่อมต่ออยู่ (ไม่จำเป็นต้องจับคู่อีกครั้ง)
  * [ ] แดชบอร์ดเปิดได้และแสดงเซสชันที่มีอยู่
  * [ ] มีไฟล์ workspace (memory, configs) อยู่ครบ


## อัปเกรด Plugin แบบแทนที่

การอัปเกรด Plugin แบบแทนที่จะคง plugin id และคีย์การกำหนดค่าเดิมไว้ แต่อาจย้ายสถานะบนดิสก์เข้าสู่เลย์เอาต์ปัจจุบัน คู่มือการอัปเกรดเฉพาะ Plugin จะอยู่ควบคู่กับแชนเนลของ Plugin นั้น:

  * [การย้ายข้อมูล Matrix](</th/channels/matrix-migration>): ขีดจำกัดการกู้คืนสถานะที่เข้ารหัส พฤติกรรมสแนปช็อตอัตโนมัติ และคำสั่งกู้คืนด้วยตนเอง


## ที่เกี่ยวข้อง

  * [`openclaw migrate`](</th/cli/migrate>): ข้อมูลอ้างอิง CLI สำหรับการนำเข้าข้ามระบบ
  * [ภาพรวมการติดตั้ง](</th/install>): วิธีการติดตั้งทั้งหมด
  * [Doctor](</th/gateway/doctor>): การตรวจสุขภาพหลังย้ายข้อมูล
  * [ถอนการติดตั้ง](</th/install/uninstall>): การลบ OpenClaw อย่างหมดจด


Was this useful?YesNo