---
title: ส่วนต่าง
source_url: https://docs.openclaw.ai/th/tools/diffs
scraped_at: 2026-05-25
---

`diffs` เป็นเครื่องมือ Plugin แบบไม่บังคับที่มีคำแนะนำระบบในตัวแบบสั้น และมี Skill คู่กันที่แปลงเนื้อหาการเปลี่ยนแปลงเป็นอาร์ติแฟกต์ diff แบบอ่านอย่างเดียวสำหรับเอเจนต์

รองรับอย่างใดอย่างหนึ่งต่อไปนี้:

  * ข้อความ `before` และ `after`
  * `patch` แบบ unified


สามารถส่งคืน:

  * URL ตัวแสดงผลของ Gateway สำหรับการนำเสนอแบบแคนวาส
  * พาธไฟล์ที่เรนเดอร์แล้ว (PNG หรือ PDF) สำหรับการส่งผ่านข้อความ
  * เอาต์พุตทั้งสองแบบในการเรียกครั้งเดียว


เมื่อเปิดใช้งาน Plugin นี้จะเติมคำแนะนำการใช้งานแบบกระชับไว้ในพื้นที่ system-prompt และยังเปิดเผย Skill แบบละเอียดสำหรับกรณีที่เอเจนต์ต้องการคำแนะนำที่ครบถ้วนกว่า

## เริ่มต้นอย่างรวดเร็ว

* ### ติดตั้ง Plugin

bashCopy code
[code]
    openclaw plugins install diffs
[/code]

* ### เปิดใช้งาน Plugin

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,      },    },  },}
[/code]

* ### เลือกโหมด

### view

โฟลว์ที่ให้ความสำคัญกับแคนวาสก่อน: เอเจนต์เรียก `diffs` ด้วย `mode: "view"` และเปิด `details.viewerUrl` ด้วย `canvas present`

### file

การส่งไฟล์ผ่านแชต: เอเจนต์เรียก `diffs` ด้วย `mode: "file"` และส่ง `details.filePath` ด้วย `message` โดยใช้ `path` หรือ `filePath`

### both

แบบรวม: เอเจนต์เรียก `diffs` ด้วย `mode: "both"` เพื่อรับอาร์ติแฟกต์ทั้งสองแบบในการเรียกครั้งเดียว

## ปิดใช้งานคำแนะนำระบบในตัว

หากคุณต้องการเปิดใช้เครื่องมือ `diffs` ต่อไปแต่ปิดใช้งานคำแนะนำ system-prompt ในตัว ให้ตั้งค่า `plugins.entries.diffs.hooks.allowPromptInjection` เป็น `false`:

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        hooks: {          allowPromptInjection: false,        },      },    },  },}
[/code]

การตั้งค่านี้จะบล็อกฮุก `before_prompt_build` ของ Plugin diffs โดยยังคงให้ Plugin เครื่องมือ และ Skill คู่กันพร้อมใช้งาน

หากคุณต้องการปิดใช้งานทั้งคำแนะนำและเครื่องมือ ให้ปิดใช้งาน Plugin แทน

## เวิร์กโฟลว์เอเจนต์ทั่วไป

* ### เรียก diffs

เอเจนต์เรียกเครื่องมือ `diffs` พร้อมอินพุต

* ### อ่านรายละเอียด

เอเจนต์อ่านฟิลด์ `details` จากการตอบกลับ

* ### นำเสนอ

เอเจนต์เปิด `details.viewerUrl` ด้วย `canvas present` หรือส่ง `details.filePath` ด้วย `message` โดยใช้ `path` หรือ `filePath` หรือทำทั้งสองอย่าง

## ตัวอย่างอินพุต

### ก่อนและหลัง

jsonCopy code
[code]
    {  "before": "# Hello\n\nOne",  "after": "# Hello\n\nTwo",  "path": "docs/example.md",  "mode": "view"}
[/code]

### Patch

