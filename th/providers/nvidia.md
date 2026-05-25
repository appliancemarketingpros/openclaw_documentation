---
title: NVIDIA
source_url: https://docs.openclaw.ai/th/providers/nvidia
scraped_at: 2026-05-25
---

NVIDIA ให้บริการ API ที่เข้ากันได้กับ OpenAI ที่ `https://integrate.api.nvidia.com/v1` สำหรับ โมเดลเปิดให้ใช้ฟรี ตรวจสอบสิทธิ์ด้วยคีย์ API จาก [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

## เริ่มต้นใช้งาน

* ### รับคีย์ API ของคุณ

สร้างคีย์ API ที่ [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

* ### ส่งออกคีย์และรันการเริ่มต้นใช้งาน

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### ตั้งค่าโมเดล NVIDIA

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

สำหรับการตั้งค่าแบบไม่โต้ตอบ คุณยังสามารถส่งคีย์โดยตรงได้:

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## ตัวอย่างการกำหนดค่า

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## แค็ตตาล็อกในตัว

ข้อมูลอ้างอิงโมเดล | ชื่อ | บริบท | เอาต์พุตสูงสุด  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## การกำหนดค่าขั้นสูง

พฤติกรรมการเปิดใช้งานอัตโนมัติ

ผู้ให้บริการจะเปิดใช้งานโดยอัตโนมัติเมื่อตั้งค่าตัวแปรสภาพแวดล้อม `NVIDIA_API_KEY` ไม่จำเป็นต้องมีการกำหนดค่าผู้ให้บริการอย่างชัดเจนนอกเหนือจากคีย์

แค็ตตาล็อกและราคา

แค็ตตาล็อกที่มาพร้อมกันเป็นแบบคงที่ ต้นทุนมีค่าเริ่มต้นเป็น `0` ในซอร์ส เนื่องจาก NVIDIA ขณะนี้ให้การเข้าถึง API ฟรีสำหรับโมเดลที่ระบุไว้

เอนด์พอยต์ที่เข้ากันได้กับ OpenAI

NVIDIA ใช้เอนด์พอยต์ completions มาตรฐาน `/v1` เครื่องมือใดๆ ที่เข้ากันได้กับ OpenAI ควรใช้งานได้ทันทีด้วย URL ฐานของ NVIDIA

การตอบกลับของผู้ให้บริการแบบกำหนดเองที่ช้า

โมเดลแบบกำหนดเองบางรายการที่โฮสต์บน NVIDIA อาจใช้เวลานานกว่า model idle watchdog เริ่มต้นก่อนที่จะปล่อยชิ้นส่วนการตอบกลับแรก สำหรับรายการผู้ให้บริการ NVIDIA แบบกำหนดเอง ให้เพิ่ม timeout ของผู้ให้บริการแทนการเพิ่ม timeout ของ runtime ของเอเจนต์ทั้งหมด:

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## ที่เกี่ยวข้อง

[**การเลือกโมเดล** การเลือกผู้ให้บริการ ข้อมูลอ้างอิงโมเดล และพฤติกรรม failover ](</th/concepts/model-providers>) [**ข้อมูลอ้างอิงการกำหนดค่า** ข้อมูลอ้างอิงการกำหนดค่าฉบับเต็มสำหรับเอเจนต์ โมเดล และผู้ให้บริการ ](</th/gateway/configuration-reference>)

Was this useful?YesNo