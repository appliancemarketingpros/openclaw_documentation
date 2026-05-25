---
title: GCP
source_url: https://docs.openclaw.ai/th/install/gcp
scraped_at: 2026-05-25
---

เรียกใช้ OpenClaw Gateway แบบคงอยู่บน GCP Compute Engine VM โดยใช้ Docker พร้อมสถานะที่คงทน ไบนารีที่อบไว้ในอิมเมจ และพฤติกรรมการรีสตาร์ตที่ปลอดภัย

ถ้าคุณต้องการ "OpenClaw 24/7 ในราคาประมาณ ~$5-12/เดือน" นี่คือการตั้งค่าที่เชื่อถือได้บน Google Cloud ราคาจะแตกต่างกันไปตามประเภทเครื่องและภูมิภาค ให้เลือก VM ที่เล็กที่สุดที่เหมาะกับเวิร์กโหลดของคุณ และปรับขนาดขึ้นหากเจอ OOM

## เรากำลังทำอะไร (แบบเข้าใจง่าย)?

  * สร้างโปรเจกต์ GCP และเปิดใช้การเรียกเก็บเงิน
  * สร้าง Compute Engine VM
  * ติดตั้ง Docker (รันไทม์แอปแบบแยกขาด)
  * เริ่ม OpenClaw Gateway ใน Docker
  * คงสถานะ `~/.openclaw` \+ `~/.openclaw/workspace` ไว้บนโฮสต์ (อยู่รอดหลังรีสตาร์ต/สร้างใหม่)
  * เข้าถึง Control UI จากแล็ปท็อปของคุณผ่าน SSH tunnel


สถานะ `~/.openclaw` ที่เมานต์ไว้นั้นรวมถึง `openclaw.json`, `agents/<agentId>/agent/auth-profiles.json` ราย agent และ `.env`

Gateway สามารถเข้าถึงได้ผ่าน:

  * การ forward พอร์ต SSH จากแล็ปท็อปของคุณ
  * การเปิดพอร์ตโดยตรง หากคุณจัดการไฟร์วอลล์และโทเค็นเอง


คู่มือนี้ใช้ Debian บน GCP Compute Engine Ubuntu ก็ใช้ได้เช่นกัน ให้แมปแพ็กเกจให้สอดคล้องกัน สำหรับโฟลว์ Docker ทั่วไป ดู [Docker](</th/install/docker>)

* * *

## เส้นทางด่วน (สำหรับผู้ปฏิบัติงานที่มีประสบการณ์)

  1. สร้างโปรเจกต์ GCP + เปิดใช้ Compute Engine API
  2. สร้าง Compute Engine VM (e2-small, Debian 12, 20GB)
  3. SSH เข้า VM
  4. ติดตั้ง Docker
  5. โคลนรีโพซิทอรี OpenClaw
  6. สร้างไดเรกทอรีโฮสต์แบบคงอยู่
  7. กำหนดค่า `.env` และ `docker-compose.yml`
  8. อบไบนารีที่จำเป็น สร้างอิมเมจ และเปิดใช้งาน


* * *

## สิ่งที่คุณต้องมี

  * บัญชี GCP (มีสิทธิ์ใช้ free tier สำหรับ e2-micro)
  * ติดตั้ง gcloud CLI แล้ว (หรือใช้ Cloud Console)
  * การเข้าถึง SSH จากแล็ปท็อปของคุณ
  * ความคุ้นเคยพื้นฐานกับ SSH + คัดลอก/วาง
  * ประมาณ 20-30 นาที
  * Docker และ Docker Compose
  * ข้อมูลรับรองการยืนยันตัวตนของโมเดล
  * ข้อมูลรับรองผู้ให้บริการเสริม 
    * WhatsApp QR
    * Telegram bot token
    * Gmail OAuth


* * *

* ### ติดตั้ง gcloud CLI (หรือใช้ Console)

**ตัวเลือก A: gcloud CLI** (แนะนำสำหรับระบบอัตโนมัติ)

ติดตั้งจาก <https://cloud.google.com/sdk/docs/install>

เริ่มต้นและยืนยันตัวตน:

bashCopy code
[code]
    gcloud initgcloud auth login
[/code]

**ตัวเลือก B: Cloud Console**

ทุกขั้นตอนสามารถทำผ่าน UI บนเว็บได้ที่ <https://console.cloud.google.com>

* ### สร้างโปรเจกต์ GCP

**CLI:**

