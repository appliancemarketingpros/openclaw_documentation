---
title: Ollama
source_url: https://docs.openclaw.ai/th/providers/ollama
scraped_at: 2026-05-25
---

OpenClaw ผสานรวมกับ API แบบเนทีฟของ Ollama (`/api/chat`) สำหรับโมเดลคลาวด์แบบโฮสต์และเซิร์ฟเวอร์ Ollama แบบ local/self-hosted คุณสามารถใช้ Ollama ได้สามโหมด: `Cloud + Local` ผ่านโฮสต์ Ollama ที่เข้าถึงได้, `Cloud only` กับ `https://ollama.com`, หรือ `Local only` กับโฮสต์ Ollama ที่เข้าถึงได้

การตั้งค่าผู้ให้บริการ Ollama ใช้ `baseUrl` เป็นคีย์หลัก OpenClaw ยังยอมรับ `baseURL` เพื่อความเข้ากันได้กับตัวอย่างสไตล์ OpenAI SDK แต่การตั้งค่าใหม่ควรใช้ `baseUrl`

## กฎการยืนยันตัวตน

โฮสต์ Local และ LAN

โฮสต์ Ollama แบบ local และ LAN ไม่จำเป็นต้องมี bearer token จริง OpenClaw ใช้ตัวทำเครื่องหมาย local `ollama-local` เฉพาะกับ URL ฐานของ Ollama แบบ loopback, เครือข่ายส่วนตัว, `.local` และชื่อโฮสต์เปล่าเท่านั้น

โฮสต์ระยะไกลและ Ollama Cloud

โฮสต์สาธารณะระยะไกลและ Ollama Cloud (`https://ollama.com`) ต้องใช้ข้อมูลรับรองจริงผ่าน `OLLAMA_API_KEY`, โปรไฟล์การยืนยันตัวตน หรือ `apiKey` ของผู้ให้บริการ

ID ผู้ให้บริการแบบกำหนดเอง

ID ผู้ให้บริการแบบกำหนดเองที่ตั้งค่า `api: "ollama"` จะทำตามกฎเดียวกัน ตัวอย่างเช่น ผู้ให้บริการ `ollama-remote` ที่ชี้ไปยังโฮสต์ Ollama บน LAN ส่วนตัวสามารถใช้ `apiKey: "ollama-local"` ได้ และ sub-agent จะ resolve ตัวทำเครื่องหมายนั้นผ่าน hook ของผู้ให้บริการ Ollama แทนที่จะถือว่าเป็นข้อมูลรับรองที่หายไป การค้นหาหน่วยความจำยังสามารถตั้งค่า `agents.defaults.memorySearch.provider` เป็น ID ผู้ให้บริการแบบกำหนดเองนั้น เพื่อให้ embeddings ใช้ endpoint Ollama ที่ตรงกัน

โปรไฟล์การยืนยันตัวตน

`auth-profiles.json` เก็บข้อมูลรับรองสำหรับ ID ผู้ให้บริการ ใส่การตั้งค่า endpoint (`baseUrl`, `api`, ID โมเดล, headers, timeouts) ไว้ใน `models.providers.<id>` ไฟล์ auth-profile แบบ flat รุ่นเก่า เช่น `{ "ollama-windows": { "apiKey": "ollama-local" } }` ไม่ใช่รูปแบบ runtime ให้รัน `openclaw doctor --fix` เพื่อเขียนใหม่เป็นโปรไฟล์ API-key แบบ canonical `ollama-windows:default` พร้อมสำรองข้อมูล `baseUrl` ในไฟล์นั้นเป็น noise เพื่อความเข้ากันได้ และควรย้ายไปยังการตั้งค่าผู้ให้บริการ

ขอบเขต embedding ของหน่วยความจำ

เมื่อใช้ Ollama สำหรับ embeddings ของหน่วยความจำ การยืนยันตัวตนแบบ bearer จะถูกจำกัดขอบเขตไว้ที่โฮสต์ที่ประกาศไว้:

  * คีย์ระดับผู้ให้บริการจะถูกส่งไปยังโฮสต์ Ollama ของผู้ให้บริการนั้นเท่านั้น
  * `agents.*.memorySearch.remote.apiKey` จะถูกส่งไปยังโฮสต์ embedding ระยะไกลของมันเท่านั้น
  * ค่า env `OLLAMA_API_KEY` ล้วนจะถูกถือเป็น convention ของ Ollama Cloud และโดยค่าเริ่มต้นจะไม่ถูกส่งไปยังโฮสต์ local หรือ self-hosted


## เริ่มต้นใช้งาน

เลือกวิธีตั้งค่าและโหมดที่คุณต้องการ

### Onboarding (แนะนำ)

**เหมาะสำหรับ:** เส้นทางที่เร็วที่สุดสู่การตั้งค่า Ollama cloud หรือ local ที่ใช้งานได้

* ### รัน onboarding

bashCopy code
[code]
    openclaw onboard
[/code]

เลือก **Ollama** จากรายการผู้ให้บริการ

* ### เลือกโหมดของคุณ

  * **Cloud + Local** — โฮสต์ Ollama แบบ local พร้อมโมเดลคลาวด์ที่ route ผ่านโฮสต์นั้น
  * **Cloud only** — โมเดล Ollama แบบโฮสต์ผ่าน `https://ollama.com`
  * **Local only** — โมเดล local เท่านั้น


* ### เลือกโมเดล

`Cloud only` จะขอ `OLLAMA_API_KEY` และแนะนำค่าเริ่มต้นของคลาวด์แบบโฮสต์ `Cloud + Local` และ `Local only` จะขอ URL ฐานของ Ollama, ค้นหาโมเดลที่มีอยู่ และ pull โมเดล local ที่เลือกให้อัตโนมัติหากยังไม่มี เมื่อ Ollama รายงานแท็ก `:latest` ที่ติดตั้งแล้ว เช่น `gemma4:latest` การตั้งค่าจะแสดงโมเดลที่ติดตั้งแล้วนั้นเพียงครั้งเดียว แทนที่จะแสดงทั้ง `gemma4` และ `gemma4:latest` หรือ pull alias เปล่าอีกครั้ง `Cloud + Local` ยังตรวจสอบด้วยว่าโฮสต์ Ollama นั้นลงชื่อเข้าใช้เพื่อเข้าถึงคลาวด์แล้วหรือไม่

* ### ตรวจสอบว่าโมเดลพร้อมใช้งาน

bashCopy code
[code]
    openclaw models list --provider ollama
[/code]

### โหมดไม่โต้ตอบ

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice ollama \  --accept-risk
[/code]

ระบุ URL ฐานหรือโมเดลแบบกำหนดเองได้ตามต้องการ:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice ollama \  --custom-base-url "http://ollama-host:11434" \  --custom-model-id "qwen3.5:27b" \  --accept-risk
[/code]

### ตั้งค่าด้วยตนเอง

**เหมาะสำหรับ:** การควบคุมการตั้งค่าคลาวด์หรือ local อย่างเต็มที่

* ### เลือกคลาวด์หรือ local

  * **Cloud + Local** : ติดตั้ง Ollama, ลงชื่อเข้าใช้ด้วย `ollama signin` และ route คำขอคลาวด์ผ่านโฮสต์นั้น
  * **Cloud only** : ใช้ `https://ollama.com` พร้อม `OLLAMA_API_KEY`
  * **Local only** : ติดตั้ง Ollama จาก [ollama.com/download](<https://ollama.com/download>)


* ### Pull โมเดล local (เฉพาะ local)

bashCopy code
[code]
    ollama pull gemma4# orollama pull gpt-oss:20b# orollama pull llama3.3
[/code]

* ### เปิดใช้ Ollama สำหรับ OpenClaw

สำหรับ `Cloud only` ให้ใช้ `OLLAMA_API_KEY` จริงของคุณ สำหรับการตั้งค่าที่มีโฮสต์รองรับ ค่า placeholder ใดก็ใช้ได้:

bashCopy code
[code]
    # Cloudexport OLLAMA_API_KEY="your-ollama-api-key" # Local-onlyexport OLLAMA_API_KEY="ollama-local" # Or configure in your config fileopenclaw config set models.providers.ollama.apiKey "OLLAMA_API_KEY"
[/code]

* ### ตรวจดูและตั้งค่าโมเดลของคุณ

bashCopy code
[code]
    openclaw models listopenclaw models set ollama/gemma4
[/code]

หรือกำหนดค่าเริ่มต้นใน config:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "ollama/gemma4" },    },  },}
[/code]

## โมเดลคลาวด์

### Cloud + Local

`Cloud + Local` ใช้โฮสต์ Ollama ที่เข้าถึงได้เป็นจุดควบคุมสำหรับทั้งโมเดล local และโมเดลคลาวด์ นี่คือ flow แบบไฮบริดที่ Ollama แนะนำ

ใช้ **Cloud + Local** ระหว่างการตั้งค่า OpenClaw จะขอ URL ฐานของ Ollama, ค้นหาโมเดล local จากโฮสต์นั้น และตรวจสอบว่าโฮสต์ลงชื่อเข้าใช้เพื่อเข้าถึงคลาวด์ด้วย `ollama signin` แล้วหรือไม่ เมื่อโฮสต์ลงชื่อเข้าใช้แล้ว OpenClaw ยังจะแนะนำค่าเริ่มต้นของคลาวด์แบบโฮสต์ เช่น `kimi-k2.5:cloud`, `minimax-m2.7:cloud` และ `glm-5.1:cloud`

หากโฮสต์ยังไม่ได้ลงชื่อเข้าใช้ OpenClaw จะคงการตั้งค่าเป็น local-only จนกว่าคุณจะรัน `ollama signin`

### Cloud only

`Cloud only` รันกับ API แบบโฮสต์ของ Ollama ที่ `https://ollama.com`

ใช้ **Cloud only** ระหว่างการตั้งค่า OpenClaw จะขอ `OLLAMA_API_KEY`, ตั้งค่า `baseUrl: "https://ollama.com"` และ seed รายการโมเดลคลาวด์แบบโฮสต์ เส้นทางนี้ **ไม่** ต้องใช้เซิร์ฟเวอร์ Ollama แบบ local หรือ `ollama signin`

รายการโมเดลคลาวด์ที่แสดงระหว่าง `openclaw onboard` จะถูกเติมแบบ live จาก `https://ollama.com/api/tags` โดยจำกัดไว้ที่ 500 รายการ ดังนั้นตัวเลือกจึงสะท้อน catalog แบบโฮสต์ปัจจุบันแทนที่จะเป็น seed แบบคงที่ หาก `ollama.com` เข้าถึงไม่ได้หรือไม่คืนโมเดลระหว่างการตั้งค่า OpenClaw จะ fallback ไปยังคำแนะนำ hardcoded ก่อนหน้า เพื่อให้ onboarding ยังเสร็จสมบูรณ์

### Local only

ในโหมด local-only OpenClaw จะค้นหาโมเดลจาก instance Ollama ที่ตั้งค่าไว้ เส้นทางนี้สำหรับเซิร์ฟเวอร์ Ollama แบบ local หรือ self-hosted

ปัจจุบัน OpenClaw แนะนำ `gemma4` เป็นค่าเริ่มต้นสำหรับ local

## การค้นหาโมเดล (ผู้ให้บริการโดยนัย)

เมื่อคุณตั้งค่า `OLLAMA_API_KEY` (หรือโปรไฟล์การยืนยันตัวตน) และ **ไม่ได้** กำหนด `models.providers.ollama` หรือผู้ให้บริการระยะไกลแบบกำหนดเองอื่นที่มี `api: "ollama"` OpenClaw จะค้นหาโมเดลจาก instance Ollama แบบ local ที่ `http://127.0.0.1:11434`

พฤติกรรม | รายละเอียด  
---|---  
คำขอ catalog | คิวรี `/api/tags`  
การตรวจหาความสามารถ | ใช้การ lookup `/api/show` แบบ best-effort เพื่ออ่าน `contextWindow`, พารามิเตอร์ Modelfile `num_ctx` ที่ขยายแล้ว และความสามารถรวมถึง vision/tools  
โมเดล Vision | โมเดลที่มีความสามารถ `vision` ที่รายงานโดย `/api/show` จะถูกทำเครื่องหมายว่ารองรับรูปภาพ (`input: ["text", "image"]`) ดังนั้น OpenClaw จะ inject รูปภาพเข้า prompt โดยอัตโนมัติ  
การตรวจหา Reasoning | ใช้ความสามารถจาก `/api/show` เมื่อมี รวมถึง `thinking`; fallback ไปยัง heuristic ตามชื่อโมเดล (`r1`, `reasoning`, `think`) เมื่อ Ollama ไม่ส่งความสามารถ  
ขีดจำกัด token | ตั้งค่า `maxTokens` เป็นเพดาน max-token เริ่มต้นของ Ollama ที่ OpenClaw ใช้  
ค่าใช้จ่าย | ตั้งค่าค่าใช้จ่ายทั้งหมดเป็น `0`  
  
วิธีนี้ช่วยหลีกเลี่ยงรายการโมเดลแบบ manual ขณะยังรักษา catalog ให้ตรงกับ instance Ollama แบบ local คุณสามารถใช้ ref แบบเต็ม เช่น `ollama/<pulled-model>:latest` ใน local `infer model run`; OpenClaw จะ resolve โมเดลที่ติดตั้งแล้วนั้นจาก catalog live ของ Ollama โดยไม่ต้องมีรายการ `models.json` ที่เขียนด้วยมือ

สำหรับโฮสต์ Ollama ที่ลงชื่อเข้าใช้แล้ว โมเดล `:cloud` บางตัวอาจใช้งานได้ผ่าน `/api/chat` และ `/api/show` ก่อนที่จะปรากฏใน `/api/tags` เมื่อคุณเลือก ref เต็ม `ollama/<model>:cloud` อย่างชัดเจน OpenClaw จะตรวจสอบโมเดลที่หายไปนั้นแบบตรงตัวด้วย `/api/show` และเพิ่มเข้า runtime catalog เฉพาะเมื่อ Ollama ยืนยัน metadata ของโมเดลเท่านั้น การพิมพ์ผิดยังคงล้มเหลวเป็นโมเดลที่ไม่รู้จัก แทนที่จะถูกสร้างอัตโนมัติ

