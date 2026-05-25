---
title: Arcee AI
source_url: https://docs.openclaw.ai/th/providers/arcee
scraped_at: 2026-05-25
---

[Arcee AI](<https://arcee.ai>) ให้การเข้าถึงโมเดลตระกูล Trinity แบบ mixture-of-experts ผ่าน API ที่เข้ากันได้กับ OpenAI โมเดล Trinity ทั้งหมดอยู่ภายใต้สัญญาอนุญาต Apache 2.0

สามารถเข้าถึงโมเดล Arcee AI ได้โดยตรงผ่านแพลตฟอร์ม Arcee หรือผ่าน [OpenRouter](</th/providers/openrouter>)

คุณสมบัติ | ค่า  
---|---  
ผู้ให้บริการ | `arcee`  
การยืนยันตัวตน | `ARCEEAI_API_KEY` (โดยตรง) หรือ `OPENROUTER_API_KEY` (ผ่าน OpenRouter)  
API | เข้ากันได้กับ OpenAI  
URL ฐาน | `https://api.arcee.ai/api/v1` (โดยตรง) หรือ `https://openrouter.ai/api/v1` (OpenRouter)  
  
## เริ่มต้นใช้งาน

### โดยตรง (แพลตฟอร์ม Arcee)

* ### รับคีย์ API

สร้างคีย์ API ที่ [Arcee AI](<https://chat.arcee.ai/>)

* ### เรียกใช้การเริ่มต้นใช้งาน

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### ตั้งค่าโมเดลเริ่มต้น

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### ผ่าน OpenRouter

* ### รับคีย์ API

สร้างคีย์ API ที่ [OpenRouter](<https://openrouter.ai/keys>)

* ### เรียกใช้การเริ่มต้นใช้งาน

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### ตั้งค่าโมเดลเริ่มต้น

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

การอ้างอิงโมเดลเดียวกันใช้ได้ทั้งกับการตั้งค่าแบบโดยตรงและผ่าน OpenRouter (เช่น `arcee/trinity-large-thinking`)

## การตั้งค่าแบบไม่โต้ตอบ

### โดยตรง (แพลตฟอร์ม Arcee)

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### ผ่าน OpenRouter

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## แคตตาล็อกในตัว

ปัจจุบัน OpenClaw มาพร้อมกับแคตตาล็อก Arcee ที่รวมไว้ดังนี้:

การอ้างอิงโมเดล | ชื่อ | อินพุต | บริบท | ค่าใช้จ่าย (เข้า/ออก ต่อ 1M) | หมายเหตุ  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | text | 256K | $0.25 / $0.90 | โมเดลเริ่มต้น; เปิดใช้การให้เหตุผล  
`arcee/trinity-large-preview` | Trinity Large Preview | text | 128K | $0.25 / $1.00 | ใช้งานทั่วไป; 400B พารามิเตอร์, 13B ทำงานอยู่  
`arcee/trinity-mini` | Trinity Mini 26B | text | 128K | $0.045 / $0.15 | รวดเร็วและคุ้มค่า; การเรียกฟังก์ชัน  
  
## ฟีเจอร์ที่รองรับ

ฟีเจอร์ | รองรับ  
---|---  
การสตรีม | ใช่  
การใช้เครื่องมือ / การเรียกฟังก์ชัน | ใช่ (Trinity Mini, Trinity Large Preview)  
เอาต์พุตที่มีโครงสร้าง (โหมด JSON และ JSON schema) | ใช่  
การคิดแบบขยาย | ใช่ (Trinity Large Thinking; ปิดใช้เครื่องมือ)  
  
หมายเหตุเกี่ยวกับสภาพแวดล้อม

หาก Gateway ทำงานเป็น daemon (launchd/systemd) โปรดตรวจสอบให้แน่ใจว่า `ARCEEAI_API_KEY` (หรือ `OPENROUTER_API_KEY`) พร้อมใช้งานสำหรับโปรเซสนั้น (เช่น ใน `~/.openclaw/.env` หรือผ่าน `env.shellEnv`)

การกำหนดเส้นทาง OpenRouter

เมื่อใช้โมเดล Arcee ผ่าน OpenRouter จะใช้การอ้างอิงโมเดล `arcee/*` แบบเดียวกัน OpenClaw จัดการการกำหนดเส้นทางอย่างโปร่งใสตามตัวเลือกการยืนยันตัวตนของคุณ ดู [เอกสารผู้ให้บริการ OpenRouter](</th/providers/openrouter>) สำหรับรายละเอียดการกำหนดค่าเฉพาะของ OpenRouter

## ที่เกี่ยวข้อง

[**OpenRouter** เข้าถึงโมเดล Arcee และโมเดลอื่นๆ อีกมากมายผ่านคีย์ API เดียว ](</th/providers/openrouter>) [**การเลือกโมเดล** การเลือกผู้ให้บริการ การอ้างอิงโมเดล และพฤติกรรม failover ](</th/concepts/model-providers>)

Was this useful?YesNo