jsonCopy code
[code]
    {  "patch": "diff --git a/src/example.ts b/src/example.ts\n--- a/src/example.ts\n+++ b/src/example.ts\n@@ -1 +1 @@\n-const x = 1;\n+const x = 2;\n",  "mode": "both"}
[/code]

## เอกสารอ้างอิงอินพุตของเครื่องมือ

ทุกฟิลด์เป็นแบบไม่บังคับ เว้นแต่จะระบุไว้

ข้อความต้นฉบับ จำเป็นต้องใช้ร่วมกับ `after` เมื่อไม่ระบุ `patch`

ข้อความที่อัปเดตแล้ว จำเป็นต้องใช้ร่วมกับ `before` เมื่อไม่ระบุ `patch`

ข้อความ unified diff ใช้ร่วมกับ `before` และ `after` ไม่ได้

ชื่อไฟล์ที่แสดงสำหรับโหมดก่อนและหลัง

คำใบ้สำหรับแทนที่ภาษาในโหมดก่อนและหลัง ค่าที่ไม่รู้จักจะย้อนกลับไปใช้ข้อความธรรมดา

ค่าแทนที่ชื่อของตัวแสดงผล

โหมดเอาต์พุต ค่าเริ่มต้นเป็นค่าเริ่มต้นของ Plugin `defaults.mode` นามแฝงที่เลิกแนะนำแล้ว: `"image"` ทำงานเหมือน `"file"` และยังคงยอมรับเพื่อความเข้ากันได้ย้อนหลัง

ธีมของตัวแสดงผล ค่าเริ่มต้นเป็นค่าเริ่มต้นของ Plugin `defaults.theme`

เลย์เอาต์ diff ค่าเริ่มต้นเป็นค่าเริ่มต้นของ Plugin `defaults.layout`

ขยายส่วนที่ไม่เปลี่ยนแปลงเมื่อมีบริบทเต็มพร้อมใช้งาน เป็นตัวเลือกต่อการเรียกเท่านั้น (ไม่ใช่คีย์ค่าเริ่มต้นของ Plugin)

รูปแบบไฟล์ที่เรนเดอร์ ค่าเริ่มต้นเป็นค่าเริ่มต้นของ Plugin `defaults.fileFormat`

พรีเซ็ตคุณภาพสำหรับการเรนเดอร์ PNG หรือ PDF

ค่าแทนที่สเกลอุปกรณ์ (`1`-`4`)

ความกว้างเรนเดอร์สูงสุดในพิกเซล CSS (`640`-`2400`)

TTL ของอาร์ติแฟกต์เป็นวินาทีสำหรับเอาต์พุตตัวแสดงผลและไฟล์แบบสแตนด์อโลน สูงสุด 21600

ค่าแทนที่ origin ของ URL ตัวแสดงผล แทนที่ `viewerBaseUrl` ของ Plugin ต้องเป็น `http` หรือ `https` และไม่มี query/hash

นามแฝงอินพุตเดิม

ยังคงยอมรับเพื่อความเข้ากันได้ย้อนหลัง:

  * `format` -> `fileFormat`
  * `imageFormat` -> `fileFormat`
  * `imageQuality` -> `fileQuality`
  * `imageScale` -> `fileScale`
  * `imageMaxWidth` -> `fileMaxWidth`

