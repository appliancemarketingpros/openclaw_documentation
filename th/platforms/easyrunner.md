---
title: EasyRunner
source_url: https://docs.openclaw.ai/th/platforms/easyrunner
scraped_at: 2026-06-29
---

PlatformsPlatforms overview

EasyRunner สามารถโฮสต์ OpenClaw Gateway เป็นแอปคอนเทนเนอร์ขนาดเล็กไว้หลังพร็อกซี Caddy ได้ คู่มือนี้ถือว่าคุณมีโฮสต์ EasyRunner ที่รันแอป Compose ที่เข้ากันได้กับ Podman และเปิดเผย HTTPS ผ่าน Caddy

## ก่อนเริ่มต้น

  * เซิร์ฟเวอร์ EasyRunner ที่มีโดเมนชี้มาหา
  * อิมเมจคอนเทนเนอร์ OpenClaw ที่ build แล้วหรือเผยแพร่แล้ว
  * วอลุ่มคอนฟิกถาวรสำหรับ `/home/node/.openclaw`
  * วอลุ่มเวิร์กสเปซถาวรสำหรับ `/workspace`
  * โทเค็นหรือรหัสผ่าน Gateway ที่รัดกุม


เปิดใช้งานการยืนยันตัวตนอุปกรณ์ไว้เมื่อทำได้ หากการปรับใช้ reverse proxy ของคุณไม่สามารถ ส่งต่อข้อมูลประจำตัวของอุปกรณ์ได้อย่างถูกต้อง ให้แก้การตั้งค่า trusted-proxy ก่อน ใช้ การข้ามการยืนยันตัวตนที่อันตรายเฉพาะกับเครือข่ายส่วนตัวเต็มรูปแบบที่ควบคุมโดยผู้ปฏิบัติงานเท่านั้น

## แอป Compose

สร้างแอป EasyRunner ด้วยไฟล์ Compose ที่มีรูปแบบดังนี้:

yamlCopy code
[code]
    services:  openclaw:    image: ghcr.io/openclaw/openclaw:latest    restart: unless-stopped    environment:      OPENCLAW_GATEWAY_TOKEN: ${OPENCLAW_GATEWAY_TOKEN}      OPENCLAW_HOME: /home/node      OPENCLAW_STATE_DIR: /home/node/.openclaw      OPENCLAW_CONFIG_PATH: /home/node/.openclaw/openclaw.json      OPENCLAW_WORKSPACE_DIR: /workspace    volumes:      - openclaw-config:/home/node/.openclaw      - openclaw-workspace:/workspace    labels:      caddy: openclaw.example.com      caddy.reverse_proxy: "{{upstreams 1455}}"    command: ["openclaw", "gateway", "--bind", "lan", "--port", "1455"] volumes:  openclaw-config:  openclaw-workspace:
[/code]

แทนที่ `openclaw.example.com` ด้วยชื่อโฮสต์ Gateway ของคุณ เก็บ `OPENCLAW_GATEWAY_TOKEN` ไว้ในตัวจัดการ secret/environment ของ EasyRunner แทนการ commit ลงในนิยามแอป

## กำหนดค่า OpenClaw

ภายในวอลุ่มคอนฟิกถาวร ให้ Gateway เข้าถึงได้ผ่าน พร็อกซีเท่านั้นและต้องมีการยืนยันตัวตน:

json5Copy code
[code]
    {  gateway: {    bind: "lan",    port: 1455,    auth: {      token: "${OPENCLAW_GATEWAY_TOKEN}",    },  },}
[/code]

หาก Caddy ยุติ TLS สำหรับ Gateway ให้กำหนดค่าการตั้งค่า trusted proxy สำหรับ เส้นทางพร็อกซีที่แน่นอน แทนการปิดใช้งานการตรวจสอบการยืนยันตัวตนแบบครอบคลุม ดู [การยืนยันตัวตน trusted proxy](</th/gateway/trusted-proxy-auth>)

## ตรวจสอบ

จากเวิร์กสเตชันของคุณ:

bashCopy code
[code]
    openclaw gateway probe --url https://openclaw.example.com --token <token>openclaw gateway status --url https://openclaw.example.com --token <token>
[/code]

จากโฮสต์ EasyRunner ให้ตรวจสอบบันทึกแอปเพื่อดูว่า Gateway กำลังฟังอยู่และไม่มี ข้อผิดพลาดการเริ่มต้นที่เกี่ยวกับ SecretRef, Plugin หรือการยืนยันตัวตนของช่องทาง

## การอัปเดตและการสำรองข้อมูล

  * ดึงหรือ build อิมเมจ OpenClaw ใหม่ แล้วปรับใช้แอป EasyRunner อีกครั้ง
  * สำรองวอลุ่ม `openclaw-config` ก่อนอัปเดต
  * สำรอง `openclaw-workspace` หาก agents เขียนข้อมูลโปรเจกต์ถาวรไว้ที่นั่น
  * รัน `openclaw doctor` หลังการอัปเดตครั้งใหญ่เพื่อตรวจจับการย้ายคอนฟิกและ คำเตือนของบริการ


## การแก้ไขปัญหา

  * `gateway probe` เชื่อมต่อไม่ได้: ยืนยันว่าชื่อโฮสต์ Caddy ชี้ไปที่แอป และคอนเทนเนอร์ฟังอยู่ที่ `0.0.0.0:1455`
  * การยืนยันตัวตนล้มเหลว: หมุนเวียนโทเค็นใน secrets ของ EasyRunner และคำสั่ง ไคลเอนต์ภายในเครื่องพร้อมกัน
  * ไฟล์เป็นของ root หลังการกู้คืน: ซ่อมแซมวอลุ่มที่เมานต์เพื่อให้ผู้ใช้ของ คอนเทนเนอร์เขียน `/home/node/.openclaw` และ `/workspace` ได้
  * Browser หรือ Plugin ช่องทางล้มเหลว: ตรวจสอบว่าไบนารีภายนอกที่จำเป็น การออกเครือข่าย และข้อมูลประจำตัวที่เมานต์ไว้พร้อมใช้งานภายใน คอนเทนเนอร์หรือไม่


Was this useful?YesNo

Open issue