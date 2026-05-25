---
title: เอกสาร
source_url: https://docs.openclaw.ai/th/cli/docs
scraped_at: 2026-05-25
---

# `openclaw docs`

ค้นหาดัชนีเอกสาร OpenClaw แบบสดจากเทอร์มินัล คำสั่งนี้เรียกใช้ปลายทางค้นหา MCP ของเอกสารสาธารณะที่โฮสต์บน Mintlify ที่ `https://docs.openclaw.ai/mcp.SearchOpenClaw` แล้วแสดงผลลัพธ์ในเทอร์มินัลของคุณ

## การใช้งาน

bashCopy code
[code]
    openclaw docs                       # print docs entrypoint and example searchopenclaw docs <query...>            # search the live docs index
[/code]

อาร์กิวเมนต์:

อาร์กิวเมนต์ | คำอธิบาย  
---|---  
`[query...]` | คำค้นหาแบบอิสระ คำค้นหาหลายคำจะถูกรวมด้วยช่องว่างและส่งเป็นรายการเดียว  
  
## ตัวอย่าง

bashCopy code
[code]
    openclaw docs browser existing-sessionopenclaw docs sandbox allowHostControlopenclaw docs gateway token secretref
[/code]

เมื่อไม่มีคำค้นหา `openclaw docs` จะพิมพ์ URL จุดเข้าเอกสารพร้อมคำสั่งค้นหาตัวอย่าง แทนที่จะเรียกใช้การค้นหา

## วิธีทำงาน

`openclaw docs` เรียกใช้ CLI `mcporter` เพื่อเรียกเครื่องมือค้นหา MCP ของเอกสาร จากนั้นแยกวิเคราะห์บล็อก `Title: / Link: / Content:` จากเอาต์พุตของเครื่องมือให้เป็นรายการผลลัพธ์

เพื่อระบุ `mcporter` OpenClaw จะตรวจสอบตามลำดับ:

  1. `mcporter` บน `PATH` (ใช้โดยตรงหากมี)
  2. `pnpm dlx mcporter ...` หากติดตั้ง `pnpm` แล้ว
  3. `npx -y mcporter ...` หากติดตั้ง `npx` แล้ว


หากไม่มีรายการใดพร้อมใช้งาน คำสั่งจะล้มเหลวพร้อมคำแนะนำให้ติดตั้ง `pnpm` (`npm install -g pnpm`)

การเรียกค้นหาใช้ระยะหมดเวลาคงที่ 30 วินาที ตัวอย่างข้อความของผลลัพธ์จะถูกตัดให้เหลือประมาณ 220 อักขระต่อรายการ

## เอาต์พุต

ในเทอร์มินัลแบบสมบูรณ์ (TTY) ผลลัพธ์จะแสดงเป็นหัวข้อตามด้วยรายการสัญลักษณ์หัวข้อย่อย แต่ละหัวข้อย่อยจะแสดงชื่อหน้า, URL เอกสารที่ลิงก์ไว้ และตัวอย่างข้อความสั้นในบรรทัดถัดไป ผลลัพธ์ว่างจะพิมพ์ว่า "ไม่พบผลลัพธ์."

ในเอาต์พุตแบบไม่สมบูรณ์ (ผ่าน pipe, `--no-color`, สคริปต์) ข้อมูลเดียวกันจะแสดงเป็น Markdown:

markdownCopy code
[code]
    # Docs search: <query> - [Title](https://docs.openclaw.ai/...) - snippet- [Title](https://docs.openclaw.ai/...) - snippet
[/code]

## รหัสออก

รหัส | ความหมาย  
---|---  
`0` | การค้นหาสำเร็จ (รวมถึงการตอบกลับที่ไม่มีผลลัพธ์)  
`1` | การเรียกเครื่องมือ MCP ล้มเหลว; `stderr` ถูกพิมพ์แบบอินไลน์  
  
## ที่เกี่ยวข้อง

  * [ข้อมูลอ้างอิง CLI](</th/cli>)
  * [เอกสารแบบสด](<https://docs.openclaw.ai>)


Was this useful?YesNo