การตรวจสอบความถูกต้องและขีดจำกัด

  * `before` และ `after` แต่ละรายการสูงสุด 512 KiB
  * `patch` สูงสุด 2 MiB
  * `path` สูงสุด 2048 ไบต์
  * `lang` สูงสุด 128 ไบต์
  * `title` สูงสุด 1024 ไบต์
  * เพดานความซับซ้อนของ patch: สูงสุด 128 ไฟล์และรวมทั้งหมด 120000 บรรทัด
  * การส่ง `patch` พร้อมกับ `before` หรือ `after` จะถูกปฏิเสธ
  * ขีดจำกัดความปลอดภัยของไฟล์ที่เรนเดอร์แล้ว (ใช้กับ PNG และ PDF): 
    * `fileQuality: "standard"`: สูงสุด 8 MP (8,000,000 พิกเซลที่เรนเดอร์)
    * `fileQuality: "hq"`: สูงสุด 14 MP (14,000,000 พิกเซลที่เรนเดอร์)
    * `fileQuality: "print"`: สูงสุด 24 MP (24,000,000 พิกเซลที่เรนเดอร์)
    * PDF ยังมีขีดจำกัดสูงสุด 50 หน้า


## สัญญารายละเอียดเอาต์พุต

เครื่องมือส่งคืนเมทาดาทาแบบมีโครงสร้างภายใต้ `details`

ฟิลด์ตัวแสดงผล

ฟิลด์ร่วมสำหรับโหมดที่สร้างตัวแสดงผล:

  * `artifactId`
  * `viewerUrl`
  * `viewerPath`
  * `title`
  * `expiresAt`
  * `inputKind`
  * `fileCount`
  * `mode`
  * `context` (`agentId`, `sessionId`, `messageChannel`, `agentAccountId` เมื่อมี)

ฟิลด์ไฟล์

ฟิลด์ไฟล์เมื่อมีการเรนเดอร์ PNG หรือ PDF:

  * `artifactId`
  * `expiresAt`
  * `filePath`
  * `path` (ค่าเดียวกับ `filePath` เพื่อความเข้ากันได้กับเครื่องมือข้อความ)
  * `fileBytes`
  * `fileFormat`
  * `fileQuality`
  * `fileScale`
  * `fileMaxWidth`

นามแฝงเพื่อความเข้ากันได้

ส่งคืนด้วยสำหรับผู้เรียกเดิม:

  * `format` (ค่าเดียวกับ `fileFormat`)
  * `imagePath` (ค่าเดียวกับ `filePath`)
  * `imageBytes` (ค่าเดียวกับ `fileBytes`)
  * `imageQuality` (ค่าเดียวกับ `fileQuality`)
  * `imageScale` (ค่าเดียวกับ `fileScale`)
  * `imageMaxWidth` (ค่าเดียวกับ `fileMaxWidth`)


สรุปพฤติกรรมของโหมด:

โหมด | สิ่งที่ส่งคืน  
---|---  
`"view"` | ฟิลด์ตัวแสดงผลเท่านั้น  
`"file"` | ฟิลด์ไฟล์เท่านั้น ไม่มีอาร์ติแฟกต์ตัวแสดงผล  
`"both"` | ฟิลด์ตัวแสดงผลพร้อมฟิลด์ไฟล์ หากการเรนเดอร์ไฟล์ล้มเหลว ตัวแสดงผลยังคงส่งคืนพร้อม `fileError` และนามแฝง `imageError`  
  
## ส่วนที่ไม่เปลี่ยนแปลงซึ่งถูกยุบไว้

  * ตัวแสดงผลสามารถแสดงแถวเช่น `N unmodified lines`
  * ตัวควบคุมขยายบนแถวเหล่านั้นมีเงื่อนไข และไม่รับประกันว่าจะมีสำหรับอินพุตทุกชนิด
  * ตัวควบคุมขยายจะปรากฏเมื่อ diff ที่เรนเดอร์มีข้อมูลบริบทที่ขยายได้ ซึ่งเป็นเรื่องปกติสำหรับอินพุตก่อนและหลัง
  * สำหรับอินพุต unified patch จำนวนมาก เนื้อหาบริบทที่ละไว้จะไม่มีอยู่ใน hunk ของ patch ที่แยกวิเคราะห์แล้ว ดังนั้นแถวอาจปรากฏโดยไม่มีตัวควบคุมขยาย นี่เป็นพฤติกรรมที่คาดไว้
  * `expandUnchanged` ใช้เฉพาะเมื่อมีบริบทที่ขยายได้อยู่เท่านั้น


