---
title: กุ้งมังกร
source_url: https://docs.openclaw.ai/th/tools/lobster
scraped_at: 2026-05-25
---

Lobster คือเชลล์เวิร์กโฟลว์ที่ช่วยให้ OpenClaw เรียกใช้ลำดับเครื่องมือหลายขั้นตอนเป็นการดำเนินการเดียวที่กำหนดผลลัพธ์ได้แน่นอน พร้อมจุดตรวจสอบการอนุมัติที่ชัดเจน

Lobster เป็นเลเยอร์การเขียนที่อยู่เหนือการทำงานเบื้องหลังแบบแยกตัว สำหรับการจัดการโฟลว์เหนือระดับงานแต่ละรายการ ดู [Task Flow](</th/automation/taskflow>) (`openclaw tasks flow`) สำหรับบัญชีกิจกรรมของงาน ดู [`openclaw tasks`](</th/automation/tasks>)

## Hook

ผู้ช่วยของคุณสามารถสร้างเครื่องมือที่จัดการตัวมันเองได้ ขอเวิร์กโฟลว์ แล้ว 30 นาทีต่อมาคุณจะได้ CLI พร้อมไปป์ไลน์ที่ทำงานเป็นการเรียกครั้งเดียว Lobster คือส่วนที่ขาดหายไป: ไปป์ไลน์ที่กำหนดผลลัพธ์ได้แน่นอน การอนุมัติที่ชัดเจน และสถานะที่กลับมาทำต่อได้

## เหตุผล

ปัจจุบัน เวิร์กโฟลว์ที่ซับซ้อนต้องใช้การเรียกเครื่องมือโต้ตอบกลับไปกลับมาหลายครั้ง การเรียกแต่ละครั้งใช้โทเค็น และ LLM ต้องจัดการทุกขั้นตอน Lobster ย้ายการจัดการนั้นไปไว้ในรันไทม์ที่มีชนิดข้อมูลชัดเจน:

  * **เรียกครั้งเดียวแทนหลายครั้ง** : OpenClaw เรียกเครื่องมือ Lobster หนึ่งครั้งและได้ผลลัพธ์แบบมีโครงสร้าง
  * **มีการอนุมัติในตัว** : ผลข้างเคียง (ส่งอีเมล โพสต์ความคิดเห็น) จะหยุดเวิร์กโฟลว์จนกว่าจะได้รับการอนุมัติอย่างชัดเจน
  * **กลับมาทำต่อได้** : เวิร์กโฟลว์ที่หยุดไว้จะส่งคืนโทเค็น อนุมัติแล้วทำต่อได้โดยไม่ต้องเรียกซ้ำทุกอย่าง


## ทำไมต้องใช้ DSL แทนโปรแกรมทั่วไป?

Lobster ตั้งใจให้มีขนาดเล็ก เป้าหมายไม่ใช่ "ภาษาใหม่" แต่เป็นสเปกไปป์ไลน์ที่คาดเดาได้ เป็นมิตรกับ AI พร้อมการอนุมัติและโทเค็นสำหรับกลับมาทำต่อเป็นองค์ประกอบหลัก

  * **อนุมัติ/กลับมาทำต่อมีในตัว** : โปรแกรมปกติสามารถขอให้มนุษย์ยืนยันได้ แต่ไม่สามารถ _หยุดชั่วคราวแล้วกลับมาทำต่อ_ ด้วยโทเค็นที่คงทนได้ เว้นแต่คุณจะสร้างรันไทม์นั้นเอง
  * **ความกำหนดผลลัพธ์ได้แน่นอน + ตรวจสอบย้อนหลังได้** : ไปป์ไลน์เป็นข้อมูล จึงบันทึก เปรียบเทียบ เล่นซ้ำ และตรวจทานได้ง่าย
  * **พื้นผิวที่จำกัดสำหรับ AI** : ไวยากรณ์ขนาดเล็ก + การส่งต่อ JSON ลดเส้นทางโค้ดแบบ "สร้างสรรค์" และทำให้การตรวจสอบความถูกต้องทำได้จริง
  * **นโยบายความปลอดภัยฝังอยู่ในตัว** : การหมดเวลา ขีดจำกัดเอาต์พุต การตรวจสอบแซนด์บ็อกซ์ และ allowlist ถูกบังคับใช้โดยรันไทม์ ไม่ใช่สคริปต์แต่ละตัว
  * **ยังเขียนโปรแกรมได้** : แต่ละขั้นตอนสามารถเรียก CLI หรือสคริปต์ใดก็ได้ หากต้องการ JS/TS ให้สร้างไฟล์ `.lobster` จากโค้ด


