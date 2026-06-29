---
title: Cohere
source_url: https://docs.openclaw.ai/th/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>) ให้การอนุมานที่เข้ากันได้กับ OpenAI ผ่าน Compatibility API ของตน OpenClaw จัดส่งผู้ให้บริการ Cohere ในช่วงการเปลี่ยนผ่านสู่การแยกเป็นภายนอก และยังเผยแพร่เป็น Plugin ภายนอกอย่างเป็นทางการพร้อมแค็ตตาล็อกโมเดล Command A

คุณสมบัติ | ค่า  
---|---  
รหัสผู้ให้บริการ | `cohere`  
Plugin | รวมมาให้ในช่วงเปลี่ยนผ่าน; แพ็กเกจภายนอกอย่างเป็นทางการ  
ตัวแปรสภาพแวดล้อมสำหรับการยืนยันตัวตน | `COHERE_API_KEY`  
แฟล็กการเริ่มต้นใช้งาน | `--auth-choice cohere-api-key`  
แฟล็ก CLI โดยตรง | `--cohere-api-key <key>`  
API | เข้ากันได้กับ OpenAI (`openai-completions`)  
URL ฐาน | `https://api.cohere.ai/compatibility/v1`  
โมเดลเริ่มต้น | `cohere/command-a-03-2025`  
  
## เริ่มต้นใช้งาน

  1. Cohere รวมอยู่ในแพ็กเกจ OpenClaw ปัจจุบัน หากไม่พร้อมใช้งาน ให้ติดตั้งแพ็กเกจภายนอกแล้วรีสตาร์ท Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. สร้างคีย์ API ของ Cohere
  3. เรียกใช้การเริ่มต้นใช้งาน:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. ยืนยันว่าแค็ตตาล็อกพร้อมใช้งาน:

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

โมเดลเริ่มต้นจะถูกตั้งค่าเฉพาะเมื่อยังไม่มีการกำหนดค่าโมเดลหลักไว้แล้ว

## การตั้งค่าด้วยสภาพแวดล้อมเท่านั้น

ทำให้ `COHERE_API_KEY` พร้อมใช้งานกับกระบวนการ Gateway จากนั้นเลือกโมเดล Cohere:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## ที่เกี่ยวข้อง

  * [ผู้ให้บริการโมเดล](</th/concepts/model-providers>)
  * [CLI สำหรับโมเดล](</th/cli/models>)
  * [ไดเรกทอรีผู้ให้บริการ](</th/providers>)


Was this useful?YesNo

Open issue