---
title: Oracle Cloud
source_url: https://docs.openclaw.ai/th/install/oracle
scraped_at: 2026-05-25
---

เรียกใช้ OpenClaw Gateway แบบทำงานต่อเนื่องบน tier ARM **Always Free** ของ Oracle Cloud (สูงสุด 4 OCPU, RAM 24 GB, พื้นที่จัดเก็บ 200 GB) โดยไม่มีค่าใช้จ่าย

## ข้อกำหนดเบื้องต้น

  * บัญชี Oracle Cloud ([สมัครใช้งาน](<https://www.oracle.com/cloud/free/>)) -- ดู [คู่มือสมัครใช้งานจากชุมชน](<https://gist.github.com/rssnyder/51e3cfedd730e7dd5f4a816143b25dbd>) หากพบปัญหา
  * บัญชี Tailscale (ฟรีที่ [tailscale.com](<https://tailscale.com>))
  * คู่คีย์ SSH
  * เวลาประมาณ 30 นาที


## การตั้งค่า

* ### สร้างอินสแตนซ์ OCI

  1. เข้าสู่ระบบที่ [Oracle Cloud Console](<https://cloud.oracle.com/>)
  2. ไปที่ **Compute > Instances > Create Instance**
  3. กำหนดค่า: 
     * **ชื่อ:** `openclaw`
     * **อิมเมจ:** Ubuntu 24.04 (aarch64)
     * **Shape:** `VM.Standard.A1.Flex` (Ampere ARM)
     * **OCPU:** 2 (หรือสูงสุด 4)
     * **หน่วยความจำ:** 12 GB (หรือสูงสุด 24 GB)
     * **Boot volume:** 50 GB (ฟรีสูงสุด 200 GB)
     * **คีย์ SSH:** เพิ่มคีย์สาธารณะของคุณ
  4. คลิก **Create** และจดที่อยู่ IP สาธารณะไว้


* ### เชื่อมต่อและอัปเดตระบบ

bashCopy code
[code]
    ssh ubuntu@YOUR_PUBLIC_IP sudo apt update && sudo apt upgrade -ysudo apt install -y build-essential
[/code]

ต้องใช้ `build-essential` สำหรับการคอมไพล์ dependency บางรายการบน ARM

* ### กำหนดค่าผู้ใช้และ hostname

bashCopy code
[code]
    sudo hostnamectl set-hostname openclawsudo passwd ubuntusudo loginctl enable-linger ubuntu
[/code]

การเปิดใช้ linger จะทำให้บริการของผู้ใช้ทำงานต่อหลังจาก logout

* ### ติดตั้ง Tailscale

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | shsudo tailscale up --ssh --hostname=openclaw
[/code]

จากนี้ไป ให้เชื่อมต่อผ่าน Tailscale: `ssh ubuntu@openclaw`

* ### ติดตั้ง OpenClaw

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bashsource ~/.bashrc
[/code]

เมื่อระบบถามว่า "How do you want to hatch your bot?" ให้เลือก **Do this later**

* ### กำหนดค่า Gateway

ใช้การยืนยันตัวตนด้วย token ร่วมกับ Tailscale Serve เพื่อการเข้าถึงระยะไกลที่ปลอดภัย

bashCopy code
[code]
    openclaw config set gateway.bind loopbackopenclaw config set gateway.auth.mode tokenopenclaw doctor --generate-gateway-tokenopenclaw config set gateway.tailscale.mode serveopenclaw config set gateway.trustedProxies '["127.0.0.1"]' systemctl --user restart openclaw-gateway.service
[/code]

`gateway.trustedProxies=["127.0.0.1"]` ตรงนี้ใช้เฉพาะสำหรับการจัดการ forwarded-IP/local-client ของพร็อกซี Tailscale Serve ภายในเครื่องเท่านั้น และ **ไม่ใช่** `gateway.auth.mode: "trusted-proxy"` เส้นทาง diff viewer จะคงพฤติกรรม fail-closed ในการตั้งค่านี้: คำขอ viewer แบบ raw `127.0.0.1` ที่ไม่มี forwarded proxy headers อาจคืนค่า `Diff not found` ใช้ `mode=file` / `mode=both` สำหรับไฟล์แนบ หรือเปิดใช้ remote viewers โดยตั้งใจแล้วตั้งค่า `plugins.entries.diffs.config.viewerBaseUrl` (หรือส่งพร็อกซี `baseUrl`) หากคุณต้องการลิงก์ viewer ที่แชร์ได้

* ### ล็อกความปลอดภัยของ VCN

บล็อกทราฟฟิกทั้งหมดที่ขอบเครือข่าย ยกเว้น Tailscale:

  1. ไปที่ **Networking > Virtual Cloud Networks** ใน OCI Console
  2. คลิก VCN ของคุณ จากนั้นไปที่ **Security Lists > Default Security List**
  3. **ลบ** ingress rules ทั้งหมด ยกเว้น `0.0.0.0/0 UDP 41641` (Tailscale)
  4. คง egress rules เริ่มต้นไว้ (อนุญาต outbound ทั้งหมด)


การทำเช่นนี้จะบล็อก SSH บนพอร์ต 22, HTTP, HTTPS และสิ่งอื่นทั้งหมดที่ขอบเครือข่าย จากจุดนี้เป็นต้นไป คุณจะเชื่อมต่อได้ผ่าน Tailscale เท่านั้น

* ### ตรวจสอบ

bashCopy code
[code]
    openclaw --versionsystemctl --user status openclaw-gateway.servicetailscale serve statuscurl http://localhost:18789
[/code]

เข้าถึง Control UI จากอุปกรณ์ใดก็ได้บน tailnet ของคุณ:

CodeCopy code
[code]
    https://openclaw.<tailnet-name>.ts.net/
[/code]

แทนที่ `<tailnet-name>` ด้วยชื่อ tailnet ของคุณ (ดูได้ใน `tailscale status`)

## ตรวจสอบสถานะความปลอดภัย

เมื่อล็อก VCN แล้ว (เปิดเฉพาะ UDP 41641) และผูก Gateway กับ local loopback ทราฟฟิกสาธารณะจะถูกบล็อกที่ขอบเครือข่าย และการเข้าถึงของผู้ดูแลระบบจะจำกัดเฉพาะ tailnet เท่านั้น วิธีนี้ตัดความจำเป็นของขั้นตอน hardening VPS แบบดั้งเดิมหลายรายการ:

ขั้นตอนแบบดั้งเดิม | จำเป็นหรือไม่ | เหตุผล  
---|---|---  
ไฟร์วอลล์ UFW | ไม่ | VCN บล็อกทราฟฟิกก่อนที่จะถึงอินสแตนซ์  
fail2ban | ไม่ | พอร์ต 22 ถูกบล็อกที่ VCN จึงไม่มีพื้นผิวสำหรับ brute-force  
การ hardening sshd | ไม่ | Tailscale SSH ไม่ได้ใช้ sshd  
ปิดการเข้าสู่ระบบ root | ไม่ | Tailscale ยืนยันตัวตนด้วยข้อมูลประจำตัวของ tailnet ไม่ใช่ผู้ใช้ระบบ  
ยืนยันตัวตนด้วยคีย์ SSH เท่านั้น | ไม่ | เช่นเดียวกัน — ข้อมูลประจำตัวของ tailnet แทนที่คีย์ SSH ของระบบ  
การ hardening IPv6 | โดยปกติไม่จำเป็น | ขึ้นอยู่กับการตั้งค่า VCN/subnet; ตรวจสอบสิ่งที่ถูกกำหนด/เปิดเผยจริง  
  
ยังแนะนำให้ทำ:

  * `chmod 700 ~/.openclaw` เพื่อจำกัดสิทธิ์ของไฟล์ข้อมูลรับรอง
  * `openclaw security audit` สำหรับการตรวจสอบสถานะความปลอดภัยเฉพาะของ OpenClaw
  * เรียกใช้ `sudo apt update && sudo apt upgrade` เป็นประจำสำหรับแพตช์ OS
  * ตรวจสอบอุปกรณ์ใน [คอนโซลผู้ดูแลระบบ Tailscale](<https://login.tailscale.com/admin>) เป็นระยะ


คำสั่งตรวจสอบอย่างรวดเร็ว:

bashCopy code
[code]
    # Confirm no public ports are listeningsudo ss -tlnp | grep -v '127.0.0.1\|::1' # Verify Tailscale SSH is activetailscale status | grep -q 'offers: ssh' && echo "Tailscale SSH active" # Optional: disable sshd entirely once Tailscale SSH is confirmed workingsudo systemctl disable --now ssh
[/code]

## หมายเหตุเกี่ยวกับ ARM

tier Always Free เป็น ARM (`aarch64`) ฟีเจอร์ส่วนใหญ่ของ OpenClaw ทำงานได้ดี มี native binaries จำนวนน้อยที่ต้องใช้ build สำหรับ ARM:

  * Node.js, Telegram, WhatsApp (Baileys): เป็น JavaScript ล้วน ไม่มีปัญหา
  * แพ็กเกจ npm ส่วนใหญ่ที่มีโค้ด native: มี artifact `linux-arm64` ที่ build ไว้ล่วงหน้า
  * ตัวช่วย CLI เสริม (เช่น ไบนารี Go/Rust ที่มาพร้อม skills): ตรวจสอบว่ามี release `aarch64` / `linux-arm64` ก่อนติดตั้ง


ตรวจสอบสถาปัตยกรรมด้วย `uname -m` (ควรพิมพ์ `aarch64`) สำหรับไบนารีที่ไม่มี build สำหรับ ARM ให้ติดตั้งจากซอร์สหรือข้ามไป

## การคงอยู่และการสำรองข้อมูล

สถานะของ OpenClaw อยู่ภายใต้:

  * `~/.openclaw/` — `openclaw.json`, `auth-profiles.json` ราย agent, สถานะของ channel/provider และข้อมูลเซสชัน
  * `~/.openclaw/workspace/` — workspace ของ agent ([SOUL.md](<http://SOUL.md>), memory, artifacts)


ข้อมูลเหล่านี้จะอยู่รอดหลังการรีบูต หากต้องการสร้าง snapshot แบบพกพา:

bashCopy code
[code]
    openclaw backup create
[/code]

## ทางเลือกสำรอง: SSH tunnel

หาก Tailscale Serve ไม่ทำงาน ให้ใช้ SSH tunnel จากเครื่องภายในของคุณ:

bashCopy code
[code]
    ssh -L 18789:127.0.0.1:18789 ubuntu@openclaw
[/code]

จากนั้นเปิด `http://localhost:18789`

## การแก้ไขปัญหา

**การสร้างอินสแตนซ์ล้มเหลว ("Out of capacity")** \-- อินสแตนซ์ ARM ของ free tier เป็นที่นิยม ให้ลองใช้ availability domain อื่น หรือลองใหม่ในช่วงเวลาที่มีการใช้งานน้อย

**Tailscale ไม่เชื่อมต่อ** \-- เรียกใช้ `sudo tailscale up --ssh --hostname=openclaw --reset` เพื่อยืนยันตัวตนใหม่

**Gateway ไม่เริ่มทำงาน** \-- เรียกใช้ `openclaw doctor --non-interactive` และตรวจสอบ log ด้วย `journalctl --user -u openclaw-gateway.service -n 50`

**ปัญหาไบนารี ARM** \-- แพ็กเกจ npm ส่วนใหญ่ทำงานบน ARM64 ได้ สำหรับ native binaries ให้มองหา release `linux-arm64` หรือ `aarch64` ตรวจสอบสถาปัตยกรรมด้วย `uname -m`

## ขั้นตอนถัดไป

  * [Channels](</th/channels>) \-- เชื่อมต่อ Telegram, WhatsApp, Discord และอื่นๆ
  * [การกำหนดค่า Gateway](</th/gateway/configuration>) \-- ตัวเลือกการกำหนดค่าทั้งหมด
  * [การอัปเดต](</th/install/updating>) \-- ทำให้ OpenClaw เป็นเวอร์ชันล่าสุดอยู่เสมอ


## ที่เกี่ยวข้อง

  * [ภาพรวมการติดตั้ง](</th/install>)
  * [GCP](</th/install/gcp>)
  * [โฮสติ้ง VPS](</th/vps>)


Was this useful?YesNo