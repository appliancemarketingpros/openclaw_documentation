---
title: Cloudflare AI Gateway
source_url: https://docs.openclaw.ai/th/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

Cloudflare AI Gateway อยู่หน้า API ของผู้ให้บริการ และช่วยให้คุณเพิ่มการวิเคราะห์ แคช และการควบคุมได้ สำหรับ Anthropic นั้น OpenClaw ใช้ Anthropic Messages API ผ่านปลายทาง Gateway ของคุณ

คุณสมบัติ | ค่า  
---|---  
ผู้ให้บริการ | `cloudflare-ai-gateway`  
URL ฐาน | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
โมเดลเริ่มต้น | `cloudflare-ai-gateway/claude-sonnet-4-6`  
คีย์ API | `CLOUDFLARE_AI_GATEWAY_API_KEY` (คีย์ API ของผู้ให้บริการสำหรับคำขอผ่าน Gateway)  
  
เมื่อเปิดใช้การคิดสำหรับโมเดล Anthropic Messages แล้ว OpenClaw จะตัดเทิร์นพรีฟิลของ assistant ที่ต่อท้ายออกก่อนส่ง payload ผ่าน Cloudflare AI Gateway Anthropic ปฏิเสธการพรีฟิลการตอบกลับเมื่อใช้ extended thinking ขณะที่การพรีฟิล แบบไม่คิดตามปกติยังคงใช้ได้

## เริ่มต้นใช้งาน

* ### ตั้งค่าคีย์ API ของผู้ให้บริการและรายละเอียด Gateway

เรียกใช้ onboarding แล้วเลือกตัวเลือกการยืนยันตัวตน Cloudflare AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

ระบบจะแจ้งให้ป้อน ID บัญชี, ID gateway และคีย์ API ของคุณ

* ### ตั้งค่าโมเดลเริ่มต้น

เพิ่มโมเดลในคอนฟิก OpenClaw ของคุณ:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### ตรวจสอบว่าโมเดลพร้อมใช้งาน

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## ตัวอย่างแบบไม่โต้ตอบ

สำหรับการตั้งค่าแบบสคริปต์หรือ CI ให้ส่งค่าทั้งหมดผ่านบรรทัดคำสั่ง:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## การกำหนดค่าขั้นสูง

Gateway ที่ยืนยันตัวตนแล้ว

หากคุณเปิดใช้การยืนยันตัวตน Gateway ใน Cloudflare ให้เพิ่มส่วนหัว `cf-aig-authorization` ซึ่งเป็นสิ่งที่ต้องใช้ **เพิ่มเติมจาก** คีย์ API ของผู้ให้บริการของคุณ

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

หมายเหตุเกี่ยวกับสภาพแวดล้อม

หาก Gateway ทำงานเป็น daemon (launchd/systemd) ให้ตรวจสอบว่า `CLOUDFLARE_AI_GATEWAY_API_KEY` พร้อมใช้งานสำหรับโปรเซสนั้น

## ที่เกี่ยวข้อง

[**การเลือกโมเดล** การเลือกผู้ให้บริการ, model refs และพฤติกรรม failover ](</th/concepts/model-providers>) [**การแก้ไขปัญหา** การแก้ไขปัญหาทั่วไปและ FAQ ](</th/help/troubleshooting>)

Was this useful?YesNo