bashCopy code
[code]
    # See what models are availableollama listopenclaw models list
[/code]

สำหรับ smoke test การสร้างข้อความแบบแคบที่หลีกเลี่ยง surface เครื่องมือ agent ทั้งหมด ให้ใช้ local `infer model run` พร้อม ref โมเดล Ollama แบบเต็ม:

bashCopy code
[code]
    OLLAMA_API_KEY=ollama-local \  openclaw infer model run \    --local \    --model ollama/llama3.2:latest \    --prompt "Reply with exactly: pong" \    --json
[/code]

เส้นทางนั้นยังคงใช้ผู้ให้บริการ การยืนยันตัวตน และ transport Ollama แบบเนทีฟ ที่ OpenClaw ตั้งค่าไว้ แต่จะไม่เริ่ม turn ของ chat-agent หรือโหลด context ของ MCP/เครื่องมือ หาก สำเร็จในขณะที่การตอบกลับของ agent ปกติล้มเหลว ให้แก้ปัญหาความจุด้าน prompt/เครื่องมือของ agent ของโมเดลเป็นลำดับถัดไป

สำหรับ smoke test โมเดล vision แบบแคบบนเส้นทาง lean เดียวกัน ให้เพิ่มไฟล์รูปภาพหนึ่งไฟล์หรือมากกว่า ลงใน `infer model run` วิธีนี้จะส่ง prompt และรูปภาพโดยตรงไปยัง โมเดล vision ของ Ollama ที่เลือก โดยไม่โหลดเครื่องมือแชต หน่วยความจำ หรือ context เซสชันก่อนหน้า:

bashCopy code
[code]
    OLLAMA_API_KEY=ollama-local \  openclaw infer model run \    --local \    --model ollama/qwen2.5vl:7b \    --prompt "Describe this image in one sentence." \    --file ./photo.jpg \    --json
[/code]

`model run --file` ยอมรับไฟล์ที่ตรวจพบเป็น `image/*` รวมถึง input PNG, JPEG และ WebP ทั่วไป ไฟล์ที่ไม่ใช่รูปภาพจะถูกปฏิเสธก่อนเรียก Ollama สำหรับการรู้จำเสียง ให้ใช้ `openclaw infer audio transcribe` แทน

เมื่อคุณสลับ conversation ด้วย `/model ollama/<model>` OpenClaw จะถือว่า เป็นการเลือกของผู้ใช้อย่างตรงตัว หาก `baseUrl` ของ Ollama ที่ตั้งค่าไว้ เข้าถึงไม่ได้ การตอบกลับถัดไปจะล้มเหลวด้วย error ของผู้ให้บริการ แทนที่จะตอบ จากโมเดล fallback อื่นที่ตั้งค่าไว้อย่างเงียบๆ

งาน Cron แบบแยกโดดเดี่ยวจะทำการตรวจสอบความปลอดภัยในเครื่องเพิ่มอีกหนึ่งขั้นก่อนเริ่มรอบของเอเจนต์ หากโมเดลที่เลือกแก้ค่าไปเป็นผู้ให้บริการ Ollama แบบโลคัล เครือข่ายส่วนตัว หรือ `.local` และไม่สามารถเข้าถึง `/api/tags` ได้ OpenClaw จะบันทึกการรัน Cron นั้นเป็น `skipped` พร้อม `ollama/<model>` ที่เลือกไว้ในข้อความข้อผิดพลาด การตรวจล่วงหน้าของเอนด์พอยต์จะถูกแคชไว้ 5 นาที ดังนั้นงาน Cron หลายงานที่ชี้ไปยังดีมอน Ollama ตัวเดียวกันที่หยุดอยู่จะไม่เริ่มคำขอโมเดลที่ล้มเหลวทั้งหมดพร้อมกัน

ตรวจสอบแบบสดสำหรับเส้นทางข้อความโลคัล เส้นทางสตรีมเนทีฟ และ embeddings กับ Ollama โลคัลด้วย:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_OLLAMA=1 OPENCLAW_LIVE_OLLAMA_WEB_SEARCH=0 \  pnpm test:live -- extensions/ollama/ollama.live.test.ts
[/code]

หากต้องการเพิ่มโมเดลใหม่ ให้ดึงโมเดลนั้นด้วย Ollama ได้โดยตรง:

bashCopy code
[code]
    ollama pull mistral
[/code]

โมเดลใหม่จะถูกค้นพบโดยอัตโนมัติและพร้อมใช้งาน

## วิชันและคำอธิบายรูปภาพ

Plugin Ollama ที่รวมมาให้จะลงทะเบียน Ollama เป็นผู้ให้บริการทำความเข้าใจสื่อที่รองรับรูปภาพ ซึ่งทำให้ OpenClaw สามารถส่งต่อคำขอคำอธิบายรูปภาพแบบชัดเจนและค่าเริ่มต้นของโมเดลรูปภาพที่กำหนดค่าไว้ผ่านโมเดลวิชันของ Ollama แบบโลคัลหรือแบบโฮสต์ได้

สำหรับวิชันโลคัล ให้ดึงโมเดลที่รองรับรูปภาพ:

bashCopy code
[code]
    ollama pull qwen2.5vl:7bexport OLLAMA_API_KEY="ollama-local"
[/code]

จากนั้นตรวจสอบด้วย infer CLI:

bashCopy code
[code]
    openclaw infer image describe \  --file ./photo.jpg \  --model ollama/qwen2.5vl:7b \  --json
[/code]

`--model` ต้องเป็นอ้างอิง `<provider/model>` แบบเต็ม เมื่อมีการตั้งค่าไว้ `openclaw infer image describe` จะรันโมเดลนั้นโดยตรง แทนที่จะข้ามคำอธิบายเพราะโมเดลรองรับวิชันแบบเนทีฟ

ใช้ `infer image describe` เมื่อคุณต้องการโฟลว์ผู้ให้บริการทำความเข้าใจรูปภาพของ OpenClaw, `agents.defaults.imageModel` ที่กำหนดค่าไว้ และรูปแบบเอาต์พุตคำอธิบายรูปภาพ ใช้ `infer model run --file` เมื่อคุณต้องการตรวจสอบโมเดลมัลติโมดัลแบบดิบด้วยพรอมป์แบบกำหนดเองและรูปภาพหนึ่งรูปหรือมากกว่า

หากต้องการทำให้ Ollama เป็นโมเดลทำความเข้าใจรูปภาพเริ่มต้นสำหรับสื่อขาเข้า ให้กำหนดค่า `agents.defaults.imageModel`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageModel: {        primary: "ollama/qwen2.5vl:7b",      },    },  },}
[/code]

ควรใช้อ้างอิง `ollama/<model>` แบบเต็ม หากโมเดลเดียวกันถูกระบุไว้ใต้ `models.providers.ollama.models` พร้อม `input: ["text", "image"]` และไม่มีผู้ให้บริการรูปภาพอื่นที่กำหนดค่าไว้เปิดเผย ID โมเดลเปล่าเดียวกันนั้น OpenClaw จะปรับอ้างอิง `imageModel` แบบเปล่า เช่น `qwen2.5vl:7b` ให้เป็น `ollama/qwen2.5vl:7b` ด้วย หากมีผู้ให้บริการรูปภาพที่กำหนดค่าไว้มากกว่าหนึ่งรายมี ID เปล่าเดียวกัน ให้ใช้คำนำหน้าผู้ให้บริการอย่างชัดเจน

โมเดลวิชันโลคัลที่ช้าอาจต้องใช้เวลาหมดเวลาของการทำความเข้าใจรูปภาพนานกว่าโมเดลคลาวด์ โมเดลเหล่านี้ยังอาจล่มหรือหยุดเมื่อ Ollama พยายามจัดสรรคอนเท็กซ์วิชันเต็มตามที่ประกาศไว้บนฮาร์ดแวร์ที่มีข้อจำกัด ตั้งค่าเวลาหมดเวลาของความสามารถ และจำกัด `num_ctx` ในรายการโมเดลเมื่อคุณต้องการเพียงรอบคำอธิบายรูปภาพปกติ:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        models: [          {            id: "qwen2.5vl:7b",            name: "qwen2.5vl:7b",            input: ["text", "image"],            params: { num_ctx: 2048, keep_alive: "1m" },          },        ],      },    },  },  tools: {    media: {      image: {        timeoutSeconds: 180,        models: [{ provider: "ollama", model: "qwen2.5vl:7b", timeoutSeconds: 300 }],      },    },  },}
[/code]

เวลาหมดเวลานี้มีผลกับการทำความเข้าใจรูปภาพขาเข้าและเครื่องมือ `image` แบบชัดเจนที่เอเจนต์สามารถเรียกใช้ระหว่างรอบได้ `models.providers.ollama.timeoutSeconds` ระดับผู้ให้บริการยังคงควบคุมตัวป้องกันคำขอ HTTP ของ Ollama พื้นฐานสำหรับการเรียกโมเดลปกติ

ตรวจสอบแบบสดสำหรับเครื่องมือรูปภาพแบบชัดเจนกับ Ollama โลคัลด้วย:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_OLLAMA_IMAGE=1 \  pnpm test:live -- src/agents/tools/image-tool.ollama.live.test.ts
[/code]

หากคุณกำหนด `models.providers.ollama.models` ด้วยตนเอง ให้ทำเครื่องหมายโมเดลวิชันว่ารองรับอินพุตรูปภาพ:

json5Copy code
[code]
    {  id: "qwen2.5vl:7b",  name: "qwen2.5vl:7b",  input: ["text", "image"],  contextWindow: 128000,  maxTokens: 8192,}
[/code]

OpenClaw จะปฏิเสธคำขอคำอธิบายรูปภาพสำหรับโมเดลที่ไม่ได้ทำเครื่องหมายว่ารองรับรูปภาพ เมื่อใช้การค้นพบโดยนัย OpenClaw จะอ่านข้อมูลนี้จาก Ollama เมื่อ `/api/show` รายงานความสามารถด้านวิชัน

## การกำหนดค่า

### Basic (implicit discovery)

เส้นทางเปิดใช้งานเฉพาะโลคัลที่ง่ายที่สุดคือผ่านตัวแปรสภาพแวดล้อม:

bashCopy code
[code]
    export OLLAMA_API_KEY="ollama-local"
[/code]

### Explicit (manual models)

ใช้การกำหนดค่าแบบชัดเจนเมื่อคุณต้องการตั้งค่าคลาวด์แบบโฮสต์, Ollama ทำงานบนโฮสต์/พอร์ตอื่น, คุณต้องการบังคับหน้าต่างคอนเท็กซ์หรือรายการโมเดลเฉพาะ, หรือคุณต้องการนิยามโมเดลด้วยตนเองทั้งหมด

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",        api: "ollama",        models: [          {            id: "kimi-k2.5:cloud",            name: "kimi-k2.5:cloud",            reasoning: false,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192          }        ]      }    }  }}
[/code]

### Custom base URL

หาก Ollama ทำงานบนโฮสต์หรือพอร์ตอื่น (การกำหนดค่าแบบชัดเจนจะปิดการค้นพบอัตโนมัติ ดังนั้นให้กำหนดโมเดลด้วยตนเอง):

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        apiKey: "ollama-local",        baseUrl: "http://ollama-host:11434", // No /v1 - use native Ollama API URL        api: "ollama", // Set explicitly to guarantee native tool-calling behavior        timeoutSeconds: 300, // Optional: give cold local models longer to connect and stream        models: [          {            id: "qwen3:32b",            name: "qwen3:32b",            params: {              keep_alive: "15m", // Optional: keep the model loaded between turns            },          },        ],      },    },  },}
[/code]

## สูตรที่ใช้บ่อย

ใช้สิ่งเหล่านี้เป็นจุดเริ่มต้นและแทนที่ ID โมเดลด้วยชื่อที่ตรงจาก `ollama list` หรือ `openclaw models list --provider ollama`

Local model with auto-discovery

ใช้สิ่งนี้เมื่อ Ollama ทำงานบนเครื่องเดียวกับ Gateway และคุณต้องการให้ OpenClaw ค้นหาโมเดลที่ติดตั้งไว้โดยอัตโนมัติ

bashCopy code
[code]
    ollama serveollama pull gemma4export OLLAMA_API_KEY="ollama-local"openclaw models list --provider ollamaopenclaw models set ollama/gemma4
[/code]

เส้นทางนี้ทำให้การกำหนดค่ามีน้อยที่สุด อย่าเพิ่มบล็อก `models.providers.ollama` เว้นแต่คุณต้องการกำหนดโมเดลด้วยตนเอง

LAN Ollama host with manual models

ใช้ URL ของ Ollama แบบเนทีฟสำหรับโฮสต์ LAN อย่าเพิ่ม `/v1`

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://gpu-box.local:11434",        apiKey: "ollama-local",        api: "ollama",        timeoutSeconds: 300,        contextWindow: 32768,        maxTokens: 8192,        models: [          {            id: "qwen3.5:9b",            name: "qwen3.5:9b",            reasoning: true,            input: ["text"],            params: {              num_ctx: 32768,              thinking: false,              keep_alive: "15m",            },          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "ollama/qwen3.5:9b" },    },  },}
[/code]

`contextWindow` คือคอนเท็กซ์บัดเจ็ตฝั่ง OpenClaw ส่วน `params.num_ctx` จะถูกส่งไปยัง Ollama สำหรับคำขอ จัดให้สองค่านี้ตรงกันเมื่อฮาร์ดแวร์ของคุณไม่สามารถรันคอนเท็กซ์เต็มตามที่โมเดลประกาศไว้ได้

Ollama Cloud only

ใช้สิ่งนี้เมื่อคุณไม่ได้รันดีมอนโลคัลและต้องการใช้โมเดล Ollama แบบโฮสต์โดยตรง

bashCopy code
[code]
    export OLLAMA_API_KEY="your-ollama-api-key"
