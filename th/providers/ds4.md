---
title: ds4
source_url: https://docs.openclaw.ai/th/providers/ds4
scraped_at: 2026-06-29
---

ModelsProviders

[ds4](<https://github.com/antirez/ds4>) ให้บริการ DeepSeek V4 Flash จากแบ็กเอนด์ Metal ในเครื่อง พร้อม API `/v1` ที่เข้ากันได้กับ OpenAI OpenClaw เชื่อมต่อกับ ds4 ผ่านตระกูลผู้ให้บริการทั่วไป `openai-completions`

ds4 ไม่ใช่ Plugin ผู้ให้บริการของ OpenClaw ที่บันเดิลมาให้ กำหนดค่าไว้ใต้ `models.providers.ds4` แล้วเลือก `ds4/deepseek-v4-flash`

  * ID ผู้ให้บริการ: `ds4`
  * Plugin: ไม่มี
  * API: Chat Completions ที่เข้ากันได้กับ OpenAI (`openai-completions`)
  * URL ฐานที่แนะนำ: `http://127.0.0.1:18000/v1`
  * ID โมเดล: `deepseek-v4-flash`
  * การเรียกใช้เครื่องมือ: รองรับผ่าน `tools` และ `tool_calls` แบบ OpenAI
  * การให้เหตุผล: `thinking` และ `reasoning_effort` แบบ DeepSeek


## ข้อกำหนด

  * macOS ที่รองรับ Metal
  * เช็กเอาต์ ds4 ที่ใช้งานได้พร้อม `ds4-server` และไฟล์ GGUF ของ DeepSeek V4 Flash
  * หน่วยความจำเพียงพอสำหรับ context ที่คุณเลือก ค่า `--ctx` ที่ใหญ่ขึ้นจะจัดสรร หน่วยความจำ KV มากขึ้นเมื่อเซิร์ฟเวอร์เริ่มทำงาน


## เริ่มต้นอย่างรวดเร็ว

* ### เริ่ม ds4-server

แทนที่ `&lt;DS4_DIR&gt;` ด้วยพาธเช็กเอาต์ ds4 ของคุณ

bashCopy code
[code]
    &lt;DS4_DIR&gt;/ds4-server \  --model &lt;DS4_DIR&gt;/ds4flash.gguf \  --host 127.0.0.1 \  --port 18000 \  --ctx 32768 \  --tokens 128
[/code]

* ### ตรวจสอบเอนด์พอยต์ที่เข้ากันได้กับ OpenAI

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

การตอบกลับควรมี `deepseek-v4-flash`

* ### เพิ่มการกำหนดค่าผู้ให้บริการ OpenClaw

เพิ่มการกำหนดค่าจาก การกำหนดค่าเต็ม แล้วรันการตรวจสอบโมเดลแบบครั้งเดียว:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

## การกำหนดค่าเต็ม

ใช้การกำหนดค่านี้เมื่อ ds4 กำลังรันอยู่แล้วบน `127.0.0.1:18000`

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "ds4/deepseek-v4-flash" },      models: {        "ds4/deepseek-v4-flash": {          alias: "DS4 local",        },      },    },  },  models: {    mode: "merge",    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

ให้ `contextWindow` ตรงกับค่า `ds4-server --ctx` ให้ `maxTokens` ตรงกับ `--tokens` เว้นแต่คุณตั้งใจให้ OpenClaw ขอเอาต์พุตน้อยกว่าค่าเริ่มต้นของเซิร์ฟเวอร์

## การเริ่มต้นตามต้องการ

OpenClaw สามารถเริ่ม ds4 ได้เฉพาะเมื่อเลือกโมเดล `ds4/...` เพิ่ม `localService` ในรายการผู้ให้บริการเดียวกัน:

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "&lt;DS4_DIR&gt;/ds4-server",          args: [            "--model",            "&lt;DS4_DIR&gt;/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "32768",            "--tokens",            "128",          ],          cwd: "&lt;DS4_DIR&gt;",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

`command` ต้องเป็นพาธไฟล์ปฏิบัติการแบบสัมบูรณ์ ไม่มีการใช้การค้นหาผ่านเชลล์และการขยาย `~` ดู [บริการโมเดลในเครื่อง](</th/gateway/local-model-services>) สำหรับทุกฟิลด์ของ `localService`

## Think Max

ds4 ใช้ Think Max เฉพาะเมื่อเงื่อนไขทั้งสองข้อนี้เป็นจริง:

  * `ds4-server` เริ่มด้วย `--ctx 393216` หรือสูงกว่า
  * คำขอใช้ `reasoning_effort: "max"` หรือฟิลด์ effort ของ ds4 ที่เทียบเท่ากัน


หากคุณรัน context ขนาดใหญ่นั้น ให้อัปเดตทั้งแฟล็กของเซิร์ฟเวอร์และเมทาดาทาโมเดลของ OpenClaw:

json5Copy code
[code]
    {  contextWindow: 393216,  maxTokens: 384000,  compat: {    supportsUsageInStreaming: true,    supportsReasoningEffort: true,    maxTokensField: "max_tokens",    supportsStrictMode: false,    thinkingFormat: "deepseek",    supportedReasoningEfforts: ["low", "medium", "high", "xhigh", "max"],  },}
[/code]

## ทดสอบ

เริ่มด้วยการตรวจสอบ HTTP โดยตรง:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"Reply with exactly: ds4-ok"}],"max_tokens":16,"stream":false,"thinking":{"type":"disabled"}}'
[/code]