## ค่าเริ่มต้นของ Plugin

ตั้งค่าเริ่มต้นทั้ง Plugin ใน `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          defaults: {            fontFamily: "Fira Code",            fontSize: 15,            lineSpacing: 1.6,            layout: "unified",            showLineNumbers: true,            diffIndicators: "bars",            wordWrap: true,            background: true,            theme: "dark",            fileFormat: "png",            fileQuality: "standard",            fileScale: 2,            fileMaxWidth: 960,            mode: "both",            ttlSeconds: 21600,          },        },      },    },  },}
[/code]

ค่าเริ่มต้นที่รองรับ:

  * `fontFamily`
  * `fontSize`
  * `lineSpacing`
  * `layout`
  * `showLineNumbers`
  * `diffIndicators`
  * `wordWrap`
  * `background`
  * `theme`
  * `fileFormat`
  * `fileQuality`
  * `fileScale`
  * `fileMaxWidth`
  * `mode`
  * `ttlSeconds`


พารามิเตอร์เครื่องมือที่ระบุอย่างชัดเจนจะแทนที่ค่าเริ่มต้นเหล่านี้

### การกำหนดค่า URL ตัวแสดงผลแบบถาวร

ค่าทางเลือกสำรองที่ Plugin เป็นเจ้าของสำหรับลิงก์ตัวแสดงผลที่ส่งคืนเมื่อการเรียกเครื่องมือไม่ส่ง `baseUrl` ต้องเป็น `http` หรือ `https` และไม่มี query/hash

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          viewerBaseUrl: "https://gateway.example.com/openclaw",        },      },    },  },}
[/code]

## การกำหนดค่าความปลอดภัย

`false`: คำขอที่ไม่ใช่ loopback ไปยัง route ของตัวแสดงผลจะถูกปฏิเสธ `true`: อนุญาตตัวแสดงผลระยะไกลหากพาธที่มีโทเค็นถูกต้อง

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          security: {            allowRemoteViewer: false,          },        },      },    },  },}
[/code]

## วงจรชีวิตและที่จัดเก็บอาร์ติแฟกต์

  * อาร์ติแฟกต์ถูกจัดเก็บไว้ใต้โฟลเดอร์ย่อยชั่วคราว: `$TMPDIR/openclaw-diffs`
  * เมทาดาทาของอาร์ติแฟกต์ตัวแสดงผลประกอบด้วย: 
    * ID อาร์ติแฟกต์แบบสุ่ม (อักขระ hex 20 ตัว)
    * โทเค็นแบบสุ่ม (อักขระ hex 48 ตัว)
    * `createdAt` และ `expiresAt`
    * พาธ `viewer.html` ที่จัดเก็บไว้
  * TTL เริ่มต้นของอาร์ติแฟกต์คือ 30 นาทีเมื่อไม่ได้ระบุ
  * TTL ของตัวแสดงผลสูงสุดที่ยอมรับคือ 6 ชั่วโมง
  * การล้างข้อมูลทำงานตามโอกาสหลังจากสร้างอาร์ติแฟกต์
  * อาร์ติแฟกต์ที่หมดอายุจะถูกลบ
  * การล้างข้อมูลสำรองจะลบโฟลเดอร์เก่าที่เก่ากว่า 24 ชั่วโมงเมื่อไม่มีเมทาดาทา


## URL ตัวแสดงผลและพฤติกรรมเครือข่าย

Route ของตัวแสดงผล:

  * `/plugins/diffs/view/{artifactId}/{token}`


แอสเซ็ตของตัวแสดงผล:

  * `/plugins/diffs/assets/viewer.js`
  * `/plugins/diffs/assets/viewer-runtime.js`


เอกสารตัวแสดงผล resolve แอสเซ็ตเหล่านั้นโดยอิงกับ URL ของตัวแสดงผล ดังนั้น prefix พาธ `baseUrl` แบบไม่บังคับจะถูกคงไว้สำหรับคำขอแอสเซ็ตทั้งสองรายการด้วย

พฤติกรรมการสร้าง URL:

  * หากระบุ `baseUrl` ในการเรียกเครื่องมือ ระบบจะใช้ค่านั้นหลังจากตรวจสอบอย่างเข้มงวด
  * มิฉะนั้น หากกำหนดค่า `viewerBaseUrl` ของ Plugin ไว้ ระบบจะใช้ค่านั้น
  * หากไม่มีค่าแทนที่ทั้งสองแบบ URL ตัวแสดงผลจะมีค่าเริ่มต้นเป็น loopback `127.0.0.1`
  * หากโหมด bind ของ Gateway เป็น `custom` และตั้งค่า `gateway.customBindHost` ไว้ ระบบจะใช้ host นั้น


กฎของ `baseUrl`:

  * ต้องเป็น `http://` หรือ `https://`
  * Query และ hash จะถูกปฏิเสธ
  * อนุญาตให้ใช้ origin พร้อมพาธฐานแบบไม่บังคับ


