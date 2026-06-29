---
title: อนุกรมวิธานวุฒิภาวะ
source_url: https://docs.openclaw.ai/th/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# อนุกรมวิธานระดับความพร้อม

โมเดลเบื้องหลังสกอร์การ์ด

พื้นผิว > หมวดหมู่ > ความสามารถ > หลักฐาน

พื้นผิว 50 รายการจัดกลุ่มเป็น 4 ตระกูล โดยทุกหมวดหมู่เชื่อมโยงกลับไปยังเอกสารมาตรฐานและรหัสความครอบคลุม QA

เรียกดูพื้นที่ผลิตภัณฑ์ / เปิดอนุกรมวิธานแบบละเอียด / [ดูคะแนน](</th/maturity/scorecard>)

## วิธีอ่านหน้านี้

พื้นผิวคือพื้นที่ผลิตภัณฑ์ เช่น รันไทม์ Gateway, Discord หรือแอป macOS แต่ละพื้นผิวมีหมวดหมู่ และแต่ละหมวดหมู่มีการตรวจสอบระดับความสามารถที่สถานการณ์ QA ครอบคลุม ใช้สกอร์การ์ดเพื่อประเมินระดับรีลีส ใช้หน้านี้เพื่อตรวจดูโมเดลที่อยู่เบื้องหลัง

## ระดับความพร้อม

M0วางแผนแล้วทราบทิศทางแล้ว แต่ยังไม่มีเส้นทางผู้ใช้ที่รองรับการเลื่อนระดับ: มีประเด็นด้านการออกแบบ เจ้าของ และพื้นผิวเป้าหมายแล้ว

M1ทดลองนำไปใช้แล้วภายใต้ข้อควรระวัง แฟล็ก บิลด์จากซอร์ส หรือโฟลว์สำหรับผู้ดูแลเท่านั้นการเลื่อนระดับ: ผู้ดูแลสามารถเรียกใช้สถานการณ์จาก main ปัจจุบันได้

M2อัลฟาผู้ใช้จริงสามารถทดลองได้ แต่คาดว่าจะมีการเปลี่ยนแปลงที่ทำให้เข้ากันไม่ได้และ UX ที่ยังไม่สมบูรณ์การเลื่อนระดับ: มีเอกสารการตั้งค่า การทดสอบพื้นฐาน ข้อควรระวังที่ทราบ และหลักฐานจากสภาพแวดล้อมจริงอย่างน้อยหนึ่งรายการ

M3เบต้ามีเส้นทางสาธารณะ และเวิร์กโฟลว์หลักใช้งานได้พร้อมข้อควรระวังที่จำกัดขอบเขตการเลื่อนระดับ: เอกสารการติดตั้ง/อัปเดต การทดสอบการถดถอย รันบุ๊กสนับสนุน และหลักฐานสถานการณ์ที่สำเร็จในสภาพแวดล้อมที่คาดไว้

M4เสถียรเส้นทางที่แนะนำสำหรับผู้ใช้ทั่วไป ความล้มเหลวจะถือเป็นการถดถอยการเลื่อนระดับ: เกตรีลีส เส้นทาง doctor/การแก้ไขปัญหา เอกสารครอบคลุม และหลักฐานจากการใช้งานจริงซ้ำหลายครั้ง

M5ยอดเยี่ยมแบบ Clawขัดเกลา น่าใช้ มีเครื่องมือสังเกตการณ์ครบถ้วน และแข่งขันได้กับเวิร์กโฟลว์เทียบเคียงที่ดีที่สุดการเลื่อนระดับ: ระดับเสถียรพร้อมผ่านสกอร์การ์ดผู้ใช้ในกลุ่มผู้ใช้ตัวแทน

## พื้นที่ผลิตภัณฑ์

### แกนหลัก

CLI M4เสถียร7 พื้นที่ - เสร็จสมบูรณ์ 90% รันไทม์ Gateway M4เสถียร13 พื้นที่ - เสร็จสมบูรณ์ 89% รันไทม์เอเจนต์ M3เบต้า9 พื้นที่ - เสร็จสมบูรณ์ 79% เซสชัน หน่วยความจำ และเอนจินบริบท M3เบต้า9 พื้นที่ - เสร็จสมบูรณ์ 79% เฟรมเวิร์กช่องทาง M3เบต้า8 พื้นที่ - เสร็จสมบูรณ์ 79% การสังเกตการณ์ระบบ M3เบต้า5 พื้นที่ - เสร็จสมบูรณ์ 79% เว็บแอป Gateway M3เบต้า6 พื้นที่ - เสร็จสมบูรณ์ 79% Plugin M3เบต้า9 ด้าน - เสร็จสมบูรณ์ 79% ความปลอดภัย, การยืนยันตัวตน, การจับคู่ และความลับ M3เบต้า6 ด้าน - เสร็จสมบูรณ์ 79% ระบบอัตโนมัติ: Cron, hooks, tasks, polling M3เบต้า6 ด้าน - เสร็จสมบูรณ์ 79% การทำความเข้าใจสื่อและการสร้างสื่อ M2อัลฟ่า6 ด้าน - เสร็จสมบูรณ์ 68% เสียงและการสนทนาแบบเรียลไทม์ M2อัลฟ่า6 ด้าน - เสร็จสมบูรณ์ 68% TUI M2อัลฟ่า5 ด้าน - เสร็จสมบูรณ์ 66% ClawHub M2อัลฟ่า4 ด้าน - เสร็จสมบูรณ์ 62% OpenClaw App SDK M2อัลฟ่า6 ด้าน - เสร็จสมบูรณ์ 53%

### แพลตฟอร์ม

โฮสต์ Linux Gateway M4เสถียร5 ด้าน - เสร็จสมบูรณ์ 89% โฮสต์ macOS Gateway M4เสถียร7 ด้าน - เสร็จสมบูรณ์ 88% การโฮสต์ด้วย Docker และ Podman M3เบต้า4 ด้าน - เสร็จสมบูรณ์ 79% Windows ผ่าน WSL2 M3เบต้า6 ด้าน - เสร็จสมบูรณ์ 79% Raspberry Pi และอุปกรณ์ Linux ขนาดเล็ก M3เบต้า4 ด้าน - เสร็จสมบูรณ์ 79% แอปคู่หู macOS M3เบต้า8 ด้าน - เสร็จสมบูรณ์ 78% แอป Android M2อัลฟ่า7 ด้าน - เสร็จสมบูรณ์ 66% Windows แบบเนทีฟ M2อัลฟา4 ด้าน - เสร็จสมบูรณ์ 66% การโฮสต์ Kubernetes M2อัลฟา4 ด้าน - เสร็จสมบูรณ์ 61% แอป iOS M1ทดลอง8 ด้าน - เสร็จสมบูรณ์ 44% เส้นทางการติดตั้ง Nix M1ทดลอง5 ด้าน - เสร็จสมบูรณ์ 44% พื้นผิวแอปคู่หู watchOS M1ทดลอง5 ด้าน - เสร็จสมบูรณ์ 44% แอปคู่หู Linux M0วางแผนแล้ว5 ด้าน - เสร็จสมบูรณ์ 21% แอปคู่หู Windows แบบเนทีฟ M0วางแผนแล้ว5 ด้าน - เสร็จสมบูรณ์ 21%

### ช่องทาง

Discord M4เสถียร6 ด้าน - เสร็จสมบูรณ์ 87% Telegram M3เบต้า5 ด้าน - เสร็จสมบูรณ์ 78% Slack M3เบต้า5 ด้าน - เสร็จสมบูรณ์ 78% iMessage และ BlueBubbles M3เบต้า5 ด้าน - เสร็จสมบูรณ์ 78% WhatsApp M3เบต้า5 ด้าน - เสร็จสมบูรณ์ 78% Matrix M2อัลฟา6 ด้าน - เสร็จสมบูรณ์ 67% Google Chat M2อัลฟา5 ด้าน - เสร็จสมบูรณ์ 66% Microsoft Teams M2อัลฟา5 ด้าน - เสร็จสมบูรณ์ 66% Signal M2อัลฟา5 ด้าน - เสร็จสมบูรณ์ 66% Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, ช่องทางระดับภูมิภาค M2อัลฟา4 ด้าน - เสร็จสมบูรณ์ 58% Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat M2อัลฟา4 ด้าน - เสร็จสมบูรณ์ 54% ช่องทางการโทรด้วยเสียง M1ทดลอง5 ด้าน - เสร็จสมบูรณ์ 44%

### Provider และเครื่องมือ

ระบบอัตโนมัติของเบราว์เซอร์, exec และเครื่องมือแซนด์บ็อกซ์ M3เบต้า3 ด้าน - เสร็จสมบูรณ์ 79% เส้นทาง Provider ของ OpenAI และ Codex M3เบต้า5 ด้าน - เสร็จสมบูรณ์ 79% เครื่องมือค้นหาเว็บ M3เบต้า4 ด้าน - เสร็จสมบูรณ์ 79% เส้นทาง Provider ของ Anthropic M3เบต้า5 ด้าน - เสร็จสมบูรณ์ 78% เส้นทาง Provider ของ Google M3เบต้า5 ด้าน - เสร็จสมบูรณ์ 78% เส้นทาง Provider ของ OpenRouter M3เบต้า4 ด้าน - เสร็จสมบูรณ์ 78% เครื่องมือสร้างภาพ วิดีโอ และเพลง M2อัลฟา5 ด้าน - เสร็จสมบูรณ์ 68% Provider โมเดลภายในเครื่อง: Ollama, vLLM, SGLang, LM Studio M2อัลฟา5 ด้าน - เสร็จสมบูรณ์ 68% Provider แบบโฮสต์กลุ่ม long-tail M2อัลฟา3 ด้าน - เสร็จสมบูรณ์ 68%

## รายละเอียด

### แกนหลัก

CLI - M4 เสถียร - 7 ด้าน

เส้นทางการตั้งค่าและการซ่อมแซมปกติได้รับการจัดทำเอกสารไว้ในเอกสารการติดตั้ง, CLI และ Gateway ส่วนเส้นทาง Windows เฉพาะแพลตฟอร์มถูกติดตามในแถว Windows ผ่าน WSL2 และ Windows แบบเนทีฟ

ความครอบคลุม ทดลอง - 4%คุณภาพ เสถียร - 83%ความสมบูรณ์ เสถียร - 90%บางส่วน - 6

การตั้งค่า CLI 6 ความสามารถ / รองรับ LTS

ทดลอง17%

เสถียร89%

เสถียร90%

[ดัชนี](</th/install>), [ตัวติดตั้ง](</th/install/installer>), [Node](</th/install/node>), [การอัปเดต](</th/install/updating>)

การเริ่มต้นใช้งานและการตั้งค่าการยืนยันตัวตน 5 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า75%

เสถียร89%

[เริ่มต้นใช้งาน](</th/cli/onboard>), [กำหนดค่า](</th/cli/configure>), [ภาพรวมการเริ่มต้นใช้งาน](</th/start/onboarding-overview>)

การตั้งค่า Plugin และช่องทาง 5 ความสามารถ

ทดลอง0%

เบต้า75%

เสถียร89%

[เริ่มต้นใช้งาน](</th/cli/onboard>), [Plugins](</th/cli/plugins>), [ช่องทาง](</th/cli/channels>)

การจัดการบริการ Gateway 5 ความสามารถ / รองรับ LTS

ทดลอง14%

เสถียร87%

เสถียร90%

[Gateway](</th/cli/gateway>), [การอัปเดต](</th/install/updating>), [การแก้ไขปัญหา](</th/gateway/troubleshooting>)

การสังเกตการณ์ของ CLI 5 ความสามารถ / รองรับ LTS

ทดลอง0%

เสถียร89%

เสถียร90%

[สถานะ](</th/cli/status>), [สุขภาพ](</th/cli/health>), [บันทึก](</th/cli/logs>), [การวินิจฉัย](</th/gateway/diagnostics>)

Doctor 10 ความสามารถ / รองรับ LTS

ทดลอง0%

เสถียร89%

เสถียร90%

[Doctor](</th/cli/doctor>), [Doctor](</th/gateway/doctor>), [ความลับ](</th/gateway/secrets>), [การแก้ไขปัญหา](</th/gateway/troubleshooting>)

การอัปเดตและการอัปเกรด 5 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า75%

เสถียร89%

[การอัปเดต](</th/install/updating>), [อัปเดต](</th/cli/update>), [การแก้ไขปัญหา](</th/gateway/troubleshooting>)

รันไทม์ Gateway - M4 เสถียร - 13 พื้นที่

สถาปัตยกรรมหลัก การยืนยันตัวตน การจับคู่ เอกสารโปรโตคอล เอกสารเดมอน และคู่มือปฏิบัติการ CLI มีความครอบคลุมกว้างและเป็นปัจจุบัน

ความครอบคลุม ทดลอง - 6%คุณภาพ เสถียร - 81%ความสมบูรณ์ เสถียร - 89%บางส่วน - 12

การอนุมัติและการดำเนินการระยะไกล 6 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า75%

เสถียร89%

[โปรโตคอล](</th/gateway/protocol>), [ดัชนี](</th/gateway/security>)

HTTP API 4 ความสามารถ / รองรับ LTS

ทดลอง25%

เสถียร90%

เสถียร90%

[ดัชนี](</th/gateway>), [Openai HTTP API](</th/gateway/openai-http-api>), [Openresponses HTTP API](</th/gateway/openresponses-http-api>), [Tools Invoke HTTP API](</th/gateway/tools-invoke-http-api>), [ฮุก](</th/automation/hooks>), [ดัชนี](</th/web>)

พื้นผิวเว็บที่โฮสต์อยู่ 4 ความสามารถ / รองรับ LTS

ทดลอง0%

เสถียร89%

เสถียร90%

[ดัชนี](</th/gateway>), [สถาปัตยกรรม](</th/concepts/architecture>), [UI ควบคุม](</th/web/control-ui>), [เว็บแชต](</th/web/webchat>), [Canvas](</th/refactor/canvas>)

Gateway RPC API และเหตุการณ์ 20 ความสามารถ / รองรับ LTS

ทดลอง9%

เสถียร90%

เสถียร90%

[โปรโตคอล](</th/gateway/protocol>), [ดัชนี](</th/gateway>), [สถาปัตยกรรม](</th/concepts/architecture>)

การยืนยันตัวตนอุปกรณ์และการจับคู่ 10 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า75%

เสถียร89%

[โปรโตคอล](</th/gateway/protocol>), [การจับคู่](</th/gateway/pairing>), [ดัชนี](</th/gateway/security>)

การเข้าถึงเครือข่ายและการค้นพบ 6 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า75%

เสถียร89%

[ดัชนี](</th/gateway>), [การค้นพบ](</th/gateway/discovery>), [โปรโตคอล](</th/gateway/protocol>)

Node และความสามารถระยะไกล 8 ความสามารถ

ทดลอง0%

เบต้า75%

เสถียร89%

[โปรโตคอล](</th/gateway/protocol>), [สถาปัตยกรรม](</th/concepts/architecture>), [ดัชนี](</th/nodes>)

สุขภาพ การวินิจฉัย และการซ่อมแซม 7 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า75%

เสถียร89%

[ดัชนี](</th/gateway>), [การวินิจฉัย](</th/gateway/diagnostics>), [Doctor](</th/gateway/doctor>)

ความเข้ากันได้ของโปรโตคอล 7 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า75%

เสถียร89%

[โปรโตคอล](</th/gateway/protocol>), [สถาปัตยกรรม](</th/concepts/architecture>), [Typebox](</th/concepts/typebox>), [โปรโตคอล Bridge](</th/gateway/bridge-protocol>)

