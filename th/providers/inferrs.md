---
title: อนุมาน
source_url: https://docs.openclaw.ai/th/providers/inferrs
scraped_at: 2026-05-25
---

[inferrs](<https://github.com/ericcurtin/inferrs>) สามารถให้บริการโมเดลภายในเครื่องหลัง API `/v1` ที่เข้ากันได้กับ OpenAI ได้ OpenClaw ทำงานกับ `inferrs` ผ่านเส้นทางทั่วไป `openai-completions`

คุณสมบัติ | ค่า  
---|---  
รหัสผู้ให้บริการ | `inferrs` (กำหนดเอง; กำหนดค่าภายใต้ `models.providers.inferrs`)  
Plugin | ไม่มี — `inferrs` ไม่ใช่ Plugin ผู้ให้บริการ OpenClaw ที่รวมมาในชุด  
ตัวแปรสภาพแวดล้อมสำหรับ Auth | ไม่บังคับ ค่าใดก็ใช้ได้หากเซิร์ฟเวอร์ inferrs ของคุณไม่มี auth  
API | เข้ากันได้กับ OpenAI (`openai-completions`)  
URL ฐานที่แนะนำ | `http://127.0.0.1:8080/v1` (หรือที่ใดก็ตามที่เซิร์ฟเวอร์ inferrs ของคุณทำงานอยู่)  
  
## เริ่มต้นใช้งาน

* ### เริ่ม inferrs ด้วยโมเดล

bashCopy code
[code]
    inferrs serve google/gemma-4-E2B-it \  --host 127.0.0.1 \  --port 8080 \  --device metal
[/code]

* ### ตรวจสอบว่าเข้าถึงเซิร์ฟเวอร์ได้

bashCopy code
[code]
    curl http://127.0.0.1:8080/healthcurl http://127.0.0.1:8080/v1/models
[/code]

* ### เพิ่มรายการผู้ให้บริการ OpenClaw

เพิ่มรายการผู้ให้บริการอย่างชัดเจนและชี้โมเดลเริ่มต้นของคุณไปยังรายการนั้น ดูตัวอย่างการกำหนดค่าแบบเต็มด้านล่าง

## ตัวอย่างการกำหนดค่าแบบเต็ม

ตัวอย่างนี้ใช้ Gemma 4 บนเซิร์ฟเวอร์ `inferrs` ภายในเครื่อง

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },      models: {        "inferrs/google/gemma-4-E2B-it": {          alias: "Gemma 4 (inferrs)",        },      },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

## การเริ่มต้นตามต้องการ

Inferrs ยังสามารถให้ OpenClaw เริ่มทำงานเฉพาะเมื่อเลือกโมเดล `inferrs/...` ได้ด้วย เพิ่ม `localService` ไปยังรายการผู้ให้บริการเดียวกัน:

json5Copy code
[code]
    {  models: {    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

`command` ต้องเป็นพาธแบบสมบูรณ์ ใช้ `which inferrs` บนโฮสต์ Gateway แล้วใส่ พาธนั้นใน config สำหรับข้อมูลอ้างอิงฟิลด์ทั้งหมด โปรดดู [บริการโมเดลภายในเครื่อง](</th/gateway/local-model-services>)

## การกำหนดค่าขั้นสูง

เหตุใด requiresStringContent จึงสำคัญ

เส้นทาง Chat Completions บางรายการของ `inferrs` ยอมรับเฉพาะ `messages[].content` ที่เป็นสตริง ไม่ใช่อาร์เรย์ content-part แบบมีโครงสร้าง

json5Copy code
[code]
    compat: {  requiresStringContent: true}
[/code]

OpenClaw จะแปลงส่วนเนื้อหาข้อความล้วนให้เป็นสตริงธรรมดาก่อนส่ง คำขอ

ข้อควรระวังเกี่ยวกับ Gemma และสคีมาเครื่องมือ

ชุดผสม `inferrs` \+ Gemma ปัจจุบันบางชุดยอมรับคำขอ `/v1/chat/completions` โดยตรงขนาดเล็ก แต่ยังล้มเหลวกับรอบ agent-runtime แบบเต็มของ OpenClaw

หากเกิดกรณีนี้ ให้ลองสิ่งนี้ก่อน:

json5Copy code
[code]
    compat: {  requiresStringContent: true,  supportsTools: false}
[/code]

การตั้งค่านี้จะปิดพื้นผิวสคีมาเครื่องมือของ OpenClaw สำหรับโมเดล และสามารถลดแรงกดของพรอมป์ ต่อแบ็กเอนด์ภายในเครื่องที่เข้มงวดกว่าได้

หากคำขอโดยตรงขนาดเล็กมากยังทำงานได้ แต่รอบ agent ปกติของ OpenClaw ยังคง แครชภายใน `inferrs` ปัญหาที่เหลือมักเป็นพฤติกรรมของโมเดล/เซิร์ฟเวอร์ต้นทาง มากกว่าชั้นการขนส่งของ OpenClaw

การทดสอบ smoke แบบแมนนวล

เมื่อตั้งค่าแล้ว ให้ทดสอบทั้งสองชั้น:

bashCopy code
[code]
    curl http://127.0.0.1:8080/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"google/gemma-4-E2B-it","messages":[{"role":"user","content":"What is 2 + 2?"}],"stream":false}'
[/code]

bashCopy code
[code]
    openclaw infer model run \  --model inferrs/google/gemma-4-E2B-it \  --prompt "What is 2 + 2? Reply with one short sentence." \  --json
[/code]

หากคำสั่งแรกทำงานได้แต่คำสั่งที่สองล้มเหลว ให้ตรวจสอบส่วนการแก้ปัญหาด้านล่าง

พฤติกรรมแบบพร็อกซี

`inferrs` ถูกปฏิบัติเป็นแบ็กเอนด์ `/v1` ที่เข้ากันได้กับ OpenAI แบบพร็อกซี ไม่ใช่ ปลายทาง OpenAI แบบเนทีฟ

  * การปรับรูปคำขอเฉพาะ OpenAI แบบเนทีฟจะไม่นำมาใช้ที่นี่
  * ไม่มี `service_tier`, ไม่มี Responses `store`, ไม่มีคำใบ้ prompt-cache และไม่มี การปรับรูปเพย์โหลด reasoning-compat ของ OpenAI
  * ส่วนหัวระบุที่มาของ OpenClaw แบบซ่อน (`originator`, `version`, `User-Agent`) จะไม่ถูกแทรกบน URL ฐาน `inferrs` แบบกำหนดเอง


## การแก้ปัญหา

curl /v1/models ล้มเหลว

`inferrs` ไม่ได้ทำงานอยู่ เข้าถึงไม่ได้ หรือไม่ได้ผูกกับ โฮสต์/พอร์ตที่คาดไว้ ตรวจสอบให้แน่ใจว่าเซิร์ฟเวอร์เริ่มทำงานแล้วและกำลังฟังบนที่อยู่ที่คุณ กำหนดค่าไว้

messages[].content คาดว่าจะเป็นสตริง

ตั้งค่า `compat.requiresStringContent: true` ในรายการโมเดล ดู ส่วน `requiresStringContent` ด้านบนสำหรับรายละเอียด

การเรียก /v1/chat/completions โดยตรงผ่าน แต่ openclaw infer model run ล้มเหลว

ลองตั้งค่า `compat.supportsTools: false` เพื่อปิดพื้นผิวสคีมาเครื่องมือ ดูข้อควรระวังเกี่ยวกับสคีมาเครื่องมือของ Gemma ด้านบน

inferrs ยังแครชในรอบ agent ที่ใหญ่กว่า

หาก OpenClaw ไม่พบข้อผิดพลาดสคีมาแล้ว แต่ `inferrs` ยังแครชในรอบ agent ที่ใหญ่กว่า ให้ถือว่าเป็นข้อจำกัดของ `inferrs` หรือโมเดลต้นทาง ลด แรงกดของพรอมป์ หรือเปลี่ยนไปใช้แบ็กเอนด์ภายในเครื่องหรือโมเดลอื่น

## ที่เกี่ยวข้อง

[**โมเดลภายในเครื่อง** การรัน OpenClaw กับเซิร์ฟเวอร์โมเดลภายในเครื่อง ](</th/gateway/local-models>) [**บริการโมเดลภายในเครื่อง** การเริ่มเซิร์ฟเวอร์โมเดลภายในเครื่องตามต้องการสำหรับผู้ให้บริการที่กำหนดค่าไว้ ](</th/gateway/local-model-services>) [**การแก้ปัญหา Gateway** การดีบักแบ็กเอนด์ภายในเครื่องที่เข้ากันได้กับ OpenAI ซึ่งผ่านการ probe แต่ล้มเหลวในการรัน agent ](</th/gateway/troubleshooting#local-openai-compatible-backend-passes-direct-probes-but-agent-runs-fail>) [**การเลือกโมเดล** ภาพรวมของผู้ให้บริการทั้งหมด การอ้างอิงโมเดล และพฤติกรรม failover ](</th/concepts/model-providers>)

Was this useful?YesNo