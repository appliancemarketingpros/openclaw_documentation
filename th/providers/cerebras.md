---
title: Cerebras
source_url: https://docs.openclaw.ai/th/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>) ให้บริการ inference ความเร็วสูงที่เข้ากันได้กับ OpenAI บนฮาร์ดแวร์ inference แบบกำหนดเอง OpenClaw มี Plugin ผู้ให้บริการ Cerebras ที่บันเดิลมาให้ พร้อมแค็ตตาล็อกแบบคงที่จำนวนสี่โมเดล

คุณสมบัติ | ค่า  
---|---  
รหัสผู้ให้บริการ | `cerebras`  
Plugin | บันเดิลมาให้, `enabledByDefault: true`  
ตัวแปร env สำหรับการยืนยันตัวตน | `CEREBRAS_API_KEY`  
แฟล็กการเริ่มต้นใช้งาน | `--auth-choice cerebras-api-key`  
แฟล็ก CLI โดยตรง | `--cerebras-api-key <key>`  
API | เข้ากันได้กับ OpenAI (`openai-completions`)  
Base URL | `https://api.cerebras.ai/v1`  
โมเดลเริ่มต้น | `cerebras/zai-glm-4.7`  
  
## เริ่มต้นใช้งาน

* ### รับ API key

สร้าง API key ใน [Cerebras Cloud Console](<https://cloud.cerebras.ai>)

* ### เรียกใช้การเริ่มต้นใช้งาน

OnboardingCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

Env onlyCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### ตรวจสอบว่าโมเดลพร้อมใช้งาน

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

รายการควรมีโมเดลที่บันเดิลมาให้ครบทั้งสี่โมเดล หาก `CEREBRAS_API_KEY` ไม่สามารถ resolve ได้ `openclaw models status --json` จะรายงานข้อมูลรับรองที่ขาดหายภายใต้ `auth.unusableProfiles`

## การตั้งค่าแบบไม่โต้ตอบ

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## แค็ตตาล็อกในตัว

OpenClaw มาพร้อมแค็ตตาล็อก Cerebras แบบคงที่ซึ่งสะท้อน endpoint สาธารณะที่เข้ากันได้กับ OpenAI โมเดลทั้งสี่ใช้ context 128k และ token เอาต์พุตสูงสุด 8,192 ร่วมกัน

การอ้างอิงโมเดล | ชื่อ | การให้เหตุผล | หมายเหตุ  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | ใช่ | โมเดลเริ่มต้น; โมเดลให้เหตุผลแบบพรีวิว  
`cerebras/gpt-oss-120b` | GPT OSS 120B | ใช่ | โมเดลให้เหตุผลสำหรับโปรดักชัน  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | ไม่ใช่ | โมเดลที่ไม่ให้เหตุผลแบบพรีวิว  
`cerebras/llama3.1-8b` | Llama 3.1 8B | ไม่ใช่ | โมเดลสำหรับโปรดักชันที่เน้นความเร็ว  
  
## การกำหนดค่าด้วยตนเอง

โดยทั่วไป Plugin ที่บันเดิลมาให้หมายความว่าคุณต้องใช้เพียง API key เท่านั้น ใช้การกำหนดค่า `models.providers.cerebras` อย่างชัดเจนเมื่อคุณต้องการแทนที่เมตาดาต้าของโมเดล หรือเรียกใช้ใน `mode: "merge"` กับแค็ตตาล็อกแบบคงที่:

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## ที่เกี่ยวข้อง

[**ผู้ให้บริการโมเดล** การเลือกผู้ให้บริการ การอ้างอิงโมเดล และพฤติกรรม failover ](</th/concepts/model-providers>) [**โหมดการคิด** ระดับ effort สำหรับการให้เหตุผลของโมเดล Cerebras สองโมเดลที่รองรับการให้เหตุผล ](</th/tools/thinking>) [**ข้อมูลอ้างอิงการกำหนดค่า** ค่าเริ่มต้นของ Agent และการกำหนดค่าโมเดล ](</th/gateway/config-agents#agent-defaults>) [**FAQ เกี่ยวกับโมเดล** โปรไฟล์การยืนยันตัวตน การสลับโมเดล และการแก้ข้อผิดพลาด "no profile" ](</th/help/faq-models>)

Was this useful?YesNo