[/code]

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",        api: "ollama",        models: [          {            id: "kimi-k2.5:cloud",            name: "kimi-k2.5:cloud",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "ollama/kimi-k2.5:cloud" },    },  },}
[/code]

Cloud plus local through a signed-in daemon

ใช้สิ่งนี้เมื่อดีมอน Ollama แบบโลคัลหรือ LAN ลงชื่อเข้าใช้ด้วย `ollama signin` และควรให้บริการทั้งโมเดลโลคัลและโมเดล `:cloud`

bashCopy code
[code]
    ollama signinollama pull gemma4
[/code]

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://127.0.0.1:11434",        apiKey: "ollama-local",        api: "ollama",        timeoutSeconds: 300,        models: [          { id: "gemma4", name: "gemma4", input: ["text"] },          { id: "kimi-k2.5:cloud", name: "kimi-k2.5:cloud", input: ["text", "image"] },        ],      },    },  },  agents: {    defaults: {      model: {        primary: "ollama/gemma4",        fallbacks: ["ollama/kimi-k2.5:cloud"],      },    },  },}
[/code]

Multiple Ollama hosts

ใช้ ID ผู้ให้บริการแบบกำหนดเองเมื่อคุณมีเซิร์ฟเวอร์ Ollama มากกว่าหนึ่งเครื่อง ผู้ให้บริการแต่ละรายจะมีโฮสต์ โมเดล การตรวจสอบสิทธิ์ เวลาหมดเวลา และอ้างอิงโมเดลของตนเอง

json5Copy code
[code]
    {  models: {    providers: {      "ollama-fast": {        baseUrl: "http://mini.local:11434",        apiKey: "ollama-local",        api: "ollama",        contextWindow: 32768,        models: [{ id: "gemma4", name: "gemma4", input: ["text"] }],      },      "ollama-large": {        baseUrl: "http://gpu-box.local:11434",        apiKey: "ollama-local",        api: "ollama",        timeoutSeconds: 420,        contextWindow: 131072,        maxTokens: 16384,        models: [{ id: "qwen3.5:27b", name: "qwen3.5:27b", input: ["text"] }],      },    },  },  agents: {    defaults: {      model: {        primary: "ollama-fast/gemma4",        fallbacks: ["ollama-large/qwen3.5:27b"],      },    },  },}
[/code]

เมื่อ OpenClaw ส่งคำขอ คำนำหน้าผู้ให้บริการที่ใช้งานอยู่จะถูกตัดออก ดังนั้น `ollama-large/qwen3.5:27b` จะไปถึง Ollama เป็น `qwen3.5:27b`

Lean local model profile

โมเดลโลคัลบางตัวอาจตอบพรอมป์ง่าย ๆ ได้ แต่มีปัญหากับพื้นผิวเครื่องมือเอเจนต์เต็มรูปแบบ เริ่มด้วยการจำกัดเครื่องมือและคอนเท็กซ์ก่อนเปลี่ยนการตั้งค่ารันไทม์ส่วนกลาง

json5Copy code
[code]
    {  agents: {    defaults: {      experimental: {        localModelLean: true,      },      model: { primary: "ollama/gemma4" },    },  },  models: {    providers: {      ollama: {        baseUrl: "http://127.0.0.1:11434",        apiKey: "ollama-local",        api: "ollama",        contextWindow: 32768,        models: [          {            id: "gemma4",            name: "gemma4",            input: ["text"],            params: { num_ctx: 32768 },            compat: { supportsTools: false },          },        ],      },    },  },}
[/code]

ใช้ `compat.supportsTools: false` เฉพาะเมื่อโมเดลหรือเซิร์ฟเวอร์ล้มเหลวกับสคีมาของเครื่องมืออย่างเชื่อถือได้เท่านั้น การตั้งค่านี้แลกความสามารถของเอเจนต์กับความเสถียร `localModelLean` จะนำเครื่องมือเบราว์เซอร์, cron และข้อความออกจากพื้นผิวของเอเจนต์ แต่จะไม่เปลี่ยน context รันไทม์หรือโหมดการคิดของ Ollama จับคู่กับ `params.num_ctx` และ `params.thinking: false` ที่ระบุชัดเจนสำหรับโมเดลคิดแบบ Qwen ขนาดเล็กที่วนซ้ำหรือใช้โควตาการตอบสนองไปกับการให้เหตุผลที่ซ่อนอยู่

### การเลือกโมเดล

เมื่อกำหนดค่าแล้ว โมเดล Ollama ทั้งหมดของคุณจะพร้อมใช้งาน:

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "ollama/gpt-oss:20b",        fallbacks: ["ollama/llama3.3", "ollama/qwen2.5-coder:32b"],      },    },  },}
[/code]

รองรับรหัสผู้ให้บริการ Ollama แบบกำหนดเองด้วยเช่นกัน เมื่อการอ้างอิงโมเดลใช้ prefix ของผู้ให้บริการที่ใช้งานอยู่ เช่น `ollama-spark/qwen3:32b` OpenClaw จะตัดเฉพาะ prefix นั้นออกก่อนเรียก Ollama เพื่อให้เซิร์ฟเวอร์ได้รับ `qwen3:32b`

สำหรับโมเดลโลคัลที่ช้า ควรปรับแต่งคำขอในขอบเขตผู้ให้บริการก่อนเพิ่ม timeout รันไทม์ของเอเจนต์ทั้งหมด:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        timeoutSeconds: 300,        models: [          {            id: "gemma4:26b",            name: "gemma4:26b",            params: { keep_alive: "15m" },          },        ],      },    },  },}
[/code]

`timeoutSeconds` ใช้กับคำขอ HTTP ของโมเดล รวมถึงการตั้งค่าการเชื่อมต่อ, headers, การสตรีม body และการยกเลิก guarded-fetch โดยรวม `params.keep_alive` จะถูกส่งต่อไปยัง Ollama เป็น `keep_alive` ระดับบนสุดในคำขอ `/api/chat` แบบ native; ตั้งค่ารายโมเดลเมื่อเวลาโหลดในเทิร์นแรกเป็นคอขวด

### การตรวจสอบอย่างรวดเร็ว

bashCopy code
[code]
    # Ollama daemon visible to this machinecurl http://127.0.0.1:11434/api/tags # OpenClaw catalog and selected modelopenclaw models list --provider ollamaopenclaw models status # Direct model smokeopenclaw infer model run \  --model ollama/gemma4 \  --prompt "Reply with exactly: ok"
[/code]

สำหรับโฮสต์ระยะไกล ให้แทนที่ `127.0.0.1` ด้วยโฮสต์ที่ใช้ใน `baseUrl` หาก `curl` ใช้งานได้แต่ OpenClaw ใช้งานไม่ได้ ให้ตรวจสอบว่า Gateway รันอยู่บนเครื่อง คอนเทนเนอร์ หรือบัญชีบริการอื่นหรือไม่

## Ollama Web Search

OpenClaw รองรับ **Ollama Web Search** เป็นผู้ให้บริการ `web_search` ที่รวมมาในชุด

คุณสมบัติ | รายละเอียด  
---|---  
โฮสต์ | ใช้โฮสต์ Ollama ที่คุณกำหนดค่าไว้ (`models.providers.ollama.baseUrl` เมื่อตั้งค่าไว้ มิฉะนั้นใช้ `http://127.0.0.1:11434`); `https://ollama.com` ใช้ API ที่โฮสต์โดยตรง  
การยืนยันตัวตน | ไม่ต้องใช้คีย์สำหรับโฮสต์ Ollama โลคัลที่ลงชื่อเข้าใช้แล้ว; ใช้ `OLLAMA_API_KEY` หรือการยืนยันตัวตนของผู้ให้บริการที่กำหนดค่าไว้สำหรับการค้นหาโดยตรงผ่าน `https://ollama.com` หรือโฮสต์ที่ป้องกันด้วยการยืนยันตัวตน  
ข้อกำหนด | โฮสต์โลคัล/โฮสต์เองต้องกำลังรันและลงชื่อเข้าใช้ด้วย `ollama signin`; การค้นหาผ่านโฮสต์โดยตรงต้องใช้ `baseUrl: "https://ollama.com"` พร้อมคีย์ Ollama API จริง  
  
เลือก **Ollama Web Search** ระหว่าง `openclaw onboard` หรือ `openclaw configure --section web` หรือตั้งค่า:

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

สำหรับการค้นหาผ่านโฮสต์โดยตรงด้วย Ollama Cloud:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",        api: "ollama",        models: [{ id: "kimi-k2.5:cloud", name: "kimi-k2.5:cloud", input: ["text"] }],      },    },  },  tools: {    web: {      search: { provider: "ollama" },    },  },}
[/code]

สำหรับ daemon โลคัลที่ลงชื่อเข้าใช้แล้ว OpenClaw จะใช้ proxy `/api/experimental/web_search` ของ daemon สำหรับ `https://ollama.com` ระบบจะเรียก endpoint `/api/web_search` ที่โฮสต์ไว้โดยตรง

## การกำหนดค่าขั้นสูง

โหมด OpenAI-compatible แบบเดิม

หากคุณจำเป็นต้องใช้ endpoint ที่เข้ากันได้กับ OpenAI แทน (เช่น อยู่หลัง proxy ที่รองรับเฉพาะรูปแบบ OpenAI) ให้ตั้งค่า `api: "openai-completions"` อย่างชัดเจน:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434/v1",        api: "openai-completions",        injectNumCtxForOpenAICompat: true, // default: true        apiKey: "ollama-local",        models: [...]      }    }  }}
[/code]

โหมดนี้อาจไม่รองรับการสตรีมและ tool calling พร้อมกัน คุณอาจต้องปิดการสตรีมด้วย `params: { streaming: false }` ในการกำหนดค่าโมเดล

เมื่อใช้ `api: "openai-completions"` กับ Ollama OpenClaw จะ inject `options.num_ctx` ตามค่าเริ่มต้น เพื่อไม่ให้ Ollama ย้อนกลับไปใช้ context window 4096 อย่างเงียบ ๆ หาก proxy/upstream ของคุณปฏิเสธฟิลด์ `options` ที่ไม่รู้จัก ให้ปิดพฤติกรรมนี้:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434/v1",        api: "openai-completions",        injectNumCtxForOpenAICompat: false,        apiKey: "ollama-local",        models: [...]      }    }  }}
[/code]

Context windows

สำหรับโมเดลที่ค้นพบอัตโนมัติ OpenClaw จะใช้ context window ที่ Ollama รายงานเมื่อมี รวมถึงค่า `PARAMETER num_ctx` ที่ใหญ่ขึ้นจาก Modelfiles แบบกำหนดเอง มิฉะนั้นจะย้อนกลับไปใช้ context window เริ่มต้นของ Ollama ที่ OpenClaw ใช้

คุณสามารถตั้งค่าเริ่มต้น `contextWindow`, `contextTokens` และ `maxTokens` ระดับผู้ให้บริการสำหรับทุกโมเดลภายใต้ผู้ให้บริการ Ollama นั้น แล้ว override รายโมเดลเมื่อจำเป็น `contextWindow` คือ budget สำหรับ prompt และ Compaction ของ OpenClaw คำขอ Ollama แบบ native จะปล่อย `options.num_ctx` ไว้โดยไม่ตั้งค่า เว้นแต่คุณจะกำหนดค่า `params.num_ctx` อย่างชัดเจน เพื่อให้ Ollama ใช้ค่าเริ่มต้นของโมเดล, `OLLAMA_CONTEXT_LENGTH` หรือค่าตาม VRAM ของตัวเองได้ หากต้องการจำกัดหรือบังคับ context รันไทม์รายคำขอของ Ollama โดยไม่ต้องสร้าง Modelfile ใหม่ ให้ตั้งค่า `params.num_ctx`; ค่าที่ไม่ถูกต้อง, ศูนย์, ติดลบ และไม่จำกัดจะถูกละเว้น อะแดปเตอร์ Ollama ที่เข้ากันได้กับ OpenAI ยังคง inject `options.num_ctx` ตามค่าเริ่มต้นจาก `params.num_ctx` หรือ `contextWindow` ที่กำหนดค่าไว้; ปิดด้วย `injectNumCtxForOpenAICompat: false` หาก upstream ของคุณปฏิเสธ `options`

รายการโมเดล Ollama แบบ native ยังรับตัวเลือก Ollama runtime ทั่วไปภายใต้ `params` รวมถึง `temperature`, `top_p`, `top_k`, `min_p`, `num_predict`, `stop`, `repeat_penalty`, `num_batch`, `num_thread` และ `use_mmap` OpenClaw ส่งต่อเฉพาะคีย์คำขอของ Ollama ดังนั้นพารามิเตอร์รันไทม์ของ OpenClaw เช่น `streaming` จะไม่รั่วไปยัง Ollama ใช้ `params.think` หรือ `params.thinking` เพื่อส่ง `think` ระดับบนสุดของ Ollama; `false` จะปิดการคิดระดับ API สำหรับโมเดลคิดแบบ Qwen

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        contextWindow: 32768,        models: [          {            id: "llama3.3",            contextWindow: 131072,            maxTokens: 65536,            params: {              num_ctx: 32768,              temperature: 0.7,              top_p: 0.9,              thinking: false,            },          }        ]      }    }  }}
[/code]

`agents.defaults.models["ollama/<model>"].params.num_ctx` รายโมเดลก็ใช้ได้เช่นกัน หากกำหนดค่าทั้งสองแบบ รายการโมเดลของผู้ให้บริการที่ระบุชัดเจนจะชนะค่าเริ่มต้นของเอเจนต์

การควบคุมการคิด

สำหรับโมเดล Ollama แบบ native OpenClaw จะส่งต่อการควบคุมการคิดตามที่ Ollama คาดไว้: `think` ระดับบนสุด ไม่ใช่ `options.think` โมเดลที่ค้นพบอัตโนมัติซึ่งการตอบกลับ `/api/show` มีความสามารถ `thinking` จะแสดง `/think low`, `/think medium`, `/think high` และ `/think max`; โมเดลที่ไม่คิดจะแสดงเฉพาะ `/think off`

