---
title: การค้นหาแบบขนาน
source_url: https://docs.openclaw.ai/th/tools/parallel-search
scraped_at: 2026-06-29
---

CapabilitiesTools

Plugin Parallel มีผู้ให้บริการ `web_search` ของ [Parallel](<https://parallel.ai/>) สองรายการ:

  * **Parallel Search (ฟรี)** (`parallel-free`) -- [Search MCP](<https://docs.parallel.ai/integrations/mcp/search-mcp>) ฟรีของ Parallel ไม่ต้องมี บัญชีหรือคีย์ API เลือกใช้โดยตรงเมื่อคุณต้องการเส้นทางการค้นหาแบบโฮสต์ของ Parallel ที่ไม่ต้องใช้คีย์
  * **Parallel Search** (`parallel`) -- Search API แบบชำระเงินของ Parallel ต้องมี `PARALLEL_API_KEY` และมีขีดจำกัดอัตราที่สูงกว่า รวมถึงการปรับแต่ง objective


ทั้งสองรายการส่งคืนข้อความตัดตอนที่จัดอันดับแล้วและปรับให้เหมาะกับ LLM จากดัชนีเว็บที่สร้างมาสำหรับเอเจนต์ AI ตั้งค่า `tools.web.search.provider` เป็น `parallel-free` หรือ `parallel` เพื่อเลือกรายการหนึ่ง โดยตรง

## ติดตั้ง Plugin

ติดตั้ง Plugin ทางการ แล้วรีสตาร์ต Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/parallel-pluginopenclaw gateway restart
[/code]

## คีย์ API (ผู้ให้บริการแบบชำระเงิน)

`parallel-free` ไม่ต้องใช้คีย์ API แต่ยังต้องเลือกเป็นผู้ให้บริการที่จัดการอยู่ ผู้ให้บริการ `parallel` แบบชำระเงินต้องใช้คีย์ API:

* ### สร้างบัญชี

สมัครใช้งานที่ [platform.parallel.ai](<https://platform.parallel.ai>) และ สร้างคีย์ API จากแดชบอร์ดของคุณ

* ### จัดเก็บคีย์

ตั้งค่า `PARALLEL_API_KEY` ในสภาพแวดล้อมของ Gateway หรือกำหนดค่าผ่าน:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## การกำหนดค่า

json5Copy code
[code]
    {  plugins: {    entries: {      parallel: {        config: {          webSearch: {            apiKey: "par-...", // optional if PARALLEL_API_KEY is set            baseUrl: "https://api.parallel.ai", // optional; OpenClaw appends /v1/search          },        },      },    },  },  tools: {    web: {      search: {        // Use "parallel-free" for the free Search MCP, or "parallel" for        // the paid API-backed provider shown here.        provider: "parallel",      },    },  },}
[/code]

**ทางเลือกผ่านสภาพแวดล้อม:** ตั้งค่า `PARALLEL_API_KEY` ในสภาพแวดล้อมของ Gateway สำหรับการติดตั้ง Gateway ให้ใส่ไว้ใน `~/.openclaw/.env`

## การแทนที่ Base URL

การแทนที่ base URL ใช้กับผู้ให้บริการ `parallel` แบบชำระเงินเท่านั้น ผู้ให้บริการฟรี `parallel-free` ใช้ `https://search.parallel.ai/mcp` เสมอ

ตั้งค่า `plugins.entries.parallel.config.webSearch.baseUrl` เมื่อคำขอ Parallel ควรผ่านพร็อกซีที่เข้ากันได้หรือ endpoint อื่นของ Parallel (เช่น Cloudflare AI Gateway) OpenClaw ทำให้โฮสต์เปล่าเป็นรูปแบบมาตรฐานโดยเติม `https://` ไว้ข้างหน้า และต่อท้าย `/v1/search` เว้นแต่ path จะลงท้ายด้วยค่านั้นอยู่แล้ว endpoint ที่แก้ไขแล้วจะถูกรวมไว้ในคีย์แคชการค้นหา ดังนั้นผลลัพธ์ จาก endpoint ของ Parallel ที่ต่างกันจะไม่ถูกใช้ร่วมกัน

## พารามิเตอร์ของเครื่องมือ

OpenClaw เปิดเผยรูปแบบการค้นหาเนทีฟของ Parallel เพื่อให้โมเดลกรอกได้ทั้ง เป้าหมายภาษาธรรมชาติและคำค้นแบบคีย์เวิร์ดสั้น ๆ สองสามรายการ ซึ่งเป็นการจับคู่ที่ Parallel [แนะนำ](<https://docs.parallel.ai/search/best-practices>) เพื่อให้ได้ ผลลัพธ์ที่ดีที่สุด

คำอธิบายภาษาธรรมชาติของคำถามหรือเป้าหมายพื้นฐาน (สูงสุด 5000 อักขระ) ควรมีบริบทครบถ้วนในตัวเอง

คำค้นแบบคีย์เวิร์ดที่กระชับ รายการละ 3-6 คำ (1-5 รายการ สูงสุด 200 อักขระ ต่อรายการ) ระบุคำค้นที่หลากหลาย 2-3 รายการเพื่อให้ได้ผลลัพธ์ที่ดีที่สุด

จำนวนผลลัพธ์ที่ต้องการส่งคืน (1-40)

id เซสชัน Parallel ที่เป็นตัวเลือก (สูงสุด 1000 อักขระบน `parallel`; Search MCP ฟรี `parallel-free` จำกัดไว้ที่ 100) ส่ง `sessionId` จากผลลัพธ์ Parallel ก่อนหน้า ในการค้นหาติดตามผลที่เป็นส่วนหนึ่งของงานเดียวกัน เพื่อให้ Parallel จัดกลุ่มการเรียกที่เกี่ยวข้องและปรับปรุงผลลัพธ์ถัดไปได้ id ที่เกินขีดจำกัด จะถูกทิ้งและสร้าง id ใหม่

ตัวระบุของโมเดลที่เรียกใช้งาน ซึ่งเป็นตัวเลือก (เช่น `claude-opus-4-7`, `gpt-5.5`) ช่วยให้ Parallel ปรับการตั้งค่าเริ่มต้นให้เหมาะกับ ความสามารถของโมเดลของคุณ ส่ง slug ของโมเดลที่ใช้งานอยู่แบบตรงตัว อย่าย่อเป็น alias ของตระกูลโมเดล

## หมายเหตุ

  * Parallel จัดอันดับและบีบอัดผลลัพธ์ตามประโยชน์ต่อการใช้เหตุผลของ LLM ไม่ใช่ อัตราการคลิกของมนุษย์ คาดว่าจะได้ข้อความตัดตอนที่หนาแน่นในแต่ละผลลัพธ์ แทนที่จะเป็น เนื้อหาทั้งหน้า
  * ข้อความตัดตอนของผลลัพธ์จะถูกส่งกลับเป็นอาร์เรย์ `excerpts` และยังถูกรวมเข้าใน ฟิลด์ `description` เพื่อให้เข้ากันได้กับสัญญา `web_search` ทั่วไป
  * Parallel ส่งคืน `session_id` ในทุกการตอบกลับ OpenClaw เปิดเผยค่านี้เป็น `sessionId` ใน payload ของเครื่องมือ เพื่อให้ผู้เรียกจัดกลุ่มการค้นหาติดตามผลได้
  * `searchId`, `warnings` และ `usage` จาก Parallel จะถูกส่งผ่านเมื่อ มีอยู่
  * OpenClaw ส่งต่อจำนวนผลลัพธ์ที่แก้ไขแล้วไปยัง Parallel เป็น `advanced_settings.max_results` เสมอ อาร์กิวเมนต์ `count` ของผู้เรียกมีลำดับความสำคัญก่อน ตามด้วย การตั้งค่าระดับบนสุด `tools.web.search.maxResults` มิฉะนั้นจะใช้ค่าเริ่มต้น `web_search` ทั่วไปของ OpenClaw (5) วิธีนี้ทำให้ปริมาณผลลัพธ์สอดคล้องกัน เมื่อสลับระหว่างผู้ให้บริการ ส่วน Parallel เองมีค่าเริ่มต้นเป็น 10
  * ผลลัพธ์ถูกแคชไว้ 15 นาทีตามค่าเริ่มต้น (กำหนดค่าได้ผ่าน `cacheTtlMinutes`)
  * ผู้ให้บริการฟรี `parallel-free` รับพารามิเตอร์เดียวกัน โดยจะใช้ `count` ฝั่งไคลเอนต์และสร้าง `session_id` ต่อการเรียกเมื่อไม่ได้ ระบุมา


## ที่เกี่ยวข้อง

  * [ภาพรวมการค้นหาเว็บ](</th/tools/web>) \-- ผู้ให้บริการทั้งหมดและการตรวจจับอัตโนมัติ
  * [การค้นหา Exa](</th/tools/exa-search>) \-- การค้นหาแบบ neural พร้อมการแยกเนื้อหา
  * [การค้นหา Perplexity](</th/tools/perplexity-search>) \-- ผลลัพธ์แบบมีโครงสร้างพร้อมการกรองโดเมน


Was this useful?YesNo

Open issue