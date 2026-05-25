---
title: Plugin WhatsApp
source_url: https://docs.openclaw.ai/th/plugins/reference/whatsapp
scraped_at: 2026-05-25
---

# Plugin WhatsApp

เพิ่มพื้นผิวช่องทาง WhatsApp สำหรับส่งและรับข้อความ OpenClaw

## การเผยแพร่

  * แพ็กเกจ: `@openclaw/whatsapp`
  * เส้นทางการติดตั้ง: npm; ClawHub


## พื้นผิว

channels: whatsapp

## หมายเหตุการติดตั้งบน Windows

บน Windows, Plugin WhatsApp ต้องใช้ Git บน `PATH` ระหว่างการติดตั้ง npm เพราะหนึ่งใน dependency ของ Baileys/libsignal ถูกดึงมาจาก URL ของ git ติดตั้ง Git for Windows จากนั้นรีสตาร์ท shell แล้วเรียกใช้การติดตั้งอีกครั้ง:

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

Portable Git ใช้งานได้เช่นกันหากไดเรกทอรี `bin` ของมันอยู่บน `PATH`

## เอกสารที่เกี่ยวข้อง

  * [whatsapp](</th/channels/whatsapp>)


Was this useful?YesNo