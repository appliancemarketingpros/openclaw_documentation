---
title: การแก้ไขปัญหาเบราว์เซอร์
source_url: https://docs.openclaw.ai/th/tools/browser-linux-troubleshooting
scraped_at: 2026-05-25
---

## ปัญหา: "Failed to start Chrome CDP on port 18800"

เซิร์ฟเวอร์ควบคุมเบราว์เซอร์ของ OpenClaw เปิด Chrome/Brave/Edge/Chromium ไม่สำเร็จพร้อมข้อผิดพลาด:

CodeCopy code
[code]
    {"error":"Error: Failed to start Chrome CDP on port 18800 for profile \"openclaw\"."}
[/code]

### สาเหตุหลัก

บน Ubuntu (และ Linux distro จำนวนมาก) การติดตั้ง Chromium เริ่มต้นเป็น **แพ็กเกจ snap** การจำกัดของ AppArmor จาก snap รบกวนวิธีที่ OpenClaw สร้างและตรวจสอบกระบวนการเบราว์เซอร์

คำสั่ง `apt install chromium` ติดตั้งแพ็กเกจ stub ที่เปลี่ยนเส้นทางไปยัง snap:

CodeCopy code
[code]
    Note, selecting 'chromium-browser' instead of 'chromium'chromium-browser is already the newest version (2:1snap1-0ubuntu2).
[/code]

นี่ไม่ใช่เบราว์เซอร์จริง เป็นเพียง wrapper เท่านั้น

ความล้มเหลวในการเปิดใช้งานบน Linux ที่พบบ่อยอื่นๆ:

  * `The profile appears to be in use by another Chromium process` หมายความว่า Chrome พบไฟล์ล็อก `Singleton*` ที่ค้างอยู่ในไดเรกทอรีโปรไฟล์ที่จัดการอยู่ OpenClaw จะลบล็อกเหล่านั้นและลองอีกครั้งหนึ่งครั้งเมื่อล็อกชี้ไปยังกระบวนการที่ตายแล้วหรือ อยู่คนละโฮสต์
  * `Missing X server or $DISPLAY` หมายความว่ามีการขอเบราว์เซอร์แบบมองเห็นได้อย่างชัดเจน บนโฮสต์ที่ไม่มีเซสชันเดสก์ท็อป ตามค่าเริ่มต้น โปรไฟล์ที่จัดการในเครื่อง ตอนนี้จะถอยกลับไปใช้โหมด headless บน Linux เมื่อทั้ง `DISPLAY` และ `WAYLAND_DISPLAY` ไม่ได้ตั้งค่าไว้ หากคุณตั้ง `OPENCLAW_BROWSER_HEADLESS=0`, `browser.headless: false` หรือ `browser.profiles.<name>.headless: false`, ให้ลบการ override แบบมีหัวนั้นออก ตั้ง `OPENCLAW_BROWSER_HEADLESS=1`, เริ่ม `Xvfb`, รัน `openclaw browser start --headless` สำหรับการเปิดใช้งานที่จัดการแบบครั้งเดียว หรือรัน OpenClaw ในเซสชันเดสก์ท็อปจริง


### วิธีแก้ไข 1: ติดตั้ง Google Chrome (แนะนำ)

ติดตั้งแพ็กเกจ `.deb` อย่างเป็นทางการของ Google Chrome ซึ่งไม่ได้ถูก sandbox โดย snap:

bashCopy code
[code]
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.debsudo dpkg -i google-chrome-stable_current_amd64.debsudo apt --fix-broken install -y  # if there are dependency errors
[/code]

จากนั้นอัปเดตการกำหนดค่า OpenClaw ของคุณ (`~/.openclaw/openclaw.json`):

jsonCopy code
[code]
    {  "browser": {    "enabled": true,    "executablePath": "/usr/bin/google-chrome-stable",    "headless": true,    "noSandbox": true  }}
[/code]

### วิธีแก้ไข 2: ใช้ Snap Chromium ด้วยโหมดแนบเท่านั้น

หากคุณจำเป็นต้องใช้ snap Chromium ให้กำหนดค่า OpenClaw ให้แนบกับเบราว์เซอร์ที่เริ่มด้วยตนเอง:

  1. อัปเดตการกำหนดค่า:

jsonCopy code
[code]
    {  "browser": {    "enabled": true,    "attachOnly": true,    "headless": true,    "noSandbox": true  }}
[/code]

  2. เริ่ม Chromium ด้วยตนเอง:

bashCopy code
[code]
    chromium-browser --headless --no-sandbox --disable-gpu \  --remote-debugging-port=18800 \  --user-data-dir=$HOME/.openclaw/browser/openclaw/user-data \  about:blank &
[/code]

  3. สร้าง systemd user service เพื่อเริ่ม Chrome อัตโนมัติหากต้องการ:

iniCopy code
[code]
    # ~/.config/systemd/user/openclaw-browser.service[Unit]Description=OpenClaw Browser (Chrome CDP)After=network.target [Service]ExecStart=/snap/bin/chromium --headless --no-sandbox --disable-gpu --remote-debugging-port=18800 --user-data-dir=%h/.openclaw/browser/openclaw/user-data about:blankRestart=on-failureRestartSec=5 [Install]WantedBy=default.target
[/code]

เปิดใช้ด้วย: `systemctl --user enable --now openclaw-browser.service`

