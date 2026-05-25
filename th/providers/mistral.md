---
title: Mistral
source_url: https://docs.openclaw.ai/th/providers/mistral
scraped_at: 2026-05-25
---

OpenClaw มี Plugin Mistral ที่มาพร้อมชุดติดตั้ง ซึ่งลงทะเบียนสัญญาไว้สี่รายการ ได้แก่ chat completions, การทำความเข้าใจสื่อ (การถอดเสียงแบบแบตช์ของ Voxtral), STT แบบเรียลไทม์สำหรับ Voice Call (Voxtral Realtime) และ memory embeddings (`mistral-embed`)

คุณสมบัติ | ค่า  
---|---  
Provider id | `mistral`  
Plugin | มาพร้อมชุดติดตั้ง, `enabledByDefault: true`  
Auth env var | `MISTRAL_API_KEY`  
แฟล็ก Onboarding | `--auth-choice mistral-api-key`  
แฟล็ก CLI โดยตรง | `--mistral-api-key <key>`  
API | เข้ากันได้กับ OpenAI (`openai-completions`)  
Base URL | `https://api.mistral.ai/v1`  
โมเดลเริ่มต้น | `mistral/mistral-large-latest`  
โมเดล Embedding | `mistral-embed`  
Voxtral แบบแบตช์ | `voxtral-mini-latest` (การถอดเสียงเสียง)  
Voxtral แบบเรียลไทม์ | `voxtral-mini-transcribe-realtime-2602`  
  
## เริ่มต้นใช้งาน

* ### รับ API key ของคุณ

สร้าง API key ใน [Mistral Console](<https://console.mistral.ai/>)

* ### เรียกใช้ onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice mistral-api-key
[/code]

หรือส่งคีย์โดยตรง:

bashCopy code
[code]
    openclaw onboard --mistral-api-key "$MISTRAL_API_KEY"
[/code]

* ### ตั้งค่าโมเดลเริ่มต้น

json5Copy code
[code]
    {  env: { MISTRAL_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "mistral/mistral-large-latest" } } },}
[/code]

* ### ตรวจสอบว่าโมเดลพร้อมใช้งาน

bashCopy code
[code]
    openclaw models list --provider mistral
[/code]

## แค็ตตาล็อก LLM ในตัว

[Mistral Medium 3.5](<https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04>) คือโมเดล Medium แบบผสานในปัจจุบันในแค็ตตาล็อกที่มาพร้อมชุดติดตั้ง: น้ำหนักแบบ dense 128B, อินพุตข้อความและรูปภาพ, คอนเท็กซ์ 256K, การเรียกใช้ฟังก์ชัน, เอาต์พุตแบบมีโครงสร้าง, การเขียนโค้ด, และการให้เหตุผลที่ปรับได้ผ่าน Chat Completions API ใช้ `mistral/mistral-medium-3-5` เมื่อคุณต้องการโมเดล agentic/เขียนโค้ดแบบรวมรุ่นใหม่ของ Mistral แทนโมเดลเริ่มต้น `mistral/mistral-large-latest`

ปัจจุบัน OpenClaw จัดส่งแค็ตตาล็อก Mistral ที่มาพร้อมชุดติดตั้งนี้:

Model ref | อินพุต | คอนเท็กซ์ | เอาต์พุตสูงสุด | หมายเหตุ  
---|---|---|---|---  
`mistral/mistral-large-latest` | ข้อความ, รูปภาพ | 262,144 | 16,384 | โมเดลเริ่มต้น  
`mistral/mistral-medium-2508` | ข้อความ, รูปภาพ | 262,144 | 8,192 | Mistral Medium 3.1  
`mistral/mistral-medium-3-5` | ข้อความ, รูปภาพ | 262,144 | 8,192 | Mistral Medium 3.5; การให้เหตุผลที่ปรับได้  
`mistral/mistral-small-latest` | ข้อความ, รูปภาพ | 128,000 | 16,384 | Mistral Small 4; การให้เหตุผลที่ปรับได้ผ่าน API `reasoning_effort`  
`mistral/pixtral-large-latest` | ข้อความ, รูปภาพ | 128,000 | 32,768 | Pixtral  
`mistral/codestral-latest` | ข้อความ | 256,000 | 4,096 | การเขียนโค้ด  
`mistral/devstral-medium-latest` | ข้อความ | 262,144 | 32,768 | Devstral 2  
`mistral/magistral-small` | ข้อความ | 128,000 | 40,000 | เปิดใช้การให้เหตุผล  
  
หลัง onboarding ให้ทดสอบ Medium 3.5 แบบ smoke test โดยไม่ต้องเริ่ม Gateway:

