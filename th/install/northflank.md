---
title: Northflank
source_url: https://docs.openclaw.ai/th/install/northflank
scraped_at: 2026-05-25
---

# Northflank

Deploy OpenClaw บน Northflank ด้วยเทมเพลตแบบ one-click และเข้าถึงผ่านเว็บ Control UI นี่คือเส้นทางที่ง่ายที่สุดแบบ "ไม่ต้องใช้เทอร์มินัลบนเซิร์ฟเวอร์": Northflank จะรัน Gateway ให้คุณ

## วิธีเริ่มต้น

  1. คลิก [Deploy OpenClaw](<https://northflank.com/stacks/deploy-openclaw>) เพื่อเปิดเทมเพลต
  2. สร้าง[บัญชีบน Northflank](<https://app.northflank.com/signup>) หากคุณยังไม่มี
  3. คลิก **Deploy OpenClaw now**
  4. ตั้งค่าตัวแปรสภาพแวดล้อมที่จำเป็น: `OPENCLAW_GATEWAY_TOKEN` (ใช้ค่าที่สุ่มอย่างแข็งแรง)
  5. คลิก **Deploy stack** เพื่อ build และรันเทมเพลต OpenClaw
  6. รอให้การ Deploy เสร็จสิ้น จากนั้นคลิก **View resources**
  7. เปิด service ของ OpenClaw
  8. เปิด URL สาธารณะของ OpenClaw ที่ `/openclaw` และเชื่อมต่อโดยใช้ shared secret ที่กำหนดค่าไว้ เทมเพลตนี้ใช้ `OPENCLAW_GATEWAY_TOKEN` โดยค่าเริ่มต้น; หากคุณแทนที่ด้วยการยืนยันตัวตนแบบรหัสผ่าน ให้ใช้รหัสผ่านนั้นแทน


## สิ่งที่คุณจะได้รับ

  * OpenClaw Gateway + Control UI แบบโฮสต์แล้ว
  * ที่เก็บข้อมูลถาวรผ่าน Northflank Volume (`/data`) เพื่อให้ `openclaw.json`, `auth-profiles.json` รายเอเจนต์ สถานะ channel/provider เซสชัน และ workspace ยังคงอยู่ข้ามการ redeploy


## เชื่อมต่อ channel

ใช้ Control UI ที่ `/openclaw` หรือรัน `openclaw onboard` ผ่าน SSH เพื่อดูคำแนะนำการตั้งค่า channel:

  * [Telegram](</th/channels/telegram>) (เร็วที่สุด — ใช้เพียง bot token)
  * [Discord](</th/channels/discord>)
  * [channels ทั้งหมด](</th/channels>)


## ขั้นตอนถัดไป

  * ตั้งค่า channels การส่งข้อความ: [Channels](</th/channels>)
  * กำหนดค่า Gateway: [การกำหนดค่า Gateway](</th/gateway/configuration>)
  * อัปเดต OpenClaw ให้ทันสมัย: [การอัปเดต](</th/install/updating>)


Was this useful?YesNo