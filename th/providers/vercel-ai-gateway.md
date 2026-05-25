---
title: Vercel AI Gateway
source_url: https://docs.openclaw.ai/th/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

[Vercel AI Gateway](<https://vercel.com/ai-gateway>) มี API แบบรวมศูนย์เพื่อ เข้าถึงโมเดลหลายร้อยรายการผ่าน endpoint เดียว

คุณสมบัติ | ค่า  
---|---  
ผู้ให้บริการ | `vercel-ai-gateway`  
การยืนยันตัวตน | `AI_GATEWAY_API_KEY`  
API | เข้ากันได้กับ Anthropic Messages  
แค็ตตาล็อกโมเดล | ค้นพบอัตโนมัติผ่าน `/v1/models`  
  
## เริ่มต้นใช้งาน

* ### ตั้งค่า API key

เรียกใช้ onboarding แล้วเลือกตัวเลือกการยืนยันตัวตนของ AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### ตั้งค่าโมเดลเริ่มต้น

เพิ่มโมเดลลงในการกำหนดค่า OpenClaw ของคุณ:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### ตรวจสอบว่าโมเดลพร้อมใช้งาน

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## ตัวอย่างแบบไม่โต้ตอบ

สำหรับการตั้งค่าด้วยสคริปต์หรือ CI ให้ส่งค่าทั้งหมดผ่านบรรทัดคำสั่ง:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## รูปแบบย่อของ Model ID

OpenClaw ยอมรับ Vercel Claude shorthand model refs และทำให้เป็นรูปแบบมาตรฐานใน runtime:

อินพุตแบบย่อ | model ref ที่ทำให้เป็นรูปแบบมาตรฐาน  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## การกำหนดค่าขั้นสูง

ตัวแปรสภาพแวดล้อมสำหรับ daemon processes

หาก OpenClaw Gateway ทำงานเป็น daemon (launchd/systemd) ให้ตรวจสอบว่า `AI_GATEWAY_API_KEY` พร้อมใช้งานสำหรับ process นั้น

การกำหนดเส้นทางของผู้ให้บริการ

Vercel AI Gateway กำหนดเส้นทางคำขอไปยัง upstream provider ตาม prefix ของ model ref ตัวอย่างเช่น `vercel-ai-gateway/anthropic/claude-opus-4.6` จะถูกกำหนดเส้นทาง ผ่าน Anthropic ส่วน `vercel-ai-gateway/openai/gpt-5.5` จะถูกกำหนดเส้นทางผ่าน OpenAI และ `vercel-ai-gateway/moonshotai/kimi-k2.6` จะถูกกำหนดเส้นทางผ่าน MoonshotAI `AI_GATEWAY_API_KEY` เดียวของคุณจัดการการยืนยันตัวตนสำหรับ upstream providers ทั้งหมด

ระดับการคิด

ตัวเลือก `/think` จะทำตาม prefixes ของ upstream model ที่เชื่อถือได้เมื่อ OpenClaw รู้ สัญญาของ upstream provider `vercel-ai-gateway/anthropic/...` ใช้ Claude thinking profile รวมถึงค่าเริ่มต้นแบบปรับตัวได้สำหรับโมเดล Claude 4.6 `vercel-ai-gateway/openai/gpt-5.4`, `gpt-5.5` และ refs แบบ Codex จะแสดง `/think xhigh` เช่นเดียวกับผู้ให้บริการ OpenAI/OpenAI Codex โดยตรง ส่วน refs แบบ namespaced อื่นจะคงระดับ reasoning ปกติไว้ เว้นแต่ metadata ของแค็ตตาล็อกจะประกาศไว้มากกว่านั้น

## ที่เกี่ยวข้อง

[**การเลือกโมเดล** การเลือกผู้ให้บริการ model refs และพฤติกรรม failover ](</th/concepts/model-providers>) [**การแก้ไขปัญหา** การแก้ไขปัญหาทั่วไปและ FAQ ](</th/help/troubleshooting>)

Was this useful?YesNo