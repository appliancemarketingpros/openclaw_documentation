---
title: StepFun
source_url: https://docs.openclaw.ai/th/providers/stepfun
scraped_at: 2026-05-25
---

OpenClaw มี Plugin ผู้ให้บริการ StepFun ที่รวมมาให้ พร้อม provider id สองรายการ:

  * `stepfun` สำหรับ endpoint มาตรฐาน
  * `stepfun-plan` สำหรับ endpoint Step Plan


## ภาพรวมภูมิภาคและ endpoint

Endpoint | จีน (`.com`) | โกลบอล (`.ai`)  
---|---|---  
Standard | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
ตัวแปรสภาพแวดล้อมสำหรับ auth: `STEPFUN_API_KEY`

## แค็ตตาล็อกในตัว

Standard (`stepfun`):

Model ref | Context | เอาต์พุตสูงสุด | หมายเหตุ  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | โมเดลมาตรฐานเริ่มต้น  
  
Step Plan (`stepfun-plan`):

Model ref | Context | เอาต์พุตสูงสุด | หมายเหตุ  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | โมเดล Step Plan เริ่มต้น  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | โมเดล Step Plan เพิ่มเติม  
  
## เริ่มต้นใช้งาน

เลือกพื้นผิวผู้ให้บริการของคุณและทำตามขั้นตอนการตั้งค่า

### Standard

**เหมาะที่สุดสำหรับ:** การใช้งานทั่วไปผ่าน endpoint StepFun มาตรฐาน

* ### Choose your endpoint region

ตัวเลือก auth | Endpoint | ภูมิภาค  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | นานาชาติ  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | จีน  
* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

หรือสำหรับ endpoint จีน:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-cn
[/code]

* ### Non-interactive alternative

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider stepfun
[/code]

### Model refs

  * โมเดลเริ่มต้น: `stepfun/step-3.5-flash`


### Step Plan

**เหมาะที่สุดสำหรับ:** endpoint การให้เหตุผลของ Step Plan

* ### Choose your endpoint region

ตัวเลือก auth | Endpoint | ภูมิภาค  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | นานาชาติ  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | จีน  
* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

หรือสำหรับ endpoint จีน:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-cn
[/code]

* ### Non-interactive alternative

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider stepfun-plan
[/code]

### Model refs

  * โมเดลเริ่มต้น: `stepfun-plan/step-3.5-flash`
  * โมเดลทางเลือก: `stepfun-plan/step-3.5-flash-2603`


## การกำหนดค่าขั้นสูง

Full config: Standard provider json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Full config: Step Plan provider json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Notes

  * ผู้ให้บริการนี้รวมมากับ OpenClaw จึงไม่มีขั้นตอนติดตั้ง Plugin แยกต่างหาก
  * ขณะนี้ `step-3.5-flash-2603` เปิดให้ใช้งานเฉพาะบน `stepfun-plan`
  * โฟลว์ auth เดียวจะเขียนโปรไฟล์ที่ตรงกับภูมิภาคสำหรับทั้ง `stepfun` และ `stepfun-plan` ดังนั้นจึงค้นพบทั้งสองพื้นผิวร่วมกันได้
  * ใช้ `openclaw models list` และ `openclaw models set <provider/model>` เพื่อตรวจสอบหรือสลับโมเดล


## ที่เกี่ยวข้อง

[**Model selection** ภาพรวมของผู้ให้บริการทั้งหมด, model refs และพฤติกรรม failover ](</th/concepts/model-providers>) [**Configuration reference** schema การกำหนดค่าเต็มสำหรับผู้ให้บริการ โมเดล และ plugins ](</th/gateway/configuration-reference>) [**Model selection** วิธีเลือกและกำหนดค่าโมเดล ](</th/concepts/models>) [**StepFun Platform** การจัดการคีย์ API ของ StepFun และเอกสารประกอบ ](<https://platform.stepfun.com>)

Was this useful?YesNo