---
title: MiniMax
source_url: https://docs.openclaw.ai/th/providers/minimax
scraped_at: 2026-05-25
---

OpenClaw's MiniMax provider defaults to **MiniMax M2.7**.

MiniMax also provides:

  * Bundled speech synthesis via T2A v2
  * Bundled image understanding via `MiniMax-VL-01`
  * Bundled music generation via `music-2.6`
  * Bundled `web_search` through the MiniMax Token Plan search API


Provider split:

Provider ID | Auth | Capabilities  
---|---|---  
`minimax` | API key | Text, image generation, music generation, video generation, image understanding, speech, web search  
`minimax-portal` | OAuth | Text, image generation, music generation, video generation, image understanding, speech  
  
## Built-in catalog

Model | Type | Description  
---|---|---  
`MiniMax-M2.7` | Chat (reasoning) | Default hosted reasoning model  
`MiniMax-M2.7-highspeed` | Chat (reasoning) | Faster M2.7 reasoning tier  
`MiniMax-VL-01` | Vision | Image understanding model  
`image-01` | Image generation | Text-to-image and image-to-image editing  
`music-2.6` | Music generation | Default music model  
`music-2.5` | Music generation | Previous music generation tier  
`music-2.0` | Music generation | Legacy music generation tier  
`MiniMax-Hailuo-2.3` | Video generation | Text-to-video and image reference flows  
  
## Getting started

Choose your preferred auth method and follow the setup steps.

### OAuth (Coding Plan)

**Best for:** quick setup with MiniMax Coding Plan via OAuth, no API key required.

### International

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice minimax-global-oauth
[/code]

This authenticates against `api.minimax.io`.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider minimax-portal
[/code]

### China

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice minimax-cn-oauth
[/code]

This authenticates against `api.minimaxi.com`.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider minimax-portal
[/code]

### API key

**Best for:** hosted MiniMax with Anthropic-compatible API.

### International

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice minimax-global-api
[/code]

This configures `api.minimax.io` as the base URL.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider minimax
[/code]

### China

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice minimax-cn-api
[/code]

This configures `api.minimaxi.com` as the base URL.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider minimax
[/code]

### Config example

json5Copy code
[code]
    {  env: { MINIMAX_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "minimax/MiniMax-M2.7" } } },  models: {    mode: "merge",    providers: {      minimax: {        baseUrl: "https://api.minimax.io/anthropic",        apiKey: "${MINIMAX_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "MiniMax-M2.7",            name: "MiniMax M2.7",            reasoning: true,            input: ["text"],            cost: { input: 0.3, output: 1.2, cacheRead: 0.06, cacheWrite: 0.375 },            contextWindow: 204800,            maxTokens: 131072,          },          {            id: "MiniMax-M2.7-highspeed",            name: "MiniMax M2.7 Highspeed",            reasoning: true,            input: ["text"],            cost: { input: 0.6, output: 2.4, cacheRead: 0.06, cacheWrite: 0.375 },            contextWindow: 204800,            maxTokens: 131072,          },        ],      },    },  },}
[/code]

## Configure via `openclaw configure`

Use the interactive config wizard to set MiniMax without editing JSON:

* ### เปิดตัวช่วยตั้งค่า

bashCopy code
[code]
    openclaw configure
[/code]

* ### เลือก Model/auth

เลือก **Model/auth** จากเมนู

* ### เลือกตัวเลือกการยืนยันตัวตน MiniMax

เลือกหนึ่งในตัวเลือก MiniMax ที่มี:

ตัวเลือกการยืนยันตัวตน | คำอธิบาย  
---|---  
`minimax-global-oauth` | OAuth ระหว่างประเทศ (Coding Plan)  
`minimax-cn-oauth` | OAuth จีน (Coding Plan)  
`minimax-global-api` | คีย์ API ระหว่างประเทศ  
`minimax-cn-api` | คีย์ API จีน  
* ### เลือกโมเดลเริ่มต้นของคุณ

เลือกโมเดลเริ่มต้นของคุณเมื่อระบบแจ้ง

## ความสามารถ

### การสร้างภาพ

Plugin MiniMax ลงทะเบียนโมเดล `image-01` สำหรับเครื่องมือ `image_generate` รองรับ:

  * **การสร้างภาพจากข้อความ** พร้อมการควบคุมอัตราส่วนภาพ
  * **การแก้ไขภาพจากภาพ** (การอ้างอิงวัตถุหลัก) พร้อมการควบคุมอัตราส่วนภาพ
  * สูงสุด **9 ภาพเอาต์พุต** ต่อคำขอ
  * สูงสุด **1 ภาพอ้างอิง** ต่อคำขอแก้ไข
  * อัตราส่วนภาพที่รองรับ: `1:1`, `16:9`, `4:3`, `3:2`, `2:3`, `3:4`, `9:16`, `21:9`


หากต้องการใช้ MiniMax สำหรับการสร้างภาพ ให้ตั้งค่าเป็นผู้ให้บริการการสร้างภาพ:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: { primary: "minimax/image-01" },    },  },}
[/code]