บทบาทและสิทธิ์ 5 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า75%

เสถียร89%

[โปรโตคอล](</th/gateway/protocol>), [ดัชนี](</th/gateway/security>)

วงจรชีวิต Gateway 7 ความสามารถ / รองรับ LTS

ทดลอง33%

เสถียร90%

เสถียร90%

[ดัชนี](</th/gateway>), [สถาปัตยกรรม](</th/concepts/architecture>)

การควบคุมความปลอดภัย 6 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า75%

เสถียร89%

[ดัชนี](</th/gateway/security>), [โปรโตคอล](</th/gateway/protocol>), [การค้นพบ](</th/gateway/discovery>)

การเชื่อมต่อ WebSocket 8 ความสามารถ / รองรับ LTS

ทดลอง13%

เสถียร90%

เสถียร90%

[โปรโตคอล](</th/gateway/protocol>), [สถาปัตยกรรม](</th/concepts/architecture>)

Agent Runtime - M3 Beta - 9 areas

ลูปหลัก โมเดล การกำหนดเส้นทางผู้ให้บริการ และการสตรีมเครื่องมือเป็นองค์ประกอบระดับหลัก แต่พฤติกรรมของผู้ให้บริการเปลี่ยนทุกสัปดาห์และต้องมีหลักฐานจากสถานการณ์ทดสอบสำหรับแต่ละรีลีส

ความครอบคลุม ขั้นทดลอง - 33%คุณภาพ เบต้า - 78%ความสมบูรณ์ เบต้า - 79%บางส่วน - 6

การดำเนินการเทิร์นของเอเจนต์ 3 ความสามารถ / รองรับ LTS

ทดลอง29%

เบต้า79%

เบต้า79%

[ลูปเอเจนต์](</th/concepts/agent-loop>), [เอเจนต์](</th/cli/agent>), [รันไทม์เอเจนต์](</th/concepts/agent-runtimes>)

รันไทม์ภายนอกและเอเจนต์ย่อย 4 ความสามารถ

ทดลอง30%

เบต้า79%

เบต้า79%

[รันไทม์เอเจนต์](</th/concepts/agent-runtimes>), [Anthropic](</th/providers/anthropic>), [Google](</th/providers/google>), [เอเจนต์ย่อย](</th/tools/subagents>)

การดำเนินการของผู้ให้บริการแบบโฮสต์ 5 ความสามารถ / รองรับ LTS

ทดลอง20%

เบต้า79%

เบต้า79%

[Openai](</th/providers/openai>), [Anthropic](</th/providers/anthropic>), [Google](</th/providers/google>), [โมเดล](</th/concepts/models>)

ผู้ให้บริการแบบโลคัลและโฮสต์เอง 5 ความสามารถ

ทดลอง0%

อัลฟ่า68%

เบต้า79%

[Ollama](</th/providers/ollama>), [โมเดล](</th/concepts/models>), [เอเจนต์](</th/cli/agent>)

การเลือกโมเดลและรันไทม์ 4 ความสามารถ / รองรับ LTS

ทดลอง25%

เบต้า79%

เบต้า79%

[โมเดล](</th/concepts/models>), [โมเดล](</th/cli/models>), [Openai](</th/providers/openai>), [รันไทม์เอเจนต์](</th/concepts/agent-runtimes>)

การยืนยันตัวตนของผู้ให้บริการ 10 ความสามารถ / รองรับ LTS

ทดลอง24%

เบต้า79%

เบต้า79%

[โมเดล](</th/concepts/models>), [เอเจนต์](</th/cli/agent>), [โมเดล](</th/cli/models>), [Openai](</th/providers/openai>), [Anthropic](</th/providers/anthropic>), [Google](</th/providers/google>), [เอเจนต์ย่อย](</th/tools/subagents>)

สตรีมมิงและความคืบหน้า 2 ความสามารถ

อัลฟ่า56%

เบต้า79%

เบต้า79%

[สตรีมมิง](</th/concepts/streaming>), [ลูปเอเจนต์](</th/concepts/agent-loop>)

การเรียกใช้เครื่องมือและการจัดการการตอบกลับ 3 ความสามารถ / รองรับ LTS

อัลฟ่า65%

เบต้า79%

เบต้า79%

[ลูปเอเจนต์](</th/concepts/agent-loop>), [Ollama](</th/providers/ollama>)

การควบคุมการเรียกใช้เครื่องมือ 6 ความสามารถ / รองรับ LTS

อัลฟา50%

เบตา79%

เบตา79%

[แซนด์บ็อกซ์เทียบกับนโยบายเครื่องมือเทียบกับสิทธิ์ยกระดับ](</th/gateway/sandbox-vs-tool-policy-vs-elevated>), [ลูปของเอเจนต์](</th/concepts/agent-loop>), [เอเจนต์ย่อย](</th/tools/subagents>)

เซสชัน หน่วยความจำ และเอนจินบริบท - M3 Beta - 9 ด้าน

เอกสารแข็งแรงและมีการพัฒนาใช้งานจริงอย่างต่อเนื่อง ระดับความพร้อมขึ้นอยู่กับความทนทานของทรานสคริปต์ คุณภาพของ Compaction และความเท่าเทียมกันข้ามไคลเอนต์

ความครอบคลุม ระยะทดลอง - 30%คุณภาพ Beta - 77%ความสมบูรณ์ Beta - 79%บางส่วน - 6

การจัดการเซสชัน CLI และทรานสคริปต์ 2 ความสามารถ / รองรับ LTS

เชิงทดลอง0%

อัลฟ่า68%

เบต้า79%

[เซสชัน](</th/concepts/session>), [Compaction การจัดการเซสชัน](</th/reference/session-management-compaction>), [เซสชัน](</th/cli/sessions>)

การจัดการโทเค็น 3 ความสามารถ / รองรับ LTS

เชิงทดลอง20%

เบต้า79%

เบต้า79%

[Compaction](</th/concepts/compaction>), [บริบท](</th/concepts/context>), [Compaction การจัดการเซสชัน](</th/reference/session-management-compaction>)

เอนจินบริบท 2 ความสามารถ / รองรับ LTS

อัลฟ่า57%

เบต้า79%

เบต้า79%

[บริบท](</th/concepts/context>), [เอนจินบริบท](</th/concepts/context-engine>), [ชุดทดสอบเอนจินบริบทของ Codex](</th/plan/codex-context-engine-harness>)

ประวัติข้ามไคลเอนต์และความเท่าเทียมของเซสชัน 2 ความสามารถ

เชิงทดลอง40%

เบต้า79%

เบต้า79%

[เว็บแชต](</th/web/webchat>), [Android](</th/platforms/android>), [การกำหนดเส้นทางช่องทาง](</th/channels/channel-routing>)

การวินิจฉัย การบำรุงรักษา และการกู้คืน 3 ความสามารถ

เชิงทดลอง40%

เบต้า79%

เบต้า79%

[การวินิจฉัย](</th/gateway/diagnostics>), [Compaction การจัดการเซสชัน](</th/reference/session-management-compaction>), [แฟล็ก](</th/diagnostics/flags>)

พรอมป์หลักและบริบท 2 ความสามารถ / รองรับ LTS

เชิงทดลอง38%

เบต้า79%

เบต้า79%

[บริบท](</th/concepts/context>), [สุขอนามัยของทรานสคริปต์](</th/reference/transcript-hygiene>), [Discord](</th/channels/discord>)

หน่วยความจำ 5 ความสามารถ

เชิงทดลอง46%

เบต้า79%

เบต้า79%

[การกำหนดค่าหน่วยความจำ](</th/reference/memory-config>), [Memory Qmd](</th/concepts/memory-qmd>), [หน่วยความจำ](</th/concepts/memory>), [Discord](</th/channels/discord>)

การกำหนดเส้นทางเซสชัน 2 ความสามารถ / รองรับ LTS

เชิงทดลอง25%

เบต้า79%

เบต้า79%

[เซสชัน](</th/concepts/session>), [การกำหนดเส้นทางช่องทาง](</th/channels/channel-routing>), [Discord](</th/channels/discord>)

การคงอยู่ของทรานสคริปต์ 2 ความสามารถ / รองรับโดย LTS

ทดลอง0%

อัลฟา68%

เบตา79%

[Compaction การจัดการเซสชัน](</th/reference/session-management-compaction>), [สุขอนามัยของทรานสคริปต์](</th/reference/transcript-hygiene>)

เฟรมเวิร์กช่องทาง - M3 เบต้า - 8 ด้าน

ช่องทางจำนวนมากใช้สัญญาการส่งมอบและการกำหนดเส้นทางของ Gateway ร่วมกัน แต่พฤติกรรมของช่องทางจะแตกต่างกันไปตาม API ต้นทางและข้อจำกัดด้านนโยบายบัญชี

ความครอบคลุม ระยะทดลอง - 13%คุณภาพ เบต้า - 76%ความครบถ้วน เบต้า - 79%บางส่วน - 5

คำสั่งและการอนุมัติของการดำเนินการในช่องทาง 5 ความสามารถ

ทดลอง0%

เบต้า79%

เบต้า79%

[กลุ่ม](</th/channels/groups>), [Discord](</th/channels/discord>), [Google Chat](</th/channels/googlechat>), [Signal](</th/channels/signal>), [Matrix](</th/channels/matrix>)

การตั้งค่าช่องทาง 5 ความสามารถ / รองรับ LTS

ทดลอง14%

เบต้า79%

เบต้า79%

[ดัชนี](</th/channels>), [การจับคู่](</th/channels/pairing>), [การแก้ไขปัญหา](</th/channels/troubleshooting>), [Plugin ช่องทาง SDK](</th/plugins/sdk-channel-plugins>)

ลักษณะการทำงานของเธรดกลุ่มและห้องแวดล้อม 5 ความสามารถ

ทดลอง36%

เบต้า79%

เบต้า79%

[กลุ่ม](</th/channels/groups>), [ข้อความกลุ่ม](</th/channels/group-messages>), [เหตุการณ์ห้องแวดล้อม](</th/channels/ambient-room-events>), [กลุ่มออกอากาศ](</th/channels/broadcast-groups>), [Discord](</th/channels/discord>)

การเข้าถึงขาเข้าและด่านยืนยันตัวตน 5 ความสามารถ / รองรับ LTS

ทดลอง0%

อัลฟ่า68%

เบต้า79%

[กลุ่มการเข้าถึง](</th/channels/access-groups>), [กลุ่ม](</th/channels/groups>), [Discord](</th/channels/discord>), [LINE](</th/channels/line>)

ไฟล์แนบสื่อและข้อมูลช่องทางแบบสมบูรณ์ 4 ความสามารถ

ทดลอง0%

อัลฟ่า68%

เบต้า79%

[LINE](</th/channels/line>), [Signal](</th/channels/signal>), [Google Chat](</th/channels/googlechat>), [Matrix](</th/channels/matrix>), [Discord](</th/channels/discord>)

การส่งขาออกและไปป์ไลน์การตอบกลับ 4 ความสามารถ / รองรับ LTS

ทดลอง38%

เบต้า79%

เบต้า79%

[กลุ่ม](</th/channels/groups>), [เหตุการณ์ห้องแวดล้อม](</th/channels/ambient-room-events>), [Discord](</th/channels/discord>), [Matrix](</th/channels/matrix>), [ช่องทางการกำหนดค่า](</th/gateway/config-channels>)

การกำหนดเส้นทางและการส่งการสนทนา 10 ความสามารถ / รองรับ LTS

ทดลอง19%

เบต้า79%

เบต้า79%

[การกำหนดเส้นทางช่องทาง](</th/channels/channel-routing>), [กลุ่ม](</th/channels/groups>), [Discord](</th/channels/discord>), [Matrix](</th/channels/matrix>), [การแก้ไขปัญหา](</th/channels/troubleshooting>), [ข้อมูลอ้างอิงการกำหนดค่า](</th/gateway/configuration-reference>)

สถานะ สุขภาพ และการควบคุมสำหรับผู้ปฏิบัติงาน 4 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า79%

เบต้า79%

[สุขภาพ](</th/gateway/health>), [ข้อมูลอ้างอิงการกำหนดค่า](</th/gateway/configuration-reference>), [การแก้ไขปัญหา](</th/channels/troubleshooting>), [Discord](</th/channels/discord>)

Observability - M3 Beta - 5 areas

มีเอกสาร OTel, Prometheus, การบันทึก log และการวินิจฉัยอยู่แล้ว ต้องมีการทบทวนระดับความสมบูรณ์แบบสาธารณะสำหรับ "สิ่งที่ผู้ปฏิบัติการควรดูก่อน"

ความครอบคลุม Experimental - 18%คุณภาพ Beta - 75%ความสมบูรณ์ Beta - 79%บางส่วน - 3

สุขภาพและการซ่อมแซม 12 ความสามารถ / รองรับ LTS

Experimental28%

Beta79%

Beta79%

[สุขภาพ](</th/gateway/health>), [Telegram](</th/channels/telegram>), [Doctor](</th/cli/doctor>), [Doctor](</th/gateway/doctor>), [พาธย่อยของ Sdk](</th/plugins/sdk-subpaths>), [สุขภาพ](</th/cli/health>), [โปรโตคอล](</th/gateway/protocol>)

การบันทึกล็อก 5 ความสามารถ / รองรับ LTS

Experimental0%

Alpha68%

Beta79%

[การบันทึกล็อก](</th/logging>), [การบันทึกล็อก](</th/gateway/logging>), [ล็อก](</th/cli/logs>)

การรวบรวมข้อมูลวินิจฉัย 8 ความสามารถ

Experimental30%

Beta79%

Beta79%

[การวินิจฉัย](</th/gateway/diagnostics>), [สุขภาพ](</th/gateway/health>), [ชุดทดสอบ Codex](</th/plugins/codex-harness>), [โปรโตคอล](</th/gateway/protocol>)

การส่งออก Telemetry 13 ความสามารถ

Experimental33%

Beta79%

Beta79%

[Hooks](</th/plugins/hooks>), [Opentelemetry](</th/gateway/opentelemetry>), [การบันทึกล็อก](</th/logging>), [พาธย่อยของ Sdk](</th/plugins/sdk-subpaths>), [Diagnostics Otel](</th/plugins/reference/diagnostics-otel>), [Prometheus](</th/gateway/prometheus>), [Diagnostics Prometheus](</th/plugins/reference/diagnostics-prometheus>)

การวินิจฉัยเซสชัน 4 ความสามารถ / รองรับ LTS

Experimental0%

Alpha68%

Beta79%

[Opentelemetry](</th/gateway/opentelemetry>), [Prometheus](</th/gateway/prometheus>), [การวินิจฉัย](</th/gateway/diagnostics>), [โปรโตคอล](</th/gateway/protocol>)

เว็บแอป Gateway - M3 Beta - 6 พื้นที่

Web UI ได้รับการจัดทำเอกสารพร้อมโฟลว์การจับคู่ แชต PWA, Talk, push และ Gateway ระยะไกล เลื่อนระดับหลังจาก scorecard ข้ามเบราว์เซอร์และ PWA บนอุปกรณ์เคลื่อนที่

ความครอบคลุม Experimental - 4%คุณภาพ Beta - 74%ความสมบูรณ์ Beta - 79%ไม่มี

การพูดคุยแบบเรียลไทม์ในเบราว์เซอร์ 5 ความสามารถ

ทดลอง0%

อัลฟ่า68%

เบต้า79%

[ส่วนติดต่อควบคุม](</th/web/control-ui>), [โปรโตคอล](</th/gateway/protocol>), [การพูดคุย](</th/nodes/talk>)

การเข้าถึงและความไว้วางใจในเบราว์เซอร์ 5 ความสามารถ

ทดลอง0%

อัลฟ่า68%

เบต้า79%

[ส่วนติดต่อควบคุม](</th/web/control-ui>), [แดชบอร์ด](</th/web/dashboard>), [Tailscale](</th/gateway/tailscale>), [ระยะไกล](</th/gateway/remote>)

การกำหนดค่า 5 ความสามารถ

ทดลอง0%

อัลฟ่า68%

เบต้า79%

[ส่วนติดต่อควบคุม](</th/web/control-ui>), [การกำหนดค่า](</th/gateway/configuration>)

ส่วนติดต่อผู้ใช้บนเบราว์เซอร์ 10 ความสามารถ

ทดลอง8%

เบต้า79%

เบต้า79%

[ส่วนติดต่อควบคุม](</th/web/control-ui>), [ดัชนี](</th/web>), [แดชบอร์ด](</th/web/dashboard>), [โปรโตคอล](</th/gateway/protocol>)

การสนทนา WebChat 15 ความสามารถ

ทดลอง10%

เบต้า79%

เบต้า79%

[ส่วนติดต่อควบคุม](</th/web/control-ui>), [Webchat](</th/web/webchat>), [เริ่มต้นใช้งาน](</th/start/getting-started>), [การกำหนดเส้นทางช่องทาง](</th/channels/channel-routing>), [การดำเนินการไฟล์อย่างปลอดภัย](</th/gateway/security/secure-file-operations>)

คอนโซลผู้ปฏิบัติงาน 10 ความสามารถ

ทดลอง8%

เบต้า79%

เบต้า79%

[ส่วนติดต่อควบคุม](</th/web/control-ui>), [สุขภาพ](</th/gateway/health>), [โปรโตคอล](</th/gateway/protocol>), [แดชบอร์ด](</th/web/dashboard>)

Plugin - M3 เบต้า - 9 ด้าน

มีเอกสารที่ครอบคลุมและหลักฐานรันไทม์ภายในที่แข็งแรงครอบคลุมแมนิเฟสต์ การค้นพบ การโหลด สถาปัตยกรรมผู้ให้บริการ/เครื่องมือ และขอบเขตการอนุมัติ ให้แถวนี้อยู่ที่ระดับเบต้าจนกว่า API ของ SDK สาธารณะ/พาธย่อย และหลักฐานการเผยแพร่ภายนอกจะแข็งแรงขึ้น

ความครอบคลุม ทดลอง - 12%คุณภาพ เบต้า - 72%ความสมบูรณ์ เบต้า - 79%บางส่วน - 7

การเขียนและการจัดแพ็กเกจ Plugin 8 ความสามารถ / รองรับแบบ LTS

ทดลอง0%

แอลฟา68%

เบตา79%

[การสร้าง Plugin](</th/plugins/building-plugins>), [ภาพรวม SDK](</th/plugins/sdk-overview>), [จุดเข้าใช้งาน SDK](</th/plugins/sdk-entrypoints>), [พาธย่อย SDK](</th/plugins/sdk-subpaths>), [Manifest](</th/plugins/manifest>), [เอกสารอ้างอิง](</th/plugins/reference>)

Plugin ที่มาพร้อมชุด 5 ความสามารถ / รองรับแบบ LTS

ทดลอง0%

แอลฟา68%

เบตา79%

[รายการ Plugin](</th/plugins/plugin-inventory>), [Plugin](</th/cli/plugins>), [รายละเอียดภายในของสถาปัตยกรรม](</th/plugins/architecture-internals>)

Canvas Plugin 6 ความสามารถ

ทดลอง0%

แอลฟา68%

เบตา79%

[Canvas](</th/plugins/reference/canvas>), [Canvas](</th/refactor/canvas>), [เอกสารอ้างอิงการกำหนดค่า](</th/gateway/configuration-reference>)

การติดตั้งและการเรียกใช้ Plugin 6 ความสามารถ / รองรับแบบ LTS

ทดลอง35%

เบตา79%

เบตา79%

[สถาปัตยกรรม](</th/plugins/architecture>), [รายละเอียดภายในของสถาปัตยกรรม](</th/plugins/architecture-internals>), [Plugin](</th/cli/plugins>)

Channel Plugin 5 ความสามารถ / รองรับแบบ LTS

ทดลอง0%

แอลฟา68%

เบตา79%

[Channel Plugin ของ SDK](</th/plugins/sdk-channel-plugins>), [ขาเข้าของ Channel ใน SDK](</th/plugins/sdk-channel-inbound>), [ขาออกของ Channel ใน SDK](</th/plugins/sdk-channel-outbound>)

Provider และ Tool Plugin 6 ความสามารถ / รองรับแบบ LTS

ทดลอง43%

เบตา79%

เบตา79%

[Provider Plugin ของ SDK](</th/plugins/sdk-provider-plugins>), [Tool Plugin](</th/plugins/tool-plugins>), [การเพิ่มความสามารถ](</th/plugins/adding-capabilities>)

การอนุมัติ Plugin 6 ความสามารถ / รองรับแบบ LTS

ทดลอง0%

แอลฟา68%

เบตา79%

[คำขอสิทธิ์ของ Plugin](</th/plugins/plugin-permission-requests>), [การอนุมัติ Exec](</th/tools/exec-approvals>), [Channel Plugin ของ SDK](</th/plugins/sdk-channel-plugins>)

การเผยแพร่ Plugin 6 ความสามารถ / รองรับแบบ LTS

ทดลอง0%

แอลฟา68%

เบตา79%

[Plugin](</th/cli/plugins>), [ความเข้ากันได้](</th/plugins/compatibility>), [การเผยแพร่](</th/clawhub/publishing>)

การทดสอบ Plugin 6 ความสามารถ

ทดลอง27%

เบตา79%

เบตา79%

[การทดสอบ SDK](</th/plugins/sdk-testing>), [การตั้งค่า SDK](</th/plugins/sdk-setup>), [ชุดทดสอบ Codex](</th/plugins/codex-harness>)

ความปลอดภัย การยืนยันตัวตน การจับคู่ และความลับ - M3 Beta - 6 ด้าน

มีเอกสารและพื้นผิวการเสริมความแข็งแกร่งที่ดีอยู่แล้ว เลื่อนระดับหลังจากการรันสถานการณ์อัปเกรด/ความปลอดภัยเป็นประจำพิสูจน์แล้วว่าไม่มีการถดถอยในการตั้งค่า

ความครอบคลุม Experimental - 16%คุณภาพ Beta - 72%ความสมบูรณ์ Beta - 79%บางส่วน - 5

นโยบายการอนุมัติและมาตรการป้องกันเครื่องมือ 2 ความสามารถ / รองรับ LTS

Alpha50%

Beta79%

Beta79%

[การอนุมัติ Exec](</th/tools/exec-approvals>), [การอนุมัติ](</th/cli/approvals>), [คำขอสิทธิ์ของ Plugin](</th/plugins/plugin-permission-requests>), [การตรวจสอบ Audit](</th/gateway/security/audit-checks>)

การยืนยันตัวตน Gateway และการเข้าถึงระยะไกล 9 ความสามารถ / รองรับ LTS

Experimental0%

Alpha68%

Beta79%

[ดัชนี](</th/gateway/security>), [Runbook การเปิดเผย](</th/gateway/security/exposure-runbook>), [การยืนยันตัวตนผ่านพร็อกซีที่เชื่อถือได้](</th/gateway/trusted-proxy-auth>), [Tailscale](</th/gateway/tailscale>), [ระยะไกล](</th/gateway/remote>), [ข้อมูลอ้างอิงการกำหนดค่า](</th/gateway/configuration-reference>), [Gateway](</th/cli/gateway>), [Doctor](</th/cli/doctor>), [Control Ui](</th/web/control-ui>), [การควบคุมเบราว์เซอร์](</th/tools/browser-control>), [การตรวจสอบ Audit](</th/gateway/security/audit-checks>)

การควบคุมการเข้าถึงช่องทาง 3 ความสามารถ / รองรับ LTS

Experimental0%

Alpha68%

Beta79%

[การจับคู่](</th/channels/pairing>), [Telegram](</th/channels/telegram>), [กลุ่มการเข้าถึง](</th/channels/access-groups>), [การตรวจสอบ Audit](</th/gateway/security/audit-checks>)

การจับคู่อุปกรณ์และ Node 11 ความสามารถ / รองรับ LTS

Experimental0%

Alpha68%

Beta79%

[โปรโตคอล](</th/gateway/protocol>), [อุปกรณ์](</th/cli/devices>), [การจับคู่](</th/channels/pairing>), [การจับคู่](</th/gateway/pairing>), [ขอบเขตผู้ปฏิบัติงาน](</th/gateway/operator-scopes>), [Control Ui](</th/web/control-ui>), [Webchat](</th/web/webchat>), [การอนุมัติ](</th/cli/approvals>)

ความน่าเชื่อถือของ Plugin 2 ความสามารถ

Experimental0%

Alpha68%

Beta79%

[Manifest](</th/plugins/manifest>), [คำขอสิทธิ์ของ Plugin](</th/plugins/plugin-permission-requests>), [จัดการ Plugin](</th/plugins/manage-plugins>), [การตรวจสอบ Audit](</th/gateway/security/audit-checks>)

สุขอนามัยของข้อมูลประจำตัวและความลับ 5 ความสามารถ / รองรับ LTS

Experimental46%

Beta79%

Beta79%

[การยืนยันตัวตน](</th/gateway/authentication>), [โมเดล](</th/cli/models>), [Openai](</th/providers/openai>), [Oauth](</th/concepts/oauth>), [ความลับ](</th/gateway/secrets>), [ความลับ](</th/cli/secrets>), [พื้นผิวข้อมูลประจำตัว Secretref](</th/reference/secretref-credential-surface>), [การตรวจสอบ Audit](</th/gateway/security/audit-checks>)

ระบบอัตโนมัติ: cron, hooks, tasks, polling - M3 Beta - 6 ด้าน

มีเอกสารและใช้งานได้ แต่หลักฐานสถานการณ์ควรครอบคลุมการส่งมอบแบบไม่ต้องเฝ้าดู การลองใหม่ และการมองเห็นความล้มเหลว

ความครอบคลุม Experimental - 2%คุณภาพ Beta - 72%ความสมบูรณ์ Beta - 79%ไม่มี

งาน Cron 15 ความสามารถ

ขั้นทดลอง0%

เบต้า79%

เบต้า79%

[งาน Cron](</th/automation/cron-jobs>), [Cron](</th/cli/cron>), [โปรโตคอล](</th/gateway/protocol>), [งาน](</th/automation/tasks>), [Discord](</th/channels/discord>)

การรับเหตุการณ์เข้า 15 ความสามารถ

ขั้นทดลอง0%

อัลฟ่า68%

เบต้า79%

