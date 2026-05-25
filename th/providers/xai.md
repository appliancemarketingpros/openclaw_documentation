---
title: xAI
source_url: https://docs.openclaw.ai/th/providers/xai
scraped_at: 2026-05-25
---

OpenClaw มาพร้อมกับ Plugin ผู้ให้บริการ `xai` แบบบันเดิลสำหรับโมเดล Grok

## เริ่มต้นใช้งาน

* ### สร้าง API key

สร้าง API key ใน [คอนโซล xAI](<https://console.x.ai/>)

* ### ตั้งค่า API key ของคุณ

ตั้งค่า `XAI_API_KEY` หรือเรียกใช้:

bashCopy code
[code]
    openclaw onboard --auth-choice xai-api-key
[/code]

* ### เลือกโมเดล

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "xai/grok-4.3" } } },}
[/code]

## แค็ตตาล็อกในตัว

OpenClaw รวมตระกูลโมเดล xAI เหล่านี้มาให้พร้อมใช้งาน:

ตระกูล | ID โมเดล  
---|---  
Grok 3 | `grok-3`, `grok-3-fast`, `grok-3-mini`, `grok-3-mini-fast`  
Grok 4.3 | `grok-4.3`  
Grok 4 | `grok-4`, `grok-4-0709`  
Grok 4 Fast | `grok-4-fast`, `grok-4-fast-non-reasoning`  
Grok 4.1 Fast | `grok-4-1-fast`, `grok-4-1-fast-non-reasoning`  
Grok 4.20 Beta | `grok-4.20-beta-latest-reasoning`, `grok-4.20-beta-latest-non-reasoning`  
Grok Code | `grok-code-fast-1`  
  
Plugin ยัง forward-resolve ID `grok-4*` และ `grok-code-fast*` ที่ใหม่กว่าเมื่อ ID เหล่านั้นใช้รูปแบบ API เดียวกัน

## การครอบคลุมฟีเจอร์ของ OpenClaw

Plugin แบบบันเดิลแมปพื้นผิว API สาธารณะปัจจุบันของ xAI ไปยังสัญญา ผู้ให้บริการและเครื่องมือที่ใช้ร่วมกันของ OpenClaw ความสามารถที่ไม่พอดีกับสัญญาที่ใช้ร่วมกัน (เช่น TTS แบบสตรีมมิงและเสียงแบบเรียลไทม์) จะไม่ถูกเปิดเผย - ดูตาราง ด้านล่าง

ความสามารถของ xAI | พื้นผิว OpenClaw | สถานะ  
---|---|---  
แชท / Responses | ผู้ให้บริการโมเดล `xai/<model>` | ใช่  
เว็บเสิร์ชฝั่งเซิร์ฟเวอร์ | ผู้ให้บริการ `web_search` `grok` | ใช่  
การค้นหา X ฝั่งเซิร์ฟเวอร์ | เครื่องมือ `x_search` | ใช่  
การประมวลผลโค้ดฝั่งเซิร์ฟเวอร์ | เครื่องมือ `code_execution` | ใช่  
รูปภาพ | `image_generate` | ใช่  
วิดีโอ | `video_generate` | ใช่  
ข้อความเป็นเสียงแบบแบตช์ | `messages.tts.provider: "xai"` / `tts` | ใช่  
TTS แบบสตรีมมิง | - | ไม่เปิดเผย; สัญญา TTS ของ OpenClaw ส่งคืนบัฟเฟอร์เสียงแบบสมบูรณ์  
เสียงพูดเป็นข้อความแบบแบตช์ | `tools.media.audio` / ความเข้าใจสื่อ | ใช่  
เสียงพูดเป็นข้อความแบบสตรีมมิง | Voice Call `streaming.provider: "xai"` | ใช่  
เสียงแบบเรียลไทม์ | - | ยังไม่เปิดเผย; สัญญาเซสชัน/WebSocket แตกต่างกัน  
ไฟล์ / แบตช์ | ความเข้ากันได้กับ API โมเดลทั่วไปเท่านั้น | ไม่ใช่เครื่องมือ OpenClaw ระดับเฟิร์สต์คลาส  
  
