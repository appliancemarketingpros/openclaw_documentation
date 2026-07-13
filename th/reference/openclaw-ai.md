---
title: แพ็กเกจ @openclaw/ai
source_url: https://docs.openclaw.ai/th/reference/openclaw-ai
scraped_at: 2026-07-13
---

ReferenceTechnical reference

`@openclaw/ai` คือรูปแบบไลบรารีที่สามารถเผยแพร่ได้ของเลเยอร์การเรียกใช้โมเดลของ OpenClaw ซึ่งประกอบด้วยสัญญาข้อความ/เครื่องมือ/สตรีมที่ไม่ขึ้นกับผู้ให้บริการ การตรวจสอบความถูกต้อง การวินิจฉัย สตรีมเหตุการณ์ รีจิสทรีรันไทม์แบบแยกอิสระ และอะแดปเตอร์ที่โหลดแบบล่าช้าสำหรับตระกูล API ในตัวทั้งแปดตระกูล (Anthropic Messages, OpenAI Completions, OpenAI Responses, Azure OpenAI Responses, ChatGPT/Codex Responses, Google Generative AI, Google Vertex, Mistral Conversations)

แพ็กเกจนี้เผยแพร่พร้อมกับแพ็กเกจราก `openclaw` ในทุกรุ่น โดยตรึงไว้ที่เวอร์ชันเดียวกัน และมี `npm-shrinkwrap.json` ของตนเองเพื่อให้แผนผังการขึ้นต่อกันแบบส่งผ่านถูกล็อกไว้ในขณะติดตั้ง การติดตั้ง `openclaw` จะติดตั้ง `@openclaw/ai` เวอร์ชันที่ตรงกันโดยอัตโนมัติ ส่วนผู้ใช้ไลบรารีสามารถกำหนดให้ขึ้นต่อแพ็กเกจนี้โดยตรงได้โดยไม่ต้องใช้โค้ดแอปพลิเคชัน OpenClaw ใดๆ

## เริ่มต้นอย่างรวดเร็ว

jsCopy code
[code]
      const runtime = createLlmRuntime();registerBuiltInApiProviders(runtime.registry); const stream = runtime.streamSimple(model, { messages }, { apiKey });for await (const event of stream) {  if (event.type === "text_delta") process.stdout.write(event.delta);}const result = await stream.result();
[/code]

เวอร์ชันที่เรียกใช้ได้อยู่ในที่เก็บโค้ดที่ `examples/ai-chat`

## สัญญาการออกแบบ

  * **กำหนดขอบเขตตามอินสแตนซ์โดยค่าเริ่มต้น** การนำเข้าแพ็กเกจจะไม่ลงทะเบียนสิ่งใดในขอบเขตส่วนกลาง `createApiRegistry()` / `createLlmRuntime()` จะคืนค่าอินสแตนซ์ที่แยกอิสระ ส่วน `registerBuiltInApiProviders(registry)` จะเลือกให้รีจิสทรีหนึ่งรายการใช้ทรานสปอร์ตในตัว โมดูล SDK ของผู้ให้บริการจะโหลดแบบล่าช้าเมื่อใช้งานครั้งแรก
  * **นโยบายของโฮสต์ถูกฉีดเข้ามา ไม่ได้รวมไว้ในแพ็กเกจ** การป้องกันการดึงข้อมูลของคำขอ (เช่น นโยบาย SSRF) การปกปิดข้อมูลลับในข้อความที่เล่นซ้ำจากผลลัพธ์เครื่องมือ ค่าเริ่มต้นของเครื่องมือแบบเข้มงวดของ OpenAI และการบันทึกการวินิจฉัย เป็นพอร์ต `AiTransportHost` ที่กำหนดค่าด้วย `configureAiTransportHost` ค่าเริ่มต้นของไลบรารีจะไม่มีการทำงานใดๆ ส่วน OpenClaw จะติดตั้งการทำงานจริงในส่วนเชื่อมต่อสตรีมของตน
  * **เอกลักษณ์ของสตรีมเหตุการณ์หนึ่งเดียว** `@openclaw/ai/event-stream` คือตัวสร้าง `EventStream` มาตรฐานที่ใช้ร่วมกันโดยแกนหลักของ OpenClaw, agent-core และผู้ใช้ภายนอก
  * **พาธย่อย`internal/*` ไม่ใช่ API** พาธเหล่านี้มีไว้สำหรับแอปพลิเคชัน OpenClaw เอง และไม่มีการรับประกันตาม semver
  * รหัสผู้ให้บริการ ข้อมูลรับรอง แค็ตตาล็อกโมเดล การลองใหม่ และการสลับไปใช้ระบบสำรอง ยังคงเป็นความรับผิดชอบของแอปพลิเคชัน OpenClaw เพิ่มเลเยอร์สำหรับสิ่งเหล่านี้ไว้รอบแพ็กเกจนี้ ส่วนผู้ใช้ไลบรารีจะระบุออบเจ็กต์ `Model` และตัวเลือกโดยตรง


## การส่งออกพาธย่อย

พาธย่อย | เนื้อหา  
---|---  
`.` | สัญญา, `createApiRegistry`, `createLlmRuntime`, `configureAiTransportHost`  
`./providers` | `registerBuiltInApiProviders`, `resetApiProviders`  
`./types` | ชนิดของโมเดล/ข้อความ/เครื่องมือ/สตรีม  
`./validation` | การตรวจสอบความถูกต้องของอาร์กิวเมนต์เครื่องมือ  
`./diagnostics` | สัญญาการวินิจฉัย  
`./event-stream` | การทำงานของ `EventStream` ที่ใช้ร่วมกัน  
`./internal/*` | สำหรับใช้ภายใน OpenClaw ไม่มีการรับประกันตาม semver  
  
Was this useful?YesNo

Open issue