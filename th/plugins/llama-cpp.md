---
title: ผู้ให้บริการ llama.cpp
source_url: https://docs.openclaw.ai/th/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp` คือ Plugin ผู้ให้บริการภายนอกอย่างเป็นทางการสำหรับ embeddings แบบ GGUF ภายในเครื่อง. Plugin นี้เป็นเจ้าของ dependency รันไทม์ `node-llama-cpp` ที่ใช้โดย `memorySearch.provider: "local"`.

ติดตั้งก่อนใช้ embeddings หน่วยความจำภายในเครื่อง:

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

แพ็กเกจ npm หลัก `openclaw` ไม่มี `node-llama-cpp` รวมอยู่ด้วย การเก็บ dependency เนทีฟไว้ใน Plugin นี้ช่วยป้องกันไม่ให้การอัปเดต npm ของ OpenClaw ตามปกติ ลบรันไทม์ที่ติดตั้งด้วยตนเองภายในไดเรกทอรีแพ็กเกจ OpenClaw.

## การกำหนดค่า

ตั้งค่าผู้ให้บริการค้นหาหน่วยความจำเป็น `local`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

โมเดลเริ่มต้นคือ `embeddinggemma-300m-qat-Q8_0.gguf` คุณยังสามารถชี้ `local.modelPath` ไปยังไฟล์ `.gguf` ภายในเครื่องได้เช่นกัน.

## รันไทม์เนทีฟ

ใช้ Node 24 เพื่อให้เส้นทางการติดตั้งเนทีฟราบรื่นที่สุด เช็กเอาต์ซอร์สที่ใช้ pnpm อาจต้องอนุมัติและ rebuild dependency เนทีฟ:

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

สำหรับ embeddings ภายในเครื่องที่มีขั้นตอนน้อยกว่า ให้ใช้ผู้ให้บริการบริการภายในเครื่อง เช่น Ollama หรือ LM Studio แทน.

Was this useful?YesNo

Open issue