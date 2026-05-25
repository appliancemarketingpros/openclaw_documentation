---
title: เริ่มต้นใช้งาน
source_url: https://docs.openclaw.ai/th/start/getting-started
scraped_at: 2026-05-25
---

ติดตั้ง OpenClaw, รันการตั้งค่าเริ่มต้น และแชตกับผู้ช่วย AI ของคุณ — ทั้งหมดนี้ใช้เวลา ประมาณ 5 นาที เมื่อจบแล้วคุณจะมี Gateway ที่ทำงานอยู่, auth ที่กำหนดค่าแล้ว, และเซสชันแชตที่ใช้งานได้

## สิ่งที่คุณต้องมี

  * **Node.js** — แนะนำ Node 24 (รองรับ Node 22.16+ ด้วย)
  * **คีย์ API** จากผู้ให้บริการโมเดล (Anthropic, OpenAI, Google ฯลฯ) — การตั้งค่าเริ่มต้นจะถามคุณ


## การตั้งค่าอย่างรวดเร็ว

* ### ติดตั้ง OpenClaw

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![กระบวนการสคริปต์ติดตั้ง](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### รันการตั้งค่าเริ่มต้น

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

วิซาร์ดจะแนะนำคุณตลอดการเลือกผู้ให้บริการโมเดล, การตั้งค่าคีย์ API, และการกำหนดค่า Gateway ใช้เวลาประมาณ 2 นาที

ดูข้อมูลอ้างอิงฉบับเต็มได้ที่ [การตั้งค่าเริ่มต้น (CLI)](</th/start/wizard>)

* ### ตรวจสอบว่า Gateway กำลังทำงาน

bashCopy code
[code]
    openclaw gateway status
[/code]

คุณควรเห็นว่า Gateway กำลังรับฟังที่พอร์ต 18789

* ### เปิดแดชบอร์ด

bashCopy code
[code]
    openclaw dashboard
[/code]

คำสั่งนี้จะเปิด Control UI ในเบราว์เซอร์ของคุณ หากโหลดได้ แสดงว่าทุกอย่างทำงานแล้ว

* ### ส่งข้อความแรกของคุณ

พิมพ์ข้อความในแชตของ Control UI แล้วคุณควรได้รับคำตอบจาก AI

อยากแชตจากโทรศัพท์แทนหรือไม่ ช่องทางที่ตั้งค่าได้เร็วที่สุดคือ [Telegram](</th/channels/telegram>) (ใช้แค่โทเค็นบอต) ดูตัวเลือกทั้งหมดที่ [ช่องทาง](</th/channels>)

ขั้นสูง: เมาต์บิลด์ Control UI แบบกำหนดเอง

หากคุณดูแลบิลด์แดชบอร์ดที่แปลภาษาหรือปรับแต่งเอง ให้ชี้ `gateway.controlUi.root` ไปยังไดเรกทอรีที่มี static assets ที่บิลด์แล้ว และ `index.html` ของคุณ

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

จากนั้นตั้งค่า:

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

รีสตาร์ต Gateway แล้วเปิดแดชบอร์ดอีกครั้ง:

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## ทำอะไรต่อไป

[**เชื่อมต่อช่องทาง** Discord, Feishu, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo และอื่น ๆ ](</th/channels>) [**การจับคู่และความปลอดภัย** ควบคุมว่าใครสามารถส่งข้อความถึงเอเจนต์ของคุณได้ ](</th/channels/pairing>) [**กำหนดค่า Gateway** โมเดล, เครื่องมือ, แซนด์บ็อกซ์ และการตั้งค่าขั้นสูง ](</th/gateway/configuration>) [**เรียกดูเครื่องมือ** เบราว์เซอร์, exec, การค้นหาเว็บ, Skills และ Plugin ](</th/tools>)

ขั้นสูง: ตัวแปรสภาพแวดล้อม

หากคุณรัน OpenClaw เป็นบัญชีบริการหรือต้องการพาธแบบกำหนดเอง:

  * `OPENCLAW_HOME` — ไดเรกทอรีหลักสำหรับการแก้ไขพาธภายใน
  * `OPENCLAW_STATE_DIR` — แทนที่ไดเรกทอรีสถานะ
  * `OPENCLAW_CONFIG_PATH` — แทนที่พาธไฟล์ config


ข้อมูลอ้างอิงฉบับเต็ม: [ตัวแปรสภาพแวดล้อม](</th/help/environment>)

## ที่เกี่ยวข้อง

  * [ภาพรวมการติดตั้ง](</th/install>)
  * [ภาพรวมช่องทาง](</th/channels>)
  * [การตั้งค่า](</th/start/setup>)


Was this useful?YesNo