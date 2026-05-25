---
title: สถานะสุขภาพ
source_url: https://docs.openclaw.ai/th/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

ดึงข้อมูลสถานะสุขภาพจาก Gateway ที่กำลังทำงานอยู่

## ตัวเลือก

แฟล็ก | ค่าเริ่มต้น | คำอธิบาย  
---|---|---  
`--json` | `false` | พิมพ์ JSON ที่เครื่องอ่านได้แทนข้อความ  
`--timeout <ms>` | `10000` | ระยะหมดเวลาการเชื่อมต่อเป็นมิลลิวินาที  
`--verbose` | `false` | การบันทึกแบบละเอียด บังคับให้ตรวจสอบแบบสดและขยายเอาต์พุตรายเอเจนต์  
`--debug` | `false` | นามแฝงสำหรับ `--verbose`  
  
ตัวอย่าง:

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

หมายเหตุ:

  * ค่าเริ่มต้น `openclaw health` จะถาม Gateway ที่กำลังทำงานอยู่เพื่อขอสแนปช็อตสถานะสุขภาพ เมื่อ Gateway มีสแนปช็อตที่แคชไว้และยังสดอยู่แล้ว ก็สามารถส่งคืนเพย์โหลดที่แคชไว้นั้นและ รีเฟรชในเบื้องหลังได้
  * `--verbose` บังคับให้ตรวจสอบแบบสด พิมพ์รายละเอียดการเชื่อมต่อ Gateway และขยาย เอาต์พุตที่มนุษย์อ่านได้สำหรับบัญชีและเอเจนต์ทั้งหมดที่กำหนดค่าไว้
  * เอาต์พุตรวม session store รายเอเจนต์เมื่อกำหนดค่าเอเจนต์หลายตัว


## ที่เกี่ยวข้อง

  * [ข้อมูลอ้างอิง CLI](</th/cli>)
  * [สถานะสุขภาพของ Gateway](</th/gateway/health>)


Was this useful?YesNo