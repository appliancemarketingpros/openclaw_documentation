---
title: Google (Gemini)
source_url: https://docs.openclaw.ai/th/providers/google
scraped_at: 2026-05-25
---

Plugin Google ให้การเข้าถึงโมเดล Gemini ผ่าน Google AI Studio รวมถึง การสร้างภาพ ความเข้าใจสื่อ (ภาพ/เสียง/วิดีโอ), การแปลงข้อความเป็นเสียง และการค้นเว็บผ่าน Gemini Grounding

  * ผู้ให้บริการ: `google`
  * การยืนยันตัวตน: `GEMINI_API_KEY` หรือ `GOOGLE_API_KEY`
  * API: Google Gemini API
  * ตัวเลือกรันไทม์: ผู้ให้บริการ/โมเดล `agentRuntime.id: "google-gemini-cli"` ใช้ Gemini CLI OAuth ซ้ำ โดยยังคงการอ้างอิงโมเดลให้เป็นมาตรฐานในรูปแบบ `google/*`


## เริ่มต้นใช้งาน

เลือกวิธีการยืนยันตัวตนที่คุณต้องการ แล้วทำตามขั้นตอนการตั้งค่า

### API key

**เหมาะที่สุดสำหรับ:** การเข้าถึง Gemini API มาตรฐานผ่าน Google AI Studio

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice gemini-api-key
[/code]

หรือส่งคีย์โดยตรง:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY"
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "google/gemini-3.1-pro-preview" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider google
[/code]

### Gemini CLI (OAuth)

**เหมาะที่สุดสำหรับ:** การใช้การเข้าสู่ระบบ Gemini CLI ที่มีอยู่ผ่าน PKCE OAuth ซ้ำ แทนการใช้ API key แยกต่างหาก

* ### Install the Gemini CLI

คำสั่ง `gemini` ภายในเครื่องต้องพร้อมใช้งานบน `PATH`

bashCopy code
[code]
    # Homebrewbrew install gemini-cli # or npmnpm install -g @google/gemini-cli
[/code]

OpenClaw รองรับทั้งการติดตั้งผ่าน Homebrew และการติดตั้ง npm แบบโกลบอล รวมถึง เลย์เอาต์ Windows/npm ที่พบได้ทั่วไป

* ### Log in via OAuth

bashCopy code
[code]
    openclaw models auth login --provider google-gemini-cli --set-default
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider google
[/code]

  * โมเดลเริ่มต้น: `google/gemini-3.1-pro-preview`
  * รันไทม์: `google-gemini-cli`
  * นามแฝง: `gemini-cli`


รหัสโมเดล Gemini API ของ Gemini 3.1 Pro คือ `gemini-3.1-pro-preview` OpenClaw ยอมรับ `google/gemini-3.1-pro` ที่สั้นกว่าเป็นนามแฝงเพื่อความสะดวก และทำให้เป็นรูปแบบมาตรฐานก่อนเรียกผู้ให้บริการ

**ตัวแปรสภาพแวดล้อม:**

  * `OPENCLAW_GEMINI_OAUTH_CLIENT_ID`
  * `OPENCLAW_GEMINI_OAUTH_CLIENT_SECRET`


(หรือรูปแบบ `GEMINI_CLI_*`)

การอ้างอิงโมเดล `google-gemini-cli/*` เป็นนามแฝงความเข้ากันได้แบบเดิม การตั้งค่าใหม่ ควรใช้การอ้างอิงโมเดล `google/*` พร้อมรันไทม์ `google-gemini-cli` เมื่อต้องการการเรียกใช้ Gemini CLI ภายในเครื่อง

## ความสามารถ

ความสามารถ | รองรับ  
---|---  
การเติมเต็มแชต | ใช่  
การสร้างภาพ | ใช่  
การสร้างเพลง | ใช่  
การแปลงข้อความเป็นเสียง | ใช่  
เสียงแบบเรียลไทม์ | ใช่ (Google Live API)  
ความเข้าใจภาพ | ใช่  
การถอดเสียงจากเสียง | ใช่  
ความเข้าใจวิดีโอ | ใช่  
การค้นเว็บ (Grounding) | ใช่  
การคิด/การให้เหตุผล | ใช่ (Gemini 2.5+ / Gemini 3+)  
โมเดล Gemma 4 | ใช่  
  
