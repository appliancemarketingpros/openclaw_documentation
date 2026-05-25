---
title: LiteLLM
source_url: https://docs.openclaw.ai/th/providers/litellm
scraped_at: 2026-05-25
---

[LiteLLM](<https://litellm.ai>) คือ Gateway LLM แบบโอเพนซอร์สที่มี API แบบรวมศูนย์สำหรับผู้ให้บริการโมเดลมากกว่า 100 ราย เชื่อม OpenClaw ผ่าน LiteLLM เพื่อให้ได้การติดตามค่าใช้จ่าย การบันทึก log และความยืดหยุ่นในการสลับ backend โดยไม่ต้องเปลี่ยน config ของ OpenClaw

## เริ่มต้นอย่างรวดเร็ว

### Onboarding (recommended)

**เหมาะที่สุดสำหรับ:** เส้นทางที่เร็วที่สุดในการตั้งค่า LiteLLM ให้ใช้งานได้

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

สำหรับการตั้งค่าแบบไม่โต้ตอบกับ proxy ระยะไกล ให้ส่ง URL ของ proxy อย่างชัดเจน:

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### Manual setup

**เหมาะที่สุดสำหรับ:** การควบคุมการติดตั้งและ config อย่างเต็มรูปแบบ

* ### Start LiteLLM Proxy

bashCopy code
[code]
    pip install 'litellm[proxy]'litellm --model claude-opus-4-6
[/code]

* ### Point OpenClaw to LiteLLM

bashCopy code
[code]
    export LITELLM_API_KEY="your-litellm-key" openclaw
[/code]

เท่านี้ก็เรียบร้อย ตอนนี้ OpenClaw จะกำหนดเส้นทางผ่าน LiteLLM

## การกำหนดค่า

### ตัวแปรสภาพแวดล้อม

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### ไฟล์ config

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## การกำหนดค่าขั้นสูง

### การสร้างภาพ

LiteLLM ยังสามารถรองรับเครื่องมือ `image_generate` ผ่านเส้นทางที่เข้ากันได้กับ OpenAI อย่าง `/images/generations` และ `/images/edits` กำหนดค่าโมเดลภาพของ LiteLLM ภายใต้ `agents.defaults.imageGenerationModel`:

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

URL ของ LiteLLM แบบ loopback เช่น `http://localhost:4000` ใช้งานได้โดยไม่ต้องมีการแทนที่ เครือข่ายส่วนตัวแบบ global สำหรับ proxy ที่โฮสต์บน LAN ให้ตั้งค่า `models.providers.litellm.request.allowPrivateNetwork: true` เพราะ API key จะถูกส่งไปยังโฮสต์ proxy ที่กำหนดค่าไว้

Virtual keys

สร้างคีย์เฉพาะสำหรับ OpenClaw พร้อมขีดจำกัดการใช้จ่าย:

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

ใช้คีย์ที่สร้างขึ้นเป็น `LITELLM_API_KEY`

Model routing

LiteLLM สามารถกำหนดเส้นทางคำขอโมเดลไปยัง backend ต่าง ๆ ได้ กำหนดค่าใน `config.yaml` ของ LiteLLM:

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

OpenClaw ยังคงขอ `claude-opus-4-6` — LiteLLM จะจัดการการกำหนดเส้นทางให้

Viewing usage

ตรวจสอบ dashboard หรือ API ของ LiteLLM:

bashCopy code
[code]
    # Key infocurl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # Spend logscurl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

Proxy behavior notes

  * LiteLLM ทำงานบน `http://localhost:4000` ตามค่าเริ่มต้น
  * OpenClaw เชื่อมต่อผ่าน endpoint `/v1` ของ LiteLLM ที่เข้ากันได้กับ OpenAI ในรูปแบบ proxy
  * การปรับรูปแบบคำขอสำหรับ OpenAI แบบ native เท่านั้นจะไม่มีผลผ่าน LiteLLM: ไม่มี `service_tier`, ไม่มี Responses `store`, ไม่มี hint ของ prompt-cache และไม่มี การปรับ payload ให้เข้ากันได้กับ reasoning ของ OpenAI
  * header แสดงที่มาของ OpenClaw แบบซ่อน (`originator`, `version`, `User-Agent`) จะไม่ถูกฉีดเข้าไปใน URL ฐานของ LiteLLM แบบกำหนดเอง


## ที่เกี่ยวข้อง

[**LiteLLM Docs** เอกสารทางการของ LiteLLM และข้อมูลอ้างอิง API ](<https://docs.litellm.ai>) [**Model selection** ภาพรวมของผู้ให้บริการทั้งหมด การอ้างอิงโมเดล และพฤติกรรม failover ](</th/concepts/model-providers>) [**Configuration** ข้อมูลอ้างอิง config แบบเต็ม ](</th/gateway/configuration>) [**Model selection** วิธีเลือกและกำหนดค่าโมเดล ](</th/concepts/models>)

Was this useful?YesNo