---
title: Raspberry Pi
source_url: https://docs.openclaw.ai/th/install/raspberry-pi
scraped_at: 2026-05-25
---

เรียกใช้ OpenClaw Gateway แบบถาวรและทำงานตลอดเวลาบน Raspberry Pi เนื่องจาก Pi ทำหน้าที่เป็นเพียง Gateway (โมเดลทำงานในคลาวด์ผ่าน API) แม้แต่ Pi สเปกปานกลางก็รองรับงานได้ดี — ค่าอุปกรณ์ทั่วไปอยู่ที่ **$35–80 จ่ายครั้งเดียว** ไม่มีค่าบริการรายเดือน

## ความเข้ากันได้ของฮาร์ดแวร์

รุ่น Pi | RAM | ใช้ได้ไหม? | หมายเหตุ  
---|---|---|---  
Pi 5 | 4/8 GB | ดีที่สุด | เร็วที่สุด แนะนำ  
Pi 4 | 4 GB | ดี | จุดที่เหมาะสำหรับผู้ใช้ส่วนใหญ่  
Pi 4 | 2 GB | พอใช้ | เพิ่ม swap  
Pi 4 | 1 GB | คับแคบ | เป็นไปได้เมื่อใช้ swap และ config ขั้นต่ำ  
Pi 3B+ | 1 GB | ช้า | ใช้ได้แต่หน่วง  
Pi Zero 2 W | 512 MB | ไม่ได้ | ไม่แนะนำ  
  
**ขั้นต่ำ:** RAM 1 GB, 1 core, พื้นที่ว่างดิสก์ 500 MB, OS 64-bit **แนะนำ:** RAM 2 GB+, SD card 16 GB+ (หรือ USB SSD), Ethernet

## ข้อกำหนดเบื้องต้น

  * Raspberry Pi 4 หรือ 5 ที่มี RAM 2 GB+ (แนะนำ 4 GB)
  * การ์ด MicroSD (16 GB+) หรือ USB SSD (ประสิทธิภาพดีกว่า)
  * แหล่งจ่ายไฟ Pi อย่างเป็นทางการ
  * การเชื่อมต่อเครือข่าย (Ethernet หรือ WiFi)
  * Raspberry Pi OS 64-bit (จำเป็น -- อย่าใช้ 32-bit)
  * ประมาณ 30 นาที


## การตั้งค่า

* ### แฟลช OS

