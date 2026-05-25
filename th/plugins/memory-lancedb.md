---
title: หน่วยความจำ LanceDB
source_url: https://docs.openclaw.ai/th/plugins/memory-lancedb
scraped_at: 2026-05-25
---

`memory-lancedb` เป็น Plugin หน่วยความจำที่บันเดิลมา ซึ่งจัดเก็บหน่วยความจำระยะยาวใน LanceDB และใช้ embeddings สำหรับการเรียกคืน สามารถเรียกคืนความทรงจำที่เกี่ยวข้องโดยอัตโนมัติ ก่อนรอบโมเดล และบันทึกข้อเท็จจริงสำคัญหลังการตอบกลับได้

ใช้เมื่อคุณต้องการฐานข้อมูลเวกเตอร์ภายในเครื่องสำหรับหน่วยความจำ ต้องการ endpoint embedding ที่เข้ากันได้กับ OpenAI หรือต้องการเก็บฐานข้อมูลหน่วยความจำไว้นอก ที่เก็บหน่วยความจำในตัวเริ่มต้น

## เริ่มต้นอย่างรวดเร็ว

json5Copy code
[code]
    {  plugins: {    slots: {      memory: "memory-lancedb",    },    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            provider: "openai",            model: "text-embedding-3-small",          },          autoRecall: true,          autoCapture: false,        },      },    },  },}
[/code]

รีสตาร์ท Gateway หลังจากเปลี่ยนการกำหนดค่า Plugin:

bashCopy code
[code]
    openclaw gateway restart
[/code]

จากนั้นตรวจสอบว่าโหลด Plugin แล้ว:

bashCopy code
[code]
    openclaw plugins list
[/code]

## Embeddings ที่รองรับด้วย Provider

`memory-lancedb` สามารถใช้อะแดปเตอร์ Provider embedding หน่วยความจำเดียวกับ `memory-core` ได้ ตั้งค่า `embedding.provider` และละ `embedding.apiKey` เพื่อใช้ โปรไฟล์ auth ที่กำหนดค่าไว้ของ Provider, environment variable หรือ `models.providers.<provider>.apiKey`

json5Copy code
[code]
    {  plugins: {    slots: {      memory: "memory-lancedb",    },    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            provider: "openai",            model: "text-embedding-3-small",          },          autoRecall: true,        },      },    },  },}
[/code]

เส้นทางนี้ทำงานกับโปรไฟล์ auth ของ Provider ที่เปิดเผยข้อมูลประจำตัว embeddings ตัวอย่างเช่น GitHub Copilot สามารถใช้ได้เมื่อโปรไฟล์/แผนของ Copilot รองรับ embeddings:

json5Copy code
[code]
    {  plugins: {    slots: {      memory: "memory-lancedb",    },    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            provider: "github-copilot",            model: "text-embedding-3-small",          },        },      },    },  },}
[/code]

OpenAI Codex / ChatGPT OAuth (`openai-codex`) ไม่ใช่ข้อมูลประจำตัว embeddings ของ OpenAI Platform สำหรับ OpenAI embeddings ให้ใช้โปรไฟล์ auth ที่เป็น OpenAI API key, `OPENAI_API_KEY` หรือ `models.providers.openai.apiKey` ผู้ใช้ที่มีเฉพาะ OAuth สามารถใช้ Provider อื่นที่รองรับ embedding เช่น GitHub Copilot หรือ Ollama

## Ollama embeddings

สำหรับ Ollama embeddings ให้ใช้ Provider embedding Ollama ที่บันเดิลมาเป็นหลัก โดยจะใช้ endpoint `/api/embed` ดั้งเดิมของ Ollama และทำตามกฎ auth/base URL เดียวกับ Provider Ollama ที่บันทึกไว้ใน [Ollama](</th/providers/ollama>)

json5Copy code
[code]
    {  plugins: {    slots: {      memory: "memory-lancedb",    },    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            provider: "ollama",            baseUrl: "http://127.0.0.1:11434",            model: "mxbai-embed-large",            dimensions: 1024,          },          recallMaxChars: 400,          autoRecall: true,          autoCapture: false,        },      },    },  },}
[/code]

ตั้งค่า `dimensions` สำหรับโมเดล embedding ที่ไม่ใช่มาตรฐาน OpenClaw ทราบ dimensions สำหรับ `text-embedding-3-small` และ `text-embedding-3-large`; โมเดลที่กำหนดเอง ต้องมีค่าใน config เพื่อให้ LanceDB สร้างคอลัมน์เวกเตอร์ได้

สำหรับโมเดล embedding ภายในเครื่องขนาดเล็ก ให้ลด `recallMaxChars` หากคุณพบข้อผิดพลาด ความยาวบริบทจากเซิร์ฟเวอร์ภายในเครื่อง

## Provider ที่เข้ากันได้กับ OpenAI

