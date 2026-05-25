---
title: DeepInfra
source_url: https://docs.openclaw.ai/th/providers/deepinfra
scraped_at: 2026-05-25
---

DeepInfra ให้บริการ **API แบบรวมศูนย์** ที่กำหนดเส้นทางคำขอไปยังโมเดลโอเพนซอร์สและโมเดลขั้นแนวหน้าที่ได้รับความนิยมที่สุดผ่าน endpoint และ API key เดียว รองรับการใช้งานแบบเข้ากันได้กับ OpenAI ดังนั้น SDK ส่วนใหญ่ของ OpenAI จึงใช้งานได้โดยเปลี่ยน base URL

## การรับ API key

  1. ไปที่ <https://deepinfra.com/>
  2. ลงชื่อเข้าใช้หรือสร้างบัญชี
  3. ไปที่ Dashboard / Keys แล้วสร้าง API key ใหม่หรือใช้อันที่สร้างให้อัตโนมัติ


## การตั้งค่า CLI

bashCopy code
[code]
    openclaw onboard --deepinfra-api-key <key>
[/code]

หรือตั้งค่าตัวแปรสภาพแวดล้อม:

bashCopy code
[code]
    export DEEPINFRA_API_KEY="<your-deepinfra-api-key>" # pragma: allowlist secret
[/code]

## ตัวอย่างการกำหนดค่า

json5Copy code
[code]
    {  env: { DEEPINFRA_API_KEY: "<your-deepinfra-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "deepinfra/deepseek-ai/DeepSeek-V3.2" },    },  },}
[/code]

## พื้นผิว OpenClaw ที่รองรับ

Plugin ที่มาพร้อมกันจะลงทะเบียนพื้นผิว DeepInfra ทั้งหมดที่ตรงกับสัญญาผู้ให้บริการของ OpenClaw ปัจจุบัน:

พื้นผิว | โมเดลเริ่มต้น | การกำหนดค่า/เครื่องมือ OpenClaw  
---|---|---  
แชต / ผู้ให้บริการโมเดล | `deepseek-ai/DeepSeek-V3.2` | `agents.defaults.model`  
การสร้าง/แก้ไขรูปภาพ | `black-forest-labs/FLUX-1-schnell` | `image_generate`, `agents.defaults.imageGenerationModel`  
การทำความเข้าใจสื่อ | `moonshotai/Kimi-K2.5` สำหรับรูปภาพ | การทำความเข้าใจรูปภาพขาเข้า  
การถอดเสียงเป็นข้อความ | `openai/whisper-large-v3-turbo` | การถอดเสียงเสียงขาเข้า  
ข้อความเป็นเสียงพูด | `hexgrad/Kokoro-82M` | `messages.tts.provider: "deepinfra"`  
การสร้างวิดีโอ | `Pixverse/Pixverse-T2V` | `video_generate`, `agents.defaults.videoGenerationModel`  
embeddings หน่วยความจำ | `BAAI/bge-m3` | `agents.defaults.memorySearch.provider: "deepinfra"`  
  
DeepInfra ยังเปิดให้ใช้ reranking, classification, object-detection และชนิดโมเดลเนทีฟอื่น ๆ ด้วย ปัจจุบัน OpenClaw ยังไม่มีสัญญาผู้ให้บริการแบบ first-class สำหรับหมวดหมู่เหล่านั้น ดังนั้น Plugin นี้จึงยังไม่ได้ลงทะเบียนรายการเหล่านี้

## โมเดลที่พร้อมใช้งาน

OpenClaw จะค้นหาโมเดล DeepInfra ที่พร้อมใช้งานแบบไดนามิกเมื่อเริ่มต้น ใช้ `/models deepinfra` เพื่อดูรายการโมเดลที่พร้อมใช้งานทั้งหมด

สามารถใช้โมเดลใดก็ได้ที่มีบน [DeepInfra.com](<https://deepinfra.com/>) พร้อม prefix `deepinfra/`:

CodeCopy code
[code]
    deepinfra/MiniMaxAI/MiniMax-M2.5deepinfra/deepseek-ai/DeepSeek-V3.2deepinfra/moonshotai/Kimi-K2.5deepinfra/zai-org/GLM-5.1...และอีกมากมาย
[/code]

## หมายเหตุ

  * การอ้างอิงโมเดลอยู่ในรูปแบบ `deepinfra/<provider>/<model>` (เช่น `deepinfra/Qwen/Qwen3-Max`)
  * โมเดลเริ่มต้น: `deepinfra/deepseek-ai/DeepSeek-V3.2`
  * Base URL: `https://api.deepinfra.com/v1/openai`
  * การสร้างวิดีโอแบบเนทีฟใช้ `https://api.deepinfra.com/v1/inference/<model>`


## ที่เกี่ยวข้อง

  * [ผู้ให้บริการโมเดล](</th/concepts/model-providers>)
  * [ผู้ให้บริการทั้งหมด](</th/providers>)


Was this useful?YesNo