[Telegram](</th/channels/telegram>), [Zalo](</th/channels/zalo>), [การแก้ไขปัญหา](</th/channels/troubleshooting>), [iMessage จาก BlueBubbles](</th/channels/imessage-from-bluebubbles>), [การผสานรวม Gmail Pub/Sub](</th/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pub/Sub](</th/automation/cron-jobs>), [Webhooks](</th/cli/webhooks>), [Webhooks](</th/automation/cron-jobs#webhooks>), [Webhook](</th/automation/cron-jobs>)

Automation Hooks 11 ความสามารถ

ขั้นทดลอง0%

อัลฟ่า68%

เบต้า79%

[Hooks](</th/automation/hooks>), [Hooks](</th/cli/hooks>), [Hooks](</th/plugins/hooks>), [คำขอสิทธิ์ของ Plugin](</th/plugins/plugin-permission-requests>), [เส้นทางย่อยของ SDK](</th/plugins/sdk-subpaths>)

งานและโฟลว์เบื้องหลัง 10 ความสามารถ

ขั้นทดลอง0%

อัลฟ่า68%

เบต้า79%

[งาน](</th/automation/tasks>), [ดัชนี](</th/automation>), [งาน](</th/cli/tasks>), [TaskFlow](</th/automation/taskflow>), [รันไทม์ SDK](</th/plugins/sdk-runtime>)

Heartbeat 5 ความสามารถ

ขั้นทดลอง14%

เบต้า79%

เบต้า79%

[ดัชนี](</th/automation>), [Heartbeat](</th/gateway/heartbeat>), [ข้อผูกพัน](</th/concepts/commitments>)

การควบคุมการโพล 10 ความสามารถ

ขั้นทดลอง0%

อัลฟ่า68%

เบต้า79%

[Poll](</th/cli/message>), [ข้อความ](</th/cli/message>), [Telegram](</th/channels/telegram>), [Msteams](</th/channels/msteams>), [กระบวนการเบื้องหลัง](</th/gateway/background-process>)

ความเข้าใจสื่อและการสร้างสื่อ - M2 Alpha - 6 พื้นที่

มีพื้นผิวความสามารถที่กว้างอยู่แล้ว แต่ความแตกต่างระหว่างผู้ให้บริการ ขีดจำกัดไฟล์ และความเท่าเทียมระหว่าง Node/แอป ทำให้สิ่งนี้ยังไม่เสถียร

ความครอบคลุม ขั้นทดลอง - 2%คุณภาพ อัลฟ่า - 64%ความสมบูรณ์ อัลฟ่า - 68%ไม่มี

การรับเข้าและการเข้าถึงสื่อ 8 ความสามารถ

ทดลอง0%

Alpha61%

Alpha68%

[ภาพรวมสื่อ](</th/tools/media-overview>), [ความเข้าใจสื่อ](</th/nodes/media-understanding>), [การดำเนินการกับไฟล์อย่างปลอดภัย](</th/gateway/security/secure-file-operations>), [Pdf](</th/tools/pdf>), [การสร้างรูปภาพ](</th/tools/image-generation>), [Qr](</th/cli/qr>), [LINE](</th/channels/line>), [WhatsApp](</th/channels/whatsapp>)

การจัดการสื่อในช่องทาง 5 ความสามารถ

ทดลอง0%

Alpha61%

Alpha68%

[รูปภาพ](</th/nodes/images>), [ภาพรวมสื่อ](</th/tools/media-overview>), [Discord](</th/channels/discord>)

การกำหนดค่าสื่อ 1 ความสามารถ

ทดลอง0%

Alpha61%

Alpha68%

[ภาพรวมสื่อ](</th/tools/media-overview>), [การสร้างรูปภาพ](</th/tools/image-generation>), [Manifest](</th/plugins/manifest>), [Codex Harness](</th/plugins/codex-harness>)

การส่งมอบการแปลงข้อความเป็นเสียงพูด 2 ความสามารถ

ทดลอง0%

Alpha61%

Alpha68%

[Tts](</th/tools/tts>), [ภาพรวมสื่อ](</th/tools/media-overview>), [Discord](</th/channels/discord>)

ความเข้าใจสื่อ 12 ความสามารถ

ทดลอง7%

Alpha69%

Alpha69%

[เสียง](</th/nodes/audio>), [ความเข้าใจสื่อ](</th/nodes/media-understanding>), [ภาพรวมสื่อ](</th/tools/media-overview>), [WhatsApp](</th/channels/whatsapp>), [รูปภาพ](</th/nodes/images>), [Infer](</th/cli/infer>), [Pdf](</th/tools/pdf>)

การสร้างสื่อ 17 ความสามารถ

ทดลอง5%

Alpha69%

Alpha69%

[การสร้างรูปภาพ](</th/tools/image-generation>), [ภาพรวมสื่อ](</th/tools/media-overview>), [Skills](</th/tools/skills>), [การสร้างเพลง](</th/tools/music-generation>), [การสร้างวิดีโอ](</th/tools/video-generation>)

เสียงและการสนทนาแบบเรียลไทม์ - M2 Alpha - 6 พื้นที่

มีการใช้งานหลายรูปแบบใน Control UI, แอป และผู้ให้บริการต่าง ๆ ต้องมีสกอร์การ์ดด้านเวลาแฝง โหมดความล้มเหลว และการตั้งค่าก่อน beta

ความครอบคลุม ทดลอง - 0%คุณภาพ Alpha - 61%ความสมบูรณ์ Alpha - 68%ไม่มี

ผู้ให้บริการ Talk 7 ความสามารถ

ทดลอง0%

Alpha61%

Alpha68%

[Openai](</th/providers/openai>), [Google](</th/providers/google>), [Plugin ผู้ให้บริการ SDK](</th/plugins/sdk-provider-plugins>), [Talk](</th/nodes/talk>), [UI ควบคุม](</th/web/control-ui>)

เซสชัน Talk แบบเรียลไทม์ 11 ความสามารถ

ทดลอง0%

Alpha61%

Alpha68%

[Talk](</th/nodes/talk>), [UI ควบคุม](</th/web/control-ui>)

เสียงพูดและการถอดเสียง 5 ความสามารถ

ทดลอง0%

Alpha61%

Alpha68%

[Talk](</th/nodes/talk>), [Openai](</th/providers/openai>), [Google](</th/providers/google>)

Talk ของแอปเนทีฟ 4 ความสามารถ

ทดลอง0%

Alpha61%

Alpha68%

[Talk](</th/nodes/talk>), [Voicewake](</th/platforms/mac/voicewake>)

การปลุกด้วยเสียงและการกำหนดเส้นทาง 4 ความสามารถ

ทดลอง0%

Alpha61%

Alpha68%

[Voicewake](</th/nodes/voicewake>), [Voicewake](</th/platforms/mac/voicewake>), [โอเวอร์เลย์เสียง](</th/platforms/mac/voice-overlay>)

ความสามารถในการสังเกตการณ์ของ Talk 5 ความสามารถ

ทดลอง0%

Alpha61%

Alpha68%

[UI ควบคุม](</th/web/control-ui>), [โอเวอร์เลย์เสียง](</th/platforms/mac/voice-overlay>), [Talk](</th/nodes/talk>)

TUI - M2 Alpha - 5 พื้นที่

มีอยู่ในเอกสารและซอร์สโค้ด แต่ยังมองเห็นได้น้อยกว่าในฐานะเวิร์กโฟลว์หลักของผู้ใช้ ต้องมีการกำหนดสถานการณ์อย่างชัดเจน

ความครอบคลุม ทดลอง - 0%คุณภาพ Alpha - 59%ความสมบูรณ์ Alpha - 66%ไม่มี

โหมด Runtime 14 ความสามารถ

เชิงทดลอง0%

Alpha59%

Alpha66%

[TUI](</th/cli/tui>), [TUI](</th/web/tui>), [ดัชนี](</th/cli>)

อินพุตและคำสั่ง 8 ความสามารถ

เชิงทดลอง0%

Alpha59%

Alpha66%

[TUI](</th/web/tui>)

การจัดการเซสชัน 3 ความสามารถ

เชิงทดลอง0%

Alpha59%

Alpha66%

[TUI](</th/web/tui>), [เซสชัน](</th/cli/sessions>)

การเรียกใช้เชลล์ในเครื่อง 4 ความสามารถ

เชิงทดลอง0%

Alpha59%

Alpha66%

[TUI](</th/web/tui>), [TUI](</th/cli/tui>)

การเรนเดอร์และความปลอดภัยของเอาต์พุต 4 ความสามารถ

เชิงทดลอง0%

Alpha59%

Alpha66%

[TUI](</th/web/tui>), [QR](</th/cli/qr>), [บันทึก](</th/cli/logs>), [การเติมคำสั่งอัตโนมัติ](</th/cli/completion>)

ClawHub - M2 Alpha - 4 พื้นที่

มีเอกสารสาธารณะและแนวคิดของระบบนิเวศแล้ว ยังต้องมีตารางคะแนนสำหรับการติดตั้ง ความน่าเชื่อถือ การอัปเดต การย้อนกลับ และความเข้ากันได้

ความครอบคลุม เชิงทดลอง - 0%คุณภาพ Alpha - 58%ความครบถ้วน Alpha - 62%ไม่มี

การเผยแพร่ ความสามารถ 7 รายการ

ทดลอง0%

อัลฟา54%

อัลฟา55%

[การเผยแพร่](</th/clawhub/publishing>), [การสร้าง Skills](</th/tools/creating-skills>), [ชุมชน](</th/plugins/community>)

การค้นพบแค็ตตาล็อก ความสามารถ 5 รายการ

ทดลอง0%

อัลฟา61%

อัลฟา68%

[Plugin](</th/tools/plugin>), [Plugins](</th/cli/plugins>), [Skills](</th/cli/skills>), [Skills](</th/tools/skills>), [ชุมชน](</th/plugins/community>)

ความเข้ากันได้และความน่าเชื่อถือ ความสามารถ 12 รายการ

ทดลอง0%

อัลฟา55%

อัลฟา56%

[Plugin](</th/tools/plugin>), [Plugins](</th/cli/plugins>), [ความเข้ากันได้](</th/plugins/compatibility>), [บัญชีรายการ Plugin](</th/plugins/plugin-inventory>), [การเผยแพร่](</th/clawhub/publishing>), [Skills](</th/tools/skills>), [การกำหนดค่า Skills](</th/tools/skills-config>)

วงจรชีวิตและสถานภาพของ Plugin ความสามารถ 26 รายการ

ทดลอง0%

อัลฟา61%

อัลฟา68%

[Plugin](</th/tools/plugin>), [Plugins](</th/cli/plugins>), [Skills](</th/cli/skills>), [Skills](</th/tools/skills>), [โปรโตคอล](</th/gateway/protocol>), [บันเดิล](</th/plugins/bundles>), [การแก้ไขการพึ่งพา](</th/plugins/dependency-resolution>)

OpenClaw App SDK - M2 อัลฟา - 6 พื้นที่

OpenClaw App SDK เป็นสัญญาแอปภายนอกที่แยกต่างหากจากรันไทม์ Gateway และ Plugin SDK การให้คะแนนปัจจุบันแสดงเส้นทาง `@openclaw/sdk` ที่มีอยู่จริง พร้อมช่องว่างด้านการจัดแพ็กเกจสาธารณะ การค้นพบอัตโนมัติ การอนุมัติ ตัวช่วย และความเข้ากันได้

ความครอบคลุม ทดลอง - 3%คุณภาพ อัลฟา - 54%ความสมบูรณ์ อัลฟา - 53%ไม่มี

API ไคลเอนต์ 4 ความสามารถ

ทดลอง0%

อัลฟา51%

อัลฟา50%

[OpenClaw SDK](</th/gateway/external-apps>), [การออกแบบ API ของ OpenClaw SDK](</th/gateway/external-apps>)

การเข้าถึง Gateway 5 ความสามารถ

ทดลอง0%

อัลฟา53%

อัลฟา54%

[OpenClaw SDK](</th/gateway/external-apps>), [การออกแบบ API ของ OpenClaw SDK](</th/gateway/external-apps>), [โปรโตคอล](</th/gateway/protocol>), [ดัชนี](</th/gateway/security>)

การสนทนาของเอเจนต์ 6 ความสามารถ

ทดลอง0%

อัลฟา52%

อัลฟา52%

[OpenClaw SDK](</th/gateway/external-apps>), [การออกแบบ API ของ OpenClaw SDK](</th/gateway/external-apps>), [โปรโตคอล](</th/gateway/protocol>)

เหตุการณ์และการอนุมัติ 5 ความสามารถ

ทดลอง0%

อัลฟา52%

อัลฟา52%

[OpenClaw SDK](</th/gateway/external-apps>), [การออกแบบ API ของ OpenClaw SDK](</th/gateway/external-apps>), [โปรโตคอล](</th/gateway/protocol>)

ตัวช่วยทรัพยากร 5 ความสามารถ

ทดลอง17%

อัลฟา62%

อัลฟา53%

[OpenClaw SDK](</th/gateway/external-apps>), [การออกแบบ API ของ OpenClaw SDK](</th/gateway/external-apps>)

ความเข้ากันได้ 5 ความสามารถ

ทดลอง0%

อัลฟา54%

อัลฟา55%

[การออกแบบ API ของ OpenClaw SDK](</th/gateway/external-apps>), [Typebox](</th/concepts/typebox>), [โปรโตคอล](</th/gateway/protocol>)

### แพลตฟอร์ม

Linux Gateway host - M4 Stable - 5 areas

แนะนำให้ใช้รันไทม์ Node, มีเอกสารสำหรับบริการผู้ใช้ systemd และมีคำแนะนำสำหรับ VPS/คอนเทนเนอร์อย่างครอบคลุม

ความครอบคลุม ทดลอง - 0%คุณภาพ เบตา - 75%ความครบถ้วน เสถียร - 89%บางส่วน - 4

การตั้งค่าและการอัปเดตโฮสต์ 4 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า75%

เสถียร89%

[ดัชนี](</th/install>), [การอัปเดต](</th/install/updating>), [Linux](</th/platforms/linux>), [ดัชนี](</th/platforms>)

รันไทม์ Gateway และการควบคุมบริการ 6 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า75%

เสถียร89%

[ดัชนี](</th/gateway>), [Gateway](</th/cli/gateway>), [Linux](</th/platforms/linux>), [VPS](</th/vps>)

การเข้าถึงระยะไกลและความปลอดภัย 6 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า75%

เสถียร89%

[ระยะไกล](</th/gateway/remote>), [Tailscale](</th/gateway/tailscale>), [คู่มือปฏิบัติเมื่อมีการเปิดเผย](</th/gateway/security/exposure-runbook>), [การรับรองความถูกต้อง](</th/gateway/authentication>), [ความลับ](</th/gateway/secrets>)

การวินิจฉัยและการซ่อมแซม 4 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า75%

เสถียร89%

[สถานะ](</th/cli/status>), [บันทึก](</th/cli/logs>), [เครื่องมือตรวจสุขภาพ](</th/cli/doctor>), [การวินิจฉัย](</th/gateway/diagnostics>), [ดัชนี](</th/gateway>)

เป้าหมายการปรับใช้ 3 ความสามารถ

ทดลอง0%

เบต้า75%

เสถียร89%

[VPS](</th/vps>), [Docker](</th/install/docker>), [Hetzner](</th/install/hetzner>), [DigitalOcean](</th/install/digitalocean>), [Kubernetes](</th/install/kubernetes>), [Podman](</th/install/podman>)

โฮสต์ Gateway บน macOS - M4 เสถียร - 7 พื้นที่

มีเอกสารสำหรับพาธบริการ LaunchAgent, โหมด Gateway แบบ local/remote, การติดตั้ง CLI และการผสานรวมแอปแล้ว

ความครอบคลุม ทดลอง - 0%คุณภาพ เบต้า - 74%ความสมบูรณ์ เสถียร - 88%ไม่มี

การตั้งค่า CLI 4 ความสามารถ

เชิงทดลอง0%

เบต้า74%

เสถียร88%

[Macos](</th/platforms/macos>), [Gateway แบบรวมมาให้](</th/platforms/mac/bundled-gateway>), [ตัวติดตั้ง](</th/install/installer>), [Node](</th/install/node>)

การผสานรวม Gateway ภายในเครื่อง 9 ความสามารถ

เชิงทดลอง0%

เบต้า74%

เสถียร88%

[Macos](</th/platforms/macos>), [Gateway แบบรวมมาให้](</th/platforms/mac/bundled-gateway>), [ระยะไกล](</th/platforms/mac/remote>), [ดัชนี](</th/gateway>), [Gateway](</th/cli/gateway>), [Bonjour](</th/gateway/bonjour>)

โหมด Gateway ระยะไกล 5 ความสามารถ

เชิงทดลอง0%

เบต้า74%

เสถียร88%

[ระยะไกล](</th/platforms/mac/remote>), [ระยะไกล](</th/gateway/remote>), [Tailscale](</th/gateway/tailscale>)

วงจรชีวิตบริการ Gateway 10 ความสามารถ

เชิงทดลอง0%

เบต้า74%

เสถียร88%

[Macos](</th/platforms/macos>), [Gateway แบบรวมมาให้](</th/platforms/mac/bundled-gateway>), [Gateway](</th/cli/gateway>), [ดัชนี](</th/gateway>), [อัปเดต](</th/cli/update>), [การอัปเดต](</th/install/updating>), [ถอนการติดตั้ง](</th/install/uninstall>), [การแก้ไขปัญหา](</th/gateway/troubleshooting>)

การวินิจฉัยและความสามารถในการสังเกต 4 ความสามารถ

เชิงทดลอง0%

เบต้า74%

เสถียร88%

[Gateway แบบรวมมาให้](</th/platforms/mac/bundled-gateway>), [Macos](</th/platforms/macos>), [Gateway](</th/cli/gateway>), [Doctor](</th/gateway/doctor>), [การแก้ไขปัญหา](</th/gateway/troubleshooting>)

สิทธิ์และความสามารถเนทีฟ 4 ความสามารถ

เชิงทดลอง0%

เบต้า74%

เสถียร88%

[Macos](</th/platforms/macos>), [ระยะไกล](</th/platforms/mac/remote>)

โปรไฟล์และการแยกส่วน 5 ความสามารถ

เชิงทดลอง0%

เบต้า74%

เสถียร88%

[หลาย Gateway](</th/gateway/multiple-gateways>), [ดัชนี](</th/gateway>), [Gateway](</th/cli/gateway>)

การโฮสต์ด้วย Docker และ Podman - M3 เบต้า - 4 ส่วน

มีเอกสารการติดตั้งอยู่แล้วและเป็นเส้นทางการปรับใช้ที่ใช้กันทั่วไป โปรโมตหลังจากสโมกเทสต์รุ่นเผยแพร่ที่เกิดซ้ำบันทึกพฤติกรรมการอัปเกรดและวอลุ่มแล้ว

ความครอบคลุม เชิงทดลอง - 7%คุณภาพ เบต้า - 71%ความสมบูรณ์ เบต้า - 79%ไม่มี

การตั้งค่าคอนเทนเนอร์ 6 ความสามารถ

ทดลอง0%

อัลฟ่า68%

เบต้า79%

[Docker](</th/install/docker>), [Podman](</th/install/podman>)

การดำเนินงานคอนเทนเนอร์ 11 ความสามารถ

ทดลอง0%

อัลฟ่า68%

เบต้า79%

[Podman](</th/install/podman>), [รันไทม์ Docker VM](</th/install/docker-vm-runtime>), [Docker](</th/install/docker>), [Hetzner](</th/install/hetzner>), [Hostinger](</th/install/hostinger>)

การเผยแพร่และการตรวจสอบความถูกต้องของอิมเมจ 5 ความสามารถ

ทดลอง29%

เบต้า79%

เบต้า79%

[Docker](</th/install/docker>), [รันไทม์ Docker VM](</th/install/docker-vm-runtime>), [การตรวจสอบความถูกต้องของรีลีสเต็มรูปแบบ](</th/reference/full-release-validation>)

แซนด์บ็อกซ์และเครื่องมือสำหรับเอเจนต์ 3 ความสามารถ

ทดลอง0%

อัลฟ่า68%

เบต้า79%

[Docker](</th/install/docker>), [รันไทม์ Docker VM](</th/install/docker-vm-runtime>)

Windows ผ่าน WSL2 - M3 เบต้า - 6 พื้นที่

เส้นทาง Windows ที่แนะนำ พร้อมคำแนะนำ systemd/user-service และเอกสารลำดับการบูต โปรโมตหลังจากมีสกอร์การ์ดการติดตั้ง/อัปเดตซ้ำหลายครั้ง

ความครอบคลุม ทดลอง - 6%คุณภาพ อัลฟ่า - 69%ความสมบูรณ์ เบต้า - 79%บางส่วน - 5

การตั้งค่า WSL 6 ความสามารถ / รองรับ LTS

Experimental0%

Alpha67%

Beta79%

[Windows](</th/platforms/windows>), [เริ่มต้นใช้งาน](</th/start/getting-started>)

CLI 8 ความสามารถ / รองรับ LTS

Experimental0%

Alpha67%

Beta79%

[Windows](</th/platforms/windows>), [เริ่มต้นใช้งาน](</th/start/getting-started>), [การอัปเดต](</th/install/updating>), [Onboard](</th/cli/onboard>), [Doctor](</th/cli/doctor>), [สถานะ](</th/cli/status>), [บันทึก](</th/cli/logs>)

วงจรชีวิตบริการ Gateway 10 ความสามารถ / รองรับ LTS

Experimental0%

Alpha67%

Beta79%

[Windows](</th/platforms/windows>), [ดัชนี](</th/gateway>), [Doctor](</th/gateway/doctor>)

การเข้าถึงและการเปิดเผย Gateway 11 ความสามารถ / รองรับ LTS

Experimental0%

Alpha67%

Beta79%

[การยืนยันตัวตน](</th/gateway/authentication>), [ความลับ](</th/gateway/secrets>), [ระยะไกล](</th/gateway/remote>), [คู่มือปฏิบัติเมื่อมีการเปิดเผย](</th/gateway/security/exposure-runbook>), [Windows](</th/platforms/windows>)

การวินิจฉัยและการซ่อมแซม 6 ความสามารถ / รองรับ LTS

Experimental38%

Beta79%

Beta79%

[Windows](</th/platforms/windows>), [สถานะ](</th/cli/status>), [บันทึก](</th/cli/logs>), [Doctor](</th/cli/doctor>), [Doctor](</th/gateway/doctor>)

เบราว์เซอร์และ UI ควบคุม 6 ความสามารถ

Experimental0%

Alpha67%

Beta79%

[การแก้ไขปัญหา Browser Wsl2 Windows Remote Cdp](</th/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [เบราว์เซอร์](</th/tools/browser>), [UI ควบคุม](</th/web/control-ui>)

Raspberry Pi และอุปกรณ์ Linux ขนาดเล็ก - M3 Beta - 4 พื้นที่

มีเอกสารแพลตฟอร์มอยู่แล้ว และเส้นทาง Gateway อิง Linux ต้องมีหลักฐานการทดสอบ smoke สำหรับรุ่นที่เฉพาะกับฮาร์ดแวร์เพื่อขยับระดับให้สูงขึ้น

ความครอบคลุม Experimental - 0%คุณภาพ Alpha - 67%ความสมบูรณ์ Beta - 79%ไม่มี

การตั้งค่าและความเข้ากันได้ 12 ความสามารถ

เชิงทดลอง0%

Alpha67%

Beta79%

[Raspberry Pi](</th/install/raspberry-pi>), [ดัชนี](</th/install>), [คำถามที่พบบ่อยสำหรับการรันครั้งแรก](</th/help/faq-first-run>), [คำถามที่พบบ่อย](</th/help/faq>), [Linux](</th/platforms/linux>), [ตัวติดตั้ง](</th/install/installer>)

การเข้าถึงระยะไกลและการตรวจสอบสิทธิ์ 9 ความสามารถ

เชิงทดลอง0%

Alpha67%

Beta79%

[Raspberry Pi](</th/install/raspberry-pi>), [การตรวจสอบสิทธิ์](</th/gateway/authentication>), [ความลับ](</th/gateway/secrets>), [การจับคู่](</th/gateway/pairing>), [อุปกรณ์](</th/cli/devices>), [ระยะไกล](</th/gateway/remote>), [Tailscale](</th/gateway/tailscale>)

รันไทม์ของ Gateway 10 ความสามารถ

เชิงทดลอง0%

Alpha67%

Beta79%

[ดัชนี](</th/gateway>), [Gateway](</th/cli/gateway>), [Raspberry Pi](</th/install/raspberry-pi>), [Linux](</th/platforms/linux>), [Vps](</th/vps>)

ประสิทธิภาพและการวินิจฉัย 5 ความสามารถ

เชิงทดลอง0%

Alpha67%

Beta79%

[Raspberry Pi](</th/install/raspberry-pi>), [Linux](</th/platforms/linux>), [สถานภาพ](</th/gateway/health>), [การวินิจฉัย](</th/gateway/diagnostics>)

แอปคู่หู macOS - M3 Beta - 8 พื้นที่

มีแอปแถบเมนูที่มีฟีเจอร์ครบถ้วน สิทธิ์ โหมด Node, Canvas, การปลุกด้วยเสียง, WebChat และโหมดระยะไกลแล้ว ยังเปลี่ยนแปลงเร็วพอที่จะหลีกเลี่ยงระดับ Stable

ความครอบคลุม เชิงทดลอง - 0%คุณภาพ Alpha - 66%ความสมบูรณ์ Beta - 78%ไม่มี

แคนวาส 4 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[แคนวาส](</th/platforms/mac/canvas>), [Macos](</th/platforms/macos>), [เว็บแชต](</th/web/webchat>)

การตั้งค่าภายในเครื่อง 7 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[Gateway ที่มาพร้อมชุด](</th/platforms/mac/bundled-gateway>), [Macos](</th/platforms/macos>), [โปรเซสลูก](</th/platforms/mac/child-process>), [การตั้งค่าสำหรับการพัฒนา](</th/platforms/mac/dev-setup>)

สถานะและการตั้งค่า 5 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[แถบเมนู](</th/platforms/mac/menu-bar>), [ไอคอน](</th/platforms/mac/icon>), [Macos](</th/platforms/macos>), [สุขภาพระบบ](</th/platforms/mac/health>), [การบันทึกล็อก](</th/platforms/mac/logging>), [ระยะไกล](</th/platforms/mac/remote>)

ความสามารถแบบเนทีฟ 5 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[Macos](</th/platforms/macos>), [Xpc](</th/platforms/mac/xpc>), [สิทธิ์อนุญาต](</th/platforms/mac/permissions>), [การลงนาม](</th/platforms/mac/signing>), [Peekaboo](</th/platforms/mac/peekaboo>)

การเชื่อมต่อระยะไกล 3 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[ระยะไกล](</th/platforms/mac/remote>), [Macos](</th/platforms/macos>), [ระยะไกล](</th/gateway/remote>)

เสียงและการสนทนา 3 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[Voicewake](</th/platforms/mac/voicewake>), [โอเวอร์เลย์เสียง](</th/platforms/mac/voice-overlay>), [การสนทนา](</th/nodes/talk>), [Macos](</th/platforms/macos>)

เว็บแชต 3 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[เว็บแชต](</th/platforms/mac/webchat>), [Macos](</th/platforms/macos>), [เว็บแชต](</th/web/webchat>)

เว็บแชตระยะไกล 5 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[เว็บแชต](</th/platforms/mac/webchat>), [ระยะไกล](</th/gateway/remote>), [ระยะไกล](</th/platforms/mac/remote>)

แอป Android - M2 อัลฟา - 7 ด้าน

มีช่องทาง Google Play สาธารณะแล้ว แต่เอกสารของแอปยังคงอธิบายการสร้างใหม่ว่าเป็นอัลฟามาก และระบุงานเพิ่มความแข็งแกร่งสำหรับการเผยแพร่

ความครอบคลุม ระยะทดลอง - 0%คุณภาพ อัลฟา - 59%ความสมบูรณ์ อัลฟา - 66%ไม่มี

การจับภาพสื่อ 1 ความสามารถ

ทดลอง0%

Alpha59%

Alpha66%

[Android](</th/platforms/android>), [กล้อง](</th/nodes/camera>)

แชตบนมือถือ 1 ความสามารถ

ทดลอง0%

Alpha59%

Alpha66%

[Android](</th/platforms/android>)

การตั้งค่าการเชื่อมต่อ 1 ความสามารถ

ทดลอง0%

Alpha59%

Alpha66%

[Android](</th/platforms/android>), [Bonjour](</th/gateway/bonjour>), [การจับคู่](</th/gateway/pairing>)

การเผยแพร่ 3 ความสามารถ

ทดลอง0%

Alpha59%

Alpha66%

[Android](</th/platforms/android>)

การตั้งค่า 1 ความสามารถ

ทดลอง0%

Alpha59%

Alpha66%

[Android](</th/platforms/android>)

เสียง 1 ความสามารถ

ทดลอง0%

Alpha59%

Alpha66%

[Android](</th/platforms/android>), [พูดคุย](</th/nodes/talk>)

รันไทม์ของอุปกรณ์ 2 ความสามารถ

ทดลอง0%

Alpha59%

Alpha66%

[Android](</th/platforms/android>), [การแก้ไขปัญหา](</th/nodes/troubleshooting>), [โปรโตคอล](</th/gateway/protocol>)

Windows แบบเนทีฟ - M2 Alpha - 4 พื้นที่

โฟลว์ CLI/Gateway หลักใช้งานได้ แต่เอกสารยังคงแนะนำ WSL2 สำหรับประสบการณ์เต็มรูปแบบและระบุข้อควรระวังของแบบเนทีฟไว้

ความครอบคลุม ทดลอง - 0%คุณภาพ Alpha - 58%ความสมบูรณ์ Alpha - 66%บางส่วน - 1

CLI 9 ความสามารถ / รองรับ LTS

ทดลอง0%

อัลฟา54%

อัลฟา64%

[ดัชนี](</th/install>), [ตัวติดตั้ง](</th/install/installer>), [Windows](</th/platforms/windows>), [เริ่มต้นใช้งาน](</th/start/getting-started>), [การเริ่มใช้งาน](</th/cli/onboard>)

การจัดการ Gateway 11 ความสามารถ

ทดลอง0%

อัลฟา59%

อัลฟา66%

[Windows](</th/platforms/windows>), [ดัชนี](</th/gateway>), [Gateway](</th/cli/gateway>), [การตรวจวินิจฉัย](</th/cli/doctor>)

เครือข่าย 4 ความสามารถ

ทดลอง0%

อัลฟา59%

อัลฟา66%

[Windows](</th/platforms/windows>), [ดัชนี](</th/gateway>), [Gateway](</th/cli/gateway>)

การอัปเดต 4 ความสามารถ

ทดลอง0%

อัลฟา59%

อัลฟา66%

[การอัปเดต](</th/install/updating>), [CI](</th/ci>)

การโฮสต์ Kubernetes - M2 อัลฟา - 4 พื้นที่

การโฮสต์ Kubernetes เป็นเส้นทางการปรับใช้คลัสเตอร์ที่อิงตาม Kustomize โดยเฉพาะ คะแนนปัจจุบันแสดงให้เห็นเส้นทางการปรับใช้ขั้นต่ำที่ใช้งานได้จริง โดยยังมีช่องว่างเกี่ยวกับ CI เฉพาะสำหรับ Kubernetes, การจัดแพ็กเกจ ingress/TLS/NetworkPolicy, การสำรอง/กู้คืน และการเสริมความแข็งแกร่งของการเปิดใช้งานในสภาพแวดล้อมการผลิต

ความครอบคลุม Experimental - 0%คุณภาพ Alpha - 55%ความสมบูรณ์ Alpha - 61%ไม่มี

การตั้งค่าการปรับใช้ 5 ความสามารถ

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</th/install/kubernetes>), [ดัชนี](</th/install>)

การกำหนดค่าและความลับ 5 ความสามารถ

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</th/install/kubernetes>), [ความลับ](</th/gateway/secrets>), [สภาพแวดล้อม](</th/help/environment>)

การเข้าถึงและการเปิดเผย 5 ความสามารถ

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</th/install/kubernetes>), [การยืนยันตัวตน](</th/gateway/authentication>), [ระยะไกล](</th/gateway/remote>), [คู่มือการดำเนินงานการเปิดเผย](</th/gateway/security/exposure-runbook>)

วงจรชีวิตของคลัสเตอร์ 5 ความสามารถ

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</th/install/kubernetes>), [ดัชนี](</th/gateway>)

แอป iOS - M1 Experimental - 8 พื้นที่

ตัวอย่างภายใน / ระดับซูเปอร์อัลฟา มี TestFlight และโฟลว์พุชที่มีรีเลย์รองรับแล้ว แต่ยังไม่มีการเผยแพร่สาธารณะ

ความครอบคลุม ทดลอง - 0%คุณภาพ ทดลอง - 41%ความครบถ้วน ทดลอง - 44%ไม่มี

สื่อและการแชร์ 1 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[Ios](</th/platforms/ios>), [กล้อง](</th/nodes/camera>)

แคนวาสและหน้าจอ 1 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[Ios](</th/platforms/ios>), [แคนวาส](</th/plugins/reference/canvas>)

แชตและเซสชัน 1 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[Ios](</th/platforms/ios>), [เว็บแชต](</th/web/webchat>), [โปรโตคอล](</th/gateway/protocol>)

การตั้งค่าและการวินิจฉัย Gateway 7 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[Ios](</th/platforms/ios>), [การจับคู่](</th/channels/pairing>)

การจัดจำหน่าย 1 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[Ios](</th/platforms/ios>)

คำสั่งอุปกรณ์ 2 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[Ios](</th/platforms/ios>), [โปรโตคอล](</th/gateway/protocol>)

การแจ้งเตือนและเบื้องหลัง 1 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[Ios](</th/platforms/ios>), [การกำหนดค่า](</th/gateway/configuration>)

เสียง 1 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[Ios](</th/platforms/ios>), [พูดคุย](</th/nodes/talk>)

Nix install path - M1 Experimental - 5 areas

ขั้นตอนการติดตั้งแบบไม่บังคับ ต้องมีคำมั่นเรื่องการรองรับที่ชัดเจนขึ้นก่อนเลื่อนสถานะเป็นอัลฟา/เบตา

ความครอบคลุม ระดับทดลอง - 0%คุณภาพ ระดับทดลอง - 41%ความครบถ้วน ระดับทดลอง - 44%ไม่มี

การส่งต่อการติดตั้ง 4 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[Nix](</th/install/nix>), [ดัชนี](</th/install>), [ไดเรกทอรีเอกสาร](</th/start/docs-directory>)

วงจรชีวิต Plugin 4 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[จัดการ Plugins](</th/plugins/manage-plugins>), [Plugin](</th/tools/plugin>), [Nix](</th/install/nix>)

การเปิดใช้งานและ UX ของแอป 7 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[Nix](</th/install/nix>)

การกำหนดค่าและสถานะ 7 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[Nix](</th/install/nix>), [ตั้งค่า](</th/cli/setup>), [สภาพแวดล้อม](</th/help/environment>)

รันไทม์บริการและการป้องกัน 8 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[Nix](</th/install/nix>), [ตั้งค่า](</th/cli/setup>), [Doctor](</th/cli/doctor>), [อัปเดต](</th/cli/update>)

พื้นผิวเสริม watchOS - M1 ทดลอง - 5 พื้นที่

ซอร์สมีพื้นผิวของแอป/ส่วนขยาย Watch; เอกสารสาธารณะยังไม่ได้นำเสนอสิ่งนี้เป็นฟีเจอร์สำหรับผู้ใช้

ความครอบคลุม ทดลอง - 0%คุณภาพ ทดลอง - 41%ความสมบูรณ์ ทดลอง - 44%ไม่มี

การส่งมอบและการกู้คืน 7 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[Ios](</th/platforms/ios>)

การอนุมัติการดำเนินการ 3 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[การอนุมัติการดำเนินการ](</th/tools/exec-approvals>), [Ios](</th/platforms/ios>)

การเผยแพร่และการสนับสนุน 6 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[Ios](</th/platforms/ios>)

การแจ้งเตือนและการตอบกลับ 7 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[Ios](</th/platforms/ios>)

UI แอปนาฬิกา 3 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[Ios](</th/platforms/ios>)

แอปคู่ขนาน Linux - M0 วางแผนแล้ว - 5 พื้นที่

เอกสารระบุว่าแอปคู่ขนาน Linux แบบเนทีฟอยู่ในแผน; Gateway เป็นเส้นทาง Linux ที่รองรับในปัจจุบัน

ความครอบคลุม ทดลอง - 0%คุณภาพ ทดลอง - 19%ความสมบูรณ์ ทดลอง - 21%ไม่มี

การแจกจ่ายแอป 3 ความสามารถ

ทดลอง0%

ทดลอง19%

ทดลอง21%

[Linux](</th/platforms/linux>), [ดัชนี](</th/platforms>), [ดัชนี](</th/install>)

การเชื่อมต่อ Gateway 4 ความสามารถ

ทดลอง0%

ทดลอง19%

ทดลอง21%

[Linux](</th/platforms/linux>), [ดัชนี](</th/gateway>), [การจับคู่](</th/gateway/pairing>), [ระยะไกล](</th/gateway/remote>)

แชตและเซสชัน 3 ความสามารถ

ทดลอง0%

ทดลอง19%

ทดลอง21%

[Linux](</th/platforms/linux>), [โปรโตคอล](</th/gateway/protocol>), [เว็บแชต](</th/web/webchat>)

ความสามารถบนเดสก์ท็อป 9 ความสามารถ

ทดลอง0%

ทดลอง19%

ทดลอง21%

[Linux](</th/platforms/linux>), [การอนุมัติ Exec](</th/tools/exec-approvals>), [ความลับ](</th/gateway/secrets>), [ดัชนี](</th/nodes>), [Exec](</th/tools/exec>), [พูดคุย](</th/nodes/talk>), [กล้อง](</th/nodes/camera>)

สถานะและการวินิจฉัย 7 ความสามารถ

ทดลอง0%

ทดลอง19%

ทดลอง21%

[Linux](</th/platforms/linux>), [OpenClaw](</th/start/openclaw>), [Doctor](</th/gateway/doctor>)

แอปคู่หู Windows แบบเนทีฟ - M0 วางแผนไว้ - 5 ด้าน

วางแผนไว้เท่านั้น

ความครอบคลุม ทดลอง - 0%คุณภาพ ทดลอง - 19%ความครบถ้วน ทดลอง - 21%ไม่มี

การติดตั้งและการอัปเดต 4 ความสามารถ

ทดลอง0%

ทดลอง19%

ทดลอง21%

[Windows](</th/platforms/windows>), [ดัชนี](</th/install>)

การเชื่อมต่อ Gateway 3 ความสามารถ

ทดลอง0%

ทดลอง19%

ทดลอง21%

[Windows](</th/platforms/windows>), [ดัชนี](</th/gateway>), [การจับคู่](</th/gateway/pairing>), [ระยะไกล](</th/gateway/remote>)

เซสชันแชท 2 ความสามารถ

ทดลอง0%

ทดลอง19%

ทดลอง21%

[Windows](</th/platforms/windows>), [โปรโตคอล](</th/gateway/protocol>)

สถานะและการซ่อมแซม 5 ความสามารถ

ทดลอง0%

ทดลอง19%

ทดลอง21%

[Windows](</th/platforms/windows>), [Doctor](</th/gateway/doctor>), [ดัชนี](</th/gateway>)

เครื่องมือเดสก์ท็อปและสิทธิ์อนุญาต 10 ความสามารถ

ทดลอง0%

ทดลอง19%

ทดลอง21%

[Windows](</th/platforms/windows>), [ดัชนี](</th/nodes>), [Exec](</th/tools/exec>), [การอนุมัติ Exec](</th/tools/exec-approvals>), [ดัชนี](</th/gateway/security>)

### ช่องทาง

Discord - M4 เสถียร - 6 พื้นที่

เอกสารเชิงลึกและความครอบคลุมของฟีเจอร์อย่างกว้างขวาง ควรให้คะแนนเส้นทางเสียง/การมอบหมายแยกต่างหากเป็นเบต้า/อัลฟ่า

ความครอบคลุม ทดลอง - 0%คุณภาพ เบต้า - 73%ความสมบูรณ์ เสถียร - 87%บางส่วน - 4

การตั้งค่าและการดำเนินงานช่องทาง 10 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า73%

เสถียร87%

[Discord](</th/channels/discord>), [Discord](</th/plugins/reference/discord>), [Fly](</th/install/fly>), [คำสั่ง Slash](</th/tools/slash-commands>), [สถานะระบบ](</th/gateway/health>), [ช่องทาง](</th/cli/channels>), [ช่องทางการกำหนดค่า](</th/gateway/config-channels>)

การเข้าถึงและอัตลักษณ์ 6 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า73%

เสถียร87%

[Discord](</th/channels/discord>), [การจับคู่](</th/channels/pairing>), [กลุ่มการเข้าถึง](</th/channels/access-groups>), [กลุ่ม](</th/channels/groups>)

การกำหนดเส้นทางและการส่งมอบบทสนทนา 12 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า73%

เสถียร87%

[Discord](</th/channels/discord>), [การกำหนดเส้นทางช่องทาง](</th/channels/channel-routing>), [กลุ่ม](</th/channels/groups>), [กลุ่มการเข้าถึง](</th/channels/access-groups>), [ตัวแทน ACP](</th/tools/acp-agents>), [ตัวแทนย่อย](</th/tools/subagents>)

สื่อและเนื้อหาแบบสมบูรณ์ 1 ความสามารถ / รองรับ LTS

ทดลอง0%

เบต้า73%

เสถียร87%

[Discord](</th/channels/discord>)

การควบคุมแบบเนทีฟและการอนุมัติ 5 ความสามารถ

ทดลอง0%

เบต้า73%

เสถียร87%

[Discord](</th/channels/discord>), [คำสั่ง Slash](</th/tools/slash-commands>)

เสียงและการโทรแบบเรียลไทม์ 5 ความสามารถ

ทดลอง0%

เบต้า73%

เสถียร87%

[Discord](</th/channels/discord>), [Openai](</th/providers/openai>), [Elevenlabs](</th/providers/elevenlabs>), [ระบบอัตโนมัติ QA E2E](</th/concepts/qa-e2e-automation>), [ช่องทางการกำหนดค่า](</th/gateway/config-channels>)

Telegram - M3 เบต้า - 5 พื้นที่

ช่องทางหลักมีความสมบูรณ์เพียงพอสำหรับการใช้งานเป็นประจำ แต่ UX ที่แปรปรวนสูงและกรณีขอบของสื่อยังต้องมีหลักฐานจากสถานการณ์ทดสอบซ้ำเป็นระยะ

ความครอบคลุม ทดลอง - 0%คุณภาพ อัลฟา - 68%ความสมบูรณ์ เบต้า - 78%เต็มรูปแบบ - 5

การตั้งค่าและการดำเนินงานของช่องทาง 10 ความสามารถ / รองรับ LTS

ทดลอง0%

Alpha66%

Beta78%

[Telegram](</th/channels/telegram>), [ช่องทางการกำหนดค่า](</th/gateway/config-channels>), [ช่องทาง](</th/cli/channels>)

การเข้าถึงและตัวตน 10 ความสามารถ / รองรับ LTS

ทดลอง0%

Alpha66%

Beta78%

[Telegram](</th/channels/telegram>), [การจับคู่](</th/channels/pairing>), [กลุ่มการเข้าถึง](</th/channels/access-groups>), [กลุ่ม](</th/channels/groups>), [หลาย Agent](</th/concepts/multi-agent>)

การกำหนดเส้นทางและการส่งมอบการสนทนา 1 ความสามารถ / รองรับ LTS

ทดลอง0%

Alpha66%

Beta78%

[Telegram](</th/channels/telegram>), [กลุ่ม](</th/channels/groups>), [หลาย Agent](</th/concepts/multi-agent>)

สื่อและเนื้อหาแบบ Rich 1 ความสามารถ / รองรับ LTS

ทดลอง0%

Alpha66%

Beta78%

[Telegram](</th/channels/telegram>), [ตำแหน่งที่ตั้ง](</th/channels/location>)

การควบคุมและการอนุมัติแบบเนทีฟ 9 ความสามารถ / รองรับ LTS

ทดลอง0%

Beta77%

Beta79%

[Telegram](</th/channels/telegram>), [การอนุมัติ Exec](</th/tools/exec-approvals>), [รีแอ็กชัน](</th/tools/reactions>)

Slack - M3 Beta - 5 ด้าน

เอกสารช่องทางและพื้นผิวการกำหนดเส้นทางระดับเฟิร์สคลาส ต้องมี scorecard สำหรับสถานการณ์การติดตั้ง/ผู้ดูแลระบบของพื้นที่ทำงาน

ความครอบคลุม ทดลอง - 0%คุณภาพ Alpha - 66%ความสมบูรณ์ Beta - 78%เต็ม - 5

การตั้งค่าและการดำเนินงานของช่องทาง 10 ความสามารถ / รองรับแบบ LTS

ทดลอง0%

Alpha66%

Beta78%

[Slack](</th/channels/slack>), [Slack](</th/plugins/reference/slack>), [ข้อมูลลับ](</th/gateway/secrets>), [การทำงานอัตโนมัติ QA E2E](</th/concepts/qa-e2e-automation>), [การแก้ไขปัญหา](</th/channels/troubleshooting>)

การเข้าถึงและตัวตน 1 ความสามารถ / รองรับแบบ LTS

ทดลอง0%

Alpha66%

Beta78%

[Slack](</th/channels/slack>), [การจับคู่](</th/channels/pairing>)

การกำหนดเส้นทางและการส่งมอบการสนทนา 5 ความสามารถ / รองรับแบบ LTS

ทดลอง0%

Alpha66%

Beta78%

[Slack](</th/channels/slack>), [การป้องกันลูปของบอต](</th/channels/bot-loop-protection>), [การจับคู่](</th/channels/pairing>)

สื่อและเนื้อหาแบบสมบูรณ์ 1 ความสามารถ / รองรับแบบ LTS

ทดลอง0%

Alpha66%

Beta78%

[Slack](</th/channels/slack>), [การทำงานอัตโนมัติ QA E2E](</th/concepts/qa-e2e-automation>)

การควบคุมและการอนุมัติแบบเนทีฟ 8 ความสามารถ / รองรับแบบ LTS

ทดลอง0%

Alpha66%

Beta78%

[Slack](</th/channels/slack>), [คำสั่ง Slash](</th/tools/slash-commands>), [การอนุมัติ Exec](</th/tools/exec-approvals>)

iMessage และ BlueBubbles - M3 Beta - 5 พื้นที่

iMessage ที่รองรับทำงานผ่าน imsg บนโฮสต์ macOS Messages ที่ลงชื่อเข้าใช้แล้ว; การกำหนดค่า BlueBubbles แบบเดิมต้องมีการย้ายข้อมูล คงคำเตือนเรื่องสิทธิ์ macOS, SSH wrapper, SIP/private API และการย้ายข้อมูลให้เห็นชัดเจน

ความครอบคลุม ทดลอง - 0%คุณภาพ Alpha - 66%ความครบถ้วน Beta - 78%ไม่มี

การตั้งค่าและการดำเนินงานของช่องทาง 11 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[Bluebubbles iMessage](</th/announcements/bluebubbles-imessage>), [iMessage จาก Bluebubbles](</th/channels/imessage-from-bluebubbles>), [กำหนดค่าช่องทาง](</th/gateway/config-channels>), [iMessage](</th/channels/imessage>)

การเข้าถึงและตัวตน 6 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[iMessage](</th/channels/imessage>), [iMessage จาก Bluebubbles](</th/channels/imessage-from-bluebubbles>), [กำหนดค่าช่องทาง](</th/gateway/config-channels>)

การกำหนดเส้นทางและการส่งมอบบทสนทนา 4 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[iMessage](</th/channels/imessage>)

สื่อและเนื้อหาแบบสมบูรณ์ 7 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[iMessage](</th/channels/imessage>), [iMessage จาก Bluebubbles](</th/channels/imessage-from-bluebubbles>), [กำหนดค่าช่องทาง](</th/gateway/config-channels>)

การควบคุมและการอนุมัติแบบเนทีฟ 3 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[iMessage](</th/channels/imessage>)

WhatsApp - M3 Beta - 5 areas

เส้นทางหลักมีความสำคัญและมีเอกสารประกอบ; ความผันผวนของ Baileys/session ต้นทางทำให้ยังอยู่ต่ำกว่าระดับเสถียร

ความครอบคลุม ทดลอง - 0%คุณภาพ อัลฟา - 66%ความครบถ้วน เบตา - 78%ไม่มี

การตั้งค่าและการดำเนินงานช่องทาง 5 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[WhatsApp](</th/channels/whatsapp>), [การกำหนดค่าช่องทาง](</th/gateway/config-channels>), [WhatsApp](</th/plugins/reference/whatsapp>), [ระบบอัตโนมัติ QA E2E](</th/concepts/qa-e2e-automation>), [เครื่องมือตรวจสอบ](</th/gateway/doctor>)

การเข้าถึงและตัวตน 7 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[WhatsApp](</th/channels/whatsapp>), [การกำหนดค่าช่องทาง](</th/gateway/config-channels>), [ระบบอัตโนมัติ QA E2E](</th/concepts/qa-e2e-automation>), [การจับคู่](</th/channels/pairing>)

การกำหนดเส้นทางและการส่งบทสนทนา 4 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[WhatsApp](</th/channels/whatsapp>), [ข้อความกลุ่ม](</th/channels/group-messages>)

สื่อและเนื้อหาแบบสมบูรณ์ 2 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[WhatsApp](</th/channels/whatsapp>)

การควบคุมและการอนุมัติแบบเนทีฟ 2 ความสามารถ

ทดลอง0%

อัลฟา66%

เบตา78%

[WhatsApp](</th/channels/whatsapp>)

Matrix - M2 อัลฟา - 6 ด้าน

รองรับผ่าน Plugin ที่รวมมาให้ ต้องมีดัชนีชี้วัดสำหรับบริดจ์ การยืนยันตัวตน และวงจรชีวิตของห้อง

ความครอบคลุม ทดลอง - 0%คุณภาพ อัลฟา - 60%ความสมบูรณ์ อัลฟา - 67%ไม่มี

การตั้งค่าและการดำเนินงานของช่องทาง 5 ความสามารถ

ทดลอง0%

อัลฟา60%

อัลฟา67%

[Matrix](</th/channels/matrix>), [การย้ายไปใช้ Matrix](</th/channels/matrix-migration>)

การเข้าถึงและตัวตน 7 ความสามารถ

ทดลอง0%

อัลฟา60%

อัลฟา67%

[Matrix](</th/channels/matrix>), [กลุ่ม](</th/channels/groups>), [การป้องกันลูปของบอต](</th/channels/bot-loop-protection>)

การกำหนดเส้นทางและการส่งมอบการสนทนา 1 ความสามารถ

ทดลอง0%

อัลฟา60%

อัลฟา67%

[Matrix](</th/channels/matrix>)

สื่อและเนื้อหาแบบริช 1 ความสามารถ

ทดลอง0%

อัลฟา60%

อัลฟา67%

[Matrix](</th/channels/matrix>)

การควบคุมและการอนุมัติแบบเนทีฟ 6 ความสามารถ

ทดลอง0%

อัลฟา60%

อัลฟา67%

[Matrix](</th/channels/matrix>)

การเข้ารหัสและการยืนยัน 3 ความสามารถ

ทดลอง0%

อัลฟา60%

อัลฟา67%

[Matrix](</th/channels/matrix>), [การย้ายไปใช้ Matrix](</th/channels/matrix-migration>)

Google Chat - M2 Alpha - 5 areas

ช่องทางที่มีเอกสารกำกับแล้ว แต่การตั้งค่าระดับองค์กร/ผู้ดูแลระบบเพิ่มความเสี่ยงด้านความสมบูรณ์

ความครอบคลุม ทดลอง - 0%คุณภาพ อัลฟา - 59%ความครบถ้วน อัลฟา - 66%ไม่มี

การตั้งค่าและการดำเนินงานช่องทาง 16 ความสามารถ

ทดลอง0%

Alpha59%

Alpha66%

[Googlechat](</th/channels/googlechat>), [Googlechat](</th/plugins/reference/googlechat>), [ช่องทางการกำหนดค่า](</th/gateway/config-channels>), [ข้อมูลอ้างอิง CLI ของวิซาร์ด](</th/start/wizard-cli-reference>), [ข้อมูลลับ](</th/gateway/secrets>), [พื้นผิวข้อมูลประจำตัว Secretref](</th/reference/secretref-credential-surface>), [สุขภาพ](</th/gateway/health>), [รายการ Plugin](</th/plugins/plugin-inventory>), [ดัชนี](</th/channels>)

การเข้าถึงและตัวตน 11 ความสามารถ

ทดลอง0%

Alpha59%

Alpha66%

[Googlechat](</th/channels/googlechat>), [การจับคู่](</th/channels/pairing>), [กลุ่มการเข้าถึง](</th/channels/access-groups>), [ช่องทางการกำหนดค่า](</th/gateway/config-channels>), [การป้องกันลูปบอต](</th/channels/bot-loop-protection>), [การกำหนดเส้นทางช่องทาง](</th/channels/channel-routing>)

การกำหนดเส้นทางและการส่งมอบการสนทนา 1 ความสามารถ

ทดลอง0%

Alpha59%

Alpha66%

[Googlechat](</th/channels/googlechat>), [การป้องกันลูปบอต](</th/channels/bot-loop-protection>), [กลุ่มการเข้าถึง](</th/channels/access-groups>), [การกำหนดเส้นทางช่องทาง](</th/channels/channel-routing>)

สื่อและเนื้อหารูปแบบสมบูรณ์ 1 ความสามารถ

ทดลอง0%

Alpha59%

Alpha66%

[Googlechat](</th/channels/googlechat>), [ข้อความ](</th/cli/message>), [ความเข้าใจสื่อ](</th/nodes/media-understanding>), [พื้นผิวข้อมูลประจำตัว Secretref](</th/reference/secretref-credential-surface>)

การควบคุมและการอนุมัติแบบเนทีฟ 16 ความสามารถ

ทดลอง0%

Alpha59%

Alpha66%

