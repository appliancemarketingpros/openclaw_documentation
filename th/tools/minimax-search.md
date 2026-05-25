---
title: การค้นหา MiniMax
source_url: https://docs.openclaw.ai/th/tools/minimax-search
scraped_at: 2026-05-25
---

OpenClaw รองรับ MiniMax ในฐานะผู้ให้บริการ `web_search` ผ่าน MiniMax Token Plan search API โดยจะส่งคืนผลการค้นหาแบบมีโครงสร้างพร้อมชื่อเรื่อง, URL, ตัวอย่างข้อความ และคำค้นหาที่เกี่ยวข้อง

## รับข้อมูลรับรอง Token Plan

* ### สร้างคีย์

สร้างหรือคัดลอกคีย์ MiniMax Token Plan จาก [MiniMax Platform](<https://platform.minimax.io/user-center/basic-information/interface-key>) การตั้งค่า OAuth สามารถใช้ `MINIMAX_OAUTH_TOKEN` แทนได้

* ### จัดเก็บคีย์

ตั้งค่า `MINIMAX_CODE_PLAN_KEY` ในสภาพแวดล้อมของ Gateway หรือกำหนดค่าผ่าน:

bashCopy code
[code]
    openclaw configure --section web
[/code]

OpenClaw ยังยอมรับ `MINIMAX_CODING_API_KEY`, `MINIMAX_OAUTH_TOKEN` และ `MINIMAX_API_KEY` เป็นนามแฝงของตัวแปรสภาพแวดล้อมด้วย `MINIMAX_API_KEY` ควรชี้ไปยัง ข้อมูลรับรอง Token Plan ที่เปิดใช้การค้นหาได้; คีย์ API รุ่นทั่วไปของ MiniMax อาจไม่ได้รับการยอมรับ โดยปลายทางการค้นหา Token Plan

## การกำหนดค่า

json5Copy code
[code]
    {  plugins: {    entries: {      minimax: {        config: {          webSearch: {            apiKey: "sk-cp-...", // optional if a MiniMax Token Plan env var is set            region: "global", // or "cn"          },        },      },    },  },  tools: {    web: {      search: {        provider: "minimax",      },    },  },}
[/code]

**ทางเลือกด้วยสภาพแวดล้อม:** ตั้งค่า `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`, `MINIMAX_OAUTH_TOKEN` หรือ `MINIMAX_API_KEY` ในสภาพแวดล้อมของ Gateway สำหรับการติดตั้ง gateway ให้ใส่ไว้ใน `~/.openclaw/.env`

## การเลือกภูมิภาค

MiniMax Search ใช้ปลายทางเหล่านี้:

  * ทั่วโลก: `https://api.minimax.io/v1/coding_plan/search`
  * CN: `https://api.minimaxi.com/v1/coding_plan/search`


หากไม่ได้ตั้งค่า `plugins.entries.minimax.config.webSearch.region` OpenClaw จะระบุ ภูมิภาคตามลำดับนี้:

  1. `tools.web.search.minimax.region` / `webSearch.region` ที่ Plugin เป็นเจ้าของ
  2. `MINIMAX_API_HOST`
  3. `models.providers.minimax.baseUrl`
  4. `models.providers.minimax-portal.baseUrl`


นั่นหมายความว่าการเริ่มต้นใช้งาน CN หรือ `MINIMAX_API_HOST=https://api.minimaxi.com/...` จะทำให้ MiniMax Search ใช้โฮสต์ CN โดยอัตโนมัติด้วย

แม้เมื่อคุณยืนยันตัวตนกับ MiniMax ผ่านเส้นทาง OAuth `minimax-portal` การค้นเว็บยังคงลงทะเบียนเป็นรหัสผู้ให้บริการ `minimax`; URL ฐานของผู้ให้บริการ OAuth จะถูกใช้เป็นคำใบ้ภูมิภาคสำหรับการเลือกโฮสต์ CN/ทั่วโลก และ `MINIMAX_OAUTH_TOKEN` สามารถใช้เป็นข้อมูลรับรอง bearer สำหรับ MiniMax Search ได้

## พารามิเตอร์ที่รองรับ

พารามิเตอร์ | ชนิด | ข้อจำกัด | คำอธิบาย  
---|---|---|---  
`query` | string | required | สตริงคำค้นหา  
`count` | integer | 1-10 | จำนวนผลลัพธ์ที่จะส่งคืน OpenClaw จะตัดรายการที่ส่งคืนให้เหลือขนาดนี้  
  
ยังไม่รองรับตัวกรองเฉพาะผู้ให้บริการในขณะนี้

## ที่เกี่ยวข้อง

  * [ภาพรวม Web Search](</th/tools/web>) \-- ผู้ให้บริการทั้งหมดและการตรวจจับอัตโนมัติ
  * [MiniMax](</th/providers/minimax>) \-- การตั้งค่าโมเดล, รูปภาพ, เสียงพูด และการยืนยันตัวตน


Was this useful?YesNo