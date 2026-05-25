---
title: เครื่องเสมือน macOS
source_url: https://docs.openclaw.ai/th/install/macos-vm
scraped_at: 2026-05-25
---

## ค่าเริ่มต้นที่แนะนำ (ผู้ใช้ส่วนใหญ่)

  * **Linux VPS ขนาดเล็ก** สำหรับ Gateway ที่เปิดใช้งานตลอดเวลาและมีต้นทุนต่ำ ดู [VPS hosting](</th/vps>)
  * **ฮาร์ดแวร์เฉพาะ** (Mac mini หรือเครื่อง Linux) หากคุณต้องการควบคุมได้เต็มที่และมี **IP สำหรับที่อยู่อาศัย** สำหรับการทำงานอัตโนมัติบนเบราว์เซอร์ หลายเว็บไซต์บล็อก IP ของศูนย์ข้อมูล ดังนั้นการท่องเว็บจากเครื่องในบ้านมักทำงานได้ดีกว่า
  * **แบบไฮบริด:** เก็บ Gateway ไว้บน VPS ราคาถูก และเชื่อมต่อ Mac ของคุณเป็น **Node** เมื่อคุณต้องการการทำงานอัตโนมัติผ่านเบราว์เซอร์/UI ดู [Nodes](</th/nodes>) และ [Gateway remote](</th/gateway/remote>)


ใช้ macOS VM เมื่อคุณต้องการความสามารถเฉพาะของ macOS โดยเฉพาะ เช่น iMessage หรือต้องการแยกสภาพแวดล้อมออกจาก Mac ที่ใช้ประจำอย่างเข้มงวด

## ตัวเลือก macOS VM

### VM ภายในเครื่องบน Apple Silicon Mac ของคุณ (Lume)

