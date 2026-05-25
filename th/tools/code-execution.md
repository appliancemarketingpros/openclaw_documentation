---
title: การเรียกใช้โค้ด
source_url: https://docs.openclaw.ai/th/tools/code-execution
scraped_at: 2026-05-25
---

`code_execution` รันการวิเคราะห์ Python ระยะไกลแบบ sandboxed บน Responses API ของ xAI โดยลงทะเบียนผ่าน Plugin `xai` ที่รวมมาให้ (ภายใต้สัญญา `tools`) และส่งต่อไปยัง endpoint `https://api.x.ai/v1/responses` เดียวกับที่ `x_search` ใช้

คุณสมบัติ | ค่า  
---|---  
ชื่อเครื่องมือ | `code_execution`  
Provider plugin | `xai` (รวมมาให้, `enabledByDefault: true`)  
Auth | โปรไฟล์ auth ของ xAI, `XAI_API_KEY`, หรือ `plugins.entries.xai.config.webSearch.apiKey`  
โมเดลเริ่มต้น | `grok-4-1-fast`  
timeout เริ่มต้น | 30 วินาที  
`maxTurns` เริ่มต้น | ไม่ได้ตั้งค่า (xAI ใช้ขีดจำกัดภายในของตนเอง)  
  
สิ่งนี้แตกต่างจาก [`exec`](</th/tools/exec>) แบบ local:

  * `exec` รันคำสั่ง shell บนเครื่องของคุณหรือ node ที่จับคู่ไว้
  * `code_execution` รัน Python ใน sandbox ระยะไกลของ xAI


ใช้ `code_execution` สำหรับ:

  * การคำนวณ
  * การจัดทำตาราง
  * สถิติอย่างรวดเร็ว
  * การวิเคราะห์รูปแบบแผนภูมิ
  * การวิเคราะห์ข้อมูลที่ส่งกลับมาจาก `x_search` หรือ `web_search`


**อย่า** ใช้เมื่อคุณต้องการไฟล์ local, shell ของคุณ, repo ของคุณ หรืออุปกรณ์ที่จับคู่ไว้ ให้ใช้ [`exec`](</th/tools/exec>) สำหรับกรณีนั้น

## การตั้งค่า

* ### ระบุคีย์ API ของ xAI

รัน `openclaw onboard --auth-choice xai-api-key` สำหรับ `code_execution` และ `x_search` หรือกำหนด `XAI_API_KEY` / กำหนดค่าคีย์ภายใต้ Plugin xAI เมื่อคุณต้องการให้การค้นหาเว็บของ Grok ใช้ credential เดียวกันด้วย:

bashCopy code
[code]
    export XAI_API_KEY=xai-...
[/code]

หรือผ่าน config:

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          webSearch: {            apiKey: "xai-...",          },        },      },    },  },}
[/code]

* ### เปิดใช้งานและปรับแต่ง code_execution

เครื่องมือนี้ถูกควบคุมด้วย `plugins.entries.xai.config.codeExecution.enabled` ค่าเริ่มต้นคือปิด

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast", // override the default xAI code-execution model            maxTurns: 2,            // optional cap on internal tool turns            timeoutSeconds: 30,     // request timeout (default: 30)          },        },      },    },  },}
[/code]

* ### รีสตาร์ท Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

`code_execution` จะปรากฏในรายการเครื่องมือของ agent เมื่อ Plugin xAI ลงทะเบียนใหม่ด้วย `enabled: true`

## วิธีใช้งาน

ถามอย่างเป็นธรรมชาติและระบุเจตนาการวิเคราะห์ให้ชัดเจน:

textCopy code
[code]
    Use code_execution to calculate the 7-day moving average for these numbers: ...
[/code]

textCopy code
[code]
    Use x_search to find posts mentioning OpenClaw this week, then use code_execution to count them by day.
[/code]

textCopy code
[code]
    Use web_search to gather the latest AI benchmark numbers, then use code_execution to compare percent changes.
[/code]

เครื่องมือนี้รับพารามิเตอร์ `task` เพียงตัวเดียวภายใน ดังนั้น agent ควรส่งคำขอวิเคราะห์แบบเต็มและข้อมูล inline ใด ๆ ใน prompt เดียว

## ข้อผิดพลาด

เมื่อเครื่องมือรันโดยไม่มี auth เครื่องมือจะส่งคืนข้อผิดพลาด `missing_xai_api_key` แบบมีโครงสร้าง ซึ่งชี้ไปยังตัวเลือก auth-profile, env var และ config ข้อผิดพลาดเป็น JSON ไม่ใช่ exception ที่ถูก throw ดังนั้น agent จึงสามารถแก้ไขเองได้:

jsonCopy code
[code]
    {  "error": "missing_xai_api_key",  "message": "code_execution needs an xAI API key. Run openclaw onboard --auth-choice xai-api-key, set XAI_API_KEY in the Gateway environment, or configure plugins.entries.xai.config.webSearch.apiKey.",  "docs": "https://docs.openclaw.ai/tools/code-execution"}
[/code]

## ขีดจำกัด

  * นี่คือการประมวลผลระยะไกลของ xAI ไม่ใช่การประมวลผล process แบบ local
  * ถือว่าผลลัพธ์เป็นการวิเคราะห์ชั่วคราว ไม่ใช่ session notebook ถาวร
  * อย่าสันนิษฐานว่ามีสิทธิ์เข้าถึงไฟล์ local หรือ workspace ของคุณ
  * สำหรับข้อมูล X ใหม่ ให้ใช้ [`x_search`](</th/tools/web#x_search>) ก่อน แล้วส่งผลลัพธ์เข้าไปยัง `code_execution`


## ที่เกี่ยวข้อง

[**เครื่องมือ Exec** การรัน shell แบบ local บนเครื่องของคุณหรือ node ที่จับคู่ไว้ ](</th/tools/exec>) [**การอนุมัติ Exec** นโยบายอนุญาต/ปฏิเสธสำหรับการรัน shell ](</th/tools/exec-approvals>) [**เครื่องมือเว็บ** `web_search`, `x_search` และ `web_fetch` ](</th/tools/web>) [**provider xAI** โมเดล Grok, การค้นหาเว็บ/x และ config การรันโค้ด ](</th/providers/xai>)

Was this useful?YesNo