---
title: Completion
source_url: https://docs.openclaw.ai/th/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

สร้างสคริปต์ shell completion และเลือกติดตั้งลงในโปรไฟล์ shell ของคุณได้

## การใช้งาน

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## ตัวเลือก

  * `-s, --shell <shell>`: shell เป้าหมาย (`zsh`, `bash`, `powershell`, `fish`; ค่าเริ่มต้น: `zsh`)
  * `-i, --install`: ติดตั้ง completion โดยเพิ่มบรรทัด source ลงในโปรไฟล์ shell ของคุณ
  * `--write-state`: เขียนสคริปต์ completion ลงใน `$OPENCLAW_STATE_DIR/completions` โดยไม่พิมพ์ไปยัง stdout
  * `-y, --yes`: ข้ามข้อความยืนยันการติดตั้ง


## หมายเหตุ

  * `--install` จะเขียนบล็อก "OpenClaw Completion" ขนาดเล็กลงในโปรไฟล์ shell ของคุณ และชี้ไปยังสคริปต์ที่แคชไว้
  * หากไม่ใช้ `--install` หรือ `--write-state` คำสั่งจะพิมพ์สคริปต์ไปยัง stdout
  * การสร้าง completion จะโหลดโครงสร้างคำสั่งแบบ eager เพื่อให้รวม subcommands ที่ซ้อนอยู่ด้วย


## ที่เกี่ยวข้อง

  * [CLI reference](</th/cli>)


Was this useful?YesNo