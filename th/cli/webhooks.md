---
title: Webhook
source_url: https://docs.openclaw.ai/th/cli/webhooks
scraped_at: 2026-05-25
---

# `openclaw webhooks`

ตัวช่วยและการผสานรวม Webhook ปัจจุบันพื้นผิวนี้จำกัดขอบเขตไว้ที่โฟลว์ Gmail Pub/Sub ที่ผสานรวมกับตัวเฝ้าดู `gog` ที่บันเดิลมา

## คำสั่งย่อย

bashCopy code
[code]
    openclaw webhooks gmail setup --account <email> [...]openclaw webhooks gmail run   [--account <email>] [...]
[/code]

คำสั่งย่อย | คำอธิบาย  
---|---  
`gmail setup` | กำหนดค่า Gmail watch, หัวข้อ/การสมัครรับ Pub/Sub และเป้าหมายการส่ง Webhook ของ OpenClaw  
`gmail run` | เรียกใช้ `gog watch serve` พร้อมลูปต่ออายุ watch อัตโนมัติ  
  
## `webhooks gmail setup`

กำหนดค่า Gmail watch, Pub/Sub และการส่ง Webhook ของ OpenClaw

bashCopy code
[code]
    openclaw webhooks gmail setup --account you@example.comopenclaw webhooks gmail setup --account you@example.com --project my-gcp-project --jsonopenclaw webhooks gmail setup --account you@example.com --hook-url https://gateway.example.com/hooks/gmail
[/code]

### จำเป็น

แฟล็ก | คำอธิบาย  
---|---  
`--account <email>` | บัญชี Gmail ที่ต้องการเฝ้าดู  
  
### ตัวเลือก Pub/Sub

แฟล็ก | ค่าเริ่มต้น | คำอธิบาย  
---|---|---  
`--project <id>` | (ไม่มี) | รหัสโปรเจกต์ GCP (เจ้าของไคลเอนต์ OAuth)  
`--topic <name>` | `gog-gmail-watch` | ชื่อหัวข้อ Pub/Sub  
`--subscription <name>` | `gog-gmail-watch-push` | ชื่อการสมัครรับ Pub/Sub  
`--label <label>` | `INBOX` | ป้ายกำกับ Gmail ที่ต้องการเฝ้าดู  
`--push-endpoint <url>` | (ไม่มี) | ปลายทาง push ของ Pub/Sub แบบระบุชัดเจน แทนที่ Tailscale  
  
### ตัวเลือกการส่งของ OpenClaw

แฟล็ก | ค่าเริ่มต้น | คำอธิบาย  
---|---|---  
`--hook-url <url>` | (ไม่มี) | URL ของ Webhook ของ OpenClaw  
`--hook-token <token>` | (ไม่มี) | โทเค็น Webhook ของ OpenClaw  
`--push-token <token>` | (ไม่มี) | โทเค็น push ที่ส่งต่อไปยัง `gog watch serve`  
  
### ตัวเลือก `gog watch serve`

แฟล็ก | ค่าเริ่มต้น | คำอธิบาย  
---|---|---  
`--bind <host>` | `127.0.0.1` | โฮสต์ bind ของ `gog watch serve`  
`--port <port>` | `8788` | พอร์ตของ `gog watch serve`  
`--path <path>` | `/gmail-pubsub` | พาธของ `gog watch serve`  
`--include-body` | `true` | รวมตัวอย่างเนื้อหาอีเมล ส่ง `--no-include-body` เพื่อปิดใช้งาน  
`--max-bytes <n>` | `20000` | จำนวนไบต์สูงสุดต่อหนึ่งตัวอย่างเนื้อหา  
`--renew-minutes <n>` | `720` (12h) | ต่ออายุ Gmail watch ทุก N นาที  
  
### การเปิดให้เข้าถึงผ่าน Tailscale

แฟล็ก | ค่าเริ่มต้น | คำอธิบาย  
---|---|---  
`--tailscale <mode>` | `funnel` | เปิดเผยปลายทาง push ผ่าน tailscale: `funnel`, `serve` หรือ `off`  
`--tailscale-path <path>` | (ไม่มี) | พาธสำหรับ tailscale serve/funnel  
`--tailscale-target <t>` | (ไม่มี) | เป้าหมาย Tailscale serve/funnel (พอร์ต, `host:port` หรือ URL)  
  
### เอาต์พุต

แฟล็ก | คำอธิบาย  
---|---  
`--json` | พิมพ์สรุปที่เครื่องอ่านได้แทนข้อความ  
  
## `webhooks gmail run`

เรียกใช้ `gog watch serve` พร้อมลูปต่ออายุ watch อัตโนมัติใน foreground

bashCopy code
[code]
    openclaw webhooks gmail run --account you@example.com
[/code]

`run` ยอมรับแฟล็ก `gog watch serve`, การส่งของ OpenClaw, Pub/Sub และ Tailscale เหมือนกับ `setup` ยกเว้น:

  * `--account` เป็น **ตัวเลือก** บน `run` (จะย้อนกลับไปใช้บัญชีที่กำหนดค่าไว้)
  * `run` **ไม่** ยอมรับ `--project`, `--push-endpoint` หรือ `--json`
  * แฟล็กของ `run` ไม่มีค่าเริ่มต้นในตัว ค่าที่หายไปจะย้อนกลับไปใช้ค่าที่ `setup` เขียนไว้

หมวดหมู่ | แฟล็ก  
---|---  
Pub/Sub | `--account`, `--topic`, `--subscription`, `--label`  
การส่งของ OpenClaw | `--hook-url`, `--hook-token`, `--push-token`  
`gog watch serve` | `--bind`, `--port`, `--path`, `--include-body`, `--max-bytes`, `--renew-minutes`  
Tailscale | `--tailscale`, `--tailscale-path`, `--tailscale-target`  
  
## โฟลว์ตั้งแต่ต้นจนจบ

ดู [การผสานรวม Gmail Pub/Sub](</th/automation/cron-jobs#gmail-pubsub-integration>) สำหรับการตั้งค่าโปรเจกต์ GCP, OAuth และฝั่ง Gateway ที่ใช้คู่กับคำสั่ง CLI เหล่านี้

## ที่เกี่ยวข้อง

  * [ข้อมูลอ้างอิง CLI](</th/cli>)
  * [ระบบอัตโนมัติของ Webhook](</th/automation/cron-jobs>)
  * [Gmail Pub/Sub](</th/automation/cron-jobs#gmail-pubsub-integration>)


Was this useful?YesNo