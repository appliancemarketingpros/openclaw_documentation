---
title: คุณสมบัติ
source_url: https://docs.openclaw.ai/th/concepts/features
scraped_at: 2026-05-25
---

## ไฮไลต์

[**ช่องทาง** Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat และอื่นๆ ด้วย Gateway เดียว ](</th/channels>) [**Plugins** Plugins ที่รวมมาให้เพิ่ม Matrix, Nextcloud Talk, Nostr, Twitch, Zalo และอื่นๆ โดยไม่ต้องติดตั้งแยกในรุ่นปัจจุบันปกติ ](</th/tools/plugin>) [**การกำหนดเส้นทาง** การกำหนดเส้นทางแบบหลายเอเจนต์พร้อมเซสชันที่แยกจากกัน ](</th/concepts/multi-agent>) [**สื่อ** รูปภาพ เสียง วิดีโอ เอกสาร และการสร้างรูปภาพ/วิดีโอ ](</th/nodes/images>) [**แอปและ UI** UI ควบคุมบนเว็บและแอปคู่หูสำหรับ macOS ](</th/web/control-ui>) [**โหนดมือถือ** โหนด iOS และ Android พร้อมการจับคู่ เสียง/แชต และคำสั่งอุปกรณ์แบบสมบูรณ์ ](</th/nodes>)

## รายการทั้งหมด

**ช่องทาง:**

  * ช่องทางในตัวประกอบด้วย Discord, Google Chat, iMessage, IRC, Signal, Slack, Telegram, WebChat และ WhatsApp
  * ช่องทาง Plugin ที่รวมมาให้ประกอบด้วย Feishu, LINE, Matrix, Mattermost, Microsoft Teams, Nextcloud Talk, Nostr, QQ Bot, Synology Chat, Tlon, Twitch, Zalo และ Zalo Personal
  * Plugins ช่องทางที่ติดตั้งแยกแบบเลือกได้ประกอบด้วย Voice Call และแพ็กเกจจากบุคคลที่สาม เช่น WeChat
  * Plugins ช่องทางจากบุคคลที่สามสามารถขยาย Gateway เพิ่มเติมได้ เช่น WeChat
  * รองรับแชตกลุ่มด้วยการเปิดใช้งานตามการกล่าวถึง
  * ความปลอดภัยของ DM ด้วย allowlists และการจับคู่


**เอเจนต์:**

  * รันไทม์เอเจนต์แบบฝังพร้อมการสตรีมเครื่องมือ
  * การกำหนดเส้นทางแบบหลายเอเจนต์พร้อมเซสชันที่แยกตามเวิร์กสเปซหรือผู้ส่ง
  * เซสชัน: แชตโดยตรงจะรวมเข้าเป็น `main` ที่ใช้ร่วมกัน; กลุ่มจะแยกจากกัน
  * การสตรีมและการแบ่งชิ้นสำหรับคำตอบยาว


**การยืนยันตัวตนและผู้ให้บริการ:**

  * ผู้ให้บริการโมเดลมากกว่า 35 ราย (Anthropic, OpenAI, Google และอื่นๆ)
  * การยืนยันตัวตนแบบสมัครสมาชิกผ่าน OAuth (เช่น OpenAI Codex)
  * รองรับผู้ให้บริการแบบกำหนดเองและโฮสต์เอง (vLLM, SGLang, Ollama และปลายทางใดๆ ที่เข้ากันได้กับ OpenAI หรือเข้ากันได้กับ Anthropic)


**สื่อ:**

  * รูปภาพ เสียง วิดีโอ และเอกสารทั้งขาเข้าและขาออก
  * พื้นผิวความสามารถร่วมสำหรับการสร้างรูปภาพและการสร้างวิดีโอ
  * การถอดเสียงโน้ตเสียง
  * แปลงข้อความเป็นเสียงด้วยผู้ให้บริการหลายราย


**แอปและอินเทอร์เฟซ:**

  * WebChat และ UI ควบคุมบนเบราว์เซอร์
  * แอปคู่หูบนแถบเมนู macOS
  * โหนด iOS พร้อมการจับคู่ Canvas กล้อง การบันทึกหน้าจอ ตำแหน่งที่ตั้ง และเสียง
  * โหนด Android พร้อมการจับคู่ แชต เสียง Canvas กล้อง และคำสั่งอุปกรณ์


**เครื่องมือและระบบอัตโนมัติ:**

  * ระบบอัตโนมัติของเบราว์เซอร์, exec, sandboxing
  * การค้นหาเว็บ (Brave, DuckDuckGo, Exa, Firecrawl, Gemini, Grok, Kimi, MiniMax Search, Ollama Web Search, Perplexity, SearXNG, Tavily)
  * งาน Cron และการกำหนดเวลา Heartbeat
  * Skills, plugins และไปป์ไลน์เวิร์กโฟลว์ (Lobster)


## ที่เกี่ยวข้อง

[**ฟีเจอร์ทดลอง** ฟีเจอร์แบบเลือกใช้ที่ยังไม่ได้เผยแพร่สู่พื้นผิวเริ่มต้น ](</th/concepts/experimental-features>) [**รันไทม์เอเจนต์** โมเดลรันไทม์เอเจนต์และวิธีการส่งรันไปดำเนินการ ](</th/concepts/agent>) [**ช่องทาง** เชื่อมต่อ Telegram, WhatsApp, Discord, Slack และอื่นๆ จาก Gateway เดียว ](</th/channels>) [**Plugins** Plugins ที่รวมมาให้และจากบุคคลที่สามซึ่งขยาย OpenClaw ](</th/tools/plugin>)

Was this useful?YesNo