Provider embedding บางรายที่เข้ากันได้กับ OpenAI ปฏิเสธพารามิเตอร์ `encoding_format` ขณะที่รายอื่นเพิกเฉยต่อพารามิเตอร์นี้และส่งคืนเวกเตอร์ `number[]` เสมอ ดังนั้น `memory-lancedb` จึงละ `encoding_format` ในคำขอ embedding และ ยอมรับได้ทั้งการตอบกลับแบบอาร์เรย์ float หรือการตอบกลับ float32 ที่เข้ารหัส base64

หากคุณมี endpoint embeddings แบบดิบที่เข้ากันได้กับ OpenAI ซึ่งไม่มี อะแดปเตอร์ Provider ที่บันเดิลมา ให้ละ `embedding.provider` (หรือปล่อยไว้เป็น `openai`) และ ตั้งค่า `embedding.apiKey` พร้อมกับ `embedding.baseUrl` วิธีนี้จะคงเส้นทางไคลเอนต์ ที่เข้ากันได้กับ OpenAI โดยตรงไว้

ตั้งค่า `embedding.dimensions` สำหรับ Provider ที่ dimensions ของโมเดลไม่ได้มีอยู่ ในตัว ตัวอย่างเช่น ZhiPu `embedding-3` ใช้ `2048` dimensions:

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            apiKey: "${ZHIPU_API_KEY}",            baseUrl: "https://open.bigmodel.cn/api/paas/v4",            model: "embedding-3",            dimensions: 2048,          },        },      },    },  },}
[/code]

## ขีดจำกัดการเรียกคืนและการบันทึก

`memory-lancedb` มีขีดจำกัดข้อความแยกกันสองค่า:

การตั้งค่า | ค่าเริ่มต้น | ช่วง | ใช้กับ  
---|---|---|---  
`recallMaxChars` | `1000` | 100-10000 | ข้อความที่ส่งไปยัง API embedding สำหรับการเรียกคืน  
`captureMaxChars` | `500` | 100-10000 | ความยาวข้อความของผู้ช่วยที่มีสิทธิ์ถูกบันทึก  
  
`recallMaxChars` ควบคุม auto-recall, เครื่องมือ `memory_recall`, เส้นทาง query ของ `memory_forget` และ `openclaw ltm search` auto-recall จะเลือก ข้อความล่าสุดของผู้ใช้จากรอบนั้นก่อน และจะย้อนกลับไปใช้ prompt ทั้งหมดเฉพาะเมื่อไม่มี ข้อความผู้ใช้เท่านั้น วิธีนี้ช่วยกัน metadata ของช่องทางและบล็อก prompt ขนาดใหญ่ ออกจากคำขอ embedding

`captureMaxChars` ควบคุมว่าการตอบกลับสั้นพอที่จะถูกพิจารณา สำหรับการบันทึกอัตโนมัติหรือไม่ ไม่ได้จำกัด embeddings ของ query สำหรับการเรียกคืน

## คำสั่ง

เมื่อ `memory-lancedb` เป็น Plugin หน่วยความจำที่ใช้งานอยู่ จะลงทะเบียน namespace CLI `ltm`:

bashCopy code
[code]
    openclaw ltm listopenclaw ltm search "project preferences"openclaw ltm stats
[/code]

Plugin ยังขยาย `openclaw memory` ด้วย subcommand `query` แบบไม่ใช่เวกเตอร์ ที่ทำงานกับตาราง LanceDB โดยตรง:

bashCopy code
[code]
    openclaw memory query --cols id,text,createdAt --limit 20openclaw memory query --filter "category = 'preference'" --order-by createdAt:desc
[/code]

  * `--cols <columns>`: รายการคอลัมน์ที่อนุญาตแบบคั่นด้วยจุลภาค (ค่าเริ่มต้นคือ `id`, `text`, `importance`, `category`, `createdAt`)
  * `--filter <condition>`: clause WHERE แบบ SQL; จำกัดที่ 200 อักขระและจำกัดเฉพาะตัวอักษรและตัวเลข, ตัวดำเนินการเปรียบเทียบ, เครื่องหมายคำพูด, วงเล็บ และเครื่องหมายวรรคตอนปลอดภัยชุดเล็ก
  * `--limit <n>`: จำนวนเต็มบวก; ค่าเริ่มต้น `10`
  * `--order-by <column>:<asc|desc>`: การเรียงลำดับในหน่วยความจำที่ใช้หลังตัวกรอง; คอลัมน์เรียงลำดับจะถูกรวมใน projection โดยอัตโนมัติ


Agents ยังได้รับเครื่องมือหน่วยความจำ LanceDB จาก Plugin หน่วยความจำที่ใช้งานอยู่ด้วย:

  * `memory_recall` สำหรับการเรียกคืนที่รองรับด้วย LanceDB
  * `memory_store` สำหรับบันทึกข้อเท็จจริงสำคัญ, การตั้งค่า, การตัดสินใจ และเอนทิตี
  * `memory_forget` สำหรับลบความทรงจำที่ตรงกัน


