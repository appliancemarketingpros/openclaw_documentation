---
title: Baseten
source_url: https://docs.openclaw.ai/th/providers/baseten
scraped_at: 2026-07-20
---

Get started

[API โมเดลของ Baseten](<https://docs.baseten.co/inference/model-apis/overview>) ให้บริการการเข้าถึงโมเดลแนวหน้าที่โฮสต์ไว้และเข้ากันได้กับ OpenAI Plugin ภายนอกอย่างเป็นทางการใช้การค้นหาที่ผ่านการยืนยันตัวตน ดังนั้น OpenClaw จึงใช้ชุดโมเดลทั้งหมดที่เปิดใช้งานสำหรับบัญชี Baseten ของคุณ ส่วนรายการสำรองแบบออฟไลน์ประกอบด้วย Model API ทุกรายการที่พร้อมใช้งานในขณะที่สร้าง OpenClaw รุ่นนี้

คุณสมบัติ | ค่า  
---|---  
รหัสผู้ให้บริการ | `baseten`  
Plugin | แพ็กเกจภายนอกอย่างเป็นทางการ (`@openclaw/baseten-provider`)  
ตัวแปรสภาพแวดล้อมสำหรับการยืนยันตัวตน | `BASETEN_API_KEY`  
แฟล็กการเริ่มต้นใช้งาน | `--auth-choice baseten-api-key`  
แฟล็ก CLI โดยตรง | `--baseten-api-key <key>`  
API | เข้ากันได้กับ OpenAI (`openai-completions`)  
URL ฐาน | `https://inference.baseten.co/v1`  
โมเดลเริ่มต้น | `baseten/thinkingmachines/inkling`  
  
## ติดตั้ง Plugin

bashCopy code
[code]
    openclaw plugins install @openclaw/baseten-provideropenclaw gateway restart
[/code]

## เริ่มต้นใช้งาน

* ### สร้างบัญชี Baseten และคีย์ API

แผน Basic ของ Baseten ไม่มีค่าธรรมเนียมแพลตฟอร์มรายเดือน ส่วนการเรียกใช้ Model API คิดราคาตามการใช้งาน สร้างคีย์ใน[การตั้งค่าคีย์ API ของ Baseten](<https://app.baseten.co/settings/api_keys>) และตรวจสอบอัตราปัจจุบันใน[หน้าราคา](<https://www.baseten.co/pricing>)

* ### ดำเนินการเริ่มต้นใช้งาน

OnboardingCopy code
[code]
    openclaw onboard --auth-choice baseten-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice baseten-api-key \--baseten-api-key "$BASETEN_API_KEY"
[/code]

Env onlyCopy code
[code]
    export BASETEN_API_KEY=...
[/code]

* ### ตรวจสอบแค็ตตาล็อกสด

bashCopy code
[code]
    openclaw models list --provider baseten
[/code]

เมื่อมีข้อมูลยืนยันตัวตนที่ใช้งานได้ Plugin จะร้องขอ `GET /v1/models` และแสดงทุกรุ่นโมเดลที่ส่งคืนสำหรับบัญชีนั้น หากไม่มีข้อมูลยืนยันตัวตน ระบบจะทำงานแบบออฟไลน์ต่อไปและใช้รายการสำรองที่รวมมาให้

## Inkling

[Inkling ของ Thinking Machines Lab](<https://thinkingmachines.ai/news/introducing-inkling/>) เป็นโมเดลเริ่มต้น ใน OpenClaw โมเดลนี้รองรับอินพุตข้อความและรูปภาพ การเรียกใช้เครื่องมือ สคีมาเครื่องมือแบบมีโครงสร้าง ระดับความพยายามในการให้เหตุผลที่กำหนดค่าได้ หน้าต่างบริบทขนาด 1.048M โทเค็น และโทเค็นเอาต์พุตสูงสุด 32k:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "baseten/thinkingmachines/inkling" },    },  },}
[/code]

ใช้ `/model baseten/thinkingmachines/inkling` เพื่อสลับโมเดลในการแชตที่มีอยู่

## แค็ตตาล็อกสำรองที่รวมมาให้

แค็ตตาล็อกสดที่ผ่านการยืนยันตัวตนเป็นแหล่งข้อมูลที่เชื่อถือได้ แถวเหล่านี้ช่วยให้การตั้งค่าและการเลือกโมเดลยังใช้งานได้ก่อนที่การค้นหาจะสำเร็จ:

การอ้างอิงโมเดล | อินพุต | บริบท | เอาต์พุตสูงสุด  
---|---|---|---  
`baseten/deepseek-ai/DeepSeek-V4-Pro` | ข้อความ | 262k | 262k  
`baseten/zai-org/GLM-4.7` | ข้อความ | 200k | 200k  
`baseten/zai-org/GLM-5` | ข้อความ | 202k | 202k  
`baseten/zai-org/GLM-5.1` | ข้อความ | 202k | 202k  
`baseten/zai-org/GLM-5.2` | ข้อความ | 202k | 202k  
`baseten/thinkingmachines/inkling` | ข้อความ, รูปภาพ | 1.048M | 32k  
`baseten/moonshotai/Kimi-K2.5` | ข้อความ, รูปภาพ | 262k | 262k  
`baseten/moonshotai/Kimi-K2.6` | ข้อความ, รูปภาพ | 262k | 262k  
`baseten/moonshotai/Kimi-K2.7-Code` | ข้อความ, รูปภาพ | 262k | 262k  
`baseten/nvidia/Nemotron-120B-A12B` | ข้อความ | 202k | 202k  
`baseten/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B` | ข้อความ | 202k | 202k  
`baseten/openai/gpt-oss-120b` | ข้อความ | 128k | 128k  
  
โมเดลที่รวมมาให้ทั้งหมดรองรับการเรียกใช้เครื่องมือและการให้เหตุผล OpenClaw จับคู่ระดับการคิดของตนกับโมเดลที่มี `reasoning_effort` ในตัว โมเดล GLM, Kimi และ Nemotron แบบเลือกรับของ Baseten ปิดการคิดไว้โดยค่าเริ่มต้น โดยส่วนใหญ่มีตัวควบคุมแบบไบนารี ปิด/เปิด ขณะที่ GLM 5.2 มีตัวเลือกปิด สูง และสูงสุด OpenClaw ส่งตัวเลือกเหล่านี้ผ่านตัวควบคุม `chat_template_args.enable_thinking` ของ Baseten และสำหรับ GLM 5.2 จะส่งผ่านพารามิเตอร์ระดับบนสุด `reasoning_effort` ที่ผ่านการตรวจสอบแล้ว

## การกำหนดค่าด้วยตนเอง

การตั้งค่าส่วนใหญ่ต้องใช้เพียงคีย์ API หากต้องการระบุผู้ให้บริการไว้อย่างชัดเจน:

json5Copy code
[code]
    {  env: { BASETEN_API_KEY: "..." },  agents: {    defaults: {      model: { primary: "baseten/thinkingmachines/inkling" },    },  },  models: {    mode: "merge",    providers: {      baseten: {        baseUrl: "https://inference.baseten.co/v1",        apiKey: "${BASETEN_API_KEY}",        api: "openai-completions",        models: [          {            id: "thinkingmachines/inkling",            name: "Inkling",            reasoning: true,            input: ["text", "image"],            contextWindow: 1048000,            maxTokens: 32000,            compat: {              supportsStore: false,              supportsDeveloperRole: false,              supportsUsageInStreaming: true,              supportsStrictMode: true,              supportsTools: true,              supportsReasoningEffort: true,              supportedReasoningEfforts: ["none", "minimal", "low", "medium", "high", "xhigh"],              reasoningEffortMap: {                off: "none",                none: "none",                adaptive: "xhigh",                max: "xhigh",              },              maxTokensField: "max_tokens",            },          },        ],      },    },  },}
[/code]

## เนื้อหาที่เกี่ยวข้อง

[**ผู้ให้บริการโมเดล** การเลือกผู้ให้บริการ การอ้างอิงโมเดล และลักษณะการทำงานเมื่อสลับไปใช้ระบบสำรอง ](</th/concepts/model-providers>) [**โหมดการคิด** เลือกระดับความพยายามในการให้เหตุผลของ OpenClaw ](</th/tools/thinking>) [**CLI สำหรับโมเดล** แสดง ตรวจสอบ และเลือกโมเดลที่ค้นพบ ](</th/cli/models>) [**คำถามที่พบบ่อยเกี่ยวกับโมเดล** การแก้ปัญหาโปรไฟล์การยืนยันตัวตนและการเลือกโมเดล ](</th/help/faq-models>)

Was this useful?YesNo

Open issue