---
title: Z.AI
source_url: https://docs.openclaw.ai/th/providers/zai
scraped_at: 2026-05-25
---

[Z.AI](<http://Z.AI>) เป็นแพลตฟอร์ม API สำหรับโมเดล **GLM** โดยมี REST APIs สำหรับ GLM และใช้ API keys สำหรับการยืนยันตัวตน สร้าง API key ของคุณในคอนโซล [Z.AI](<http://Z.AI>) OpenClaw ใช้ provider `zai` พร้อม [Z.AI](<http://Z.AI>) API key

  * Provider: `zai`
  * การยืนยันตัวตน: `ZAI_API_KEY`
  * API: [Z.AI](<http://Z.AI>) Chat Completions (การยืนยันตัวตนแบบ Bearer)


## เริ่มต้นใช้งาน

### ตรวจหาปลายทางอัตโนมัติ

**เหมาะที่สุดสำหรับ:** ผู้ใช้ส่วนใหญ่ OpenClaw ตรวจหาปลายทาง [Z.AI](<http://Z.AI>) ที่ตรงกับคีย์และใช้ URL ฐานที่ถูกต้องโดยอัตโนมัติ

* ### เรียกใช้การเริ่มต้นใช้งาน

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### ตั้งค่าโมเดลเริ่มต้น

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### ตรวจสอบว่าโมเดลอยู่ในรายการ

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### ปลายทางภูมิภาคแบบระบุชัดเจน

**เหมาะที่สุดสำหรับ:** ผู้ใช้ที่ต้องการบังคับใช้ Coding Plan หรือพื้นผิว API ทั่วไปที่เจาะจง

* ### เลือกตัวเลือกการเริ่มต้นใช้งานที่ถูกต้อง

bashCopy code
[code]
    # Coding Plan Global (recommended for Coding Plan users)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (China region)openclaw onboard --auth-choice zai-coding-cn # General APIopenclaw onboard --auth-choice zai-global # General API CN (China region)openclaw onboard --auth-choice zai-cn
[/code]

* ### ตั้งค่าโมเดลเริ่มต้น

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### ตรวจสอบว่าโมเดลอยู่ในรายการ

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## แคตตาล็อกในตัว

OpenClaw มาพร้อมแคตตาล็อก provider `zai` ที่รวมมาในแมนิเฟสต์ Plugin ดังนั้นการแสดงรายการแบบอ่านอย่างเดียว จึงสามารถแสดงแถว GLM ที่รู้จักได้โดยไม่ต้องโหลดรันไทม์ของ provider:

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

แคตตาล็อกที่อิงตามแมนิเฟสต์ในปัจจุบันประกอบด้วย:

การอ้างอิงโมเดล | หมายเหตุ  
---|---  
`zai/glm-5.1` | โมเดลเริ่มต้น  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## การกำหนดค่าขั้นสูง

การแก้ไขโมเดล GLM-5 ที่ไม่รู้จักแบบส่งต่อ

id `glm-5*` ที่ไม่รู้จักยังคงแก้ไขแบบส่งต่อบนเส้นทาง provider ที่รวมมา โดย สังเคราะห์เมทาดาทาที่ provider เป็นเจ้าของจากเทมเพลต `glm-4.7` เมื่อ id ตรงกับรูปแบบตระกูล GLM-5 ปัจจุบัน

การสตรีมการเรียกเครื่องมือ

`tool_stream` เปิดใช้งานเป็นค่าเริ่มต้นสำหรับการสตรีมการเรียกเครื่องมือของ [Z.AI](<http://Z.AI>) หากต้องการปิดใช้งาน:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

การคิดและการคงการคิดไว้

การคิดของ [Z.AI](<http://Z.AI>) ทำตามตัวควบคุม `/think` ของ OpenClaw เมื่อปิดการคิด OpenClaw จะส่ง `thinking: { type: "disabled" }` เพื่อหลีกเลี่ยงคำตอบที่ ใช้งบประมาณเอาต์พุตกับ `reasoning_content` ก่อนข้อความที่มองเห็นได้

การคงการคิดไว้เป็นแบบเลือกเปิด เพราะ [Z.AI](<http://Z.AI>) ต้องการให้เล่นซ้ำ `reasoning_content` ในประวัติทั้งหมด ซึ่งเพิ่มจำนวนโทเค็นพรอมป์ เปิดใช้งาน ต่อโมเดล:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.1": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

เมื่อเปิดใช้งานและการคิดเปิดอยู่ OpenClaw จะส่ง `thinking: { type: "enabled", clear_thinking: false }` และเล่นซ้ำ `reasoning_content` ก่อนหน้าสำหรับทรานสคริปต์เดียวกันที่เข้ากันได้กับ OpenAI

ผู้ใช้ขั้นสูงยังสามารถแทนที่เพย์โหลด provider ที่แน่นอนได้ด้วย `params.extra_body.thinking`

ความเข้าใจรูปภาพ

Plugin [Z.AI](<http://Z.AI>) ที่รวมมาจะลงทะเบียนความเข้าใจรูปภาพ

คุณสมบัติ | ค่า  
---|---  
โมเดล | `glm-4.6v`  
  
ความเข้าใจรูปภาพจะถูกแก้ไขโดยอัตโนมัติจากการยืนยันตัวตน [Z.AI](<http://Z.AI>) ที่กำหนดค่าไว้ โดย ไม่ต้องมีการกำหนดค่าเพิ่มเติม

รายละเอียดการยืนยันตัวตน

  * [Z.AI](<http://Z.AI>) ใช้การยืนยันตัวตนแบบ Bearer ด้วย API key ของคุณ
  * ตัวเลือกการเริ่มต้นใช้งาน `zai-api-key` จะตรวจหาปลายทาง [Z.AI](<http://Z.AI>) ที่ตรงกันจากคำนำหน้าคีย์โดยอัตโนมัติ
  * ใช้ตัวเลือกภูมิภาคแบบระบุชัดเจน (`zai-coding-global`, `zai-coding-cn`, `zai-global`, `zai-cn`) เมื่อคุณต้องการบังคับใช้พื้นผิว API ที่เจาะจง


## ที่เกี่ยวข้อง

[**ตระกูลโมเดล GLM** ภาพรวมตระกูลโมเดลสำหรับ GLM ](</th/providers/glm>) [**การเลือกโมเดล** การเลือก provider, การอ้างอิงโมเดล และพฤติกรรม failover ](</th/concepts/model-providers>)

Was this useful?YesNo