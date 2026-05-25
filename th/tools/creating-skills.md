---
title: การสร้าง Skills
source_url: https://docs.openclaw.ai/th/tools/creating-skills
scraped_at: 2026-05-25
---

Skills สอน agent ว่าควรใช้เครื่องมืออย่างไรและเมื่อใด skill แต่ละรายการคือไดเรกทอรี ที่มีไฟล์ `SKILL.md` พร้อม YAML frontmatter และคำแนะนำแบบ markdown

สำหรับวิธีโหลดและจัดลำดับความสำคัญของ Skills โปรดดู [Skills](</th/tools/skills>)

## สร้าง skill แรกของคุณ

* ### สร้างไดเรกทอรีของ skill

Skills อยู่ใน workspace ของคุณ สร้างโฟลเดอร์ใหม่:

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/hello-world
[/code]

* ### เขียน SKILL.md

สร้าง `SKILL.md` ภายในไดเรกทอรีนั้น frontmatter จะกำหนด metadata และเนื้อหา markdown จะมีคำแนะนำสำหรับ agent

markdownCopy code
[code]
    ---name: hello-worlddescription: A simple skill that says hello.--- # Hello World Skill When the user asks for a greeting, use the `echo` tool to say"Hello from your custom skill!".
[/code]

ใช้รูปแบบ hyphen-case ด้วยตัวอักษรพิมพ์เล็ก ตัวเลข และยัติภังค์สำหรับ `name` ของ skill ให้ชื่อโฟลเดอร์และ `name` ใน frontmatter ตรงกัน

* ### เพิ่มเครื่องมือ (ไม่บังคับ)

คุณสามารถกำหนด schema ของเครื่องมือแบบกำหนดเองใน frontmatter หรือสั่งให้ agent ใช้เครื่องมือระบบที่มีอยู่ (เช่น `exec` หรือ `browser`) Skills ยังสามารถ มากับ plugins พร้อมกับเครื่องมือที่มันจัดทำเอกสารประกอบได้ด้วย

* ### โหลด skill

เริ่มเซสชันใหม่เพื่อให้ OpenClaw ตรวจพบ skill:

bashCopy code
[code]
    # From chat/new # Or restart the gatewayopenclaw gateway restart
[/code]

ตรวจสอบว่าโหลด skill แล้ว:

bashCopy code
[code]
    openclaw skills list
[/code]

* ### ทดสอบ

ส่งข้อความที่ควรกระตุ้น skill:

bashCopy code
[code]
    openclaw agent --message "give me a greeting"
[/code]

หรือเพียงแค่แชทกับ agent แล้วขอคำทักทาย

## ข้อมูลอ้างอิง metadata ของ skill

YAML frontmatter รองรับฟิลด์เหล่านี้:

ฟิลด์ | จำเป็น | คำอธิบาย  
---|---|---  
`name` | ใช่ | ตัวระบุเฉพาะที่ใช้ตัวอักษรพิมพ์เล็ก ตัวเลข และยัติภังค์  
`description` | ใช่ | คำอธิบายหนึ่งบรรทัดที่แสดงให้ agent เห็น  
`metadata.openclaw.os` | ไม่ | ตัวกรอง OS (`["darwin"]`, `["linux"]` ฯลฯ)  
`metadata.openclaw.requires.bins` | ไม่ | ไบนารีที่จำเป็นต้องมีบน PATH  
`metadata.openclaw.requires.config` | ไม่ | คีย์ config ที่จำเป็น  
  
## แนวทางปฏิบัติที่ดี

  * **กระชับ** — สั่ง model ว่าต้องทำ _อะไร_ ไม่ใช่ว่าต้องเป็น AI อย่างไร
  * **ความปลอดภัยมาก่อน** — หาก skill ของคุณใช้ `exec` ให้แน่ใจว่า prompt ไม่อนุญาตให้มีการแทรกคำสั่งโดยอำเภอใจจากอินพุตที่ไม่น่าเชื่อถือ
  * **ทดสอบในเครื่อง** — ใช้ `openclaw agent --message "..."` เพื่อทดสอบก่อนแชร์
  * **ใช้ ClawHub** — เรียกดูและร่วมเพิ่ม skills ได้ที่ [ClawHub](<https://clawhub.ai>)


## Skills อยู่ที่ไหน

ตำแหน่ง | ลำดับความสำคัญ | ขอบเขต  
---|---|---  
`\<workspace\>/skills/` | สูงสุด | ต่อ agent  
`\<workspace\>/.agents/skills/` | สูง | agent ต่อ workspace  
`~/.agents/skills/` | ปานกลาง | โปรไฟล์ agent ที่แชร์  
`~/.openclaw/skills/` | ปานกลาง | แชร์ (agent ทั้งหมด)  
รวมมาในชุด (มาพร้อมกับ OpenClaw) | ต่ำ | ทั่วทั้งระบบ  
`skills.load.extraDirs` | ต่ำสุด | โฟลเดอร์ที่แชร์แบบกำหนดเอง  
  
## ที่เกี่ยวข้อง

  * [ข้อมูลอ้างอิง Skills](</th/tools/skills>) — กฎการโหลด ลำดับความสำคัญ และการ gating
  * [config ของ Skills](</th/tools/skills-config>) — schema ของ config `skills.*`
  * [ClawHub](</th/clawhub>) — registry สาธารณะของ skill
  * [การสร้าง Plugins](</th/plugins/building-plugins>) — plugins สามารถมาพร้อมกับ skills ได้


Was this useful?YesNo