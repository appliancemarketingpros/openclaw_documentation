---
title: Chutes
source_url: https://docs.openclaw.ai/th/providers/chutes
scraped_at: 2026-05-25
---

[Chutes](<https://chutes.ai>) เปิดเผยแค็ตตาล็อกโมเดลโอเพนซอร์สผ่าน API ที่เข้ากันได้กับ OpenAI OpenClaw รองรับทั้ง OAuth ผ่านเบราว์เซอร์และการยืนยันตัวตนด้วย API key โดยตรงสำหรับผู้ให้บริการ `chutes` ที่รวมมาให้

คุณสมบัติ | ค่า  
---|---  
ผู้ให้บริการ | `chutes`  
API | เข้ากันได้กับ OpenAI  
URL ฐาน | `https://llm.chutes.ai/v1`  
การยืนยันตัวตน | OAuth หรือ API key (ดูด้านล่าง)  
  
## เริ่มต้นใช้งาน

### OAuth

* ### เรียกใช้ขั้นตอนเริ่มต้นใช้งาน OAuth

bashCopy code
[code]
    openclaw onboard --auth-choice chutes
[/code]

OpenClaw เปิดขั้นตอนผ่านเบราว์เซอร์ในเครื่อง หรือแสดง URL + ขั้นตอนคัดลอกการเปลี่ยนเส้นทางไปวาง บนโฮสต์ระยะไกล/ไม่มีหน้าจอ โทเค็น OAuth จะรีเฟรชอัตโนมัติผ่านโปรไฟล์การยืนยันตัวตนของ OpenClaw

* ### ตรวจสอบโมเดลเริ่มต้น

หลังจากเริ่มต้นใช้งานแล้ว โมเดลเริ่มต้นจะถูกตั้งค่าเป็น `chutes/zai-org/GLM-4.7-TEE` และแค็ตตาล็อก Chutes ที่รวมมาให้จะถูก ลงทะเบียน

### API key

* ### รับ API key

สร้างคีย์ที่ [chutes.ai/settings/api-keys](<https://chutes.ai/settings/api-keys>)

* ### เรียกใช้ขั้นตอนเริ่มต้นใช้งาน API key

bashCopy code
[code]
    openclaw onboard --auth-choice chutes-api-key
[/code]

* ### ตรวจสอบโมเดลเริ่มต้น

หลังจากเริ่มต้นใช้งานแล้ว โมเดลเริ่มต้นจะถูกตั้งค่าเป็น `chutes/zai-org/GLM-4.7-TEE` และแค็ตตาล็อก Chutes ที่รวมมาให้จะถูก ลงทะเบียน

## พฤติกรรมการค้นพบ

เมื่อมีการยืนยันตัวตนของ Chutes พร้อมใช้งาน OpenClaw จะสอบถามแค็ตตาล็อก Chutes ด้วย ข้อมูลรับรองนั้นและใช้โมเดลที่ค้นพบ หากการค้นพบล้มเหลว OpenClaw จะถอยกลับ ไปใช้แค็ตตาล็อกแบบคงที่ที่รวมมาให้ เพื่อให้การเริ่มต้นใช้งานและการเริ่มทำงานยังคงใช้งานได้

## นามแฝงเริ่มต้น

OpenClaw ลงทะเบียนนามแฝงเพื่อความสะดวกสามรายการสำหรับแค็ตตาล็อก Chutes ที่รวมมาให้:

นามแฝง | โมเดลเป้าหมาย  
---|---  
`chutes-fast` | `chutes/zai-org/GLM-4.7-FP8`  
`chutes-pro` | `chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes-vision` | `chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
  
## แค็ตตาล็อกเริ่มต้นในตัว

แค็ตตาล็อกสำรองที่รวมมาให้มี ref ของ Chutes ปัจจุบัน:

ref โมเดล  
---  
`chutes/zai-org/GLM-4.7-TEE`  
`chutes/zai-org/GLM-5-TEE`  
`chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes/deepseek-ai/DeepSeek-R1-0528-TEE`  
`chutes/moonshotai/Kimi-K2.5-TEE`  
`chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
`chutes/Qwen/Qwen3-Coder-Next-TEE`  
`chutes/openai/gpt-oss-120b-TEE`  
  
## ตัวอย่างการกำหนดค่า

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "chutes/zai-org/GLM-4.7-TEE" },      models: {        "chutes/zai-org/GLM-4.7-TEE": { alias: "Chutes GLM 4.7" },        "chutes/deepseek-ai/DeepSeek-V3.2-TEE": { alias: "Chutes DeepSeek V3.2" },      },    },  },}
[/code]

การแทนที่ OAuth

คุณสามารถปรับแต่งขั้นตอน OAuth ด้วยตัวแปรสภาพแวดล้อมเพิ่มเติมได้:

ตัวแปร | วัตถุประสงค์  
---|---  
`CHUTES_CLIENT_ID` | ID ไคลเอนต์ OAuth แบบกำหนดเอง  
`CHUTES_CLIENT_SECRET` | ความลับไคลเอนต์ OAuth แบบกำหนดเอง  
`CHUTES_OAUTH_REDIRECT_URI` | URI การเปลี่ยนเส้นทางแบบกำหนดเอง  
`CHUTES_OAUTH_SCOPES` | ขอบเขต OAuth แบบกำหนดเอง  
  
ดู[เอกสาร OAuth ของ Chutes](<https://chutes.ai/docs/sign-in-with-chutes/overview>) สำหรับข้อกำหนดของแอปการเปลี่ยนเส้นทางและความช่วยเหลือ

หมายเหตุ

  * การค้นพบด้วย API-key และ OAuth ใช้ id ผู้ให้บริการ `chutes` เดียวกัน
  * โมเดล Chutes จะถูกลงทะเบียนเป็น `chutes/<model-id>`
  * หากการค้นพบล้มเหลวตอนเริ่มทำงาน ระบบจะใช้แค็ตตาล็อกแบบคงที่ที่รวมมาให้โดยอัตโนมัติ


## ที่เกี่ยวข้อง

[**การเลือกโมเดล** กฎของผู้ให้บริการ, ref โมเดล และพฤติกรรมการสลับเมื่อเกิดความล้มเหลว ](</th/concepts/model-providers>) [**ข้อมูลอ้างอิงการกำหนดค่า** สคีมาการกำหนดค่าทั้งหมด รวมถึงการตั้งค่าผู้ให้บริการ ](</th/gateway/configuration-reference>) [**Chutes** แดชบอร์ด Chutes และเอกสาร API ](<https://chutes.ai>) [**API key ของ Chutes** สร้างและจัดการ API key ของ Chutes ](<https://chutes.ai/settings/api-keys>)

Was this useful?YesNo