### การแมปโหมดเร็ว

`/fast on` หรือ `agents.defaults.models["xai/<model>"].params.fastMode: true` เขียนคำขอ xAI แบบเนทีฟใหม่ดังนี้:

โมเดลต้นทาง | เป้าหมายโหมดเร็ว  
---|---  
`grok-3` | `grok-3-fast`  
`grok-3-mini` | `grok-3-mini-fast`  
`grok-4` | `grok-4-fast`  
`grok-4-0709` | `grok-4-fast`  
  
### นามแฝงความเข้ากันได้แบบดั้งเดิม

นามแฝงดั้งเดิมยังคงถูก normalize เป็น ID แบบบันเดิลมาตรฐาน:

นามแฝงดั้งเดิม | ID มาตรฐาน  
---|---  
`grok-4-fast-reasoning` | `grok-4-fast`  
`grok-4-1-fast-reasoning` | `grok-4-1-fast`  
`grok-4.20-reasoning` | `grok-4.20-beta-latest-reasoning`  
`grok-4.20-non-reasoning` | `grok-4.20-beta-latest-non-reasoning`  
  
## ฟีเจอร์

เว็บเสิร์ช

ผู้ให้บริการเว็บเสิร์ช `grok` แบบบันเดิลสามารถใช้ `XAI_API_KEY` หรือคีย์ เว็บเสิร์ชของ Plugin ได้:

bashCopy code
[code]
    openclaw config set tools.web.search.provider grok
[/code]

การสร้างวิดีโอ

Plugin `xai` แบบบันเดิลลงทะเบียนการสร้างวิดีโอผ่านเครื่องมือ `video_generate` ที่ใช้ร่วมกัน

  * โมเดลวิดีโอเริ่มต้น: `xai/grok-imagine-video`
  * โหมด: ข้อความเป็นวิดีโอ, ภาพเป็นวิดีโอ, การสร้างภาพอ้างอิง, การแก้ไขวิดีโอระยะไกล และการขยายวิดีโอระยะไกล
  * อัตราส่วนภาพ: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`
  * ความละเอียด: `480P`, `720P`
  * ระยะเวลา: 1-15 วินาทีสำหรับการสร้าง/ภาพเป็นวิดีโอ, 1-10 วินาทีเมื่อใช้บทบาท `reference_image`, 2-10 วินาทีสำหรับการขยาย
  * การสร้างภาพอ้างอิง: ตั้งค่า `imageRoles` เป็น `reference_image` สำหรับภาพที่ให้มาทุกภาพ; xAI ยอมรับภาพดังกล่าวได้สูงสุด 7 ภาพ


หากต้องการใช้ xAI เป็นผู้ให้บริการวิดีโอเริ่มต้น:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "xai/grok-imagine-video",      },    },  },}
[/code]

การสร้างรูปภาพ

Plugin `xai` แบบบันเดิลลงทะเบียนการสร้างรูปภาพผ่านเครื่องมือ `image_generate` ที่ใช้ร่วมกัน

  * โมเดลรูปภาพเริ่มต้น: `xai/grok-imagine-image`
  * โมเดลเพิ่มเติม: `xai/grok-imagine-image-pro`
  * โหมด: ข้อความเป็นรูปภาพและการแก้ไขภาพอ้างอิง
  * อินพุตอ้างอิง: `image` หนึ่งรายการหรือ `images` ได้สูงสุดห้ารายการ
  * อัตราส่วนภาพ: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `2:3`, `3:2`
  * ความละเอียด: `1K`, `2K`
  * จำนวน: ได้สูงสุด 4 ภาพ


OpenClaw ขอการตอบกลับรูปภาพแบบ `b64_json` จาก xAI เพื่อให้สื่อที่สร้างขึ้นสามารถ จัดเก็บและส่งผ่านเส้นทางไฟล์แนบของช่องทางปกติได้ รูปภาพอ้างอิงในเครื่อง จะถูกแปลงเป็น URL ข้อมูล; การอ้างอิง `http(s)` ระยะไกลจะถูกส่งผ่านตามเดิม

หากต้องการใช้ xAI เป็นผู้ให้บริการรูปภาพเริ่มต้น:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "xai/grok-imagine-image",      },    },  },}
[/code]

ข้อความเป็นเสียง

Plugin `xai` แบบบันเดิลลงทะเบียนข้อความเป็นเสียงผ่านพื้นผิวผู้ให้บริการ `tts` ที่ใช้ร่วมกัน

  * เสียง: `eve`, `ara`, `rex`, `sal`, `leo`, `una`
  * เสียงเริ่มต้น: `eve`
  * รูปแบบ: `mp3`, `wav`, `pcm`, `mulaw`, `alaw`
  * ภาษา: รหัส BCP-47 หรือ `auto`
  * ความเร็ว: การแทนที่ความเร็วแบบเนทีฟของผู้ให้บริการ
  * ไม่รองรับรูปแบบวอยซ์โน้ต Opus แบบเนทีฟ


หากต้องการใช้ xAI เป็นผู้ให้บริการ TTS เริ่มต้น:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "xai",      providers: {        xai: {          voiceId: "eve",        },      },    },  },}
[/code]

เสียงพูดเป็นข้อความ

Plugin `xai` แบบบันเดิลลงทะเบียนเสียงพูดเป็นข้อความแบบแบตช์ผ่านพื้นผิว การถอดเสียงเพื่อความเข้าใจสื่อของ OpenClaw

  * โมเดลเริ่มต้น: `grok-stt`
  * ปลายทาง: xAI REST `/v1/stt`
  * เส้นทางอินพุต: อัปโหลดไฟล์เสียงแบบ multipart
  * OpenClaw รองรับในทุกที่ที่การถอดเสียงขาเข้าใช้ `tools.media.audio` รวมถึงส่วนเสียงของช่องเสียง Discord และ ไฟล์แนบเสียงของช่องทาง


หากต้องการบังคับใช้ xAI สำหรับการถอดเสียงขาเข้า:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [          {            type: "provider",            provider: "xai",            model: "grok-stt",          },        ],      },    },  },}
[/code]

สามารถระบุภาษาได้ผ่านการกำหนดค่าสื่อเสียงที่ใช้ร่วมกันหรือคำขอถอดเสียง รายการต่อรายการ คำใบ้พรอมป์ได้รับการยอมรับโดยพื้นผิว OpenClaw ที่ใช้ร่วมกัน แต่การผสานรวม xAI REST STT ส่งต่อเฉพาะไฟล์ โมเดล และ ภาษา เพราะสิ่งเหล่านั้นแมปกับปลายทางสาธารณะปัจจุบันของ xAI ได้อย่างชัดเจน

เสียงพูดเป็นข้อความแบบสตรีมมิง

Plugin `xai` แบบบันเดิลยังลงทะเบียนผู้ให้บริการการถอดเสียงแบบเรียลไทม์ สำหรับเสียงสายเสียงสดด้วย

  * ปลายทาง: xAI WebSocket `wss://api.x.ai/v1/stt`
  * การเข้ารหัสเริ่มต้น: `mulaw`
  * อัตราสุ่มตัวอย่างเริ่มต้น: `8000`
  * endpointing เริ่มต้น: `800ms`
  * ข้อความถอดเสียงชั่วคราว: เปิดใช้งานตามค่าเริ่มต้น


สตรีมสื่อ Twilio ของ Voice Call ส่งเฟรมเสียง G.711 µ-law ดังนั้น ผู้ให้บริการ xAI จึงส่งต่อเฟรมเหล่านั้นได้โดยตรงโดยไม่ต้องแปลงรหัส:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "xai",            providers: {              xai: {                apiKey: "${XAI_API_KEY}",                endpointingMs: 800,                language: "en",              },            },          },        },      },    },  },}
[/code]