## โมเดลความปลอดภัย

การเสริมความปลอดภัยของ Viewer

  * จำกัดเฉพาะ loopback โดยค่าเริ่มต้น
  * เส้นทาง Viewer แบบมีโทเค็น พร้อมการตรวจสอบ ID และโทเค็นอย่างเข้มงวด
  * CSP ของการตอบกลับจาก Viewer: 
    * `default-src 'none'`
    * สคริปต์และแอสเซ็ตมาจาก self เท่านั้น
    * ไม่มี `connect-src` ขาออก
  * จำกัดความถี่ของ remote miss เมื่อเปิดใช้การเข้าถึงระยะไกล: 
    * ล้มเหลว 40 ครั้งต่อ 60 วินาที
    * ล็อกเอาต์ 60 วินาที (`429 Too Many Requests`)

การเสริมความปลอดภัยของการเรนเดอร์ไฟล์

  * การกำหนดเส้นทางคำขอเบราว์เซอร์สำหรับสกรีนช็อตเป็นแบบปฏิเสธโดยค่าเริ่มต้น
  * อนุญาตเฉพาะแอสเซ็ต Viewer ภายในเครื่องจาก `http://127.0.0.1/plugins/diffs/assets/*`
  * คำขอเครือข่ายภายนอกถูกบล็อก


## ข้อกำหนดของเบราว์เซอร์สำหรับโหมดไฟล์

`mode: "file"` และ `mode: "both"` ต้องใช้เบราว์เซอร์ที่เข้ากันได้กับ Chromium

ลำดับการแก้ไข:

* ### Config

`browser.executablePath` ในการกำหนดค่า OpenClaw

* ### ตัวแปรสภาพแวดล้อม

  * `OPENCLAW_BROWSER_EXECUTABLE_PATH`
  * `BROWSER_EXECUTABLE_PATH`
  * `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH`


* ### ทางเลือกสำรองของแพลตฟอร์ม

ทางเลือกสำรองสำหรับการค้นพบคำสั่ง/เส้นทางของแพลตฟอร์ม

ข้อความความล้มเหลวที่พบบ่อย:

  * `Diff PNG/PDF rendering requires a Chromium-compatible browser...`


แก้ไขโดยติดตั้ง Chrome, Chromium, Edge หรือ Brave หรือตั้งค่าหนึ่งในตัวเลือกเส้นทางไฟล์ปฏิบัติการด้านบน

## การแก้ไขปัญหา