bashCopy code
[code]
    openclaw infer model run --local \  --model mistral/mistral-medium-3-5 \  --prompt "Reply with exactly: mistral-ok" \  --json
[/code]

หากต้องการดูแถวของแค็ตตาล็อกที่มาพร้อมชุดติดตั้งก่อนเปลี่ยน config:

bashCopy code
[code]
    openclaw models list --all --provider mistral --plain
[/code]

## การถอดเสียงเสียง (Voxtral)

ใช้ Voxtral สำหรับการถอดเสียงแบบแบตช์ผ่านไปป์ไลน์การทำความเข้าใจสื่อ

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "mistral", model: "voxtral-mini-latest" }],      },    },  },}
[/code]

## STT แบบสตรีมมิงของ Voice Call

Plugin `mistral` ที่มาพร้อมชุดติดตั้งลงทะเบียน Voxtral Realtime เป็นผู้ให้บริการ STT แบบสตรีมมิงสำหรับ Voice Call

การตั้งค่า | พาธ Config | ค่าเริ่มต้น  
---|---|---  
API key | `plugins.entries.voice-call.config.streaming.providers.mistral.apiKey` | ถอยกลับไปใช้ `MISTRAL_API_KEY`  
โมเดล | `...mistral.model` | `voxtral-mini-transcribe-realtime-2602`  
การเข้ารหัส | `...mistral.encoding` | `pcm_mulaw`  
อัตราสุ่มตัวอย่าง | `...mistral.sampleRate` | `8000`  
ดีเลย์เป้าหมาย | `...mistral.targetStreamingDelayMs` | `800`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "mistral",            providers: {              mistral: {                apiKey: "${MISTRAL_API_KEY}",                targetStreamingDelayMs: 800,              },            },          },        },      },    },  },}
[/code]

## การกำหนดค่าขั้นสูง

การให้เหตุผลที่ปรับได้

`mistral/mistral-small-latest` (Mistral Small 4) และ `mistral/mistral-medium-3-5` รองรับ [การให้เหตุผลที่ปรับได้](<https://docs.mistral.ai/studio-api/conversations/reasoning/adjustable>) บน Chat Completions API ผ่าน `reasoning_effort` (`none` ลดการคิดเพิ่มเติมในเอาต์พุตให้น้อยที่สุด; `high` แสดงร่องรอยการคิดแบบเต็มก่อนคำตอบสุดท้าย) Mistral แนะนำ `reasoning_effort="high"` สำหรับกรณีการใช้งาน agentic และโค้ดของ Medium 3.5

OpenClaw แมประดับ **thinking** ของเซสชันไปยัง API ของ Mistral:

ระดับ thinking ของ OpenClaw | `reasoning_effort` ของ Mistral  
---|---  
**off** / **minimal** | `none`  
**low** / **medium** / **high** / **xhigh** / **adaptive** / **max** | `high`  
  
ตัวอย่าง config ตามขอบเขตโมเดลสำหรับการให้เหตุผลของ Medium 3.5:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "mistral/mistral-medium-3-5" },      models: {        "mistral/mistral-medium-3-5": {          params: { thinking: "high" },        },      },    },  },}
[/code]

Memory embeddings

Mistral สามารถให้บริการ memory embeddings ผ่าน `/v1/embeddings` (โมเดลเริ่มต้น: `mistral-embed`)

json5Copy code
[code]
    {  memorySearch: { provider: "mistral" },}
[/code]

Auth และ base URL

  * Auth ของ Mistral ใช้ `MISTRAL_API_KEY` (Bearer header)
  * Base URL ของผู้ให้บริการมีค่าเริ่มต้นเป็น `https://api.mistral.ai/v1` และรับรูปแบบคำขอ chat-completions มาตรฐานที่เข้ากันได้กับ OpenAI
  * โมเดลเริ่มต้นของ onboarding คือ `mistral/mistral-large-latest`
  * แทนที่ base URL ภายใต้ `models.providers.mistral.baseUrl` เฉพาะเมื่อ Mistral เผยแพร่ regional endpoint ที่คุณต้องใช้ไว้อย่างชัดเจนเท่านั้น


## ที่เกี่ยวข้อง

[**การเลือกโมเดล** การเลือกผู้ให้บริการ, model refs และพฤติกรรม failover ](</th/concepts/model-providers>) [**การทำความเข้าใจสื่อ** การตั้งค่าการถอดเสียงเสียงและการเลือกผู้ให้บริการ ](</th/nodes/media-understanding>)

Was this useful?YesNo