Plugin ใช้ `MINIMAX_API_KEY` เดียวกัน หรือการยืนยันตัวตน OAuth เดียวกับโมเดลข้อความ ไม่จำเป็นต้องตั้งค่าเพิ่มเติมหากตั้งค่า MiniMax ไว้แล้ว

ทั้ง `minimax` และ `minimax-portal` ลงทะเบียน `image_generate` ด้วยโมเดล `image-01` เดียวกัน การตั้งค่าด้วยคีย์ API ใช้ `MINIMAX_API_KEY`; การตั้งค่าด้วย OAuth สามารถใช้ เส้นทางการยืนยันตัวตน `minimax-portal` ที่รวมมาให้แทนได้

การสร้างภาพใช้ปลายทางภาพเฉพาะของ MiniMax เสมอ (`/v1/image_generation`) และละเว้น `models.providers.minimax.baseUrl` เนื่องจากฟิลด์นั้นกำหนดค่า URL ฐานสำหรับแชต/ที่เข้ากันได้กับ Anthropic ตั้งค่า `MINIMAX_API_HOST=https://api.minimaxi.com` เพื่อกำหนดเส้นทางการสร้างภาพ ผ่านปลายทาง CN; ปลายทางสากลเริ่มต้นคือ `https://api.minimax.io`

เมื่อการเริ่มต้นใช้งานหรือการตั้งค่าคีย์ API เขียนรายการ `models.providers.minimax` แบบชัดเจน OpenClaw จะสร้าง `MiniMax-M2.7` และ `MiniMax-M2.7-highspeed` เป็นโมเดลแชตแบบข้อความเท่านั้น การเข้าใจภาพ ถูกเปิดเผยแยกต่างหากผ่านผู้ให้บริการสื่อ `MiniMax-VL-01` ที่ Plugin เป็นเจ้าของ

### ข้อความเป็นเสียงพูด

Plugin `minimax` ที่รวมมาให้ลงทะเบียน MiniMax T2A v2 เป็นผู้ให้บริการเสียงพูดสำหรับ `messages.tts`

  * โมเดล TTS เริ่มต้น: `speech-2.8-hd`
  * เสียงเริ่มต้น: `English_expressive_narrator`
  * ID โมเดลที่รวมมาและรองรับ ได้แก่ `speech-2.8-hd`, `speech-2.8-turbo`, `speech-2.6-hd`, `speech-2.6-turbo`, `speech-02-hd`, `speech-02-turbo`, `speech-01-hd` และ `speech-01-turbo`
  * การแก้ไขการยืนยันตัวตนใช้ `messages.tts.providers.minimax.apiKey` จากนั้น โปรไฟล์การยืนยันตัวตน OAuth/token ของ `minimax-portal` จากนั้นคีย์สภาพแวดล้อม Token Plan (`MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`) แล้วจึงใช้ `MINIMAX_API_KEY`
  * หากไม่ได้กำหนดค่าโฮสต์ TTS OpenClaw จะใช้โฮสต์ OAuth ของ `minimax-portal` ที่กำหนดค่าไว้ซ้ำ และตัดส่วนท้ายเส้นทางที่เข้ากันได้กับ Anthropic เช่น `/anthropic`
  * ไฟล์แนบเสียงปกติยังคงเป็น MP3
  * ปลายทางโน้ตเสียง เช่น Feishu และ Telegram จะถูกแปลงรหัสจาก MP3 ของ MiniMax เป็น Opus 48kHz ด้วย `ffmpeg` เนื่องจาก API ไฟล์ของ Feishu/Lark ยอมรับเฉพาะ `file_type: "opus"` สำหรับข้อความเสียงแบบเนทีฟ
  * MiniMax T2A ยอมรับ `speed` และ `vol` แบบทศนิยม แต่ `pitch` จะถูกส่งเป็น จำนวนเต็ม; OpenClaw จะตัดค่าทศนิยมของ `pitch` ออกก่อนส่งคำขอ API

การตั้งค่า | ตัวแปรสภาพแวดล้อม | ค่าเริ่มต้น | คำอธิบาย  
---|---|---|---  
`messages.tts.providers.minimax.baseUrl` | `MINIMAX_API_HOST` | `https://api.minimax.io` | โฮสต์ API MiniMax T2A  
`messages.tts.providers.minimax.model` | `MINIMAX_TTS_MODEL` | `speech-2.8-hd` | ID โมเดล TTS  
`messages.tts.providers.minimax.voiceId` | `MINIMAX_TTS_VOICE_ID` | `English_expressive_narrator` | ID เสียงที่ใช้สำหรับเอาต์พุตเสียงพูด  
`messages.tts.providers.minimax.speed` |  | `1.0` | ความเร็วการเล่น, `0.5..2.0`  
`messages.tts.providers.minimax.vol` |  | `1.0` | ระดับเสียง, `(0, 10]`  
`messages.tts.providers.minimax.pitch` |  | `0` | การเลื่อนระดับเสียงแบบจำนวนเต็ม, `-12..12`  
  
### การสร้างเพลง

Plugin MiniMax ที่รวมมาให้ลงทะเบียนการสร้างเพลงผ่านเครื่องมือร่วม `music_generate` สำหรับทั้ง `minimax` และ `minimax-portal`

  * โมเดลเพลงเริ่มต้น: `minimax/music-2.6`
  * โมเดลเพลง OAuth: `minimax-portal/music-2.6`
  * รองรับ `minimax/music-2.5` และ `minimax/music-2.0` ด้วย
  * การควบคุมพรอมต์: `lyrics`, `instrumental`, `durationSeconds`
  * รูปแบบเอาต์พุต: `mp3`
  * การรันที่มีเซสชันรองรับจะแยกทำงานผ่านโฟลว์งาน/สถานะร่วม รวมถึง `action: "status"`


หากต้องการใช้ MiniMax เป็นผู้ให้บริการเพลงเริ่มต้น:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "minimax/music-2.6",      },    },  },}
[/code]

### การสร้างวิดีโอ

Plugin MiniMax ที่รวมมาให้ลงทะเบียนการสร้างวิดีโอผ่านเครื่องมือร่วม `video_generate` สำหรับทั้ง `minimax` และ `minimax-portal`

  * โมเดลวิดีโอเริ่มต้น: `minimax/MiniMax-Hailuo-2.3`
  * โมเดลวิดีโอ OAuth: `minimax-portal/MiniMax-Hailuo-2.3`
  * โหมด: โฟลว์ข้อความเป็นวิดีโอและการอ้างอิงภาพเดี่ยว
  * รองรับ `aspectRatio` และ `resolution`


หากต้องการใช้ MiniMax เป็นผู้ให้บริการวิดีโอเริ่มต้น:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "minimax/MiniMax-Hailuo-2.3",      },    },  },}
[/code]

### การเข้าใจรูปภาพ

Plugin MiniMax ลงทะเบียนการเข้าใจรูปภาพแยกจากแค็ตตาล็อกข้อความ:

ID ผู้ให้บริการ | โมเดลรูปภาพเริ่มต้น  
---|---  
`minimax` | `MiniMax-VL-01`  
`minimax-portal` | `MiniMax-VL-01`  
  
นี่คือเหตุผลที่การกำหนดเส้นทางสื่ออัตโนมัติสามารถใช้การเข้าใจรูปภาพของ MiniMax ได้ แม้ว่าแค็ตตาล็อกผู้ให้บริการข้อความที่รวมมาแล้วยังแสดงเฉพาะ refs แชต M2.7 แบบข้อความเท่านั้น

### การค้นหาเว็บ

Plugin MiniMax ยังลงทะเบียน `web_search` ผ่าน API ค้นหา MiniMax Token Plan ด้วย

  * ID ผู้ให้บริการ: `minimax`
  * ผลลัพธ์แบบมีโครงสร้าง: ชื่อเรื่อง, URL, snippets, คำค้นหาที่เกี่ยวข้อง
  * env var ที่แนะนำ: `MINIMAX_CODE_PLAN_KEY`
  * env aliases ที่ยอมรับ: `MINIMAX_CODING_API_KEY`, `MINIMAX_OAUTH_TOKEN`
  * fallback เพื่อความเข้ากันได้: `MINIMAX_API_KEY` เมื่อชี้ไปยังข้อมูลรับรอง token-plan อยู่แล้ว
  * การใช้ภูมิภาคซ้ำ: `plugins.entries.minimax.config.webSearch.region` จากนั้น `MINIMAX_API_HOST` จากนั้น base URLs ของผู้ให้บริการ MiniMax
  * การค้นหายังคงอยู่บน ID ผู้ให้บริการ `minimax`; การตั้งค่า OAuth CN/global สามารถกำหนดภูมิภาคทางอ้อมผ่าน `models.providers.minimax-portal.baseUrl` และสามารถให้ bearer auth ผ่าน `MINIMAX_OAUTH_TOKEN`