จากนั้นทดสอบการกำหนดเส้นทางโมเดลของ OpenClaw:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

สำหรับ smoke test แบบเอเจนต์เต็มและการเรียกใช้เครื่องมือ ให้ใช้ context อย่างน้อย 32768:

bashCopy code
[code]
    openclaw agent \  --local \  --session-id ds4-tool-smoke \  --model ds4/deepseek-v4-flash \  --thinking off \  --message "Use the shell command pwd once, then reply exactly: tool-ok <output>" \  --json \  --timeout 240
[/code]

ผลลัพธ์ที่คาดหวัง:

  * `executionTrace.winnerProvider` คือ `ds4`
  * `executionTrace.winnerModel` คือ `deepseek-v4-flash`
  * `toolSummary.calls` มีค่าอย่างน้อย `1`
  * `finalAssistantVisibleText` เริ่มด้วย `tool-ok`


## การแก้ไขปัญหา

curl /v1/models เชื่อมต่อไม่ได้

ds4 ไม่ได้รันอยู่ หรือไม่ได้ผูกกับโฮสต์และพอร์ตใน `baseUrl` เริ่ม `ds4-server` แล้วลองใหม่:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

500 prompt exceeds context

`--ctx` ที่กำหนดค่าไว้เล็กเกินไปสำหรับรอบการทำงานของ OpenClaw เพิ่มค่า `ds4-server --ctx` แล้วอัปเดต `models.providers.ds4.models[].contextWindow` ให้ตรงกัน รอบการทำงานของเอเจนต์เต็มที่มีเครื่องมือต้องใช้ context มากกว่าคำขอ curl แบบข้อความเดียวโดยตรงอย่างมาก

Think Max ไม่เปิดใช้งาน

ds4 ใช้ Think Max เฉพาะเมื่อ `--ctx` มีค่าอย่างน้อย `393216` และคำขอ ขอ `reasoning_effort: "max"` context ที่เล็กกว่าจะย้อนกลับไปใช้การให้เหตุผลระดับสูง

คำขอแรกช้า

ds4 มีช่วง residency ของ Metal แบบ cold และช่วงวอร์มอัปโมเดล ใช้ `localService.readyTimeoutMs: 300000` เมื่อ OpenClaw เริ่มเซิร์ฟเวอร์ตามต้องการ

## ที่เกี่ยวข้อง

[**บริการโมเดลในเครื่อง** เริ่มเซิร์ฟเวอร์โมเดลในเครื่องตามต้องการก่อนคำขอโมเดล ](</th/gateway/local-model-services>) [**โมเดลในเครื่อง** เลือกและใช้งานแบ็กเอนด์โมเดลในเครื่อง ](</th/gateway/local-models>) [**ผู้ให้บริการโมเดล** กำหนดค่า provider refs, การยืนยันตัวตน และ failover ](</th/concepts/model-providers>) [**DeepSeek** พฤติกรรมผู้ให้บริการ DeepSeek แบบเนทีฟและการควบคุม thinking ](</th/providers/deepseek>)

Was this useful?YesNo

Open issue