---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/th/providers/kilocode
scraped_at: 2026-05-25
---

Kilo Gateway ให้บริการ **API แบบรวมศูนย์** ที่ส่งต่อคำขอไปยังโมเดลจำนวนมากเบื้องหลัง endpoint และ API key เดียว รองรับการทำงานแบบเข้ากันได้กับ OpenAI ดังนั้น OpenAI SDK ส่วนใหญ่จึงใช้งานได้ด้วยการเปลี่ยน base URL

คุณสมบัติ | ค่า  
---|---  
ผู้ให้บริการ | `kilocode`  
การยืนยันตัวตน | `KILOCODE_API_KEY`  
API | เข้ากันได้กับ OpenAI  
URL ฐาน | `https://api.kilo.ai/api/gateway/`  
  
## เริ่มต้นใช้งาน

* ### สร้างบัญชี

ไปที่ [app.kilo.ai](<https://app.kilo.ai>) ลงชื่อเข้าใช้หรือสร้างบัญชี จากนั้นไปที่ API Keys แล้วสร้างคีย์ใหม่

* ### เรียกใช้ onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

หรือกำหนดตัวแปรสภาพแวดล้อมโดยตรง:

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### ตรวจสอบว่าโมเดลพร้อมใช้งาน

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## โมเดลเริ่มต้น

โมเดลเริ่มต้นคือ `kilocode/kilo/auto` ซึ่งเป็นโมเดล smart-routing ที่ผู้ให้บริการเป็นเจ้าของและจัดการโดย Kilo Gateway

## แค็ตตาล็อกในตัว

OpenClaw ค้นหาโมเดลที่พร้อมใช้งานจาก Kilo Gateway แบบไดนามิกเมื่อเริ่มต้นระบบ ใช้ `/models kilocode` เพื่อดูรายการโมเดลทั้งหมดที่บัญชีของคุณใช้ได้

โมเดลใดก็ตามที่พร้อมใช้งานบน gateway สามารถใช้กับ prefix `kilocode/` ได้:

Ref ของโมเดล | หมายเหตุ  
---|---  
`kilocode/kilo/auto` | เริ่มต้น — smart routing  
`kilocode/anthropic/claude-sonnet-4` | Anthropic ผ่าน Kilo  
`kilocode/openai/gpt-5.5` | OpenAI ผ่าน Kilo  
`kilocode/google/gemini-3.1-pro-preview` | Google ผ่าน Kilo  
...และอื่น ๆ อีกมากมาย | ใช้ `/models kilocode` เพื่อแสดงทั้งหมด  
  
## ตัวอย่างการตั้งค่า

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

การรับส่งข้อมูลและความเข้ากันได้

Kilo Gateway มีเอกสารในซอร์สว่าเข้ากันได้กับ OpenRouter ดังนั้นจึงยังอยู่บน เส้นทางที่เข้ากันได้กับ OpenAI แบบ proxy-style แทนการจัดรูปแบบคำขอ OpenAI แบบ native

  * Kilo refs ที่รองรับด้วย Gemini จะยังอยู่บนเส้นทาง proxy-Gemini ดังนั้น OpenClaw จึงคง การทำความสะอาด thought-signature ของ Gemini ไว้ที่นั่น โดยไม่เปิดใช้การตรวจสอบ replay ของ Gemini แบบ native หรือ bootstrap rewrites
  * Kilo Gateway ใช้ Bearer token กับ API key ของคุณเบื้องหลัง

Stream wrapper และ reasoning

stream wrapper ที่ใช้ร่วมกันของ Kilo จะเพิ่ม provider app header และปรับ proxy reasoning payloads ให้เป็นมาตรฐานสำหรับ ref ของโมเดลจริงที่รองรับ

การแก้ไขปัญหา

  * หากการค้นหาโมเดลล้มเหลวเมื่อเริ่มต้นระบบ OpenClaw จะ fallback ไปยังแค็ตตาล็อกแบบคงที่ที่รวมมาในแพ็กเกจ ซึ่งมี `kilocode/kilo/auto`
  * ยืนยันว่า API key ของคุณถูกต้อง และบัญชี Kilo ของคุณเปิดใช้โมเดลที่ต้องการแล้ว
  * เมื่อ Gateway ทำงานเป็น daemon ตรวจสอบให้แน่ใจว่า `KILOCODE_API_KEY` พร้อมใช้งานสำหรับ process นั้น (เช่น ใน `~/.openclaw/.env` หรือผ่าน `env.shellEnv`)


## ที่เกี่ยวข้อง

[**การเลือกโมเดล** การเลือกผู้ให้บริการ, ref ของโมเดล และพฤติกรรม failover ](</th/concepts/model-providers>) [**ข้อมูลอ้างอิงการตั้งค่า** ข้อมูลอ้างอิงการตั้งค่า OpenClaw ฉบับเต็ม ](</th/gateway/configuration-reference>) [**Kilo Gateway** แดชบอร์ด Kilo Gateway, API keys และการจัดการบัญชี ](<https://app.kilo.ai>)

Was this useful?YesNo