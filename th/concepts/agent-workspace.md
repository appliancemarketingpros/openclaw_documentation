---
title: พื้นที่ทำงานของเอเจนต์
source_url: https://docs.openclaw.ai/th/concepts/agent-workspace
scraped_at: 2026-05-25
---

พื้นที่ทำงานคือบ้านของเอเจนต์ เป็นไดเรกทอรีทำงานเดียวที่ใช้สำหรับเครื่องมือไฟล์และบริบทพื้นที่ทำงาน เก็บไว้เป็นส่วนตัวและปฏิบัติต่อมันเหมือนหน่วยความจำ

สิ่งนี้แยกจาก `~/.openclaw/` ซึ่งใช้เก็บการกำหนดค่า ข้อมูลประจำตัว และเซสชัน

## ตำแหน่งเริ่มต้น

  * ค่าเริ่มต้น: `~/.openclaw/workspace`
  * หากตั้งค่า `OPENCLAW_PROFILE` และไม่ใช่ `"default"` ค่าเริ่มต้นจะกลายเป็น `~/.openclaw/workspace-<profile>`
  * แทนที่ใน `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

`openclaw onboard`, `openclaw configure` หรือ `openclaw setup` จะสร้างพื้นที่ทำงานและใส่ไฟล์บูตสแตรปเริ่มต้นให้ หากไฟล์เหล่านั้นหายไป

หากคุณจัดการไฟล์พื้นที่ทำงานด้วยตัวเองอยู่แล้ว คุณสามารถปิดการสร้างไฟล์บูตสแตรปได้:

json5Copy code
[code]
    { agents: { defaults: { skipBootstrap: true } } }
[/code]

## โฟลเดอร์พื้นที่ทำงานเพิ่มเติม

การติดตั้งเก่าอาจเคยสร้าง `~/openclaw` ไว้ การเก็บไดเรกทอรีพื้นที่ทำงานหลายชุดไว้อาจทำให้ข้อมูลยืนยันตัวตนหรือสถานะคลาดเคลื่อนจนสับสนได้ เพราะมีพื้นที่ทำงานที่ใช้งานอยู่ได้เพียงชุดเดียวในแต่ละครั้ง

## แผนผังไฟล์พื้นที่ทำงาน

ต่อไปนี้คือไฟล์มาตรฐานที่ OpenClaw คาดว่าจะพบภายในพื้นที่ทำงาน:

AGENTS.md - คำสั่งการปฏิบัติงาน

คำสั่งการปฏิบัติงานสำหรับเอเจนต์และวิธีที่เอเจนต์ควรใช้หน่วยความจำ โหลดเมื่อเริ่มทุกเซสชัน เหมาะสำหรับกฎ ลำดับความสำคัญ และรายละเอียด "วิธีปฏิบัติตัว"

SOUL.md - บุคลิกและโทน

บุคลิก โทน และขอบเขต โหลดทุกเซสชัน คู่มือ: [คู่มือบุคลิกภาพ SOUL.md](</th/concepts/soul>)

USER.md - ผู้ใช้คือใคร

ผู้ใช้คือใครและควรเรียกพวกเขาอย่างไร โหลดทุกเซสชัน

IDENTITY.md - ชื่อ บรรยากาศ อีโมจิ

ชื่อ บรรยากาศ และอีโมจิของเอเจนต์ สร้าง/อัปเดตระหว่างพิธีบูตสแตรป

TOOLS.md - ข้อตกลงของเครื่องมือโลคัล

หมายเหตุเกี่ยวกับเครื่องมือและข้อตกลงโลคัลของคุณ ไม่ได้ควบคุมความพร้อมใช้งานของเครื่องมือ เป็นเพียงคำแนะนำเท่านั้น

HEARTBEAT.md - เช็กลิสต์ Heartbeat

เช็กลิสต์ขนาดเล็กที่เป็นทางเลือกสำหรับการรัน Heartbeat ควรทำให้สั้นเพื่อหลีกเลี่ยงการใช้โทเค็นมากเกินไป

BOOT.md - เช็กลิสต์เริ่มต้น

เช็กลิสต์เริ่มต้นที่เป็นทางเลือก ซึ่งรันอัตโนมัติเมื่อ Gateway รีสตาร์ต (เมื่อเปิดใช้ [ฮุกภายใน](</th/automation/hooks>)) ควรทำให้สั้น ใช้เครื่องมือข้อความสำหรับการส่งออก

BOOTSTRAP.md - พิธีรันครั้งแรก

พิธีรันครั้งแรกแบบครั้งเดียว สร้างเฉพาะสำหรับพื้นที่ทำงานใหม่เอี่ยม ลบทิ้งหลังจากพิธีเสร็จสมบูรณ์

memory/YYYY-MM-DD.md - บันทึกหน่วยความจำรายวัน

บันทึกหน่วยความจำรายวัน (หนึ่งไฟล์ต่อวัน) แนะนำให้อ่านของวันนี้ + เมื่อวานเมื่อเริ่มเซสชัน

MEMORY.md - หน่วยความจำระยะยาวที่คัดสรรแล้ว (ทางเลือก)

หน่วยความจำระยะยาวที่คัดสรรแล้ว: ข้อเท็จจริงที่คงทน ความชอบ การตัดสินใจ และสรุปสั้น ๆ เก็บบันทึกรายละเอียดไว้ใน `memory/YYYY-MM-DD.md` เพื่อให้เครื่องมือหน่วยความจำดึงมาใช้เมื่อต้องการได้ โดยไม่ต้องแทรกเข้าไปในทุก prompt โหลด `MEMORY.md` เฉพาะในเซสชันหลักแบบส่วนตัวเท่านั้น (ไม่ใช่บริบทที่แชร์/กลุ่ม) ดู [หน่วยความจำ](</th/concepts/memory>) สำหรับเวิร์กโฟลว์และการล้างหน่วยความจำอัตโนมัติ

skills/ - Skills ของพื้นที่ทำงาน (ทางเลือก)

Skills เฉพาะพื้นที่ทำงาน ตำแหน่ง Skill ที่มีลำดับความสำคัญสูงสุดสำหรับพื้นที่ทำงานนั้น แทนที่ Skills ของเอเจนต์โปรเจกต์, Skills ของเอเจนต์ส่วนตัว, Skills ที่จัดการ, Skills ที่บันเดิลมา และ `skills.load.extraDirs` เมื่อชื่อชนกัน

canvas/ - ไฟล์ Canvas UI (ทางเลือก)

ไฟล์ Canvas UI สำหรับการแสดงผลโหนด (เช่น `canvas/index.html`)

## สิ่งที่ไม่ได้อยู่ในพื้นที่ทำงาน

สิ่งเหล่านี้อยู่ใต้ `~/.openclaw/` และไม่ควร commit ไปยัง repo ของพื้นที่ทำงาน:

  * `~/.openclaw/openclaw.json` (การกำหนดค่า)
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` (โปรไฟล์การยืนยันตัวตนของโมเดล: OAuth + API keys)
  * `~/.openclaw/agents/<agentId>/agent/codex-home/` (บัญชีรันไทม์ Codex รายเอเจนต์ การกำหนดค่า Skills, plugins และสถานะเธรด native)
  * `~/.openclaw/credentials/` (สถานะช่องทาง/ผู้ให้บริการ รวมถึงข้อมูลนำเข้า OAuth เดิม)
  * `~/.openclaw/agents/<agentId>/sessions/` (ทรานสคริปต์เซสชัน + เมทาดาตา)
  * `~/.openclaw/skills/` (Skills ที่จัดการ)


