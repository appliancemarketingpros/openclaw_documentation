---
title: ดอกไม้ไฟ
source_url: https://docs.openclaw.ai/th/providers/fireworks
scraped_at: 2026-05-25
---

[Fireworks](<https://fireworks.ai>) เปิดให้ใช้โมเดล open-weight และโมเดลแบบ routed ผ่าน API ที่เข้ากันได้กับ OpenAI OpenClaw มี Plugin ผู้ให้บริการ Fireworks แบบ bundled ซึ่งมาพร้อมโมเดล Kimi ที่จัดทำแค็ตตาล็อกไว้ล่วงหน้า 2 รุ่น และรับ model id หรือ router id ใดๆ ของ Fireworks ได้ขณะรันไทม์

คุณสมบัติ | ค่า  
---|---  
รหัสผู้ให้บริการ | `fireworks` (นามแฝง: `fireworks-ai`)  
Plugin | bundled, `enabledByDefault: true`  
ตัวแปรสภาพแวดล้อมสำหรับยืนยันตัวตน | `FIREWORKS_API_KEY`  
แฟล็กการเริ่มต้นใช้งาน | `--auth-choice fireworks-api-key`  
แฟล็ก CLI โดยตรง | `--fireworks-api-key <key>`  
API | เข้ากันได้กับ OpenAI (`openai-completions`)  
URL ฐาน | `https://api.fireworks.ai/inference/v1`  
โมเดลเริ่มต้น | `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`  
นามแฝงเริ่มต้น | `Kimi K2.5 Turbo`  
  
## เริ่มต้นใช้งาน

* ### Set the Fireworks API key

OnboardingCopy code
[code]
    openclaw onboard --auth-choice fireworks-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice fireworks-api-key \--fireworks-api-key "$FIREWORKS_API_KEY"
[/code]

Env onlyCopy code
[code]
    export FIREWORKS_API_KEY=fw-...
[/code]

การเริ่มต้นใช้งานจะจัดเก็บคีย์ไว้กับผู้ให้บริการ `fireworks` ในโปรไฟล์การยืนยันตัวตนของคุณ และตั้งค่าเราเตอร์ Kimi K2.5 Turbo ของ **Fire Pass** เป็นโมเดลเริ่มต้น

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider fireworks
[/code]

รายการควรมี `Kimi K2.6` และ `Kimi K2.5 Turbo (Fire Pass)` หาก `FIREWORKS_API_KEY` ไม่สามารถ resolve ได้ `openclaw models status --json` จะรายงานข้อมูลรับรองที่หายไปภายใต้ `auth.unusableProfiles`

## การตั้งค่าแบบไม่โต้ตอบ

สำหรับการติดตั้งผ่านสคริปต์หรือ CI ให้ส่งทุกอย่างผ่านบรรทัดคำสั่ง:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice fireworks-api-key \  --fireworks-api-key "$FIREWORKS_API_KEY" \  --skip-health \  --accept-risk
[/code]

## แค็ตตาล็อกในตัว

การอ้างอิงโมเดล | ชื่อ | อินพุต | คอนเท็กซ์ | เอาต์พุตสูงสุด | Thinking  
---|---|---|---|---|---  
`fireworks/accounts/fireworks/models/kimi-k2p6` | Kimi K2.6 | ข้อความ + รูปภาพ | 262,144 | 262,144 | บังคับปิด  
`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo` | Kimi K2.5 Turbo (Fire Pass) | ข้อความ + รูปภาพ | 256,000 | 256,000 | บังคับปิด (ค่าเริ่มต้น)  
  
## model id แบบกำหนดเองของ Fireworks

OpenClaw รับ model id หรือ router id ใดๆ ของ Fireworks ได้ขณะรันไทม์ ใช้ id ตรงตามที่ Fireworks แสดงและเติม prefix ด้วย `fireworks/` การ resolve แบบไดนามิกจะ clone เทมเพลต Fire Pass (อินพุตข้อความ + รูปภาพ, API ที่เข้ากันได้กับ OpenAI, ค่าใช้จ่ายเริ่มต้นเป็นศูนย์) และปิด thinking โดยอัตโนมัติเมื่อ id ตรงกับรูปแบบ Kimi

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "fireworks/accounts/fireworks/models/<your-model-id>",      },    },  },}
[/code]

How model id prefixing works

การอ้างอิงโมเดล Fireworks ทุกตัวใน OpenClaw เริ่มต้นด้วย `fireworks/` ตามด้วย id หรือเส้นทางเราเตอร์ที่ตรงจากแพลตฟอร์ม Fireworks ตัวอย่างเช่น:

  * โมเดลเราเตอร์: `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`
  * โมเดลโดยตรง: `fireworks/accounts/fireworks/models/<model-name>`


OpenClaw จะตัด prefix `fireworks/` ออกเมื่อสร้างคำขอ API และส่งเส้นทางที่เหลือไปยัง endpoint ของ Fireworks เป็นฟิลด์ `model` ที่เข้ากันได้กับ OpenAI

Why thinking is forced off for Kimi

Fireworks K2.6 จะส่งคืน 400 หากคำขอมีพารามิเตอร์ `reasoning_*` แม้ว่า Kimi จะรองรับ thinking ผ่าน API ของ Moonshot เองก็ตาม นโยบายแบบ bundled (`extensions/fireworks/thinking-policy.ts`) จะประกาศเฉพาะระดับ thinking `off` สำหรับ model id ของ Kimi เพื่อให้การสลับ `/think` แบบแมนนวลและพื้นผิวนโยบายผู้ให้บริการสอดคล้องกับสัญญารันไทม์

หากต้องการใช้การให้เหตุผลของ Kimi แบบครบวงจร ให้กำหนดค่า [ผู้ให้บริการ Moonshot](</th/providers/moonshot>) และ route โมเดลเดียวกันผ่านผู้ให้บริการนั้น

Environment availability for the daemon

หาก Gateway ทำงานเป็นบริการที่มีการจัดการ (launchd, systemd, Docker) คีย์ Fireworks ต้องมองเห็นได้สำหรับโปรเซสนั้น ไม่ใช่แค่ shell แบบโต้ตอบของคุณ

บน macOS, `openclaw gateway install` จะเชื่อม `~/.openclaw/.env` เข้ากับไฟล์สภาพแวดล้อมของ LaunchAgent อยู่แล้ว ให้รัน install อีกครั้ง (หรือ `openclaw doctor --fix`) หลังจากหมุนเวียนคีย์

## ที่เกี่ยวข้อง

[**Model providers** การเลือกผู้ให้บริการ การอ้างอิงโมเดล และพฤติกรรม failover ](</th/concepts/model-providers>) [**Thinking modes** ระดับ `/think` นโยบายผู้ให้บริการ และการ route โมเดลที่มีความสามารถด้านการให้เหตุผล ](</th/tools/thinking>) [**Moonshot** รัน Kimi พร้อมเอาต์พุต thinking แบบเนทีฟผ่าน API ของ Moonshot เอง ](</th/providers/moonshot>) [**Troubleshooting** การแก้ไขปัญหาทั่วไปและคำถามที่พบบ่อย ](</th/help/troubleshooting>)

Was this useful?YesNo