---
title: Qianfan
source_url: https://docs.openclaw.ai/th/providers/qianfan
scraped_at: 2026-05-25
---

Qianfan คือแพลตฟอร์ม MaaS ของ Baidu ซึ่งมี **API แบบรวมศูนย์** ที่ส่งคำขอไปยังโมเดลจำนวนมากหลัง endpoint และ API key เดียว แพลตฟอร์มนี้เข้ากันได้กับ OpenAI ดังนั้น OpenAI SDK ส่วนใหญ่จึงทำงานได้โดยเปลี่ยน base URL

คุณสมบัติ | ค่า  
---|---  
ผู้ให้บริการ | `qianfan`  
การยืนยันตัวตน | `QIANFAN_API_KEY`  
API | เข้ากันได้กับ OpenAI  
Base URL | `https://qianfan.baidubce.com/v2`  
  
## เริ่มต้นใช้งาน

* ### Create a Baidu Cloud account

สมัครหรือล็อกอินที่ [Qianfan Console](<https://console.bce.baidu.com/qianfan/ais/console/apiKey>) และตรวจสอบให้แน่ใจว่าคุณเปิดใช้งานการเข้าถึง Qianfan API แล้ว

* ### Generate an API key

สร้างแอปพลิเคชันใหม่หรือเลือกแอปพลิเคชันที่มีอยู่ จากนั้นสร้าง API key รูปแบบของคีย์คือ `bce-v3/ALTAK-...`

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice qianfan-api-key
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider qianfan
[/code]

## แค็ตตาล็อกในตัว

การอ้างอิงโมเดล | อินพุต | บริบท | เอาต์พุตสูงสุด | การให้เหตุผล | หมายเหตุ  
---|---|---|---|---|---  
`qianfan/deepseek-v3.2` | ข้อความ | 98,304 | 32,768 | ใช่ | โมเดลเริ่มต้น  
`qianfan/ernie-5.0-thinking-preview` | ข้อความ, รูปภาพ | 119,000 | 64,000 | ใช่ | หลายรูปแบบ  
  
## ตัวอย่างการกำหนดค่า

json5Copy code
[code]
    {  env: { QIANFAN_API_KEY: "bce-v3/ALTAK-..." },  agents: {    defaults: {      model: { primary: "qianfan/deepseek-v3.2" },      models: {        "qianfan/deepseek-v3.2": { alias: "QIANFAN" },      },    },  },  models: {    providers: {      qianfan: {        baseUrl: "https://qianfan.baidubce.com/v2",        api: "openai-completions",        models: [          {            id: "deepseek-v3.2",            name: "DEEPSEEK V3.2",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 98304,            maxTokens: 32768,          },          {            id: "ernie-5.0-thinking-preview",            name: "ERNIE-5.0-Thinking-Preview",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 119000,            maxTokens: 64000,          },        ],      },    },  },}
[/code]

Transport and compatibility

Qianfan ทำงานผ่านเส้นทางการส่งข้อมูลที่เข้ากันได้กับ OpenAI ไม่ใช่การจัดรูปแบบคำขอแบบเนทีฟของ OpenAI ซึ่งหมายความว่าฟีเจอร์มาตรฐานของ OpenAI SDK ใช้งานได้ แต่พารามิเตอร์เฉพาะผู้ให้บริการอาจไม่ถูกส่งต่อ

Catalog and overrides

แค็ตตาล็อกที่บันเดิลมาในปัจจุบันมี `deepseek-v3.2` และ `ernie-5.0-thinking-preview` เพิ่มหรือแทนที่ `models.providers.qianfan` เฉพาะเมื่อคุณต้องการ base URL แบบกำหนดเองหรือข้อมูลเมตาของโมเดลเท่านั้น

Troubleshooting

  * ตรวจสอบให้แน่ใจว่า API key ของคุณขึ้นต้นด้วย `bce-v3/ALTAK-` และเปิดใช้งานการเข้าถึง Qianfan API ในคอนโซล Baidu Cloud แล้ว
  * หากไม่มีการแสดงรายการโมเดล ให้ยืนยันว่าบัญชีของคุณเปิดใช้งานบริการ Qianfan แล้ว
  * base URL เริ่มต้นคือ `https://qianfan.baidubce.com/v2` เปลี่ยนเฉพาะเมื่อคุณใช้ endpoint หรือพร็อกซีแบบกำหนดเองเท่านั้น


## ที่เกี่ยวข้อง

[**Model selection** การเลือกผู้ให้บริการ การอ้างอิงโมเดล และพฤติกรรมการสลับไปใช้ระบบสำรองเมื่อเกิดข้อผิดพลาด ](</th/concepts/model-providers>) [**Configuration reference** เอกสารอ้างอิงการกำหนดค่า OpenClaw ฉบับเต็ม ](</th/gateway/configuration-reference>) [**Agent setup** การกำหนดค่าเริ่มต้นของเอเจนต์และการกำหนดโมเดล ](</th/concepts/agent>) [**Qianfan API docs** เอกสาร API อย่างเป็นทางการของ Qianfan ](<https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb>)

Was this useful?YesNo