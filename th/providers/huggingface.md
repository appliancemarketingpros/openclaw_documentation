---
title: Hugging Face (inference)
source_url: https://docs.openclaw.ai/th/providers/huggingface
scraped_at: 2026-05-25
---

[Hugging Face Inference Providers](<https://huggingface.co/docs/inference-providers>) ให้บริการ chat completions ที่เข้ากันได้กับ OpenAI ผ่าน router API เดียว คุณสามารถเข้าถึงหลายโมเดลได้ (เช่น DeepSeek, Llama และอื่น ๆ) ด้วยโทเค็นเพียงตัวเดียว OpenClaw ใช้ **endpoint ที่เข้ากันได้กับ OpenAI** (เฉพาะ chat completions เท่านั้น); สำหรับ text-to-image, embeddings หรือ speech ให้ใช้ [HF inference clients](<https://huggingface.co/docs/api-inference/quicktour>) โดยตรง

  * Provider: `huggingface`
  * Auth: `HUGGINGFACE_HUB_TOKEN` หรือ `HF_TOKEN` (fine-grained token ที่มีสิทธิ์ **Make calls to Inference Providers**)
  * API: แบบเข้ากันได้กับ OpenAI (`https://router.huggingface.co/v1`)
  * การเรียกเก็บเงิน: HF token ตัวเดียว; [ราคา](<https://huggingface.co/docs/inference-providers/pricing>) เป็นไปตามอัตราของ provider พร้อม free tier


## เริ่มต้นใช้งาน

* ### สร้าง fine-grained token

ไปที่ [Hugging Face Settings Tokens](<https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained>) แล้วสร้าง fine-grained token ใหม่

* ### เรียกใช้ onboarding

เลือก **Hugging Face** ในเมนูดรอปดาวน์ provider แล้วกรอก API key ของคุณเมื่อระบบถาม:

bashCopy code
[code]
    openclaw onboard --auth-choice huggingface-api-key
[/code]

* ### เลือกโมเดลเริ่มต้น

ในเมนูดรอปดาวน์ **Default Hugging Face model** ให้เลือกโมเดลที่คุณต้องการ รายการนี้จะโหลดจาก Inference API เมื่อคุณมีโทเค็นที่ถูกต้อง; มิฉะนั้นจะแสดงรายการในตัว ตัวเลือกของคุณจะถูกบันทึกเป็นโมเดลเริ่มต้น

คุณยังสามารถตั้งค่าหรือเปลี่ยนโมเดลเริ่มต้นภายหลังในคอนฟิกได้:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/deepseek-ai/DeepSeek-R1" },    },  },}
[/code]

* ### ตรวจสอบว่าโมเดลพร้อมใช้งาน

bashCopy code
[code]
    openclaw models list --provider huggingface
[/code]

### การตั้งค่าแบบ non-interactive

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice huggingface-api-key \  --huggingface-api-key "$HF_TOKEN"
[/code]

การตั้งค่านี้จะตั้ง `huggingface/deepseek-ai/DeepSeek-R1` เป็นโมเดลเริ่มต้น

## รหัสโมเดล

model ref ใช้รูปแบบ `huggingface/<org>/<model>` (Hub-style ID) รายการด้านล่างมาจาก **GET** `https://router.huggingface.co/v1/models`; แค็ตตาล็อกของคุณอาจมีมากกว่านี้

Model | Ref (เติมคำนำหน้าด้วย `huggingface/`)  
---|---  
DeepSeek R1 | `deepseek-ai/DeepSeek-R1`  
DeepSeek V3.2 | `deepseek-ai/DeepSeek-V3.2`  
Qwen3 8B | `Qwen/Qwen3-8B`  
Qwen2.5 7B Instruct | `Qwen/Qwen2.5-7B-Instruct`  
Qwen3 32B | `Qwen/Qwen3-32B`  
Llama 3.3 70B Instruct | `meta-llama/Llama-3.3-70B-Instruct`  
Llama 3.1 8B Instruct | `meta-llama/Llama-3.1-8B-Instruct`  
GPT-OSS 120B | `openai/gpt-oss-120b`  
GLM 4.7 | `zai-org/GLM-4.7`  
Kimi K2.5 | `moonshotai/Kimi-K2.5`  
  
## การกำหนดค่าขั้นสูง

การค้นหาโมเดลและดรอปดาวน์ onboarding

OpenClaw ค้นหาโมเดลโดยเรียก **Inference endpoint โดยตรง** :

bashCopy code
[code]
    GET https://router.huggingface.co/v1/models
[/code]

(ไม่บังคับ: ส่ง `Authorization: Bearer $HUGGINGFACE_HUB_TOKEN` หรือ `$HF_TOKEN` เพื่อรับรายการแบบเต็ม; บาง endpoint จะส่งคืนเพียงบางส่วนหากไม่มี auth) การตอบกลับเป็นแบบ OpenAI-style `{ "object": "list", "data": [ { "id": "Qwen/Qwen3-8B", "owned_by": "Qwen", ... }, ... ] }`

เมื่อคุณกำหนดค่า Hugging Face API key (ผ่าน onboarding, `HUGGINGFACE_HUB_TOKEN` หรือ `HF_TOKEN`) OpenClaw จะใช้ GET นี้เพื่อค้นหาโมเดล chat-completion ที่พร้อมใช้งาน ระหว่าง **การตั้งค่าแบบโต้ตอบ** หลังจากคุณกรอกโทเค็นแล้ว คุณจะเห็นเมนูดรอปดาวน์ **Default Hugging Face model** ที่เติมข้อมูลจากรายการนั้น (หรือจากแค็ตตาล็อกในตัวหากคำขอล้มเหลว) ที่ runtime (เช่น ตอน Gateway เริ่มทำงาน) เมื่อมี key อยู่ OpenClaw จะเรียก **GET** `https://router.huggingface.co/v1/models` อีกครั้งเพื่อรีเฟรชแค็ตตาล็อก รายการนี้จะถูกรวมกับแค็ตตาล็อกในตัว (สำหรับเมทาดาทา เช่น หน้าต่างบริบทและต้นทุน) หากคำขอล้มเหลวหรือไม่ได้ตั้งค่า key จะใช้เฉพาะแค็ตตาล็อกในตัวเท่านั้น

ชื่อโมเดล, alias และ suffix ของนโยบาย

  * **ชื่อจาก API:** ชื่อที่ใช้แสดงของโมเดลจะถูก **เติมข้อมูลจาก GET /v1/models** เมื่อ API ส่งคืน `name`, `title` หรือ `display_name`; มิฉะนั้นจะอนุมานจาก model id (เช่น `deepseek-ai/DeepSeek-R1` จะกลายเป็น "DeepSeek R1")
  * **override ชื่อที่ใช้แสดง:** คุณสามารถตั้งป้ายชื่อแบบกำหนดเองต่อโมเดลในคอนฟิกได้ เพื่อให้แสดงตามที่คุณต้องการใน CLI และ UI:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1 (fast)" },        "huggingface/deepseek-ai/DeepSeek-R1:cheapest": { alias: "DeepSeek R1 (cheap)" },      },    },  },}
[/code]

  * **suffix ของนโยบาย:** เอกสารและ helper ของ Hugging Face แบบ bundled ใน OpenClaw ปัจจุบันถือว่า suffix สองตัวนี้เป็นตัวแปรนโยบายในตัว:

    * **`:fastest`** — throughput สูงสุด
    * **`:cheapest`** — ต้นทุนต่อ output token ต่ำสุด

คุณสามารถเพิ่มค่าเหล่านี้เป็นรายการแยกใน `models.providers.huggingface.models` หรือตั้ง `model.primary` พร้อม suffix ได้ คุณยังสามารถตั้งค่าลำดับ provider เริ่มต้นของคุณได้ใน [Inference Provider settings](<https://hf.co/settings/inference-providers>) (ไม่มี suffix = ใช้ลำดับนั้น)

  * **การรวมคอนฟิก:** รายการที่มีอยู่เดิมใน `models.providers.huggingface.models` (เช่น ใน `models.json`) จะยังคงอยู่เมื่อมีการรวมคอนฟิก ดังนั้น `name`, `alias` หรือ model option แบบกำหนดเองที่คุณตั้งไว้จะยังคงถูกรักษาไว้


การตั้งค่า environment และ daemon

หาก Gateway ทำงานเป็น daemon (launchd/systemd) โปรดตรวจสอบให้แน่ใจว่า `HUGGINGFACE_HUB_TOKEN` หรือ `HF_TOKEN` พร้อมใช้งานสำหรับ process นั้น (เช่น ใน `~/.openclaw/.env` หรือผ่าน `env.shellEnv`)

คอนฟิก: DeepSeek R1 พร้อม fallback เป็น Qwen json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-R1",        fallbacks: ["huggingface/Qwen/Qwen3-8B"],      },      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1" },        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },      },    },  },}
[/code]

คอนฟิก: Qwen พร้อมตัวแปร cheapest และ fastest json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen3-8B" },      models: {        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },        "huggingface/Qwen/Qwen3-8B:cheapest": { alias: "Qwen3 8B (cheapest)" },        "huggingface/Qwen/Qwen3-8B:fastest": { alias: "Qwen3 8B (fastest)" },      },    },  },}
[/code]

คอนฟิก: DeepSeek + Llama + GPT-OSS พร้อม alias json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-V3.2",        fallbacks: [          "huggingface/meta-llama/Llama-3.3-70B-Instruct",          "huggingface/openai/gpt-oss-120b",        ],      },      models: {        "huggingface/deepseek-ai/DeepSeek-V3.2": { alias: "DeepSeek V3.2" },        "huggingface/meta-llama/Llama-3.3-70B-Instruct": { alias: "Llama 3.3 70B" },        "huggingface/openai/gpt-oss-120b": { alias: "GPT-OSS 120B" },      },    },  },}
[/code]

คอนฟิก: Qwen และ DeepSeek หลายตัวพร้อม suffix ของนโยบาย json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest" },      models: {        "huggingface/Qwen/Qwen2.5-7B-Instruct": { alias: "Qwen2.5 7B" },        "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest": { alias: "Qwen2.5 7B (cheap)" },        "huggingface/deepseek-ai/DeepSeek-R1:fastest": { alias: "DeepSeek R1 (fast)" },        "huggingface/meta-llama/Llama-3.1-8B-Instruct": { alias: "Llama 3.1 8B" },      },    },  },}
[/code]

## ที่เกี่ยวข้อง

[**การเลือกโมเดล** ภาพรวมของ provider ทั้งหมด, model ref และพฤติกรรม failover ](</th/concepts/model-providers>) [**การเลือกโมเดล** วิธีเลือกและกำหนดค่าโมเดล ](</th/concepts/models>) [**เอกสาร Inference Providers** เอกสารทางการของ Hugging Face Inference Providers ](<https://huggingface.co/docs/inference-providers>) [**Configuration** ข้อมูลอ้างอิงคอนฟิกแบบเต็ม ](</th/gateway/configuration>)

Was this useful?YesNo