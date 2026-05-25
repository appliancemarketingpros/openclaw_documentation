---
title: การนำ BlueBubbles ออกและเส้นทาง iMessage ของ imsg
source_url: https://docs.openclaw.ai/th/announcements/bluebubbles-imessage
scraped_at: 2026-05-25
---

# การนำ BlueBubbles ออกและเส้นทาง iMessage ผ่าน imsg

OpenClaw ไม่ได้มาพร้อมกับช่องทาง BlueBubbles อีกต่อไปแล้ว ตอนนี้การรองรับ iMessage ทำงานผ่าน Plugin `imessage` ที่รวมมาให้ ซึ่งเริ่ม [`imsg`](<https://github.com/steipete/imsg>) ภายในเครื่องหรือผ่านตัวห่อ SSH และสื่อสาร JSON-RPC ผ่าน stdin/stdout

หากการกำหนดค่าของคุณยังมี `channels.bluebubbles` ให้ย้ายไปเป็น `channels.imessage` URL เอกสารเดิม `/channels/bluebubbles` จะเปลี่ยนเส้นทางไปยัง [การย้ายมาจาก BlueBubbles](</th/channels/imessage-from-bluebubbles>) ซึ่งมีตารางแปลการกำหนดค่าแบบเต็มและเช็กลิสต์การเปลี่ยนระบบ

## สิ่งที่เปลี่ยนไป

  * ไม่มีเซิร์ฟเวอร์ HTTP ของ BlueBubbles, เส้นทาง Webhook, รหัสผ่าน REST หรือรันไทม์ Plugin ของ BlueBubbles ในเส้นทาง iMessage ของ OpenClaw ที่รองรับ
  * OpenClaw อ่านและเฝ้าดู Messages ผ่าน `imsg` บน Mac ที่ลงชื่อเข้าใช้ Messages.app อยู่
  * การส่ง รับ ประวัติ และสื่อพื้นฐานใช้พื้นผิว `imsg` ปกติและสิทธิ์ของ macOS
  * การทำงานขั้นสูง เช่น การตอบกลับในเธรด, tapbacks, แก้ไข, ยกเลิกการส่ง, เอฟเฟกต์, ใบตอบรับการอ่าน, ตัวบ่งชี้การพิมพ์ และการจัดการกลุ่ม ต้องใช้ `imsg launch` พร้อมบริดจ์ API ส่วนตัวที่พร้อมใช้งาน
  * Gateway บน Linux และ Windows ยังคงใช้ iMessage ได้โดยตั้งค่า `channels.imessage.cliPath` เป็นตัวห่อ SSH ที่เรียกใช้ `imsg` บน Mac ที่ลงชื่อเข้าใช้แล้ว


## สิ่งที่ต้องทำ

  1. ติดตั้งและตรวจสอบ `imsg` บน Mac ที่ใช้ Messages:

bashCopy code
[code]brew install steipete/tap/imsgimsg --versionimsg chats --limit 3imsg rpc --help
[/code]

  2. ให้สิทธิ์ Full Disk Access และ Automation แก่บริบทของโปรเซสที่เรียกใช้ `imsg` และ OpenClaw

  3. แปลงการกำหนดค่าเดิม:

json5Copy code
[code]{  channels: {    imessage: {      enabled: true,      cliPath: "/opt/homebrew/bin/imsg",      dmPolicy: "pairing",      allowFrom: ["+15555550123"],      groupPolicy: "allowlist",      groupAllowFrom: ["+15555550123"],      groups: {        "*": { requireMention: true },      },      includeAttachments: true,    },  },}
[/code]

  4. รีสตาร์ท Gateway แล้วตรวจสอบ:

bashCopy code
[code]openclaw channels status --probe
[/code]

  5. ทดสอบ DM, กลุ่ม, ไฟล์แนบ และการทำงานของ API ส่วนตัวใดๆ ที่คุณต้องพึ่งพา ก่อนลบเซิร์ฟเวอร์ BlueBubbles เดิมของคุณ


## หมายเหตุการย้ายระบบ

  * `channels.bluebubbles.serverUrl` และ `channels.bluebubbles.password` ไม่มีค่าเทียบเท่าใน iMessage
  * `channels.bluebubbles.allowFrom`, `groupAllowFrom`, `groups`, `includeAttachments`, รากไฟล์แนบ, ขีดจำกัดขนาดสื่อ, การแบ่งชิ้น และสวิตช์การทำงาน มีค่าเทียบเท่าใน iMessage
  * `channels.imessage.includeAttachments` ยังคงปิดตามค่าเริ่มต้น ให้ตั้งค่าอย่างชัดเจนหากคุณคาดหวังให้รูปภาพ ข้อความเสียง วิดีโอ หรือไฟล์ขาเข้าถึงเอเจนต์
  * เมื่อใช้ `groupPolicy: "allowlist"` ให้คัดลอกบล็อก `groups` เดิม รวมถึงรายการไวลด์การ์ด `"*"` หากมี รายการอนุญาตผู้ส่งในกลุ่มและรีจิสทรีของกลุ่มเป็นด่านแยกกัน
  * การผูก ACP ที่จับคู่กับ `channel: "bluebubbles"` ต้องเปลี่ยนเป็น `channel: "imessage"`
  * คีย์เซสชัน BlueBubbles เดิมจะไม่กลายเป็นคีย์เซสชัน iMessage การอนุมัติการจับคู่จะส่งต่อด้วยแฮนเดิล แต่ประวัติการสนทนาภายใต้คีย์เซสชัน BlueBubbles จะไม่ส่งต่อ


## ดูเพิ่มเติม

  * [การย้ายมาจาก BlueBubbles](</th/channels/imessage-from-bluebubbles>)
  * [iMessage](</th/channels/imessage>)
  * [ข้อมูลอ้างอิงการกำหนดค่า - iMessage](</th/gateway/config-channels#imessage>)


Was this useful?YesNo