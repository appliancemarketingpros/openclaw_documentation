---
title: Tavily
source_url: https://docs.openclaw.ai/th/tools/tavily
scraped_at: 2026-05-25
---

[Tavily](<https://tavily.com>) คือ API การค้นหาที่ออกแบบมาสำหรับแอปพลิเคชัน AI OpenClaw เปิดให้ใช้งานได้สองวิธี:

  * เป็นผู้ให้บริการ `web_search` สำหรับเครื่องมือค้นหาทั่วไป
  * เป็นเครื่องมือ Plugin แบบชัดเจน: `tavily_search` และ `tavily_extract`


Tavily ส่งคืนผลลัพธ์แบบมีโครงสร้างที่ปรับให้เหมาะสำหรับการใช้งานของ LLM พร้อมความลึกในการค้นหาที่กำหนดค่าได้ การกรองหัวข้อ ตัวกรองโดเมน สรุปคำตอบที่สร้างโดย AI และการดึงเนื้อหาจาก URL (รวมถึงหน้าที่เรนเดอร์ด้วย JavaScript)

คุณสมบัติ | ค่า  
---|---  
รหัส Plugin | `tavily`  
การยืนยันตัวตน | `TAVILY_API_KEY` หรือ config `apiKey`  
URL พื้นฐาน | `https://api.tavily.com` (ค่าเริ่มต้น)  
เครื่องมือที่รวมมา | `tavily_search`, `tavily_extract`  
  
## เริ่มต้นใช้งาน

* ### รับ API key

สร้างบัญชี Tavily ที่ [tavily.com](<https://tavily.com>) จากนั้นสร้าง API key ในแดชบอร์ด

* ### กำหนดค่า Plugin และผู้ให้บริการ

json5Copy code
[code]
    {  plugins: {    entries: {      tavily: {        enabled: true,        config: {          webSearch: {            apiKey: "tvly-...", // optional if TAVILY_API_KEY is set            baseUrl: "https://api.tavily.com",          },        },      },    },  },  tools: {    web: {      search: {        provider: "tavily",      },    },  },}
[/code]

* ### ตรวจสอบว่าการค้นหาทำงาน

เรียกใช้ `web_search` จาก agent ใดก็ได้ หรือเรียก `tavily_search` โดยตรง

## อ้างอิงเครื่องมือ

### `tavily_search`

ใช้เครื่องมือนี้เมื่อต้องการตัวควบคุมการค้นหาเฉพาะของ Tavily แทน `web_search` ทั่วไป

พารามิเตอร์ | ประเภท | ข้อจำกัด / ค่าเริ่มต้น | คำอธิบาย  
---|---|---|---  
`query` | string | จำเป็น | สตริงคำค้นหา ควรสั้นกว่า 400 อักขระ  
`search_depth` | enum | `basic` (ค่าเริ่มต้น), `advanced` | `advanced` ช้ากว่าแต่มีความเกี่ยวข้องสูงกว่า  
`topic` | enum | `general` (ค่าเริ่มต้น), `news`, `finance` | กรองตามกลุ่มหัวข้อ  
`max_results` | integer | 1-20 | จำนวนผลลัพธ์  
`include_answer` | boolean | ค่าเริ่มต้น `false` | รวมสรุปคำตอบที่สร้างโดย AI ของ Tavily  
`time_range` | enum | `day`, `week`, `month`, `year` | กรองผลลัพธ์ตามความใหม่  
`include_domains` | string array | (ไม่มี) | รวมเฉพาะผลลัพธ์จากโดเมนเหล่านี้  
`exclude_domains` | string array | (ไม่มี) | ยกเว้นผลลัพธ์จากโดเมนเหล่านี้  
  
ข้อแลกเปลี่ยนของความลึกในการค้นหา:

ความลึก | ความเร็ว | ความเกี่ยวข้อง | เหมาะสำหรับ  
---|---|---|---  
`basic` | เร็วกว่า | สูง | คำค้นหาใช้งานทั่วไป (ค่าเริ่มต้น)  
`advanced` | ช้ากว่า | สูงสุด | การวิจัยที่ต้องการความแม่นยำและการค้นหาข้อเท็จจริง  
  
### `tavily_extract`

ใช้เครื่องมือนี้เพื่อดึงเนื้อหาที่สะอาดจาก URL หนึ่งรายการหรือหลายรายการ รองรับหน้าที่เรนเดอร์ด้วย JavaScript และรองรับการแบ่งส่วนตามคำค้นหาเพื่อการดึงข้อมูลแบบเจาะจง

พารามิเตอร์ | ประเภท | ข้อจำกัด / ค่าเริ่มต้น | คำอธิบาย  
---|---|---|---  
`urls` | string array | จำเป็น, 1-20 | URL ที่ต้องการดึงเนื้อหา  
`query` | string | (ไม่บังคับ) | จัดอันดับส่วนที่ดึงมาใหม่ตามความเกี่ยวข้องกับคำค้นหานี้  
`extract_depth` | enum | `basic` (ค่าเริ่มต้น), `advanced` | ใช้ `advanced` สำหรับหน้าที่ใช้ JS หนัก, SPA หรือตารางแบบไดนามิก  
`chunks_per_source` | integer | 1-5; **ต้องมี`query`** | จำนวนส่วนที่ส่งคืนต่อ URL เกิดข้อผิดพลาดหากตั้งค่าโดยไม่มี `query`  
`include_images` | boolean | ค่าเริ่มต้น `false` | รวม URL รูปภาพในผลลัพธ์  
  
ข้อแลกเปลี่ยนของความลึกในการดึงข้อมูล:

ความลึก | ควรใช้เมื่อใด  
---|---  
`basic` | หน้าง่าย ๆ ลองใช้ตัวนี้ก่อน  
`advanced` | SPA ที่เรนเดอร์ด้วย JS, เนื้อหาแบบไดนามิก, ตาราง  
  
## การเลือกเครื่องมือที่เหมาะสม

ความต้องการ | เครื่องมือ  
---|---  
ค้นหาเว็บอย่างรวดเร็ว ไม่มีตัวเลือกพิเศษ | `web_search`  
ค้นหาพร้อมความลึก หัวข้อ คำตอบจาก AI | `tavily_search`  
ดึงเนื้อหาจาก URL ที่ระบุ | `tavily_extract`  
  
## การกำหนดค่าขั้นสูง

ลำดับการค้นหา API key

ไคลเอนต์ Tavily ค้นหา API key ตามลำดับนี้:

  1. `plugins.entries.tavily.config.webSearch.apiKey` (แก้ไขผ่าน SecretRefs)
  2. `TAVILY_API_KEY` จากสภาพแวดล้อม Gateway


`tavily_extract` จะแจ้งข้อผิดพลาดการตั้งค่าหากไม่มีทั้งสองรายการ

URL พื้นฐานแบบกำหนดเอง

แทนที่ `plugins.entries.tavily.config.webSearch.baseUrl` หากคุณส่ง Tavily ผ่านพร็อกซี ค่าเริ่มต้นคือ `https://api.tavily.com`

`chunks_per_source` ต้องมี `query`

`tavily_extract` ปฏิเสธการเรียกที่ส่ง `chunks_per_source` โดยไม่มี `query` Tavily จัดอันดับส่วนต่าง ๆ ตามความเกี่ยวข้องกับคำค้นหา ดังนั้นพารามิเตอร์นี้จึงไม่มีความหมายหากไม่มีคำค้นหา

## ที่เกี่ยวข้อง

[**ภาพรวมการค้นหาเว็บ** ผู้ให้บริการทั้งหมดและกฎการตรวจจับอัตโนมัติ ](</th/tools/web>) [**Firecrawl** การค้นหาพร้อมการสแครปและการดึงเนื้อหา ](</th/tools/firecrawl>) [**Exa Search** การค้นหาแบบ neural พร้อมการดึงเนื้อหา ](</th/tools/exa-search>) [**การกำหนดค่า** สคีมา config แบบเต็มสำหรับรายการ Plugin และการกำหนดเส้นทางเครื่องมือ ](</th/gateway/configuration>)

Was this useful?YesNo