## การค้นเว็บ

ผู้ให้บริการค้นเว็บ `gemini` ที่รวมมาด้วยใช้การ Grounding ของ Gemini Google Search กำหนดค่าคีย์ค้นหาเฉพาะภายใต้ `plugins.entries.google.config.webSearch` หรือให้ใช้ `models.providers.google.apiKey` ซ้ำหลังจาก `GEMINI_API_KEY`:

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash",          },        },      },    },  },}
[/code]

ลำดับความสำคัญของข้อมูลประจำตัวคือ `webSearch.apiKey` เฉพาะก่อน จากนั้น `GEMINI_API_KEY` แล้วจึง `models.providers.google.apiKey` `webSearch.baseUrl` เป็นตัวเลือก และ มีไว้สำหรับพร็อกซีของผู้ปฏิบัติงานหรือปลายทาง Gemini API ที่เข้ากันได้ เมื่อเว้นไว้ การค้นเว็บ Gemini จะใช้ `models.providers.google.baseUrl` ซ้ำ ดู [การค้นหา Gemini](</th/tools/gemini-search>) สำหรับพฤติกรรมเครื่องมือเฉพาะผู้ให้บริการ

## การสร้างภาพ

ผู้ให้บริการสร้างภาพ `google` ที่รวมมาด้วยมีค่าเริ่มต้นเป็น `google/gemini-3.1-flash-image-preview`

  * รองรับ `google/gemini-3-pro-image-preview` ด้วย
  * สร้าง: สูงสุด 4 ภาพต่อคำขอ
  * โหมดแก้ไข: เปิดใช้งาน สูงสุด 5 ภาพอินพุต
  * การควบคุมเรขาคณิต: `size`, `aspectRatio` และ `resolution`


หากต้องการใช้ Google เป็นผู้ให้บริการภาพเริ่มต้น:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

## การสร้างวิดีโอ

Plugin `google` ที่รวมมาด้วยยังลงทะเบียนการสร้างวิดีโอผ่านเครื่องมือที่ใช้ร่วมกัน `video_generate`

  * โมเดลวิดีโอเริ่มต้น: `google/veo-3.1-fast-generate-preview`
  * โหมด: ข้อความเป็นวิดีโอ, ภาพเป็นวิดีโอ และโฟลว์อ้างอิงวิดีโอเดียว
  * รองรับ `aspectRatio` (`16:9`, `9:16`) และ `resolution` (`720P`, `1080P`); เอาต์พุตเสียงยังไม่รองรับโดย Veo ในปัจจุบัน
  * ระยะเวลาที่รองรับ: **4, 6 หรือ 8 วินาที** (ค่าอื่นจะปรับไปยังค่าที่อนุญาตซึ่งใกล้ที่สุด)


หากต้องการใช้ Google เป็นผู้ให้บริการวิดีโอเริ่มต้น:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",      },    },  },}
[/code]

## การสร้างเพลง

Plugin `google` ที่รวมมาด้วยยังลงทะเบียนการสร้างเพลงผ่านเครื่องมือที่ใช้ร่วมกัน `music_generate`

  * โมเดลเพลงเริ่มต้น: `google/lyria-3-clip-preview`
  * รองรับ `google/lyria-3-pro-preview` ด้วย
  * การควบคุมพรอมป์: `lyrics` และ `instrumental`
  * รูปแบบเอาต์พุต: ค่าเริ่มต้นคือ `mp3` และมี `wav` บน `google/lyria-3-pro-preview`
  * อินพุตอ้างอิง: สูงสุด 10 ภาพ
  * การรันที่มีเซสชันรองรับจะแยกการทำงานผ่านโฟลว์งาน/สถานะที่ใช้ร่วมกัน รวมถึง `action: "status"`


หากต้องการใช้ Google เป็นผู้ให้บริการเพลงเริ่มต้น:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

## การแปลงข้อความเป็นเสียง

ผู้ให้บริการเสียงพูด `google` ที่รวมมาด้วยใช้เส้นทาง Gemini API TTS พร้อม `gemini-3.1-flash-tts-preview`

  * เสียงเริ่มต้น: `Kore`
  * การยืนยันตัวตน: `messages.tts.providers.google.apiKey`, `models.providers.google.apiKey`, `GEMINI_API_KEY` หรือ `GOOGLE_API_KEY`
  * เอาต์พุต: WAV สำหรับไฟล์แนบ TTS ปกติ, Opus สำหรับเป้าหมายข้อความเสียง, PCM สำหรับ Talk/โทรศัพท์
  * เอาต์พุตข้อความเสียง: Google PCM ถูกห่อเป็น WAV และแปลงรหัสเป็น Opus 48 kHz ด้วย `ffmpeg`


เส้นทาง Gemini TTS แบบแบตช์ของ Google ส่งคืนเสียงที่สร้างใน การตอบกลับ `generateContent` ที่เสร็จสมบูรณ์ สำหรับการสนทนาพูดที่มีเวลาแฝงต่ำสุด ให้ใช้ ผู้ให้บริการเสียงแบบเรียลไทม์ของ Google ที่รองรับโดย Gemini Live API แทน TTS แบบแบตช์

หากต้องการใช้ Google เป็นผู้ให้บริการ TTS เริ่มต้น:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "google",      providers: {        google: {          model: "gemini-3.1-flash-tts-preview",          voiceName: "Kore",          audioProfile: "Speak professionally with a calm tone.",        },      },    },  },}
[/code]

Gemini API TTS ใช้พรอมป์ภาษาธรรมชาติสำหรับการควบคุมสไตล์ ตั้งค่า `audioProfile` เพื่อเติมพรอมป์สไตล์ที่ใช้ซ้ำได้ก่อนข้อความที่จะพูด ตั้งค่า `speakerName` เมื่อข้อความพรอมป์ของคุณอ้างถึงผู้พูดที่มีชื่อ

Gemini API TTS ยังยอมรับแท็กเสียงในวงเล็บเหลี่ยมที่สื่ออารมณ์ในข้อความ เช่น `[whispers]` หรือ `[laughs]` หากต้องการกันแท็กออกจากคำตอบแชตที่มองเห็น แต่ยังส่งไปยัง TTS ให้ใส่ไว้ในบล็อก `[[tts:text]]...[[/tts:text]]`:

textCopy code
[code]
    Here is the clean reply text. [[tts:text]][whispers] Here is the spoken version.[[/tts:text]]
[/code]

## เสียงแบบเรียลไทม์

Plugin `google` ที่รวมมาด้วยลงทะเบียนผู้ให้บริการเสียงแบบเรียลไทม์ที่รองรับโดย Gemini Live API สำหรับบริดจ์เสียงแบ็กเอนด์ เช่น Voice Call และ Google Meet

การตั้งค่า | พาธการกำหนดค่า | ค่าเริ่มต้น  
---|---|---  
โมเดล | `plugins.entries.voice-call.config.realtime.providers.google.model` | `gemini-2.5-flash-native-audio-preview-12-2025`  
เสียง | `...google.voice` | `Kore`  
อุณหภูมิ | `...google.temperature` | (ไม่ได้ตั้งค่า)  
ความไวเริ่มต้นของ VAD | `...google.startSensitivity` | (ไม่ได้ตั้งค่า)  
ความไวสิ้นสุดของ VAD | `...google.endSensitivity` | (ไม่ได้ตั้งค่า)  
ระยะเวลาความเงียบ | `...google.silenceDurationMs` | (ไม่ได้ตั้งค่า)  
การจัดการกิจกรรม | `...google.activityHandling` | ค่าเริ่มต้นของ Google, `start-of-activity-interrupts`  
การครอบคลุมรอบสนทนา | `...google.turnCoverage` | ค่าเริ่มต้นของ Google, `only-activity`  
ปิดใช้งาน VAD อัตโนมัติ | `...google.automaticActivityDetectionDisabled` | `false`  
การกลับมาใช้เซสชันต่อ | `...google.sessionResumption` | `true`  
การบีบอัดบริบท | `...google.contextWindowCompression` | `true`  
คีย์ API | `...google.apiKey` | สำรองไปใช้ `models.providers.google.apiKey`, `GEMINI_API_KEY` หรือ `GOOGLE_API_KEY`  
  
ตัวอย่างการกำหนดค่า Voice Call แบบเรียลไทม์:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          realtime: {            enabled: true,            provider: "google",            providers: {              google: {                model: "gemini-2.5-flash-native-audio-preview-12-2025",                voice: "Kore",                activityHandling: "start-of-activity-interrupts",                turnCoverage: "only-activity",              },            },          },        },      },    },  },}
[/code]

สำหรับการยืนยันแบบสดของผู้ดูแล ให้รัน `OPENAI_API_KEY=... GEMINI_API_KEY=... node --import tsx scripts/dev/realtime-talk-live-smoke.ts` smoke ยังครอบคลุมพาธแบ็กเอนด์/WebRTC ของ OpenAI ด้วย; ช่วง Google จะออกโทเค็น Live API แบบมีข้อจำกัดรูปแบบเดียวกับที่ Control UI Talk ใช้ เปิดเอนด์พอยต์ WebSocket ของเบราว์เซอร์ ส่งเพย์โหลดการตั้งค่าเริ่มต้น และรอ `setupComplete`

## การกำหนดค่าขั้นสูง

การใช้แคช Gemini โดยตรงซ้ำ

สำหรับการรัน Gemini API โดยตรง (`api: "google-generative-ai"`), OpenClaw ส่งตัวจัดการ `cachedContent` ที่กำหนดค่าไว้ต่อไปยังคำขอ Gemini

  * กำหนดค่าพารามิเตอร์ต่อโมเดลหรือแบบส่วนกลางด้วย `cachedContent` หรือ `cached_content` แบบเดิม
  * หากมีทั้งคู่ `cachedContent` จะมีผลก่อน
  * ค่าตัวอย่าง: `cachedContents/prebuilt-context`
  * การใช้งานแคชฮิตของ Gemini ถูกทำให้เป็นมาตรฐานเป็น `cacheRead` ของ OpenClaw จาก `cachedContentTokenCount` ต้นทาง

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "google/gemini-2.5-pro": {          params: {            cachedContent: "cachedContents/prebuilt-context",          },        },      },    },  },}
[/code]

หมายเหตุการใช้งาน JSON ของ Gemini CLI

เมื่อใช้ผู้ให้บริการ OAuth `google-gemini-cli`, OpenClaw ทำให้ เอาต์พุต JSON ของ CLI เป็นมาตรฐานดังนี้:

  * ข้อความตอบกลับมาจากฟิลด์ `response` ใน JSON ของ CLI
  * การใช้งานจะสำรองไปใช้ `stats` เมื่อ CLI ปล่อย `usage` ว่างไว้
  * `stats.cached` ถูกทำให้เป็นมาตรฐานเป็น `cacheRead` ของ OpenClaw
  * หากไม่มี `stats.input`, OpenClaw จะอนุมานโทเค็นอินพุตจาก `stats.input_tokens - stats.cached`

การตั้งค่าสภาพแวดล้อมและดีมอน

หาก Gateway ทำงานเป็นดีมอน (launchd/systemd), ตรวจสอบให้แน่ใจว่า `GEMINI_API_KEY` พร้อมใช้งานสำหรับกระบวนการนั้น (เช่น ใน `~/.openclaw/.env` หรือผ่าน `env.shellEnv`)

## ที่เกี่ยวข้อง

[**การเลือกโมเดล** การเลือกผู้ให้บริการ, การอ้างอิงโมเดล และพฤติกรรมการสลับเมื่อเกิดข้อผิดพลาด ](</th/concepts/model-providers>) [**การสร้างรูปภาพ** พารามิเตอร์เครื่องมือรูปภาพที่ใช้ร่วมกันและการเลือกผู้ให้บริการ ](</th/tools/image-generation>) [**การสร้างวิดีโอ** พารามิเตอร์เครื่องมือวิดีโอที่ใช้ร่วมกันและการเลือกผู้ให้บริการ ](</th/tools/video-generation>) [**การสร้างเพลง** พารามิเตอร์เครื่องมือเพลงที่ใช้ร่วมกันและการเลือกผู้ให้บริการ ](</th/tools/music-generation>)

Was this useful?YesNo