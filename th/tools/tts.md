---
title: ข้อความเป็นเสียงพูด
source_url: https://docs.openclaw.ai/th/tools/tts
scraped_at: 2026-05-25
---

OpenClaw สามารถแปลงคำตอบขาออกเป็นเสียงผ่าน **14 ผู้ให้บริการเสียงพูด** และส่งข้อความเสียงแบบเนทีฟบน Feishu, Matrix, Telegram และ WhatsApp, ไฟล์แนบเสียงในที่อื่นทั้งหมด และสตรีม PCM/Ulaw สำหรับโทรศัพท์และ Talk

TTS คือครึ่งส่วนเอาต์พุตเสียงพูดของโหมด `stt-tts` ของ Talk เซสชัน Talk แบบ `realtime` ที่เป็นเนทีฟของผู้ให้บริการจะสังเคราะห์เสียงภายในผู้ให้บริการแบบเรียลไทม์ แทนการเรียกเส้นทาง TTS นี้ ส่วนเซสชัน `transcription` จะไม่สังเคราะห์ เสียงตอบกลับของผู้ช่วย

## เริ่มต้นอย่างรวดเร็ว

* ### เลือกผู้ให้บริการ

OpenAI และ ElevenLabs เป็นตัวเลือกแบบโฮสต์ที่น่าเชื่อถือที่สุด Microsoft และ CLI ภายในเครื่องทำงานได้โดยไม่ต้องใช้คีย์ API ดู ตารางผู้ให้บริการ สำหรับรายการทั้งหมด

* ### ตั้งค่าคีย์ API

ส่งออก env var สำหรับผู้ให้บริการของคุณ (เช่น `OPENAI_API_KEY`, `ELEVENLABS_API_KEY`) Microsoft และ CLI ภายในเครื่องไม่ต้องใช้คีย์

* ### เปิดใช้ในการกำหนดค่า

ตั้งค่า `messages.tts.auto: "always"` และ `messages.tts.provider`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",    },  },}
[/code]

* ### ลองใช้ในแชต

`/tts status` แสดงสถานะปัจจุบัน `/tts audio Hello from OpenClaw` ส่งคำตอบเสียงแบบครั้งเดียว

## ผู้ให้บริการที่รองรับ

ผู้ให้บริการ | การยืนยันตัวตน | หมายเหตุ  
---|---|---  
**Azure Speech** | `AZURE_SPEECH_KEY` \+ `AZURE_SPEECH_REGION` (รวมถึง `AZURE_SPEECH_API_KEY`, `SPEECH_KEY`, `SPEECH_REGION`) | เอาต์พุตบันทึกเสียง Ogg/Opus แบบเนทีฟและโทรศัพท์  
**DeepInfra** | `DEEPINFRA_API_KEY` | TTS ที่เข้ากันได้กับ OpenAI ค่าเริ่มต้นเป็น `hexgrad/Kokoro-82M`  
**ElevenLabs** | `ELEVENLABS_API_KEY` หรือ `XI_API_KEY` | โคลนเสียง หลายภาษา กำหนดผลได้ด้วย `seed`; สตรีมสำหรับการเล่นเสียงใน Discord  
**Google Gemini** | `GEMINI_API_KEY` หรือ `GOOGLE_API_KEY` | Gemini API batch TTS; รับรู้ persona ผ่าน `promptTemplate: "audio-profile-v1"`  
**Gradium** | `GRADIUM_API_KEY` | เอาต์พุตบันทึกเสียงและโทรศัพท์  
**Inworld** | `INWORLD_API_KEY` | Streaming TTS API บันทึกเสียง Opus แบบเนทีฟและโทรศัพท์ PCM  
**Local CLI** | ไม่มี | เรียกใช้คำสั่ง TTS ภายในเครื่องที่กำหนดค่าไว้  
**Microsoft** | ไม่มี | TTS neural สาธารณะของ Edge ผ่าน `node-edge-tts` แบบพยายามให้ดีที่สุด ไม่มี SLA  
**MiniMax** | `MINIMAX_API_KEY` (หรือ Token Plan: `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`) | T2A v2 API ค่าเริ่มต้นเป็น `speech-2.8-hd`  
**OpenAI** | `OPENAI_API_KEY` | ใช้สำหรับสรุปอัตโนมัติด้วย; รองรับ `instructions` ของ persona  
**OpenRouter** | `OPENROUTER_API_KEY` (สามารถใช้ `models.providers.openrouter.apiKey` ซ้ำได้) | โมเดลเริ่มต้น `hexgrad/kokoro-82m`  
**Volcengine** | `VOLCENGINE_TTS_API_KEY` หรือ `BYTEPLUS_SEED_SPEECH_API_KEY` (AppID/token เดิม: `VOLCENGINE_TTS_APPID`/`_TOKEN`) | BytePlus Seed Speech HTTP API  
**Vydra** | `VYDRA_API_KEY` | ผู้ให้บริการรูปภาพ วิดีโอ และเสียงพูดที่ใช้ร่วมกัน  
**xAI** | `XAI_API_KEY` | xAI batch TTS **ไม่** รองรับบันทึกเสียง Opus แบบเนทีฟ  
**Xiaomi MiMo** | `XIAOMI_API_KEY` | MiMo TTS ผ่าน chat completions ของ Xiaomi  
  
หากกำหนดค่าผู้ให้บริการหลายราย รายที่เลือกจะถูกใช้ก่อน และรายอื่นจะเป็นตัวเลือกสำรอง สรุปอัตโนมัติใช้ `summaryModel` (หรือ `agents.defaults.model.primary`) ดังนั้น ผู้ให้บริการนั้นต้องผ่านการยืนยันตัวตนด้วยหากคุณยังเปิดใช้สรุปอยู่

## การกำหนดค่า

การกำหนดค่า TTS อยู่ภายใต้ `messages.tts` ใน `~/.openclaw/openclaw.json` เลือก preset แล้วปรับบล็อกผู้ให้บริการ:

### Azure Speech

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "azure-speech",  providers: {    "azure-speech": {      apiKey: "${AZURE_SPEECH_KEY}",      region: "eastus",      voice: "en-US-JennyNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      voiceNoteOutputFormat: "ogg-24khz-16bit-mono-opus",    },  },},},}
[/code]

### ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "elevenlabs",  providers: {    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      voiceId: "EXAVITQu4vr4xnSDxMaL",    },  },},},}
[/code]

### Google Gemini

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "google",  providers: {    google: {      apiKey: "${GEMINI_API_KEY}",      model: "gemini-3.1-flash-tts-preview",      voiceName: "Kore",      // Optional natural-language style prompts:      // audioProfile: "Speak in a calm, podcast-host tone.",      // speakerName: "Alex",    },  },},},}
[/code]

### Gradium

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "gradium",  providers: {    gradium: {      apiKey: "${GRADIUM_API_KEY}",      voiceId: "YTpq7expH9539ERJ",    },  },},},}
[/code]

### Inworld

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "inworld",  providers: {    inworld: {      apiKey: "${INWORLD_API_KEY}",      modelId: "inworld-tts-1.5-max",      voiceId: "Sarah",      temperature: 0.7,    },  },},},}
[/code]

### Local CLI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "tts-local-cli",  providers: {    "tts-local-cli": {      command: "say",      args: ["-o", "{{OutputPath}}", "{{Text}}"],      outputFormat: "wav",      timeoutMs: 120000,    },  },},},}
[/code]

### Microsoft (ไม่ต้องใช้คีย์)

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "microsoft",  providers: {    microsoft: {      enabled: true,      voice: "en-US-MichelleNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      rate: "+0%",      pitch: "+0%",    },  },},},}
[/code]

### MiniMax

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "minimax",  providers: {    minimax: {      apiKey: "${MINIMAX_API_KEY}",      model: "speech-2.8-hd",      voiceId: "English_expressive_narrator",      speed: 1.0,      vol: 1.0,      pitch: 0,    },  },},},}
[/code]

### OpenAI + ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openai",  summaryModel: "openai/gpt-4.1-mini",  modelOverrides: { enabled: true },  providers: {    openai: {      apiKey: "${OPENAI_API_KEY}",      model: "gpt-4o-mini-tts",      voice: "alloy",    },    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      voiceId: "EXAVITQu4vr4xnSDxMaL",      voiceSettings: { stability: 0.5, similarityBoost: 0.75, style: 0.0, useSpeakerBoost: true, speed: 1.0 },      applyTextNormalization: "auto",      languageCode: "en",    },  },},},}
[/code]

### OpenRouter

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openrouter",  providers: {    openrouter: {      apiKey: "${OPENROUTER_API_KEY}",      model: "hexgrad/kokoro-82m",      voice: "af_alloy",      responseFormat: "mp3",    },  },},},}
[/code]

### Volcengine

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "volcengine",  providers: {    volcengine: {      apiKey: "${VOLCENGINE_TTS_API_KEY}",      resourceId: "seed-tts-1.0",      voice: "en_female_anna_mars_bigtts",    },  },},},}
[/code]

### xAI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xai",  providers: {    xai: {      apiKey: "${XAI_API_KEY}",      voiceId: "eve",      language: "en",      responseFormat: "mp3",    },  },},},}
[/code]

### Xiaomi MiMo

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xiaomi",  providers: {    xiaomi: {      apiKey: "${XIAOMI_API_KEY}",      model: "mimo-v2.5-tts",      voice: "mimo_default",      format: "mp3",    },  },},},}
[/code]

### การแทนที่เสียงราย agent

ใช้ `agents.list[].tts` เมื่อ agent หนึ่งควรพูดด้วยผู้ให้บริการ เสียง โมเดล persona หรือโหมด Auto-TTS ที่แตกต่างกัน บล็อก agent จะ deep-merge ทับ `messages.tts` ดังนั้นข้อมูลประจำตัวของผู้ให้บริการสามารถอยู่ในการกำหนดค่าผู้ให้บริการส่วนกลางได้:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",      providers: {        elevenlabs: { apiKey: "${ELEVENLABS_API_KEY}", model: "eleven_multilingual_v2" },      },    },  },  agents: {    list: [      {        id: "reader",        tts: {          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL" },          },        },      },    ],  },}
[/code]

หากต้องการตรึงบุคลิกต่อเอเจนต์ ให้ตั้งค่า `agents.list[].tts.persona` ควบคู่กับการกำหนดค่าผู้ให้บริการ ซึ่งจะแทนที่ `messages.tts.persona` ส่วนกลางสำหรับเอเจนต์นั้นเท่านั้น

ลำดับความสำคัญสำหรับการตอบกลับอัตโนมัติ, `/tts audio`, `/tts status` และเครื่องมือเอเจนต์ `tts`:

  1. `messages.tts`
  2. `agents.list[].tts` ที่ใช้งานอยู่
  3. การแทนที่ของช่องทาง เมื่อช่องทางรองรับ `channels.<channel>.tts`
  4. การแทนที่ของบัญชี เมื่อช่องทางส่งผ่าน `channels.<channel>.accounts.<id>.tts`
  5. ค่ากำหนด `/tts` ภายในเครื่องสำหรับโฮสต์นี้
  6. คำสั่งกำกับแบบอินไลน์ `[[tts:...]]` เมื่อเปิดใช้ การแทนที่โดยโมเดล


การแทนที่ของช่องทางและบัญชีใช้รูปแบบเดียวกับ `messages.tts` และทำการผสานเชิงลึกทับเลเยอร์ก่อนหน้า ดังนั้นข้อมูลประจำตัวของผู้ให้บริการที่ใช้ร่วมกันสามารถอยู่ใน `messages.tts` ขณะที่ช่องทางหรือบัญชีบอทเปลี่ยนเฉพาะเสียง โมเดล บุคลิก หรือโหมดอัตโนมัติ:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "openai",      providers: {        openai: { apiKey: "${OPENAI_API_KEY}", model: "gpt-4o-mini-tts" },      },    },  },  channels: {    feishu: {      accounts: {        english: {          tts: {            providers: {              openai: { voice: "shimmer" },            },          },        },      },    },  },}
[/code]

## บุคลิก

**บุคลิก** คืออัตลักษณ์เสียงพูดที่เสถียรซึ่งนำไปใช้ข้ามผู้ให้บริการได้อย่างกำหนดแน่นอน สามารถระบุผู้ให้บริการที่ต้องการ กำหนดเจตนาพรอมป์ที่ไม่ผูกกับผู้ให้บริการ และเก็บการผูกค่าเฉพาะผู้ให้บริการสำหรับเสียง โมเดล เทมเพลตพรอมป์ seed และการตั้งค่าเสียง

### บุคลิกขั้นต่ำ

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "narrator",      personas: {        narrator: {          label: "Narrator",          provider: "elevenlabs",          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL", modelId: "eleven_multilingual_v2" },          },        },      },    },  },}
[/code]

### บุคลิกแบบเต็ม (พรอมป์ไม่ผูกกับผู้ให้บริการ)

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "alfred",      personas: {        alfred: {          label: "Alfred",          description: "Dry, warm British butler narrator.",          provider: "google",          fallbackPolicy: "preserve-persona",          prompt: {            profile: "A brilliant British butler. Dry, witty, warm, charming, emotionally expressive, never generic.",            scene: "A quiet late-night study. Close-mic narration for a trusted operator.",            sampleContext: "The speaker is answering a private technical request with concise confidence and dry warmth.",            style: "Refined, understated, lightly amused.",            accent: "British English.",            pacing: "Measured, with short dramatic pauses.",            constraints: ["Do not read configuration values aloud.", "Do not explain the persona."],          },          providers: {            google: {              model: "gemini-3.1-flash-tts-preview",              voiceName: "Algieba",              promptTemplate: "audio-profile-v1",            },            openai: { model: "gpt-4o-mini-tts", voice: "cedar" },            elevenlabs: {              voiceId: "voice_id",              modelId: "eleven_multilingual_v2",              seed: 42,              voiceSettings: {                stability: 0.65,                similarityBoost: 0.8,                style: 0.25,                useSpeakerBoost: true,                speed: 0.95,              },            },          },        },      },    },  },}
[/code]

### การกำหนดบุคลิก

บุคลิกที่ใช้งานอยู่จะถูกเลือกอย่างกำหนดแน่นอน:

  1. ค่ากำหนดภายในเครื่อง `/tts persona <id>` หากตั้งไว้
  2. `messages.tts.persona` หากตั้งไว้
  3. ไม่มีบุคลิก


การเลือกผู้ให้บริการใช้แบบระบุชัดเจนก่อน:

  1. การแทนที่โดยตรง (CLI, gateway, Talk, คำสั่งกำกับ TTS ที่อนุญาต)
  2. ค่ากำหนดภายในเครื่อง `/tts provider <id>`
  3. `provider` ของบุคลิกที่ใช้งานอยู่
  4. `messages.tts.provider`
  5. การเลือกอัตโนมัติจากรีจิสทรี


สำหรับความพยายามของผู้ให้บริการแต่ละครั้ง OpenClaw จะผสานการกำหนดค่าตามลำดับนี้:

  1. `messages.tts.providers.<id>`
  2. `messages.tts.personas.<persona>.providers.<id>`
  3. การแทนที่จากคำขอที่เชื่อถือได้
  4. การแทนที่จากคำสั่งกำกับ TTS ที่โมเดลส่งออกและอนุญาต


### ผู้ให้บริการใช้พรอมป์บุคลิกอย่างไร

ฟิลด์พรอมป์บุคลิก (`profile`, `scene`, `sampleContext`, `style`, `accent`, `pacing`, `constraints`) เป็นแบบ **ไม่ผูกกับผู้ให้บริการ** ผู้ให้บริการแต่ละรายตัดสินใจเองว่าจะใช้อย่างไร:

Google Gemini

ห่อฟิลด์พรอมป์บุคลิกในโครงสร้างพรอมป์ Gemini TTS **เฉพาะเมื่อ** การกำหนดค่าผู้ให้บริการ Google ที่มีผลตั้งค่า `promptTemplate: "audio-profile-v1"` หรือ `personaPrompt` ฟิลด์เก่า `audioProfile` และ `speakerName` ยังคงถูกเติมนำหน้าเป็นข้อความพรอมป์เฉพาะ Google แท็กเสียงแบบอินไลน์ เช่น `[whispers]` หรือ `[laughs]` ภายในบล็อก `[[tts:text]]` จะถูกเก็บไว้ภายในทรานสคริปต์ Gemini; OpenClaw ไม่ได้สร้างแท็กเหล่านี้

OpenAI

แมปฟิลด์พรอมป์บุคลิกไปยังฟิลด์คำขอ `instructions` **เฉพาะเมื่อ** ไม่มีการกำหนดค่า OpenAI `instructions` ไว้อย่างชัดเจน `instructions` ที่ระบุชัดเจนจะมีผลเหนือกว่าเสมอ

ผู้ให้บริการอื่น

ใช้เฉพาะการผูกค่าบุคลิกเฉพาะผู้ให้บริการภายใต้ `personas.<id>.providers.<provider>` ฟิลด์พรอมป์บุคลิกจะถูกละเว้น เว้นแต่ผู้ให้บริการจะติดตั้งการแมปพรอมป์บุคลิกของตนเอง

### นโยบาย fallback

`fallbackPolicy` ควบคุมพฤติกรรมเมื่อบุคลิก **ไม่มีการผูกค่า** สำหรับผู้ให้บริการที่พยายามใช้:

นโยบาย | พฤติกรรม  
---|---  
`preserve-persona` | **ค่าเริ่มต้น** ฟิลด์พรอมป์ที่ไม่ผูกกับผู้ให้บริการยังคงพร้อมใช้งาน ผู้ให้บริการอาจใช้หรือละเว้นฟิลด์เหล่านั้น  
`provider-defaults` | บุคลิกจะถูกละเว้นจากการเตรียมพรอมป์สำหรับความพยายามนั้น ผู้ให้บริการใช้ค่าเริ่มต้นแบบเป็นกลางของตนเอง ขณะที่การ fallback ไปยังผู้ให้บริการอื่นยังดำเนินต่อไป  
`fail` | ข้ามความพยายามของผู้ให้บริการนั้นด้วย `reasonCode: "not_configured"` และ `personaBinding: "missing"` ผู้ให้บริการ fallback ยังถูกลองต่อ  
  
คำขอ TTS ทั้งหมดจะล้มเหลวเฉพาะเมื่อผู้ให้บริการที่พยายามใช้ **ทุก** รายถูกข้ามหรือล้มเหลวเท่านั้น

การเลือกผู้ให้บริการของเซสชัน Talk มีขอบเขตเฉพาะเซสชัน ไคลเอนต์ Talk ควรเลือก id ผู้ให้บริการ, id โมเดล, id เสียง และ locale จาก `talk.catalog` และส่งผ่านเซสชัน Talk หรือคำขอส่งต่อ การเปิดเซสชันเสียงไม่ควรแก้ไข `messages.tts` หรือค่าเริ่มต้นผู้ให้บริการ Talk ส่วนกลาง

## คำสั่งกำกับโดยโมเดล

โดยค่าเริ่มต้น ผู้ช่วย **สามารถ** ส่งคำสั่งกำกับ `[[tts:...]]` เพื่อแทนที่เสียง โมเดล หรือความเร็วสำหรับการตอบกลับครั้งเดียว พร้อมบล็อก `[[tts:text]]...[[/tts:text]]` ที่เป็นทางเลือกสำหรับคิวการแสดงออกซึ่งควรปรากฏเฉพาะในเสียง:

textCopy code
[code]
    Here you go. [[tts:voiceId=pMsXgVXv3BLzUgSXRplE model=eleven_v3 speed=1.1]][[tts:text]](laughs) Read the song once more.[[/tts:text]]
[/code]

เมื่อ `messages.tts.auto` เป็น `"tagged"` **ต้องมีคำสั่งกำกับ** เพื่อเรียกใช้เสียง การส่งบล็อกแบบสตรีมจะลบคำสั่งกำกับออกจากข้อความที่มองเห็นได้ก่อนที่ช่องทางจะเห็น แม้เมื่อถูกแยกข้ามบล็อกที่อยู่ติดกัน

`provider=...` จะถูกละเว้น เว้นแต่ `modelOverrides.allowProvider: true` เมื่อการตอบกลับประกาศ `provider=...` คีย์อื่นในคำสั่งกำกับนั้นจะถูกแยกวิเคราะห์โดยผู้ให้บริการนั้นเท่านั้น คีย์ที่ไม่รองรับจะถูกลบออกและรายงานเป็นคำเตือนคำสั่งกำกับ TTS

**คีย์คำสั่งกำกับที่ใช้ได้:**

  * `provider` (id ผู้ให้บริการที่ลงทะเบียน ต้องมี `allowProvider: true`)
  * `voice` / `voiceName` / `voice_name` / `google_voice` / `voiceId`
  * `model` / `google_model`
  * `stability`, `similarityBoost`, `style`, `speed`, `useSpeakerBoost`
  * `vol` / `volume` (ระดับเสียง MiniMax, 0–10)
  * `pitch` (pitch จำนวนเต็มของ MiniMax, −12 ถึง 12; ค่าทศนิยมจะถูกตัดทิ้ง)
  * `emotion` (แท็กอารมณ์ Volcengine)
  * `applyTextNormalization` (`auto|on|off`)
  * `languageCode` (ISO 639-1)
  * `seed`


**ปิดใช้การแทนที่โดยโมเดลทั้งหมด:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: false } } } }
[/code]

**อนุญาตให้สลับผู้ให้บริการโดยยังคงกำหนดค่าปุ่มปรับอื่นได้:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: true, allowProvider: true, allowSeed: false } } } }
[/code]

## คำสั่ง slash

คำสั่งเดียวคือ `/tts` บน Discord, OpenClaw ยังลงทะเบียน `/voice` ด้วย เพราะ `/tts` เป็นคำสั่ง Discord ในตัว โดยข้อความ `/tts ...` ยังคงใช้งานได้

textCopy code
[code]
    /tts off | on | status/tts chat on | off | default/tts latest/tts provider <id>/tts persona <id> | off/tts limit <chars>/tts summary off/tts audio <text>
[/code]

หมายเหตุพฤติกรรม:

  * `/tts on` เขียนค่ากำหนด TTS ภายในเครื่องเป็น `always`; `/tts off` เขียนเป็น `off`
  * `/tts chat on|off|default` เขียนการแทนที่ auto-TTS ที่มีขอบเขตเฉพาะเซสชันสำหรับแชตปัจจุบัน
  * `/tts persona <id>` เขียนค่ากำหนดบุคลิกภายในเครื่อง; `/tts persona off` ล้างค่านั้น
  * `/tts latest` อ่านคำตอบล่าสุดของผู้ช่วยจากทรานสคริปต์เซสชันปัจจุบันและส่งเป็นเสียงหนึ่งครั้ง โดยเก็บเฉพาะแฮชของคำตอบนั้นในรายการเซสชันเพื่อระงับการส่งเสียงซ้ำ
  * `/tts audio` สร้างการตอบกลับเสียงแบบครั้งเดียว (ไม่ได้เปิด TTS)
  * `limit` และ `summary` ถูกเก็บไว้ใน **ค่ากำหนดภายในเครื่อง** ไม่ใช่การกำหนดค่าหลัก
  * `/tts status` รวมการวินิจฉัย fallback สำหรับความพยายามล่าสุด ได้แก่ `Fallback: <primary> -> <used>`, `Attempts: ...` และรายละเอียดต่อความพยายาม (`provider:outcome(reasonCode) latency`)
  * `/status` แสดงโหมด TTS ที่ใช้งานอยู่ พร้อมผู้ให้บริการ โมเดล เสียง และเมทาดาตา endpoint กำหนดเองที่ผ่านการล้างข้อมูลแล้วเมื่อเปิดใช้ TTS


## ค่ากำหนดต่อผู้ใช้

คำสั่ง slash เขียนการแทนที่ภายในเครื่องไปยัง `prefsPath` ค่าเริ่มต้นคือ `~/.openclaw/settings/tts.json`; แทนที่ด้วยตัวแปรสภาพแวดล้อม `OPENCLAW_TTS_PREFS` หรือ `messages.tts.prefsPath`

ฟิลด์ที่จัดเก็บ | ผล  
---|---  
`auto` | การแทนที่ auto-TTS ภายในเครื่อง (`always`, `off`, …)  
`provider` | การแทนที่ผู้ให้บริการหลักภายในเครื่อง  
`persona` | การแทนที่บุคลิกภายในเครื่อง  
`maxLength` | เกณฑ์การสรุป (ค่าเริ่มต้น `1500` อักขระ)  
`summarize` | สวิตช์การสรุป (ค่าเริ่มต้น `true`)  
  
ค่าเหล่านี้แทนที่การกำหนดค่าที่มีผลจาก `messages.tts` รวมกับบล็อก `agents.list[].tts` ที่ใช้งานอยู่สำหรับโฮสต์นั้น

## รูปแบบเอาต์พุต (คงที่)

การส่งเสียง TTS ขับเคลื่อนโดยความสามารถของช่องทาง Plugin ของช่องทางประกาศว่า TTS แบบเสียงพูดควรขอเป้าหมาย `voice-note` แบบเนทีฟจากผู้ให้บริการ หรือคงการสังเคราะห์ `audio-file` ปกติไว้และเพียงทำเครื่องหมายเอาต์พุตที่เข้ากันได้สำหรับการส่งเสียง

  * **ช่องทางที่รองรับข้อความเสียง** : การตอบกลับเป็นข้อความเสียงจะเลือกใช้ Opus ก่อน (`opus_48000_64` จาก ElevenLabs, `opus` จาก OpenAI) 
    * 48 kHz / 64 kbps เป็นจุดสมดุลที่ดีสำหรับข้อความเสียง
  * **Feishu / WhatsApp** : เมื่อการตอบกลับเป็นข้อความเสียงถูกสร้างเป็น MP3/WebM/WAV/M4A หรือเป็นไฟล์เสียงประเภทอื่นที่น่าจะใช่ Plugin ของช่องทางจะแปลงรหัสเป็น 48 kHz Ogg/Opus ด้วย `ffmpeg` ก่อนส่งข้อความเสียงแบบเนทีฟ WhatsApp ส่ง ผลลัพธ์ผ่านเพย์โหลด `audio` ของ Baileys พร้อม `ptt: true` และ `audio/ogg; codecs=opus` หากการแปลงล้มเหลว Feishu จะได้รับไฟล์เดิม เป็นไฟล์แนบ ส่วน WhatsApp จะส่งล้มเหลวแทนการโพสต์เพย์โหลด PTT ที่ไม่เข้ากัน
  * **ช่องทางอื่น** : MP3 (`mp3_44100_128` จาก ElevenLabs, `mp3` จาก OpenAI) 
    * 44.1 kHz / 128 kbps เป็นสมดุลเริ่มต้นสำหรับความชัดเจนของเสียงพูด
  * **MiniMax** : MP3 (โมเดล `speech-2.8-hd`, อัตราสุ่มตัวอย่าง 32 kHz) สำหรับไฟล์แนบเสียงปกติ สำหรับเป้าหมายข้อความเสียงที่ช่องทางประกาศไว้ OpenClaw จะแปลงรหัส MiniMax MP3 เป็น Opus 48 kHz ด้วย `ffmpeg` ก่อนส่งมอบเมื่อช่องทางประกาศว่ารองรับการแปลงรหัส
  * **Xiaomi MiMo** : ใช้ MP3 โดยค่าเริ่มต้น หรือ WAV เมื่อกำหนดค่าไว้ สำหรับเป้าหมายข้อความเสียงที่ช่องทางประกาศไว้ OpenClaw จะแปลงรหัสเอาต์พุตของ Xiaomi เป็น Opus 48 kHz ด้วย `ffmpeg` ก่อนส่งมอบเมื่อช่องทางประกาศว่ารองรับการแปลงรหัส
  * **CLI ภายในเครื่อง** : ใช้ `outputFormat` ที่กำหนดค่าไว้ เป้าหมายข้อความเสียงจะถูก แปลงเป็น Ogg/Opus และเอาต์พุตโทรศัพท์จะถูกแปลงเป็น PCM โมโนดิบ 16 kHz ด้วย `ffmpeg`
  * **Google Gemini** : TTS ของ Gemini API ส่งคืน PCM ดิบ 24 kHz OpenClaw ห่อหุ้มเป็น WAV สำหรับไฟล์แนบเสียง แปลงรหัสเป็น Opus 48 kHz สำหรับเป้าหมายข้อความเสียง และส่งคืน PCM โดยตรงสำหรับ Talk/โทรศัพท์
  * **Gradium** : WAV สำหรับไฟล์แนบเสียง, Opus สำหรับเป้าหมายข้อความเสียง และ `ulaw_8000` ที่ 8 kHz สำหรับโทรศัพท์
  * **Inworld** : MP3 สำหรับไฟล์แนบเสียงปกติ, `OGG_OPUS` แบบเนทีฟสำหรับเป้าหมายข้อความเสียง และ `PCM` ดิบที่ 22050 Hz สำหรับ Talk/โทรศัพท์
  * **xAI** : ใช้ MP3 โดยค่าเริ่มต้น; `responseFormat` อาจเป็น `mp3`, `wav`, `pcm`, `mulaw` หรือ `alaw` OpenClaw ใช้จุดปลายทาง TTS แบบ REST ชุดงานของ xAI และส่งคืนไฟล์แนบเสียงที่สมบูรณ์ เส้นทางผู้ให้บริการนี้ไม่ใช้ TTS แบบสตรีมผ่าน WebSocket ของ xAI เส้นทางนี้ไม่รองรับรูปแบบข้อความเสียง Opus แบบเนทีฟ
  * **Microsoft** : ใช้ `microsoft.outputFormat` (ค่าเริ่มต้น `audio-24khz-48kbitrate-mono-mp3`) 
    * ทรานสปอร์ตที่รวมมารองรับ `outputFormat` แต่บริการไม่ได้มีทุกรูปแบบให้ใช้
    * ค่าเอาต์พุตรูปแบบเป็นไปตามรูปแบบเอาต์พุตของ Microsoft Speech (รวมถึง Ogg/WebM Opus)
    * Telegram `sendVoice` รองรับ OGG/MP3/M4A; ใช้ OpenAI/ElevenLabs หากคุณต้องการ ข้อความเสียง Opus ที่รับประกันได้
    * หากรูปแบบเอาต์พุต Microsoft ที่กำหนดค่าไว้ล้มเหลว OpenClaw จะลองใหม่ด้วย MP3


รูปแบบเอาต์พุตของ OpenAI/ElevenLabs ถูกกำหนดตายตัวตามช่องทาง (ดูด้านบน)

## ลักษณะการทำงานของ Auto-TTS

เมื่อเปิดใช้ `messages.tts.auto` แล้ว OpenClaw จะ:

  * ข้าม TTS หากการตอบกลับมีสื่ออยู่แล้วหรือมีคำสั่ง `MEDIA:`
  * ข้ามการตอบกลับที่สั้นมาก (ต่ำกว่า 10 อักขระ)
  * สรุปการตอบกลับยาวเมื่อเปิดใช้การสรุป โดยใช้ `summaryModel` (หรือ `agents.defaults.model.primary`)
  * แนบเสียงที่สร้างขึ้นกับการตอบกลับ
  * ใน `mode: "final"` ยังคงส่ง TTS เฉพาะเสียงสำหรับการตอบกลับสุดท้ายแบบสตรีม หลังจากสตรีมข้อความเสร็จสิ้นแล้ว สื่อที่สร้างขึ้นจะผ่านการทำให้สื่อของช่องทาง เป็นปกติแบบเดียวกับไฟล์แนบการตอบกลับทั่วไป


หากการตอบกลับเกิน `maxLength` และการสรุปถูกปิดอยู่ (หรือไม่มีคีย์ API สำหรับ โมเดลสรุป) จะข้ามเสียงและส่งการตอบกลับข้อความปกติ

textCopy code
[code]
    Reply -> TTS enabled?  no  -> send text  yes -> has media / MEDIA: / short?          yes -> send text          no  -> length > limit?                   no  -> TTS -> attach audio                   yes -> summary enabled?                            no  -> send text                            yes -> summarize -> TTS -> attach audio
[/code]

## รูปแบบเอาต์พุตตามช่องทาง

เป้าหมาย | รูปแบบ  
---|---  
Feishu / Matrix / Telegram / WhatsApp | การตอบกลับเป็นข้อความเสียงจะเลือกใช้ **Opus** ก่อน (`opus_48000_64` จาก ElevenLabs, `opus` จาก OpenAI) 48 kHz / 64 kbps สมดุลระหว่างความชัดเจนและขนาด  
ช่องทางอื่น | **MP3** (`mp3_44100_128` จาก ElevenLabs, `mp3` จาก OpenAI) ค่าเริ่มต้น 44.1 kHz / 128 kbps สำหรับเสียงพูด  
Talk / โทรศัพท์ | **PCM** แบบเนทีฟของผู้ให้บริการ (Inworld 22050 Hz, Google 24 kHz) หรือ `ulaw_8000` จาก Gradium สำหรับโทรศัพท์  
  
หมายเหตุตามผู้ให้บริการ:

  * **การแปลงรหัสของ Feishu / WhatsApp:** เมื่อการตอบกลับเป็นข้อความเสียงมาถึงเป็น MP3/WebM/WAV/M4A Plugin ของช่องทางจะแปลงรหัสเป็น Ogg/Opus 48 kHz ด้วย `ffmpeg` WhatsApp ส่งผ่าน Baileys พร้อม `ptt: true` และ `audio/ogg; codecs=opus` หากการแปลงล้มเหลว: Feishu จะย้อนกลับไปแนบไฟล์เดิม ส่วน WhatsApp จะส่งล้มเหลวแทนการโพสต์เพย์โหลด PTT ที่ไม่เข้ากัน
  * **MiniMax / Xiaomi MiMo:** ค่าเริ่มต้นเป็น MP3 (32 kHz สำหรับ MiniMax `speech-2.8-hd`); แปลงรหัสเป็น Opus 48 kHz สำหรับเป้าหมายข้อความเสียงผ่าน `ffmpeg`
  * **CLI ภายในเครื่อง:** ใช้ `outputFormat` ที่กำหนดค่าไว้ เป้าหมายข้อความเสียงถูกแปลงเป็น Ogg/Opus และเอาต์พุตโทรศัพท์เป็น PCM โมโนดิบ 16 kHz
  * **Google Gemini:** ส่งคืน PCM ดิบ 24 kHz OpenClaw ห่อหุ้มเป็น WAV สำหรับไฟล์แนบ แปลงรหัสเป็น Opus 48 kHz สำหรับเป้าหมายข้อความเสียง และส่งคืน PCM โดยตรงสำหรับ Talk/โทรศัพท์
  * **Inworld:** ไฟล์แนบ MP3, ข้อความเสียง `OGG_OPUS` แบบเนทีฟ, `PCM` ดิบ 22050 Hz สำหรับ Talk/โทรศัพท์
  * **xAI:** ใช้ MP3 โดยค่าเริ่มต้น; `responseFormat` อาจเป็น `mp3|wav|pcm|mulaw|alaw` ใช้จุดปลายทาง REST แบบชุดงานของ xAI — **ไม่** ใช้ TTS ผ่าน WebSocket แบบสตรีม ไม่รองรับรูปแบบข้อความเสียง Opus แบบเนทีฟ
  * **Microsoft:** ใช้ `microsoft.outputFormat` (ค่าเริ่มต้น `audio-24khz-48kbitrate-mono-mp3`) Telegram `sendVoice` รองรับ OGG/MP3/M4A; ใช้ OpenAI/ElevenLabs หากคุณต้องการข้อความเสียง Opus ที่รับประกันได้ หากรูปแบบ Microsoft ที่กำหนดค่าไว้ล้มเหลว OpenClaw จะลองใหม่ด้วย MP3


รูปแบบเอาต์พุตของ OpenAI และ ElevenLabs ถูกกำหนดตายตัวตามช่องทางดังที่แสดงไว้ด้านบน

## อ้างอิงฟิลด์

Top-level messages.tts.*

โหมด Auto-TTS `inbound` ส่งเสียงหลังจากข้อความเสียงขาเข้าเท่านั้น; `tagged` ส่งเสียงเฉพาะเมื่อการตอบกลับมีคำสั่ง `[[tts:...]]` หรือบล็อก `[[tts:text]]`

สวิตช์เดิม `openclaw doctor --fix` จะย้ายค่านี้ไปยัง `auto`

`"all"` รวมการตอบกลับจากเครื่องมือ/บล็อกเพิ่มเติมจากการตอบกลับสุดท้าย

รหัสผู้ให้บริการเสียงพูด เมื่อไม่ได้ตั้งค่า OpenClaw จะใช้ผู้ให้บริการรายแรกที่กำหนดค่าไว้ตามลำดับการเลือกอัตโนมัติของรีจิสทรี ค่าเดิม `provider: "edge"` จะถูกเขียนใหม่เป็น `"microsoft"` โดย `openclaw doctor --fix`

รหัสเพอร์โซนาที่ใช้งานอยู่จาก `personas` ทำให้เป็นตัวพิมพ์เล็ก

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBlcnNvbmFzLjxpZA " type="object"> อัตลักษณ์เสียงพูดที่เสถียร ฟิลด์: `label`, `description`, `provider`, `fallbackPolicy`, `prompt`, `providers.<provider>` ดู เพอร์โซนา

โมเดลราคาถูกสำหรับสรุปอัตโนมัติ; ค่าเริ่มต้นเป็น `agents.defaults.model.primary` รองรับ `provider/model` หรือชื่อแทนโมเดลที่กำหนดค่าไว้

อนุญาตให้โมเดลปล่อยคำสั่ง TTS `enabled` มีค่าเริ่มต้นเป็น `true`; `allowProvider` มีค่าเริ่มต้นเป็น `false`

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb3ZpZGVycy48aWQ " type="object"> การตั้งค่าที่ผู้ให้บริการเป็นเจ้าของโดยใช้รหัสผู้ให้บริการเสียงพูดเป็นคีย์ บล็อกตรงแบบเดิม (`messages.tts.openai`, `.elevenlabs`, `.microsoft`, `.edge`) จะถูกเขียนใหม่โดย `openclaw doctor --fix`; ให้คอมมิตเฉพาะ `messages.tts.providers.<id>`

เพดานสูงสุดแบบแข็งสำหรับจำนวนอักขระอินพุต TTS `/tts audio` จะล้มเหลวหากเกินค่านี้

เวลาหมดเวลาของคำขอเป็นมิลลิวินาที

แทนที่เส้นทาง JSON การตั้งค่าภายในเครื่อง (ผู้ให้บริการ/ขีดจำกัด/สรุป) ค่าเริ่มต้น `~/.openclaw/settings/tts.json`

Azure Speech

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg ตัวแปรสภาพแวดล้อม: `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY` หรือ `SPEECH_KEY` OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlZ2lvbiIgdHlwZT0ic3RyaW5nIg ภูมิภาค Azure Speech (เช่น `eastus`) ตัวแปรสภาพแวดล้อม: `AZURE_SPEECH_REGION` หรือ `SPEECH_REGION` OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVuZHBvaW50IiB0eXBlPSJzdHJpbmci การแทนที่จุดปลายทาง Azure Speech แบบไม่บังคับ (นามแฝง `baseUrl`) OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci ShortName ของเสียง Azure ค่าเริ่มต้น `en-US-JennyNeural` OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI รหัสภาษา SSML ค่าเริ่มต้น `en-US` OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Azure `X-Microsoft-OutputFormat` สำหรับเสียงมาตรฐาน ค่าเริ่มต้น `audio-24khz-48kbitrate-mono-mp3` OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTm90ZU91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Azure `X-Microsoft-OutputFormat` สำหรับเอาต์พุตข้อความเสียง ค่าเริ่มต้น `ogg-24khz-16bit-mono-opus` OPENCLAW_DOCS_MARKER:paramClose:

ElevenLabs

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg ย้อนกลับไปใช้ `ELEVENLABS_API_KEY` หรือ `XI_API_KEY` OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci รหัสโมเดล (เช่น `eleven_multilingual_v2`, `eleven_v3`) OPENCLAW_DOCS_MARKER:paramClose:

`stability`, `similarityBoost`, `style` (แต่ละค่า `0..1`), `useSpeakerBoost` (`true|false`), `speed` (`0.5..2.0`, `1.0` = ปกติ)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlQ29kZSIgdHlwZT0ic3RyaW5nIg ISO 639-1 แบบ 2 ตัวอักษร (เช่น `en`, `de`) OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNlZWQiIHR5cGU9Im51bWJlciI จำนวนเต็ม `0..4294967295` สำหรับความกำหนดซ้ำได้แบบพยายามให้ดีที่สุด OPENCLAW_DOCS_MARKER:paramClose:

Google Gemini

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg ย้อนกลับไปใช้ `GEMINI_API_KEY` / `GOOGLE_API_KEY` หากละไว้ TTS สามารถใช้ `models.providers.google.apiKey` ซ้ำก่อนย้อนกลับไปใช้ตัวแปรสภาพแวดล้อม OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci โมเดล Gemini TTS ค่าเริ่มต้น `gemini-3.1-flash-tts-preview` OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTmFtZSIgdHlwZT0ic3RyaW5nIg ชื่อเสียงสำเร็จรูปของ Gemini ค่าเริ่มต้น `Kore` นามแฝง: `voice` OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb21wdFRlbXBsYXRlIiB0eXBlPSciYXVkaW8tcHJvZmlsZS12MSIn ตั้งเป็น `audio-profile-v1` เพื่อห่อหุ้มฟิลด์พรอมต์เพอร์โซนาที่ใช้งานอยู่ในโครงสร้างพรอมต์ Gemini TTS ที่กำหนดซ้ำได้ OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI ยอมรับเฉพาะ `https://generativelanguage.googleapis.com` OPENCLAW_DOCS_MARKER:paramClose:

Gradium

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `GRADIUM_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI ค่าเริ่มต้น `https://api.gradium.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI ค่าเริ่มต้น Emma (`YTpq7expH9539ERJ`). OPENCLAW_DOCS_MARKER:paramClose:

Inworld

### หลักของ Inworld

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `INWORLD_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI ค่าเริ่มต้น `https://api.inworld.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsSWQiIHR5cGU9InN0cmluZyI ค่าเริ่มต้น `inworld-tts-1.5-max` นอกจากนี้ยังมี: `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI ค่าเริ่มต้น `Sarah`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRlbXBlcmF0dXJlIiB0eXBlPSJudW1iZXIi อุณหภูมิการสุ่มตัวอย่าง `0..2`. OPENCLAW_DOCS_MARKER:paramClose:

CLI ภายในเครื่อง (tts-local-cli)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFyZ3MiIHR5cGU9InN0cmluZ1tdIg อาร์กิวเมนต์คำสั่ง รองรับตัวแทนที่ `{{Text}}`, `{{OutputPath}}`, `{{OutputDir}}`, `{{OutputBase}}`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0nIm1wMyIgfCAib3B1cyIgfCAid2F2Iic รูปแบบเอาต์พุต CLI ที่คาดไว้ ค่าเริ่มต้น `mp3` สำหรับไฟล์แนบเสียง. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg ระยะหมดเวลาของคำสั่งเป็นมิลลิวินาที ค่าเริ่มต้น `120000`. OPENCLAW_DOCS_MARKER:paramClose:

Microsoft (ไม่มีคีย์ API)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci ชื่อเสียง neural ของ Microsoft (เช่น `en-US-MichelleNeural`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI รหัสภาษา (เช่น `en-US`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg รูปแบบเอาต์พุตของ Microsoft ค่าเริ่มต้น `audio-24khz-48kbitrate-mono-mp3` การขนส่งที่บันเดิลและอิง Edge ไม่รองรับทุกรูปแบบ. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJhdGUgLyBwaXRjaCAvIHZvbHVtZSIgdHlwZT0ic3RyaW5nIg สตริงเปอร์เซ็นต์ (เช่น `+10%`, `-5%`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVkZ2UuKiIgdHlwZT0ib2JqZWN0IiBkZXByZWNhdGVk นามแฝงแบบเดิม เรียกใช้ `openclaw doctor --fix` เพื่อเขียนการกำหนดค่าที่บันทึกไว้ใหม่เป็น `providers.microsoft`. OPENCLAW_DOCS_MARKER:paramClose:

MiniMax

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg ย้อนกลับไปใช้ `MINIMAX_API_KEY` การตรวจสอบสิทธิ์ Token Plan ผ่าน `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY` หรือ `MINIMAX_CODING_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI ค่าเริ่มต้น `https://api.minimax.io` Env: `MINIMAX_API_HOST`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci ค่าเริ่มต้น `speech-2.8-hd` Env: `MINIMAX_TTS_MODEL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI ค่าเริ่มต้น `English_expressive_narrator` Env: `MINIMAX_TTS_VOICE_ID`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWVkIiB0eXBlPSJudW1iZXIi `0.5..2.0` ค่าเริ่มต้น `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvbCIgdHlwZT0ibnVtYmVyIg `(0, 10]` ค่าเริ่มต้น `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBpdGNoIiB0eXBlPSJudW1iZXIi จำนวนเต็ม `-12..12` ค่าเริ่มต้น `0` ค่าทศนิยมจะถูกตัดก่อนส่งคำขอ. OPENCLAW_DOCS_MARKER:paramClose:

OpenAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg ย้อนกลับไปใช้ `OPENAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci รหัสโมเดล TTS ของ OpenAI (เช่น `gpt-4o-mini-tts`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci ชื่อเสียง (เช่น `alloy`, `cedar`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imluc3RydWN0aW9ucyIgdHlwZT0ic3RyaW5nIg ฟิลด์ `instructions` ของ OpenAI แบบชัดเจน เมื่อตั้งค่าแล้ว ฟิลด์พรอมป์ persona จะ **ไม่** ถูกแมปโดยอัตโนมัติ. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImV4dHJhQm9keSAvIGV4dHJhX2JvZHkiIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 ">ฟิลด์ JSON เพิ่มเติมที่ผสานเข้าในเนื้อหาคำขอ `/audio/speech` หลังจากฟิลด์ TTS ของ OpenAI ที่สร้างขึ้น ใช้สิ่งนี้สำหรับ endpoint ที่เข้ากันได้กับ OpenAI เช่น Kokoro ซึ่งต้องใช้คีย์เฉพาะผู้ให้บริการอย่าง `lang`; คีย์ prototype ที่ไม่ปลอดภัยจะถูกละเว้น. OPENCLAW_DOCS_MARKER:paramClose:

แทนที่ endpoint TTS ของ OpenAI ลำดับการแก้ไข: config → `OPENAI_TTS_BASE_URL` → `https://api.openai.com/v1` ค่าที่ไม่ใช่ค่าเริ่มต้นจะถือเป็น endpoint TTS ที่เข้ากันได้กับ OpenAI ดังนั้นจึงยอมรับชื่อโมเดลและชื่อเสียงแบบกำหนดเอง.

OpenRouter

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `OPENROUTER_API_KEY` สามารถใช้ `models.providers.openrouter.apiKey` ซ้ำได้. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI ค่าเริ่มต้น `https://openrouter.ai/api/v1` ค่าเดิม `https://openrouter.ai/v1` จะถูกทำให้เป็นมาตรฐาน. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci ค่าเริ่มต้น `hexgrad/kokoro-82m` นามแฝง: `modelId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci ค่าเริ่มต้น `af_alloy` นามแฝง: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJwY20iJw ค่าเริ่มต้น `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Volcengine (BytePlus Seed Speech)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `VOLCENGINE_TTS_API_KEY` หรือ `BYTEPLUS_SEED_SPEECH_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc291cmNlSWQiIHR5cGU9InN0cmluZyI ค่าเริ่มต้น `seed-tts-1.0` Env: `VOLCENGINE_TTS_RESOURCE_ID` ใช้ `seed-tts-2.0` เมื่อโปรเจ็กต์ของคุณมีสิทธิ์ TTS 2.0. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcEtleSIgdHlwZT0ic3RyaW5nIg ส่วนหัวคีย์แอป ค่าเริ่มต้น `aGjiRDfUWi` Env: `VOLCENGINE_TTS_APP_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI แทนที่ endpoint HTTP ของ Seed Speech TTS Env: `VOLCENGINE_TTS_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci ประเภทเสียง ค่าเริ่มต้น `en_female_anna_mars_bigtts` Env: `VOLCENGINE_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcElkIC8gdG9rZW4gLyBjbHVzdGVyIiB0eXBlPSJzdHJpbmciIGRlcHJlY2F0ZWQ ฟิลด์ Volcengine Speech Console แบบเดิม Env: `VOLCENGINE_TTS_APPID`, `VOLCENGINE_TTS_TOKEN`, `VOLCENGINE_TTS_CLUSTER` (ค่าเริ่มต้น `volcano_tts`). OPENCLAW_DOCS_MARKER:paramClose:

xAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `XAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI ค่าเริ่มต้น `https://api.x.ai/v1` Env: `XAI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI ค่าเริ่มต้น `eve` เสียงสด: `ara`, `eve`, `leo`, `rex`, `sal`, `una`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlIiB0eXBlPSJzdHJpbmci รหัสภาษา BCP-47 หรือ `auto` ค่าเริ่มต้น `en`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJ3YXYiIHwgInBjbSIgfCAibXVsYXciIHwgImFsYXciJw ค่าเริ่มต้น `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Xiaomi MiMo

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `XIAOMI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI ค่าเริ่มต้น `https://api.xiaomimimo.com/v1` Env: `XIAOMI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci ค่าเริ่มต้น `mimo-v2.5-tts` Env: `XIAOMI_TTS_MODEL` ยังรองรับ `mimo-v2-tts`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci ค่าเริ่มต้น `mimo_default` Env: `XIAOMI_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImZvcm1hdCIgdHlwZT0nIm1wMyIgfCAid2F2Iic ค่าเริ่มต้น `mp3` Env: `XIAOMI_TTS_FORMAT`. OPENCLAW_DOCS_MARKER:paramClose:

## เครื่องมือ Agent

เครื่องมือ `tts` แปลงข้อความเป็นเสียงพูดและส่งคืนไฟล์แนบเสียงสำหรับ การส่งคำตอบ บน Feishu, Matrix, Telegram และ WhatsApp เสียงจะถูก ส่งเป็นข้อความเสียงแทนไฟล์แนบ Feishu และ WhatsApp สามารถแปลงเอาต์พุต TTS ที่ไม่ใช่ Opus บนเส้นทางนี้ได้เมื่อมี `ffmpeg` พร้อมใช้งาน.

WhatsApp ส่งเสียงผ่าน Baileys เป็นบันทึกเสียง PTT (`audio` พร้อม `ptt: true`) และส่งข้อความที่มองเห็นได้ **แยกต่างหาก** จากเสียง PTT เพราะ ไคลเอนต์ไม่ได้แสดงคำบรรยายบนบันทึกเสียงอย่างสม่ำเสมอ.

เครื่องมือนี้ยอมรับฟิลด์ `channel` และ `timeoutMs` ที่ไม่บังคับ; `timeoutMs` คือ ระยะหมดเวลาคำขอผู้ให้บริการต่อการเรียกหนึ่งครั้งเป็นมิลลิวินาที.

## Gateway RPC

เมธอด | วัตถุประสงค์  
---|---  
`tts.status` | อ่านสถานะ TTS ปัจจุบันและความพยายามล่าสุด.  
`tts.enable` | ตั้งค่าการกำหนดลักษณะอัตโนมัติภายในเครื่องเป็น `always`.  
`tts.disable` | ตั้งค่าการกำหนดลักษณะอัตโนมัติภายในเครื่องเป็น `off`.  
`tts.convert` | แปลงข้อความเป็นเสียงแบบครั้งเดียว.  
`tts.setProvider` | ตั้งค่าการกำหนดลักษณะผู้ให้บริการภายในเครื่อง.  
`tts.setPersona` | ตั้งค่าการกำหนดลักษณะ persona ภายในเครื่อง.  
`tts.providers` | แสดงรายการผู้ให้บริการที่กำหนดค่าไว้และสถานะ.  
  
## ลิงก์บริการ

  * [คู่มือข้อความเป็นเสียงพูดของ OpenAI](<https://platform.openai.com/docs/guides/text-to-speech>)
  * [เอกสารอ้างอิง OpenAI Audio API](<https://platform.openai.com/docs/api-reference/audio>)
  * [Azure Speech REST ข้อความเป็นเสียงพูด](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)
  * [ผู้ให้บริการ Azure Speech](</th/providers/azure-speech>)
  * [ข้อความเป็นเสียงพูดของ ElevenLabs](<https://elevenlabs.io/docs/api-reference/text-to-speech>)
  * [การตรวจสอบสิทธิ์ของ ElevenLabs](<https://elevenlabs.io/docs/api-reference/authentication>)
  * [Gradium](</th/providers/gradium>)
  * [Inworld TTS API](<https://docs.inworld.ai/tts/tts>)
  * [MiniMax T2A v2 API](<https://platform.minimaxi.com/document/T2A%20V2>)
  * [Volcengine TTS HTTP API](</th/providers/volcengine#text-to-speech>)
  * [การสังเคราะห์เสียงพูดของ Xiaomi MiMo](</th/providers/xiaomi#text-to-speech>)
  * [node-edge-tts](<https://github.com/SchneeHertz/node-edge-tts>)
  * [รูปแบบเอาต์พุต Microsoft Speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech#audio-outputs>)
  * [ข้อความเป็นเสียงพูดของ xAI](<https://docs.x.ai/developers/rest-api-reference/inference/voice#text-to-speech-rest>)


## ที่เกี่ยวข้อง

  * [ภาพรวมสื่อ](</th/tools/media-overview>)
  * [การสร้างเพลง](</th/tools/music-generation>)
  * [การสร้างวิดีโอ](</th/tools/video-generation>)
  * [คำสั่ง Slash](</th/tools/slash-commands>)
  * [Plugin การโทรด้วยเสียง](</th/plugins/voice-call>)


Was this useful?YesNo