bashCopy code
[code]
    gcloud projects create my-openclaw-project --name="OpenClaw Gateway"gcloud config set project my-openclaw-project
[/code]

เปิดใช้การเรียกเก็บเงินที่ <https://console.cloud.google.com/billing> (จำเป็นสำหรับ Compute Engine)

เปิดใช้ Compute Engine API:

bashCopy code
[code]
    gcloud services enable compute.googleapis.com
[/code]

**Console:**

  1. ไปที่ IAM & Admin > Create Project
  2. ตั้งชื่อและสร้าง
  3. เปิดใช้การเรียกเก็บเงินสำหรับโปรเจกต์
  4. ไปที่ APIs & Services > Enable APIs > ค้นหา "Compute Engine API" > Enable


* ### สร้าง VM

**ประเภทเครื่อง:**

ประเภท | สเปก | ค่าใช้จ่าย | หมายเหตุ  
---|---|---|---  
e2-medium | 2 vCPU, RAM 4GB | ประมาณ $25/เดือน | เชื่อถือได้ที่สุดสำหรับการ build Docker ในเครื่อง  
e2-small | 2 vCPU, RAM 2GB | ประมาณ $12/เดือน | ขั้นต่ำที่แนะนำสำหรับการ build Docker  
e2-micro | 2 vCPU (shared), RAM 1GB | มีสิทธิ์ใช้ free tier | มักล้มเหลวด้วย OOM ระหว่าง Docker build (exit 137)  
  
**CLI:**

bashCopy code
[code]
    gcloud compute instances create openclaw-gateway \  --zone=us-central1-a \  --machine-type=e2-small \  --boot-disk-size=20GB \  --image-family=debian-12 \  --image-project=debian-cloud
[/code]

**Console:**

  1. ไปที่ Compute Engine > VM instances > Create instance
  2. ชื่อ: `openclaw-gateway`
  3. ภูมิภาค: `us-central1`, โซน: `us-central1-a`
  4. ประเภทเครื่อง: `e2-small`
  5. ดิสก์บูต: Debian 12, 20GB
  6. สร้าง


* ### SSH เข้า VM

**CLI:**

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
[/code]

**Console:**

คลิกปุ่ม "SSH" ข้าง VM ของคุณในแดชบอร์ด Compute Engine

หมายเหตุ: การเผยแพร่คีย์ SSH อาจใช้เวลา 1-2 นาทีหลังสร้าง VM หากการเชื่อมต่อถูกปฏิเสธ ให้รอแล้วลองใหม่

* ### ติดตั้ง Docker (บน VM)

bashCopy code
[code]
    sudo apt-get updatesudo apt-get install -y git curl ca-certificatescurl -fsSL https://get.docker.com | sudo shsudo usermod -aG docker $USER
[/code]

ออกจากระบบแล้วเข้าสู่ระบบใหม่เพื่อให้การเปลี่ยนกลุ่มมีผล:

bashCopy code
[code]
    exit
[/code]

จากนั้น SSH กลับเข้าไป:

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
[/code]

ตรวจสอบ:

bashCopy code
[code]
    docker --versiondocker compose version
[/code]

* ### โคลนรีโพซิทอรี OpenClaw

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclaw
[/code]

คู่มือนี้สมมติว่าคุณจะ build อิมเมจแบบกำหนดเองเพื่อรับประกันการคงอยู่ของไบนารี

* ### สร้างไดเรกทอรีโฮสต์แบบคงอยู่

Docker containers เป็นแบบชั่วคราว สถานะที่ต้องอยู่ยาวทั้งหมดต้องอยู่บนโฮสต์

bashCopy code
[code]
    mkdir -p ~/.openclawmkdir -p ~/.openclaw/workspace
[/code]

* ### กำหนดค่าตัวแปรสภาพแวดล้อม

สร้าง `.env` ในรากของรีโพซิทอรี

bashCopy code
[code]
    OPENCLAW_IMAGE=openclaw:latestOPENCLAW_GATEWAY_TOKEN=OPENCLAW_GATEWAY_BIND=lanOPENCLAW_GATEWAY_PORT=18789 OPENCLAW_CONFIG_DIR=/home/$USER/.openclawOPENCLAW_WORKSPACE_DIR=/home/$USER/.openclaw/workspace GOG_KEYRING_PASSWORD=XDG_CONFIG_HOME=/home/node/.openclaw
[/code]

ตั้งค่า `OPENCLAW_GATEWAY_TOKEN` เมื่อคุณต้องการจัดการโทเค็น Gateway ที่เสถียรผ่าน `.env`; มิฉะนั้นให้กำหนดค่า `gateway.auth.token` ก่อนพึ่งพาไคลเอนต์ข้ามการรีสตาร์ต หากไม่มีแหล่งใดอยู่เลย OpenClaw จะใช้โทเค็นเฉพาะรันไทม์สำหรับการเริ่มต้นครั้งนั้น สร้างรหัสผ่าน keyring แล้ววางลงใน `GOG_KEYRING_PASSWORD`:

bashCopy code
[code]
    openssl rand -hex 32
[/code]

**อย่า commit ไฟล์นี้**

ไฟล์ `.env` นี้มีไว้สำหรับ env ของ container/runtime เช่น `OPENCLAW_GATEWAY_TOKEN` การยืนยันตัวตน OAuth/API-key ของผู้ให้บริการที่จัดเก็บไว้จะอยู่ใน `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` ที่เมานต์ไว้

* ### การกำหนดค่า Docker Compose

สร้างหรืออัปเดต `docker-compose.yml`

yamlCopy code
[code]
    services:  openclaw-gateway:    image: ${OPENCLAW_IMAGE}    build: .    restart: unless-stopped    env_file:      - .env    environment:      - HOME=/home/node      - NODE_ENV=production      - TERM=xterm-256color      - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}      - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}      - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}      - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}      - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin    volumes:      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace    ports:      # Recommended: keep the Gateway loopback-only on the VM; access via SSH tunnel.      # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.      - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"    command:      [        "node",        "dist/index.js",        "gateway",        "--bind",        "${OPENCLAW_GATEWAY_BIND}",        "--port",        "${OPENCLAW_GATEWAY_PORT}",        "--allow-unconfigured",      ]
[/code]

`--allow-unconfigured` มีไว้เพื่อความสะดวกในการ bootstrap เท่านั้น ไม่ใช่สิ่งทดแทนการกำหนดค่า gateway ที่เหมาะสม ให้ตั้งค่าการยืนยันตัวตน (`gateway.auth.token` หรือรหัสผ่าน) และใช้การตั้งค่า bind ที่ปลอดภัยสำหรับการ deploy ของคุณอยู่ดี

* ### ขั้นตอนรันไทม์ Docker VM ที่ใช้ร่วมกัน

ใช้คู่มือรันไทม์ที่ใช้ร่วมกันสำหรับโฟลว์โฮสต์ Docker ทั่วไป:

  * [อบไบนารีที่จำเป็นลงในอิมเมจ](</th/install/docker-vm-runtime#bake-required-binaries-into-the-image>)
  * [Build และเปิดใช้งาน](</th/install/docker-vm-runtime#build-and-launch>)
  * [อะไรคงอยู่ที่ไหน](</th/install/docker-vm-runtime#what-persists-where>)
  * [การอัปเดต](</th/install/docker-vm-runtime#updates>)


* ### หมายเหตุการเปิดใช้งานเฉพาะ GCP

บน GCP หาก build ล้มเหลวด้วย `Killed` หรือ `exit code 137` ระหว่าง `pnpm install --frozen-lockfile` แปลว่า VM หน่วยความจำไม่พอ ใช้ `e2-small` เป็นอย่างน้อย หรือ `e2-medium` เพื่อให้การ build ครั้งแรกเชื่อถือได้มากขึ้น

เมื่อ bind เข้ากับ LAN (`OPENCLAW_GATEWAY_BIND=lan`) ให้กำหนดค่า browser origin ที่เชื่อถือได้ก่อนดำเนินการต่อ:

bashCopy code
[code]
    docker compose run --rm openclaw-cli config set gateway.controlUi.allowedOrigins '["http://127.0.0.1:18789"]' --strict-json
[/code]

หากคุณเปลี่ยนพอร์ต Gateway ให้แทนที่ `18789` ด้วยพอร์ตที่คุณกำหนดค่าไว้

* ### เข้าถึงจากแล็ปท็อปของคุณ

สร้าง SSH tunnel เพื่อ forward พอร์ต Gateway:

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a -- -L 18789:127.0.0.1:18789
[/code]

เปิดในเบราว์เซอร์ของคุณ:

`http://127.0.0.1:18789/`

พิมพ์ลิงก์แดชบอร์ดแบบสะอาดอีกครั้ง:

bashCopy code
[code]
    docker compose run --rm openclaw-cli dashboard --no-open
[/code]

หาก UI แจ้งให้ป้อนการยืนยันตัวตนแบบ shared-secret ให้วางโทเค็นหรือรหัสผ่านที่กำหนดค่าไว้ใน Control UI settings โฟลว์ Docker นี้จะเขียนโทเค็นตามค่าเริ่มต้น หากคุณเปลี่ยนการกำหนดค่า container เป็นการยืนยันตัวตนด้วยรหัสผ่าน ให้ใช้รหัสผ่านนั้นแทน

หาก Control UI แสดง `unauthorized` หรือ `disconnected (1008): pairing required` ให้อนุมัติอุปกรณ์เบราว์เซอร์:

bashCopy code
[code]
    docker compose run --rm openclaw-cli devices listdocker compose run --rm openclaw-cli devices approve <requestId>
[/code]

ต้องการอ้างอิงเรื่อง persistence และการอัปเดตที่ใช้ร่วมกันอีกครั้งหรือไม่? ดู [Docker VM Runtime](</th/install/docker-vm-runtime#what-persists-where>) และ [การอัปเดต Docker VM Runtime](</th/install/docker-vm-runtime#updates>)

* * *

## การแก้ไขปัญหา

**การเชื่อมต่อ SSH ถูกปฏิเสธ**

การเผยแพร่คีย์ SSH อาจใช้เวลา 1-2 นาทีหลังสร้าง VM ให้รอแล้วลองใหม่

**ปัญหา OS Login**

ตรวจสอบโปรไฟล์ OS Login ของคุณ:

bashCopy code
[code]
    gcloud compute os-login describe-profile
[/code]

ตรวจสอบให้แน่ใจว่าบัญชีของคุณมีสิทธิ์ IAM ที่จำเป็น (Compute OS Login หรือ Compute OS Admin Login)

**หน่วยความจำไม่พอ (OOM)**

หาก Docker build ล้มเหลวด้วย `Killed` และ `exit code 137` แปลว่า VM ถูก OOM-killed ให้อัปเกรดเป็น e2-small (ขั้นต่ำ) หรือ e2-medium (แนะนำสำหรับการ build ในเครื่องที่เชื่อถือได้):

bashCopy code
[code]
    # Stop the VM firstgcloud compute instances stop openclaw-gateway --zone=us-central1-a # Change machine typegcloud compute instances set-machine-type openclaw-gateway \  --zone=us-central1-a \  --machine-type=e2-small # Start the VMgcloud compute instances start openclaw-gateway --zone=us-central1-a
[/code]

* * *

## Service accounts (แนวทางปฏิบัติที่ดีที่สุดด้านความปลอดภัย)

สำหรับการใช้งานส่วนตัว บัญชีผู้ใช้เริ่มต้นของคุณใช้ได้ดี

สำหรับระบบอัตโนมัติหรือ pipeline CI/CD ให้สร้าง service account เฉพาะพร้อมสิทธิ์ขั้นต่ำ:

  1. สร้าง service account:

bashCopy code
[code]gcloud iam service-accounts create openclaw-deploy \  --display-name="OpenClaw Deployment"
[/code]

  2. ให้บทบาท Compute Instance Admin (หรือบทบาทกำหนดเองที่แคบกว่า):

bashCopy code
[code]gcloud projects add-iam-policy-binding my-openclaw-project \  --member="serviceAccount:openclaw-deploy@my-openclaw-project.iam.gserviceaccount.com" \  --role="roles/compute.instanceAdmin.v1"
[/code]


หลีกเลี่ยงการใช้บทบาท Owner สำหรับระบบอัตโนมัติ ใช้หลักการให้สิทธิ์น้อยที่สุด

ดูรายละเอียดบทบาท IAM ได้ที่ <https://cloud.google.com/iam/docs/understanding-roles>

* * *

## ขั้นตอนถัดไป

  * ตั้งค่าช่องทางการส่งข้อความ: [ช่องทาง](</th/channels>)
  * จับคู่อุปกรณ์ภายในเครื่องเป็นโหนด: [โหนด](</th/nodes>)
  * กำหนดค่า Gateway: [การกำหนดค่า Gateway](</th/gateway/configuration>)


## ที่เกี่ยวข้อง

  * [ภาพรวมการติดตั้ง](</th/install>)
  * [Azure](</th/install/azure>)
  * [การโฮสต์ VPS](</th/vps>)


Was this useful?YesNo