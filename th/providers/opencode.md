---
title: OpenCode
source_url: https://docs.openclaw.ai/th/providers/opencode
scraped_at: 2026-05-25
---

OpenCode เปิดเผยแค็ตตาล็อกที่โฮสต์ไว้ 2 ชุดใน OpenClaw:

แค็ตตาล็อก | Prefix | Runtime provider  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
ทั้งสองแค็ตตาล็อกใช้ OpenCode API key เดียวกัน OpenClaw แยก runtime provider ids ออกจากกันเพื่อให้การกำหนดเส้นทางต่อโมเดลจากต้นทางยังคงถูกต้อง แต่ onboarding และเอกสาร จะถือว่าเป็นการตั้งค่า OpenCode ชุดเดียวกัน

## เริ่มต้นใช้งาน

### แค็ตตาล็อก Zen

**เหมาะสำหรับ:** พร็อกซีหลายโมเดลแบบคัดสรรของ OpenCode (Claude, GPT, Gemini)

* ### รัน onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

หรือส่งคีย์โดยตรง:

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### ตั้งโมเดล Zen เป็นค่าเริ่มต้น

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### ตรวจสอบว่ามีโมเดลให้ใช้งาน

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### แค็ตตาล็อก Go

**เหมาะสำหรับ:** ชุดโมเดล Kimi, GLM และ MiniMax ที่ OpenCode โฮสต์ไว้

* ### รัน onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

หรือส่งคีย์โดยตรง:

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### ตั้งโมเดล Go เป็นค่าเริ่มต้น

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### ตรวจสอบว่ามีโมเดลให้ใช้งาน

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## ตัวอย่าง config

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## แค็ตตาล็อกในตัว

### Zen

คุณสมบัติ | ค่า  
---|---  
Runtime provider | `opencode`  
ตัวอย่างโมเดล | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3-pro`  
  
### Go

คุณสมบัติ | ค่า  
---|---  
Runtime provider | `opencode-go`  
ตัวอย่างโมเดล | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## การกำหนดค่าขั้นสูง

API key aliases

`OPENCODE_ZEN_API_KEY` รองรับเช่นกันในฐานะ alias ของ `OPENCODE_API_KEY`

ข้อมูลรับรองที่ใช้ร่วมกัน

การกรอก OpenCode key หนึ่งครั้งระหว่างการตั้งค่า จะจัดเก็บข้อมูลรับรองสำหรับ runtime providers ทั้งสองตัว คุณไม่จำเป็นต้องทำ onboarding ให้แต่ละแค็ตตาล็อกแยกกัน

การเรียกเก็บเงินและแดชบอร์ด

คุณจะลงชื่อเข้าใช้ OpenCode เพิ่มรายละเอียดการเรียกเก็บเงิน และคัดลอก API key ของคุณ การเรียกเก็บเงิน และความพร้อมใช้งานของแค็ตตาล็อกจะถูกจัดการจากแดชบอร์ด OpenCode

พฤติกรรมการ replay ของ Gemini

ref ของ OpenCode ที่ใช้ Gemini เป็นฐานจะยังคงอยู่บนเส้นทาง proxy-Gemini ดังนั้น OpenClaw จะคง การทำความสะอาด thought-signature ของ Gemini ไว้ในเส้นทางนั้น โดยไม่เปิดใช้งานการตรวจสอบ replay validation แบบ Gemini ดั้งเดิม หรือการเขียน bootstrap ใหม่

พฤติกรรมการ replay ของ Non-Gemini

ref ของ OpenCode ที่ไม่ใช่ Gemini จะคงนโยบาย replay แบบ OpenAI-compatible ขั้นต่ำไว้

## ที่เกี่ยวข้อง

[**การเลือกโมเดล** การเลือก providers, model refs และพฤติกรรม failover ](</th/concepts/model-providers>) [**เอกสารอ้างอิงการตั้งค่า** เอกสารอ้างอิง config ฉบับเต็มสำหรับ agents, models และ providers ](</th/gateway/configuration-reference>)

Was this useful?YesNo