---
title: แดชบอร์ด
source_url: https://docs.openclaw.ai/th/cli/dashboard
scraped_at: 2026-05-25
---

# `openclaw dashboard`

เปิด UI ควบคุมโดยใช้การยืนยันตัวตนปัจจุบันของคุณ

bashCopy code
[code]
    openclaw dashboardopenclaw dashboard --no-open
[/code]

หมายเหตุ:

  * `dashboard` จะแปลงค่า SecretRefs ของ `gateway.auth.token` ที่กำหนดค่าไว้เมื่อทำได้
  * `dashboard` จะทำตาม `gateway.tls.enabled`: Gateway ที่เปิดใช้ TLS จะพิมพ์/เปิด URL ของ UI ควบคุมแบบ `https://` และเชื่อมต่อผ่าน `wss://`
  * หากการส่ง URL แดชบอร์ดที่ยืนยันตัวตนด้วยโทเค็นไปยังคลิปบอร์ด/เบราว์เซอร์ล้มเหลว `dashboard` จะบันทึกคำแนะนำการยืนยันตัวตนด้วยตนเองที่ปลอดภัย โดยระบุชื่อ `OPENCLAW_GATEWAY_TOKEN`, `gateway.auth.token` และคีย์แฟรกเมนต์ `token` โดยไม่พิมพ์ค่าโทเค็น
  * สำหรับโทเค็นที่จัดการด้วย SecretRef (ไม่ว่าจะถูกแปลงค่าแล้วหรือยังไม่ถูกแปลงค่า) `dashboard` จะพิมพ์/คัดลอก/เปิด URL ที่ไม่มีโทเค็น เพื่อหลีกเลี่ยงการเปิดเผยความลับภายนอกในเอาต์พุตเทอร์มินัล ประวัติคลิปบอร์ด หรืออาร์กิวเมนต์การเปิดเบราว์เซอร์
  * หาก `gateway.auth.token` ถูกจัดการด้วย SecretRef แต่ยังไม่ถูกแปลงค่าในเส้นทางคำสั่งนี้ คำสั่งจะพิมพ์ URL ที่ไม่มีโทเค็นและคำแนะนำการแก้ไขที่ชัดเจน แทนที่จะฝังตัวยึดตำแหน่งโทเค็นที่ไม่ถูกต้อง


## ที่เกี่ยวข้อง

  * [ข้อมูลอ้างอิง CLI](</th/cli>)
  * [แดชบอร์ด](</th/web/dashboard>)


Was this useful?YesNo