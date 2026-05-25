---
title: พร็อกซี API ของ Claude Max
source_url: https://docs.openclaw.ai/th/providers/claude-max-api-proxy
scraped_at: 2026-05-25
---

**claude-max-api-proxy** เป็นเครื่องมือจากชุมชนที่เปิดเผยการสมัครใช้งาน Claude Max/Pro ของคุณเป็นปลายทาง API ที่เข้ากันได้กับ OpenAI ซึ่งทำให้คุณสามารถใช้การสมัครใช้งานของคุณกับเครื่องมือใดก็ได้ที่รองรับรูปแบบ API ของ OpenAI

## ทำไมจึงควรใช้สิ่งนี้?

แนวทาง | ค่าใช้จ่าย | เหมาะที่สุดสำหรับ  
---|---|---  
Anthropic API | จ่ายตามโทเคน (~$15/M input, $75/M output สำหรับ Opus) | แอป production, ปริมาณการใช้งานสูง  
การสมัครใช้งาน Claude Max | ราคาเหมาจ่าย $200/เดือน | การใช้งานส่วนตัว, การพัฒนา, การใช้งานไม่จำกัด  
  
หากคุณมีการสมัครใช้งาน Claude Max และต้องการใช้กับเครื่องมือที่เข้ากันได้กับ OpenAI พร็อกซีนี้อาจช่วยลดต้นทุนสำหรับบางเวิร์กโฟลว์ได้ API key ยังคงเป็นเส้นทางด้านนโยบายที่ชัดเจนกว่าสำหรับการใช้งาน production

## วิธีการทำงาน

CodeCopy code
[code]
    แอปของคุณ → claude-max-api-proxy → Claude Code CLI → Anthropic (ผ่านการสมัครใช้งาน)     (รูปแบบ OpenAI)              (แปลงรูปแบบ)      (ใช้การเข้าสู่ระบบของคุณ)
[/code]

พร็อกซีนี้จะ:

  1. รับคำขอในรูปแบบ OpenAI ที่ `http://localhost:3456/v1/chat/completions`
  2. แปลงเป็นคำสั่งของ Claude Code CLI
  3. ส่งกลับคำตอบในรูปแบบ OpenAI (รองรับการสตรีม)


## เริ่มต้นใช้งาน

* ### ติดตั้งพร็อกซี

ต้องใช้ Node.js 20+ และ Claude Code CLI

bashCopy code
[code]
    npm install -g claude-max-api-proxy # Verify Claude CLI is authenticatedclaude --version
[/code]

* ### เริ่มต้นเซิร์ฟเวอร์

bashCopy code
[code]
    claude-max-api# Server runs at http://localhost:3456
[/code]

* ### ทดสอบพร็อกซี

bashCopy code
[code]
    # Health checkcurl http://localhost:3456/health # List modelscurl http://localhost:3456/v1/models # Chat completioncurl http://localhost:3456/v1/chat/completions \  -H "Content-Type: application/json" \  -d '{    "model": "claude-opus-4",    "messages": [{"role": "user", "content": "Hello!"}]  }'
[/code]

* ### กำหนดค่า OpenClaw

ชี้ OpenClaw ไปยังพร็อกซีในฐานะปลายทางแบบกำหนดเองที่เข้ากันได้กับ OpenAI:

json5Copy code
[code]
    {  env: {    OPENAI_API_KEY: "not-needed",    OPENAI_BASE_URL: "http://localhost:3456/v1",  },  agents: {    defaults: {      model: { primary: "openai/claude-opus-4" },    },  },}
[/code]

## แค็ตตาล็อกที่มีมาให้

Model ID | แมปไปยัง  
---|---  
`claude-opus-4` | Claude Opus 4  
`claude-sonnet-4` | Claude Sonnet 4  
`claude-haiku-4` | Claude Haiku 4  
  
## การกำหนดค่าขั้นสูง

หมายเหตุเกี่ยวกับเส้นทางแบบพร็อกซีที่เข้ากันได้กับ OpenAI

เส้นทางนี้ใช้แนวทางแบบพร็อกซีที่เข้ากันได้กับ OpenAI แบบเดียวกับแบ็กเอนด์ `/v1` แบบกำหนดเองอื่น ๆ:

  * จะไม่มีการปรับแต่งคำขอแบบ native ที่ใช้เฉพาะ OpenAI
  * ไม่มี `service_tier`, ไม่มี Responses `store`, ไม่มี hint ของ prompt-cache และไม่มี การปรับแต่ง payload ด้านความเข้ากันได้ของ reasoning แบบ OpenAI
  * จะไม่มีการฉีด header แสดงที่มาของ OpenClaw ที่ซ่อนไว้ (`originator`, `version`, `User-Agent`) ลงบน URL ของพร็อกซี

เริ่มอัตโนมัติบน macOS ด้วย LaunchAgent

สร้าง LaunchAgent เพื่อให้พร็อกซีทำงานโดยอัตโนมัติ:

bashCopy code
[code]
    cat > ~/Library/LaunchAgents/com.claude-max-api.plist << 'EOF'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>Label</key>  <string>com.claude-max-api</string>  <key>RunAtLoad</key>  <true/>  <key>KeepAlive</key>  <true/>  <key>ProgramArguments</key>  <array>    <string>/usr/local/bin/node</string>    <string>/usr/local/lib/node_modules/claude-max-api-proxy/dist/server/standalone.js</string>  </array>  <key>EnvironmentVariables</key>  <dict>    <key>PATH</key>    <string>/usr/local/bin:/opt/homebrew/bin:~/.local/bin:/usr/bin:/bin</string>  </dict></dict></plist>EOF launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.claude-max-api.plist
[/code]

## ลิงก์

  * **npm:** <https://www.npmjs.com/package/claude-max-api-proxy>
  * **GitHub:** <https://github.com/atalovesyou/claude-max-api-proxy>
  * **Issues:** <https://github.com/atalovesyou/claude-max-api-proxy/issues>


## หมายเหตุ

  * นี่คือ **เครื่องมือจากชุมชน** ไม่ได้รับการสนับสนุนอย่างเป็นทางการจาก Anthropic หรือ OpenClaw
  * ต้องมีการสมัครใช้งาน Claude Max/Pro ที่ยังใช้งานอยู่ และ Claude Code CLI ต้องยืนยันตัวตนแล้ว
  * พร็อกซีทำงานภายในเครื่องและไม่ส่งข้อมูลไปยังเซิร์ฟเวอร์ของบุคคลที่สาม
  * รองรับการตอบกลับแบบสตรีมอย่างสมบูรณ์


## ที่เกี่ยวข้อง

[**Anthropic provider** การผสานรวม OpenClaw แบบเนทีฟกับ Claude CLI หรือ API key ](</th/providers/anthropic>) [**OpenAI provider** สำหรับการสมัครใช้งาน OpenAI/Codex ](</th/providers/openai>) [**Model selection** ภาพรวมของผู้ให้บริการทั้งหมด, model ref และพฤติกรรม failover ](</th/concepts/model-providers>) [**Configuration** ข้อมูลอ้างอิงคอนฟิกแบบเต็ม ](</th/gateway/configuration>)

Was this useful?YesNo