### การตรวจสอบว่าเบราว์เซอร์ทำงาน

ตรวจสอบสถานะ:

bashCopy code
[code]
    curl -s http://127.0.0.1:18791/ | jq '{running, pid, chosenBrowser}'
[/code]

ทดสอบการเรียกดู:

bashCopy code
[code]
    curl -s -X POST http://127.0.0.1:18791/startcurl -s http://127.0.0.1:18791/tabs
[/code]

### อ้างอิงการกำหนดค่า

ตัวเลือก | คำอธิบาย | ค่าเริ่มต้น  
---|---|---  
`browser.enabled` | เปิดใช้การควบคุมเบราว์เซอร์ | `true`  
`browser.executablePath` | เส้นทางไปยังไบนารีเบราว์เซอร์ที่ใช้ Chromium (Chrome/Brave/Edge/Chromium) | ตรวจพบอัตโนมัติ (เลือกเบราว์เซอร์เริ่มต้นก่อนเมื่อเป็นเบราว์เซอร์ที่ใช้ Chromium)  
`browser.headless` | รันโดยไม่มี GUI | `false`  
`OPENCLAW_BROWSER_HEADLESS` | การ override ต่อกระบวนการสำหรับโหมด headless ของเบราว์เซอร์ที่จัดการในเครื่อง | ไม่ได้ตั้งค่า  
`browser.noSandbox` | เพิ่ม flag `--no-sandbox` (จำเป็นสำหรับการตั้งค่า Linux บางแบบ) | `false`  
`browser.attachOnly` | ไม่เปิดเบราว์เซอร์ แนบกับตัวที่มีอยู่เท่านั้น | `false`  
`browser.cdpPort` | พอร์ต Chrome DevTools Protocol | `18800`  
`browser.localLaunchTimeoutMs` | ระยะหมดเวลาการค้นหา Chrome ที่จัดการในเครื่อง | `15000`  
`browser.localCdpReadyTimeoutMs` | ระยะหมดเวลาความพร้อมของ CDP หลังเปิดใช้งานที่จัดการในเครื่อง | `8000`  
  
บน Raspberry Pi, โฮสต์ VPS รุ่นเก่า หรือสตอเรจที่ช้า ให้เพิ่ม `browser.localLaunchTimeoutMs` เมื่อ Chrome ต้องใช้เวลามากขึ้นในการเปิดเผย endpoint HTTP ของ CDP เพิ่ม `browser.localCdpReadyTimeoutMs` เมื่อเปิดใช้งานสำเร็จแต่ `openclaw browser start` ยังรายงานว่า `not reachable after start` ค่าต้องเป็น จำนวนเต็มบวกสูงสุด `120000` มิลลิวินาที ค่าการกำหนดค่าที่ไม่ถูกต้องจะถูกปฏิเสธ

### ปัญหา: "No Chrome tabs found for profile="user""

คุณกำลังใช้โปรไฟล์ `existing-session` / Chrome MCP OpenClaw สามารถมองเห็น Chrome ในเครื่องได้ แต่ไม่มีแท็บที่เปิดอยู่ให้แนบได้

ตัวเลือกการแก้ไข:

  1. **ใช้เบราว์เซอร์ที่จัดการ:** `openclaw browser start --browser-profile openclaw` (หรือตั้ง `browser.defaultProfile: "openclaw"`)
  2. **ใช้ Chrome MCP:** ตรวจสอบให้แน่ใจว่า Chrome ในเครื่องกำลังรันอยู่พร้อมแท็บที่เปิดอย่างน้อยหนึ่งแท็บ จากนั้นลองใหม่ด้วย `--browser-profile user`


หมายเหตุ:

  * `user` ใช้ได้เฉพาะโฮสต์เท่านั้น สำหรับเซิร์ฟเวอร์ Linux, คอนเทนเนอร์ หรือโฮสต์ระยะไกล ให้ใช้โปรไฟล์ CDP
  * โปรไฟล์ `user` / `existing-session` อื่นๆ จะคงข้อจำกัดปัจจุบันของ Chrome MCP: การกระทำที่ขับเคลื่อนด้วย ref, hook อัปโหลดไฟล์เดียว, ไม่มีการ override ระยะหมดเวลาของ dialog, ไม่มี `wait --load networkidle` และไม่มี `responsebody`, การส่งออก PDF, การดักดาวน์โหลด หรือการกระทำแบบ batch
  * โปรไฟล์ `openclaw` ในเครื่องจะกำหนด `cdpPort`/`cdpUrl` อัตโนมัติ ตั้งค่าเหล่านี้เฉพาะสำหรับ CDP ระยะไกลเท่านั้น
  * โปรไฟล์ CDP ระยะไกลยอมรับ `http://`, `https://`, `ws://` และ `wss://` ใช้ HTTP(S) สำหรับการค้นหา `/json/version` หรือใช้ WS(S) เมื่อบริการเบราว์เซอร์ของคุณ ให้ URL ซ็อกเก็ต DevTools โดยตรง


## ที่เกี่ยวข้อง

  * [เบราว์เซอร์](</th/tools/browser>)
  * [การเข้าสู่ระบบเบราว์เซอร์](</th/tools/browser-login>)
  * [การแก้ไขปัญหา Browser WSL2](</th/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo