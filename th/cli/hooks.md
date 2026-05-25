---
title: ฮุก
source_url: https://docs.openclaw.ai/th/cli/hooks
scraped_at: 2026-05-25
---

# `openclaw hooks`

จัดการฮุกของเอเจนต์ (ระบบอัตโนมัติแบบขับเคลื่อนด้วยเหตุการณ์สำหรับคำสั่งอย่าง `/new`, `/reset` และการเริ่มต้น Gateway)

การรัน `openclaw hooks` โดยไม่มีคำสั่งย่อยจะเทียบเท่ากับ `openclaw hooks list`

ที่เกี่ยวข้อง:

  * ฮุก: [ฮุก](</th/automation/hooks>)
  * ฮุกของ Plugin: [ฮุกของ Plugin](</th/plugins/hooks>)


## แสดงฮุกทั้งหมด

bashCopy code
[code]
    openclaw hooks list
[/code]

แสดงฮุกทั้งหมดที่ค้นพบจากไดเรกทอรีเวิร์กสเปซ ไดเรกทอรีที่มีการจัดการ ไดเรกทอรีเพิ่มเติม และไดเรกทอรีที่รวมมาให้ การเริ่มต้น Gateway จะไม่โหลดตัวจัดการฮุกภายในจนกว่าจะมีการกำหนดค่าฮุกภายในอย่างน้อยหนึ่งรายการ

**ตัวเลือก:**

  * `--eligible`: แสดงเฉพาะฮุกที่ใช้งานได้ (ตรงตามข้อกำหนด)
  * `--json`: ส่งออกเป็น JSON
  * `-v, --verbose`: แสดงข้อมูลโดยละเอียดรวมถึงข้อกำหนดที่ขาดหายไป


**ตัวอย่างเอาต์พุต:**

CodeCopy code
[code]
    Hooks (4/4 ready) Ready:  🚀 boot-md ✓ - Run BOOT.md on gateway startup  📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap  📝 command-logger ✓ - Log all command events to a centralized audit file  💾 session-memory ✓ - Save session context to memory when /new or /reset command is issued
[/code]

**ตัวอย่าง (แบบละเอียด):**

bashCopy code
[code]
    openclaw hooks list --verbose
[/code]

แสดงข้อกำหนดที่ขาดหายไปสำหรับฮุกที่ยังใช้งานไม่ได้

**ตัวอย่าง (JSON):**

bashCopy code
[code]
    openclaw hooks list --json
[/code]

คืนค่า JSON ที่มีโครงสร้างสำหรับการใช้งานเชิงโปรแกรม

## ดูข้อมูลฮุก

bashCopy code
[code]
    openclaw hooks info <name>
[/code]

แสดงข้อมูลโดยละเอียดเกี่ยวกับฮุกเฉพาะรายการ

**อาร์กิวเมนต์:**

  * `<name>`: ชื่อฮุกหรือคีย์ฮุก (เช่น `session-memory`)


**ตัวเลือก:**

  * `--json`: ส่งออกเป็น JSON


**ตัวอย่าง:**

bashCopy code
[code]
    openclaw hooks info session-memory
[/code]

**เอาต์พุต:**

CodeCopy code
[code]
    💾 session-memory ✓ Ready Save session context to memory when /new or /reset command is issued Details:  Source: openclaw-bundled  Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md  Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts  Homepage: https://docs.openclaw.ai/automation/hooks#session-memory  Events: command:new, command:reset Requirements:  Config: ✓ workspace.dir
[/code]

## ตรวจสอบความพร้อมใช้งานของฮุก

bashCopy code
[code]
    openclaw hooks check
[/code]

แสดงสรุปสถานะความพร้อมใช้งานของฮุก (จำนวนที่พร้อมเทียบกับไม่พร้อม)

**ตัวเลือก:**

  * `--json`: ส่งออกเป็น JSON


**ตัวอย่างเอาต์พุต:**

CodeCopy code
[code]
    Hooks Status Total hooks: 4Ready: 4Not ready: 0
[/code]

## เปิดใช้งานฮุก

bashCopy code
[code]
    openclaw hooks enable <name>
[/code]

เปิดใช้งานฮุกเฉพาะรายการโดยเพิ่มลงในการกำหนดค่าของคุณ (ค่าเริ่มต้นคือ `~/.openclaw/openclaw.json`)

**หมายเหตุ:** ฮุกของเวิร์กสเปซจะถูกปิดใช้งานโดยค่าเริ่มต้นจนกว่าจะเปิดใช้งานที่นี่หรือในการกำหนดค่า ฮุกที่จัดการโดย Plugin จะแสดง `plugin:<id>` ใน `openclaw hooks list` และไม่สามารถเปิด/ปิดใช้งานได้ที่นี่ ให้เปิด/ปิดใช้งาน Plugin แทน

**อาร์กิวเมนต์:**

  * `<name>`: ชื่อฮุก (เช่น `session-memory`)


**ตัวอย่าง:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**เอาต์พุต:**

CodeCopy code
[code]
    ✓ Enabled hook: 💾 session-memory
[/code]

**สิ่งที่คำสั่งนี้ทำ:**

  * ตรวจสอบว่าฮุกมีอยู่และใช้งานได้
  * อัปเดต `hooks.internal.entries.<name>.enabled = true` ในการกำหนดค่าของคุณ
  * บันทึกการกำหนดค่าลงดิสก์


หากฮุกมาจาก `<workspace>/hooks/` ขั้นตอนการเลือกเปิดใช้งานนี้จำเป็นก่อนที่ Gateway จะโหลดฮุกนั้น

**หลังจากเปิดใช้งาน:**

  * รีสตาร์ท Gateway เพื่อให้ฮุกโหลดใหม่ (รีสตาร์ทแอปบนแถบเมนูใน macOS หรือรีสตาร์ทกระบวนการ Gateway ของคุณในโหมดพัฒนา)


## ปิดใช้งานฮุก

bashCopy code
[code]
    openclaw hooks disable <name>
[/code]

ปิดใช้งานฮุกเฉพาะรายการโดยอัปเดตการกำหนดค่าของคุณ

**อาร์กิวเมนต์:**

  * `<name>`: ชื่อฮุก (เช่น `command-logger`)


**ตัวอย่าง:**

bashCopy code
[code]
    openclaw hooks disable command-logger
[/code]

**เอาต์พุต:**

CodeCopy code
[code]
    ⏸ Disabled hook: 📝 command-logger
[/code]

**หลังจากปิดใช้งาน:**

  * รีสตาร์ท Gateway เพื่อให้ฮุกโหลดใหม่


## หมายเหตุ

  * `openclaw hooks list --json`, `info --json` และ `check --json` เขียน JSON ที่มีโครงสร้างไปยัง stdout โดยตรง
  * ฮุกที่จัดการโดย Plugin ไม่สามารถเปิดหรือปิดใช้งานได้ที่นี่ ให้เปิดหรือปิดใช้งาน Plugin ที่เป็นเจ้าของแทน


## ติดตั้งชุดฮุก

bashCopy code
[code]
    openclaw plugins install <package>        # npm by defaultopenclaw plugins install npm:<package>    # npm onlyopenclaw plugins install <package> --pin  # pin versionopenclaw plugins install <path>           # local path
[/code]

ติดตั้งชุดฮุกผ่านตัวติดตั้ง plugins แบบรวมศูนย์

`openclaw hooks install` ยังคงทำงานในฐานะชื่อแทนเพื่อความเข้ากันได้ แต่จะแสดง คำเตือนการเลิกใช้และส่งต่อไปยัง `openclaw plugins install`

สเปก npm เป็นแบบ **registry-only** (ชื่อแพ็กเกจ + **เวอร์ชันที่แน่นอน** หรือ **dist-tag** ที่เลือกได้) สเปก Git/URL/file และช่วง semver จะถูกปฏิเสธ การติดตั้ง dependency จะรันแบบภายในโปรเจกต์พร้อม `--ignore-scripts` เพื่อความปลอดภัย แม้ว่า shell ของคุณจะมีการตั้งค่าการติดตั้ง npm แบบโกลบอลก็ตาม

สเปกเปล่าและ `@latest` จะอยู่บนสายเสถียร หาก npm resolve รายการใดรายการหนึ่ง ไปเป็น prerelease OpenClaw จะหยุดและขอให้คุณเลือกเข้าร่วมอย่างชัดเจนด้วยแท็ก prerelease เช่น `@beta`/`@rc` หรือเวอร์ชัน prerelease ที่แน่นอน

**สิ่งที่คำสั่งนี้ทำ:**

  * คัดลอกชุดฮุกไปยัง `~/.openclaw/hooks/<id>`
  * เปิดใช้งานฮุกที่ติดตั้งใน `hooks.internal.entries.*`
  * บันทึกการติดตั้งไว้ภายใต้ `hooks.internal.installs`


