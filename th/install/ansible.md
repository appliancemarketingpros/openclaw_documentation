---
title: Ansible
source_url: https://docs.openclaw.ai/th/install/ansible
scraped_at: 2026-05-25
---

ปรับใช้ OpenClaw บนเซิร์ฟเวอร์สำหรับงานจริงด้วย **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** \-- ตัวติดตั้งอัตโนมัติที่มีสถาปัตยกรรมที่ให้ความสำคัญกับความปลอดภัยเป็นอันดับแรก

## ข้อกำหนดเบื้องต้น

ข้อกำหนด | รายละเอียด  
---|---  
**OS** | Debian 11+ หรือ Ubuntu 20.04+  
**การเข้าถึง** | สิทธิ์ Root หรือ sudo  
**เครือข่าย** | การเชื่อมต่ออินเทอร์เน็ตสำหรับการติดตั้งแพ็กเกจ  
**Ansible** | 2.14+ (ติดตั้งโดยอัตโนมัติด้วยสคริปต์เริ่มต้นแบบด่วน)  
  
## สิ่งที่คุณจะได้รับ

  * **ความปลอดภัยแบบ Firewall-first** \-- การแยก UFW + Docker (เข้าถึงได้เฉพาะ SSH + Tailscale)
  * **Tailscale VPN** \-- การเข้าถึงจากระยะไกลอย่างปลอดภัยโดยไม่เปิดเผยบริการต่อสาธารณะ
  * **Docker** \-- คอนเทนเนอร์ sandbox แบบแยกส่วน ผูกกับ localhost เท่านั้น
  * **Defense in depth** \-- สถาปัตยกรรมความปลอดภัย 4 ชั้น
  * **การผสานรวม Systemd** \-- เริ่มต้นอัตโนมัติเมื่อบูตพร้อมการเสริมความปลอดภัย
  * **ตั้งค่าด้วยคำสั่งเดียว** \-- ปรับใช้เสร็จสมบูรณ์ในไม่กี่นาที


## เริ่มต้นแบบด่วน

ติดตั้งด้วยคำสั่งเดียว:

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## สิ่งที่ถูกติดตั้ง

Ansible playbook จะติดตั้งและกำหนดค่า:

  1. **Tailscale** \-- mesh VPN สำหรับการเข้าถึงจากระยะไกลอย่างปลอดภัย
  2. **ไฟร์วอลล์ UFW** \-- เฉพาะพอร์ต SSH + Tailscale
  3. **Docker CE + Compose V2** \-- สำหรับ backend sandbox ของ agent เริ่มต้น
  4. **Node.js 24 + pnpm** \-- การพึ่งพาสำหรับ runtime (Node 22 LTS ซึ่งปัจจุบันคือ `22.16+` ยังคงรองรับอยู่)
  5. **OpenClaw** \-- ทำงานบนโฮสต์ ไม่ได้อยู่ในคอนเทนเนอร์
  6. **บริการ Systemd** \-- เริ่มต้นอัตโนมัติพร้อมการเสริมความปลอดภัย


## การตั้งค่าหลังติดตั้ง

* ### สลับไปใช้ผู้ใช้ openclaw

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### เรียกใช้ตัวช่วยตั้งค่าเริ่มต้น

สคริปต์หลังติดตั้งจะแนะนำคุณตลอดการกำหนดค่าการตั้งค่า OpenClaw

* ### เชื่อมต่อผู้ให้บริการส่งข้อความ

เข้าสู่ระบบ WhatsApp, Telegram, Discord หรือ Signal:

bashCopy code
[code]
    openclaw channels login
[/code]

* ### ตรวจสอบการติดตั้ง

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### เชื่อมต่อกับ Tailscale

เข้าร่วม VPN mesh ของคุณเพื่อการเข้าถึงจากระยะไกลอย่างปลอดภัย

### คำสั่งด่วน

bashCopy code
[code]
    # Check service statussudo systemctl status openclaw # View live logssudo journalctl -u openclaw -f # Restart gatewaysudo systemctl restart openclaw # Provider login (run as openclaw user)sudo -i -u openclawopenclaw channels login
[/code]

## สถาปัตยกรรมความปลอดภัย