## ที่เก็บข้อมูล

โดยค่าเริ่มต้น ข้อมูล LanceDB จะอยู่ใต้ `~/.openclaw/memory/lancedb` แทนที่ path ได้ด้วย `dbPath`:

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-lancedb": {        enabled: true,        config: {          dbPath: "~/.openclaw/memory/lancedb",          embedding: {            apiKey: "${OPENAI_API_KEY}",            model: "text-embedding-3-small",          },        },      },    },  },}
[/code]

`storageOptions` รับคู่ key/value แบบสตริงสำหรับ backend ที่เก็บข้อมูลของ LanceDB และ รองรับการขยาย `${ENV_VAR}`:

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-lancedb": {        enabled: true,        config: {          dbPath: "s3://memory-bucket/openclaw",          storageOptions: {            access_key: "${AWS_ACCESS_KEY_ID}",            secret_key: "${AWS_SECRET_ACCESS_KEY}",            endpoint: "${AWS_ENDPOINT_URL}",          },          embedding: {            apiKey: "${OPENAI_API_KEY}",            model: "text-embedding-3-small",          },        },      },    },  },}
[/code]

## Runtime dependencies

`memory-lancedb` ขึ้นอยู่กับแพ็กเกจ native `@lancedb/lancedb` OpenClaw ที่แพ็กเกจแล้ว ถือว่าแพ็กเกจนั้นเป็นส่วนหนึ่งของแพ็กเกจ Plugin การเริ่มต้น Gateway จะไม่ซ่อมแซม dependency ของ Plugin; หาก dependency ขาดหาย ให้ติดตั้งใหม่หรือ อัปเดตแพ็กเกจ Plugin แล้วรีสตาร์ท Gateway

หากการติดตั้งรุ่นเก่าบันทึกข้อผิดพลาดว่าไม่มี `dist/package.json` หรือไม่มี `@lancedb/lancedb` ระหว่างโหลด Plugin ให้อัปเกรด OpenClaw แล้วรีสตาร์ท Gateway

หาก Plugin บันทึกว่า LanceDB ไม่พร้อมใช้งานบน `darwin-x64` ให้ใช้ backend หน่วยความจำเริ่มต้นบนเครื่องนั้น ย้าย Gateway ไปยังแพลตฟอร์มที่รองรับ หรือ ปิดใช้งาน `memory-lancedb`

## การแก้ไขปัญหา

### ความยาวอินพุตเกินความยาวบริบท

โดยปกติหมายความว่าโมเดล embedding ปฏิเสธ query สำหรับการเรียกคืน:

textCopy code
[code]
    memory-lancedb: recall failed: Error: 400 the input length exceeds the context length
[/code]

ตั้งค่า `recallMaxChars` ให้ต่ำลง จากนั้นรีสตาร์ท Gateway:

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-lancedb": {        config: {          recallMaxChars: 400,        },      },    },  },}
[/code]

สำหรับ Ollama ให้ตรวจสอบด้วยว่าเซิร์ฟเวอร์ embedding เข้าถึงได้จากโฮสต์ Gateway:

bashCopy code
[code]
    curl http://127.0.0.1:11434/v1/embeddings \  -H "Content-Type: application/json" \  -d '{"model":"mxbai-embed-large","input":"hello"}'
[/code]

### โมเดล embedding ไม่รองรับ

หากไม่มี `dimensions` จะรู้จักเฉพาะ dimensions ของ OpenAI embedding ที่มีในตัวเท่านั้น สำหรับโมเดล embedding ภายในเครื่องหรือแบบกำหนดเอง ให้ตั้งค่า `embedding.dimensions` เป็นขนาดเวกเตอร์ ที่โมเดลนั้นรายงาน

### Plugin โหลดได้แต่ไม่ปรากฏความทรงจำ

ตรวจสอบว่า `plugins.slots.memory` ชี้ไปที่ `memory-lancedb` จากนั้นรัน:

bashCopy code
[code]
    openclaw ltm statsopenclaw ltm search "recent preference"
[/code]

หาก `autoCapture` ถูกปิดใช้งาน Plugin จะเรียกคืนความทรงจำที่มีอยู่ แต่จะ ไม่จัดเก็บความทรงจำใหม่โดยอัตโนมัติ ใช้เครื่องมือ `memory_store` หรือเปิดใช้งาน `autoCapture` หากคุณต้องการการบันทึกอัตโนมัติ

## ที่เกี่ยวข้อง

  * [ภาพรวมหน่วยความจำ](</th/concepts/memory>)
  * [Active memory](</th/concepts/active-memory>)
  * [การค้นหาหน่วยความจำ](</th/concepts/memory-search>)
  * [Memory Wiki](</th/plugins/memory-wiki>)
  * [Ollama](</th/providers/ollama>)


Was this useful?YesNo