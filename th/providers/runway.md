---
title: รันเวย์
source_url: https://docs.openclaw.ai/th/providers/runway
scraped_at: 2026-05-25
---

OpenClaw มาพร้อมกับผู้ให้บริการ `runway` ที่บันเดิลไว้สำหรับการสร้างวิดีโอแบบโฮสต์ Plugin นี้เปิดใช้งานโดยค่าเริ่มต้นและลงทะเบียนผู้ให้บริการ `runway` กับสัญญา `videoGenerationProviders`

คุณสมบัติ | ค่า  
---|---  
รหัสผู้ให้บริการ | `runway`  
Plugin | บันเดิลไว้, `enabledByDefault: true`  
ตัวแปรสภาพแวดล้อมสำหรับการยืนยันตัวตน | `RUNWAYML_API_SECRET` (มาตรฐาน) หรือ `RUNWAY_API_KEY`  
แฟล็กการเริ่มต้นใช้งาน | `--auth-choice runway-api-key`  
แฟล็ก CLI โดยตรง | `--runway-api-key <key>`  
API | การสร้างวิดีโอของ Runway แบบอิงงาน (`GET /v1/tasks/{id}` polling)  
โมเดลเริ่มต้น | `runway/gen4.5`  
  
## เริ่มต้นใช้งาน

* ### ตั้งค่าคีย์ API

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### ตั้งค่า Runway เป็นผู้ให้บริการวิดีโอเริ่มต้น

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### สร้างวิดีโอ

ขอให้เอเจนต์สร้างวิดีโอ Runway จะถูกใช้โดยอัตโนมัติ

## โหมดและโมเดลที่รองรับ

ผู้ให้บริการนี้เปิดเผยโมเดล Runway เจ็ดโมเดลที่แบ่งออกเป็นสามโหมด รหัสโมเดลเดียวกันสามารถใช้ได้มากกว่าหนึ่งโหมด (เช่น `gen4.5` ใช้ได้ทั้งข้อความเป็นวิดีโอและรูปภาพเป็นวิดีโอ)

โหมด | โมเดล | อินพุตอ้างอิง  
---|---|---  
ข้อความเป็นวิดีโอ | `gen4.5` (ค่าเริ่มต้น), `veo3.1`, `veo3.1_fast`, `veo3` | ไม่มี  
รูปภาพเป็นวิดีโอ | `gen4.5`, `gen4_turbo`, `gen3a_turbo`, `veo3.1`, `veo3.1_fast`, `veo3` | รูปภาพในเครื่องหรือระยะไกล 1 รูป  
วิดีโอเป็นวิดีโอ | `gen4_aleph` | วิดีโอในเครื่องหรือระยะไกล 1 รายการ  
  
รองรับการอ้างอิงรูปภาพและวิดีโอในเครื่องผ่าน data URI

อัตราส่วนภาพ | ค่าที่อนุญาต  
---|---  
ข้อความเป็นวิดีโอ | `16:9`, `9:16`  
การแก้ไขรูปภาพและวิดีโอ | `1:1`, `16:9`, `9:16`, `3:4`, `4:3`, `21:9`  
  
## การกำหนดค่า

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## การกำหนดค่าขั้นสูง

นามแฝงของตัวแปรสภาพแวดล้อม

OpenClaw รู้จักทั้ง `RUNWAYML_API_SECRET` (มาตรฐาน) และ `RUNWAY_API_KEY` ตัวแปรใดตัวแปรหนึ่งสามารถใช้ยืนยันตัวตนกับผู้ให้บริการ Runway ได้

การ polling งาน

Runway ใช้ API แบบอิงงาน หลังจากส่งคำขอสร้างแล้ว OpenClaw จะ poll `GET /v1/tasks/{id}` จนกว่าวิดีโอจะพร้อม ไม่จำเป็นต้องมี การกำหนดค่าเพิ่มเติมสำหรับพฤติกรรมการ polling

## ที่เกี่ยวข้อง

[**การสร้างวิดีโอ** พารามิเตอร์เครื่องมือร่วม การเลือกผู้ให้บริการ และพฤติกรรมแบบ async ](</th/tools/video-generation>) [**ข้อมูลอ้างอิงการกำหนดค่า** การตั้งค่าเริ่มต้นของเอเจนต์ รวมถึงโมเดลการสร้างวิดีโอ ](</th/gateway/config-agents#agent-defaults>)

Was this useful?YesNo