---
title: การส่งโดยเอเจนต์
source_url: https://docs.openclaw.ai/th/tools/agent-send
scraped_at: 2026-05-25
---

`openclaw agent` เรียกใช้เอเจนต์หนึ่งรอบจากบรรทัดคำสั่งโดยไม่ต้องมี ข้อความแชตขาเข้า ใช้สำหรับเวิร์กโฟลว์แบบสคริปต์ การทดสอบ และ การส่งแบบโปรแกรม

## เริ่มต้นอย่างรวดเร็ว

* ### Run a simple agent turn

bashCopy code
[code]
    openclaw agent --message "What is the weather today?"
[/code]

คำสั่งนี้จะส่งข้อความผ่าน Gateway และพิมพ์คำตอบออกมา

* ### Target a specific agent or session

bashCopy code
[code]
    # Target a specific agentopenclaw agent --agent ops --message "Summarize logs" # Target a phone number (derives session key)openclaw agent --to +15555550123 --message "Status update" # Reuse an existing sessionopenclaw agent --session-id abc123 --message "Continue the task"
[/code]

* ### Deliver the reply to a channel

bashCopy code
[code]
    # Deliver to WhatsApp (default channel)openclaw agent --to +15555550123 --message "Report ready" --deliver # Deliver to Slackopenclaw agent --agent ops --message "Generate report" \  --deliver --reply-channel slack --reply-to "#reports"
[/code]

## แฟล็ก

แฟล็ก | คำอธิบาย  
---|---  
`--message \<text\>` | ข้อความที่จะส่ง (จำเป็น)  
`--to \<dest\>` | สร้างคีย์เซสชันจากเป้าหมาย (โทรศัพท์, chat id)  
`--agent \<id\>` | กำหนดเป้าหมายเป็นเอเจนต์ที่ตั้งค่าไว้ (ใช้เซสชัน `main` ของเอเจนต์นั้น)  
`--session-id \<id\>` | ใช้เซสชันที่มีอยู่ตาม id  
`--local` | บังคับใช้รันไทม์แบบฝังในเครื่อง (ข้าม Gateway)  
`--deliver` | ส่งคำตอบไปยังช่องทางแชต  
`--channel \<name\>` | ช่องทางการส่ง (whatsapp, telegram, discord, slack ฯลฯ)  
`--reply-to \<target\>` | ระบุเป้าหมายการส่งแทนค่าเริ่มต้น  
`--reply-channel \<name\>` | ระบุช่องทางการส่งแทนค่าเริ่มต้น  
`--reply-account \<id\>` | ระบุ id บัญชีการส่งแทนค่าเริ่มต้น  
`--thinking \<level\>` | ตั้งค่าระดับการคิดสำหรับโปรไฟล์โมเดลที่เลือก  
`--verbose \<on|full|off\>` | ตั้งค่าระดับ verbose  
`--timeout \<seconds\>` | กำหนด timeout ของเอเจนต์แทนค่าเริ่มต้น  
`--json` | ส่งออก JSON แบบมีโครงสร้าง  
  
## พฤติกรรม

  * โดยค่าเริ่มต้น CLI จะทำงาน **ผ่าน Gateway** เพิ่ม `--local` เพื่อบังคับใช้ รันไทม์แบบฝังในเครื่องปัจจุบัน
  * หากเข้าถึง Gateway ไม่ได้ CLI จะ **fallback** ไปใช้การรันแบบฝังในเครื่อง
  * การเลือกเซสชัน: `--to` สร้างคีย์เซสชัน (เป้าหมายแบบกลุ่ม/ช่องทาง จะคงการแยกกันไว้; แชตโดยตรงจะถูกรวมเป็น `main`)
  * แฟล็ก thinking และ verbose จะถูกเก็บต่อเนื่องไว้ใน session store
  * เอาต์พุต: ค่าเริ่มต้นเป็นข้อความธรรมดา หรือใช้ `--json` สำหรับ payload + metadata แบบมีโครงสร้าง
  * เมื่อใช้ `--json --deliver` JSON จะรวมสถานะการส่งสำหรับการส่งที่ส่งแล้ว, ถูกระงับ, บางส่วน และล้มเหลว ดู [สถานะการส่ง JSON](</th/cli/agent#json-delivery-status>)


## ตัวอย่าง

bashCopy code
[code]
    # Simple turn with JSON outputopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --json # Turn with thinking levelopenclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium # Deliver to a different channel than the sessionopenclaw agent --agent ops --message "Alert" --deliver --reply-channel telegram --reply-to "@admin"
[/code]

## ที่เกี่ยวข้อง

[**Agent CLI reference** เอกสารอ้างอิงแฟล็กและตัวเลือกทั้งหมดของ `openclaw agent` ](</th/cli/agent>) [**Sub-agents** การสร้างเอเจนต์ย่อยเบื้องหลัง ](</th/tools/subagents>) [**Sessions** วิธีการทำงานของคีย์เซสชัน และวิธีที่ `--to`, `--agent` และ `--session-id` resolve คีย์เหล่านั้น ](</th/concepts/session>) [**Slash commands** แค็ตตาล็อกคำสั่ง native ที่ใช้ภายในเซสชันของเอเจนต์ ](</th/tools/slash-commands>)

Was this useful?YesNo