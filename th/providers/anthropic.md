---
title: Anthropic
source_url: https://docs.openclaw.ai/th/providers/anthropic
scraped_at: 2026-05-25
---

Anthropic สร้างตระกูลโมเดล **Claude** OpenClaw รองรับเส้นทางการยืนยันตัวตนสองแบบ:

  * **คีย์ API** — เข้าถึง Anthropic API โดยตรงพร้อมการเรียกเก็บเงินตามการใช้งาน (โมเดล `anthropic/*`)
  * **Claude CLI** — ใช้การเข้าสู่ระบบ Claude CLI ที่มีอยู่บนโฮสต์เดียวกันซ้ำ


## เริ่มต้นใช้งาน

### คีย์ API

**เหมาะสำหรับ:** การเข้าถึง API มาตรฐานและการเรียกเก็บเงินตามการใช้งาน

* ### รับคีย์ API ของคุณ

สร้างคีย์ API ใน [Anthropic Console](<https://console.anthropic.com/>)

* ### เรียกใช้การเริ่มต้นใช้งาน

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

หรือส่งคีย์โดยตรง:

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### ตรวจสอบว่าโมเดลพร้อมใช้งาน

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### ตัวอย่างการกำหนดค่า

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "sk-ant-..." },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### Claude CLI

**เหมาะสำหรับ:** การใช้การเข้าสู่ระบบ Claude CLI ที่มีอยู่ซ้ำโดยไม่ต้องมีคีย์ API แยกต่างหาก

* ### ตรวจสอบให้แน่ใจว่าติดตั้งและเข้าสู่ระบบ Claude CLI แล้ว

ตรวจสอบด้วย:

bashCopy code
[code]
    claude --version
[/code]

* ### เรียกใช้การเริ่มต้นใช้งาน

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

OpenClaw ตรวจพบและใช้ข้อมูลรับรอง Claude CLI ที่มีอยู่ซ้ำ

* ### ตรวจสอบว่าโมเดลพร้อมใช้งาน

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### ตัวอย่างการกำหนดค่า

แนะนำให้ใช้การอ้างอิงโมเดล Anthropic แบบมาตรฐานร่วมกับการแทนที่รันไทม์ CLI:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-7" },      models: {        "anthropic/claude-opus-4-7": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

การอ้างอิงโมเดลแบบเดิม `claude-cli/claude-opus-4-7` ยังคงใช้งานได้เพื่อ ความเข้ากันได้ แต่การกำหนดค่าใหม่ควรเก็บการเลือก provider/model เป็น `anthropic/*` และใส่แบ็กเอนด์การทำงานไว้ในนโยบายรันไทม์ของ provider/model

## ค่าเริ่มต้นของการคิด (Claude 4.6)

โมเดล Claude 4.6 มีค่าเริ่มต้นเป็นการคิดแบบ `adaptive` ใน OpenClaw เมื่อไม่ได้ตั้งค่าระดับการคิดไว้อย่างชัดเจน

แทนที่แบบรายข้อความด้วย `/think:<level>` หรือในพารามิเตอร์โมเดล:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { thinking: "adaptive" },        },      },    },  },}
[/code]

## การแคชพรอมป์

OpenClaw รองรับฟีเจอร์การแคชพรอมป์ของ Anthropic สำหรับการยืนยันตัวตนด้วยคีย์ API

ค่า | ระยะเวลาแคช | คำอธิบาย  
---|---|---  
`"short"` (ค่าเริ่มต้น) | 5 นาที | ใช้โดยอัตโนมัติสำหรับการยืนยันตัวตนด้วยคีย์ API  
`"long"` | 1 ชั่วโมง | แคชแบบขยาย  
`"none"` | ไม่มีการแคช | ปิดใช้งานการแคชพรอมป์  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

การแทนที่แคชต่อเอเจนต์

ใช้พารามิเตอร์ระดับโมเดลเป็นค่าพื้นฐาน แล้วแทนที่เอเจนต์เฉพาะผ่าน `agents.list[].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

ลำดับการผสานการกำหนดค่า:

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params` (จับคู่ `id`, แทนที่ตามคีย์)


สิ่งนี้ช่วยให้เอเจนต์หนึ่งรักษาแคชระยะยาวไว้ได้ ขณะที่เอเจนต์อีกตัวบนโมเดลเดียวกันปิดการแคชสำหรับทราฟฟิกที่มาเป็นช่วง ๆ หรือมีการใช้ซ้ำน้อย

หมายเหตุ Bedrock Claude

  * โมเดล Anthropic Claude บน Bedrock (`amazon-bedrock/*anthropic.claude*`) ยอมรับการส่งผ่าน `cacheRetention` เมื่อกำหนดค่าไว้
  * โมเดล Bedrock ที่ไม่ใช่ Anthropic จะถูกบังคับเป็น `cacheRetention: "none"` ขณะรันไทม์
  * ค่าเริ่มต้นอัจฉริยะสำหรับคีย์ API ยังตั้งต้น `cacheRetention: "short"` สำหรับการอ้างอิง Claude-on-Bedrock เมื่อไม่ได้ตั้งค่าไว้อย่างชัดเจน