เรียกใช้ OpenClaw ใน macOS VM แบบ sandbox บน Apple Silicon Mac ที่คุณมีอยู่โดยใช้ [Lume](<https://cua.ai/docs/lume>)

สิ่งนี้ให้คุณ:

  * สภาพแวดล้อม macOS เต็มรูปแบบที่แยกออกมา (โฮสต์ของคุณยังคงสะอาด)
  * รองรับ iMessage ผ่าน `imsg` (พาธภายในเครื่องเริ่มต้นเป็นไปไม่ได้บน Linux/Windows)
  * รีเซ็ตได้ทันทีด้วยการโคลน VM
  * ไม่ต้องใช้ฮาร์ดแวร์เพิ่มเติมหรือมีค่าใช้จ่ายคลาวด์


### ผู้ให้บริการ Mac แบบโฮสต์ (คลาวด์)

หากคุณต้องการ macOS ในคลาวด์ ผู้ให้บริการ Mac แบบโฮสต์ก็ใช้งานได้เช่นกัน:

  * [MacStadium](<https://www.macstadium.com/>) (Mac แบบโฮสต์)
  * ผู้ให้บริการ Mac แบบโฮสต์รายอื่นก็ใช้งานได้เช่นกัน ให้ทำตามเอกสาร VM + SSH ของพวกเขา


เมื่อคุณมีสิทธิ์เข้าถึง SSH ไปยัง macOS VM แล้ว ให้ดำเนินต่อที่ขั้นตอน 6 ด้านล่าง

* * *

## เส้นทางด่วน (Lume, ผู้ใช้ที่มีประสบการณ์)

  1. ติดตั้ง Lume
  2. `lume create openclaw --os macos --ipsw latest`
  3. ทำ Setup Assistant ให้เสร็จ เปิดใช้ Remote Login (SSH)
  4. `lume run openclaw --no-display`
  5. SSH เข้าไป ติดตั้ง OpenClaw กำหนดค่าช่องทาง
  6. เสร็จสิ้น


* * *

## สิ่งที่คุณต้องมี (Lume)

  * Apple Silicon Mac (M1/M2/M3/M4)
  * macOS Sequoia หรือใหม่กว่าบนโฮสต์
  * พื้นที่ดิสก์ว่างประมาณ 60 GB ต่อ VM
  * ประมาณ 20 นาที


* * *

## 1) ติดตั้ง Lume

bashCopy code
[code]
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"
[/code]

หาก `~/.local/bin` ไม่อยู่ใน PATH ของคุณ:

bashCopy code
[code]
    echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.zshrc && source ~/.zshrc
[/code]

ตรวจสอบ:

bashCopy code
[code]
    lume --version
[/code]

เอกสาร: [การติดตั้ง Lume](<https://cua.ai/docs/lume/guide/getting-started/installation>)

* * *

## 2) สร้าง macOS VM

bashCopy code
[code]
    lume create openclaw --os macos --ipsw latest
[/code]

คำสั่งนี้จะดาวน์โหลด macOS และสร้าง VM หน้าต่าง VNC จะเปิดขึ้นโดยอัตโนมัติ

* * *

## 3) ทำ Setup Assistant ให้เสร็จ

ในหน้าต่าง VNC:

  1. เลือกภาษาและภูมิภาค
  2. ข้าม Apple ID (หรือเข้าสู่ระบบหากคุณต้องการใช้ iMessage ในภายหลัง)
  3. สร้างบัญชีผู้ใช้ (จำชื่อผู้ใช้และรหัสผ่านไว้)
  4. ข้ามฟีเจอร์เสริมทั้งหมด


หลังจากตั้งค่าเสร็จแล้ว ให้เปิดใช้ SSH:

  1. เปิด System Settings → General → Sharing
  2. เปิดใช้ "Remote Login"


* * *

## 4) รับที่อยู่ IP ของ VM

bashCopy code
[code]
    lume get openclaw
[/code]

มองหาที่อยู่ IP (โดยปกติคือ `192.168.64.x`)

* * *

## 5) SSH เข้า VM

bashCopy code
[code]
    ssh youruser@192.168.64.X
[/code]

แทนที่ `youruser` ด้วยบัญชีที่คุณสร้าง และแทนที่ IP ด้วย IP ของ VM ของคุณ

* * *

## 6) ติดตั้ง OpenClaw

ภายใน VM:

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

ทำตามพรอมป์การเริ่มต้นใช้งานเพื่อตั้งค่าผู้ให้บริการโมเดลของคุณ (Anthropic, OpenAI ฯลฯ)

* * *

## 7) กำหนดค่าช่องทาง

แก้ไขไฟล์การกำหนดค่า:

bashCopy code
[code]
    nano ~/.openclaw/openclaw.json
[/code]

เพิ่มช่องทางของคุณ:

json5Copy code
[code]
    {  channels: {    whatsapp: {      dmPolicy: "allowlist",      allowFrom: ["+15551234567"],    },    telegram: {      botToken: "YOUR_BOT_TOKEN",    },  },}
[/code]

จากนั้นเข้าสู่ระบบ WhatsApp (สแกน QR):

bashCopy code
[code]
    openclaw channels login
[/code]

* * *

## 8) เรียกใช้ VM แบบไม่มีหน้าจอ

หยุด VM แล้วเริ่มใหม่โดยไม่มีจอแสดงผล:

bashCopy code
[code]
    lume stop openclawlume run openclaw --no-display
[/code]

VM จะทำงานอยู่เบื้องหลัง daemon ของ OpenClaw จะคอยให้ Gateway ทำงานต่อไป

เพื่อตรวจสอบสถานะ:

bashCopy code
[code]
    ssh youruser@192.168.64.X "openclaw status"
[/code]

* * *

## เพิ่มเติม: การผสานรวม iMessage

นี่คือฟีเจอร์เด่นของการรันบน macOS ใช้ [iMessage](</th/channels/imessage>) กับ `imsg` เพื่อเพิ่ม Messages เข้าใน OpenClaw

ภายใน VM:

  1. เข้าสู่ระบบ Messages
  2. ติดตั้ง `imsg`
  3. ให้สิทธิ์ Full Disk Access และ Automation สำหรับโปรเซสที่รัน OpenClaw/`imsg`
  4. ตรวจสอบการรองรับ RPC ด้วย `imsg rpc --help`


เพิ่มลงในการกำหนดค่า OpenClaw ของคุณ:

json5Copy code
[code]
    {  channels: {    imessage: {      enabled: true,      cliPath: "imsg",      dbPath: "~/Library/Messages/chat.db",    },  },}
[/code]

รีสตาร์ท Gateway ตอนนี้เอเจนต์ของคุณสามารถส่งและรับ iMessage ได้แล้ว

รายละเอียดการตั้งค่าแบบเต็ม: [ช่องทาง iMessage](</th/channels/imessage>)

* * *

## บันทึกอิมเมจต้นแบบ

ก่อนปรับแต่งเพิ่มเติม ให้สร้าง snapshot ของสถานะสะอาดของคุณ:

bashCopy code
[code]
    lume stop openclawlume clone openclaw openclaw-golden
[/code]

รีเซ็ตได้ทุกเมื่อ:

bashCopy code
[code]
    lume stop openclaw && lume delete openclawlume clone openclaw-golden openclawlume run openclaw --no-display
[/code]

* * *

## การรันตลอด 24/7

ทำให้ VM ทำงานต่อเนื่องโดย:

  * เสียบปลั๊ก Mac ของคุณไว้
  * ปิดโหมดพักเครื่องใน System Settings → Energy Saver
  * ใช้ `caffeinate` หากจำเป็น


สำหรับการเปิดใช้งานตลอดเวลาอย่างแท้จริง ให้พิจารณา Mac mini เฉพาะหรือ VPS ขนาดเล็ก ดู [VPS hosting](</th/vps>)

* * *

## การแก้ไขปัญหา

ปัญหา | วิธีแก้ไข  
---|---  
ไม่สามารถ SSH เข้า VM ได้ | ตรวจสอบว่าเปิดใช้ "Remote Login" ใน System Settings ของ VM แล้ว  
IP ของ VM ไม่แสดง | รอให้ VM บูตจนเสร็จสมบูรณ์ แล้วรัน `lume get openclaw` อีกครั้ง  
ไม่พบคำสั่ง Lume | เพิ่ม `~/.local/bin` ลงใน PATH ของคุณ  
สแกน QR ของ WhatsApp ไม่ได้ | ตรวจสอบว่าคุณเข้าสู่ระบบใน VM (ไม่ใช่โฮสต์) เมื่อรัน `openclaw channels login`  
  
* * *

## เอกสารที่เกี่ยวข้อง

  * [VPS hosting](</th/vps>)
  * [Nodes](</th/nodes>)
  * [Gateway remote](</th/gateway/remote>)
  * [ช่องทาง iMessage](</th/channels/imessage>)
  * [เริ่มต้นใช้งาน Lume อย่างรวดเร็ว](<https://cua.ai/docs/lume/guide/getting-started/quickstart>)
  * [ข้อมูลอ้างอิง Lume CLI](<https://cua.ai/docs/lume/reference/cli-reference>)
  * [การตั้งค่า VM แบบไม่ต้องเฝ้าดู](<https://cua.ai/docs/lume/guide/fundamentals/unattended-setup>) (ขั้นสูง)
  * [Docker Sandboxing](</th/install/docker>) (แนวทางการแยกสภาพแวดล้อมทางเลือก)


Was this useful?YesNo