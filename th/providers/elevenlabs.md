---
title: ElevenLabs
source_url: https://docs.openclaw.ai/th/providers/elevenlabs
scraped_at: 2026-05-25
---

OpenClaw ใช้ ElevenLabs สำหรับการแปลงข้อความเป็นเสียง, การแปลงเสียงเป็นข้อความแบบแบตช์ด้วย Scribe v2 และ STT แบบสตรีมมิงด้วย Scribe v2 Realtime

ความสามารถ | พื้นที่ใช้งานของ OpenClaw | ค่าเริ่มต้น  
---|---|---  
การแปลงข้อความเป็นเสียง | `messages.tts` / `talk` | `eleven_multilingual_v2`  
การแปลงเสียงเป็นข้อความแบบแบตช์ | `tools.media.audio` | `scribe_v2`  
การแปลงเสียงเป็นข้อความแบบสตรีมมิง | การสตรีม Voice Call หรือ Google Meet `realtime.transcriptionProvider` | `scribe_v2_realtime`  
  
## การยืนยันตัวตน

ตั้งค่า `ELEVENLABS_API_KEY` ในสภาพแวดล้อม และยังยอมรับ `XI_API_KEY` เพื่อ ความเข้ากันได้กับเครื่องมือ ElevenLabs ที่มีอยู่

bashCopy code
[code]
    export ELEVENLABS_API_KEY="..."
[/code]

## การแปลงข้อความเป็นเสียง

json5Copy code
[code]
    {  messages: {    tts: {      providers: {        elevenlabs: {          apiKey: "${ELEVENLABS_API_KEY}",          voiceId: "pMsXgVXv3BLzUgSXRplE",          modelId: "eleven_multilingual_v2",        },      },    },  },}
[/code]

ตั้งค่า `modelId` เป็น `eleven_v3` เพื่อใช้ ElevenLabs v3 TTS โดย OpenClaw คง `eleven_multilingual_v2` เป็นค่าเริ่มต้นสำหรับการติดตั้งที่มีอยู่

ช่องเสียง Discord ใช้ปลายทาง TTS แบบสตรีมมิงของ ElevenLabs เมื่อ ElevenLabs เป็น ผู้ให้บริการ `voice.tts`/`messages.tts` ที่เลือกไว้ การเล่นจะเริ่มจากสตรีมเสียง ที่ส่งกลับมาแทนการรอให้ OpenClaw ดาวน์โหลดและเขียนไฟล์เสียงทั้งหมดก่อน `latencyTier` จะจับคู่กับพารามิเตอร์คิวรี `optimize_streaming_latency` ของ ElevenLabs สำหรับโมเดลที่รองรับ OpenClaw จะละพารามิเตอร์นั้นสำหรับ `eleven_v3` ซึ่งปฏิเสธพารามิเตอร์นี้

## การแปลงเสียงเป็นข้อความ

ใช้ Scribe v2 สำหรับไฟล์แนบเสียงขาเข้าและส่วนเสียงพูดที่บันทึกไว้แบบสั้น:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "elevenlabs", model: "scribe_v2" }],      },    },  },}
[/code]

OpenClaw ส่งเสียงแบบ multipart ไปยัง ElevenLabs `/v1/speech-to-text` พร้อม `model_id: "scribe_v2"` คำใบ้ภาษาจะจับคู่กับ `language_code` เมื่อมีอยู่

## STT แบบสตรีมมิง

Plugin `elevenlabs` ที่รวมมาด้วยจะลงทะเบียน Scribe v2 Realtime สำหรับการถอดเสียงแบบสตรีมมิงของ Voice Call และ โหมดเอเจนต์ Google Meet

การตั้งค่า | เส้นทางการกำหนดค่า | ค่าเริ่มต้น  
---|---|---  
คีย์ API | `plugins.entries.voice-call.config.streaming.providers.elevenlabs.apiKey` | ถอยกลับไปใช้ `ELEVENLABS_API_KEY` / `XI_API_KEY`  
โมเดล | `...elevenlabs.modelId` | `scribe_v2_realtime`  
รูปแบบเสียง | `...elevenlabs.audioFormat` | `ulaw_8000`  
อัตราสุ่มตัวอย่าง | `...elevenlabs.sampleRate` | `8000`  
กลยุทธ์การคอมมิต | `...elevenlabs.commitStrategy` | `vad`  
ภาษา | `...elevenlabs.languageCode` | (ไม่ได้ตั้งค่า)  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "elevenlabs",            providers: {              elevenlabs: {                apiKey: "${ELEVENLABS_API_KEY}",                audioFormat: "ulaw_8000",                commitStrategy: "vad",                languageCode: "en",              },            },          },        },      },    },  },}
[/code]

สำหรับโหมดเอเจนต์ Google Meet ให้ตั้งค่า `plugins.entries.google-meet.config.realtime.transcriptionProvider` เป็น `"elevenlabs"` และกำหนดค่าบล็อกผู้ให้บริการเดียวกันภายใต้ `plugins.entries.google-meet.config.realtime.providers.elevenlabs`

## ที่เกี่ยวข้อง

  * [การแปลงข้อความเป็นเสียง](</th/tools/tts>)
  * [Google Meet](</th/plugins/google-meet>)
  * [การเลือกโมเดล](</th/concepts/model-providers>)


Was this useful?YesNo