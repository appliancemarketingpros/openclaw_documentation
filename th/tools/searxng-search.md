---
title: การค้นหาด้วย SearXNG
source_url: https://docs.openclaw.ai/th/tools/searxng-search
scraped_at: 2026-05-25
---

OpenClaw รองรับ [SearXNG](<https://docs.searxng.org/>) เป็นผู้ให้บริการ `web_search` แบบ **โฮสต์เอง, ไม่ต้องใช้คีย์** SearXNG เป็นเครื่องมือค้นหาแบบเมตาโอเพนซอร์ส ที่รวบรวมผลลัพธ์จาก Google, Bing, DuckDuckGo และแหล่งอื่นๆ

ข้อดี:

  * **ฟรีและไม่จำกัด** \-- ไม่ต้องใช้คีย์ API หรือการสมัครสมาชิกเชิงพาณิชย์
  * **ความเป็นส่วนตัว / air-gap** \-- คำค้นหาจะไม่ออกจากเครือข่ายของคุณ
  * **ใช้งานได้ทุกที่** \-- ไม่มีข้อจำกัดตามภูมิภาคของ API ค้นหาเชิงพาณิชย์


## การตั้งค่า

* ### Run a SearXNG instance

bashCopy code
[code]
    docker run -d -p 8888:8080 searxng/searxng
[/code]

หรือใช้การปรับใช้ SearXNG ที่มีอยู่ใดๆ ที่คุณเข้าถึงได้ ดู [เอกสารประกอบ SearXNG](<https://docs.searxng.org/>) สำหรับการตั้งค่าระดับโปรดักชัน

* ### Configure

bashCopy code
[code]
    openclaw configure --section web# Select "searxng" as the provider
[/code]

หรือตั้งค่าตัวแปรสภาพแวดล้อมแล้วให้การตรวจจับอัตโนมัติค้นหา:

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

## การกำหนดค่า

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "searxng",      },    },  },}
[/code]

การตั้งค่าระดับ Plugin สำหรับอินสแตนซ์ SearXNG:

json5Copy code
[code]
    {  plugins: {    entries: {      searxng: {        config: {          webSearch: {            baseUrl: "http://localhost:8888",            categories: "general,news", // optional            language: "en", // optional          },        },      },    },  },}
[/code]

ฟิลด์ `baseUrl` ยังรับออบเจ็กต์ SecretRef ได้ด้วย

กฎการขนส่ง:

  * `https://` ใช้งานได้กับโฮสต์ SearXNG สาธารณะหรือส่วนตัว
  * `http://` จะยอมรับเฉพาะโฮสต์เครือข่ายส่วนตัวที่เชื่อถือได้หรือโฮสต์ loopback เท่านั้น
  * โฮสต์ SearXNG สาธารณะต้องใช้ `https://`
  * โฮสต์ส่วนตัว/ภายในใช้การป้องกันเครือข่ายแบบโฮสต์เอง; โฮสต์ `https://` สาธารณะจะยังอยู่บนการป้องกัน web-search แบบเข้มงวดและไม่สามารถเปลี่ยนเส้นทางไปยัง ที่อยู่ส่วนตัวได้


## ตัวแปรสภาพแวดล้อม

ตั้งค่า `SEARXNG_BASE_URL` เป็นทางเลือกแทนการกำหนดค่า:

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

เมื่อตั้งค่า `SEARXNG_BASE_URL` และไม่ได้กำหนดค่าผู้ให้บริการอย่างชัดเจน การตรวจจับอัตโนมัติ จะเลือก SearXNG โดยอัตโนมัติ (ที่ลำดับความสำคัญต่ำสุด -- ผู้ให้บริการที่มี API รองรับพร้อม คีย์จะชนะก่อน)

## อ้างอิงการกำหนดค่า Plugin

ฟิลด์ | คำอธิบาย  
---|---  
`baseUrl` | URL ฐานของอินสแตนซ์ SearXNG ของคุณ (จำเป็น)  
`categories` | หมวดหมู่คั่นด้วยจุลภาค เช่น `general`, `news` หรือ `science`  
`language` | รหัสภาษาสำหรับผลลัพธ์ เช่น `en`, `de` หรือ `fr`  
  
## หมายเหตุ

  * **JSON API** \-- ใช้ปลายทาง `format=json` ดั้งเดิมของ SearXNG ไม่ใช่การ scrape HTML
  * **URL ผลลัพธ์รูปภาพ** \-- ผลลัพธ์ในหมวดหมู่รูปภาพจะรวม `img_src` เมื่อ SearXNG ส่งคืน URL รูปภาพโดยตรง
  * **ไม่มีคีย์ API** \-- ใช้งานได้กับอินสแตนซ์ SearXNG ใดๆ ทันที
  * **การตรวจสอบ URL ฐาน** \-- `baseUrl` ต้องเป็น URL `http://` หรือ `https://` ที่ถูกต้อง; โฮสต์สาธารณะต้องใช้ `https://`
  * **การป้องกันเครือข่าย** \-- ปลายทาง SearXNG ส่วนตัว/ภายในเลือกใช้ การเข้าถึงเครือข่ายส่วนตัว; ปลายทาง SearXNG `https://` สาธารณะคงการป้องกัน SSRF แบบเข้มงวด
  * **ลำดับการตรวจจับอัตโนมัติ** \-- SearXNG จะถูกตรวจสอบเป็นลำดับสุดท้าย (ลำดับ 200) ใน การตรวจจับอัตโนมัติ ผู้ให้บริการที่มี API รองรับพร้อมคีย์ที่กำหนดค่าไว้จะทำงานก่อน จากนั้น DuckDuckGo (ลำดับ 100) และตามด้วย Ollama Web Search (ลำดับ 110)
  * **โฮสต์เอง** \-- คุณควบคุมอินสแตนซ์ คำค้นหา และเครื่องมือค้นหาต้นทางเอง
  * **หมวดหมู่** มีค่าเริ่มต้นเป็น `general` เมื่อไม่ได้กำหนดค่า
  * **การ fallback ของหมวดหมู่** \-- หากคำขอหมวดหมู่ที่ไม่ใช่ `general` สำเร็จแต่ ส่งคืนผลลัพธ์เป็นศูนย์ OpenClaw จะลองคำค้นหาเดิมอีกครั้งหนึ่งด้วย `general` ก่อนส่งคืนชุดผลลัพธ์ว่าง


## ที่เกี่ยวข้อง

  * [ภาพรวม Web Search](</th/tools/web>) \-- ผู้ให้บริการทั้งหมดและการตรวจจับอัตโนมัติ
  * [DuckDuckGo Search](</th/tools/duckduckgo-search>) \-- fallback แบบไม่ต้องใช้คีย์อีกตัวหนึ่ง
  * [Brave Search](</th/tools/brave-search>) \-- ผลลัพธ์แบบมีโครงสร้างพร้อมระดับใช้งานฟรี


Was this useful?YesNo