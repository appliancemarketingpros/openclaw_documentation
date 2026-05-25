---
title: SGLang
source_url: https://docs.openclaw.ai/th/providers/sglang
scraped_at: 2026-05-25
---

SGLang ให้บริการโมเดล open-weight ผ่าน API HTTP ที่เข้ากันได้กับ OpenAI OpenClaw เชื่อมต่อกับ SGLang โดยใช้ตระกูลผู้ให้บริการ `openai-completions` พร้อมการค้นหาโมเดลที่พร้อมใช้งานโดยอัตโนมัติ

คุณสมบัติ | ค่า  
---|---  
ID ผู้ให้บริการ | `sglang`  
Plugin | รวมมาให้, `enabledByDefault: true`  
ตัวแปรสภาพแวดล้อมสำหรับการยืนยันตัวตน | `SGLANG_API_KEY` (ค่าใดก็ได้ที่ไม่ว่าง หากเซิร์ฟเวอร์ไม่มีการยืนยันตัวตน)  
แฟล็กการเริ่มต้นใช้งาน | `--auth-choice sglang`  
API | เข้ากันได้กับ OpenAI (`openai-completions`)  
URL ฐานเริ่มต้น | `http://127.0.0.1:30000/v1`  
ตัวยึดตำแหน่งโมเดลเริ่มต้น | `sglang/Qwen/Qwen3-8B`  
การใช้งานแบบสตรีม | ใช่ (`supportsStreamingUsage: true`)  
ราคา | ทำเครื่องหมายเป็นใช้งานภายนอกฟรี (`modelPricing.external: false`)  
  
OpenClaw ยัง **ค้นหาโดยอัตโนมัติ** โมเดลที่พร้อมใช้งานจาก SGLang เมื่อคุณเลือกใช้ด้วย `SGLANG_API_KEY` ใช้ `sglang/*` ใน `agents.defaults.models` เพื่อให้การค้นหาเป็นแบบไดนามิกเมื่อคุณกำหนดค่า URL ฐาน SGLang แบบกำหนดเองด้วย ดู การค้นหาโมเดล (ผู้ให้บริการโดยนัย) ด้านล่าง

## เริ่มต้นใช้งาน

* ### Start SGLang

เปิดใช้ SGLang พร้อมเซิร์ฟเวอร์ที่เข้ากันได้กับ OpenAI URL ฐานของคุณควรเปิดเผย เอนด์พอยต์ `/v1` (เช่น `/v1/models`, `/v1/chat/completions`) โดยทั่วไป SGLang จะทำงานที่:

  * `http://127.0.0.1:30000/v1`


* ### Set an API key

ค่าใดก็ใช้ได้หากไม่ได้กำหนดค่าการยืนยันตัวตนบนเซิร์ฟเวอร์ของคุณ:

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

* ### Run onboarding or set a model directly

bashCopy code
[code]
    openclaw onboard
[/code]

หรือกำหนดค่าโมเดลด้วยตนเอง:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "sglang/your-model-id" },    },  },}
[/code]

## การค้นหาโมเดล (ผู้ให้บริการโดยนัย)

เมื่อมีการตั้งค่า `SGLANG_API_KEY` (หรือมีโปรไฟล์การยืนยันตัวตนอยู่แล้ว) และคุณ **ไม่ได้** กำหนด `models.providers.sglang` OpenClaw จะส่งคำขอไปที่:

  * `GET http://127.0.0.1:30000/v1/models`


และแปลง ID ที่ส่งคืนเป็นรายการโมเดล

## การกำหนดค่าอย่างชัดเจน (โมเดลแบบกำหนดเอง)

ใช้การกำหนดค่าอย่างชัดเจนเมื่อ:

  * SGLang ทำงานบนโฮสต์/พอร์ตอื่น
  * คุณต้องการตรึงค่า `contextWindow`/`maxTokens`
  * เซิร์ฟเวอร์ของคุณต้องใช้คีย์ API จริง (หรือคุณต้องการควบคุมส่วนหัว)

json5Copy code
[code]
    {  models: {    providers: {      sglang: {        baseUrl: "http://127.0.0.1:30000/v1",        apiKey: "${SGLANG_API_KEY}",        api: "openai-completions",        models: [          {            id: "your-model-id",            name: "Local SGLang Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## การกำหนดค่าขั้นสูง

Proxy-style behavior

SGLang ถูกจัดการเป็นแบ็กเอนด์ `/v1` ที่เข้ากันได้กับ OpenAI แบบพร็อกซี ไม่ใช่ เอนด์พอยต์ OpenAI แบบเนทีฟ

พฤติกรรม | SGLang  
---|---  
การจัดรูปแบบคำขอเฉพาะ OpenAI | ไม่ได้นำไปใช้  
`service_tier`, Responses `store`, คำใบ้ prompt-cache | ไม่ส่ง  
การจัดรูปแบบเพย์โหลดที่เข้ากันได้กับ reasoning | ไม่ได้นำไปใช้  
ส่วนหัวระบุแหล่งที่มาแบบซ่อน (`originator`, `version`, `User-Agent`) | ไม่ถูกแทรกใน URL ฐาน SGLang แบบกำหนดเอง  
Troubleshooting

**ไม่สามารถเชื่อมต่อกับเซิร์ฟเวอร์ได้**

ตรวจสอบว่าเซิร์ฟเวอร์กำลังทำงานและตอบสนอง:

bashCopy code
[code]
    curl http://127.0.0.1:30000/v1/models
[/code]

**ข้อผิดพลาดการยืนยันตัวตน**

หากคำขอล้มเหลวด้วยข้อผิดพลาดการยืนยันตัวตน ให้ตั้งค่า `SGLANG_API_KEY` จริงที่ตรงกับ การกำหนดค่าเซิร์ฟเวอร์ของคุณ หรือกำหนดค่าผู้ให้บริการอย่างชัดเจนภายใต้ `models.providers.sglang`

## ที่เกี่ยวข้อง

[**Model selection** การเลือกผู้ให้บริการ การอ้างอิงโมเดล และพฤติกรรมการสลับเมื่อเกิดความล้มเหลว ](</th/concepts/model-providers>) [**Configuration reference** สคีมาการกำหนดค่าแบบเต็ม รวมถึงรายการผู้ให้บริการ ](</th/gateway/configuration-reference>)

Was this useful?YesNo