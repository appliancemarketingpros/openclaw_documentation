---
title: Vydra
source_url: https://docs.openclaw.ai/th/providers/vydra
scraped_at: 2026-05-25
---

Plugin Vydra ที่รวมมาให้เพิ่ม:

  * การสร้างรูปภาพผ่าน `vydra/grok-imagine`
  * การสร้างวิดีโอผ่าน `vydra/veo3` และ `vydra/kling`
  * การสังเคราะห์เสียงพูดผ่านเส้นทาง TTS ของ Vydra ที่ใช้ ElevenLabs เป็นเบื้องหลัง


OpenClaw ใช้ `VYDRA_API_KEY` เดียวกันสำหรับความสามารถทั้งสามอย่าง

คุณสมบัติ | ค่า  
---|---  
รหัสผู้ให้บริการ | `vydra`  
Plugin | รวมมาให้, `enabledByDefault: true`  
ตัวแปรสภาพแวดล้อมสำหรับการยืนยันตัวตน | `VYDRA_API_KEY`  
แฟล็กการเริ่มใช้งาน | `--auth-choice vydra-api-key`  
แฟล็ก CLI โดยตรง | `--vydra-api-key <key>`  
สัญญา | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
URL ฐาน | `https://www.vydra.ai/api/v1` (ใช้โฮสต์ `www`)  
  
## การตั้งค่า

* ### Run interactive onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

หรือตั้งค่าตัวแปรสภาพแวดล้อมโดยตรง:

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### Choose a default capability

เลือกความสามารถอย่างน้อยหนึ่งรายการด้านล่าง (รูปภาพ วิดีโอ หรือเสียงพูด) แล้วใช้การกำหนดค่าที่ตรงกัน

## ความสามารถ

Image generation

โมเดลรูปภาพเริ่มต้น:

  * `vydra/grok-imagine`


ตั้งค่าให้เป็นผู้ให้บริการรูปภาพเริ่มต้น:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

การรองรับที่รวมมาให้ในปัจจุบันมีเฉพาะ text-to-image เท่านั้น เส้นทางแก้ไขที่โฮสต์โดย Vydra คาดหวัง URL รูปภาพระยะไกล และ OpenClaw ยังไม่ได้เพิ่มบริดจ์อัปโหลดเฉพาะ Vydra ใน Plugin ที่รวมมาให้

Video generation

โมเดลวิดีโอที่ลงทะเบียนไว้:

  * `vydra/veo3` สำหรับ text-to-video
  * `vydra/kling` สำหรับ image-to-video


ตั้งค่า Vydra ให้เป็นผู้ให้บริการวิดีโอเริ่มต้น:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

หมายเหตุ:

  * `vydra/veo3` รวมมาให้เป็น text-to-video เท่านั้น
  * `vydra/kling` ปัจจุบันต้องใช้การอ้างอิง URL รูปภาพระยะไกล การอัปโหลดไฟล์ในเครื่องจะถูกปฏิเสธตั้งแต่ต้น
  * เส้นทาง HTTP `kling` ปัจจุบันของ Vydra มีความไม่สม่ำเสมอว่าต้องใช้ `image_url` หรือ `video_url`; ผู้ให้บริการที่รวมมาให้จึงแมป URL รูปภาพระยะไกลเดียวกันลงในทั้งสองฟิลด์
  * Plugin ที่รวมมาให้ยังคงใช้แนวทางระมัดระวังและไม่ส่งต่อปุ่มปรับแต่งสไตล์ที่ไม่ได้จัดทำเอกสาร เช่น อัตราส่วนภาพ ความละเอียด ลายน้ำ หรือเสียงที่สร้างขึ้น

Video live tests

การครอบคลุมการทดสอบสดเฉพาะผู้ให้บริการ:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

ไฟล์สดของ Vydra ที่รวมมาให้ตอนนี้ครอบคลุม:

  * `vydra/veo3` text-to-video
  * `vydra/kling` image-to-video โดยใช้ URL รูปภาพระยะไกล


แทนที่ fixture รูปภาพระยะไกลเมื่อจำเป็น:

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

Speech synthesis

ตั้งค่า Vydra ให้เป็นผู้ให้บริการเสียงพูด:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          voiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

ค่าเริ่มต้น:

  * โมเดล: `elevenlabs/tts`
  * รหัสเสียง: `21m00Tcm4TlvDq8ikWAM`


Plugin ที่รวมมาให้ปัจจุบันเปิดเผยเสียงเริ่มต้นหนึ่งรายการที่ทราบว่าใช้งานได้ดี และส่งคืนไฟล์เสียง MP3

## ที่เกี่ยวข้อง

[**Provider directory** เรียกดูผู้ให้บริการทั้งหมดที่มี ](</th/providers>) [**Image generation** พารามิเตอร์เครื่องมือรูปภาพที่ใช้ร่วมกันและการเลือกผู้ให้บริการ ](</th/tools/image-generation>) [**Video generation** พารามิเตอร์เครื่องมือวิดีโอที่ใช้ร่วมกันและการเลือกผู้ให้บริการ ](</th/tools/video-generation>) [**Configuration reference** ค่าเริ่มต้นของ Agent และการกำหนดค่าโมเดล ](</th/gateway/config-agents#agent-defaults>)

Was this useful?YesNo