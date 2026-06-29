---
title: NovitaAI
source_url: https://docs.openclaw.ai/th/providers/novita
scraped_at: 2026-06-29
---

ModelsProviders

NovitaAI เป็นผู้ให้บริการโครงสร้างพื้นฐาน AI แบบโฮสต์ที่มี API โมเดลที่เข้ากันได้กับ OpenAI ใน OpenClaw ผู้ให้บริการนี้เป็นผู้ให้บริการโมเดลที่บันเดิลมาให้ ดังนั้น provider id คือ `novita` ข้อมูลประจำตัวจะผ่านโฟลว์การยืนยันตัวตนโมเดลตามปกติ และ model refs จะมีรูปแบบเช่น `novita/deepseek/deepseek-v3-0324`

ใช้ Novita เมื่อคุณต้องการเข้าถึงโมเดล open-weight และเส้นทางโมเดลจากบุคคลที่สามแบบโฮสต์ โดยไม่ต้องรัน inference server ของคุณเอง แค็ตตาล็อกที่บันเดิลมาเน้นโมเดลแชตที่เหมาะกับ agent turns รวมถึงเส้นทาง DeepSeek, Moonshot, MiniMax, GLM และ Qwen ที่ Novita เปิดให้ใช้

ผู้ให้บริการนี้ใช้ endpoint ของ Novita ที่เข้ากันได้กับ OpenAI OpenClaw จัดการการลงทะเบียนผู้ให้บริการ การยืนยันตัวตน aliases การทำให้ model ref เป็นมาตรฐาน และการเลือก base URL ส่วน Novita ควบคุมความพร้อมใช้งานของโมเดลจริง สิทธิ์ของบัญชี ราคา และขีดจำกัดอัตราการใช้งาน

## การตั้งค่า

สร้าง API key ที่ [novita.ai/settings/key-management](<https://novita.ai/settings/key-management>) แล้วรัน:

bashCopy code
[code]
    openclaw onboard --auth-choice novita-api-key
[/code]

หรือตั้งค่า:

bashCopy code
[code]
    export NOVITA_API_KEY="<your-novita-api-key>" # pragma: allowlist secret
[/code]

## ค่าเริ่มต้น

  * ผู้ให้บริการ: `novita`
  * Aliases: `novita-ai`, `novitaai`
  * Base URL: `https://api.novita.ai/openai/v1`
  * ตัวแปร env: `NOVITA_API_KEY`
  * โมเดลเริ่มต้น: `novita/deepseek/deepseek-v3-0324`


## ควรเลือก Novita เมื่อใด

  * คุณต้องการเข้าถึงโมเดล open-weight แบบโฮสต์ด้วย API ที่เข้ากันได้กับ OpenAI
  * คุณต้องการเส้นทาง DeepSeek, Kimi, MiniMax, GLM หรือโมเดลตระกูล Qwen ผ่านบัญชีผู้ให้บริการเดียว
  * คุณต้องการเส้นทาง fallback แบบโฮสต์อีกเส้นทางหนึ่งนอกเหนือจาก OpenRouter, GMI, DeepInfra หรือ API ของผู้ขายโดยตรง
  * คุณต้องการให้ผู้ให้บริการโฮสต์โมเดลให้ แทนการดูแลโครงสร้างพื้นฐาน vLLM, SGLang, LM Studio หรือ Ollama เอง


เลือกผู้ให้บริการจากผู้ขายโดยตรงเมื่อคุณต้องการพารามิเตอร์คำขอแบบ vendor-native หรือสัญญาการสนับสนุน เลือกผู้ให้บริการภายในเครื่องเมื่อโมเดลต้องรันบนฮาร์ดแวร์ของคุณเองหรืออยู่หลังขอบเขตเครือข่ายของคุณเอง

## โมเดล

แค็ตตาล็อกที่บันเดิลมาจะเติม route ids ของ NovitaAI ที่มักพร้อมใช้งาน รวมถึง:

  * `novita/moonshotai/kimi-k2.5`
  * `novita/minimax/minimax-m2.7`
  * `novita/zai-org/glm-5`
  * `novita/deepseek/deepseek-v3-0324`
  * `novita/deepseek/deepseek-r1-0528`
  * `novita/qwen/qwen3-235b-a22b-fp8`


แค็ตตาล็อกนี้เป็นจุดเริ่มต้นสำหรับการเลือกโมเดลใน OpenClaw บัญชี ภูมิภาค หรือแค็ตตาล็อกปัจจุบันของ Novita อาจเพิ่ม ลบ หรือจำกัดเส้นทางได้ ตรวจสอบผู้ให้บริการจาก CLI ก่อนตั้งค่าเริ่มต้นระยะยาว:

bashCopy code
[code]
    openclaw models list --provider novita
[/code]

## การแก้ไขปัญหา

  * `401` หรือ `403`: ตรวจสอบ key ในหน้าการจัดการ key ของ Novita และรัน `openclaw onboard --auth-choice novita-api-key` อีกครั้งหากโปรไฟล์ที่จัดเก็บไว้เก่า
  * ข้อผิดพลาดโมเดลไม่รู้จัก: ใช้ `novita/<route-id>` ที่ตรงกับค่าที่ส่งคืนโดย `openclaw models list --provider novita`
  * เส้นทางช้าหรือล้มเหลว: ลองเส้นทางโมเดล Novita อื่น หรือตั้ง Novita เป็นผู้ให้บริการ fallback สำหรับงานที่ยอมรับความแปรปรวนเฉพาะผู้ให้บริการได้


## ที่เกี่ยวข้อง

  * [ผู้ให้บริการโมเดล](</th/concepts/model-providers>)
  * [ผู้ให้บริการทั้งหมด](</th/providers>)


Was this useful?YesNo

Open issue