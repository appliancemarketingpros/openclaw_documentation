---
title: การค้นหา Exa
source_url: https://docs.openclaw.ai/th/tools/exa-search
scraped_at: 2026-05-25
---

OpenClaw รองรับ [Exa AI](<https://exa.ai/>) เป็นผู้ให้บริการ `web_search` Exa มีโหมดการค้นหาแบบนิวรัล คีย์เวิร์ด และไฮบริด พร้อมการดึงเนื้อหาในตัว (ไฮไลต์ ข้อความ บทสรุป)

## ขอรับคีย์ API

* ### สร้างบัญชี

ลงทะเบียนที่ [exa.ai](<https://exa.ai/>) และสร้างคีย์ API จากแดชบอร์ดของคุณ

* ### จัดเก็บคีย์

ตั้งค่า `EXA_API_KEY` ในสภาพแวดล้อมของ Gateway หรือกำหนดค่าผ่าน:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## การกำหนดค่า

json5Copy code
[code]
    {  plugins: {    entries: {      exa: {        config: {          webSearch: {            apiKey: "exa-...", // optional if EXA_API_KEY is set            baseUrl: "https://api.exa.ai", // optional; OpenClaw appends /search          },        },      },    },  },  tools: {    web: {      search: {        provider: "exa",      },    },  },}
[/code]

**ทางเลือกสำหรับสภาพแวดล้อม:** ตั้งค่า `EXA_API_KEY` ในสภาพแวดล้อมของ Gateway สำหรับการติดตั้ง Gateway ให้ใส่ไว้ใน `~/.openclaw/.env`

## การแทนที่ URL ฐาน

ตั้งค่า `plugins.entries.exa.config.webSearch.baseUrl` เมื่อคำขอค้นหาของ Exa ควรผ่านพร็อกซีที่เข้ากันได้หรือปลายทาง Exa ทางเลือก OpenClaw ปรับโฮสต์เปล่าให้เป็นรูปแบบปกติโดยเติม `https://` ไว้ด้านหน้า และเติม `/search` เว้นแต่ พาธจะลงท้ายด้วยค่านั้นอยู่แล้ว ปลายทางที่แก้ไขแล้วจะถูกรวมไว้ในคีย์แคชการค้นหา ดังนั้นผลลัพธ์จากปลายทาง Exa ต่างกันจะไม่ถูกใช้ร่วมกัน

## พารามิเตอร์ของเครื่องมือ

คำค้นหา

ผลลัพธ์ที่จะส่งคืน (1–100)

โหมดการค้นหา

ตัวกรองเวลา

ผลลัพธ์หลังวันที่นี้ (`YYYY-MM-DD`)

ผลลัพธ์ก่อนวันที่นี้ (`YYYY-MM-DD`)

ตัวเลือกการดึงเนื้อหา (ดูด้านล่าง)

### การดึงเนื้อหา

Exa สามารถส่งคืนเนื้อหาที่ดึงมาแล้วควบคู่กับผลลัพธ์การค้นหาได้ ส่งอ็อบเจกต์ `contents` เพื่อเปิดใช้งาน:

javascriptCopy code
[code]
    await web_search({  query: "transformer architecture explained",  type: "neural",  contents: {    text: true, // full page text    highlights: { numSentences: 3 }, // key sentences    summary: true, // AI summary  },});
[/code]

ตัวเลือก Contents | ประเภท | คำอธิบาย  
---|---|---  
`text` | `boolean | { maxCharacters }` | ดึงข้อความทั้งหน้า  
`highlights` | `boolean | { maxCharacters, query, numSentences, highlightsPerUrl }` | ดึงประโยคสำคัญ  
`summary` | `boolean | { query }` | บทสรุปที่สร้างโดย AI  
  
### โหมดการค้นหา

โหมด | คำอธิบาย  
---|---  
`auto` | Exa เลือกโหมดที่ดีที่สุด (ค่าเริ่มต้น)  
`neural` | การค้นหาเชิงความหมาย/ตามความหมาย  
`fast` | การค้นหาคีย์เวิร์ดแบบรวดเร็ว  
`deep` | การค้นหาเชิงลึกอย่างละเอียด  
`deep-reasoning` | การค้นหาเชิงลึกพร้อมการให้เหตุผล  
`instant` | ผลลัพธ์ที่เร็วที่สุด  
  
## หมายเหตุ

  * หากไม่ได้ระบุตัวเลือก `contents` Exa จะใช้ค่าเริ่มต้นเป็น `{ highlights: true }` เพื่อให้ผลลัพธ์มีข้อความตัดตอนของประโยคสำคัญ
  * ผลลัพธ์จะคงฟิลด์ `highlightScores` และ `summary` จากการตอบกลับของ Exa API เมื่อมีให้ใช้
  * คำอธิบายผลลัพธ์จะถูกแก้จากไฮไลต์ก่อน จากนั้นเป็นบทสรุป แล้วจึงเป็น ข้อความเต็ม แล้วแต่ว่ารายการใดมีให้ใช้
  * ไม่สามารถใช้ `freshness` ร่วมกับ `date_after`/`date_before` ได้ ให้ใช้ โหมดตัวกรองเวลาอย่างใดอย่างหนึ่ง
  * ส่งคืนผลลัพธ์ได้สูงสุด 100 รายการต่อคำค้นหา (ขึ้นอยู่กับขีดจำกัด ของประเภทการค้นหาของ Exa)
  * ผลลัพธ์จะถูกแคชเป็นเวลา 15 นาทีโดยค่าเริ่มต้น (กำหนดค่าได้ผ่าน `cacheTtlMinutes`)
  * Exa เป็นการผสานรวม API อย่างเป็นทางการพร้อมการตอบกลับ JSON แบบมีโครงสร้าง


## ที่เกี่ยวข้อง

  * [ภาพรวม Web Search](</th/tools/web>) \-- ผู้ให้บริการทั้งหมดและการตรวจจับอัตโนมัติ
  * [Brave Search](</th/tools/brave-search>) \-- ผลลัพธ์แบบมีโครงสร้างพร้อมตัวกรองประเทศ/ภาษา
  * [Perplexity Search](</th/tools/perplexity-search>) \-- ผลลัพธ์แบบมีโครงสร้างพร้อมการกรองโดเมน


Was this useful?YesNo