bashCopy code
[code]
    openclaw agent --model ollama/gemma4 --thinking offopenclaw agent --model ollama/gemma4 --thinking low
[/code]

คุณยังสามารถตั้งค่าเริ่มต้นของโมเดลได้ด้วย:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "ollama/gemma4": {          thinking: "low",        },      },    },  },}
[/code]

`params.think` หรือ `params.thinking` รายโมเดลสามารถปิดหรือบังคับการคิดของ Ollama API สำหรับโมเดลที่กำหนดค่าไว้โดยเฉพาะได้ OpenClaw จะรักษาพารามิเตอร์โมเดลที่ระบุชัดเจนเหล่านั้นไว้เมื่อการรันที่ใช้งานอยู่มีเพียงค่าเริ่มต้นโดยนัย `off`; คำสั่งรันไทม์ที่ไม่ใช่ off เช่น `/think medium` ยังคง override การรันที่ใช้งานอยู่

โมเดลการให้เหตุผล

OpenClaw ถือว่าโมเดลที่มีชื่อเช่น `deepseek-r1`, `reasoning` หรือ `think` รองรับการให้เหตุผลตามค่าเริ่มต้น

bashCopy code
[code]
    ollama pull deepseek-r1:32b
[/code]

ไม่ต้องมีการกำหนดค่าเพิ่มเติม OpenClaw จะทำเครื่องหมายให้โดยอัตโนมัติ

ค่าใช้จ่ายของโมเดล

Ollama ฟรีและรันในเครื่อง ดังนั้นค่าใช้จ่ายของโมเดลทั้งหมดจะถูกตั้งเป็น $0 ซึ่งใช้กับทั้งโมเดลที่ค้นพบอัตโนมัติและโมเดลที่กำหนดเอง

Memory embeddings

Plugin Ollama ที่รวมมาในชุดจะลงทะเบียนผู้ให้บริการ memory embedding สำหรับ [การค้นหาหน่วยความจำ](</th/concepts/memory>) โดยใช้ URL ฐานของ Ollama และ API key ที่กำหนดค่าไว้ เรียก endpoint `/api/embed` ปัจจุบันของ Ollama และจัดชุด ชิ้นส่วนหน่วยความจำหลายรายการเป็นคำขอ `input` เดียวเมื่อทำได้

คุณสมบัติ | ค่า  
---|---  
โมเดลเริ่มต้น | `nomic-embed-text`  
Auto-pull | ใช่ — โมเดล embedding จะถูกดึงโดยอัตโนมัติหากยังไม่มีอยู่ในเครื่อง  
  
embedding ณ เวลา query ใช้ prefix สำหรับการดึงข้อมูลสำหรับโมเดลที่ต้องใช้หรือแนะนำให้ใช้ รวมถึง `nomic-embed-text`, `qwen3-embedding` และ `mxbai-embed-large` ชุดเอกสารหน่วยความจำจะคงรูปแบบดิบไว้ เพื่อให้ดัชนีที่มีอยู่ไม่ต้อง migrate รูปแบบ

หากต้องการเลือก Ollama เป็นผู้ให้บริการ embedding สำหรับการค้นหาหน่วยความจำ:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "ollama",        remote: {          // Default for Ollama. Raise on larger hosts if reindexing is too slow.          nonBatchConcurrency: 1,        },      },    },  },}
[/code]

สำหรับโฮสต์ embedding ระยะไกล ให้จำกัดขอบเขตการยืนยันตัวตนไว้ที่โฮสต์นั้น:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "ollama",        model: "nomic-embed-text",        remote: {          baseUrl: "http://gpu-box.local:11434",          apiKey: "ollama-local",          nonBatchConcurrency: 2,        },      },    },  },}
[/code]

การกำหนดค่าการสตรีม

การผสานการทำงาน Ollama ของ OpenClaw ใช้ **API Ollama แบบเนทีฟ** (`/api/chat`) เป็นค่าเริ่มต้น ซึ่งรองรับทั้งการสตรีมและการเรียกใช้เครื่องมือพร้อมกันอย่างสมบูรณ์ ไม่จำเป็นต้องกำหนดค่าพิเศษ

สำหรับคำขอ `/api/chat` แบบเนทีฟ OpenClaw ยังส่งต่อการควบคุมการคิดไปยัง Ollama โดยตรงด้วย: `/think off` และ `openclaw agent --thinking off` จะส่ง `think: false` ระดับบนสุด เว้นแต่มีการกำหนดค่า model `params.think`/`params.thinking` ไว้อย่างชัดเจน ส่วน `/think low|medium|high` จะส่งสตริงระดับความพยายาม `think` ระดับบนสุดที่ตรงกัน `/think max` จะถูกแมปเป็นระดับความพยายามแบบเนทีฟสูงสุดของ Ollama คือ `think: "high"`

## การแก้ไขปัญหา

ลูปการแครชของ WSL2 (รีบูตซ้ำ)

บน WSL2 ที่ใช้ NVIDIA/CUDA ตัวติดตั้ง Ollama สำหรับ Linux อย่างเป็นทางการจะสร้างหน่วย systemd `ollama.service` พร้อม `Restart=always` หากบริการนั้นเริ่มอัตโนมัติและโหลดโมเดลที่ใช้ GPU ระหว่างการบูต WSL2 Ollama อาจยึดหน่วยความจำของโฮสต์ไว้ขณะโหลดโมเดล การเรียกคืนหน่วยความจำของ Hyper-V อาจไม่สามารถเรียกคืนเพจที่ถูกยึดไว้เหล่านั้นได้เสมอ ทำให้ Windows อาจยุติ VM ของ WSL2 จากนั้น systemd จะเริ่ม Ollama อีกครั้ง และลูปก็เกิดซ้ำ

หลักฐานที่พบบ่อย:

  * WSL2 รีบูตหรือถูกยุติซ้ำจากฝั่ง Windows
  * CPU สูงใน `app.slice` หรือ `ollama.service` ไม่นานหลังจาก WSL2 เริ่มต้น
  * SIGTERM จาก systemd แทนที่จะเป็นเหตุการณ์ Linux OOM-killer


OpenClaw จะบันทึกคำเตือนตอนเริ่มต้นเมื่อตรวจพบ WSL2, `ollama.service` ที่เปิดใช้งานพร้อม `Restart=always` และตัวบ่งชี้ CUDA ที่มองเห็นได้

การบรรเทาปัญหา:

bashCopy code
[code]
    sudo systemctl disable ollama
[/code]

เพิ่มสิ่งนี้ลงใน `%USERPROFILE%\.wslconfig` บนฝั่ง Windows แล้วรัน `wsl --shutdown`:

iniCopy code
[code]
    [experimental]autoMemoryReclaim=disabled
[/code]

ตั้งค่า keep-alive ให้สั้นลงในสภาพแวดล้อมของบริการ Ollama หรือเริ่ม Ollama ด้วยตนเองเฉพาะเมื่อคุณต้องใช้:

bashCopy code
[code]
    export OLLAMA_KEEP_ALIVE=5mollama serve
[/code]

