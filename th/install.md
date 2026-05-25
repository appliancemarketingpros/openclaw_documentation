---
title: ติดตั้ง
source_url: https://docs.openclaw.ai/th/install
scraped_at: 2026-05-25
---

## ข้อกำหนดของระบบ

  * **Node 24** (แนะนำ) หรือ Node 22.16+ - สคริปต์ติดตั้งจัดการเรื่องนี้ให้อัตโนมัติ
  * **macOS, Linux หรือ Windows** \- รองรับทั้ง Windows แบบเนทีฟและ WSL2; WSL2 มีความเสถียรมากกว่า ดู [Windows](</th/platforms/windows>)
  * จำเป็นต้องใช้ `pnpm` เฉพาะเมื่อคุณ build จากซอร์ส


## แนะนำ: สคริปต์ติดตั้ง

วิธีติดตั้งที่เร็วที่สุด โดยจะตรวจหา OS ของคุณ ติดตั้ง Node หากจำเป็น ติดตั้ง OpenClaw และเริ่ม onboarding

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

หากต้องการติดตั้งโดยไม่รัน onboarding:

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

สำหรับ flags ทั้งหมดและตัวเลือก CI/automation ดู [รายละเอียดภายในของตัวติดตั้ง](</th/install/installer>)

## วิธีติดตั้งทางเลือก

### ตัวติดตั้งแบบ local prefix (`install-cli.sh`)

ใช้วิธีนี้เมื่อคุณต้องการเก็บ OpenClaw และ Node ไว้ใต้ local prefix เช่น `~/.openclaw` โดยไม่ต้องพึ่งการติดตั้ง Node ระดับทั้งระบบ:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

โดยค่าเริ่มต้นรองรับการติดตั้งผ่าน npm รวมถึงการติดตั้งแบบ git-checkout ภายใต้ flow prefix เดียวกัน อ้างอิงฉบับเต็ม: [รายละเอียดภายในของตัวติดตั้ง](</th/install/installer#install-clish>)

ติดตั้งไว้แล้วใช่ไหม สลับระหว่างการติดตั้งแบบ package และ git ด้วย `openclaw update --channel dev` และ `openclaw update --channel stable` ดู [การอัปเดต](</th/install/updating#switch-between-npm-and-git-installs>)

### npm, pnpm หรือ bun

หากคุณจัดการ Node เองอยู่แล้ว:

### npm

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

### pnpm

bashCopy code
[code]
    pnpm add -g openclaw@latestpnpm approve-builds -gopenclaw onboard --install-daemon
[/code]

### bun

bashCopy code
[code]
    bun add -g openclaw@latestopenclaw onboard --install-daemon
[/code]

การแก้ไขปัญหา: ข้อผิดพลาดการ build ของ sharp (npm)

หาก `sharp` ล้มเหลวเนื่องจาก libvips ที่ติดตั้งแบบ global:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### จากซอร์ส

สำหรับผู้ร่วมพัฒนาหรือใครก็ตามที่ต้องการรันจาก checkout ภายในเครื่อง:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

หรือข้ามการ link แล้วใช้ `pnpm openclaw ...` จากภายใน repo ดู [การตั้งค่า](</th/start/setup>) สำหรับ workflow การพัฒนาแบบเต็ม

### ติดตั้งจาก GitHub main

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### Containers และ package managers

[**Docker** การ deploy แบบ containerized หรือ headless ](</th/install/docker>) [**Podman** ทางเลือก container แบบ rootless แทน Docker ](</th/install/podman>) [**Nix** การติดตั้งแบบ declarative ผ่าน Nix flake ](</th/install/nix>) [**Ansible** การ provision fleet แบบอัตโนมัติ ](</th/install/ansible>) [**Bun** การใช้งานเฉพาะ CLI ผ่านรันไทม์ Bun ](</th/install/bun>)

## ตรวจสอบการติดตั้ง

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

หากคุณต้องการ managed startup หลังติดตั้ง:

  * macOS: LaunchAgent ผ่าน `openclaw onboard --install-daemon` หรือ `openclaw gateway install`
  * Linux/WSL2: systemd user service ผ่านคำสั่งเดียวกัน
  * Windows แบบเนทีฟ: ใช้ Scheduled Task ก่อน โดยมีรายการ login ใน Startup-folder ต่อผู้ใช้เป็น fallback หากการสร้าง task ถูกปฏิเสธ


## Hosting และ deployment

Deploy OpenClaw บน cloud server หรือ VPS:

[**VPS** [**Docker VM** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii90aC9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** อัปเดต ย้าย หรือถอนการติดตั้ง [**การอัปเดต** ทำให้ OpenClaw เป็นปัจจุบันอยู่เสมอ ](</th/install/updating>) [**การย้าย** ย้ายไปยังเครื่องใหม่ ](</th/install/migrating>) [**ถอนการติดตั้ง** ลบ OpenClaw ออกทั้งหมด ](</th/install/uninstall>) การแก้ไขปัญหา: ไม่พบ `openclaw` หากติดตั้งสำเร็จแล้วแต่ไม่พบ `openclaw` ใน terminal ของคุณ: bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

หาก `$(npm prefix -g)/bin` ไม่อยู่ใน `$PATH` ของคุณ ให้เพิ่มลงในไฟล์ startup ของ shell (`~/.zshrc` หรือ `~/.bashrc`): bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

จากนั้นเปิด terminal ใหม่ ดู [การตั้งค่า Node](</th/install/node>) สำหรับรายละเอียดเพิ่มเติม ](</th/install/northflank>) Was this useful?YesNo ](</th/install/render>)](</th/install/railway>)](</th/install/azure>)](</th/install/gcp>)](</th/install/hetzner>)](</th/install/kubernetes>)](</th/install/docker-vm-runtime>)](</th/vps>)