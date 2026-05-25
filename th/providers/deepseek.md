---
title: DeepSeek
source_url: https://docs.openclaw.ai/th/providers/deepseek
scraped_at: 2026-05-25
---

[DeepSeek](<https://www.deepseek.com>) มีโมเดล AI ที่ทรงพลังพร้อม API ที่เข้ากันได้กับ OpenAI

คุณสมบัติ | ค่า  
---|---  
ผู้ให้บริการ | `deepseek`  
การยืนยันตัวตน | `DEEPSEEK_API_KEY`  
API | เข้ากันได้กับ OpenAI  
URL ฐาน | `https://api.deepseek.com`  
  
## เริ่มต้นใช้งาน

* ### รับ API key ของคุณ

สร้าง API key ที่ [platform.deepseek.com](<https://platform.deepseek.com/api_keys>)

* ### เรียกใช้การตั้งค่าเริ่มต้น

bashCopy code
[code]
    openclaw onboard --auth-choice deepseek-api-key
[/code]

คำสั่งนี้จะแจ้งให้ป้อน API key ของคุณและตั้ง `deepseek/deepseek-v4-flash` เป็นโมเดลเริ่มต้น

* ### ตรวจสอบว่ามีโมเดลพร้อมใช้งาน

bashCopy code
[code]
    openclaw models list --provider deepseek
[/code]

หากต้องการตรวจสอบแคตตาล็อกแบบคงที่ที่รวมมาโดยไม่ต้องมี Gateway ที่กำลังทำงานอยู่ ให้ใช้:

bashCopy code
[code]
    openclaw models list --all --provider deepseek
[/code]

การตั้งค่าแบบไม่โต้ตอบ

สำหรับการติดตั้งผ่านสคริปต์หรือแบบไม่มีหน้าจอ ให้ส่งแฟล็กทั้งหมดโดยตรง:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice deepseek-api-key \  --deepseek-api-key "$DEEPSEEK_API_KEY" \  --skip-health \  --accept-risk
[/code]

## แคตตาล็อกในตัว

อ้างอิงโมเดล | ชื่อ | อินพุต | บริบท | เอาต์พุตสูงสุด | หมายเหตุ  
---|---|---|---|---|---  
`deepseek/deepseek-v4-flash` | DeepSeek V4 Flash | text | 1,000,000 | 384,000 | โมเดลเริ่มต้น; พื้นผิว V4 ที่รองรับการคิด  
`deepseek/deepseek-v4-pro` | DeepSeek V4 Pro | text | 1,000,000 | 384,000 | พื้นผิว V4 ที่รองรับการคิด  
`deepseek/deepseek-chat` | DeepSeek Chat | text | 131,072 | 8,192 | พื้นผิว DeepSeek V3.2 แบบไม่คิด  
`deepseek/deepseek-reasoner` | DeepSeek Reasoner | text | 131,072 | 65,536 | พื้นผิว V3.2 ที่เปิดใช้การให้เหตุผล  
  
## การคิดและเครื่องมือ

เซสชันการคิดของ DeepSeek V4 มีสัญญาการเล่นซ้ำที่เข้มงวดกว่าผู้ให้บริการส่วนใหญ่ ที่เข้ากันได้กับ OpenAI: หลังจากรอบที่เปิดใช้การคิดใช้เครื่องมือแล้ว DeepSeek คาดว่าข้อความ assistant ที่เล่นซ้ำจากรอบนั้นจะมี `reasoning_content` ในคำขอต่อเนื่อง OpenClaw จัดการเรื่องนี้ภายใน Plugin ของ DeepSeek ดังนั้นการใช้เครื่องมือแบบหลายรอบตามปกติจึงทำงานได้กับ `deepseek/deepseek-v4-flash` และ `deepseek/deepseek-v4-pro`

หากคุณสลับเซสชันที่มีอยู่จากผู้ให้บริการอื่นที่เข้ากันได้กับ OpenAI ไปเป็น โมเดล DeepSeek V4 รอบการเรียกใช้เครื่องมือของ assistant รุ่นเก่าอาจไม่มี `reasoning_content` แบบเนทีฟของ DeepSeek OpenClaw เติมฟิลด์ที่ขาดหายไปนั้นในข้อความ assistant ที่เล่นซ้ำสำหรับคำขอการคิดของ DeepSeek V4 เพื่อให้ผู้ให้บริการยอมรับ ประวัติได้โดยไม่ต้องใช้ `/new`

เมื่อปิดใช้การคิดใน OpenClaw (รวมถึงการเลือก **None** ใน UI) OpenClaw จะส่ง `thinking: { type: "disabled" }` ของ DeepSeek และตัด `reasoning_content` ที่เล่นซ้ำออกจากประวัติขาออก ซึ่งทำให้เซสชันที่ปิดการคิด อยู่บนเส้นทาง DeepSeek แบบไม่คิด

ใช้ `deepseek/deepseek-v4-flash` สำหรับเส้นทางเร็วเริ่มต้น ใช้ `deepseek/deepseek-v4-pro` เมื่อคุณต้องการโมเดล V4 ที่แข็งแกร่งกว่าและยอมรับ ค่าใช้จ่ายหรือเวลาแฝงที่สูงขึ้นได้

## การทดสอบสด

ชุดทดสอบโมเดลสดโดยตรงรวม DeepSeek V4 ไว้ในชุดโมเดลสมัยใหม่ หากต้องการ เรียกใช้เฉพาะการตรวจสอบโมเดลโดยตรงของ DeepSeek V4:

bashCopy code
[code]
    OPENCLAW_LIVE_PROVIDERS=deepseek \OPENCLAW_LIVE_MODELS="deepseek/deepseek-v4-flash,deepseek/deepseek-v4-pro" \pnpm test:live src/agents/models.profiles.live.test.ts
[/code]

การตรวจสอบสดนั้นยืนยันว่าโมเดล V4 ทั้งสองสามารถทำงานให้เสร็จได้ และรอบต่อเนื่อง ของการคิด/เครื่องมือรักษาเพย์โหลดการเล่นซ้ำที่ DeepSeek ต้องการไว้

## ตัวอย่างการกำหนดค่า

json5Copy code
[code]
    {  env: { DEEPSEEK_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "deepseek/deepseek-v4-flash" },    },  },}
[/code]

## ที่เกี่ยวข้อง

[**การเลือกโมเดล** การเลือกผู้ให้บริการ การอ้างอิงโมเดล และพฤติกรรมการสลับไปใช้สำรอง ](</th/concepts/model-providers>) [**ข้อมูลอ้างอิงการกำหนดค่า** ข้อมูลอ้างอิงการกำหนดค่าฉบับเต็มสำหรับ agent โมเดล และผู้ให้บริการ ](</th/gateway/configuration-reference>)

Was this useful?YesNo