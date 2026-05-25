---
title: Synthetic
source_url: https://docs.openclaw.ai/th/providers/synthetic
scraped_at: 2026-05-25
---

[Synthetic](<https://synthetic.new>) เปิดเผยปลายทางที่เข้ากันได้กับ Anthropic OpenClaw ลงทะเบียนมันเป็น provider `synthetic` และใช้ Anthropic Messages API

คุณสมบัติ | ค่า  
---|---  
Provider | `synthetic`  
Auth | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
Base URL | `https://api.synthetic.new/anthropic`  
  
## เริ่มต้นใช้งาน

* ### รับ API key

รับ `SYNTHETIC_API_KEY` จากบัญชี Synthetic ของคุณ หรือให้ onboarding wizard ถามคุณก็ได้

* ### รันการเริ่มต้นใช้งาน

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### ตรวจสอบโมเดลเริ่มต้น

หลัง onboarding โมเดลเริ่มต้นจะถูกตั้งเป็น:

textCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## ตัวอย่าง Config

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## แค็ตตาล็อกที่มาพร้อมระบบ

โมเดล Synthetic ทั้งหมดใช้ cost `0` (input/output/cache)

Model ID | Context window | Max tokens | Reasoning | อินพุต  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192,000 | 65,536 | no | text  
`hf:moonshotai/Kimi-K2-Thinking` | 256,000 | 8,192 | yes | text  
`hf:zai-org/GLM-4.7` | 198,000 | 128,000 | no | text  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3.1` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3.2` | 159,000 | 8,192 | no | text  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128,000 | 8,192 | no | text  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524,000 | 8,192 | no | text  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256,000 | 8,192 | no | text  
`hf:moonshotai/Kimi-K2.5` | 256,000 | 8,192 | yes | text + image  
`hf:openai/gpt-oss-120b` | 128,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250,000 | 8,192 | no | text + image  
`hf:zai-org/GLM-4.5` | 128,000 | 128,000 | no | text  
`hf:zai-org/GLM-4.6` | 198,000 | 128,000 | no | text  
`hf:zai-org/GLM-5` | 256,000 | 128,000 | yes | text + image  
`hf:deepseek-ai/DeepSeek-V3` | 128,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256,000 | 8,192 | yes | text  
  
Model allowlist

หากคุณเปิดใช้ model allowlist (`agents.defaults.models`) ให้เพิ่มทุก โมเดล Synthetic ที่คุณวางแผนจะใช้ โมเดลที่ไม่อยู่ใน allowlist จะถูกซ่อน จากเอเจนต์

Base URL override

หาก Synthetic เปลี่ยน API endpoint ให้ override base URL ใน config ของคุณ:

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

โปรดจำไว้ว่า OpenClaw จะต่อท้าย `/v1` ให้อัตโนมัติ

## ที่เกี่ยวข้อง

[**การเลือกโมเดล** กฎของ provider, model refs และลักษณะการทำงานของ failover ](</th/concepts/model-providers>) [**ข้อมูลอ้างอิงการกำหนดค่า** schema ของ config แบบเต็ม รวมถึงการตั้งค่า provider ](</th/gateway/configuration-reference>) [**Synthetic** แดชบอร์ด Synthetic และเอกสาร API ](<https://synthetic.new>)

Was this useful?YesNo