หากคุณต้องย้ายเซสชันหรือการกำหนดค่า ให้คัดลอกแยกต่างหากและเก็บไว้นอกการควบคุมเวอร์ชัน

## การสำรองข้อมูลด้วย Git (แนะนำ, ส่วนตัว)

ปฏิบัติต่อพื้นที่ทำงานเหมือนหน่วยความจำส่วนตัว ใส่ไว้ใน repo git แบบ **ส่วนตัว** เพื่อให้มีข้อมูลสำรองและกู้คืนได้

รันขั้นตอนเหล่านี้บนเครื่องที่ Gateway รันอยู่ (ซึ่งเป็นที่ที่พื้นที่ทำงานอยู่)

* ### เริ่มต้น repo

หากติดตั้ง git แล้ว พื้นที่ทำงานใหม่เอี่ยมจะถูกเริ่มต้นโดยอัตโนมัติ หากพื้นที่ทำงานนี้ยังไม่ใช่ repo ให้รัน:

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md memory/git commit -m "Add agent workspace"
[/code]

* ### เพิ่ม remote ส่วนตัว

### GitHub web UI

  1. สร้าง repository **ส่วนตัว** ใหม่บน GitHub
  2. อย่าเริ่มต้นด้วย README (เพื่อหลีกเลี่ยง merge conflicts)
  3. คัดลอก HTTPS remote URL
  4. เพิ่ม remote และ push:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

