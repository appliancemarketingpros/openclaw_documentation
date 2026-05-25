---
title: การค้นหาด้วย DuckDuckGo
source_url: https://docs.openclaw.ai/th/tools/duckduckgo-search
scraped_at: 2026-05-25
---

OpenClaw รองรับ DuckDuckGo เป็นผู้ให้บริการ `web_search` แบบ **ไม่ต้องใช้คีย์** ไม่จำเป็นต้องมีคีย์ API หรือบัญชี

## การตั้งค่า

ไม่ต้องใช้คีย์ API - เพียงตั้งค่า DuckDuckGo เป็นผู้ให้บริการของคุณ:

* ### Configure

bashCopy code
[code]
    openclaw configure --section web# Select "duckduckgo" as the provider
[/code]

## การกำหนดค่า

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

การตั้งค่าระดับ Plugin ที่ไม่บังคับสำหรับภูมิภาคและ SafeSearch:

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo region code            safeSearch: "moderate", // "strict", "moderate", or "off"          },        },      },    },  },}
[/code]

## พารามิเตอร์ของเครื่องมือ

คำค้นหา

จำนวนผลลัพธ์ที่จะส่งคืน (1-10)

รหัสภูมิภาคของ DuckDuckGo (เช่น `us-en`, `uk-en`, `de-de`)

ระดับ SafeSearch

ภูมิภาคและ SafeSearch สามารถตั้งค่าใน config ของ Plugin ได้เช่นกัน (ดูด้านบน) - พารามิเตอร์ ของเครื่องมือจะแทนที่ค่า config เป็นรายคำค้นหา

## หมายเหตุ

  * **ไม่ต้องใช้คีย์ API** \- ใช้งานได้ทันทีโดยไม่ต้องกำหนดค่า
  * **ทดลอง** \- รวบรวมผลลัพธ์จากหน้า HTML ค้นหาแบบไม่ใช้ JavaScript ของ DuckDuckGo ไม่ใช่ API หรือ SDK อย่างเป็นทางการ
  * **ความเสี่ยงจากการท้าทายบอต** \- DuckDuckGo อาจแสดง CAPTCHA หรือบล็อกคำขอ ภายใต้การใช้งานหนักหรือแบบอัตโนมัติ
  * **การแยกวิเคราะห์ HTML** \- ผลลัพธ์ขึ้นอยู่กับโครงสร้างหน้า ซึ่งอาจเปลี่ยนแปลงได้โดยไม่ แจ้งให้ทราบ
  * **ลำดับการตรวจจับอัตโนมัติ** \- DuckDuckGo เป็น fallback แบบไม่ต้องใช้คีย์ตัวแรก (ลำดับ 100) ในการตรวจจับอัตโนมัติ ผู้ให้บริการที่ใช้ API พร้อมคีย์ที่กำหนดค่าไว้จะทำงาน ก่อน จากนั้น Ollama Web Search (ลำดับ 110) แล้วจึง SearXNG (ลำดับ 200)
  * **SafeSearch ใช้ค่าเริ่มต้นเป็น moderate** เมื่อไม่ได้กำหนดค่า


## ที่เกี่ยวข้อง

  * [ภาพรวม Web Search](</th/tools/web>) \-- ผู้ให้บริการทั้งหมดและการตรวจจับอัตโนมัติ
  * [Brave Search](</th/tools/brave-search>) \-- ผลลัพธ์แบบมีโครงสร้างพร้อม tier ฟรี
  * [Exa Search](</th/tools/exa-search>) \-- การค้นหาแบบ neural พร้อมการดึงเนื้อหา


Was this useful?YesNo