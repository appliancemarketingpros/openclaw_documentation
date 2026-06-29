---
title: CLI ของ Workboard
source_url: https://docs.openclaw.ai/th/cli/workboard
scraped_at: 2026-06-29
---

ReferenceCLI commands

`openclaw workboard` คือพื้นผิวเทอร์มินัลสำหรับ [Plugin Workboard](</th/plugins/workboard>) ที่บันเดิลมาให้ ช่วยให้ผู้ปฏิบัติงานแสดงรายการการ์ด สร้าง การ์ด ตรวจสอบการ์ดหนึ่งใบ และสั่งให้ Gateway ที่กำลังทำงานอยู่ส่งงานที่พร้อมไปยัง การรัน worker ของ subagent ได้

เปิดใช้ Plugin ก่อนใช้คำสั่ง:

bashCopy code
[code]
    openclaw plugins enable workboardopenclaw gateway restart
[/code]

## การใช้งาน

bashCopy code
[code]
    openclaw workboard list [--board <id>] [--status <status>] [--include-archived] [--json]openclaw workboard create <title...> [--notes <text>] [--status <status>] [--priority <priority>] [--agent <id>] [--board <id>] [--labels <items>] [--json]openclaw workboard show <id> [--json]openclaw workboard dispatch [--url <url>] [--token <token>] [--timeout <ms>] [--json]
[/code]

คำสั่งนี้อ่านและเขียนฐานข้อมูล SQLite ที่ Plugin เป็นเจ้าของชุดเดียวกับที่ แดชบอร์ดและเครื่องมือเอเจนต์ Workboard ใช้ สามารถส่ง id ของการ์ดเป็น id เต็มหรือเป็น คำนำหน้าที่ไม่กำกวมได้เมื่อคำสั่งรองรับ id ของการ์ด

## `list`

bashCopy code
[code]
    openclaw workboard listopenclaw workboard list --board default --status readyopenclaw workboard list --json
[/code]

เอาต์พุตแบบข้อความมีรูปแบบกระชับ:

textCopy code
[code]
    7f4a2c10  ready     high    default agent-a  Fix stale worker heartbeat
[/code]

คอลัมน์คือคำนำหน้า id, สถานะ, ลำดับความสำคัญ, id ของบอร์ด, id ของเอเจนต์ที่อาจมี และชื่อเรื่อง

แฟล็ก:

แฟล็ก | วัตถุประสงค์  
---|---  
`--board <id>` | จำกัดผลลัพธ์ไว้ที่เนมสเปซของบอร์ดเดียว  
`--status <status>` | จำกัดผลลัพธ์ไว้ที่สถานะ Workboard หนึ่งสถานะ  
`--include-archived` | รวมการ์ดที่เก็บถาวรแล้วในเอาต์พุตข้อความแบบกระชับ  
`--json` | พิมพ์รายการการ์ดทั้งหมดเป็น JSON สำหรับเครื่อง  
  
โดยค่าเริ่มต้น เอาต์พุตข้อความแบบกระชับจะซ่อนการ์ดที่เก็บถาวรแล้ว เพื่อให้ CLI ตรงกับ คำสั่ง `/workboard list` ส่ง `--include-archived` เพื่อแสดงการ์ดเหล่านั้น เอาต์พุต JSON จะคงรายการการ์ดทั้งหมด รวมถึงการ์ดที่เก็บถาวรแล้ว สำหรับระบบอัตโนมัติที่มีอยู่

## `create`

bashCopy code
[code]
    openclaw workboard create "Fix stale worker heartbeat" --priority high --labels bug,workboardopenclaw workboard create "Write Workboard docs" --status ready --agent docs-agent --board docs --notes "Cover CLI, slash command, dispatch, and SQLite state."
[/code]

แฟล็ก:

แฟล็ก | วัตถุประสงค์  
---|---  
`--notes <text>` | บันทึกเริ่มต้นของการ์ด  
`--status <status>` | สถานะเริ่มต้น ค่าเริ่มต้นคือ `todo`  
`--priority <priority>` | ลำดับความสำคัญ ค่าเริ่มต้นคือ `normal`  
`--agent <id>` | มอบหมายการ์ดให้เอเจนต์หรือ id เจ้าของ  
`--board <id>` | จัดเก็บการ์ดไว้ในเนมสเปซของบอร์ด  
`--labels <items>` | ป้ายกำกับที่คั่นด้วยจุลภาค  
`--json` | พิมพ์การ์ดที่สร้างแล้วเป็น JSON สำหรับเครื่อง  
  
`create` เขียนไปยังสถานะ SQLite ของ Workboard โดยตรง การ์ดจะมองเห็นได้ทันที ในแท็บ Workboard ของ Control UI และในเครื่องมือ Workboard

## `show`

