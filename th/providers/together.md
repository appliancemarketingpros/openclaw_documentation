---
title: Together AI
source_url: https://docs.openclaw.ai/th/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>) ให้การเข้าถึงโมเดลโอเพนซอร์สชั้นนำ รวมถึง Llama, DeepSeek, Kimi และอื่น ๆ ผ่าน API แบบรวมศูนย์

คุณสมบัติ | ค่า  
---|---  
ผู้ให้บริการ | `together`  
การยืนยันตัวตน | `TOGETHER_API_KEY`  
API | เข้ากันได้กับ OpenAI  
URL พื้นฐาน | `https://api.together.xyz/v1`  
  
## เริ่มต้นใช้งาน

* ### รับ API key

สร้าง API key ที่ [api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>).

* ### เรียกใช้การเริ่มต้นใช้งาน

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### ตั้งค่าโมเดลเริ่มต้น

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### ตัวอย่างแบบไม่โต้ตอบ

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## แค็ตตาล็อกในตัว

OpenClaw มาพร้อมกับแค็ตตาล็อก Together ที่รวมมาให้ดังนี้:

อ้างอิงโมเดล | ชื่อ | อินพุต | บริบท | หมายเหตุ  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | ข้อความ, รูปภาพ | 262,144 | โมเดลเริ่มต้น; เปิดใช้การให้เหตุผล  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | ข้อความ | 202,752 | โมเดลข้อความอเนกประสงค์  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | ข้อความ | 131,072 | โมเดลคำสั่งที่รวดเร็ว  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | ข้อความ, รูปภาพ | 10,000,000 | มัลติโมดัล  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | ข้อความ, รูปภาพ | 20,000,000 | มัลติโมดัล  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | ข้อความ | 131,072 | โมเดลข้อความทั่วไป  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | ข้อความ | 131,072 | โมเดลการให้เหตุผล  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | ข้อความ | 262,144 | โมเดลข้อความ Kimi สำรอง  
  
## การสร้างวิดีโอ

Plugin `together` ที่รวมมาให้ยังลงทะเบียนการสร้างวิดีโอผ่าน เครื่องมือ `video_generate` ที่ใช้ร่วมกันด้วย

คุณสมบัติ | ค่า  
---|---  
โมเดลวิดีโอเริ่มต้น | `together/Wan-AI/Wan2.2-T2V-A14B`  
โหมด | ข้อความเป็นวิดีโอ, อ้างอิงรูปภาพเดียว  
พารามิเตอร์ที่รองรับ | `aspectRatio`, `resolution`  
  
หากต้องการใช้ Together เป็นผู้ให้บริการวิดีโอเริ่มต้น:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

หมายเหตุเกี่ยวกับสภาพแวดล้อม

หาก Gateway ทำงานเป็น daemon (launchd/systemd) ให้ตรวจสอบว่า `TOGETHER_API_KEY` พร้อมใช้งานสำหรับโปรเซสนั้น (เช่น ใน `~/.openclaw/.env` หรือผ่าน `env.shellEnv`)

การแก้ไขปัญหา

  * ตรวจสอบว่าคีย์ของคุณใช้งานได้: `openclaw models list --provider together`
  * หากโมเดลไม่ปรากฏ ให้ยืนยันว่า API key ถูกตั้งค่าในสภาพแวดล้อมที่ถูกต้อง สำหรับโปรเซส Gateway ของคุณ
  * การอ้างอิงโมเดลใช้รูปแบบ `together/<model-id>`


## ที่เกี่ยวข้อง

[**การเลือกโมเดล** กฎของผู้ให้บริการ การอ้างอิงโมเดล และพฤติกรรมการสลับไปใช้ตัวสำรอง ](</th/concepts/model-providers>) [**การสร้างวิดีโอ** พารามิเตอร์เครื่องมือสร้างวิดีโอที่ใช้ร่วมกันและการเลือกผู้ให้บริการ ](</th/tools/video-generation>) [**ข้อมูลอ้างอิงการกำหนดค่า** สคีมาการกำหนดค่าแบบเต็ม รวมถึงการตั้งค่าผู้ให้บริการ ](</th/gateway/configuration-reference>) [**Together AI** แดชบอร์ด Together AI, เอกสาร API และราคา ](<https://together.ai>)

Was this useful?YesNo