## วิธีทำงาน

OpenClaw เรียกใช้เวิร์กโฟลว์ Lobster **ในโปรเซสเดียวกัน** โดยใช้ตัวรันแบบฝัง ไม่มีการสร้างซับโปรเซส CLI ภายนอก เครื่องยนต์เวิร์กโฟลว์จะทำงานภายในโปรเซส Gateway และส่งคืนซอง JSON โดยตรง หากไปป์ไลน์หยุดเพื่อรอการอนุมัติ เครื่องมือจะส่งคืน `resumeToken` เพื่อให้คุณดำเนินการต่อภายหลังได้

## รูปแบบ: CLI ขนาดเล็ก + JSON pipe + การอนุมัติ

สร้างคำสั่งขนาดเล็กที่สื่อสารด้วย JSON แล้วเชื่อมต่อเข้าด้วยกันเป็นการเรียก Lobster ครั้งเดียว (ชื่อตัวอย่างคำสั่งด้านล่าง - เปลี่ยนเป็นของคุณเองได้)

bashCopy code
[code]
    inbox list --jsoninbox categorize --jsoninbox apply --json
[/code]

jsonCopy code
[code]
    {  "action": "run",  "pipeline": "exec --json --shell 'inbox list --json' | exec --stdin json --shell 'inbox categorize --json' | exec --stdin json --shell 'inbox apply --json' | approve --preview-from-stdin --limit 5 --prompt 'Apply changes?'",  "timeoutMs": 30000}
[/code]

หากไปป์ไลน์ขอการอนุมัติ ให้กลับมาทำต่อด้วยโทเค็น:

jsonCopy code
[code]
    {  "action": "resume",  "token": "<resumeToken>",  "approve": true}
[/code]

AI เรียกเวิร์กโฟลว์; Lobster ดำเนินการตามขั้นตอน เกตการอนุมัติทำให้ผลข้างเคียงชัดเจนและตรวจสอบย้อนหลังได้

ตัวอย่าง: แมปรายการอินพุตเป็นการเรียกเครื่องมือ:

bashCopy code
[code]
    gog.gmail.search --query 'newer_than:1d' \  | openclaw.invoke --tool message --action send --each --item-key message --args-json '{"provider":"telegram","to":"..."}'
[/code]

## ขั้นตอน LLM แบบ JSON เท่านั้น (llm-task)

สำหรับเวิร์กโฟลว์ที่ต้องมี **ขั้นตอน LLM แบบมีโครงสร้าง** ให้เปิดใช้เครื่องมือ Plugin เสริม `llm-task` แล้วเรียกจาก Lobster วิธีนี้ทำให้เวิร์กโฟลว์ยังคงกำหนดผลลัพธ์ได้แน่นอน แต่ยังให้คุณจัดประเภท/สรุป/ร่างข้อความด้วยโมเดลได้

เปิดใช้เครื่องมือ:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": { "enabled": true }    }  },  "agents": {    "list": [      {        "id": "main",        "tools": { "alsoAllow": ["llm-task"] }      }    ]  }}
[/code]

### ข้อจำกัดสำคัญ: Lobster แบบฝังเทียบกับ `openclaw.invoke`

Plugin Lobster ที่รวมมาในชุดจะเรียกใช้เวิร์กโฟลว์ **ในโปรเซสเดียวกัน** ภายใน Gateway ในโหมดฝังนี้ `openclaw.invoke` จะ **ไม่** สืบทอด URL ของ Gateway/บริบทการยืนยันตัวตนโดยอัตโนมัติสำหรับการเรียกเครื่องมือ OpenClaw CLI แบบซ้อน

นั่นหมายความว่ารูปแบบนี้ **ยังไม่น่าเชื่อถือในตัวรันแบบฝังในปัจจุบัน** :

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{ ... }'
[/code]

ใช้ตัวอย่างด้านล่างเฉพาะเมื่อเรียกใช้ **Lobster CLI แบบสแตนด์อโลน** ในสภาพแวดล้อมที่ `openclaw.invoke` ได้รับการกำหนดค่าด้วยบริบท Gateway/การยืนยันตัวตนที่ถูกต้องแล้ว

ใช้ในไปป์ไลน์ Lobster CLI แบบสแตนด์อโลน:

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{  "prompt": "Given the input email, return intent and draft.",  "thinking": "low",  "input": { "subject": "Hello", "body": "Can you help?" },  "schema": {    "type": "object",    "properties": {      "intent": { "type": "string" },      "draft": { "type": "string" }    },    "required": ["intent", "draft"],    "additionalProperties": false  }}'
[/code]

หากคุณใช้ Plugin Lobster แบบฝังในปัจจุบัน ให้เลือกใช้หนึ่งในวิธีต่อไปนี้:

  * เรียกเครื่องมือ `llm-task` โดยตรงนอก Lobster หรือ
  * ใช้ขั้นตอนที่ไม่ใช่ `openclaw.invoke` ภายในไปป์ไลน์ Lobster จนกว่าจะเพิ่มบริดจ์แบบฝังที่รองรับ


ดูรายละเอียดและตัวเลือกการกำหนดค่าได้ที่ [LLM Task](</th/tools/llm-task>)

## ไฟล์เวิร์กโฟลว์ (.lobster)

Lobster สามารถเรียกใช้ไฟล์เวิร์กโฟลว์ YAML/JSON ที่มีฟิลด์ `name`, `args`, `steps`, `env`, `condition` และ `approval` ได้ ในการเรียกเครื่องมือ OpenClaw ให้ตั้งค่า `pipeline` เป็นพาธไฟล์

yamlCopy code
[code]
    name: inbox-triageargs:  tag:    default: "family"steps:  - id: collect    command: inbox list --json  - id: categorize    command: inbox categorize --json    stdin: $collect.stdout  - id: approve    command: inbox apply --approve    stdin: $categorize.stdout    approval: required  - id: execute    command: inbox apply --execute    stdin: $categorize.stdout    condition: $approve.approved
[/code]

หมายเหตุ:

  * `stdin: $step.stdout` และ `stdin: $step.json` ส่งเอาต์พุตของขั้นตอนก่อนหน้า
  * `condition` (หรือ `when`) สามารถใช้เป็นเกตขั้นตอนตาม `$step.approved`


## ติดตั้ง Lobster

เวิร์กโฟลว์ Lobster ที่รวมมาในชุดจะทำงานในโปรเซสเดียวกัน ไม่จำเป็นต้องมีไบนารี `lobster` แยกต่างหาก ตัวรันแบบฝังมาพร้อมกับ Plugin Lobster

หากคุณต้องการ Lobster CLI แบบสแตนด์อโลนสำหรับการพัฒนาหรือไปป์ไลน์ภายนอก ให้ติดตั้งจาก [รีโป Lobster](<https://github.com/openclaw/lobster>) และตรวจสอบให้แน่ใจว่า `lobster` อยู่ใน `PATH`

## เปิดใช้เครื่องมือ

Lobster เป็นเครื่องมือ Plugin **เสริม** (ไม่ได้เปิดใช้โดยค่าเริ่มต้น)

แนะนำ (เพิ่มเข้าไปได้อย่างปลอดภัย):

jsonCopy code
[code]
    {  "tools": {    "alsoAllow": ["lobster"]  }}
[/code]

หรือกำหนดต่อเอเจนต์:

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "tools": {          "alsoAllow": ["lobster"]        }      }    ]  }}
[/code]

หลีกเลี่ยงการใช้ `tools.allow: ["lobster"]` เว้นแต่คุณตั้งใจจะทำงานในโหมด allowlist แบบจำกัด

## ตัวอย่าง: การคัดแยกอีเมล

เมื่อไม่มี Lobster:

CodeCopy code
[code]
    User: "Check my email and draft replies"→ openclaw calls gmail.list→ LLM summarizes→ User: "draft replies to #2 and #5"→ LLM drafts→ User: "send #2"→ openclaw calls gmail.send(repeat daily, no memory of what was triaged)
[/code]

เมื่อใช้ Lobster:

jsonCopy code
[code]
    {  "action": "run",  "pipeline": "email.triage --limit 20",  "timeoutMs": 30000}
[/code]

ส่งคืนซอง JSON (ตัดทอนแล้ว):

jsonCopy code
[code]
    {  "ok": true,  "status": "needs_approval",  "output": [{ "summary": "5 need replies, 2 need action" }],  "requiresApproval": {    "type": "approval_request",    "prompt": "Send 2 draft replies?",    "items": [],    "resumeToken": "..."  }}
[/code]

ผู้ใช้อนุมัติ → กลับมาทำต่อ:

jsonCopy code
[code]
    {  "action": "resume",  "token": "<resumeToken>",  "approve": true}
[/code]

หนึ่งเวิร์กโฟลว์ กำหนดผลลัพธ์ได้แน่นอน ปลอดภัย

## พารามิเตอร์ของเครื่องมือ

### `run`

เรียกใช้ไปป์ไลน์ในโหมดเครื่องมือ

jsonCopy code
[code]
    {  "action": "run",  "pipeline": "gog.gmail.search --query 'newer_than:1d' | email.triage",  "cwd": "workspace",  "timeoutMs": 30000,  "maxStdoutBytes": 512000}
[/code]

เรียกใช้ไฟล์เวิร์กโฟลว์พร้อมอาร์กิวเมนต์:

jsonCopy code
[code]
    {  "action": "run",  "pipeline": "/path/to/inbox-triage.lobster",  "argsJson": "{\"tag\":\"family\"}"}
[/code]

### `resume`

ทำเวิร์กโฟลว์ที่หยุดไว้ต่อหลังการอนุมัติ

jsonCopy code
[code]
    {  "action": "resume",  "token": "<resumeToken>",  "approve": true}
[/code]

### อินพุตเสริม

  * `cwd`: ไดเรกทอรีทำงานแบบสัมพัทธ์สำหรับไปป์ไลน์ (ต้องอยู่ภายในไดเรกทอรีทำงานของ Gateway)
  * `timeoutMs`: ยกเลิกเวิร์กโฟลว์หากเกินระยะเวลานี้ (ค่าเริ่มต้น: 20000)
  * `maxStdoutBytes`: ยกเลิกเวิร์กโฟลว์หากเอาต์พุตเกินขนาดนี้ (ค่าเริ่มต้น: 512000)
  * `argsJson`: สตริง JSON ที่ส่งให้ `lobster run --args-json` (เฉพาะไฟล์เวิร์กโฟลว์)


## ซองเอาต์พุต

Lobster ส่งคืนซอง JSON พร้อมหนึ่งในสามสถานะ:

  * `ok` → เสร็จสิ้นสำเร็จ
  * `needs_approval` → หยุดชั่วคราว; ต้องใช้ `requiresApproval.resumeToken` เพื่อกลับมาทำต่อ
  * `cancelled` → ถูกปฏิเสธหรือยกเลิกอย่างชัดเจน


เครื่องมือแสดงซองทั้งใน `content` (JSON แบบจัดรูปแบบสวยงาม) และ `details` (ออบเจกต์ดิบ)

## การอนุมัติ

หากมี `requiresApproval` ให้ตรวจสอบพรอมป์แล้วตัดสินใจ:

  * `approve: true` → กลับมาทำต่อและดำเนินผลข้างเคียงต่อไป
  * `approve: false` → ยกเลิกและจบเวิร์กโฟลว์


ใช้ `approve --preview-from-stdin --limit N` เพื่อแนบตัวอย่าง JSON กับคำขออนุมัติโดยไม่ต้องใช้ jq/heredoc แบบกำหนดเอง โทเค็นสำหรับกลับมาทำต่อมีขนาดกะทัดรัดแล้ว: Lobster เก็บสถานะการกลับมาทำต่อของเวิร์กโฟลว์ไว้ใต้ไดเรกทอรีสถานะของตัวเองและส่งคืนคีย์โทเค็นขนาดเล็ก

## OpenProse

OpenProse ทำงานร่วมกับ Lobster ได้ดี: ใช้ `/prose` เพื่อจัดการการเตรียมงานแบบหลายเอเจนต์ แล้วเรียกไปป์ไลน์ Lobster สำหรับการอนุมัติที่กำหนดผลลัพธ์ได้แน่นอน หากโปรแกรม Prose ต้องใช้ Lobster ให้อนุญาตเครื่องมือ `lobster` สำหรับเอเจนต์ย่อยผ่าน `tools.subagents.tools` ดู [OpenProse](</th/prose>)

## ความปลอดภัย

  * **เฉพาะในโปรเซสเดียวกันแบบโลคัล** \- เวิร์กโฟลว์ทำงานภายในโปรเซส Gateway; ไม่มีการเรียกเครือข่ายจากตัว Plugin เอง
  * **ไม่มีความลับ** \- Lobster ไม่จัดการ OAuth; มันเรียกเครื่องมือ OpenClaw ที่จัดการเรื่องนั้น
  * **รับรู้แซนด์บ็อกซ์** \- ปิดใช้งานเมื่อบริบทเครื่องมืออยู่ในแซนด์บ็อกซ์
  * **เสริมความแข็งแรงแล้ว** \- ตัวรันแบบฝังบังคับใช้การหมดเวลาและขีดจำกัดเอาต์พุต


## การแก้ไขปัญหา

  * **`lobster timed out`** → เพิ่ม `timeoutMs` หรือแยกไปป์ไลน์ยาวออกเป็นส่วนๆ
  * **`lobster output exceeded maxStdoutBytes`** → เพิ่ม `maxStdoutBytes` หรือลดขนาดเอาต์พุต
  * **`lobster returned invalid JSON`** → ตรวจสอบให้แน่ใจว่าไปป์ไลน์ทำงานในโหมดเครื่องมือและพิมพ์เฉพาะ JSON
  * **`lobster failed`** → ตรวจสอบล็อก Gateway สำหรับรายละเอียดข้อผิดพลาดของตัวรันแบบฝัง


## เรียนรู้เพิ่มเติม

  * [Plugins](</th/tools/plugin>)
  * [การเขียนเครื่องมือ Plugin](</th/plugins/building-plugins#registering-agent-tools>)


## กรณีศึกษา: เวิร์กโฟลว์ชุมชน

ตัวอย่างสาธารณะหนึ่งรายการ: CLI "สมองที่สอง" + ไปป์ไลน์ Lobster ที่จัดการคลัง Markdown สามแห่ง (ส่วนตัว คู่ชีวิต ใช้ร่วมกัน) CLI ส่งออก JSON สำหรับสถิติ รายการกล่องขาเข้า และการสแกนรายการค้างเก่า; Lobster เชื่อมคำสั่งเหล่านั้นเป็นเวิร์กโฟลว์ เช่น `weekly-review`, `inbox-triage`, `memory-consolidation` และ `shared-task-sync` โดยแต่ละรายการมีเกตการอนุมัติ AI จัดการการตัดสินใจ (การจัดหมวดหมู่) เมื่อพร้อมใช้งาน และถอยกลับไปใช้กฎที่กำหนดผลลัพธ์ได้แน่นอนเมื่อไม่พร้อม

  * เธรด: <https://x.com/plattenschieber/status/2014508656335770033>
  * รีโป: <https://github.com/bloomedai/brain-cli>


## ที่เกี่ยวข้อง

  * [Automation](</th/automation>) \- การตั้งเวลาเวิร์กโฟลว์ Lobster
  * [ภาพรวม Automation](</th/automation>) \- กลไกอัตโนมัติทั้งหมด
  * [ภาพรวมเครื่องมือ](</th/tools>) \- เครื่องมือเอเจนต์ทั้งหมดที่พร้อมใช้งาน


Was this useful?YesNo