bashCopy code
[code]
    openclaw workboard show 7f4a2c10openclaw workboard show 7f4a2c10 --json
[/code]

เอาต์พุตข้อความจะพิมพ์บรรทัดการ์ดแบบกระชับและบันทึก เอาต์พุต JSON จะคืนค่าเรคอร์ด การ์ดแบบเต็ม รวมถึงเมทาดาทาการดำเนินการ ความพยายาม ความคิดเห็น ลิงก์ หลักฐาน อาร์ติแฟกต์ บันทึก worker สถานะโปรโตคอล การวินิจฉัย และเมทาดาทาระบบอัตโนมัติ

## `dispatch`

bashCopy code
[code]
    openclaw workboard dispatchopenclaw workboard dispatch --jsonopenclaw workboard dispatch --url http://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
[/code]

`dispatch` จะเรียกเมธอด RPC ของ Gateway ที่กำลังทำงานอยู่ `workboard.cards.dispatch` ก่อน เส้นทางนั้นใช้ runtime ของ subagent ชุดเดียวกับการกระทำ dispatch ในแดชบอร์ด ดังนั้นการ์ดที่พร้อมจะกลายเป็นการรัน worker ที่ติดตามเป็นงานพร้อม คีย์เซสชันที่เชื่อมโยงไว้ การ์ดที่มีเอเจนต์กำหนดไว้จะใช้คีย์เซสชัน subagent ตามขอบเขตเอเจนต์ ส่วนการ์ดที่ไม่ได้กำหนดเอเจนต์จะคงคีย์ subagent แบบไม่มีขอบเขตไว้ เพื่อให้คง เอเจนต์ค่าเริ่มต้นที่กำหนดไว้ของ Gateway

ลูป dispatch:

  1. เลื่อน children ที่ dependency พร้อมแล้วเป็น `ready`
  2. บล็อก claim ที่หมดอายุหรือการรัน worker ที่หมดเวลา
  3. บันทึกเมทาดาทา dispatch บนการ์ดที่พร้อม
  4. เลือกชุดเล็กของการ์ด `ready` ที่ยังไม่มี claim
  5. claim การ์ดที่เลือกแต่ละใบให้ dispatcher หรือเอเจนต์ที่กำหนดไว้
  6. เริ่มการรัน worker ของ subagent ด้วยบริบทการ์ดที่มีขอบเขตจำกัดและ token claim ของการ์ด
  7. จัดเก็บ id การรัน worker, คีย์เซสชัน, การเชื่อมโยงงานเมื่อบัญชีแยกประเภทงานของ Gateway รายงานมา, สถานะการดำเนินการ และบันทึก worker บนการ์ด


การคัดเลือกตั้งใจให้ระมัดระวัง โดยค่าเริ่มต้น dispatch หนึ่งครั้งจะเริ่ม worker ได้สูงสุดสามตัว ข้ามการ์ดที่เก็บถาวรหรือมี claim แล้ว และเริ่มเพียงการ์ดเดียวต่อเจ้าของหรือเอเจนต์ ในหนึ่งรอบ การ์ดที่มีเจ้าของเป็นงานที่กำลังรันหรืออยู่ระหว่างรีวิวอยู่แล้วจะถูกปล่อยไว้สำหรับ dispatch ภายหลัง

หากเริ่ม worker ไม่สำเร็จหลังจากการ์ดถูก claim แล้ว Workboard จะบล็อกการ์ดนั้น ล้าง claim และบันทึกความล้มเหลวไว้ในเมทาดาทาการดำเนินการของการ์ดและ worker-log วิธีนี้ทำให้การเริ่มที่ล้มเหลวมองเห็นได้ แทนที่จะส่งการ์ดกลับเข้าคิวอย่างเงียบ ๆ

หากไม่ได้ระบุเป้าหมาย Gateway อย่างชัดเจน และ Gateway ภายในเครื่องไม่พร้อมใช้งาน หรือยังไม่เปิดเผยเมธอด dispatch ของ Workboard CLI จะ fallback ไปใช้ dispatch เฉพาะข้อมูลกับสถานะ Workboard ภายในเครื่อง dispatch เฉพาะข้อมูลยังสามารถ เลื่อน dependency, ล้าง claim ค้าง และบล็อกการรันที่หมดเวลาได้ แต่จะ ไม่เริ่ม worker ความล้มเหลวด้าน auth, สิทธิ์, การตรวจสอบความถูกต้อง และความล้มเหลวสำหรับเป้าหมาย `--url` หรือ `--token` ที่ระบุชัดเจน จะถูกรายงานโดยตรง

เอาต์พุตข้อความรายงานการเริ่ม worker:

textCopy code
[code]
    dispatch complete: started=2 failures=0
[/code]

เอาต์พุต fallback ระบุอย่างชัดเจน:

textCopy code
[code]
    gateway unavailable; data dispatch only: promoted=1 blocked=0
