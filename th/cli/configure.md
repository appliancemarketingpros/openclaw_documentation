---
title: กำหนดค่า
source_url: https://docs.openclaw.ai/th/cli/configure
scraped_at: 2026-05-25
---

# `openclaw configure`

พรอมป์แบบโต้ตอบสำหรับเปลี่ยนแปลงการตั้งค่าที่มีอยู่แบบเจาะจง: ข้อมูลรับรอง, อุปกรณ์, ค่าเริ่มต้นของเอเจนต์, Gateway, ช่องทาง, Plugin, Skills และการตรวจสอบสถานภาพ

ใช้ `openclaw onboard` สำหรับขั้นตอนเริ่มใช้งานครั้งแรกแบบมีคำแนะนำเต็มรูปแบบ, ใช้ `openclaw setup` สำหรับ config/workspace พื้นฐานเท่านั้น และใช้ `openclaw channels add` เมื่อคุณต้องการตั้งค่าบัญชีช่องทางเท่านั้น

เมื่อ configure เริ่มจากตัวเลือกการยืนยันตัวตนของผู้ให้บริการ ตัวเลือกโมเดลเริ่มต้นและ allowlist จะเลือกผู้ให้บริการนั้นโดยอัตโนมัติ สำหรับผู้ให้บริการแบบคู่ เช่น Volcengine และ BytePlus การตั้งค่าเดียวกันนี้ยังจับคู่กับตัวแปรแผนการเขียนโค้ดของผู้ให้บริการเหล่านั้นด้วย (`volcengine-plan/*`, `byteplus-plan/*`) หากตัวกรองผู้ให้บริการที่ต้องการจะทำให้รายการว่าง configure จะย้อนกลับไปใช้แค็ตตาล็อกแบบไม่กรองแทนการแสดงตัวเลือกว่างเปล่า

สำหรับการค้นหาเว็บ `openclaw configure --section web` ให้คุณเลือกผู้ให้บริการ และกำหนดค่าข้อมูลรับรองของผู้ให้บริการนั้น ผู้ให้บริการบางรายยังแสดงพรอมป์ติดตามผล เฉพาะผู้ให้บริการด้วย:

  * **Grok** สามารถเสนอการตั้งค่า `x_search` แบบไม่บังคับด้วย `XAI_API_KEY` เดียวกัน และ ให้คุณเลือกโมเดล `x_search`
  * **Kimi** สามารถถามภูมิภาค Moonshot API (`api.moonshot.ai` เทียบกับ `api.moonshot.cn`) และโมเดลค้นหาเว็บ Kimi เริ่มต้น


ที่เกี่ยวข้อง:

  * ข้อมูลอ้างอิงการกำหนดค่า Gateway: [การกำหนดค่า](</th/gateway/configuration>)
  * Config CLI: [Config](</th/cli/config>)


## ตัวเลือก

  * `--section <section>`: ตัวกรองส่วนที่ทำซ้ำได้


ส่วนที่ใช้ได้:

  * `workspace`
  * `model`
  * `web`
  * `gateway`
  * `daemon`
  * `channels`
  * `plugins`
  * `skills`
  * `health`


หมายเหตุ:

  * การเลือกตำแหน่งที่ Gateway ทำงานจะอัปเดต `gateway.mode` เสมอ คุณสามารถเลือก "ดำเนินการต่อ" โดยไม่มีส่วนอื่นได้หากนั่นคือทั้งหมดที่คุณต้องการ
  * หลังจากเขียน config ในเครื่องแล้ว configure จะติดตั้ง Plugin ที่ดาวน์โหลดได้ที่เลือกไว้เมื่อเส้นทางการตั้งค่าที่เลือกต้องใช้ Plugin เหล่านั้น การกำหนดค่า Gateway ระยะไกลจะไม่ติดตั้งแพ็กเกจ Plugin ในเครื่อง
  * บริการที่เน้นช่องทาง (Slack/Discord/Matrix/Microsoft Teams) จะแจ้งให้ระบุ allowlist ของช่องทาง/ห้องระหว่างการตั้งค่า คุณสามารถป้อนชื่อหรือ ID ได้ วิซาร์ดจะแปลงชื่อเป็น ID เมื่อเป็นไปได้
  * หากคุณเรียกใช้ขั้นตอนติดตั้ง daemon, การยืนยันตัวตนด้วยโทเค็นต้องใช้โทเค็น และ `gateway.auth.token` ถูกจัดการด้วย SecretRef, configure จะตรวจสอบ SecretRef แต่จะไม่บันทึกค่าโทเค็นแบบข้อความธรรมดาที่แก้ไขแล้วลงในเมตาดาต้าสภาพแวดล้อมของบริการ supervisor
  * หากการยืนยันตัวตนด้วยโทเค็นต้องใช้โทเค็น และ SecretRef ของโทเค็นที่กำหนดค่าไว้ยังแก้ไขไม่ได้ configure จะบล็อกการติดตั้ง daemon พร้อมคำแนะนำในการแก้ไขที่นำไปปฏิบัติได้
  * หากทั้ง `gateway.auth.token` และ `gateway.auth.password` ถูกกำหนดค่าไว้ และไม่ได้ตั้งค่า `gateway.auth.mode`, configure จะบล็อกการติดตั้ง daemon จนกว่าจะตั้งค่าโหมดอย่างชัดเจน


## ตัวอย่าง

bashCopy code
[code]
    openclaw configureopenclaw configure --section webopenclaw configure --section model --section channelsopenclaw configure --section gateway --section daemon
[/code]

## ที่เกี่ยวข้อง

  * [ข้อมูลอ้างอิง CLI](</th/cli>)
  * [การกำหนดค่า](</th/gateway/configuration>)


Was this useful?YesNo