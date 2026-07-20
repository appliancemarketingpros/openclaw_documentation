---
title: Plugin การประชุม Microsoft Teams
source_url: https://docs.openclaw.ai/th/plugins/teams-meetings
scraped_at: 2026-07-20
---

CapabilitiesPlugin guides

Plugin `teams-meetings` จะเข้าร่วมลิงก์ Microsoft Teams ในฐานะผู้เยี่ยมชมผ่านโปรไฟล์ Chrome ของ OpenClaw โดยรองรับลิงก์สำหรับที่ทำงานภายใต้ `teams.microsoft.com/l/meetup-join/...` และลิงก์สำหรับผู้ใช้ทั่วไปภายใต้ `teams.live.com/meet/...` แต่จะไม่สร้างการประชุม โทรเข้าร่วม โทรหา Microsoft Graph หรือบันทึกการประชุม

## การตั้งค่า

การพูดตอบกลับใช้ข้อกำหนดเบื้องต้นด้านเสียงภายในเครื่องเช่นเดียวกับ [Plugin Google Meet](</th/plugins/google-meet>) ได้แก่ macOS, อุปกรณ์เสียงเสมือน `BlackHole 2ch` และ SoX

bashCopy code
[code]
    brew install blackhole-2ch soxsudo rebootsystem_profiler SPAudioDataType | grep -i BlackHolecommand -v sox
[/code]

เปิดใช้งาน Plugin แล้วตรวจสอบการตั้งค่า:

json5Copy code
[code]
    {  plugins: {    entries: {      "teams-meetings": {        enabled: true,        config: {          defaultMode: "agent",          chrome: { guestName: "OpenClaw Agent" },        },      },    },  },}
[/code]

bashCopy code
[code]
    openclaw teamsmeetings setupopenclaw teamsmeetings join 'https://teams.microsoft.com/l/meetup-join/...'
[/code]

ใช้ `chromeNode.node` เพื่อเรียกใช้ Chrome, BlackHole และ SoX บน Node macOS ที่จับคู่ไว้ โดย Node ต้องอนุญาต `teamsmeetings.chrome` และ `browser.proxy`

## โหมด

โหมด | ลักษณะการทำงาน  
---|---  
`agent` | การถอดเสียงแบบเรียลไทม์จะปรึกษาเอเจนต์ OpenClaw ที่กำหนดค่าไว้ และ TTS จะพูดตอบกลับ  
`bidi` | โมเดลเสียงแบบเรียลไทม์จะฟังและตอบกลับโดยตรง  
`transcribe` | เข้าร่วมเพื่อสังเกตการณ์เท่านั้น พร้อมสแนปชอตข้อความถอดเสียงจากคำบรรยายสด  
  
โหมดถอดเสียงจะเปิดใช้คำบรรยายสดของ Teams หลังได้รับอนุญาตให้เข้าร่วม และบันทึกแถวคำบรรยายพร้อมระบุผู้พูด การดำเนินการ `transcript` จะส่งคืนบัฟเฟอร์คำบรรยายที่มีขอบเขตจำกัดสำหรับเซสชันการประชุม OpenClaw ที่ใช้งานอยู่

## ข้อจำกัดในการเข้าร่วมในฐานะผู้เยี่ยมชม

อะแดปเตอร์เบราว์เซอร์จะปิดหน้าคั่นสำหรับแอป กรอกชื่อผู้เยี่ยมชม ปิดกล้อง กำหนดค่าไมโครโฟนตามโหมดที่เลือก และคลิกปุ่มเข้าร่วม สถานะระหว่างสายจะใช้ตัวควบคุมวางสาย ส่วนสถานะล็อบบี้ การลงชื่อเข้าใช้ของผู้เช่า และสิทธิ์อนุญาตของอุปกรณ์จะส่งคืนเหตุผลที่ระบุชัดเจนว่าต้องดำเนินการด้วยตนเอง ระบบรองรับการเปลี่ยนเส้นทางของตัวเปิดการประชุมสำหรับผู้ใช้ทั่วไปและป้ายกำกับ `BlackHole 2ch (Virtual)` ที่ Chrome แสดง

นโยบายผู้เช่าของ Teams อาจกำหนดให้ลงชื่อเข้าใช้ ยืนยันอีเมล หรือรอผู้จัดอนุญาตให้เข้าร่วม ดำเนินการขั้นตอนดังกล่าวในโปรไฟล์ Chrome ของ OpenClaw แล้วลองตรวจสอบสถานะหรือใช้เสียงพูดอีกครั้ง Plugin จะไม่หลีกเลี่ยงนโยบายผู้เช่า

เว็บไคลเอ็นต์ Teams สำหรับผู้ใช้ทั่วไปผ่านการตรวจสอบแบบสดแล้วในส่วนของหน้าคั่นสำหรับแอป การป้อนชื่อผู้เยี่ยมชม การสลับไมโครโฟน/กล้องก่อนเข้าร่วม การเข้าร่วม การอนุญาตจากล็อบบี้ สิทธิ์อนุญาตสื่อ การตรวจจับสถานะระหว่างสาย คำบรรยายสด การกำหนดเส้นทางอินพุต/เอาต์พุตของ BlackHole การออกจากการประชุม และการตรวจจับสถานะหลังจบสาย ผู้เช่าสำหรับที่ทำงานอาจกำหนดนโยบายการลงชื่อเข้าใช้ การยืนยันอีเมล การอนุญาตให้เข้าร่วม และการยืนยันการออกจากการประชุมที่แตกต่างกัน ให้ดำเนินการด้วยตนเองตามที่ระบบแจ้งในโปรไฟล์ Chrome ของ OpenClaw

## พื้นผิวของเครื่องมือและ Gateway

เครื่องมือเอเจนต์ `teams_meetings` รองรับ `join`, `leave`, `status`, `transcript` และ `speak` เมธอดของ Gateway ใช้คำนำหน้า `teamsmeetings.*` ส่วนคำสั่งของ Node คือ `teamsmeetings.chrome`

## เนื้อหาที่เกี่ยวข้อง

  * [ภาพรวม Plugin สำหรับการประชุม](</th/plugins/meeting-plugins>)
  * [ช่องทาง Microsoft Teams](</th/channels/msteams>)


Was this useful?YesNo

Open issue