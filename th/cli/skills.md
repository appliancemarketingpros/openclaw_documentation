---
title: Skills
source_url: https://docs.openclaw.ai/th/cli/skills
scraped_at: 2026-05-25
---

# `openclaw skills`

ตรวจสอบ Skills ในเครื่อง และติดตั้ง/อัปเดต Skills จาก ClawHub

ที่เกี่ยวข้อง:

  * ระบบ Skills: [Skills](</th/tools/skills>)
  * การกำหนดค่า Skills: [Skills config](</th/tools/skills-config>)
  * การติดตั้ง ClawHub: [ClawHub](</th/clawhub/cli>)


## คำสั่ง

bashCopy code
[code]
    openclaw skills search "calendar"openclaw skills search --limit 20 --jsonopenclaw skills install <slug>openclaw skills install <slug> --version <version>openclaw skills install <slug> --forceopenclaw skills install <slug> --agent <id>openclaw skills update <slug>openclaw skills update --allopenclaw skills update --all --agent <id>openclaw skills listopenclaw skills list --eligibleopenclaw skills list --jsonopenclaw skills list --verboseopenclaw skills list --agent <id>openclaw skills info <name>openclaw skills info <name> --jsonopenclaw skills info <name> --agent <id>openclaw skills checkopenclaw skills check --agent <id>openclaw skills check --json
[/code]

`search`/`install`/`update` ใช้ ClawHub โดยตรง และติดตั้งลงในไดเรกทอรี `skills/` ของเวิร์กสเปซที่ใช้งานอยู่ `list`/`info`/`check` ยังคงตรวจสอบ Skills ในเครื่องที่มองเห็นได้สำหรับเวิร์กสเปซและการกำหนดค่าปัจจุบัน คำสั่งที่มี เวิร์กสเปซรองรับจะระบุเวิร์กสเปซเป้าหมายจาก `--agent <id>` จากนั้นจึงใช้ไดเรกทอรี ทำงานปัจจุบันเมื่ออยู่ภายในเวิร์กสเปซของเอเจนต์ที่กำหนดค่าไว้ แล้วจึงใช้เอเจนต์ เริ่มต้น

คำสั่ง CLI `install` นี้ดาวน์โหลดโฟลเดอร์ Skills จาก ClawHub การติดตั้ง การพึ่งพาของ Skills ที่รองรับโดย Gateway ซึ่งถูกทริกเกอร์จากการเริ่มใช้งานหรือ การตั้งค่า Skills จะใช้เส้นทางคำขอ `skills.install` แยกต่างหากแทน

หมายเหตุ:

  * `search [query...]` รับคำค้นหาที่ไม่บังคับ ระบุได้; ละไว้เพื่อเรียกดูฟีดค้นหา ClawHub เริ่มต้น
  * `search --limit <n>` จำกัดจำนวนผลลัพธ์ที่ส่งกลับ
  * `install --force` เขียนทับโฟลเดอร์ Skills ของเวิร์กสเปซที่มีอยู่สำหรับ slug เดียวกัน
  * `--agent <id>` กำหนดเป้าหมายไปยังเวิร์กสเปซของเอเจนต์ที่กำหนดค่าไว้หนึ่งรายการ และแทนที่การอนุมานจากไดเรกทอรีทำงานปัจจุบัน
  * `update --all` อัปเดตเฉพาะการติดตั้ง ClawHub ที่ถูกติดตามในเวิร์กสเปซที่ใช้งานอยู่
  * `check --agent <id>` ตรวจสอบเวิร์กสเปซของเอเจนต์ที่เลือก และรายงานว่า Skills ที่พร้อมใช้งานใดมองเห็นได้จริงบนพื้นผิวพรอมป์หรือคำสั่งของเอเจนต์นั้น
  * `list` เป็นการดำเนินการเริ่มต้นเมื่อไม่ได้ระบุคำสั่งย่อย
  * `list`, `info` และ `check` เขียนเอาต์พุตที่เรนเดอร์แล้วไปยัง stdout เมื่อใช้ `--json` หมายความว่าเพย์โหลดที่เครื่องอ่านได้จะคงอยู่บน stdout สำหรับไพป์ และสคริปต์


## ที่เกี่ยวข้อง

  * [CLI reference](</th/cli>)
  * [Skills](</th/tools/skills>)


Was this useful?YesNo