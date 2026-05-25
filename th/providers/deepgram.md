---
title: Deepgram
source_url: https://docs.openclaw.ai/th/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram เป็น API สำหรับแปลงเสียงเป็นข้อความ ใน OpenClaw จะใช้สำหรับการถอดเสียงไฟล์เสียง/ข้อความเสียงขาเข้าผ่าน `tools.media.audio` และสำหรับ STT แบบสตรีมมิงของ Voice Call ผ่าน `plugins.entries.voice-call.config.streaming`

สำหรับการถอดเสียงแบบแบตช์ OpenClaw จะอัปโหลดไฟล์เสียงทั้งไฟล์ไปยัง Deepgram และแทรกข้อความถอดเสียงเข้าไปในไปป์ไลน์การตอบกลับ (`{{Transcript}}` \+ บล็อก `[Audio]`) สำหรับ Voice Call แบบสตรีมมิง OpenClaw จะส่งต่อเฟรม G.711 u-law แบบสดผ่าน WebSocket `listen` endpoint ของ Deepgram และส่งข้อความถอดเสียงแบบบางส่วนหรือแบบสมบูรณ์เมื่อ Deepgram ส่งกลับมา

รายละเอียด | ค่า  
---|---  
เว็บไซต์ | [deepgram.com](<https://deepgram.com>)  
เอกสาร | [developers.deepgram.com](<https://developers.deepgram.com>)  
การยืนยันตัวตน | `DEEPGRAM_API_KEY`  
โมเดลเริ่มต้น | `nova-3`  
  
## เริ่มต้นใช้งาน

* ### ตั้งค่า API key ของคุณ

เพิ่ม Deepgram API key ของคุณลงใน environment:

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### เปิดใช้งานผู้ให้บริการเสียง

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### ส่งข้อความเสียง

ส่งข้อความเสียงผ่านช่องทางที่เชื่อมต่ออยู่ช่องทางใดก็ได้ OpenClaw จะถอดเสียงผ่าน Deepgram และแทรกข้อความถอดเสียงเข้าไปในไปป์ไลน์การตอบกลับ

## ตัวเลือกการกำหนดค่า

ตัวเลือก | พาธ | คำอธิบาย  
---|---|---  
`model` | `tools.media.audio.models[].model` | รหัสโมเดลของ Deepgram (ค่าเริ่มต้น: `nova-3`)  
`language` | `tools.media.audio.models[].language` | คำใบ้ภาษา (ไม่บังคับ)  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | เปิดใช้การตรวจจับภาษา (ไม่บังคับ)  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | เปิดใช้เครื่องหมายวรรคตอน (ไม่บังคับ)  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | เปิดใช้การจัดรูปแบบอัจฉริยะ (ไม่บังคับ)  
  
### พร้อมคำใบ้ภาษา

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### พร้อมตัวเลือกของ Deepgram

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## STT แบบสตรีมมิงของ Voice Call

Plugin `deepgram` ที่มาพร้อมกันยังลงทะเบียนผู้ให้บริการถอดเสียงแบบเรียลไทม์สำหรับ Plugin Voice Call ด้วย

การตั้งค่า | พาธการกำหนดค่า | ค่าเริ่มต้น  
---|---|---  
API key | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | ใช้ `DEEPGRAM_API_KEY` เป็นค่าตกทอด  
โมเดล | `...deepgram.model` | `nova-3`  
ภาษา | `...deepgram.language` | (ไม่ได้ตั้งค่า)  
Encoding | `...deepgram.encoding` | `mulaw`  
อัตราสุ่มตัวอย่าง | `...deepgram.sampleRate` | `8000`  
Endpointing | `...deepgram.endpointingMs` | `800`  
ผลลัพธ์ระหว่างทาง | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## หมายเหตุ

การยืนยันตัวตน

การยืนยันตัวตนเป็นไปตามลำดับการยืนยันตัวตนมาตรฐานของผู้ให้บริการ `DEEPGRAM_API_KEY` เป็นวิธีที่ง่ายที่สุด

พร็อกซีและ endpoint แบบกำหนดเอง

แทนที่ endpoint หรือ header ได้ด้วย `tools.media.audio.baseUrl` และ `tools.media.audio.headers` เมื่อใช้งานผ่านพร็อกซี

ลักษณะการแสดงผลลัพธ์

ผลลัพธ์เป็นไปตามกฎเสียงเดียวกันกับผู้ให้บริการรายอื่น (ขีดจำกัดขนาด, การหมดเวลา, การแทรกข้อความถอดเสียง)

## ที่เกี่ยวข้อง

[**เครื่องมือสื่อ** ภาพรวมไปป์ไลน์การประมวลผลเสียง รูปภาพ และวิดีโอ ](</th/tools/media-overview>) [**การกำหนดค่า** เอกสารอ้างอิงการกำหนดค่าแบบเต็ม รวมถึงการตั้งค่าเครื่องมือสื่อ ](</th/gateway/configuration>) [**การแก้ไขปัญหา** ปัญหาที่พบบ่อยและขั้นตอนการดีบัก ](</th/help/troubleshooting>) [**คำถามที่พบบ่อย** คำถามที่พบบ่อยเกี่ยวกับการตั้งค่า OpenClaw ](</th/help/faq>)

Was this useful?YesNo