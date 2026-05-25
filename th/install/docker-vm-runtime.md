---
title: รันไทม์ VM ของ Docker
source_url: https://docs.openclaw.ai/th/install/docker-vm-runtime
scraped_at: 2026-05-25
---

ขั้นตอน runtime ที่ใช้ร่วมกันสำหรับการติดตั้ง Docker บน VM เช่น GCP, Hetzner และผู้ให้บริการ VPS ที่คล้ายกัน

## ใส่ไบนารีที่จำเป็นไว้ในอิมเมจ

การติดตั้งไบนารีภายในคอนเทนเนอร์ที่กำลังทำงานอยู่เป็นกับดัก สิ่งใดก็ตามที่ติดตั้งตอน runtime จะหายไปเมื่อรีสตาร์ท

ไบนารีภายนอกทั้งหมดที่ Skills ต้องใช้ต้องติดตั้งในช่วงสร้างอิมเมจ

ตัวอย่างด้านล่างแสดงไบนารีทั่วไปเพียงสามรายการ:

  * `gog` (จาก `gogcli`) สำหรับการเข้าถึง Gmail
  * `goplaces` สำหรับ Google Places
  * `wacli` สำหรับ WhatsApp


สิ่งเหล่านี้เป็นตัวอย่าง ไม่ใช่รายการที่ครบถ้วน คุณสามารถติดตั้งไบนารีได้มากเท่าที่ต้องการโดยใช้รูปแบบเดียวกัน

หากคุณเพิ่ม Skills ใหม่ในภายหลังที่ต้องพึ่งพาไบนารีเพิ่มเติม คุณต้อง:

  1. อัปเดต Dockerfile
  2. สร้างอิมเมจใหม่
  3. รีสตาร์ทคอนเทนเนอร์


**ตัวอย่าง Dockerfile**

dockerfileCopy code
[code]
    FROM node:24-bookworm RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/* # Example binary 1: Gmail CLI (gogcli — installs as `gog`)# Copy the current Linux asset URL from https://github.com/steipete/gogcli/releasesRUN curl -L https://github.com/steipete/gogcli/releases/latest/download/gogcli_linux_amd64.tar.gz \  | tar -xzO gog > /usr/local/bin/gog; \  chmod +x /usr/local/bin/gog # Example binary 2: Google Places CLI# Copy the current Linux asset URL from https://github.com/steipete/goplaces/releasesRUN curl -L https://github.com/steipete/goplaces/releases/latest/download/goplaces_linux_amd64.tar.gz \  | tar -xzO goplaces > /usr/local/bin/goplaces; \  chmod +x /usr/local/bin/goplaces # Example binary 3: WhatsApp CLI# Copy the current Linux asset URL from https://github.com/steipete/wacli/releasesRUN curl -L https://github.com/steipete/wacli/releases/latest/download/wacli-linux-amd64.tar.gz \  | tar -xzO wacli > /usr/local/bin/wacli; \  chmod +x /usr/local/bin/wacli # Add more binaries below using the same pattern WORKDIR /appCOPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./COPY ui/package.json ./ui/package.jsonCOPY scripts ./scripts RUN corepack enableRUN pnpm install --frozen-lockfile COPY . .RUN pnpm buildRUN pnpm ui:installRUN pnpm ui:build ENV NODE_ENV=production CMD ["node","dist/index.js"]
[/code]

## สร้างและเปิดใช้งาน

bashCopy code
[code]
    docker compose builddocker compose up -d openclaw-gateway
[/code]

หาก build ล้มเหลวด้วย `Killed` หรือ `exit code 137` ระหว่าง `pnpm install --frozen-lockfile` แสดงว่า VM หน่วยความจำไม่พอ ให้ใช้คลาสเครื่องที่ใหญ่ขึ้นก่อนลองใหม่

ตรวจสอบไบนารี:

bashCopy code
[code]
    docker compose exec openclaw-gateway which gogdocker compose exec openclaw-gateway which goplacesdocker compose exec openclaw-gateway which wacli
[/code]

ผลลัพธ์ที่คาดหวัง:

CodeCopy code
[code]
    /usr/local/bin/gog/usr/local/bin/goplaces/usr/local/bin/wacli
[/code]

ตรวจสอบ Gateway:

bashCopy code
[code]
    docker compose logs -f openclaw-gateway
[/code]

ผลลัพธ์ที่คาดหวัง:

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:18789
[/code]

## สิ่งใดคงอยู่ที่ใด

OpenClaw ทำงานใน Docker แต่ Docker ไม่ใช่แหล่งข้อมูลหลัก สถานะที่มีอายุยาวทั้งหมดต้องอยู่รอดหลังการรีสตาร์ท การ rebuild และการ reboot

ส่วนประกอบ | ตำแหน่ง | กลไกการคงอยู่ | หมายเหตุ  
---|---|---|---  
การกำหนดค่า Gateway | `/home/node/.openclaw/` | การ mount volume จากโฮสต์ | รวม `openclaw.json`, `.env`  
โปรไฟล์การยืนยันตัวตนของโมเดล | `/home/node/.openclaw/agents/` | การ mount volume จากโฮสต์ | `agents/<agentId>/agent/auth-profiles.json` (OAuth, API keys)  
คีย์โปรไฟล์การยืนยันตัวตน | `/home/node/.config/openclaw/` | การ mount volume จากโฮสต์ | คีย์เข้ารหัสภายในเครื่องสำหรับวัสดุ token ของโปรไฟล์การยืนยันตัวตน OAuth  
การกำหนดค่า Skills | `/home/node/.openclaw/skills/` | การ mount volume จากโฮสต์ | สถานะระดับ Skill  
พื้นที่ทำงานของเอเจนต์ | `/home/node/.openclaw/workspace/` | การ mount volume จากโฮสต์ | โค้ดและ artifact ของเอเจนต์  
เซสชัน WhatsApp | `/home/node/.openclaw/` | การ mount volume จากโฮสต์ | เก็บรักษาการเข้าสู่ระบบด้วย QR  
keyring ของ Gmail | `/home/node/.openclaw/` | volume ของโฮสต์ + รหัสผ่าน | ต้องใช้ `GOG_KEYRING_PASSWORD`  
แพ็กเกจ Plugin | `/home/node/.openclaw/npm`, `/home/node/.openclaw/git` | การ mount volume จากโฮสต์ | รากของแพ็กเกจ Plugin ที่ดาวน์โหลดได้  
ไบนารีภายนอก | `/usr/local/bin/` | อิมเมจ Docker | ต้องใส่ไว้ในช่วง build  
runtime ของ Node | ระบบไฟล์ของคอนเทนเนอร์ | อิมเมจ Docker | สร้างใหม่ทุกครั้งที่ build อิมเมจ  
แพ็กเกจ OS | ระบบไฟล์ของคอนเทนเนอร์ | อิมเมจ Docker | อย่าติดตั้งตอน runtime  
คอนเทนเนอร์ Docker | ชั่วคราว | รีสตาร์ทได้ | ลบทิ้งได้อย่างปลอดภัย  
  
## การอัปเดต

หากต้องการอัปเดต OpenClaw บน VM:

bashCopy code
[code]
    git pulldocker compose builddocker compose up -d
[/code]

## ที่เกี่ยวข้อง

  * [Docker](</th/install/docker>)
  * [Podman](</th/install/podman>)
  * [ClawDock](</th/install/clawdock>)


Was this useful?YesNo