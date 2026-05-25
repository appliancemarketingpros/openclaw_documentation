---
title: Moonshot AI
source_url: https://docs.openclaw.ai/th/providers/moonshot
scraped_at: 2026-05-25
---

Moonshot ให้บริการ Kimi API พร้อม endpoint ที่เข้ากันได้กับ OpenAI กำหนดค่า provider และตั้งค่าโมเดลเริ่มต้นเป็น `moonshot/kimi-k2.6` หรือใช้ Kimi Coding ด้วย `kimi/kimi-for-coding`

## แคตตาล็อกโมเดลในตัว

Model ref | ชื่อ | การให้เหตุผล | อินพุต | บริบท | เอาต์พุตสูงสุด  
---|---|---|---|---|---  
`moonshot/kimi-k2.6` | Kimi K2.6 | ไม่ใช่ | ข้อความ, รูปภาพ | 262,144 | 262,144  
`moonshot/kimi-k2.5` | Kimi K2.5 | ไม่ใช่ | ข้อความ, รูปภาพ | 262,144 | 262,144  
`moonshot/kimi-k2-thinking` | Kimi K2 Thinking | ใช่ | ข้อความ | 262,144 | 262,144  
`moonshot/kimi-k2-thinking-turbo` | Kimi K2 Thinking Turbo | ใช่ | ข้อความ | 262,144 | 262,144  
`moonshot/kimi-k2-turbo` | Kimi K2 Turbo | ไม่ใช่ | ข้อความ | 256,000 | 16,384  
  
การประมาณค่าใช้จ่ายที่รวมมากับโมเดล K2 ปัจจุบันที่โฮสต์โดย Moonshot ใช้อัตราแบบจ่ายตามการใช้งานจริงที่ Moonshot เผยแพร่ไว้: Kimi K2.6 คือ $0.16/MTok สำหรับ cache hit, $0.95/MTok อินพุต, และ $4.00/MTok เอาต์พุต; Kimi K2.5 คือ $0.10/MTok สำหรับ cache hit, $0.60/MTok อินพุต, และ $3.00/MTok เอาต์พุต รายการแคตตาล็อกเดิมอื่นๆ จะคง placeholder ค่าใช้จ่ายเป็นศูนย์ไว้ เว้นแต่คุณจะแทนที่ใน config

## เริ่มต้นใช้งาน

เลือก provider ของคุณและทำตามขั้นตอนการตั้งค่า

### Moonshot API

**เหมาะที่สุดสำหรับ:** โมเดล Kimi K2 ผ่าน Moonshot Open Platform

* ### เลือกภูมิภาค endpoint ของคุณ

ตัวเลือกการยืนยันตัวตน | Endpoint | ภูมิภาค  
---|---|---  
`moonshot-api-key` | `https://api.moonshot.ai/v1` | นานาชาติ  
`moonshot-api-key-cn` | `https://api.moonshot.cn/v1` | จีน  
* ### เรียกใช้ onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key
[/code]

หรือสำหรับ endpoint ของจีน:

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key-cn
[/code]

* ### ตั้งค่าโมเดลเริ่มต้น

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },    },  },}
[/code]

* ### ตรวจสอบว่าโมเดลพร้อมใช้งาน

bashCopy code
[code]
    openclaw models list --provider moonshot
[/code]

* ### เรียกใช้ smoke test แบบสด

ใช้ไดเรกทอรีสถานะแยกต่างหากเมื่อคุณต้องการตรวจสอบการเข้าถึงโมเดลและการติดตามค่าใช้จ่าย โดยไม่แตะต้องเซสชันปกติของคุณ:

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=/tmp/openclaw-kimi/openclaw.json \OPENCLAW_STATE_DIR=/tmp/openclaw-kimi \openclaw agent --local \  --session-id live-kimi-cost \  --message 'Reply exactly: KIMI_LIVE_OK' \  --thinking off \  --json
[/code]

การตอบกลับ JSON ควรรายงาน `provider: "moonshot"` และ `model: "kimi-k2.6"` รายการ transcript ของผู้ช่วยจะจัดเก็บ การใช้ token ที่ปรับให้เป็นมาตรฐานแล้ว รวมถึงค่าใช้จ่ายโดยประมาณภายใต้ `usage.cost` เมื่อ Moonshot ส่งคืน metadata การใช้งาน

### ตัวอย่าง Config

json5Copy code
[code]
    {  env: { MOONSHOT_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },      models: {        // moonshot-kimi-k2-aliases:start        "moonshot/kimi-k2.6": { alias: "Kimi K2.6" },        "moonshot/kimi-k2.5": { alias: "Kimi K2.5" },        "moonshot/kimi-k2-thinking": { alias: "Kimi K2 Thinking" },        "moonshot/kimi-k2-thinking-turbo": { alias: "Kimi K2 Thinking Turbo" },        "moonshot/kimi-k2-turbo": { alias: "Kimi K2 Turbo" },        // moonshot-kimi-k2-aliases:end      },    },  },  models: {    mode: "merge",    providers: {      moonshot: {        baseUrl: "https://api.moonshot.ai/v1",        apiKey: "${MOONSHOT_API_KEY}",        api: "openai-completions",        models: [          // moonshot-kimi-k2-models:start          {            id: "kimi-k2.6",            name: "Kimi K2.6",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.95, output: 4, cacheRead: 0.16, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2.5",            name: "Kimi K2.5",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.6, output: 3, cacheRead: 0.1, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking",            name: "Kimi K2 Thinking",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking-turbo",            name: "Kimi K2 Thinking Turbo",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-turbo",            name: "Kimi K2 Turbo",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 256000,            maxTokens: 16384,          },          // moonshot-kimi-k2-models:end        ],      },    },  },}
[/code]

### Kimi Coding

**เหมาะที่สุดสำหรับ:** งานที่เน้นโค้ดผ่าน endpoint ของ Kimi Coding

* ### เรียกใช้ onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kimi-code-api-key
[/code]

* ### ตั้งค่าโมเดลเริ่มต้น

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },    },  },}
[/code]

* ### ตรวจสอบว่าโมเดลพร้อมใช้งาน

bashCopy code
[code]
    openclaw models list --provider kimi
[/code]

### ตัวอย่าง Config

json5Copy code
[code]
    {  env: { KIMI_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },      models: {        "kimi/kimi-for-coding": { alias: "Kimi" },      },    },  },}
[/code]

## การค้นหาเว็บของ Kimi

OpenClaw ยังมาพร้อมกับ **Kimi** ในฐานะผู้ให้บริการ `web_search` ซึ่งขับเคลื่อนโดยการค้นหาเว็บของ Moonshot

* ### Run interactive web search setup

bashCopy code
[code]
    openclaw configure --section web
[/code]

เลือก **Kimi** ในส่วนการค้นหาเว็บเพื่อจัดเก็บ `plugins.entries.moonshot.config.webSearch.*`.

* ### Configure the web search region and model

การตั้งค่าแบบโต้ตอบจะแจ้งให้กรอก:

การตั้งค่า | ตัวเลือก  
---|---  
ภูมิภาค API | `https://api.moonshot.ai/v1` (สากล) หรือ `https://api.moonshot.cn/v1` (จีน)  
โมเดลการค้นหาเว็บ | ค่าเริ่มต้นคือ `kimi-k2.6`  
  
การตั้งค่าอยู่ภายใต้ `plugins.entries.moonshot.config.webSearch`:

json5Copy code
[code]
    {  plugins: {    entries: {      moonshot: {        config: {          webSearch: {            apiKey: "sk-...", // or use KIMI_API_KEY / MOONSHOT_API_KEY            baseUrl: "https://api.moonshot.ai/v1",            model: "kimi-k2.6",          },        },      },    },  },  tools: {    web: {      search: {        provider: "kimi",      },    },  },}
[/code]

## การตั้งค่าขั้นสูง

Native thinking mode

Moonshot Kimi รองรับโหมดการคิดแบบเนทีฟชนิดไบนารี:

  * `thinking: { type: "enabled" }`
  * `thinking: { type: "disabled" }`


ตั้งค่าต่อโมเดลผ่าน `agents.defaults.models.<provider/model>.params`:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "disabled" },          },        },      },    },  },}
[/code]

OpenClaw ยังแมประดับ runtime `/think` สำหรับ Moonshot ด้วย:

ระดับ `/think` | พฤติกรรมของ Moonshot  
---|---  
`/think off` | `thinking.type=disabled`  
ระดับใดก็ตามที่ไม่ใช่ off | `thinking.type=enabled`  
  
