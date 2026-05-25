---
title: Node.js
source_url: https://docs.openclaw.ai/th/install/node
scraped_at: 2026-05-25
---

OpenClaw ต้องใช้ **Node 22.16 หรือใหม่กว่า** **Node 24 เป็น runtime เริ่มต้นและที่แนะนำ** สำหรับการติดตั้ง, CI และเวิร์กโฟลว์การเผยแพร่ Node 22 ยังรองรับผ่านสาย LTS ที่ยังใช้งานอยู่ [สคริปต์ติดตั้ง](</th/install#alternative-install-methods>) จะตรวจจับและติดตั้ง Node โดยอัตโนมัติ - หน้านี้มีไว้สำหรับกรณีที่คุณต้องการตั้งค่า Node ด้วยตนเองและตรวจสอบให้แน่ใจว่าทุกอย่างเชื่อมต่อถูกต้อง (เวอร์ชัน, PATH, การติดตั้งแบบ global)

## ตรวจสอบเวอร์ชันของคุณ

bashCopy code
[code]
    node -v
[/code]

หากคำสั่งนี้แสดง `v24.x.x` หรือสูงกว่า แสดงว่าคุณอยู่บนค่าเริ่มต้นที่แนะนำ หากแสดง `v22.16.x` หรือสูงกว่า แสดงว่าคุณอยู่บนเส้นทาง Node 22 LTS ที่รองรับ แต่เรายังคงแนะนำให้อัปเกรดเป็น Node 24 เมื่อสะดวก หากยังไม่ได้ติดตั้ง Node หรือเวอร์ชันเก่าเกินไป ให้เลือกวิธีติดตั้งด้านล่าง

## ติดตั้ง Node

### macOS

**Homebrew** (แนะนำ):

bashCopy code
[code]
    brew install node
[/code]

หรือดาวน์โหลดตัวติดตั้ง macOS จาก [nodejs.org](<https://nodejs.org/>)

### Linux

**Ubuntu / Debian:**

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt-get install -y nodejs
[/code]

**Fedora / RHEL:**

bashCopy code
[code]
    sudo dnf install nodejs
[/code]

หรือใช้ตัวจัดการเวอร์ชัน (ดูด้านล่าง)

### Windows

**winget** (แนะนำ):

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey:**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

หรือดาวน์โหลดตัวติดตั้ง Windows จาก [nodejs.org](<https://nodejs.org/>)

การใช้ตัวจัดการเวอร์ชัน (nvm, fnm, mise, asdf)

ตัวจัดการเวอร์ชันช่วยให้คุณสลับระหว่างเวอร์ชันของ Node ได้ง่าย ตัวเลือกยอดนิยม:

  * [**fnm**](<https://github.com/Schniz/fnm>) \- รวดเร็ว ใช้ได้ข้ามแพลตฟอร์ม
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- ใช้งานแพร่หลายบน macOS/Linux
  * [**mise**](<https://mise.jdx.dev/>) \- รองรับหลายภาษา (Node, Python, Ruby ฯลฯ)


ตัวอย่างด้วย fnm:

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## การแก้ไขปัญหา

### `openclaw: command not found`

ปัญหานี้เกือบทุกครั้งหมายความว่าไดเรกทอรี global bin ของ npm ไม่ได้อยู่ใน PATH ของคุณ

* ### ค้นหา global npm prefix ของคุณ

bashCopy code
[code]
    npm prefix -g
[/code]

* ### ตรวจสอบว่าอยู่ใน PATH ของคุณหรือไม่

bashCopy code
[code]
    echo "$PATH"
[/code]

มองหา `<npm-prefix>/bin` (macOS/Linux) หรือ `<npm-prefix>` (Windows) ในผลลัพธ์

* ### เพิ่มลงในไฟล์เริ่มต้นของเชลล์

### macOS / Linux

เพิ่มลงใน `~/.zshrc` หรือ `~/.bashrc`:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

จากนั้นเปิดเทอร์มินัลใหม่ (หรือรัน `rehash` ใน zsh / `hash -r` ใน bash)

### Windows

เพิ่มผลลัพธ์ของ `npm prefix -g` ลงใน PATH ของระบบผ่าน Settings → System → Environment Variables

### ข้อผิดพลาดด้านสิทธิ์ใน `npm install -g` (Linux)

หากคุณเห็นข้อผิดพลาด `EACCES` ให้เปลี่ยน global prefix ของ npm ไปยังไดเรกทอรีที่ผู้ใช้เขียนได้:

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

เพิ่มบรรทัด `export PATH=...` ลงใน `~/.bashrc` หรือ `~/.zshrc` เพื่อให้มีผลถาวร

## ที่เกี่ยวข้อง

  * [ภาพรวมการติดตั้ง](</th/install>) \- วิธีติดตั้งทั้งหมด
  * [การอัปเดต](</th/install/updating>) \- การทำให้ OpenClaw เป็นปัจจุบันอยู่เสมอ
  * [เริ่มต้นใช้งาน](</th/start/getting-started>) \- ขั้นตอนแรกหลังการติดตั้ง


Was this useful?YesNo