การกำหนดค่าที่ provider เป็นเจ้าของอยู่ภายใต้ `plugins.entries.voice-call.config.streaming.providers.xai` คีย์ที่รองรับ ได้แก่ `apiKey`, `baseUrl`, `sampleRate`, `encoding` (`pcm`, `mulaw` หรือ `alaw`), `interimResults`, `endpointingMs` และ `language`

การกำหนดค่า x_search

Plugin xAI ที่มาพร้อมชุดติดตั้งเปิดเผย `x_search` เป็นเครื่องมือ OpenClaw สำหรับค้นหา เนื้อหา X (เดิมคือ Twitter) ผ่าน Grok

เส้นทางการกำหนดค่า: `plugins.entries.xai.config.xSearch`

คีย์ | ประเภท | ค่าเริ่มต้น | คำอธิบาย  
---|---|---|---  
`enabled` | boolean | - | เปิดหรือปิดใช้งาน x_search  
`model` | string | `grok-4-1-fast` | โมเดลที่ใช้สำหรับคำขอ x_search  
`baseUrl` | string | - | การแทนที่ URL ฐานของ xAI Responses  
`inlineCitations` | boolean | - | รวมการอ้างอิงแบบอินไลน์ในผลลัพธ์  
`maxTurns` | number | - | จำนวนรอบการสนทนาสูงสุด  
`timeoutSeconds` | number | - | ระยะหมดเวลาของคำขอเป็นวินาที  
`cacheTtlMinutes` | number | - | อายุแคชเป็นนาที  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast",            baseUrl: "https://api.x.ai/v1",            inlineCitations: true,          },        },      },    },  },}
[/code]

การกำหนดค่า Code execution

Plugin xAI ที่มาพร้อมชุดติดตั้งเปิดเผย `code_execution` เป็นเครื่องมือ OpenClaw สำหรับ การรันโค้ดระยะไกลในสภาพแวดล้อม sandbox ของ xAI

เส้นทางการกำหนดค่า: `plugins.entries.xai.config.codeExecution`

คีย์ | ประเภท | ค่าเริ่มต้น | คำอธิบาย  
---|---|---|---  
`enabled` | boolean | `true` (หากมีคีย์) | เปิดหรือปิดใช้งานการรันโค้ด  
`model` | string | `grok-4-1-fast` | โมเดลที่ใช้สำหรับคำขอรันโค้ด  
`maxTurns` | number | - | จำนวนรอบการสนทนาสูงสุด  
`timeoutSeconds` | number | - | ระยะหมดเวลาของคำขอเป็นวินาที  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast",          },        },      },    },  },}
[/code]

ข้อจำกัดที่ทราบ

  * การยืนยันตัวตนในปัจจุบันใช้คีย์ API เท่านั้น คีย์ API อาจถูกเก็บไว้ในโปรไฟล์การยืนยันตัวตน xAI ตัวแปรสภาพแวดล้อม หรือการกำหนดค่า Plugin ยังไม่มี OAuth ของ xAI หรือ โฟลว์ device-code ใน OpenClaw
  * `grok-4.20-multi-agent-experimental-beta-0304` ไม่รองรับบนเส้นทาง provider xAI ปกติ เพราะต้องใช้พื้นผิว API ต้นทางที่แตกต่างจาก การขนส่ง xAI มาตรฐานของ OpenClaw
  * เสียง xAI Realtime ยังไม่ได้ลงทะเบียนเป็น provider ของ OpenClaw ต้องใช้สัญญาเซสชันเสียงแบบสองทิศทางที่แตกต่างจาก STT แบบแบตช์หรือ การถอดเสียงแบบสตรีมมิง
  * `quality` ของภาพ xAI, `mask` ของภาพ และอัตราส่วนภาพเพิ่มเติมที่ใช้ได้เฉพาะแบบ native ยังไม่ถูกเปิดเผยจนกว่าเครื่องมือ `image_generate` ที่ใช้ร่วมกันจะมี ตัวควบคุมข้าม provider ที่สอดคล้องกัน

หมายเหตุขั้นสูง

  * OpenClaw ใช้การแก้ไขความเข้ากันได้สำหรับ schema ของเครื่องมือและการเรียกเครื่องมือที่เฉพาะกับ xAI โดยอัตโนมัติบนเส้นทาง runner ที่ใช้ร่วมกัน
  * คำขอ xAI แบบ native ตั้งค่าเริ่มต้นเป็น `tool_stream: true` ตั้งค่า `agents.defaults.models["xai/<model>"].params.tool_stream` เป็น `false` เพื่อ ปิดใช้งาน
  * wrapper xAI ที่มาพร้อมชุดติดตั้งจะลบแฟล็ก schema ของเครื่องมือแบบ strict ที่ไม่รองรับและ คีย์ payload การให้เหตุผลก่อนส่งคำขอ xAI แบบ native
  * `web_search`, `x_search` และ `code_execution` ถูกเปิดเผยเป็นเครื่องมือ OpenClaw OpenClaw เปิดใช้งาน built-in ของ xAI ที่ต้องใช้ภายในคำขอเครื่องมือแต่ละรายการ แทนการแนบเครื่องมือ native ทั้งหมดกับทุกเทิร์นของแชต
  * Grok `web_search` อ่าน `plugins.entries.xai.config.webSearch.baseUrl` `x_search` อ่าน `plugins.entries.xai.config.xSearch.baseUrl` จากนั้น fallback ไปยัง URL ฐานของการค้นหาเว็บ Grok
  * `x_search` และ `code_execution` เป็นของ Plugin xAI ที่มาพร้อมชุดติดตั้ง ไม่ได้ถูก hardcode ไว้ใน runtime โมเดลหลัก
  * `code_execution` คือการรันใน sandbox ของ xAI ระยะไกล ไม่ใช่ [`exec`](</th/tools/exec>) ในเครื่อง


## การทดสอบแบบ live

เส้นทางสื่อ xAI ครอบคลุมด้วย unit test และชุดทดสอบแบบ live ที่เลือกเปิดใช้ คำสั่ง live จะโหลด secrets จาก shell ล็อกอินของคุณ รวมถึง `~/.profile` ก่อน probe `XAI_API_KEY`

bashCopy code
[code]
    pnpm test extensions/xaiOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 pnpm test:live -- extensions/xai/xai.live.test.tsOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 OPENCLAW_LIVE_IMAGE_GENERATION_PROVIDERS=xai pnpm test:live -- test/image-generation.runtime.live.test.ts
[/code]

ไฟล์ live เฉพาะ provider จะสังเคราะห์ TTS ปกติ, PCM TTS ที่เหมาะกับระบบโทรศัพท์, ถอดเสียงผ่าน STT แบบแบตช์ของ xAI, สตรีม PCM เดียวกันผ่าน STT เรียลไทม์ของ xAI, สร้างผลลัพธ์ text-to-image และแก้ไขภาพอ้างอิง ไฟล์ live ของภาพที่ใช้ร่วมกัน ยืนยัน provider xAI เดียวกันผ่านเส้นทางการเลือก runtime, fallback, การทำให้เป็นมาตรฐาน, และแนบสื่อของ OpenClaw

## ที่เกี่ยวข้อง

[**การเลือกโมเดล** การเลือก provider, model refs และพฤติกรรม failover ](</th/concepts/model-providers>) [**การสร้างวิดีโอ** พารามิเตอร์เครื่องมือวิดีโอที่ใช้ร่วมกันและการเลือก provider ](</th/tools/video-generation>) [**provider ทั้งหมด** ภาพรวม provider ที่กว้างขึ้น ](</th/providers>) [**การแก้ไขปัญหา** ปัญหาทั่วไปและการแก้ไข ](</th/help/troubleshooting>)

Was this useful?YesNo