## การกำหนดค่าขั้นสูง

โหมดเร็ว

สวิตช์ `/fast` ที่ใช้ร่วมกันของ OpenClaw รองรับทราฟฟิก Anthropic โดยตรง (คีย์ API และ OAuth ไปยัง `api.anthropic.com`)

คำสั่ง | แมปไปยัง  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

การเข้าใจสื่อ (รูปภาพและ PDF)

Plugin Anthropic ที่มาพร้อมระบบลงทะเบียนการเข้าใจรูปภาพและ PDF OpenClaw แก้ความสามารถด้านสื่อโดยอัตโนมัติจากการยืนยันตัวตน Anthropic ที่กำหนดค่าไว้ — ไม่จำเป็นต้องมี การกำหนดค่าเพิ่มเติม

คุณสมบัติ | ค่า  
---|---  
โมเดลเริ่มต้น | `claude-opus-4-7`  
อินพุตที่รองรับ | รูปภาพ, เอกสาร PDF  
  
เมื่อแนบรูปภาพหรือ PDF กับการสนทนา OpenClaw จะกำหนดเส้นทางผ่านผู้ให้บริการการเข้าใจสื่อของ Anthropic โดยอัตโนมัติ

หน้าต่างบริบท 1M (เบต้า)

หน้าต่างบริบท 1M ของ Anthropic ถูกควบคุมด้วยเบต้า เปิดใช้ต่อโมเดล:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { context1m: true },        },      },    },  },}
[/code]

OpenClaw แมปสิ่งนี้เป็น `anthropic-beta: context-1m-2025-08-07` บนคำขอ

`params.context1m: true` ยังใช้กับแบ็กเอนด์ Claude CLI (`claude-cli/*`) สำหรับโมเดล Opus และ Sonnet ที่มีสิทธิ์ โดยขยายหน้าต่างบริบท ของรันไทม์สำหรับเซสชัน CLI เหล่านั้นให้ตรงกับพฤติกรรม API โดยตรง

บริบท 1M ของ Claude Opus 4.7

`anthropic/claude-opus-4.7` และเวอร์ชัน `claude-cli` ของมันมีหน้าต่างบริบท 1M โดยค่าเริ่มต้น — ไม่ต้องใช้ `params.context1m: true`

## การแก้ไขปัญหา

ข้อผิดพลาด 401 / โทเค็นใช้งานไม่ได้กะทันหัน

การยืนยันตัวตนด้วยโทเค็นของ Anthropic หมดอายุและอาจถูกเพิกถอนได้ สำหรับการตั้งค่าใหม่ ให้ใช้คีย์ Anthropic API แทน

ไม่พบคีย์ API สำหรับ provider "anthropic"

การยืนยันตัวตน Anthropic เป็นแบบ **ต่อเอเจนต์** — เอเจนต์ใหม่จะไม่สืบทอดคีย์ของเอเจนต์หลัก เรียกใช้การเริ่มต้นใช้งานอีกครั้งสำหรับเอเจนต์นั้น (หรือกำหนดค่าคีย์ API บนโฮสต์ Gateway) แล้วตรวจสอบด้วย `openclaw models status`

ไม่พบข้อมูลรับรองสำหรับโปรไฟล์ "anthropic:default"

เรียกใช้ `openclaw models status` เพื่อดูว่าโปรไฟล์การยืนยันตัวตนใดกำลังใช้งานอยู่ เรียกใช้การเริ่มต้นใช้งานอีกครั้ง หรือกำหนดค่าคีย์ API สำหรับเส้นทางโปรไฟล์นั้น

ไม่มีโปรไฟล์การยืนยันตัวตนที่พร้อมใช้งาน (ทั้งหมดอยู่ในคูลดาวน์)

ตรวจสอบ `openclaw models status --json` สำหรับ `auth.unusableProfiles` คูลดาวน์ของการจำกัดอัตรา Anthropic อาจกำหนดขอบเขตตามโมเดล ดังนั้นโมเดล Anthropic ข้างเคียงอาจยังใช้งานได้ เพิ่มโปรไฟล์ Anthropic อีกโปรไฟล์หนึ่งหรือรอให้คูลดาวน์สิ้นสุด

## ที่เกี่ยวข้อง

[**การเลือกโมเดล** การเลือกผู้ให้บริการ การอ้างอิงโมเดล และพฤติกรรมการสลับไปใช้ตัวสำรอง ](</th/concepts/model-providers>) [**แบ็กเอนด์ CLI** การตั้งค่าแบ็กเอนด์ Claude CLI และรายละเอียดรันไทม์ ](</th/gateway/cli-backends>) [**การแคชพรอมป์** วิธีการทำงานของการแคชพรอมป์ข้ามผู้ให้บริการ ](</th/reference/prompt-caching>) [**OAuth และการยืนยันตัวตน** รายละเอียดการยืนยันตัวตนและกฎการใช้ข้อมูลรับรองซ้ำ ](</th/gateway/authentication>)

Was this useful?YesNo