ข้อผิดพลาดการตรวจสอบอินพุต

  * `Provide patch or both before and after text.` — ระบุทั้ง `before` และ `after` หรือระบุ `patch`
  * `Provide either patch or before/after input, not both.` — อย่าผสมโหมดอินพุต
  * `Invalid baseUrl: ...` — ใช้ origin แบบ `http(s)` พร้อม path ที่ไม่บังคับได้ ไม่มี query/hash
  * `{field} exceeds maximum size (...)` — ลดขนาด payload
  * การปฏิเสธแพตช์ขนาดใหญ่ — ลดจำนวนไฟล์แพตช์หรือจำนวนบรรทัดทั้งหมด

การเข้าถึง Viewer

  * URL ของ Viewer จะ resolve เป็น `127.0.0.1` โดยค่าเริ่มต้น
  * สำหรับสถานการณ์การเข้าถึงระยะไกล ให้ทำอย่างใดอย่างหนึ่ง: 
    * ตั้งค่า Plugin `viewerBaseUrl` หรือ
    * ส่ง `baseUrl` ต่อการเรียกเครื่องมือแต่ละครั้ง หรือ
    * ใช้ `gateway.bind=custom` และ `gateway.customBindHost`
  * หาก `gateway.trustedProxies` มี loopback สำหรับพร็อกซีโฮสต์เดียวกัน (ตัวอย่างเช่น Tailscale Serve) คำขอ Viewer แบบ raw loopback ที่ไม่มีส่วนหัว client-IP ที่ถูกส่งต่อมาจะล้มเหลวแบบ fail closed ตามการออกแบบ
  * สำหรับ topology ของพร็อกซีนั้น: 
    * ควรใช้ `mode: "file"` หรือ `mode: "both"` เมื่อคุณต้องการเพียงไฟล์แนบ หรือ
    * ตั้งใจเปิดใช้ `security.allowRemoteViewer` และตั้งค่า Plugin `viewerBaseUrl` หรือส่ง `baseUrl` ของพร็อกซี/สาธารณะ เมื่อคุณต้องการ URL ของ Viewer ที่แชร์ได้
  * เปิดใช้ `security.allowRemoteViewer` เฉพาะเมื่อคุณตั้งใจให้เข้าถึง Viewer จากภายนอก

แถวบรรทัดที่ไม่ได้แก้ไขไม่มีปุ่มขยาย

สิ่งนี้อาจเกิดขึ้นกับอินพุตแพตช์เมื่อแพตช์ไม่มีบริบทที่ขยายได้ นี่เป็นพฤติกรรมที่คาดไว้และไม่ได้บ่งชี้ว่า Viewer ล้มเหลว

ไม่พบอาร์ติแฟกต์

  * อาร์ติแฟกต์หมดอายุเนื่องจาก TTL
  * โทเค็นหรือเส้นทางเปลี่ยนไป
  * การล้างข้อมูลนำข้อมูลเก่าออกแล้ว


## คำแนะนำการดำเนินงาน

  * ควรใช้ `mode: "view"` สำหรับการรีวิวแบบโต้ตอบภายในเครื่องในแคนวาส
  * ควรใช้ `mode: "file"` สำหรับช่องแชตขาออกที่ต้องใช้ไฟล์แนบ
  * ปิดใช้ `allowRemoteViewer` ไว้ เว้นแต่การปรับใช้ของคุณต้องใช้ URL ของ Viewer ระยะไกล
  * ตั้งค่า `ttlSeconds` แบบสั้นอย่างชัดเจนสำหรับ diff ที่ละเอียดอ่อน
  * หลีกเลี่ยงการส่งข้อมูลลับในอินพุต diff เมื่อไม่จำเป็น
  * หากช่องของคุณบีบอัดรูปภาพอย่างรุนแรง (ตัวอย่างเช่น Telegram หรือ WhatsApp) ควรใช้เอาต์พุต PDF (`fileFormat: "pdf"`)


## ที่เกี่ยวข้อง

  * [เบราว์เซอร์](</th/tools/browser>)
  * [Plugin](</th/tools/plugin>)
  * [ภาพรวมเครื่องมือ](</th/tools>)


Was this useful?YesNo