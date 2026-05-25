---
title: Volcengine (Doubao)
source_url: https://docs.openclaw.ai/th/providers/volcengine
scraped_at: 2026-05-25
---

ผู้ให้บริการ Volcengine ให้การเข้าถึงโมเดล Doubao และโมเดลของบุคคลที่สาม ที่โฮสต์อยู่บน Volcano Engine โดยมี endpoint แยกสำหรับงานทั่วไปและงานเขียนโค้ด Plugin แบบ bundled เดียวกันนี้ยังสามารถลงทะเบียน Volcengine Speech เป็นผู้ให้บริการ TTS ได้ด้วย

รายละเอียด | ค่า  
---|---  
ผู้ให้บริการ | `volcengine` (ทั่วไป + TTS) + `volcengine-plan` (เขียนโค้ด)  
Model auth | `VOLCANO_ENGINE_API_KEY`  
TTS auth | `VOLCENGINE_TTS_API_KEY` หรือ `BYTEPLUS_SEED_SPEECH_API_KEY`  
API | โมเดลแบบเข้ากันได้กับ OpenAI, BytePlus Seed Speech TTS  
  
## เริ่มต้นใช้งาน

* ### ตั้งค่า API key

เรียกใช้ onboarding แบบโต้ตอบ:

bashCopy code
[code]
    openclaw onboard --auth-choice volcengine-api-key
[/code]

การดำเนินการนี้จะลงทะเบียนทั้งผู้ให้บริการทั่วไป (`volcengine`) และผู้ให้บริการสำหรับงานเขียนโค้ด (`volcengine-plan`) จาก API key เดียว

* ### ตั้งค่าโมเดลเริ่มต้น

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "volcengine-plan/ark-code-latest" },    },  },}
[/code]

* ### ตรวจสอบว่าโมเดลพร้อมใช้งาน

bashCopy code
[code]
    openclaw models list --provider volcengineopenclaw models list --provider volcengine-plan
[/code]

## ผู้ให้บริการและ endpoint

ผู้ให้บริการ | Endpoint | กรณีใช้งาน  
---|---|---  
`volcengine` | `ark.cn-beijing.volces.com/api/v3` | โมเดลทั่วไป  
`volcengine-plan` | `ark.cn-beijing.volces.com/api/coding/v3` | โมเดลสำหรับเขียนโค้ด  
  
## แค็ตตาล็อกในตัว

### ทั่วไป (volcengine)

การอ้างอิงโมเดล | ชื่อ | อินพุต | คอนเท็กซ์  
---|---|---|---  
`volcengine/doubao-seed-1-8-251228` | Doubao Seed 1.8 | text, image | 256,000  
`volcengine/doubao-seed-code-preview-251028` | doubao-seed-code-preview-251028 | text, image | 256,000  
`volcengine/kimi-k2-5-260127` | Kimi K2.5 | text, image | 256,000  
`volcengine/glm-4-7-251222` | GLM 4.7 | text, image | 200,000  
`volcengine/deepseek-v3-2-251201` | DeepSeek V3.2 | text, image | 128,000  
  
### สำหรับเขียนโค้ด (volcengine-plan)

การอ้างอิงโมเดล | ชื่อ | อินพุต | คอนเท็กซ์  
---|---|---|---  
`volcengine-plan/ark-code-latest` | Ark Coding Plan | text | 256,000  
`volcengine-plan/doubao-seed-code` | Doubao Seed Code | text | 256,000  
`volcengine-plan/glm-4.7` | GLM 4.7 Coding | text | 200,000  
`volcengine-plan/kimi-k2-thinking` | Kimi K2 Thinking | text | 256,000  
`volcengine-plan/kimi-k2.5` | Kimi K2.5 Coding | text | 256,000  
`volcengine-plan/doubao-seed-code-preview-251028` | Doubao Seed Code Preview | text | 256,000  
  
## การแปลงข้อความเป็นเสียง

Volcengine TTS ใช้ BytePlus Seed Speech HTTP API และมีการตั้งค่า แยกจาก API key ของโมเดล Doubao แบบเข้ากันได้กับ OpenAI ในคอนโซล BytePlus ให้เปิด Seed Speech > Settings > API Keys แล้วคัดลอก API key จากนั้นตั้งค่า:

bashCopy code
[code]
    export VOLCENGINE_TTS_API_KEY="byteplus_seed_speech_api_key"export VOLCENGINE_TTS_RESOURCE_ID="seed-tts-1.0"
[/code]

จากนั้นเปิดใช้งานใน `openclaw.json`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "volcengine",      providers: {        volcengine: {          apiKey: "byteplus_seed_speech_api_key",          voice: "en_female_anna_mars_bigtts",          speedRatio: 1.0,        },      },    },  },}
[/code]

สำหรับปลายทางแบบ voice-note นั้น OpenClaw จะขอ `ogg_opus` แบบเนทีฟของผู้ให้บริการจาก Volcengine สำหรับไฟล์แนบเสียงปกติ จะขอ `mp3` แทน Provider alias `bytedance` และ `doubao` ก็ถูกแยกความละเอียดไปยังผู้ให้บริการเสียงเดียวกันเช่นกัน

resource id เริ่มต้นคือ `seed-tts-1.0` เพราะนี่คือสิ่งที่ BytePlus มอบให้ กับ API key ของ Seed Speech ที่สร้างใหม่ในโปรเจกต์เริ่มต้น หากโปรเจกต์ของคุณ มีสิทธิ์ใช้งาน TTS 2.0 ให้ตั้งค่า `VOLCENGINE_TTS_RESOURCE_ID=seed-tts-2.0`

การยืนยันตัวตนแบบ AppID/token เดิมยังคงรองรับสำหรับแอปพลิเคชัน Speech Console รุ่นเก่า:

bashCopy code
[code]
    export VOLCENGINE_TTS_APPID="speech_app_id"export VOLCENGINE_TTS_TOKEN="speech_access_token"export VOLCENGINE_TTS_CLUSTER="volcano_tts"
[/code]

## การตั้งค่าขั้นสูง

โมเดลเริ่มต้นหลัง onboarding

`openclaw onboard --auth-choice volcengine-api-key` ปัจจุบันตั้งค่า `volcengine-plan/ark-code-latest` เป็นโมเดลเริ่มต้น พร้อมกับลงทะเบียน แค็ตตาล็อก `volcengine` ทั่วไปด้วย

พฤติกรรม fallback ของตัวเลือกโมเดล

ระหว่าง onboarding/การกำหนดค่าการเลือกโมเดล ตัวเลือก auth ของ Volcengine จะให้ความสำคัญกับ แถว `volcengine/*` และ `volcengine-plan/*` ทั้งคู่ หากโมเดลเหล่านั้น ยังไม่ถูกโหลด OpenClaw จะ fallback ไปยังแค็ตตาล็อกที่ไม่กรอง แทนที่จะแสดง ตัวเลือกที่จำกัดขอบเขตเฉพาะผู้ให้บริการซึ่งว่างเปล่า

ตัวแปรสภาพแวดล้อมสำหรับโปรเซส daemon

หาก Gateway ทำงานเป็น daemon (launchd/systemd) ให้ตรวจสอบว่าตัวแปรสภาพแวดล้อม ของโมเดลและ TTS เช่น `VOLCANO_ENGINE_API_KEY`, `VOLCENGINE_TTS_API_KEY`, `BYTEPLUS_SEED_SPEECH_API_KEY`, `VOLCENGINE_TTS_APPID` และ `VOLCENGINE_TTS_TOKEN` พร้อมใช้งานสำหรับโปรเซสนั้น (เช่น ใน `~/.openclaw/.env` หรือผ่าน `env.shellEnv`)

## ที่เกี่ยวข้อง

[**การเลือกโมเดล** การเลือกผู้ให้บริการ การอ้างอิงโมเดล และพฤติกรรม failover ](</th/concepts/model-providers>) [**การกำหนดค่า** เอกสารอ้างอิง config แบบเต็มสำหรับ agents, models และ providers ](</th/gateway/configuration>) [**การแก้ไขปัญหา** ปัญหาที่พบบ่อยและขั้นตอนการดีบัก ](</th/help/troubleshooting>) [**คำถามที่พบบ่อย** คำถามที่พบบ่อยเกี่ยวกับการตั้งค่า OpenClaw ](</th/help/faq>)

Was this useful?YesNo