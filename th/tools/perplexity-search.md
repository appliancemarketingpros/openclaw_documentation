---
title: การค้นหา Perplexity
source_url: https://docs.openclaw.ai/th/tools/perplexity-search
scraped_at: 2026-05-25
---

OpenClaw รองรับ Perplexity Search API เป็นผู้ให้บริการ `web_search` โดยจะส่งคืนผลลัพธ์แบบมีโครงสร้างพร้อมฟิลด์ `title`, `url` และ `snippet`

เพื่อความเข้ากันได้ OpenClaw ยังรองรับการตั้งค่า Perplexity Sonar/OpenRouter แบบเดิมด้วย หากคุณใช้ `OPENROUTER_API_KEY`, คีย์ `sk-or-...` ใน `plugins.entries.perplexity.config.webSearch.apiKey` หรือตั้งค่า `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` ผู้ให้บริการจะสลับไปใช้เส้นทาง chat-completions และส่งคืนคำตอบที่ AI สังเคราะห์พร้อมการอ้างอิงแทนผลลัพธ์ Search API แบบมีโครงสร้าง

## การรับคีย์ Perplexity API

  1. สร้างบัญชี Perplexity ที่ [perplexity.ai/settings/api](<https://www.perplexity.ai/settings/api>)
  2. สร้างคีย์ API ในแดชบอร์ด
  3. จัดเก็บคีย์ไว้ในการกำหนดค่า หรือตั้งค่า `PERPLEXITY_API_KEY` ในสภาพแวดล้อมของ Gateway


## ความเข้ากันได้กับ OpenRouter

หากคุณใช้ OpenRouter สำหรับ Perplexity Sonar อยู่แล้ว ให้คง `provider: "perplexity"` ไว้และตั้งค่า `OPENROUTER_API_KEY` ในสภาพแวดล้อมของ Gateway หรือจัดเก็บคีย์ `sk-or-...` ใน `plugins.entries.perplexity.config.webSearch.apiKey`

การควบคุมความเข้ากันได้แบบไม่บังคับ:

  * `plugins.entries.perplexity.config.webSearch.baseUrl`
  * `plugins.entries.perplexity.config.webSearch.model`


## ตัวอย่างการกำหนดค่า

### Perplexity Search API แบบเนทีฟ

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "pplx-...",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

### ความเข้ากันได้กับ OpenRouter / Sonar

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "<openrouter-api-key>",            baseUrl: "https://openrouter.ai/api/v1",            model: "perplexity/sonar-pro",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

## ตำแหน่งที่ตั้งค่าคีย์

**ผ่านการกำหนดค่า:** เรียกใช้ `openclaw configure --section web` ซึ่งจะจัดเก็บคีย์ใน `~/.openclaw/openclaw.json` ใต้ `plugins.entries.perplexity.config.webSearch.apiKey` ฟิลด์นั้นยังยอมรับออบเจ็กต์ SecretRef ด้วย

**ผ่านสภาพแวดล้อม:** ตั้งค่า `PERPLEXITY_API_KEY` หรือ `OPENROUTER_API_KEY` ในสภาพแวดล้อมของกระบวนการ Gateway สำหรับการติดตั้ง gateway ให้ใส่ไว้ใน `~/.openclaw/.env` (หรือสภาพแวดล้อมของบริการของคุณ) ดู [ตัวแปรสภาพแวดล้อม](</th/help/faq#env-vars-and-env-loading>)

หากกำหนดค่า `provider: "perplexity"` ไว้ และ SecretRef ของคีย์ Perplexity ไม่สามารถแก้ค่าได้โดยไม่มีตัวสำรองจากสภาพแวดล้อม การเริ่มต้น/โหลดซ้ำจะล้มเหลวทันที

## พารามิเตอร์ของเครื่องมือ

พารามิเตอร์เหล่านี้ใช้กับเส้นทาง Perplexity Search API แบบเนทีฟ

คำค้นหา

จำนวนผลลัพธ์ที่จะส่งคืน (1-10)

รหัสประเทศ ISO 2 ตัวอักษร (เช่น `US`, `DE`)

รหัสภาษา ISO 639-1 (เช่น `en`, `de`, `fr`)

ตัวกรองเวลา - `day` คือ 24 ชั่วโมง

เฉพาะผลลัพธ์ที่เผยแพร่หลังวันที่นี้ (`YYYY-MM-DD`)

เฉพาะผลลัพธ์ที่เผยแพร่ก่อนวันที่นี้ (`YYYY-MM-DD`)

อาร์เรย์รายการโดเมนที่อนุญาต/ปฏิเสธ (สูงสุด 20)

งบประมาณเนื้อหารวม (สูงสุด 1000000)

ขีดจำกัดโทเค็นต่อหน้า

สำหรับเส้นทางความเข้ากันได้กับ Sonar/OpenRouter แบบเดิม:

  * ยอมรับ `query`, `count` และ `freshness`
  * `count` มีไว้เพื่อความเข้ากันได้เท่านั้นในเส้นทางนั้น การตอบกลับยังคงเป็นคำตอบที่สังเคราะห์ขึ้นหนึ่งรายการ พร้อมการอ้างอิง ไม่ใช่รายการผลลัพธ์ N รายการ
  * ตัวกรองที่ใช้ได้เฉพาะ Search API เช่น `country`, `language`, `date_after`, `date_before`, `domain_filter`, `max_tokens` และ `max_tokens_per_page` จะส่งคืนข้อผิดพลาดอย่างชัดเจน


**ตัวอย่าง:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (allowlist)await web_search({  query: "climate research",  domain_filter: ["nature.com", "science.org", ".edu"],}); // Domain filtering (denylist - prefix with -)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],}); // More content extractionawait web_search({  query: "detailed AI research",  max_tokens: 50000,  max_tokens_per_page: 4096,});
[/code]

### กฎตัวกรองโดเมน

  * สูงสุด 20 โดเมนต่อหนึ่งตัวกรอง
  * ไม่สามารถผสมรายการอนุญาตและรายการปฏิเสธในคำขอเดียวกันได้
  * ใช้คำนำหน้า `-` สำหรับรายการปฏิเสธ (เช่น `["-reddit.com"]`)


## หมายเหตุ

  * Perplexity Search API ส่งคืนผลลัพธ์การค้นหาเว็บแบบมีโครงสร้าง (`title`, `url`, `snippet`)
  * OpenRouter หรือ `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` ที่ระบุอย่างชัดเจน จะสลับ Perplexity กลับไปใช้ Sonar chat completions เพื่อความเข้ากันได้
  * ความเข้ากันได้กับ Sonar/OpenRouter ส่งคืนคำตอบที่สังเคราะห์ขึ้นหนึ่งรายการพร้อมการอ้างอิง ไม่ใช่แถวผลลัพธ์แบบมีโครงสร้าง
  * ผลลัพธ์ถูกแคชเป็นค่าเริ่มต้น 15 นาที (กำหนดค่าได้ผ่าน `cacheTtlMinutes`)


## ที่เกี่ยวข้อง

[**ภาพรวมการค้นหาเว็บ** ผู้ให้บริการทั้งหมดและกฎการตรวจจับอัตโนมัติ ](</th/tools/web>) [**การค้นหา Brave** ผลลัพธ์แบบมีโครงสร้างพร้อมตัวกรองประเทศและภาษา ](</th/tools/brave-search>) [**การค้นหา Exa** การค้นหาแบบนิวรัลพร้อมการดึงเนื้อหา ](</th/tools/exa-search>) [**เอกสาร Perplexity Search API** คู่มือเริ่มต้นอย่างรวดเร็วและเอกสารอ้างอิงอย่างเป็นทางการของ Perplexity Search API ](<https://docs.perplexity.ai/docs/search/quickstart>)

Was this useful?YesNo