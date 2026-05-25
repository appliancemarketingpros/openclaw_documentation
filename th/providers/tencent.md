---
title: Tencent Cloud (TokenHub)
source_url: https://docs.openclaw.ai/th/providers/tencent
scraped_at: 2026-05-25
---

Tencent Cloud จัดส่งมาเป็น Plugin ผู้ให้บริการที่บันเดิลมากับ OpenClaw โดยให้เข้าถึง Tencent Hy3 preview ผ่านเอ็นด์พอยต์ TokenHub (`tencent-tokenhub`) ด้วย API ที่เข้ากันได้กับ OpenAI

คุณสมบัติ | ค่า  
---|---  
รหัสผู้ให้บริการ | `tencent-tokenhub`  
Plugin | บันเดิลมา, `enabledByDefault: true`  
ตัวแปร env สำหรับการยืนยันตัวตน | `TOKENHUB_API_KEY`  
แฟล็กการเริ่มต้นใช้งาน | `--auth-choice tokenhub-api-key`  
แฟล็ก CLI โดยตรง | `--tokenhub-api-key <key>`  
API | เข้ากันได้กับ OpenAI (`openai-completions`)  
URL ฐานเริ่มต้น | `https://tokenhub.tencentmaas.com/v1`  
URL ฐานส่วนกลาง | `https://tokenhub-intl.tencentmaas.com/v1` (เขียนทับค่าได้)  
โมเดลเริ่มต้น | `tencent-tokenhub/hy3-preview`  
  
## เริ่มต้นอย่างรวดเร็ว

* ### สร้างคีย์ TokenHub API

สร้างคีย์ API ใน Tencent Cloud TokenHub หากคุณเลือกขอบเขตการเข้าถึงแบบจำกัดสำหรับคีย์ ให้รวม **Hy3 preview** ไว้ในโมเดลที่อนุญาตด้วย

* ### เรียกใช้การเริ่มต้นใช้งาน

OnboardingCopy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

Env onlyCopy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### ตรวจสอบโมเดล

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## การตั้งค่าแบบไม่โต้ตอบ

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## แค็ตตาล็อกในตัว

อ้างอิงโมเดล | ชื่อ | อินพุต | บริบท | เอาต์พุตสูงสุด | หมายเหตุ  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | Hy3 preview (TokenHub) | text | 256,000 | 64,000 | ค่าเริ่มต้น; รองรับการใช้เหตุผล  
  
Hy3 preview คือโมเดลภาษา MoE ขนาดใหญ่ของ Tencent Hunyuan สำหรับการใช้เหตุผล การทำตามคำสั่งในบริบทยาว โค้ด และเวิร์กโฟลว์ของเอเจนต์ ตัวอย่างที่เข้ากันได้กับ OpenAI ของ Tencent ใช้ `hy3-preview` เป็นรหัสโมเดล และรองรับการเรียกใช้เครื่องมือแบบ chat-completions มาตรฐาน รวมถึง `reasoning_effort`

## การกำหนดราคาแบบแบ่งระดับ

แค็ตตาล็อกที่บันเดิลมาจัดส่งมาพร้อมเมทาดาทาต้นทุนแบบแบ่งระดับ ซึ่งปรับตามความยาวของหน้าต่างอินพุต ดังนั้นการประมาณต้นทุนจึงถูกเติมให้โดยไม่ต้องเขียนทับค่าด้วยตนเอง

ช่วงโทเค็นอินพุต | อัตราอินพุต | อัตราเอาต์พุต | การอ่านแคช  
---|---|---|---  
0 - 16,000 | 0.176 | 0.587 | 0.059  
16,000 - 32,000 | 0.235 | 0.939 | 0.088  
32,000+ | 0.293 | 1.173 | 0.117  
  
อัตราคิดเป็นต่อหนึ่งล้านโทเค็นในสกุล USD ตามที่ Tencent ประกาศไว้ เขียนทับการกำหนดราคาใต้ `models.providers.tencent-tokenhub` เฉพาะเมื่อคุณต้องการพื้นผิวที่แตกต่าง

## การกำหนดค่าขั้นสูง

เขียนทับเอ็นด์พอยต์

OpenClaw ใช้เอ็นด์พอยต์ `https://tokenhub.tencentmaas.com/v1` ของ Tencent Cloud เป็นค่าเริ่มต้น Tencent ยังมีเอกสารเอ็นด์พอยต์ TokenHub ระหว่างประเทศด้วย:

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

เขียนทับเอ็นด์พอยต์เฉพาะเมื่อบัญชีหรือภูมิภาค TokenHub ของคุณกำหนดให้ต้องใช้เท่านั้น

ความพร้อมใช้งานของสภาพแวดล้อมสำหรับดีมอน

หาก Gateway ทำงานเป็นบริการที่มีการจัดการ (launchd, systemd, Docker), `TOKENHUB_API_KEY` ต้องมองเห็นได้สำหรับโปรเซสนั้น ตั้งค่าไว้ใน `~/.openclaw/.env` หรือผ่าน `env.shellEnv` เพื่อให้สภาพแวดล้อมของ launchd, systemd หรือ Docker exec อ่านได้

## ที่เกี่ยวข้อง

[**ผู้ให้บริการโมเดล** การเลือกผู้ให้บริการ อ้างอิงโมเดล และพฤติกรรมการเฟลโอเวอร์ ](</th/concepts/model-providers>) [**ข้อมูลอ้างอิงการกำหนดค่า** สคีมาการกำหนดค่าฉบับเต็ม รวมถึงการตั้งค่าผู้ให้บริการ ](</th/gateway/configuration>) [**Tencent TokenHub** หน้าผลิตภัณฑ์ TokenHub ของ Tencent Cloud ](<https://cloud.tencent.com/product/tokenhub>) [**การ์ดโมเดล Hy3 preview** รายละเอียดและเบนช์มาร์กของ Tencent Hunyuan Hy3 preview ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo