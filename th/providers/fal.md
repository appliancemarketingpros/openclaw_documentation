---
title: Fal
source_url: https://docs.openclaw.ai/th/providers/fal
scraped_at: 2026-05-25
---

OpenClaw มาพร้อมกับผู้ให้บริการ `fal` ที่บันเดิลมาให้สำหรับการสร้างรูปภาพและวิดีโอแบบโฮสต์

คุณสมบัติ | ค่า  
---|---  
ผู้ให้บริการ | `fal`  
การยืนยันตัวตน | `FAL_KEY` (ค่าหลัก; `FAL_API_KEY` ใช้เป็น fallback ได้เช่นกัน)  
API | endpoint โมเดล fal  
  
## เริ่มต้นใช้งาน

* ### ตั้งค่า API key

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### ตั้งค่าโมเดลรูปภาพเริ่มต้น

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## การสร้างรูปภาพ

ผู้ให้บริการสร้างรูปภาพ `fal` ที่บันเดิลมาให้จะใช้ค่าเริ่มต้นเป็น `fal/fal-ai/flux/dev`

ความสามารถ | ค่า  
---|---  
จำนวนรูปภาพสูงสุด | 4 ต่อคำขอ  
โหมดแก้ไข | Flux: รูปภาพอ้างอิง 1 รูป; GPT Image 2: 10; Nano Banana 2: 14  
การแทนที่ขนาด | รองรับ  
อัตราส่วนภาพ | รองรับสำหรับ generate และการแก้ไข GPT Image 2/Nano Banana 2  
ความละเอียด | รองรับ  
รูปแบบเอาต์พุต | `png` หรือ `jpeg`  
  
ใช้ `outputFormat: "png"` เมื่อต้องการเอาต์พุต PNG fal ไม่ประกาศการควบคุมพื้นหลังโปร่งใสแบบชัดเจนใน OpenClaw ดังนั้น `background: "transparent"` จะถูกรายงานเป็นการแทนที่ที่ถูกละเว้นสำหรับโมเดล fal

หากต้องการใช้ fal เป็นผู้ให้บริการรูปภาพเริ่มต้น:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## การสร้างวิดีโอ

ผู้ให้บริการสร้างวิดีโอ `fal` ที่บันเดิลมาให้จะใช้ค่าเริ่มต้นเป็น `fal/fal-ai/minimax/video-01-live`

ความสามารถ | ค่า  
---|---  
โหมด | ข้อความเป็นวิดีโอ, การอ้างอิงรูปภาพเดียว, Seedance reference-to-video  
รันไทม์ | โฟลว์ submit/status/result ที่มีคิวรองรับสำหรับงานที่ใช้เวลานาน  
  
โมเดลวิดีโอที่มีให้ใช้

**HeyGen video-agent:**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0:**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

ตัวอย่างการกำหนดค่า Seedance 2.0 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

ตัวอย่างการกำหนดค่า Seedance 2.0 reference-to-video json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

Reference-to-video รองรับรูปภาพสูงสุด 9 รูป, วิดีโอ 3 รายการ และข้อมูลอ้างอิงเสียง 3 รายการ ผ่านพารามิเตอร์ `video_generate` ที่ใช้ร่วมกัน ได้แก่ `images`, `videos` และ `audioRefs` โดยมีไฟล์อ้างอิงรวมสูงสุด 12 ไฟล์

ตัวอย่างการกำหนดค่า HeyGen video-agent json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## ที่เกี่ยวข้อง

[**การสร้างรูปภาพ** พารามิเตอร์เครื่องมือรูปภาพที่ใช้ร่วมกันและการเลือกผู้ให้บริการ ](</th/tools/image-generation>) [**การสร้างวิดีโอ** พารามิเตอร์เครื่องมือวิดีโอที่ใช้ร่วมกันและการเลือกผู้ให้บริการ ](</th/tools/video-generation>) [**ข้อมูลอ้างอิงการกำหนดค่า** ค่าเริ่มต้นของ agent รวมถึงการเลือกโมเดลรูปภาพและวิดีโอ ](</th/gateway/config-agents#agent-defaults>)

Was this useful?YesNo