[/code]

เอาต์พุต JSON มีผลลัพธ์ dispatch รวมอยู่ด้วย dispatch ที่มี Gateway รองรับอาจมี `started` และ `startFailures`; fallback เฉพาะข้อมูลมี `gatewayUnavailable: true` token claim จะถูกปกปิดจากเอาต์พุต JSON ของการ์ด

ในแดชบอร์ด ผลลัพธ์ dispatch ชุดเดียวกันจะแสดงเป็นสรุปสั้น ๆ เพื่อให้ ผู้ปฏิบัติงานเห็นได้ว่ามีการ์ดกี่ใบที่เริ่ม เลื่อนสถานะ บล็อก เรียกคืน หรือ ล้มเหลว โดยไม่ต้องเปิดรายละเอียดการ์ด

## ความเท่าเทียมของคำสั่ง Slash

ช่องทางที่รองรับคำสั่งสามารถใช้คำสั่ง slash ที่สอดคล้องกันได้:

textCopy code
[code]
    /workboard list/workboard show 7f4a2c10/workboard create Fix stale worker heartbeat/workboard dispatch
[/code]

dispatch ผ่านคำสั่ง slash ก็ใช้ runtime ของ subagent ใน Gateway เช่นกัน ดังนั้นจึงเป็นไปตาม พฤติกรรม claim, การเริ่ม worker และความล้มเหลวเดียวกับเส้นทาง Gateway ของแดชบอร์ดและ CLI

`/workboard list` และ `/workboard show` เป็นคำสั่งอ่านสำหรับผู้ส่งคำสั่งที่ได้รับอนุญาต `/workboard create` และ `/workboard dispatch` เปลี่ยนแปลงสถานะบอร์ดและ ต้องมีสถานะเจ้าของบนพื้นผิวแชต หรือเป็นไคลเอนต์ Gateway ที่มี `operator.write` หรือ `operator.admin`

## สิทธิ์

เส้นทาง dispatch ของ CLI เรียก RPC ของ Gateway ด้วย scope `operator.read` และ `operator.write` token Gateway แบบอ่านอย่างเดียวสามารถตรวจสอบข้อมูล Workboard ผ่านเมธอดอ่านได้ แต่ไม่สามารถสร้างการ์ดหรือ dispatch worker ได้

คำสั่ง `list`, `create` และ `show` ภายในเครื่องทำงานกับไดเรกทอรีสถานะ OpenClaw ภายในเครื่อง ที่โปรไฟล์ปัจจุบันใช้ ใช้ `--dev` หรือ `--profile <name>` บนคำสั่ง `openclaw` ระดับบนสุดเมื่อคุณต้องใช้รูทสถานะอื่น

## การแก้ไขปัญหา

### ไม่ปรากฏการ์ด

ยืนยันว่า Plugin เปิดใช้งานสำหรับโปรไฟล์และรูทสถานะเดียวกัน:

bashCopy code
[code]
    openclaw plugins inspect workboard --runtime --json
[/code]

หากแดชบอร์ดแสดงการ์ดแต่ CLI ไม่แสดง ให้ตรวจสอบว่าทั้งสองคำสั่งใช้ การตั้งค่า `--dev` หรือ `--profile` เดียวกัน

### Dispatch แจ้งว่าเป็นเฉพาะข้อมูล

เริ่มหรือรีสตาร์ท Gateway:

bashCopy code
[code]
    openclaw gateway restartopenclaw gateway status --deep
[/code]

จากนั้นลอง `openclaw workboard dispatch` อีกครั้ง fallback เฉพาะข้อมูลมีประโยชน์สำหรับการล้าง สถานะภายในเครื่อง แต่การรัน worker ต้องใช้ Gateway ที่ทำงานอยู่

### Dispatch ไม่เริ่มอะไรเลย

ตรวจสอบว่ามีการ์ด `ready` อย่างน้อยหนึ่งใบที่ไม่มี claim ที่ใช้งานอยู่:

bashCopy code
[code]
    openclaw workboard list --status ready
[/code]

การ์ดอาจถูกข้ามได้เช่นกันเมื่อเจ้าของเดียวกันมีงานที่กำลังรันหรืออยู่ระหว่างรีวิวอยู่แล้ว ย้ายงานที่เสร็จแล้วไปยัง `done`, ปล่อย claim ค้างผ่านเครื่องมือ Workboard หรือรัน dispatch อีกครั้งหลังจาก worker ที่ใช้งานอยู่เสร็จสิ้น

## ที่เกี่ยวข้อง

  * [Plugin Workboard](</th/plugins/workboard>)
  * [อ้างอิง CLI](</th/cli>)
  * [คำสั่ง Slash](</th/tools/slash-commands>)
  * [Control UI](</th/web/control-ui>)


Was this useful?YesNo

Open issue