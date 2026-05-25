---
title: Honcho memory
source_url: https://docs.openclaw.ai/th/concepts/memory-honcho
scraped_at: 2026-05-25
---

[Honcho](<https://honcho.dev>) เพิ่ม memory แบบ AI-native ให้กับ OpenClaw โดยจะเก็บ บทสนทนาไว้ในบริการเฉพาะ และสร้างแบบจำลองผู้ใช้และเอเจนต์ตามเวลา ทำให้เอเจนต์ของคุณมีบริบทข้ามเซสชันที่ไปไกลกว่าไฟล์ Markdown ของ workspace

## สิ่งที่มันมีให้

  * **memory ข้ามเซสชัน** \-- บทสนทนาจะถูกเก็บหลังจากทุกเทิร์น ดังนั้น บริบทจะคงอยู่ข้ามการรีเซ็ตเซสชัน Compaction และการสลับแชนแนล
  * **การสร้างแบบจำลองผู้ใช้** \-- Honcho ดูแลโปรไฟล์ของผู้ใช้แต่ละคน (ความชอบ ข้อเท็จจริง รูปแบบการสื่อสาร) และของเอเจนต์ (บุคลิก ลักษณะพฤติกรรม ที่เรียนรู้มา)
  * **semantic search** \-- ค้นหาจาก observations ของบทสนทนาในอดีต ไม่ใช่ แค่เซสชันปัจจุบัน
  * **การรับรู้หลายเอเจนต์** \-- parent agents จะติดตาม sub-agents ที่ spawn ขึ้นโดยอัตโนมัติ โดย parent จะถูกเพิ่มเป็น observers ใน child sessions


## tools ที่มีให้

Honcho ลงทะเบียน tools ที่เอเจนต์สามารถใช้ระหว่างบทสนทนา:

**การดึงข้อมูล (เร็ว, ไม่มีการเรียก LLM):**

Tool | สิ่งที่ทำ  
---|---  
`honcho_context` | ตัวแทนผู้ใช้แบบเต็มข้ามเซสชัน  
`honcho_search_conclusions` | semantic search บน conclusions ที่เก็บไว้  
`honcho_search_messages` | ค้นหาข้อความข้ามเซสชัน (กรองตามผู้ส่ง วันที่)  
`honcho_session` | ประวัติและสรุปของเซสชันปัจจุบัน  
  
**Q &A (ขับเคลื่อนด้วย LLM):**

Tool | สิ่งที่ทำ  
---|---  
`honcho_ask` | ถามเกี่ยวกับผู้ใช้ ใช้ `depth='quick'` สำหรับข้อเท็จจริง และ `'thorough'` สำหรับการสังเคราะห์  
  
## เริ่มต้นใช้งาน

ติดตั้ง Plugin และรันการตั้งค่า:

bashCopy code
[code]
    openclaw plugins install @honcho-ai/openclaw-honchoopenclaw honcho setupopenclaw gateway --force
[/code]

คำสั่ง setup จะถามข้อมูลรับรอง API ของคุณ เขียน config และ ย้ายไฟล์ memory ของ workspace ที่มีอยู่เดิมได้ตามตัวเลือก

## การกำหนดค่า

การตั้งค่าอยู่ภายใต้ `plugins.entries["openclaw-honcho"].config`:

json5Copy code
[code]
    {  plugins: {    entries: {      "openclaw-honcho": {        config: {          apiKey: "your-api-key", // ละไว้ได้สำหรับ self-hosted          workspaceId: "openclaw", // การแยก memory          baseUrl: "https://api.honcho.dev",        },      },    },  },}
[/code]

สำหรับอินสแตนซ์ self-hosted ให้ชี้ `baseUrl` ไปยังเซิร์ฟเวอร์ภายในเครื่องของคุณ (เช่น `http://localhost:8000`) และไม่ต้องระบุ API key

## การย้าย memory ที่มีอยู่เดิม

หากคุณมีไฟล์ memory ของ workspace อยู่แล้ว (`USER.md`, `MEMORY.md`, `IDENTITY.md`, `memory/`, `canvas/`) คำสั่ง `openclaw honcho setup` จะตรวจพบและ เสนอให้ย้ายไฟล์เหล่านั้น

## การทำงานของมัน

หลังจากแต่ละ AI turn บทสนทนาจะถูกเก็บลงใน Honcho ทั้งข้อความของผู้ใช้และ เอเจนต์จะถูกสังเกต ทำให้ Honcho สามารถสร้างและปรับปรุงแบบจำลองของตนต่อไปได้ ตามเวลา

ระหว่างบทสนทนา tools ของ Honcho จะ query บริการในระยะ `before_prompt_build` และแทรกบริบทที่เกี่ยวข้องก่อนที่โมเดลจะเห็น prompt วิธีนี้ช่วยให้ ขอบเขตของเทิร์นแม่นยำและการเรียกคืนมีความเกี่ยวข้อง

## Honcho เทียบกับ memory ในตัว

| ในตัว / QMD | Honcho  
---|---|---  
**การจัดเก็บ** | ไฟล์ Markdown ของ workspace | บริการเฉพาะ (ภายในเครื่องหรือโฮสต์)  
**ข้ามเซสชัน** | ผ่านไฟล์ memory | อัตโนมัติ มีในตัว  
**การสร้างแบบจำลองผู้ใช้** | ทำเอง (เขียนลง `MEMORY.md`) | โปรไฟล์อัตโนมัติ  
**การค้นหา** | Vector + keyword (hybrid) | semantic บน observations  
**หลายเอเจนต์** | ไม่มีการติดตาม | รับรู้ parent/child  
**Dependencies** | ไม่มี (ในตัว) หรือ QMD binary | ติดตั้ง Plugin  
  
Honcho และระบบ memory ในตัวสามารถทำงานร่วมกันได้ เมื่อกำหนดค่า QMD แล้ว จะมี tools เพิ่มเติมสำหรับค้นหาไฟล์ Markdown ภายในเครื่องควบคู่ไปกับ memory ข้ามเซสชันของ Honcho

## คำสั่ง CLI

bashCopy code
[code]
    openclaw honcho setup                        # กำหนดค่า API key และย้ายไฟล์openclaw honcho status                       # ตรวจสอบสถานะการเชื่อมต่อopenclaw honcho ask <question>               # query Honcho เกี่ยวกับผู้ใช้openclaw honcho search <query> [-k N] [-d D] # semantic search บน memory
[/code]

## อ่านเพิ่มเติม

  * [ซอร์สโค้ดของ Plugin](<https://github.com/plastic-labs/openclaw-honcho>)
  * [เอกสาร Honcho](<https://docs.honcho.dev>)
  * [คู่มือการผสานรวม Honcho กับ OpenClaw](<https://docs.honcho.dev/v3/guides/integrations/openclaw>)
  * [Memory](</th/concepts/memory>) \-- ภาพรวม memory ของ OpenClaw
  * [Context Engines](</th/concepts/context-engine>) \-- วิธีทำงานของ Plugin context engines


## ที่เกี่ยวข้อง

  * [Memory overview](</th/concepts/memory>)
  * [Builtin memory engine](</th/concepts/memory-builtin>)
  * [QMD memory engine](</th/concepts/memory-qmd>)


Was this useful?YesNo