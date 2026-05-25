---
title: Gradium
source_url: https://docs.openclaw.ai/th/providers/gradium
scraped_at: 2026-05-25
---

[Gradium](<https://gradium.ai>) เป็นผู้ให้บริการแปลงข้อความเป็นเสียงที่มาพร้อมกับ OpenClaw Plugin นี้สามารถสร้างการตอบกลับเสียงปกติ (WAV), เอาต์พุต Opus ที่เข้ากันได้กับบันทึกเสียง และเสียง u-law 8 kHz สำหรับพื้นผิวโทรศัพท์ได้

คุณสมบัติ | ค่า  
---|---  
รหัสผู้ให้บริการ | `gradium`  
การยืนยันตัวตน | `GRADIUM_API_KEY` หรือ config `apiKey`  
URL ฐาน | `https://api.gradium.ai` (ค่าเริ่มต้น)  
เสียงเริ่มต้น | `Emma` (`YTpq7expH9539ERJ`)  
  
## การตั้งค่า

สร้างคีย์ Gradium API จากนั้นส่งให้ OpenClaw ใช้งานด้วย env var หรือคีย์ config อย่างใดอย่างหนึ่ง

### Env var

bashCopy code
[code]
    export GRADIUM_API_KEY="gsk_..."
[/code]

### คีย์ Config

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          apiKey: "${GRADIUM_API_KEY}",        },      },    },  },}
[/code]

Plugin จะตรวจสอบ `apiKey` ที่ resolve แล้วก่อน และ fallback ไปใช้ตัวแปรสภาพแวดล้อม `GRADIUM_API_KEY`

## Config

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          voiceId: "YTpq7expH9539ERJ",          // apiKey: "${GRADIUM_API_KEY}",          // baseUrl: "https://api.gradium.ai",        },      },    },  },}
[/code]

คีย์ | ประเภท | คำอธิบาย  
---|---|---  
`messages.tts.providers.gradium.apiKey` | string | คีย์ API ที่ resolve แล้ว รองรับ `${ENV}` และ secret refs  
`messages.tts.providers.gradium.baseUrl` | string | แทนที่ origin ของ API เครื่องหมายทับท้ายสุดจะถูกตัดออก ค่าเริ่มต้นคือ `https://api.gradium.ai`  
`messages.tts.providers.gradium.voiceId` | string | รหัสเสียงเริ่มต้นที่ใช้เมื่อไม่มี directive override  
  
รูปแบบเสียงเอาต์พุตจะถูกเลือกโดยอัตโนมัติโดย runtime ตามพื้นผิวเป้าหมาย และไม่สามารถกำหนดค่าจาก `openclaw.json` ได้ ดู เอาต์พุต ด้านล่าง

## เสียง

ชื่อ | รหัสเสียง  
---|---  
Emma | `YTpq7expH9539ERJ`  
Kent | `LFZvm12tW_z0xfGo`  
Tiffany | `Eu9iL_CYe8N-Gkx_`  
Christina | `2H4HY2CBNyJHBCrP`  
Sydney | `jtEKaLYNn6iif5PR`  
John | `KWJiFWu2O9nMPYcR`  
Arthur | `3jUdJyOi9pgbxBTK`  
  
เสียงเริ่มต้น: Emma

### การ override เสียงต่อข้อความ

เมื่อนโยบายเสียงพูดที่ใช้งานอยู่อนุญาตให้ override เสียงได้ คุณสามารถสลับเสียงแบบ inline ด้วยโทเคน directive ได้ รายการทั้งหมดนี้ resolve เป็น override `voiceId` เดียวกัน:

textCopy code
[code]
    /voice:LFZvm12tW_z0xfGo/voice_id:LFZvm12tW_z0xfGo/voiceid:LFZvm12tW_z0xfGo/gradium_voice:LFZvm12tW_z0xfGo/gradiumvoice:LFZvm12tW_z0xfGo
[/code]

หากนโยบายเสียงพูดปิดใช้งานการ override เสียง directive จะถูกใช้แต่ถูกละเว้น

## เอาต์พุต

runtime จะเลือกรูปแบบเอาต์พุตจากพื้นผิวเป้าหมาย ปัจจุบันผู้ให้บริการไม่ได้สังเคราะห์รูปแบบอื่น

เป้าหมาย | รูปแบบ | นามสกุลไฟล์ | อัตราสุ่มตัวอย่าง | แฟล็กที่เข้ากันได้กับเสียง  
---|---|---|---|---  
เสียงมาตรฐาน | `wav` | `.wav` | ผู้ให้บริการ | ไม่  
บันทึกเสียง | `opus` | `.opus` | ผู้ให้บริการ | ใช่  
โทรศัพท์ | `ulaw_8000` | n/a | 8 kHz | n/a  
  
## ลำดับการเลือกอัตโนมัติ

ในบรรดาผู้ให้บริการ TTS ที่กำหนดค่าไว้ ลำดับการเลือกอัตโนมัติของ Gradium คือ `30` ดู [การแปลงข้อความเป็นเสียง](</th/tools/tts>) สำหรับวิธีที่ OpenClaw เลือกผู้ให้บริการที่ใช้งานอยู่เมื่อไม่ได้ pin `messages.tts.provider`

## ที่เกี่ยวข้อง

  * [การแปลงข้อความเป็นเสียง](</th/tools/tts>)
  * [ภาพรวมสื่อ](</th/tools/media-overview>)


Was this useful?YesNo