ดู [ollama/ollama#11317](<https://github.com/ollama/ollama/issues/11317>)

ตรวจไม่พบ Ollama

ตรวจสอบให้แน่ใจว่า Ollama กำลังทำงาน และคุณตั้งค่า `OLLAMA_API_KEY` (หรือโปรไฟล์การยืนยันตัวตน) แล้ว และคุณ **ไม่ได้** กำหนดรายการ `models.providers.ollama` ไว้อย่างชัดเจน:

bashCopy code
[code]
    ollama serve
[/code]

ตรวจสอบว่าเข้าถึง API ได้:

bashCopy code
[code]
    curl http://localhost:11434/api/tags
[/code]

ไม่มีโมเดลพร้อมใช้งาน

หากโมเดลของคุณไม่อยู่ในรายการ ให้ดึงโมเดลมาไว้ในเครื่องหรือกำหนดอย่างชัดเจนใน `models.providers.ollama`

bashCopy code
[code]
    ollama list  # See what's installedollama pull gemma4ollama pull gpt-oss:20bollama pull llama3.3     # Or another model
[/code]

การเชื่อมต่อถูกปฏิเสธ

ตรวจสอบว่า Ollama กำลังทำงานบนพอร์ตที่ถูกต้อง:

bashCopy code
[code]
    # Check if Ollama is runningps aux | grep ollama # Or restart Ollamaollama serve
[/code]

โฮสต์ระยะไกลใช้ curl ได้ แต่ใช้ OpenClaw ไม่ได้

ตรวจสอบจากเครื่องและรันไทม์เดียวกันกับที่รัน Gateway:

bashCopy code
[code]
    openclaw gateway status --deepcurl http://ollama-host:11434/api/tags
[/code]

สาเหตุที่พบบ่อย:

  * `baseUrl` ชี้ไปที่ `localhost` แต่ Gateway รันใน Docker หรือบนโฮสต์อื่น
  * URL ใช้ `/v1` ซึ่งเลือกพฤติกรรมที่เข้ากันได้กับ OpenAI แทน Ollama แบบเนทีฟ
  * โฮสต์ระยะไกลต้องเปลี่ยนการตั้งค่าไฟร์วอลล์หรือการผูก LAN ทางฝั่ง Ollama
  * โมเดลมีอยู่บนเดมอนของแล็ปท็อปคุณ แต่ไม่มีอยู่บนเดมอนระยะไกล

โมเดลส่งออก JSON ของเครื่องมือเป็นข้อความ

โดยทั่วไปหมายความว่าผู้ให้บริการกำลังใช้โหมดที่เข้ากันได้กับ OpenAI หรือโมเดลไม่สามารถจัดการสคีมาของเครื่องมือได้

แนะนำให้ใช้โหมด Ollama แบบเนทีฟ:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434",        api: "ollama",      },    },  },}
[/code]

หากโมเดลโลคัลขนาดเล็กยังคงล้มเหลวกับสคีมาของเครื่องมือ ให้ตั้งค่า `compat.supportsTools: false` ในรายการโมเดลนั้นแล้วทดสอบใหม่

Kimi หรือ GLM ส่งคืนสัญลักษณ์ผิดเพี้ยน

คำตอบ Kimi/GLM ที่โฮสต์ไว้ซึ่งยาวและเป็นชุดสัญลักษณ์ที่ไม่ใช่ภาษา จะถูกถือว่าเป็นเอาต์พุตผู้ให้บริการที่ล้มเหลว แทนที่จะเป็นคำตอบผู้ช่วยที่สำเร็จ ซึ่งทำให้การลองใหม่ การสำรอง หรือการจัดการข้อผิดพลาดตามปกติเข้ามาทำงานได้โดยไม่บันทึกข้อความที่เสียหายลงในเซสชัน

หากเกิดขึ้นซ้ำ ให้บันทึกชื่อโมเดลดิบ ไฟล์เซสชันปัจจุบัน และการรันนั้นใช้ `Cloud + Local` หรือ `Cloud only` จากนั้นลองเซสชันใหม่และโมเดลสำรอง:

bashCopy code
[code]
    openclaw infer model run --model ollama/kimi-k2.5:cloud --prompt "Reply with exactly: ok" --jsonopenclaw models set ollama/gemma4
[/code]

โมเดลโลคัลแบบเย็นหมดเวลา

โมเดลโลคัลขนาดใหญ่อาจต้องใช้เวลานานในการโหลดครั้งแรกก่อนเริ่มสตรีม จำกัด timeout ให้อยู่ในขอบเขตของผู้ให้บริการ Ollama และเลือกให้ Ollama โหลดโมเดลค้างไว้ระหว่างรอบการสนทนาได้:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        timeoutSeconds: 300,        models: [          {            id: "gemma4:26b",            name: "gemma4:26b",            params: { keep_alive: "15m" },          },        ],      },    },  },}
[/code]

หากตัวโฮสต์เองรับการเชื่อมต่อได้ช้า `timeoutSeconds` จะขยาย timeout การเชื่อมต่อ Undici ที่มีการป้องกันสำหรับผู้ให้บริการนี้ด้วย

โมเดลบริบทขนาดใหญ่ช้าเกินไปหรือหน่วยความจำไม่พอ

โมเดล Ollama จำนวนมากประกาศขนาดบริบทที่ใหญ่เกินกว่าฮาร์ดแวร์ของคุณจะรันได้อย่างสบาย Ollama แบบเนทีฟใช้ค่าเริ่มต้นของบริบทรันไทม์ของ Ollama เอง เว้นแต่คุณตั้งค่า `params.num_ctx` จำกัดทั้งงบประมาณของ OpenClaw และบริบทคำขอของ Ollama เมื่อต้องการ latency ของโทเค็นแรกที่คาดการณ์ได้:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        contextWindow: 32768,        maxTokens: 8192,        models: [          {            id: "qwen3.5:9b",            name: "qwen3.5:9b",            params: { num_ctx: 32768, thinking: false },          },        ],      },    },  },}
[/code]

ลด `contextWindow` ก่อนหาก OpenClaw กำลังส่งพรอมป์มากเกินไป ลด `params.num_ctx` หาก Ollama กำลังโหลดบริบทรันไทม์ที่ใหญ่เกินไปสำหรับเครื่อง ลด `maxTokens` หากการสร้างข้อความใช้เวลานานเกินไป

## ที่เกี่ยวข้อง

[**ผู้ให้บริการโมเดล** ภาพรวมของผู้ให้บริการทั้งหมด การอ้างอิงโมเดล และพฤติกรรม failover ](</th/concepts/model-providers>) [**การเลือกโมเดล** วิธีเลือกและกำหนดค่าโมเดล ](</th/concepts/models>) [**การค้นหาเว็บด้วย Ollama** รายละเอียดการตั้งค่าและพฤติกรรมทั้งหมดสำหรับการค้นหาเว็บที่ขับเคลื่อนด้วย Ollama ](</th/tools/ollama-search>) [**การกำหนดค่า** เอกสารอ้างอิงการกำหนดค่าฉบับเต็ม ](</th/gateway/configuration>)

Was this useful?YesNo