Kimi K2.6 ยังรับฟิลด์ `thinking.keep` ที่เป็นตัวเลือก ซึ่งควบคุม การคง `reasoning_content` ไว้ข้ามหลายเทิร์น ตั้งค่าเป็น `"all"` เพื่อเก็บ reasoning ทั้งหมดข้ามเทิร์น; ละเว้นฟิลด์นี้ (หรือปล่อยให้เป็น `null`) เพื่อใช้กลยุทธ์ ค่าเริ่มต้นของเซิร์ฟเวอร์ OpenClaw จะส่งต่อ `thinking.keep` เฉพาะสำหรับ `moonshot/kimi-k2.6` และจะตัดฟิลด์นี้ออกจากโมเดลอื่น

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "enabled", keep: "all" },          },        },      },    },  },}
[/code]

Tool call id sanitization

Moonshot Kimi ให้บริการ tool_call ids ที่มีรูปแบบเช่น `functions.<name>:<index>` OpenClaw จะคงค่าเหล่านั้นไว้เหมือนเดิมเพื่อให้การเรียกเครื่องมือหลายเทิร์นยังทำงานต่อไปได้

หากต้องการบังคับใช้การทำให้เป็นรูปแบบปลอดภัยอย่างเคร่งครัดกับผู้ให้บริการแบบกำหนดเองที่เข้ากันได้กับ OpenAI ให้ตั้งค่า `sanitizeToolCallIds: true`:

json5Copy code
[code]
    {  models: {    providers: {      "my-kimi-proxy": {        api: "openai-completions",        sanitizeToolCallIds: true,      },    },  },}
[/code]

Streaming usage compatibility

Endpoint แบบเนทีฟของ Moonshot (`https://api.moonshot.ai/v1` และ `https://api.moonshot.cn/v1`) ประกาศความเข้ากันได้ของการใช้งานแบบสตรีมบน transport `openai-completions` ที่ใช้ร่วมกัน OpenClaw อิงค่าดังกล่าวจาก ความสามารถของ endpoint ดังนั้น ids ผู้ให้บริการแบบกำหนดเองที่เข้ากันได้ซึ่งชี้ไปยังโฮสต์ Moonshot แบบเนทีฟเดียวกันจะสืบทอดพฤติกรรม streaming-usage เดียวกัน

ด้วยราคาของ K2.6 ที่รวมมาให้ การใช้งานแบบสตรีมที่รวมโทเคนขาเข้า ขาออก และ cache-read จะถูกแปลงเป็นต้นทุน USD โดยประมาณในเครื่องสำหรับ `/status`, `/usage full`, `/usage cost` และการบันทึกบัญชีเซสชัน ที่อ้างอิงจาก transcript ด้วย

ข้อมูลอ้างอิงปลายทางและ model ref ผู้ให้บริการ | คำนำหน้า model ref | ปลายทาง | ตัวแปรสภาพแวดล้อมสำหรับ Auth  
---|---|---|---  
Moonshot | `moonshot/` | `https://api.moonshot.ai/v1` | `MOONSHOT_API_KEY`  
Moonshot CN | `moonshot/` | `https://api.moonshot.cn/v1` | `MOONSHOT_API_KEY`  
Kimi Coding | `kimi/` | ปลายทาง Kimi Coding | `KIMI_API_KEY`  
การค้นหาเว็บ | N/A | เหมือนกับภูมิภาค Moonshot API | `KIMI_API_KEY` หรือ `MOONSHOT_API_KEY`  
  
  * การค้นหาเว็บของ Kimi ใช้ `KIMI_API_KEY` หรือ `MOONSHOT_API_KEY` และค่าเริ่มต้นคือ `https://api.moonshot.ai/v1` พร้อมโมเดล `kimi-k2.6`
  * แทนที่ราคาและเมทาดาทาบริบทใน `models.providers` หากจำเป็น
  * หาก Moonshot เผยแพร่ขีดจำกัดบริบทที่แตกต่างกันสำหรับโมเดล ให้ปรับ `contextWindow` ให้สอดคล้อง


## ที่เกี่ยวข้อง

[**การเลือกโมเดล** การเลือกผู้ให้บริการ, model refs และพฤติกรรม failover ](</th/concepts/model-providers>) [**การค้นหาเว็บ** การกำหนดค่าผู้ให้บริการค้นหาเว็บ รวมถึง Kimi ](</th/tools/web>) [**ข้อมูลอ้างอิงการกำหนดค่า** สคีมาการกำหนดค่าแบบครบถ้วนสำหรับผู้ให้บริการ โมเดล และ plugins ](</th/gateway/configuration-reference>) [**Moonshot Open Platform** การจัดการคีย์ Moonshot API และเอกสารประกอบ ](<https://platform.moonshot.ai>)

Was this useful?YesNo