[Googlechat](</th/channels/googlechat>), [ข้อความ](</th/cli/message>), [ความเข้าใจสื่อ](</th/nodes/media-understanding>), [พื้นผิวข้อมูลประจำตัว Secretref](</th/reference/secretref-credential-surface>), [ปฏิกิริยา](</th/tools/reactions>), [คำสั่ง Slash](</th/tools/slash-commands>), [การกำหนดค่าตัวแทน](</th/gateway/config-agents>), [การปรับโครงสร้างวงจรชีวิตข้อความ](</th/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alpha - 5 พื้นที่

โฟลว์การยืนยันตัวตน/ผู้ดูแลระบบระดับองค์กรต้องมีหลักฐานสถานการณ์ที่ชัดเจน

ความครอบคลุม ทดลอง - 0%คุณภาพ Alpha - 59%ความสมบูรณ์ Alpha - 66%ไม่มี

การตั้งค่าและการดำเนินงานของช่องทาง 9 ความสามารถ

ทดลอง0%

อัลฟา59%

อัลฟา66%

[Msteams](</th/channels/msteams>), [Msteams](</th/plugins/reference/msteams>), [การกำหนดค่าช่องทาง](</th/gateway/config-channels>), [สถานภาพ](</th/gateway/health>)

การเข้าถึงและตัวตน 9 ความสามารถ

ทดลอง0%

อัลฟา59%

อัลฟา66%

[Msteams](</th/channels/msteams>), [การจับคู่](</th/channels/pairing>), [กลุ่มการเข้าถึง](</th/channels/access-groups>)

การกำหนดเส้นทางและการส่งมอบการสนทนา 5 ความสามารถ

ทดลอง0%

อัลฟา59%

อัลฟา66%

[Msteams](</th/channels/msteams>), [กลุ่ม](</th/channels/groups>), [การกำหนดเส้นทางช่องทาง](</th/channels/channel-routing>)

สื่อและเนื้อหาแบบสมบูรณ์ 5 ความสามารถ

ทดลอง0%

อัลฟา59%

อัลฟา66%

[Msteams](</th/channels/msteams>)

การควบคุมและการอนุมัติแบบเนทีฟ 5 ความสามารถ

ทดลอง0%

อัลฟา59%

อัลฟา66%

[Msteams](</th/channels/msteams>), [การอนุมัติ Exec ขั้นสูง](</th/tools/exec-approvals-advanced>)

Signal - M2 อัลฟา - 5 ด้าน

มีเอกสารช่องทางที่รองรับแล้ว แต่ยังต้องมีหลักฐานการติดตั้งและการเชื่อมต่อใหม่ที่แข็งแรงขึ้น

ความครอบคลุม ทดลอง - 0%คุณภาพ อัลฟา - 59%ความสมบูรณ์ อัลฟา - 66%ไม่มี

การตั้งค่าและการดำเนินงานของช่องทาง 7 ความสามารถ

เชิงทดลอง0%

อัลฟา59%

อัลฟา66%

[Signal](</th/channels/signal>), [Signal](</th/plugins/reference/signal>)

การเข้าถึงและตัวตน 6 ความสามารถ

เชิงทดลอง0%

อัลฟา59%

อัลฟา66%

[Signal](</th/channels/signal>)

การกำหนดเส้นทางและการส่งบทสนทนา 1 ความสามารถ

เชิงทดลอง0%

อัลฟา59%

อัลฟา66%

[Signal](</th/channels/signal>)

สื่อและเนื้อหาสมบูรณ์ 7 ความสามารถ

เชิงทดลอง0%

อัลฟา59%

อัลฟา66%

[Signal](</th/channels/signal>)

การควบคุมและการอนุมัติแบบเนทีฟ 3 ความสามารถ

เชิงทดลอง0%

อัลฟา59%

อัลฟา66%

[Signal](</th/channels/signal>)

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, ช่องทางภูมิภาค - M2 อัลฟา - 4 ด้าน

ความครอบคลุมระดับภูมิภาคที่สำคัญ แต่ควรปรับเทียบระดับการรองรับสาธารณะตามประเภทบัญชี การอนุมัติจาก upstream และหลักฐานจากผู้ดูแล

ความครอบคลุม เชิงทดลอง - 0%คุณภาพ อัลฟา - 55%ความครบถ้วน อัลฟา - 58%ไม่มี

การตั้งค่าและการดำเนินงานของช่องทาง 6 ความสามารถ

ทดลอง0%

อัลฟา61%

อัลฟา68%

[ดัชนี](</th/channels>), [การจับคู่](</th/channels/pairing>), [Feishu](</th/plugins/reference/feishu>), [สถาปัตยกรรมภายใน](</th/plugins/architecture-internals>)

การเข้าถึงและตัวตน 1 ความสามารถ

ทดลอง0%

อัลฟา53%

อัลฟา54%

ไม่มีเอกสารที่ลิงก์ไว้

การกำหนดเส้นทางและการส่งบทสนทนา 1 ความสามารถ

ทดลอง0%

อัลฟา53%

อัลฟา54%

ไม่มีเอกสารที่ลิงก์ไว้

สื่อและเนื้อหาสมบูรณ์ 1 ความสามารถ

ทดลอง0%

อัลฟา53%

อัลฟา54%

ไม่มีเอกสารที่ลิงก์ไว้

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 อัลฟา - 4 พื้นที่

มีพื้นผิวการทำงานที่รองรับอยู่ แต่ระดับความพร้อมใช้งานอาจแตกต่างกันไปตาม upstream และความครอบคลุมของผู้ดูแล ให้คะแนนแยกรายการในภายหลัง

ความครอบคลุม ทดลอง - 0%คุณภาพ อัลฟา - 53%ความสมบูรณ์ อัลฟา - 54%ไม่มี

การตั้งค่าและการดำเนินงานของช่องทาง 1 ความสามารถ

ทดลอง0%

Alpha53%

Alpha54%

ไม่มีเอกสารที่ลิงก์ไว้

การเข้าถึงและข้อมูลประจำตัว 1 ความสามารถ

ทดลอง0%

Alpha53%

Alpha54%

ไม่มีเอกสารที่ลิงก์ไว้

การกำหนดเส้นทางและการส่งมอบบทสนทนา 1 ความสามารถ

ทดลอง0%

Alpha53%

Alpha54%

ไม่มีเอกสารที่ลิงก์ไว้

สื่อและเนื้อหาแบบสมบูรณ์ 1 ความสามารถ

ทดลอง0%

Alpha53%

Alpha54%

ไม่มีเอกสารที่ลิงก์ไว้

ช่องทางการโทรด้วยเสียง - M1 ทดลอง - 5 พื้นที่

เส้นทางทางเลือก/Plugin พร้อมพฤติกรรมแบบเรียลไทม์ที่ซับซ้อน ต้องมีดัชนีชี้วัดสถานการณ์ก่อนเบต้าสาธารณะ

ความครอบคลุม ทดลอง - 0%คุณภาพ ทดลอง - 41%ความครบถ้วน ทดลอง - 44%ไม่มี

การตั้งค่าและการดำเนินงานของช่องทาง 2 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[Voicecall](</th/cli/voicecall>), [การโทรด้วยเสียง](</th/plugins/voice-call>), [Protocol](</th/gateway/protocol>)

การเข้าถึงและข้อมูลประจำตัว 1 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[การโทรด้วยเสียง](</th/plugins/voice-call>), [Voicecall](</th/cli/voicecall>)

การกำหนดเส้นทางและการส่งมอบการสนทนา 1 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[การโทรด้วยเสียง](</th/plugins/voice-call>)

สื่อและเนื้อหาสมบูรณ์ 2 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[การโทรด้วยเสียง](</th/plugins/voice-call>), [คลังรายการ Plugin](</th/plugins/plugin-inventory>)

เสียงและการโทรแบบเรียลไทม์ 2 ความสามารถ

ทดลอง0%

ทดลอง41%

ทดลอง44%

[การโทรด้วยเสียง](</th/plugins/voice-call>)

### ผู้ให้บริการและเครื่องมือ

ระบบอัตโนมัติของเบราว์เซอร์, exec และเครื่องมือ sandbox - M3 เบต้า - 3 พื้นที่

เครื่องมือหลักมีการจัดทำเอกสารไว้แล้ว แต่ความปลอดภัยของโฮสต์และ UX สิทธิ์ควรอยู่ภายใต้การทบทวน scorecard อย่างต่อเนื่อง

ความครอบคลุม ทดลอง - 21%คุณภาพ เบต้า - 75%ความสมบูรณ์ เบต้า - 79%บางส่วน - 2

การทำงานอัตโนมัติของเบราว์เซอร์ 8 ความสามารถ

Experimental13%

Beta79%

Beta79%

[การควบคุมเบราว์เซอร์](</th/tools/browser-control>), [การทดสอบ](</th/help/testing>), [เบราว์เซอร์](</th/tools/browser>), [ดัชนี](</th/gateway/security>), [การตรวจสอบ Audit](</th/gateway/security/audit-checks>)

การเรียกใช้และการดำเนินการของเครื่องมือ 6 ความสามารถ / รองรับ LTS

Alpha50%

Beta79%

Beta79%

[Exec](</th/tools/exec>), [กระบวนการเบื้องหลัง](</th/gateway/background-process>), [Tools Invoke Http Api](</th/gateway/tools-invoke-http-api>), [ขอบเขตผู้ควบคุม](</th/gateway/operator-scopes>), [โปรโตคอล](</th/gateway/protocol>), [การอนุมัติ Exec](</th/tools/exec-approvals>), [การอนุมัติ Exec ขั้นสูง](</th/tools/exec-approvals-advanced>), [Elevated](</th/tools/elevated>)

Sandbox และนโยบายเครื่องมือ 6 ความสามารถ / รองรับ LTS

Experimental0%

Alpha68%

Beta79%

[Sandboxing](</th/gateway/sandboxing>), [Sandbox เทียบกับนโยบายเครื่องมือเทียบกับ Elevated](</th/gateway/sandbox-vs-tool-policy-vs-elevated>), [เครื่องมือ Sandbox หลาย Agent](</th/tools/multi-agent-sandbox-tools>), [ข้อมูลอ้างอิง Codex Harness](</th/plugins/codex-harness-reference>), [เครื่องมือกำหนดค่า](</th/gateway/config-tools>)

เส้นทางผู้ให้บริการ OpenAI และ Codex - M3 Beta - 5 พื้นที่

เอกสารเชิงลึก, เส้นทาง OAuth/การสมัครสมาชิก, เสียงแบบเรียลไทม์, รูปภาพ และพฤติกรรมด้านความเข้ากันได้ การเปลี่ยนแปลงของผู้ให้บริการยังทำให้ส่วนนี้ไม่เป็น Stable หากไม่มีหลักฐานจาก release-scorecard

ความครอบคลุม Experimental - 26%คุณภาพ Beta - 74%ความสมบูรณ์ Beta - 79%บางส่วน - 3

โมเดลและการยืนยันตัวตน 6 ความสามารถ / รองรับ LTS

Experimental44%

Beta79%

Beta79%

[Openai](</th/providers/openai>), [ชุดทดสอบ Codex](</th/plugins/codex-harness>), [โมเดล](</th/concepts/models>), [Oauth](</th/concepts/oauth>), [ข้อมูลอ้างอิงชุดทดสอบ Codex](</th/plugins/codex-harness-reference>), [การตรวจสอบการยืนยันตัวตน](</th/gateway/authentication>)

การตอบกลับและความเข้ากันได้ของเครื่องมือ 4 ความสามารถ / รองรับ LTS

Experimental40%

Beta79%

Beta79%

[Openai](</th/providers/openai>), [Openresponses Http Api](</th/gateway/openresponses-http-api>), [Openai Http Api](</th/gateway/openai-http-api>), [Plugin แบบเนทีฟของ Codex](</th/plugins/codex-native-plugins>)

ชุดทดสอบ Codex แบบเนทีฟ 2 ความสามารถ / รองรับ LTS

Experimental44%

Beta79%

Beta79%

[ชุดทดสอบ Codex](</th/plugins/codex-harness>), [รันไทม์ชุดทดสอบ Codex](</th/plugins/codex-harness-runtime>), [ข้อมูลอ้างอิงชุดทดสอบ Codex](</th/plugins/codex-harness-reference>), [Plugin แบบเนทีฟของ Codex](</th/plugins/codex-native-plugins>)

รูปภาพและอินพุตหลายรูปแบบ 2 ความสามารถ

Experimental0%

Alpha67%

Beta79%

[Openai](</th/providers/openai>), [การสร้างรูปภาพ](</th/tools/image-generation>), [รูปภาพ](</th/nodes/images>)

เสียงพูดและเสียงแบบเรียลไทม์ 2 ความสามารถ

Experimental0%

Alpha67%

Beta79%

[Openai](</th/providers/openai>), [Discord](</th/channels/discord>), [การโทรด้วยเสียง](</th/plugins/voice-call>)

เครื่องมือค้นหาเว็บ - M3 Beta - 4 พื้นที่

มีผู้ให้บริการและเอกสารหลายรายการ ต้องมีหลักฐานโควตา/ข้อผิดพลาด/SSRF แยกตามตระกูลผู้ให้บริการ

ความครอบคลุม Experimental - 9%คุณภาพ Beta - 74%ความครบถ้วน Beta - 79%ไม่มี

ผู้ให้บริการค้นหา 19 ความสามารถ

ทดลอง11%

Beta79%

Beta79%

[เว็บ](</th/tools/web>), [Brave Search](</th/tools/brave-search>), [Tavily](</th/tools/tavily>), [Exa Search](</th/tools/exa-search>), [Firecrawl](</th/tools/firecrawl>), [Perplexity Search](</th/tools/perplexity-search>), [Duckduckgo Search](</th/tools/duckduckgo-search>), [Searxng Search](</th/tools/searxng-search>), [Gemini Search](</th/tools/gemini-search>), [Grok Search](</th/tools/grok-search>), [Kimi Search](</th/tools/kimi-search>), [Minimax Search](</th/tools/minimax-search>), [Ollama Search](</th/tools/ollama-search>), [เส้นทางย่อย Sdk](</th/plugins/sdk-subpaths>), [ภาพรวม Sdk](</th/plugins/sdk-overview>), [Manifest](</th/plugins/manifest>)

การตั้งค่าและการวินิจฉัย 9 ความสามารถ

ทดลอง0%

Alpha68%

Beta79%

[เว็บ](</th/tools/web>), [ดึงข้อมูลเว็บ](</th/tools/web-fetch>), [คำถามที่พบบ่อย](</th/help/faq>), [ค่าใช้จ่ายการใช้ Api](</th/reference/api-usage-costs>), [Brave Search](</th/tools/brave-search>), [Perplexity Search](</th/tools/perplexity-search>), [Tavily](</th/tools/tavily>), [Firecrawl](</th/tools/firecrawl>)

ความปลอดภัยของเครือข่าย 4 ความสามารถ

ทดลอง0%

Alpha68%

Beta79%

[เว็บ](</th/tools/web>), [ดึงข้อมูลเว็บ](</th/tools/web-fetch>), [Firecrawl](</th/tools/firecrawl>), [Searxng Search](</th/tools/searxng-search>)

ความพร้อมใช้งานของเครื่องมือและการดึงข้อมูล 11 ความสามารถ

ทดลอง25%

Beta79%

Beta79%

[เครื่องมือกำหนดค่า](</th/gateway/config-tools>), [ดึงข้อมูลเว็บ](</th/tools/web-fetch>), [เว็บ](</th/tools/web>), [คำถามที่พบบ่อย](</th/help/faq>)

เส้นทางผู้ให้บริการ Anthropic - M3 Beta - 5 พื้นที่

ผู้ให้บริการโมเดลระดับแนวหน้า ต้องมีหลักฐานสถานการณ์การตรวจสอบสิทธิ์/แค็ตตาล็อก/การเรียกเครื่องมือเป็นประจำ

ความครอบคลุม ทดลอง - 0%คุณภาพ Beta - 71%ความสมบูรณ์ Beta - 78%ไม่มี

การยืนยันตัวตนและการกู้คืนของผู้ให้บริการ 9 ความสามารถ

ทดลอง0%

Alpha66%

Beta78%

[Anthropic](</th/providers/anthropic>), [Doctor](</th/gateway/doctor>), [ตัวอย่างการกำหนดค่า](</th/gateway/configuration-examples>), [การแก้ไขปัญหา](</th/gateway/troubleshooting>), [Prompt Caching](</th/reference/prompt-caching>)

การเลือกโมเดลและรันไทม์ 10 ความสามารถ

ทดลอง0%

Beta78%

Beta79%

[Anthropic](</th/providers/anthropic>), [กำหนดค่าเอเจนต์](</th/gateway/config-agents>), [โมเดล](</th/concepts/models>), [แบ็กเอนด์ CLI](</th/gateway/cli-backends>)

การส่งคำขอและความหมายของรอบการโต้ตอบ 10 ความสามารถ

ทดลอง0%

Beta77%

Beta79%

[Anthropic](</th/providers/anthropic>), [Prompt Caching](</th/reference/prompt-caching>), [การแก้ไขปัญหา](</th/gateway/troubleshooting>), [แบ็กเอนด์ CLI](</th/gateway/cli-backends>), [ผู้ให้บริการโมเดล](</th/concepts/model-providers>)

แคชพรอมป์และบริบท 5 ความสามารถ

ทดลอง0%

Alpha66%

Beta78%

[Anthropic](</th/providers/anthropic>), [Prompt Caching](</th/reference/prompt-caching>), [การแก้ไขปัญหา](</th/gateway/troubleshooting>), [Heartbeat](</th/gateway/heartbeat>)

อินพุตสื่อ 4 ความสามารถ

ทดลอง0%

Alpha66%

Beta78%

[Anthropic](</th/providers/anthropic>), [กำหนดค่าเอเจนต์](</th/gateway/config-agents>)

เส้นทางผู้ให้บริการ Google - M3 Beta - 5 พื้นที่

ผู้ให้บริการระดับเฟิร์สคลาสที่มีพื้นผิวโมเดลและเรียลไทม์ ต้องมีการให้คะแนน Live/Talk แยกต่างหาก

ความครอบคลุม ทดลอง - 0%คุณภาพ Alpha - 66%ความสมบูรณ์ Beta - 78%ไม่มี

การตั้งค่าผู้ให้บริการและข้อมูลรับรอง 10 ความสามารถ

ทดลอง0%

อัลฟา66%

เบต้า78%

[Google](</th/providers/google>), [ผู้ให้บริการโมเดล](</th/concepts/model-providers>)

การกำหนดเส้นทางโมเดลและปลายทาง 10 ความสามารถ

ทดลอง0%

อัลฟา66%

เบต้า78%

[Google](</th/providers/google>), [ผู้ให้บริการโมเดล](</th/concepts/model-providers>), [Google](</th/plugins/reference/google>), [การค้นหา Gemini](</th/tools/gemini-search>)

รันไทม์ Gemini โดยตรง 9 ความสามารถ

ทดลอง0%

อัลฟา66%

เบต้า78%

[Google](</th/providers/google>), [ผู้ให้บริการโมเดล](</th/concepts/model-providers>), [FAQ โมเดล](</th/help/faq-models>), [การทดสอบแบบสด](</th/help/testing-live>)

สื่อ การค้นหา และแบบเรียลไทม์ 10 ความสามารถ

ทดลอง0%

อัลฟา66%

เบต้า78%

[Google](</th/plugins/reference/google>), [Google](</th/providers/google>)

การแคชพรอมต์ 5 ความสามารถ

ทดลอง0%

อัลฟา66%

เบต้า78%

[การแคชพรอมต์](</th/reference/prompt-caching>), [Google](</th/providers/google>), [ผู้ให้บริการโมเดล](</th/concepts/model-providers>), [การใช้โทเค็น](</th/reference/token-use>)

เส้นทางผู้ให้บริการ OpenRouter - M3 เบต้า - 4 พื้นที่

เส้นทางผู้ให้บริการแบบรวมมีการจัดทำเอกสารไว้และมีประโยชน์ แต่พฤติกรรมเฉพาะโมเดลแตกต่างกันไป

ความครอบคลุม ทดลอง - 0%คุณภาพ อัลฟา - 66%ความสมบูรณ์ เบต้า - 78%ไม่มี

การตั้งค่าและการยืนยันตัวตนของผู้ให้บริการ 14 ความสามารถ

ทดลอง0%

Alpha66%

Beta78%

[Openrouter](</th/providers/openrouter>), [ผู้ให้บริการโมเดล](</th/concepts/model-providers>), [กำหนดค่า](</th/cli/configure>), [การยืนยันตัวตน](</th/gateway/authentication>), [สภาพแวดล้อม](</th/help/environment>), [โมเดล](</th/cli/models>), [โมเดล](</th/concepts/models>)

รันไทม์แชตและการทำให้เป็นมาตรฐาน 15 ความสามารถ

ทดลอง0%

Alpha66%

Beta78%

[Openrouter](</th/providers/openrouter>), [ผู้ให้บริการโมเดล](</th/concepts/model-providers>), [Prompt Caching](</th/reference/prompt-caching>)

การกู้คืนและการวินิจฉัยของผู้ให้บริการ 5 ความสามารถ

ทดลอง0%

Alpha66%

Beta78%

[การเปลี่ยนโมเดลสำรอง](</th/concepts/model-failover>), [Openrouter](</th/providers/openrouter>), [โมเดล](</th/cli/models>)

การสร้างสื่อและเสียงพูด 7 ความสามารถ

ทดลอง0%

Alpha66%

Beta78%

[Openrouter](</th/providers/openrouter>), [การสร้างรูปภาพ](</th/tools/image-generation>), [การสร้างเพลง](</th/tools/music-generation>), [ภาพรวมสื่อ](</th/tools/media-overview>), [การสร้างวิดีโอ](</th/tools/video-generation>), [Tts](</th/tools/tts>)

เครื่องมือสร้างรูปภาพ วิดีโอ และเพลง - M2 Alpha - 5 พื้นที่

มีความสามารถนี้ในผู้ให้บริการหลายราย แต่คุณภาพ เวลาแฝง และความเข้ากันได้ของพารามิเตอร์แตกต่างกันมากเกินไปสำหรับ beta หากไม่มีหลักฐานแยกตามผู้ให้บริการ

ความครอบคลุม ทดลอง - 0%คุณภาพ Alpha - 61%ความสมบูรณ์ Alpha - 68%ไม่มี

การกำหนดเส้นทางและการค้นพบสื่อ 4 ความสามารถ

ทดลอง0%

อัลฟา61%

อัลฟา68%

[การกำหนดค่าเอเจนต์](</th/gateway/config-agents>), [การสร้างรูปภาพ](</th/tools/image-generation>), [การสร้างวิดีโอ](</th/tools/video-generation>), [การสร้างเพลง](</th/tools/music-generation>)

วงจรชีวิตและการส่งมอบงาน 12 ความสามารถ

ทดลอง0%

อัลฟา61%

อัลฟา68%

[ภาพรวมสื่อ](</th/tools/media-overview>), [การสร้างรูปภาพ](</th/tools/image-generation>), [การสร้างวิดีโอ](</th/tools/video-generation>), [การสร้างเพลง](</th/tools/music-generation>)

การสร้างรูปภาพ 9 ความสามารถ

ทดลอง0%

อัลฟา61%

อัลฟา68%

[การสร้างรูปภาพ](</th/tools/image-generation>), [อนุมาน](</th/cli/infer>), [ภาพรวมสื่อ](</th/tools/media-overview>)

การสร้างวิดีโอ 11 ความสามารถ

ทดลอง0%

อัลฟา61%

อัลฟา68%

[การสร้างวิดีโอ](</th/tools/video-generation>), [Runway](</th/providers/runway>), [Pixverse](</th/providers/pixverse>), [Fal](</th/providers/fal>), [Openrouter](</th/providers/openrouter>)

การสร้างเพลง 6 ความสามารถ

ทดลอง0%

อัลฟา61%

อัลฟา68%

[การสร้างเพลง](</th/tools/music-generation>)

ผู้ให้บริการโมเดลภายในเครื่อง: Ollama, vLLM, SGLang, LM Studio - M2 อัลฟา - 5 พื้นที่

มีประโยชน์และมีเอกสารกำกับ แต่ความแตกต่างของสภาพแวดล้อมสูง

การครอบคลุม ทดลอง - 0%คุณภาพ อัลฟา - 61%ความครบถ้วน อัลฟา - 68%ไม่มี

การตั้งค่าผู้ให้บริการ วงจรชีวิต และการวินิจฉัย 12 ความสามารถ

ทดลอง0%

อัลฟา61%

อัลฟา68%

[โมเดลภายในเครื่อง](</th/gateway/local-models>), [Lmstudio](</th/providers/lmstudio>), [Ollama](</th/providers/ollama>), [Vllm](</th/providers/vllm>), [บริการโมเดลภายในเครื่อง](</th/gateway/local-model-services>), [เอเจนต์การกำหนดค่า](</th/gateway/config-agents>), [การแก้ไขปัญหา](</th/gateway/troubleshooting>), [ตัวตรวจสุขภาพ](</th/gateway/doctor>)

Plugin ผู้ให้บริการแบบเนทีฟ 10 ความสามารถ

ทดลอง0%

อัลฟา61%

อัลฟา68%

[Ollama](</th/providers/ollama>), [Lmstudio](</th/providers/lmstudio>)

ความเข้ากันได้ของรันไทม์ที่เข้ากันได้กับ OpenAI 8 ความสามารถ

ทดลอง0%

อัลฟา61%

อัลฟา68%

[Vllm](</th/providers/vllm>), [Sglang](</th/providers/sglang>), [โมเดลภายในเครื่อง](</th/gateway/local-models>), [Lmstudio](</th/providers/lmstudio>)

หน่วยความจำและการฝังเวกเตอร์ภายในเครื่อง 5 ความสามารถ

ทดลอง0%

อัลฟา61%

อัลฟา68%

[หน่วยความจำ](</th/concepts/memory>), [ตัวตรวจสุขภาพ](</th/gateway/doctor>)

ความปลอดภัยของเครือข่ายและการควบคุมพรอมป์ต์ 2 ความสามารถ

ทดลอง0%

อัลฟา61%

อัลฟา68%

[ดัชนี](</th/gateway/security>), [เครื่องมือการกำหนดค่า](</th/gateway/config-tools>), [โมเดลภายในเครื่อง](</th/gateway/local-models>)

ผู้ให้บริการโฮสต์ระยะยาว - M2 อัลฟา - 3 พื้นที่

มีหน้าเอกสาร/อ้างอิงอยู่มากมาย ควรสร้างคะแนนจากเมทาดาทาของผู้ให้บริการร่วมกับความครอบคลุมของการทดสอบ smoke แบบสด

ความครอบคลุม เชิงทดลอง - 0%คุณภาพ อัลฟา - 61%ความครบถ้วน อัลฟา - 68%ไม่มี

ผู้ให้บริการ LLM แบบโฮสต์ 12 ความสามารถ

เชิงทดลอง0%

อัลฟา61%

อัลฟา68%

[ดัชนี](</th/providers>), [ผู้ให้บริการโมเดล](</th/concepts/model-providers>), [การทดสอบจริง](</th/help/testing-live>), [เริ่มใช้งาน](</th/cli/onboard>)

ผู้ให้บริการสื่อแบบโฮสต์ 8 ความสามารถ

เชิงทดลอง0%

อัลฟา61%

อัลฟา68%

[Manifest](</th/plugins/manifest>), [การทดสอบจริง](</th/help/testing-live>), [ดัชนี](</th/providers>)

การดำเนินงานของผู้ให้บริการ 12 ความสามารถ

เชิงทดลอง0%

อัลฟา61%

อัลฟา68%

[ดัชนี](</th/providers>), [ผู้ให้บริการโมเดล](</th/concepts/model-providers>), [Manifest](</th/plugins/manifest>), [การทดสอบจริง](</th/help/testing-live>), [โมเดล](</th/cli/models>)

Was this useful?YesNo

Open issue