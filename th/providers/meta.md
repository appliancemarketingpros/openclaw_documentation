---
title: เมตา
source_url: https://docs.openclaw.ai/th/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

**Meta API** ใช้ **Responses API** ที่เข้ากันได้กับ OpenAI (`POST /v1/responses`) สำหรับโมเดลการให้เหตุผล `muse-spark-1.1` โดยผู้ให้บริการนี้จัดส่งมาในรูปแบบ Plugin ที่รวมมากับ OpenClaw

คุณสมบัติ | ค่า  
---|---  
รหัสผู้ให้บริการ | `meta`  
Plugin | ผู้ให้บริการที่รวมมาให้  
ตัวแปรสภาพแวดล้อมการยืนยันตัวตน | `MODEL_API_KEY`  
แฟล็กการเริ่มต้นใช้งาน | `--auth-choice meta-api-key`  
แฟล็ก CLI โดยตรง | `--meta-api-key <key>`  
API | Responses API (`openai-responses`)  
URL ฐาน | `https://api.meta.ai/v1`  
โมเดลเริ่มต้น | `meta/muse-spark-1.1`  
การให้เหตุผลเริ่มต้น | `high` (`reasoning.effort`)  
  
## เริ่มต้นใช้งาน

* ### ตั้งค่าคีย์ API

การเริ่มต้นใช้งานCopy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

แฟล็กโดยตรงCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

เฉพาะตัวแปรสภาพแวดล้อมCopy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### ตรวจสอบว่าโมเดลพร้อมใช้งาน

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

แสดงรายการแค็ตตาล็อกแบบคงที่ของ `muse-spark-1.1` หากไม่สามารถระบุค่า `MODEL_API_KEY` ได้ `openclaw models status --json` จะรายงานข้อมูลประจำตัวที่ขาดหายไปภายใต้ `auth.unusableProfiles`

## การตั้งค่าแบบไม่โต้ตอบ

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## แค็ตตาล็อกในตัว

การอ้างอิงโมเดล | ชื่อ | การให้เหตุผล | หน้าต่างบริบท | เอาต์พุตสูงสุด  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | ใช่ | 1,048,576 | 131,072  
  
ความสามารถ:

  * อินพุตข้อความและรูปภาพ
  * การเรียกใช้เครื่องมือและการสตรีม
  * ระดับความพยายามในการให้เหตุผล: `minimal`, `low`, `medium`, `high`, `xhigh` (ค่าเริ่มต้น: `high`)
  * การเล่นซ้ำการให้เหตุผลแบบเข้ารหัสโดยไม่เก็บสถานะ (`store: false`, `include: ["reasoning.encrypted_content"]`)


## การกำหนดค่าด้วยตนเอง

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## การทดสอบเบื้องต้น

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

การทดสอบแบบใช้งานจริงใช้ `muse-spark-1.1` กับ `POST /v1/responses`

## เนื้อหาที่เกี่ยวข้อง

[**ผู้ให้บริการโมเดล** การเลือกผู้ให้บริการ การอ้างอิงโมเดล และลักษณะการทำงานเมื่อสลับไปใช้ตัวสำรอง ](</th/concepts/model-providers>) [**โหมดการคิด** ระดับความพยายามในการให้เหตุผลสำหรับ muse-spark-1.1 ](</th/tools/thinking>) [**เอกสารอ้างอิงการกำหนดค่า** ค่าเริ่มต้นของเอเจนต์และการกำหนดค่าโมเดล ](</th/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue