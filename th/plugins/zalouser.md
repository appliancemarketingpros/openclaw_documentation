---
title: Plugin ส่วนบุคคลของ Zalo
source_url: https://docs.openclaw.ai/th/plugins/zalouser
scraped_at: 2026-05-25
---

รองรับ Zalo Personal สำหรับ OpenClaw ผ่าน Plugin โดยใช้ `zca-js` แบบเนทีฟเพื่อทำงานอัตโนมัติกับบัญชีผู้ใช้ Zalo ปกติ

## การตั้งชื่อ

รหัสช่องทางคือ `zalouser` เพื่อระบุให้ชัดเจนว่าสิ่งนี้ทำงานอัตโนมัติกับ**บัญชีผู้ใช้ Zalo ส่วนบุคคล** (ไม่เป็นทางการ) เราสงวน `zalo` ไว้สำหรับการผสานรวม Zalo API อย่างเป็นทางการที่อาจมีในอนาคต

## ตำแหน่งที่ทำงาน

Plugin นี้ทำงาน**ภายในโปรเซส Gateway**

หากคุณใช้ Gateway ระยะไกล ให้ติดตั้ง/กำหนดค่าบน**เครื่องที่รัน Gateway** แล้วรีสตาร์ท Gateway

ไม่จำเป็นต้องมีไบนารี CLI ภายนอก `zca`/`openzca`

## ติดตั้ง

### ตัวเลือก A: ติดตั้งจาก npm

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

ใช้แพ็กเกจแบบไม่ระบุเวอร์ชันเพื่อติดตามแท็กรุ่นทางการปัจจุบัน ปักหมุดเวอร์ชันที่แน่นอน เฉพาะเมื่อคุณต้องการการติดตั้งที่ทำซ้ำได้เท่านั้น

รีสตาร์ท Gateway หลังจากนั้น

### ตัวเลือก B: ติดตั้งจากโฟลเดอร์ภายในเครื่อง (สำหรับพัฒนา)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

รีสตาร์ท Gateway หลังจากนั้น

## การกำหนดค่า

การกำหนดค่าช่องทางอยู่ภายใต้ `channels.zalouser` (ไม่ใช่ `plugins.entries.*`):

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## เครื่องมือ Agent

ชื่อเครื่องมือ: `zalouser`

การกระทำ: `send`, `image`, `link`, `friends`, `groups`, `me`, `status`

การกระทำข้อความช่องทางยังรองรับ `react` สำหรับการแสดงปฏิกิริยาต่อข้อความด้วย

## ที่เกี่ยวข้อง

  * [การสร้าง Plugin](</th/plugins/building-plugins>)
  * [ClawHub](</th/clawhub>)


Was this useful?YesNo