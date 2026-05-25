---
title: OpenClaw
source_url: https://docs.openclaw.ai/th
scraped_at: 2026-05-25
---

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _"ลอกคราบ! ลอกคราบ!"_ — ลอบสเตอร์อวกาศตัวหนึ่ง อาจจะ

**Gateway บนระบบปฏิบัติการใดก็ได้สำหรับ AI agents บน Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo และอื่นๆ**

ส่งข้อความ แล้วรับคำตอบจาก agent ได้จากในกระเป๋าของคุณ รัน Gateway หนึ่งตัวบนแชนเนลในตัว, channel plugins ที่รวมมาให้, WebChat และโหนดมือถือ

[**เริ่มต้นใช้งาน** ติดตั้ง OpenClaw และเปิดใช้งาน Gateway ได้ในไม่กี่นาที ](</th/start/getting-started>) [**รันการเริ่มต้นใช้งาน** การตั้งค่าแบบมีคำแนะนำด้วย `openclaw onboard` และขั้นตอนการจับคู่ ](</th/start/wizard>) [**เปิด Control UI** เปิดแดชบอร์ดในเบราว์เซอร์สำหรับแชต การกำหนดค่า และเซสชัน ](</th/web/control-ui>)

## OpenClaw คืออะไร?

OpenClaw คือ **gateway แบบโฮสต์เอง** ที่เชื่อมต่อแอปแชตและพื้นผิวแชนเนลที่คุณชื่นชอบ — แชนเนลในตัว รวมถึง channel plugins ที่รวมมาให้หรือจากภายนอก เช่น Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo และอื่นๆ — เข้ากับ AI coding agents อย่าง Pi คุณรันกระบวนการ Gateway เพียงตัวเดียวบนเครื่องของคุณเอง (หรือบนเซิร์ฟเวอร์) แล้วมันจะกลายเป็นสะพานเชื่อมระหว่างแอปส่งข้อความของคุณกับผู้ช่วย AI ที่พร้อมใช้งานเสมอ

**เหมาะกับใคร?** นักพัฒนาและผู้ใช้ขั้นสูงที่ต้องการผู้ช่วย AI ส่วนตัวซึ่งส่งข้อความถึงได้จากทุกที่ โดยไม่ต้องสละการควบคุมข้อมูลของตนหรือพึ่งพาบริการแบบโฮสต์

**อะไรที่ทำให้แตกต่าง?**

  * **โฮสต์เอง** : รันบนฮาร์ดแวร์ของคุณ ตามกฎของคุณ
  * **หลายแชนเนล** : Gateway หนึ่งตัวให้บริการแชนเนลในตัว รวมถึง channel plugins ที่รวมมาให้หรือจากภายนอกได้พร้อมกัน
  * **ออกแบบมาสำหรับ agent** : สร้างมาสำหรับ coding agents ที่มีการใช้เครื่องมือ เซสชัน หน่วยความจำ และการกำหนดเส้นทางหลาย agent
  * **โอเพนซอร์ส** : ใช้สัญญาอนุญาต MIT และขับเคลื่อนโดยชุมชน


**คุณต้องมีอะไรบ้าง?** Node 24 (แนะนำ) หรือ Node 22 LTS (`22.16+`) เพื่อความเข้ากันได้, API key จากผู้ให้บริการที่คุณเลือก และเวลา 5 นาที เพื่อคุณภาพและความปลอดภัยที่ดีที่สุด ให้ใช้โมเดลรุ่นล่าสุดที่แข็งแกร่งที่สุดที่มี

## วิธีการทำงาน
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["Pi agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

Gateway คือแหล่งข้อมูลจริงเพียงหนึ่งเดียวสำหรับเซสชัน การกำหนดเส้นทาง และการเชื่อมต่อแชนเนล

## ความสามารถหลัก

[**Gateway หลายแชนเนล** Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat และอื่นๆ ด้วยกระบวนการ Gateway เพียงตัวเดียว ](</th/channels>) [**แชนเนล Plugin** Plugins ที่รวมมาให้เพิ่ม Matrix, Nostr, Twitch, Zalo และอื่นๆ ในรุ่นปัจจุบันปกติ ](</th/tools/plugin>) [**การกำหนดเส้นทางหลาย agent** เซสชันที่แยกกันตาม agent, พื้นที่ทำงาน หรือผู้ส่ง ](</th/concepts/multi-agent>) [**การรองรับสื่อ** ส่งและรับรูปภาพ เสียง และเอกสาร ](</th/nodes/images>) [**Web Control UI** แดชบอร์ดในเบราว์เซอร์สำหรับแชต การกำหนดค่า เซสชัน และโหนด ](</th/web/control-ui>) [**โหนดมือถือ** จับคู่โหนด iOS และ Android สำหรับเวิร์กโฟลว์ที่รองรับ Canvas, กล้อง และเสียง ](</th/nodes>)

## เริ่มต้นอย่างรวดเร็ว

* ### ติดตั้ง OpenClaw

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### เริ่มต้นใช้งานและติดตั้งบริการ

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### แชต

เปิด Control UI ในเบราว์เซอร์ของคุณและส่งข้อความ:

bashCopy code
[code]
    openclaw dashboard
[/code]

หรือเชื่อมต่อแชนเนล ([Telegram](</th/channels/telegram>) เร็วที่สุด) แล้วแชตจากโทรศัพท์ของคุณ

ต้องการการติดตั้งและการตั้งค่าสำหรับพัฒนาแบบครบถ้วนใช่ไหม? ดู [เริ่มต้นใช้งาน](</th/start/getting-started>)

## แดชบอร์ด

เปิด Control UI ในเบราว์เซอร์หลังจาก Gateway เริ่มทำงาน

  * ค่าเริ่มต้นในเครื่อง: <http://127.0.0.1:18789/>
  * การเข้าถึงจากระยะไกล: [พื้นผิวเว็บ](</th/web>) และ [Tailscale](</th/gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## การกำหนดค่า (ไม่บังคับ)

การกำหนดค่าอยู่ที่ `~/.openclaw/openclaw.json`

  * หากคุณ **ไม่ทำอะไรเลย** OpenClaw จะใช้ไบนารี Pi ที่รวมมาให้ในโหมด RPC พร้อมเซสชันแยกตามผู้ส่ง
  * หากคุณต้องการจำกัดการใช้งาน ให้เริ่มจาก `channels.whatsapp.allowFrom` และกฎการกล่าวถึง (สำหรับกลุ่ม)


ตัวอย่าง:

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## เริ่มที่นี่

[**ศูนย์รวมเอกสาร** เอกสารและคู่มือทั้งหมด จัดตามกรณีการใช้งาน ](</th/start/hubs>) [**การกำหนดค่า** การตั้งค่า Gateway หลัก โทเค็น และการกำหนดค่าผู้ให้บริการ ](</th/gateway/configuration>) [**การเข้าถึงจากระยะไกล** รูปแบบการเข้าถึงผ่าน SSH และ tailnet ](</th/gateway/remote>) [**แชนเนล** การตั้งค่าเฉพาะแชนเนลสำหรับ Feishu, Microsoft Teams, WhatsApp, Telegram, Discord และอื่นๆ ](</th/channels/telegram>) [**โหนด** โหนด iOS และ Android พร้อมการจับคู่, Canvas, กล้อง และการทำงานของอุปกรณ์ ](</th/nodes>) [**ความช่วยเหลือ** จุดเริ่มต้นสำหรับการแก้ไขปัญหาทั่วไปและการแก้ไขข้อขัดข้อง ](</th/help>)

## เรียนรู้เพิ่มเติม

[**รายการฟีเจอร์ทั้งหมด** ความสามารถของแชนเนล การกำหนดเส้นทาง และสื่ออย่างครบถ้วน ](</th/concepts/features>) [**การกำหนดเส้นทางหลาย agent** การแยกพื้นที่ทำงานและเซสชันตาม agent ](</th/concepts/multi-agent>) [**ความปลอดภัย** โทเค็น รายการอนุญาต และการควบคุมความปลอดภัย ](</th/gateway/security>) [**การแก้ไขปัญหา** การวินิจฉัย Gateway และข้อผิดพลาดทั่วไป ](</th/gateway/troubleshooting>) [**เกี่ยวกับและเครดิต** จุดกำเนิดโครงการ ผู้มีส่วนร่วม และสัญญาอนุญาต ](</th/reference/credits>)

Was this useful?YesNo