ใช้ **Raspberry Pi OS Lite (64-bit)** \-- ไม่ต้องมีเดสก์ท็อปสำหรับเซิร์ฟเวอร์แบบ headless

  1. ดาวน์โหลด [Raspberry Pi Imager](<https://www.raspberrypi.com/software/>)
  2. เลือก OS: **Raspberry Pi OS Lite (64-bit)**
  3. ในกล่องโต้ตอบการตั้งค่า ให้กำหนดค่าล่วงหน้า: 
     * Hostname: `gateway-host`
     * เปิดใช้ SSH
     * ตั้งชื่อผู้ใช้และรหัสผ่าน
     * กำหนดค่า WiFi (ถ้าไม่ได้ใช้ Ethernet)
  4. แฟลชลง SD card หรือไดรฟ์ USB ของคุณ ใส่เข้าเครื่อง แล้วบูต Pi


* ### เชื่อมต่อผ่าน SSH

bashCopy code
[code]
    ssh user@gateway-host
[/code]

* ### อัปเดตระบบ

bashCopy code
[code]
    sudo apt update && sudo apt upgrade -ysudo apt install -y git curl build-essential # Set timezone (important for cron and reminders)sudo timedatectl set-timezone America/Chicago
[/code]

* ### ติดตั้ง Node.js 24

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt install -y nodejsnode --version
[/code]

* ### เพิ่ม swap (สำคัญสำหรับ 2 GB หรือน้อยกว่า)

bashCopy code
[code]
    sudo fallocate -l 2G /swapfilesudo chmod 600 /swapfilesudo mkswap /swapfilesudo swapon /swapfileecho '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab # Reduce swappiness for low-RAM devicesecho 'vm.swappiness=10' | sudo tee -a /etc/sysctl.confsudo sysctl -p
[/code]

* ### ติดตั้ง OpenClaw

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

* ### เรียกใช้การเริ่มต้นใช้งาน

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

ทำตามวิซาร์ด แนะนำให้ใช้ API keys แทน OAuth สำหรับอุปกรณ์แบบ headless Telegram เป็นช่องทางที่เริ่มใช้ง่ายที่สุด

* ### ตรวจสอบ

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### เข้าถึง Control UI

บนคอมพิวเตอร์ของคุณ รับ URL แดชบอร์ดจาก Pi:

bashCopy code
[code]
    ssh user@gateway-host 'openclaw dashboard --no-open'
[/code]

จากนั้นสร้าง SSH tunnel ในเทอร์มินัลอีกอัน:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@gateway-host
[/code]

เปิด URL ที่พิมพ์ออกมาในเบราว์เซอร์ภายในเครื่องของคุณ สำหรับการเข้าถึงระยะไกลแบบทำงานตลอดเวลา ดู [การผสานรวม Tailscale](</th/gateway/tailscale>)

## เคล็ดลับด้านประสิทธิภาพ

**ใช้ USB SSD** \-- SD card ช้าและเสื่อมสภาพได้ USB SSD ช่วยเพิ่มประสิทธิภาพได้อย่างมาก ดู [คู่มือการบูต Pi ผ่าน USB](<https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#usb-mass-storage-boot>)

**เปิดใช้แคชการคอมไพล์โมดูล** \-- เร่งความเร็วการเรียกใช้ CLI ซ้ำ ๆ บนโฮสต์ Pi ที่ใช้พลังงานต่ำกว่า:

bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF' # pragma: allowlist secretexport NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

**ลดการใช้หน่วยความจำ** \-- สำหรับการตั้งค่าแบบ headless ให้คืนหน่วยความจำ GPU และปิดบริการที่ไม่ได้ใช้:

bashCopy code
[code]
    echo 'gpu_mem=16' | sudo tee -a /boot/config.txtsudo systemctl disable bluetooth
[/code]

**systemd drop-in สำหรับการรีสตาร์ตที่เสถียร** \-- ถ้า Pi เครื่องนี้ใช้รัน OpenClaw เป็นหลัก ให้เพิ่ม service drop-in:

bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

จากนั้นเรียกใช้ `systemctl --user daemon-reload && systemctl --user restart openclaw-gateway.service` บน Pi แบบ headless ให้เปิดใช้ lingering หนึ่งครั้งด้วย เพื่อให้บริการของผู้ใช้ยังทำงานต่อหลังออกจากระบบ: `sudo loginctl enable-linger "$(whoami)"`

## การตั้งค่าโมเดลที่แนะนำ

เนื่องจาก Pi รันเฉพาะ Gateway ให้ใช้โมเดล API ที่โฮสต์บนคลาวด์:

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-sonnet-4-6",        "fallbacks": ["openai/gpt-5.4-mini"]      }    }  }}
[/code]

อย่ารัน LLM ภายในเครื่องบน Pi — แม้แต่โมเดลขนาดเล็กก็ช้าเกินกว่าจะใช้งานได้จริง ให้ Claude หรือ GPT ทำงานด้านโมเดลแทน

## หมายเหตุเกี่ยวกับไบนารี ARM

ฟีเจอร์ส่วนใหญ่ของ OpenClaw ทำงานบน ARM64 ได้โดยไม่ต้องเปลี่ยนแปลง (Node.js, Telegram, WhatsApp/Baileys, Chromium) ไบนารีที่บางครั้งไม่มี build สำหรับ ARM มักเป็นเครื่องมือ Go/Rust CLI ที่เป็นตัวเลือกและมาพร้อมกับ Skills ตรวจสอบหน้า release ของไบนารีที่หายไปว่ามี artifact สำหรับ `linux-arm64` / `aarch64` ก่อนจะย้อนกลับไป build จากซอร์ส

## ความคงอยู่ของข้อมูลและการสำรองข้อมูล

สถานะของ OpenClaw อยู่ภายใต้:

  * `~/.openclaw/` — `openclaw.json`, `auth-profiles.json` แยกตาม agent, สถานะช่องทาง/ผู้ให้บริการ, เซสชัน
  * `~/.openclaw/workspace/` — workspace ของ agent ([SOUL.md](<http://SOUL.md>), หน่วยความจำ, artifacts)


ข้อมูลเหล่านี้ยังอยู่หลังรีบูต สร้าง snapshot แบบพกพาได้ด้วย:

bashCopy code
[code]
    openclaw backup create
[/code]

ถ้าคุณเก็บข้อมูลเหล่านี้บน SSD ทั้งประสิทธิภาพและอายุการใช้งานจะดีกว่า SD card

## การแก้ปัญหา

**หน่วยความจำไม่พอ** \-- ตรวจสอบว่า swap ทำงานอยู่ด้วย `free -h` ปิดบริการที่ไม่ได้ใช้ (`sudo systemctl disable cups bluetooth avahi-daemon`) ใช้เฉพาะโมเดลที่อิง API

**ประสิทธิภาพช้า** \-- ใช้ USB SSD แทน SD card ตรวจสอบการถูกจำกัดความเร็ว CPU ด้วย `vcgencmd get_throttled` (ควรคืนค่า `0x0`)

**บริการไม่เริ่มทำงาน** \-- ตรวจสอบบันทึกด้วย `journalctl --user -u openclaw-gateway.service --no-pager -n 100` และเรียกใช้ `openclaw doctor --non-interactive` ถ้านี่เป็น Pi แบบ headless ให้ตรวจสอบด้วยว่าเปิดใช้ lingering แล้ว: `sudo loginctl enable-linger "$(whoami)"`

**ปัญหาไบนารี ARM** \-- ถ้า skill ล้มเหลวพร้อมข้อความ "exec format error" ให้ตรวจสอบว่าไบนารีมี build สำหรับ ARM64 หรือไม่ ตรวจสอบสถาปัตยกรรมด้วย `uname -m` (ควรแสดง `aarch64`)

**WiFi หลุด** \-- ปิดการจัดการพลังงาน WiFi: `sudo iwconfig wlan0 power off`

## ขั้นตอนถัดไป

  * [ช่องทาง](</th/channels>) \-- เชื่อมต่อ Telegram, WhatsApp, Discord และอื่น ๆ
  * [การกำหนดค่า Gateway](</th/gateway/configuration>) \-- ตัวเลือก config ทั้งหมด
  * [การอัปเดต](</th/install/updating>) \-- ทำให้ OpenClaw เป็นเวอร์ชันล่าสุดอยู่เสมอ


## ที่เกี่ยวข้อง

  * [ภาพรวมการติดตั้ง](</th/install>)
  * [เซิร์ฟเวอร์ Linux](</th/vps>)
  * [แพลตฟอร์ม](</th/platforms>)


Was this useful?YesNo