การกำหนดค่าอยู่ใต้ `plugins.entries.minimax.config.webSearch.*`

## การกำหนดค่าขั้นสูง

ตัวเลือกการกำหนดค่า ตัวเลือก | คำอธิบาย  
---|---  
`models.providers.minimax.baseUrl` | แนะนำให้ใช้ `https://api.minimax.io/anthropic` (เข้ากันได้กับ Anthropic); `https://api.minimax.io/v1` เป็นตัวเลือกสำหรับ payload ที่เข้ากันได้กับ OpenAI  
`models.providers.minimax.api` | แนะนำให้ใช้ `anthropic-messages`; `openai-completions` เป็นตัวเลือกสำหรับ payload ที่เข้ากันได้กับ OpenAI  
`models.providers.minimax.apiKey` | คีย์ API ของ MiniMax (`MINIMAX_API_KEY`)  
`models.providers.minimax.models` | กำหนด `id`, `name`, `reasoning`, `contextWindow`, `maxTokens`, `cost`  
`agents.defaults.models` | ตั้ง alias ให้โมเดลที่คุณต้องการใน allowlist  
`models.mode` | คง `merge` ไว้หากคุณต้องการเพิ่ม MiniMax ควบคู่กับรายการ built-in  
ค่าเริ่มต้นของ Thinking

บน `api: "anthropic-messages"` OpenClaw จะฉีด `thinking: { type: "disabled" }` เว้นแต่จะตั้งค่า thinking ไว้อย่างชัดเจนใน params/config แล้ว

วิธีนี้ป้องกันไม่ให้ endpoint streaming ของ MiniMax ปล่อย `reasoning_content` ใน delta chunks สไตล์ OpenAI ซึ่งจะทำให้ reasoning ภายในรั่วไหลไปยังผลลัพธ์ที่มองเห็นได้

โหมดเร็ว

`/fast on` หรือ `params.fastMode: true` จะเขียน `MiniMax-M2.7` ใหม่เป็น `MiniMax-M2.7-highspeed` บนเส้นทางสตรีมที่เข้ากันได้กับ Anthropic

ตัวอย่าง fallback

**เหมาะที่สุดสำหรับ:** ใช้โมเดลรุ่นล่าสุดที่แรงที่สุดของคุณเป็น primary และ fail over ไปยัง MiniMax M2.7 ตัวอย่างด้านล่างใช้ Opus เป็น primary แบบเจาะจง; เปลี่ยนเป็นโมเดล primary รุ่นล่าสุดที่คุณต้องการ

json5Copy code
[code]
    {  env: { MINIMAX_API_KEY: "sk-..." },  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": { alias: "primary" },        "minimax/MiniMax-M2.7": { alias: "minimax" },      },      model: {        primary: "anthropic/claude-opus-4-6",        fallbacks: ["minimax/MiniMax-M2.7"],      },    },  },}
[/code]

รายละเอียดการใช้งาน Coding Plan

  * API การใช้งาน Coding Plan: `https://api.minimaxi.com/v1/token_plan/remains` หรือ `https://api.minimax.io/v1/token_plan/remains` (ต้องใช้คีย์ coding plan)
  * การ polling การใช้งานจะหา host จาก `models.providers.minimax-portal.baseUrl` หรือ `models.providers.minimax.baseUrl` เมื่อกำหนดค่าไว้ ดังนั้นการตั้งค่า global ที่ใช้ `https://api.minimax.io/anthropic` จะ poll `api.minimax.io` หาก base URL ขาดหายหรือผิดรูปแบบ จะคง fallback CN ไว้เพื่อความเข้ากันได้
  * OpenClaw ปรับรูปแบบการใช้งาน coding-plan ของ MiniMax ให้เป็นการแสดงผล `% left` แบบเดียวกับผู้ให้บริการอื่น ฟิลด์ดิบ `usage_percent` / `usagePercent` ของ MiniMax คือโควตาที่เหลือ ไม่ใช่โควตาที่ใช้ไป ดังนั้น OpenClaw จึงกลับค่าเหล่านั้น ฟิลด์แบบนับจำนวนจะมีสิทธิ์เหนือกว่าเมื่อมีอยู่
  * เมื่อ API ส่งคืน `model_remains` OpenClaw จะเลือก entry ของโมเดลแชต สร้างป้ายกำกับหน้าต่างจาก `start_time` / `end_time` เมื่อจำเป็น และใส่ชื่อโมเดลที่เลือกไว้ในป้ายกำกับแผน เพื่อให้แยกแยะหน้าต่าง coding-plan ได้ง่ายขึ้น
  * snapshots การใช้งานถือว่า `minimax`, `minimax-cn` และ `minimax-portal` เป็นพื้นผิวโควตา MiniMax เดียวกัน และเลือกใช้ MiniMax OAuth ที่เก็บไว้ก่อนจะ fallback ไปยัง env vars ของคีย์ Coding Plan


## หมายเหตุ

  * refs โมเดลจะตามเส้นทาง auth: 
    * การตั้งค่าคีย์ API: `minimax/<model>`
    * การตั้งค่า OAuth: `minimax-portal/<model>`
  * โมเดลแชตเริ่มต้น: `MiniMax-M2.7`
  * โมเดลแชตทางเลือก: `MiniMax-M2.7-highspeed`
  * การ onboarding และการตั้งค่าคีย์ API โดยตรงจะเขียนคำจำกัดความโมเดลแบบข้อความเท่านั้นสำหรับ M2.7 ทั้งสอง variants
  * การเข้าใจรูปภาพใช้ผู้ให้บริการสื่อ `MiniMax-VL-01` ที่ Plugin เป็นเจ้าของ
  * อัปเดตราคาค่าใช้จ่ายใน `models.json` หากคุณต้องการติดตามต้นทุนอย่างแม่นยำ
  * ใช้ `openclaw models list` เพื่อยืนยัน ID ผู้ให้บริการปัจจุบัน จากนั้นสลับด้วย `openclaw models set minimax/MiniMax-M2.7` หรือ `openclaw models set minimax-portal/MiniMax-M2.7`


## การแก้ไขปัญหา

"Unknown model: minimax/MiniMax-M2.7"

โดยทั่วไปหมายความว่า **ไม่ได้กำหนดค่าผู้ให้บริการ MiniMax** (ไม่พบ entry ผู้ให้บริการที่ตรงกัน และไม่พบโปรไฟล์ auth/env key ของ MiniMax) การแก้ไขการตรวจจับนี้อยู่ใน **2026.1.12** แก้ไขโดย:

  * อัปเกรดเป็น **2026.1.12** (หรือรันจาก source `main`) จากนั้นรีสตาร์ท gateway
  * รัน `openclaw configure` แล้วเลือกตัวเลือก auth ของ **MiniMax** หรือ
  * เพิ่มบล็อก `models.providers.minimax` หรือ `models.providers.minimax-portal` ที่ตรงกันด้วยตนเอง หรือ
  * ตั้งค่า `MINIMAX_API_KEY`, `MINIMAX_OAUTH_TOKEN` หรือโปรไฟล์ auth ของ MiniMax เพื่อให้สามารถฉีดผู้ให้บริการที่ตรงกันได้


ตรวจสอบให้แน่ใจว่า ID โมเดลเป็นแบบ **case-sensitive** :

  * เส้นทางคีย์ API: `minimax/MiniMax-M2.7` หรือ `minimax/MiniMax-M2.7-highspeed`
  * เส้นทาง OAuth: `minimax-portal/MiniMax-M2.7` หรือ `minimax-portal/MiniMax-M2.7-highspeed`


จากนั้นตรวจสอบอีกครั้งด้วย:

bashCopy code
[code]
    openclaw models list
[/code]

## ที่เกี่ยวข้อง

[**การเลือกโมเดล** การเลือกผู้ให้บริการ, refs โมเดล และพฤติกรรมการ failover ](</th/concepts/model-providers>) [**การสร้างรูปภาพ** พารามิเตอร์เครื่องมือรูปภาพที่ใช้ร่วมกันและการเลือกผู้ให้บริการ ](</th/tools/image-generation>) [**การสร้างเพลง** พารามิเตอร์เครื่องมือเพลงที่ใช้ร่วมกันและการเลือกผู้ให้บริการ ](</th/tools/music-generation>) [**การสร้างวิดีโอ** พารามิเตอร์เครื่องมือวิดีโอที่ใช้ร่วมกันและการเลือกผู้ให้บริการ ](</th/tools/video-generation>) [**MiniMax Search** การกำหนดค่าการค้นหาเว็บผ่าน MiniMax Token Plan ](</th/tools/minimax-search>) [**การแก้ไขปัญหา** การแก้ไขปัญหาทั่วไปและ FAQ ](</th/help/troubleshooting>)

Was this useful?YesNo