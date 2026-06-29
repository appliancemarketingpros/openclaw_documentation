---
title: PixVerse
source_url: https://docs.openclaw.ai/th/providers/pixverse
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw มี `pixverse` เป็น Plugin ภายนอกอย่างเป็นทางการสำหรับการสร้างวิดีโอ PixVerse แบบโฮสต์ Plugin นี้ลงทะเบียนผู้ให้บริการ `pixverse` กับคอนแทรกต์ `videoGenerationProviders`

คุณสมบัติ | ค่า  
---|---  
รหัสผู้ให้บริการ | `pixverse`  
แพ็กเกจ Plugin | `@openclaw/pixverse-provider`  
ตัวแปรสภาพแวดล้อมสำหรับการยืนยันตัวตน | `PIXVERSE_API_KEY`  
แฟล็กการตั้งค่าเริ่มต้น | `--auth-choice pixverse-api-key`  
แฟล็ก CLI โดยตรง | `--pixverse-api-key <key>`  
API | PixVerse Platform API v2 (การส่ง `video_id` พร้อมการโพลผลลัพธ์)  
โมเดลเริ่มต้น | `pixverse/v6`  
ภูมิภาค API เริ่มต้น | สากล  
  
## เริ่มต้นใช้งาน

* ### ติดตั้ง Plugin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/pixverse-provideropenclaw gateway restart
[/code]

* ### ตั้งค่า API key

bashCopy code
[code]
    openclaw onboard --auth-choice pixverse-api-key
[/code]

ตัวช่วยตั้งค่าจะถามว่าจะใช้เอนด์พอยต์สากล (`https://app-api.pixverse.ai/openapi/v2`) หรือเอนด์พอยต์ CN (`https://app-api.pixverseai.cn/openapi/v2`) ก่อนเขียน `region` และ `baseUrl` ลงในการกำหนดค่าผู้ให้บริการ

* ### ตั้งค่า PixVerse เป็นผู้ให้บริการวิดีโอเริ่มต้น

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "pixverse/v6"
[/code]

* ### สร้างวิดีโอ

ขอให้เอเจนต์สร้างวิดีโอ ระบบจะใช้ PixVerse โดยอัตโนมัติ

## โหมดและโมเดลที่รองรับ

ผู้ให้บริการเปิดเผยโมเดลการสร้างของ PixVerse ผ่านเครื่องมือวิดีโอที่ใช้ร่วมกันของ OpenClaw

โหมด | โมเดล | อินพุตอ้างอิง  
---|---|---  
ข้อความเป็นวิดีโอ | `v6` (ค่าเริ่มต้น), `c1` | ไม่มี  
รูปภาพเป็นวิดีโอ | `v6` (ค่าเริ่มต้น), `c1` | รูปภาพภายในเครื่องหรือระยะไกล 1 รูป  
  
การอ้างอิงรูปภาพภายในเครื่องจะถูกอัปโหลดไปยัง PixVerse ก่อนคำขอรูปภาพเป็นวิดีโอ URL รูปภาพระยะไกลจะถูกส่งผ่านเอนด์พอยต์อัปโหลดรูปภาพของ PixVerse เป็น `image_url`

ตัวเลือก | ค่าที่รองรับ  
---|---  
ระยะเวลา | 1-15 วินาที  
ความละเอียด | `360P`, `540P`, `720P`, `1080P`  
อัตราส่วนภาพ | `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `2:3`, `3:2`, `21:9` สำหรับข้อความเป็นวิดีโอ  
เสียงที่สร้างขึ้น | `audio: true`  
  
## ตัวเลือกผู้ให้บริการ

ผู้ให้บริการวิดีโอยอมรับคีย์เฉพาะผู้ให้บริการที่เป็นทางเลือกเหล่านี้:

ตัวเลือก | ชนิด | ผลลัพธ์  
---|---|---  
`seed` | number | seed แบบกำหนดแน่นอนเมื่อรองรับ  
`negativePrompt` / `negative_prompt` | string | พรอมป์ต์เชิงลบ  
`quality` | string | คุณภาพของ PixVerse เช่น `720p`  
`motionMode` / `motion_mode` | string | โหมดการเคลื่อนไหวสำหรับรูปภาพเป็นวิดีโอ  
`cameraMovement` / `camera_movement` | string | ค่าที่ตั้งไว้ล่วงหน้าสำหรับการเคลื่อนกล้องของ PixVerse  
`templateId` / `template_id` | number | รหัสเทมเพลต PixVerse ที่เปิดใช้งาน  
  
## การกำหนดค่า

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "pixverse/v6",      },    },  },}
[/code]

## การกำหนดค่าขั้นสูง

ภูมิภาค API

OpenClaw ใช้ PixVerse API สากลเป็นค่าเริ่มต้น ตั้งค่า `models.providers.pixverse.region` ด้วยตนเองเมื่อคีย์ของคุณเป็นของภูมิภาคแพลตฟอร์ม PixVerse เฉพาะ หรือใช้ `openclaw onboard --auth-choice pixverse-api-key` เพื่อเลือกหนึ่งรายการในตัวช่วยตั้งค่า:

ค่าภูมิภาค | URL ฐานของ PixVerse API  
---|---  
`international` | `https://app-api.pixverse.ai/openapi/v2`  
`cn` | `https://app-api.pixverseai.cn/openapi/v2`  
  
json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        region: "cn", // "international" or "cn"        baseUrl: "https://app-api.pixverseai.cn/openapi/v2",        models: [],      },    },  },}
[/code]

URL ฐานแบบกำหนดเอง

ตั้งค่า `models.providers.pixverse.baseUrl` เฉพาะเมื่อกำหนดเส้นทางผ่านพร็อกซีที่เข้ากันได้และเชื่อถือได้ `baseUrl` มีลำดับความสำคัญเหนือ `region`

json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        baseUrl: "https://app-api.pixverse.ai/openapi/v2",      },    },  },}
[/code]

การโพล Task

PixVerse ส่งคืน `video_id` จากคำขอสร้าง OpenClaw จะโพล `/openapi/v2/video/result/{video_id}` จนกว่า Task จะสำเร็จ ล้มเหลว หรือหมดเวลา

## ที่เกี่ยวข้อง

[**การสร้างวิดีโอ** พารามิเตอร์เครื่องมือที่ใช้ร่วมกัน การเลือกผู้ให้บริการ และพฤติกรรมแบบอะซิงโครนัส ](</th/tools/video-generation>) [**ข้อมูลอ้างอิงการกำหนดค่า** การตั้งค่าเริ่มต้นของเอเจนต์ รวมถึงโมเดลการสร้างวิดีโอ ](</th/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue