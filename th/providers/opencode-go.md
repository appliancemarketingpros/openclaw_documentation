---
title: OpenCode Go
source_url: https://docs.openclaw.ai/th/providers/opencode-go
scraped_at: 2026-05-25
---

OpenCode Go คือแค็ตตาล็อก Go ภายใน [OpenCode](</th/providers/opencode>) โดยใช้ `OPENCODE_API_KEY` เดียวกันกับแค็ตตาล็อก Zen แต่คงรหัสผู้ให้บริการรันไทม์เป็น `opencode-go` เพื่อให้การกำหนดเส้นทางต่อโมเดลจากต้นทางยังคงถูกต้อง

คุณสมบัติ | ค่า  
---|---  
ผู้ให้บริการรันไทม์ | `opencode-go`  
การยืนยันตัวตน | `OPENCODE_API_KEY`  
การตั้งค่าหลัก | [OpenCode](</th/providers/opencode>)  
  
## แค็ตตาล็อกในตัว

OpenClaw ดึงรายการส่วนใหญ่ของแค็ตตาล็อก Go จากรีจิสทรีโมเดล pi ที่มาพร้อมกับระบบ และเสริมรายการปัจจุบันจากต้นทางระหว่างที่รีจิสทรีกำลังอัปเดตให้ทัน ใช้คำสั่ง `openclaw models list --provider opencode-go` เพื่อดูรายการโมเดลปัจจุบัน

ผู้ให้บริการนี้ประกอบด้วย:

การอ้างอิงโมเดล | ชื่อ  
---|---  
`opencode-go/glm-5` | GLM-5  
`opencode-go/glm-5.1` | GLM-5.1  
`opencode-go/kimi-k2.5` | Kimi K2.5  
`opencode-go/kimi-k2.6` | Kimi K2.6 (ขีดจำกัด 3 เท่า)  
`opencode-go/deepseek-v4-pro` | DeepSeek V4 Pro  
`opencode-go/deepseek-v4-flash` | DeepSeek V4 Flash  
`opencode-go/mimo-v2-omni` | MiMo V2 Omni  
`opencode-go/mimo-v2-pro` | MiMo V2 Pro  
`opencode-go/minimax-m2.5` | MiniMax M2.5  
`opencode-go/minimax-m2.7` | MiniMax M2.7  
`opencode-go/qwen3.5-plus` | Qwen3.5 Plus  
`opencode-go/qwen3.6-plus` | Qwen3.6 Plus  
  
## เริ่มต้นใช้งาน

### โต้ตอบ

* ### เรียกใช้การตั้งค่าเริ่มต้น

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

* ### ตั้งค่าโมเดล Go เป็นค่าเริ่มต้น

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### ตรวจสอบว่ามีโมเดลพร้อมใช้งาน

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

### ไม่โต้ตอบ

* ### ส่งคีย์โดยตรง

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### ตรวจสอบว่ามีโมเดลพร้อมใช้งาน

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## ตัวอย่างการกำหนดค่า

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "YOUR_API_KEY_HERE" }, // pragma: allowlist secret  agents: { defaults: { model: { primary: "opencode-go/kimi-k2.6" } } },}
[/code]

## การกำหนดค่าขั้นสูง

พฤติกรรมการกำหนดเส้นทาง

OpenClaw จัดการการกำหนดเส้นทางต่อโมเดลโดยอัตโนมัติเมื่อการอ้างอิงโมเดลใช้ `opencode-go/...` โดยไม่ต้องมีการกำหนดค่าผู้ให้บริการเพิ่มเติม

รูปแบบการอ้างอิงรันไทม์

การอ้างอิงรันไทม์ยังคงระบุอย่างชัดเจน: `opencode/...` สำหรับ Zen, `opencode-go/...` สำหรับ Go วิธีนี้ช่วยให้การกำหนดเส้นทางต่อโมเดลจากต้นทางถูกต้องในทั้งสองแค็ตตาล็อก

ข้อมูลรับรองที่ใช้ร่วมกัน

ทั้งแค็ตตาล็อก Zen และ Go ใช้ `OPENCODE_API_KEY` เดียวกัน เมื่อป้อน คีย์ระหว่างการตั้งค่า ระบบจะจัดเก็บข้อมูลรับรองให้กับผู้ให้บริการรันไทม์ทั้งสองรายการ

## ที่เกี่ยวข้อง

[**OpenCode (หลัก)** การตั้งค่าที่ใช้ร่วมกัน ภาพรวมแค็ตตาล็อก และหมายเหตุขั้นสูง ](</th/providers/opencode>) [**การเลือกโมเดล** การเลือกผู้ให้บริการ การอ้างอิงโมเดล และพฤติกรรมการสลับสำรอง ](</th/concepts/model-providers>)

Was this useful?YesNo