### GitHub CLI (gh)

bashCopy code
[code]
    gh auth logingh repo create openclaw-workspace --private --source . --remote origin --push
[/code]

### GitLab web UI

  1. สร้าง repository **ส่วนตัว** ใหม่บน GitLab
  2. อย่าเริ่มต้นด้วย README (เพื่อหลีกเลี่ยง merge conflicts)
  3. คัดลอก HTTPS remote URL
  4. เพิ่ม remote และ push:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

* ### การอัปเดตต่อเนื่อง

bashCopy code
[code]
    git statusgit add .git commit -m "Update memory"git push
[/code]

## อย่า commit ความลับ

ตัวอย่างเริ่มต้น `.gitignore` ที่แนะนำ:

gitignoreCopy code
[code]
    .DS_Store.env**/*.key**/*.pem**/secrets*
[/code]

## การย้ายพื้นที่ทำงานไปยังเครื่องใหม่

* ### Clone repo

Clone repo ไปยังพาธที่ต้องการ (ค่าเริ่มต้น `~/.openclaw/workspace`)

* ### อัปเดตการกำหนดค่า

ตั้งค่า `agents.defaults.workspace` เป็นพาธนั้นใน `~/.openclaw/openclaw.json`

* ### Seed ไฟล์ที่หายไป

รัน `openclaw setup --workspace <path>` เพื่อ seed ไฟล์ที่หายไป

* ### คัดลอกเซสชัน (ทางเลือก)

หากคุณต้องใช้เซสชัน ให้คัดลอก `~/.openclaw/agents/<agentId>/sessions/` จากเครื่องเก่าแยกต่างหาก

## หมายเหตุขั้นสูง

  * การกำหนดเส้นทางแบบหลายเอเจนต์สามารถใช้พื้นที่ทำงานที่ต่างกันต่อเอเจนต์ได้ ดู [การกำหนดเส้นทางช่องทาง](</th/channels/channel-routing>) สำหรับการกำหนดค่าการกำหนดเส้นทาง
  * หากเปิดใช้ `agents.defaults.sandbox` เซสชันที่ไม่ใช่ main สามารถใช้พื้นที่ทำงานแซนด์บ็อกซ์รายเซสชันใต้ `agents.defaults.sandbox.workspaceRoot`


## ที่เกี่ยวข้อง

  * [Heartbeat](</th/gateway/heartbeat>) \- ไฟล์พื้นที่ทำงาน [HEARTBEAT.md](<http://HEARTBEAT.md>)
  * [แซนด์บ็อกซ์](</th/gateway/sandboxing>) \- การเข้าถึงพื้นที่ทำงานในสภาพแวดล้อมที่เป็นแซนด์บ็อกซ์
  * [เซสชัน](</th/concepts/session>) \- พาธที่เก็บเซสชัน
  * [คำสั่งประจำ](</th/automation/standing-orders>) \- คำสั่งถาวรในไฟล์พื้นที่ทำงาน


Was this useful?YesNo