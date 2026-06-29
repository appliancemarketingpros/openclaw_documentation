---
title: กล่อง Upstash
source_url: https://docs.openclaw.ai/th/install/upstash
scraped_at: 2026-06-29
---

InstallHosting

เรียกใช้ OpenClaw Gateway แบบถาวรบน Upstash Box ซึ่งเป็นสภาพแวดล้อม Linux แบบจัดการ พร้อมรองรับวงจรชีวิตแบบ keep-alive

ใช้ SSH tunnel สำหรับการเข้าถึงแดชบอร์ด อย่าเปิดเผยพอร์ต Gateway โดยตรง สู่สาธารณะบนอินเทอร์เน็ต

## ข้อกำหนดเบื้องต้น

  * บัญชี Upstash
  * Upstash Box แบบ keep-alive
  * ไคลเอนต์ SSH บนเครื่องภายในของคุณ


## สร้าง Box

สร้าง Box แบบ keep-alive ใน Upstash Console จด Box ID เช่น `right-flamingo-14486` และ Box API key ของคุณไว้

Upstash ดูแลคำแนะนำ OpenClaw Box ปัจจุบันไว้ที่ [การตั้งค่า OpenClaw](<https://upstash.com/docs/box/guides/openclaw-setup>)

## เชื่อมต่อด้วย SSH tunnel

ส่งต่อพอร์ตแดชบอร์ด OpenClaw มายังเครื่องภายในของคุณ ใช้ Box API key ของคุณ เป็นรหัสผ่าน SSH เมื่อระบบแจ้ง:

bashCopy code
[code]
    ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

ตัวเลือก keepalive ช่วยลดการหลุดของ tunnel เมื่อไม่ได้ใช้งานระหว่างการเริ่มต้นใช้งาน

## ติดตั้ง OpenClaw

ภายใน Box:

bashCopy code
[code]
    sudo npm install -g openclaw
[/code]

## เรียกใช้การเริ่มต้นใช้งาน

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

ทำตามพรอมป์ คัดลอก URL แดชบอร์ดและโทเค็นเมื่อการเริ่มต้นใช้งานเสร็จสิ้น

## เริ่ม Gateway

กำหนดค่า Gateway สำหรับเครือข่าย Box และเริ่มทำงานในเบื้องหลัง:

bashCopy code
[code]
    openclaw config set gateway.bind lannohup openclaw gateway > gateway.log 2>&1 &
[/code]

เมื่อ SSH tunnel ทำงานอยู่ ให้เปิด URL แดชบอร์ดในเครื่อง:

textCopy code
[code]
    http://127.0.0.1:18789/#token=<your-token>
[/code]

## รีสตาร์ทอัตโนมัติ

ตั้งค่าคำสั่งนี้เป็นสคริปต์เริ่มต้นของ Box เพื่อให้ Gateway รีสตาร์ทเมื่อ Box เริ่มทำงาน:

bashCopy code
[code]
    nohup openclaw gateway > gateway.log 2>&1 &
[/code]

## การแก้ไขปัญหา

หาก SSH ค้างระหว่างการเริ่มต้นใช้งาน ให้เชื่อมต่อใหม่ด้วยการกำหนดค่า SSH ที่สะอาดและ keepalives:

bashCopy code
[code]
    ssh -F /dev/null -o ControlMaster=no -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

วิธีนี้จะข้ามการตั้งค่า `~/.ssh/config` ภายในเครื่องที่ล้าสมัย และคงให้ tunnel ทำงานอยู่ ตลอดช่วงที่เครือข่ายไม่ได้ใช้งาน

## ที่เกี่ยวข้อง

  * [การเข้าถึงระยะไกล](</th/gateway/remote>)
  * [ความปลอดภัยของ Gateway](</th/gateway/security>)
  * [การอัปเดต OpenClaw](</th/install/updating>)


Was this useful?YesNo

Open issue