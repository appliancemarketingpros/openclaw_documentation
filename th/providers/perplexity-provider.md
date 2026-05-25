---
title: Perplexity
source_url: https://docs.openclaw.ai/th/providers/perplexity-provider
scraped_at: 2026-05-25
---

Plugin Perplexity มอบความสามารถในการค้นหาเว็บผ่าน Perplexity Search API หรือ Perplexity Sonar ผ่าน OpenRouter

คุณสมบัติ | ค่า  
---|---  
ประเภท | ผู้ให้บริการค้นหาเว็บ (ไม่ใช่ผู้ให้บริการโมเดล)  
การยืนยันตัวตน | `PERPLEXITY_API_KEY` (โดยตรง) หรือ `OPENROUTER_API_KEY` (ผ่าน OpenRouter)  
พาธการกำหนดค่า | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## เริ่มต้นใช้งาน

* ### ตั้งค่าคีย์ API

เรียกใช้โฟลว์การกำหนดค่าการค้นหาเว็บแบบโต้ตอบ:

bashCopy code
[code]
    openclaw configure --section web
[/code]

หรือตั้งค่าคีย์โดยตรง:

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### เริ่มค้นหา

เอเจนต์จะใช้ Perplexity สำหรับการค้นหาเว็บโดยอัตโนมัติเมื่อกำหนดค่าคีย์แล้ว ไม่จำเป็นต้องมีขั้นตอนเพิ่มเติม

## โหมดการค้นหา

Plugin จะเลือกกลไกการรับส่งข้อมูลโดยอัตโนมัติตามคำนำหน้าคีย์ API:

### Perplexity API แบบเนทีฟ (pplx-)

เมื่อคีย์ของคุณขึ้นต้นด้วย `pplx-` OpenClaw จะใช้ Perplexity Search API แบบเนทีฟ กลไกการรับส่งข้อมูลนี้ส่งคืนผลลัพธ์แบบมีโครงสร้าง และรองรับตัวกรองโดเมน ภาษา และวันที่ (ดูตัวเลือกการกรองด้านล่าง)

### OpenRouter / Sonar (sk-or-)

เมื่อคีย์ของคุณขึ้นต้นด้วย `sk-or-` OpenClaw จะกำหนดเส้นทางผ่าน OpenRouter โดยใช้ โมเดล Perplexity Sonar กลไกการรับส่งข้อมูลนี้ส่งคืนคำตอบที่ AI สังเคราะห์พร้อม การอ้างอิง

คำนำหน้าคีย์ | กลไกการรับส่งข้อมูล | ความสามารถ  
---|---|---  
`pplx-` | Perplexity Search API แบบเนทีฟ | ผลลัพธ์แบบมีโครงสร้าง, ตัวกรองโดเมน/ภาษา/วันที่  
`sk-or-` | OpenRouter (Sonar) | คำตอบที่ AI สังเคราะห์พร้อมการอ้างอิง  
  
## การกรองของ API แบบเนทีฟ

เมื่อใช้ Perplexity API แบบเนทีฟ การค้นหารองรับตัวกรองต่อไปนี้:

ตัวกรอง | คำอธิบาย | ตัวอย่าง  
---|---|---  
ประเทศ | รหัสประเทศ 2 ตัวอักษร | `us`, `de`, `jp`  
ภาษา | รหัสภาษา ISO 639-1 | `en`, `fr`, `zh`  
ช่วงวันที่ | กรอบเวลาความใหม่ | `day`, `week`, `month`, `year`  
ตัวกรองโดเมน | รายการอนุญาตหรือรายการปฏิเสธ (สูงสุด 20 โดเมน) | `example.com`  
งบประมาณเนื้อหา | ขีดจำกัดโทเค็นต่อคำตอบ / ต่อหน้า | `max_tokens`, `max_tokens_per_page`  
  
## การกำหนดค่าขั้นสูง

ตัวแปรสภาพแวดล้อมสำหรับกระบวนการเดมอน

หาก OpenClaw Gateway ทำงานเป็นเดมอน (launchd/systemd) โปรดตรวจสอบให้แน่ใจว่า `PERPLEXITY_API_KEY` พร้อมใช้งานสำหรับกระบวนการนั้น

การตั้งค่าพร็อกซี OpenRouter

หากคุณต้องการกำหนดเส้นทางการค้นหา Perplexity ผ่าน OpenRouter ให้ตั้งค่า `OPENROUTER_API_KEY` (คำนำหน้า `sk-or-`) แทนคีย์ Perplexity แบบเนทีฟ OpenClaw จะตรวจจับคำนำหน้าและสลับไปใช้กลไกการรับส่งข้อมูล Sonar โดยอัตโนมัติ

## ที่เกี่ยวข้อง

[**เครื่องมือค้นหา Perplexity** วิธีที่เอเจนต์เรียกใช้การค้นหา Perplexity และตีความผลลัพธ์ ](</th/tools/perplexity-search>) [**ข้อมูลอ้างอิงการกำหนดค่า** ข้อมูลอ้างอิงการกำหนดค่าฉบับเต็ม รวมถึงรายการ Plugin ](</th/gateway/configuration-reference>)

Was this useful?YesNo