การปรับใช้นี้ใช้โมเดลการป้องกัน 4 ชั้น:

  1. **ไฟร์วอลล์ (UFW)** \-- เปิดเผยต่อสาธารณะเฉพาะ SSH (22) + Tailscale (41641/udp)
  2. **VPN (Tailscale)** \-- เข้าถึง Gateway ได้เฉพาะผ่าน VPN mesh
  3. **การแยก Docker** \-- เชน iptables ของ DOCKER-USER ป้องกันการเปิดเผยพอร์ตภายนอก
  4. **การเสริมความปลอดภัย Systemd** \-- NoNewPrivileges, PrivateTmp, ผู้ใช้ที่ไม่มีสิทธิ์พิเศษ


เพื่อตรวจสอบพื้นผิวการโจมตีจากภายนอกของคุณ:

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

ควรเปิดเฉพาะพอร์ต 22 (SSH) เท่านั้น บริการอื่นทั้งหมด (Gateway, Docker) จะถูกล็อกไว้

ติดตั้ง Docker สำหรับ sandbox ของ agent (การดำเนินการเครื่องมือแบบแยกส่วน) ไม่ใช่สำหรับการรัน Gateway เอง ดูการกำหนดค่า sandbox ได้ที่ [Multi-Agent Sandbox and Tools](</th/tools/multi-agent-sandbox-tools>)

## การติดตั้งด้วยตนเอง

หากคุณต้องการควบคุมการทำงานอัตโนมัติด้วยตนเอง:

* ### ติดตั้งข้อกำหนดเบื้องต้น

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### โคลน repository

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### ติดตั้ง Ansible collections

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### เรียกใช้ playbook

bashCopy code
[code]
    ./run-playbook.sh
[/code]

หรือเรียกใช้โดยตรงแล้วจึงเรียกใช้สคริปต์ตั้งค่าด้วยตนเองภายหลัง:

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Then run: /tmp/openclaw-setup.sh
[/code]

## การอัปเดต

ตัวติดตั้ง Ansible จะตั้งค่า OpenClaw สำหรับการอัปเดตด้วยตนเอง ดูขั้นตอนการอัปเดตมาตรฐานได้ที่ [Updating](</th/install/updating>)

หากต้องการเรียกใช้ Ansible playbook อีกครั้ง (เช่น สำหรับการเปลี่ยนแปลงการกำหนดค่า):

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

การทำงานนี้เป็นแบบ idempotent และสามารถเรียกใช้ซ้ำได้อย่างปลอดภัยหลายครั้ง

## การแก้ไขปัญหา

ไฟร์วอลล์บล็อกการเชื่อมต่อของฉัน

  * ตรวจสอบให้แน่ใจก่อนว่าคุณเข้าถึงผ่าน Tailscale VPN ได้
  * การเข้าถึง SSH (พอร์ต 22) อนุญาตไว้เสมอ
  * Gateway ถูกออกแบบมาให้เข้าถึงได้เฉพาะผ่าน Tailscale

บริการไม่เริ่มทำงาน bashCopy code
[code]
    # Check logssudo journalctl -u openclaw -n 100 # Verify permissionssudo ls -la /opt/openclaw # Test manual startsudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

ปัญหา Docker sandbox bashCopy code
[code]
    # Verify Docker is runningsudo systemctl status docker # Check sandbox imagesudo docker images | grep openclaw-sandbox # Build sandbox image if missing (requires source checkout)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# For npm installs without a source checkout, see# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

เข้าสู่ระบบผู้ให้บริการไม่สำเร็จ

ตรวจสอบให้แน่ใจว่าคุณกำลังทำงานในฐานะผู้ใช้ `openclaw`:

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## การกำหนดค่าขั้นสูง

สำหรับสถาปัตยกรรมความปลอดภัยและการแก้ไขปัญหาโดยละเอียด โปรดดูรีโป openclaw-ansible:

  * [สถาปัตยกรรมความปลอดภัย](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [รายละเอียดทางเทคนิค](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [คู่มือการแก้ไขปัญหา](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## ที่เกี่ยวข้อง

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- คู่มือการปรับใช้ฉบับสมบูรณ์
  * [Docker](</th/install/docker>) \-- การตั้งค่า Gateway แบบคอนเทนเนอร์
  * [Sandboxing](</th/gateway/sandboxing>) \-- การกำหนดค่า sandbox ของ agent
  * [Multi-Agent Sandbox and Tools](</th/tools/multi-agent-sandbox-tools>) \-- การแยกส่วนต่อ agent


Was this useful?YesNo