**ตัวเลือก:**

  * `-l, --link`: ลิงก์ไดเรกทอรีภายในเครื่องแทนการคัดลอก (เพิ่มลงใน `hooks.internal.load.extraDirs`)
  * `--pin`: บันทึกการติดตั้ง npm เป็น `name@version` ที่ resolve แล้วแบบแน่นอนใน `hooks.internal.installs`


**อาร์ไคฟ์ที่รองรับ:** `.zip`, `.tgz`, `.tar.gz`, `.tar`

**ตัวอย่าง:**

bashCopy code
[code]
    # Local directoryopenclaw plugins install ./my-hook-pack # Local archiveopenclaw plugins install ./my-hook-pack.zip # NPM packageopenclaw plugins install @openclaw/my-hook-pack # Link a local directory without copyingopenclaw plugins install -l ./my-hook-pack
[/code]

ชุดฮุกที่ลิงก์ไว้จะถูกถือว่าเป็นฮุกที่มีการจัดการจากไดเรกทอรีที่โอเปอเรเตอร์กำหนดค่า ไม่ใช่ฮุกของเวิร์กสเปซ

## อัปเดตชุดฮุก

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins update --all
[/code]

อัปเดตชุดฮุกที่ติดตามอยู่และอิงตาม npm ผ่านตัวอัปเดต plugins แบบรวมศูนย์

`openclaw hooks update` ยังคงทำงานในฐานะชื่อแทนเพื่อความเข้ากันได้ แต่จะแสดง คำเตือนการเลิกใช้และส่งต่อไปยัง `openclaw plugins update`

**ตัวเลือก:**

  * `--all`: อัปเดตชุดฮุกทั้งหมดที่ติดตามอยู่
  * `--dry-run`: แสดงสิ่งที่จะเปลี่ยนแปลงโดยไม่เขียนข้อมูล


เมื่อมีแฮช integrity ที่จัดเก็บไว้และแฮชของอาร์ติแฟกต์ที่ดึงมาเปลี่ยนไป OpenClaw จะแสดงคำเตือนและขอการยืนยันก่อนดำเนินการต่อ ใช้ `--yes` แบบโกลบอลเพื่อข้ามพรอมต์ใน CI/การรันแบบไม่โต้ตอบ

## ฮุกที่รวมมาให้

### session-memory

บันทึกบริบทเซสชันลงในหน่วยความจำเมื่อคุณออกคำสั่ง `/new` หรือ `/reset`

**เปิดใช้งาน:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**เอาต์พุต:** ค่าเริ่มต้นคือ `~/.openclaw/workspace/memory/YYYY-MM-DD-HHMM.md` ตั้งค่า `hooks.internal.entries.session-memory.llmSlug: true` สำหรับ slug ชื่อไฟล์ที่สร้างโดยโมเดล

**ดู:** [เอกสาร session-memory](</th/automation/hooks#session-memory>)

### bootstrap-extra-files

แทรกไฟล์ bootstrap เพิ่มเติม (เช่น `AGENTS.md` / `TOOLS.md` ภายใน monorepo) ระหว่าง `agent:bootstrap`

**เปิดใช้งาน:**

bashCopy code
[code]
    openclaw hooks enable bootstrap-extra-files
[/code]

**ดู:** [เอกสาร bootstrap-extra-files](</th/automation/hooks#bootstrap-extra-files>)

### command-logger

บันทึกเหตุการณ์คำสั่งทั้งหมดลงในไฟล์ audit แบบรวมศูนย์

**เปิดใช้งาน:**

bashCopy code
[code]
    openclaw hooks enable command-logger
[/code]

**เอาต์พุต:** `~/.openclaw/logs/commands.log`

**ดูบันทึก:**

bashCopy code
[code]
    # Recent commandstail -n 20 ~/.openclaw/logs/commands.log # Pretty-printcat ~/.openclaw/logs/commands.log | jq . # Filter by actiongrep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
[/code]

**ดู:** [เอกสาร command-logger](</th/automation/hooks#command-logger>)

### boot-md

รัน `BOOT.md` เมื่อ Gateway เริ่มทำงาน (หลังจาก channels เริ่มทำงาน)

**เหตุการณ์** : `gateway:startup`

**เปิดใช้งาน** :

bashCopy code
[code]
    openclaw hooks enable boot-md
[/code]

**ดู:** [เอกสาร boot-md](</th/automation/hooks#boot-md>)

## ที่เกี่ยวข้อง

  * [อ้างอิง CLI](</th/cli>)
  * [ฮุกอัตโนมัติ](</th/automation/hooks>)


Was this useful?YesNo