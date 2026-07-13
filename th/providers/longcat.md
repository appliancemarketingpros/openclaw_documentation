---
title: LongCat
source_url: https://docs.openclaw.ai/th/providers/longcat
scraped_at: 2026-07-13
---

ModelsProviders

[LongCat](<https://longcat.ai>) ให้บริการ API แบบโฮสต์สำหรับ LongCat-2.0 ซึ่งเป็นโมเดลการให้เหตุผลที่สร้างขึ้นสำหรับงานเขียนโค้ดและเวิร์กโหลดแบบเอเจนต์ OpenClaw มี Plugin `longcat` อย่างเป็นทางการสำหรับเอนด์พอยต์ที่เข้ากันได้กับ OpenAI ของ LongCat

คุณสมบัติ | ค่า  
---|---  
ผู้ให้บริการ | `longcat`  
การยืนยันตัวตน | `LONGCAT_API_KEY`  
API | Chat Completions ที่เข้ากันได้กับ OpenAI  
URL ฐาน | `https://api.longcat.chat/openai`  
โมเดล | `longcat/LongCat-2.0`  
บริบท | 1,048,576 โทเค็น  
เอาต์พุตสูงสุด | 131,072 โทเค็น  
อินพุต | ข้อความ  
  
## ติดตั้ง Plugin

ติดตั้งแพ็กเกจอย่างเป็นทางการ แล้วรีสตาร์ต Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/longcat-provideropenclaw gateway restart
[/code]

## เริ่มต้นใช้งาน

* ### สร้างคีย์ API

ลงชื่อเข้าใช้ [แพลตฟอร์ม LongCat API](<https://longcat.chat/platform/>) และ สร้างคีย์ในหน้า [API Keys](<https://longcat.chat/platform/api_keys>)

* ### เรียกใช้การเริ่มต้นระบบ

bashCopy code
[code]
    openclaw onboard --auth-choice longcat-api-key
[/code]

* ### ตรวจสอบโมเดล

bashCopy code
[code]
    openclaw models list --provider longcat
[/code]

การเริ่มต้นระบบจะเพิ่มแค็ตตาล็อกแบบโฮสต์และเลือก `longcat/LongCat-2.0` เมื่อยัง ไม่ได้กำหนดค่าโมเดลหลักไว้

### การตั้งค่าแบบไม่โต้ตอบ

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice longcat-api-key \  --longcat-api-key "$LONGCAT_API_KEY"
[/code]

## ลักษณะการทำงานของการให้เหตุผล

LongCat มีการควบคุมการคิดแบบเปิดหรือปิด OpenClaw จะแมประดับการคิดที่เปิดใช้งาน ไปยัง `thinking: { type: "enabled" }` และแมป `/think off` ไปยัง `thinking: { type: "disabled" }` ปัจจุบัน LongCat ยังไม่มีเอกสารเกี่ยวกับ `reasoning_effort` ดังนั้น OpenClaw จึงไม่ส่งค่านี้

LongCat ส่งคืนการให้เหตุผลใน `reasoning_content` OpenClaw จะคงฟิลด์ดังกล่าวไว้ เมื่อเล่นซ้ำเทิร์นการเรียกใช้เครื่องมือของผู้ช่วย เพื่อให้เซสชันเอเจนต์แบบหลายเทิร์น ยังคงมีรูปแบบข้อความตามที่ผู้ให้บริการคาดไว้

## ราคา

แค็ตตาล็อกในตัวใช้ราคาตามการใช้งานจริงของ LongCat ในหน่วยดอลลาร์สหรัฐต่อหนึ่งล้าน โทเค็น ได้แก่ อินพุตที่ไม่ใช้แคช $0.75 อินพุตที่ใช้แคช $0.015 และเอาต์พุต $2.95 LongCat อาจเสนอส่วนลดชั่วคราว โดย[หน้าราคา](<https://longcat.chat/platform/docs/Pricing/LongCat-2.0.html>) และบันทึกการเรียกเก็บเงินของคุณถือเป็นข้อมูลอ้างอิงที่เชื่อถือได้

## LongCat-2.0 ที่โฮสต์ด้วยตนเอง

ผู้ให้บริการ `longcat` มีเป้าหมายสำหรับ API แบบโฮสต์ของ LongCat สำหรับน้ำหนักโมเดลแบบเปิดบน [Hugging Face](<https://huggingface.co/meituan-longcat/LongCat-2.0>) ให้บริการ โมเดลผ่านรันไทม์ที่เข้ากันได้กับ OpenAI และใช้ผู้ให้บริการ [vLLM](</th/providers/vllm>) หรือ [SGLang](</th/providers/sglang>) ที่มีอยู่แล้วของ OpenClaw แทน

เก็บตัวระบุโมเดลที่ตรงกับรันไทม์ไว้ในแค็ตตาล็อกของผู้ให้บริการที่โฮสต์ด้วยตนเอง อย่ากำหนดเส้นทางการติดตั้งใช้งานภายในเครื่องผ่าน `longcat/LongCat-2.0`

## การแก้ไขปัญหา

คีย์ใช้งานได้ในเชลล์ แต่ใช้ไม่ได้ใน Gateway

กระบวนการ Gateway ที่จัดการโดยดีมอนจะไม่ได้รับตัวแปรทุกตัวจากเชลล์แบบโต้ตอบ ใส่ `LONGCAT_API_KEY` ใน `~/.openclaw/.env` กำหนดค่าผ่าน การเริ่มต้นระบบ หรือใช้ข้อมูลอ้างอิงข้อมูลลับที่ได้รับอนุมัติ

คำขอล้มเหลวด้วยรหัส 402 หรือ 429

`402` หมายถึงบัญชีมีโควตาโทเค็นไม่เพียงพอ `429` หมายถึงคีย์ API ใช้งานถึงขีดจำกัดอัตราแล้ว ตรวจสอบ[การใช้งาน LongCat](<https://longcat.chat/platform/usage>) และลองส่งคำขอที่ถูกจำกัดอัตราอีกครั้งหลังพ้นช่วงหน่วงเวลาของผู้ให้บริการ

โมเดลไม่ปรากฏ

เรียกใช้ `openclaw plugins list` และยืนยันว่า Plugin `longcat` เปิดใช้งานอยู่ จากนั้นเรียกใช้ `openclaw models list --provider longcat`

## เนื้อหาที่เกี่ยวข้อง

[**ผู้ให้บริการโมเดล** การกำหนดค่าผู้ให้บริการ ข้อมูลอ้างอิงโมเดล และลักษณะการทำงานเมื่อสลับไปใช้ระบบสำรอง ](</th/concepts/model-providers>) [**เอกสาร LongCat API** เอนด์พอยต์ API แบบโฮสต์ การยืนยันตัวตน ขีดจำกัด และตัวอย่าง ](<https://longcat.chat/platform/docs/>) [**การ์ดโมเดล LongCat-2.0** สถาปัตยกรรม แนวทางการติดตั้งใช้งาน และรายละเอียดของโมเดล ](<https://huggingface.co/meituan-longcat/LongCat-2.0>) [**ข้อมูลลับ** จัดเก็บข้อมูลรับรองของผู้ให้บริการโดยไม่ฝังข้อความธรรมดาไว้ในการกำหนดค่า ](</th/gateway/secrets>)

Was this useful?YesNo

Open issue