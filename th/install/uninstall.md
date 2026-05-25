---
title: ถอนการติดตั้ง
source_url: https://docs.openclaw.ai/th/install/uninstall
scraped_at: 2026-05-25
---

มี 2 เส้นทาง:

  * **เส้นทางง่าย** หากยังติดตั้ง `openclaw` อยู่
  * **ลบบริการด้วยตนเอง** หาก CLI ถูกลบไปแล้ว แต่บริการยังคงทำงานอยู่


## เส้นทางง่าย (ยังติดตั้ง CLI อยู่)

แนะนำ: ใช้ตัวถอนการติดตั้งที่มีมาในตัว:

bashCopy code
[code]
    openclaw uninstall
[/code]

แบบไม่โต้ตอบ (automation / npx):

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

ขั้นตอนแบบ manual (ได้ผลลัพธ์เหมือนกัน):

  1. หยุดบริการ gateway:

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. ถอนการติดตั้งบริการ gateway (launchd/systemd/schtasks):

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. ลบ state + config:

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

หากคุณตั้ง `OPENCLAW_CONFIG_PATH` ไปยังตำแหน่งแบบกำหนดเองที่อยู่นอก state dir ให้ลบไฟล์นั้นด้วย

  4. ลบ workspace ของคุณ (ไม่บังคับ, จะลบไฟล์ของเอเจนต์):

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. ลบการติดตั้ง CLI (เลือกตามที่คุณใช้):

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. หากคุณติดตั้งแอป macOS:

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

หมายเหตุ:

  * หากคุณใช้โปรไฟล์ (`--profile` / `OPENCLAW_PROFILE`) ให้ทำขั้นตอนที่ 3 ซ้ำสำหรับแต่ละ state dir (ค่าปริยายคือ `~/.openclaw-<profile>`)
  * ในโหมด remote, state dir จะอยู่บน **โฮสต์ gateway** ดังนั้นให้ทำขั้นตอนที่ 1-4 บนเครื่องนั้นด้วย


## ลบบริการด้วยตนเอง (ไม่ได้ติดตั้ง CLI แล้ว)

ใช้วิธีนี้หากบริการ gateway ยังทำงานต่อ แต่ไม่มี `openclaw` แล้ว

### macOS (launchd)

label ค่าปริยายคือ `ai.openclaw.gateway` (หรือ `ai.openclaw.<profile>`; legacy `com.openclaw.*` อาจยังคงมีอยู่):

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

หากคุณใช้โปรไฟล์ ให้แทนที่ label และชื่อ plist ด้วย `ai.openclaw.<profile>` ลบ plist แบบ legacy `com.openclaw.*` หากมีอยู่ด้วย

### Linux (systemd user unit)

ชื่อ unit ค่าปริยายคือ `openclaw-gateway.service` (หรือ `openclaw-gateway-<profile>.service`):

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows (Scheduled Task)

ชื่องานค่าปริยายคือ `OpenClaw Gateway` (หรือ `OpenClaw Gateway (<profile>)`) สคริปต์ของงานจะอยู่ภายใต้ state dir ของคุณ

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
[/code]

หากคุณใช้โปรไฟล์ ให้ลบชื่องานที่ตรงกันและ `~\.openclaw-<profile>\gateway.cmd`

## การติดตั้งปกติ vs source checkout

### การติดตั้งปกติ (`install.sh` / npm / pnpm / bun)

หากคุณใช้ `https://openclaw.ai/install.sh` หรือ `install.ps1`, CLI จะถูกติดตั้งด้วย `npm install -g openclaw@latest` ให้ลบด้วย `npm rm -g openclaw` (หรือ `pnpm remove -g` / `bun remove -g` หากคุณติดตั้งด้วยวิธีนั้น)

### Source checkout (`git clone`)

หากคุณรันจาก repo checkout (`git clone` \+ `openclaw ...` / `bun run openclaw ...`):

  1. ถอนการติดตั้งบริการ gateway **ก่อน** ลบ repo (ใช้เส้นทางง่ายด้านบนหรือการลบบริการด้วยตนเอง)
  2. ลบไดเรกทอรี repo
  3. ลบ state + workspace ตามที่แสดงด้านบน


## ที่เกี่ยวข้อง

  * [ภาพรวมการติดตั้ง](</th/install>)
  * [คู่มือการย้ายระบบ](</th/install/migrating>)


Was this useful?YesNo