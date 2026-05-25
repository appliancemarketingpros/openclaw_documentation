---
title: โหมดยกระดับสิทธิ์
source_url: https://docs.openclaw.ai/th/tools/elevated
scraped_at: 2026-05-25
---

เมื่อ agent ทำงานภายใน sandbox คำสั่ง `exec` ของมันจะถูกจำกัดให้อยู่ใน สภาพแวดล้อม sandbox **โหมด elevated** ช่วยให้ agent ออกจากข้อจำกัดนั้นและเรียกใช้คำสั่ง ภายนอก sandbox แทน พร้อมเกตการอนุมัติที่กำหนดค่าได้

## คำสั่งกำกับ

ควบคุมโหมด elevated ต่อเซสชันด้วยคำสั่ง slash:

คำสั่งกำกับ | สิ่งที่ทำ  
---|---  
`/elevated on` | ทำงานภายนอก sandbox บนเส้นทาง host ที่กำหนดค่าไว้ โดยยังคงการอนุมัติไว้  
`/elevated ask` | เหมือนกับ `on` (alias)  
`/elevated full` | ทำงานภายนอก sandbox บนเส้นทาง host ที่กำหนดค่าไว้และข้ามการอนุมัติ  
`/elevated off` | กลับไปใช้การดำเนินการที่ถูกจำกัดอยู่ใน sandbox  
  
ยังใช้งานได้ในรูปแบบ `/elev on|off|ask|full` ด้วย

ส่ง `/elevated` โดยไม่มีอาร์กิวเมนต์เพื่อดูระดับปัจจุบัน

## วิธีการทำงาน

* ### ตรวจสอบความพร้อมใช้งาน

ต้องเปิดใช้งาน Elevated ใน config และผู้ส่งต้องอยู่ใน allowlist:

json5Copy code
[code]
    {  tools: {    elevated: {      enabled: true,      allowFrom: {        discord: ["user-id-123"],        whatsapp: ["+15555550123"],      },    },  },}
[/code]

* ### ตั้งค่าระดับ

ส่งข้อความที่มีเฉพาะคำสั่งกำกับเพื่อตั้งค่าเริ่มต้นของเซสชัน:

CodeCopy code
[code]
    /elevated full
[/code]

หรือใช้แบบ inline (มีผลกับข้อความนั้นเท่านั้น):

CodeCopy code
[code]
    /elevated on run the deployment script
[/code]

* ### คำสั่งทำงานภายนอก sandbox

เมื่อ elevated เปิดใช้งานอยู่ การเรียก `exec` จะออกจาก sandbox โดย host ที่มีผลจริงคือ `gateway` ตามค่าเริ่มต้น หรือ `node` เมื่อเป้าหมาย exec ที่กำหนดค่าไว้/ของเซสชันคือ `node` ในโหมด `full` การอนุมัติ exec จะถูกข้าม ในโหมด `on`/`ask` กฎการอนุมัติที่กำหนดค่าไว้ยังคงมีผล

## ลำดับการพิจารณา

  1. **คำสั่งกำกับแบบ inline** ในข้อความ (มีผลกับข้อความนั้นเท่านั้น)
  2. **การ override ของเซสชัน** (ตั้งค่าโดยส่งข้อความที่มีเฉพาะคำสั่งกำกับ)
  3. **ค่าเริ่มต้นส่วนกลาง** (`agents.defaults.elevatedDefault` ใน config)


## ความพร้อมใช้งานและ allowlist

  * **เกตส่วนกลาง** : `tools.elevated.enabled` (ต้องเป็น `true`)
  * **allowlist ของผู้ส่ง** : `tools.elevated.allowFrom` พร้อมรายการแยกตามช่องทาง
  * **เกตต่อ agent** : `agents.list[].tools.elevated.enabled` (ทำได้เพียงจำกัดเพิ่มเติม)
  * **allowlist ต่อ agent** : `agents.list[].tools.elevated.allowFrom` (ผู้ส่งต้องตรงกับทั้งส่วนกลาง + ต่อ agent)
  * **fallback ของ Discord** : หากละ `tools.elevated.allowFrom.discord` ไว้ จะใช้ `channels.discord.allowFrom` เป็น fallback
  * **ทุกเกตต้องผ่าน** มิฉะนั้น elevated จะถือว่าไม่พร้อมใช้งาน


รูปแบบรายการ allowlist:

คำนำหน้า | ตรงกับ  
---|---  
(ไม่มี) | ID ผู้ส่ง, E.164 หรือฟิลด์ From  
`name:` | ชื่อที่แสดงของผู้ส่ง  
`username:` | username ของผู้ส่ง  
`tag:` | tag ของผู้ส่ง  
`id:`, `from:`, `e164:` | การระบุตัวตนเป้าหมายอย่างชัดเจน  
  
## สิ่งที่ elevated ไม่ได้ควบคุม

  * **นโยบายเครื่องมือ** : หาก `exec` ถูกปฏิเสธโดยนโยบายเครื่องมือ elevated จะ override ไม่ได้
  * **นโยบายการเลือก host** : elevated ไม่ได้เปลี่ยน `auto` ให้เป็นการ override ข้าม host ได้อย่างอิสระ แต่จะใช้กฎเป้าหมาย exec ที่กำหนดค่าไว้/ของเซสชัน โดยเลือก `node` เฉพาะเมื่อเป้าหมายเป็น `node` อยู่แล้ว
  * **แยกจาก`/exec`**: คำสั่งกำกับ `/exec` ปรับค่าเริ่มต้น exec ต่อเซสชันสำหรับผู้ส่งที่ได้รับอนุญาต และไม่จำเป็นต้องใช้โหมด elevated


## ที่เกี่ยวข้อง

[**เครื่องมือ Exec** การเรียกใช้คำสั่ง shell จาก agent ](</th/tools/exec>) [**การอนุมัติ Exec** ระบบการอนุมัติและ allowlist สำหรับ `exec` ](</th/tools/exec-approvals>) [**Sandboxing** การกำหนดค่า sandbox ระดับ Gateway ](</th/gateway/sandboxing>) [**Sandbox เทียบกับนโยบายเครื่องมือเทียบกับ Elevated** วิธีที่เกตทั้งสามประกอบกันระหว่างการเรียกเครื่องมือ ](</th/gateway/sandbox-vs-tool-policy-vs-elevated>)

Was this useful?YesNo