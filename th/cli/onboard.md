---
title: เริ่มต้นใช้งาน
source_url: https://docs.openclaw.ai/th/cli/onboard
scraped_at: 2026-05-25
---

# `openclaw onboard`

การตั้งค่าเริ่มต้นแบบมีคำแนะนำครบถ้วนสำหรับการตั้งค่า Gateway แบบโลคัลหรือรีโมต ใช้คำสั่งนี้เมื่อคุณต้องการให้ OpenClaw พาไล่ผ่านการยืนยันตัวตนของโมเดล พื้นที่ทำงาน Gateway ช่องทาง Skills และสุขภาพระบบในโฟลว์เดียว

## คู่มือที่เกี่ยวข้อง

[**ศูนย์รวมการตั้งค่าเริ่มต้นของ CLI** คำแนะนำแบบทีละขั้นของโฟลว์ CLI แบบโต้ตอบ ](</th/start/wizard>) [**ภาพรวมการตั้งค่าเริ่มต้น** วิธีที่การตั้งค่าเริ่มต้นของ OpenClaw ทำงานร่วมกัน ](</th/start/onboarding-overview>) [**เอกสารอ้างอิงการตั้งค่า CLI** เอาต์พุต กลไกภายใน และพฤติกรรมรายขั้นตอน ](</th/start/wizard-cli-reference>) [**การทำงานอัตโนมัติของ CLI** แฟล็กแบบไม่โต้ตอบและการตั้งค่าผ่านสคริปต์ ](</th/start/wizard-cli-automation>) [**การตั้งค่าเริ่มต้นของแอป macOS** โฟลว์การตั้งค่าเริ่มต้นสำหรับแอปแถบเมนูของ macOS ](</th/start/onboarding>)

## ตัวอย่าง

bashCopy code
[code]
    openclaw onboardopenclaw onboard --modernopenclaw onboard --flow quickstartopenclaw onboard --flow manualopenclaw onboard --flow importopenclaw onboard --import-from hermes --import-source ~/.hermesopenclaw onboard --skip-bootstrapopenclaw onboard --mode remote --remote-url wss://gateway-host:18789
[/code]

`--flow import` ใช้ผู้ให้บริการ migration ที่ Plugin เป็นเจ้าของ เช่น Hermes โดยจะทำงานกับการตั้งค่า OpenClaw ใหม่เท่านั้น หากมีไฟล์ config, credentials, sessions หรือไฟล์ memory/identity ของพื้นที่ทำงานอยู่แล้ว ให้รีเซ็ตหรือเลือกการตั้งค่าใหม่ก่อนนำเข้า

`--modern` เริ่มพรีวิวการตั้งค่าเริ่มต้นแบบสนทนาของ Crestodian หากไม่มี `--modern`, `openclaw onboard` จะคงใช้โฟลว์การตั้งค่าเริ่มต้นแบบคลาสสิก

สำหรับเป้าหมาย `ws://` แบบ plaintext ในเครือข่ายส่วนตัว (เฉพาะเครือข่ายที่เชื่อถือได้) ให้ตั้งค่า `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` ใน environment ของกระบวนการตั้งค่าเริ่มต้น ไม่มีตัวเทียบเท่าใน `openclaw.json` สำหรับ transport ฝั่งไคลเอนต์ แบบ break-glass นี้

ผู้ให้บริการแบบกำหนดเองในโหมดไม่โต้ตอบ:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --secret-input-mode plaintext \  --custom-compatibility openai \  --custom-image-input
[/code]

`--custom-api-key` เป็นตัวเลือกในโหมดไม่โต้ตอบ หากละไว้ การตั้งค่าเริ่มต้นจะตรวจสอบ `CUSTOM_API_KEY` OpenClaw ทำเครื่องหมาย ID โมเดล vision ทั่วไปว่า รองรับรูปภาพโดยอัตโนมัติ ส่ง `--custom-image-input` สำหรับ ID vision แบบกำหนดเองที่ไม่รู้จัก หรือ `--custom-text-input` เพื่อบังคับ metadata แบบข้อความเท่านั้น

LM Studio ยังรองรับแฟล็กคีย์เฉพาะผู้ให้บริการในโหมดไม่โต้ตอบด้วย:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice lmstudio \  --custom-base-url "http://localhost:1234/v1" \  --custom-model-id "qwen/qwen3.5-9b" \  --lmstudio-api-key "$LM_API_TOKEN" \  --accept-risk
[/code]

Ollama แบบไม่โต้ตอบ:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice ollama \  --custom-base-url "http://ollama-host:11434" \  --custom-model-id "qwen3.5:27b" \  --accept-risk
[/code]

`--custom-base-url` มีค่าเริ่มต้นเป็น `http://127.0.0.1:11434` `--custom-model-id` เป็นตัวเลือก หากละไว้ การตั้งค่าเริ่มต้นจะใช้ค่าเริ่มต้นที่ Ollama แนะนำ ID โมเดลคลาวด์ เช่น `kimi-k2.5:cloud` ก็ใช้ได้ที่นี่เช่นกัน

จัดเก็บคีย์ผู้ให้บริการเป็น refs แทน plaintext:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

เมื่อใช้ `--secret-input-mode ref` การตั้งค่าเริ่มต้นจะเขียน refs ที่อ้างอิง env แทนค่าคีย์ plaintext สำหรับผู้ให้บริการที่อิง auth-profile สิ่งนี้จะเขียนรายการ `keyRef`; สำหรับผู้ให้บริการแบบกำหนดเอง สิ่งนี้จะเขียน `models.providers.<id>.apiKey` เป็น env ref (เช่น `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`)

สัญญาของโหมด `ref` แบบไม่โต้ตอบ:

  * ตั้งค่า env var ของผู้ให้บริการใน environment ของกระบวนการตั้งค่าเริ่มต้น (เช่น `OPENAI_API_KEY`)
  * อย่าส่งแฟล็กคีย์แบบ inline (เช่น `--openai-api-key`) เว้นแต่ว่า env var นั้นถูกตั้งค่าไว้ด้วย
  * หากส่งแฟล็กคีย์แบบ inline โดยไม่มี env var ที่จำเป็น การตั้งค่าเริ่มต้นจะล้มเหลวทันทีพร้อมคำแนะนำ


ตัวเลือกโทเค็น Gateway ในโหมดไม่โต้ตอบ:

  * `--gateway-auth token --gateway-token <token>` จัดเก็บโทเค็นแบบ plaintext
  * `--gateway-auth token --gateway-token-ref-env <name>` จัดเก็บ `gateway.auth.token` เป็น env SecretRef
  * `--gateway-token` และ `--gateway-token-ref-env` ใช้ร่วมกันไม่ได้
  * `--gateway-token-ref-env` ต้องมี env var ที่ไม่ว่างใน environment ของกระบวนการตั้งค่าเริ่มต้น
  * เมื่อใช้ `--install-daemon` หาก token auth ต้องใช้โทเค็น โทเค็น Gateway ที่จัดการด้วย SecretRef จะถูกตรวจสอบความถูกต้อง แต่จะไม่ถูกบันทึกเป็น plaintext ที่ resolve แล้วใน metadata ของ environment บริการ supervisor
  * เมื่อใช้ `--install-daemon` หากโหมดโทเค็นต้องใช้โทเค็นและ SecretRef ของโทเค็นที่กำหนดไว้ยัง resolve ไม่ได้ การตั้งค่าเริ่มต้นจะ fail closed พร้อมคำแนะนำการแก้ไข
  * เมื่อใช้ `--install-daemon` หากมีทั้ง `gateway.auth.token` และ `gateway.auth.password` ถูกกำหนดไว้ และ `gateway.auth.mode` ไม่ได้ตั้งค่า การตั้งค่าเริ่มต้นจะบล็อกการติดตั้งจนกว่าจะตั้งค่า mode อย่างชัดเจน
  * การตั้งค่าเริ่มต้นแบบโลคัลจะเขียน `gateway.mode="local"` ลงใน config หากไฟล์ config ภายหลังไม่มี `gateway.mode` ให้ถือว่าเป็น config ที่เสียหายหรือการแก้ไขด้วยตนเองที่ไม่สมบูรณ์ ไม่ใช่ทางลัด local-mode ที่ถูกต้อง
  * การตั้งค่าเริ่มต้นแบบโลคัลจะติดตั้ง Plugin ที่ดาวน์โหลดได้ซึ่งเลือกไว้ เมื่อเส้นทางการตั้งค่าที่เลือกต้องใช้
  * การตั้งค่าเริ่มต้นแบบรีโมตจะเขียนเฉพาะข้อมูลการเชื่อมต่อสำหรับ Gateway รีโมต และไม่ติดตั้งแพ็กเกจ Plugin โลคัล
  * `--allow-unconfigured` เป็น escape hatch สำหรับรันไทม์ Gateway แยกต่างหาก ไม่ได้หมายความว่าการตั้งค่าเริ่มต้นสามารถละ `gateway.mode` ได้


ตัวอย่าง:

bashCopy code
[code]
    export OPENCLAW_GATEWAY_TOKEN="your-token"openclaw onboard --non-interactive \  --mode local \  --auth-choice skip \  --gateway-auth token \  --gateway-token-ref-env OPENCLAW_GATEWAY_TOKEN \  --accept-risk
[/code]

สุขภาพ Gateway โลคัลแบบไม่โต้ตอบ:

  * เว้นแต่คุณจะส่ง `--skip-health` การตั้งค่าเริ่มต้นจะรอให้ Gateway โลคัลเข้าถึงได้ก่อนจึงจะออกสำเร็จ
  * `--install-daemon` จะเริ่มเส้นทางการติดตั้ง Gateway แบบจัดการก่อน หากไม่มี คุณต้องมี Gateway โลคัลที่ทำงานอยู่แล้ว เช่น `openclaw gateway run`
  * หากคุณต้องการเพียงการเขียน config/workspace/bootstrap ในระบบอัตโนมัติ ให้ใช้ `--skip-health`
  * หากคุณจัดการไฟล์พื้นที่ทำงานเอง ให้ส่ง `--skip-bootstrap` เพื่อตั้งค่า `agents.defaults.skipBootstrap: true` และข้ามการสร้าง `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md` และ `BOOTSTRAP.md`
  * บน Windows แบบ native, `--install-daemon` จะลอง Scheduled Tasks ก่อน และ fallback ไปยังรายการเข้าสู่ระบบในโฟลเดอร์ Startup ระดับผู้ใช้ หากการสร้าง task ถูกปฏิเสธ


พฤติกรรมการตั้งค่าเริ่มต้นแบบโต้ตอบเมื่อใช้โหมดอ้างอิง:

  * เลือก **ใช้การอ้างอิง secret** เมื่อระบบถาม
  * จากนั้นเลือกอย่างใดอย่างหนึ่ง: 
    * Environment variable
    * ผู้ให้บริการ secret ที่กำหนดค่าไว้ (`file` หรือ `exec`)
  * การตั้งค่าเริ่มต้นจะตรวจสอบ preflight อย่างรวดเร็วก่อนบันทึก ref 
    * หากการตรวจสอบล้มเหลว การตั้งค่าเริ่มต้นจะแสดงข้อผิดพลาดและให้คุณลองใหม่


### ตัวเลือก endpoint ของ [Z.AI](<http://Z.AI>) แบบไม่โต้ตอบ

bashCopy code
[code]
    # Promptless endpoint selectionopenclaw onboard --non-interactive \  --auth-choice zai-coding-global \  --zai-api-key "$ZAI_API_KEY" # Other Z.AI endpoint choices:# --auth-choice zai-coding-cn# --auth-choice zai-global# --auth-choice zai-cn
[/code]

ตัวอย่าง Mistral แบบไม่โต้ตอบ:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY"
[/code]

## หมายเหตุของโฟลว์

ประเภทโฟลว์

  * `quickstart`: prompt ขั้นต่ำ สร้างโทเค็น Gateway อัตโนมัติ
  * `manual`: prompt ครบถ้วนสำหรับ port, bind และ auth (alias ของ `advanced`)
  * `import`: เรียกใช้ผู้ให้บริการ migration ที่ตรวจพบ แสดงตัวอย่างแผน แล้วจึงปรับใช้หลังยืนยัน

การกรองผู้ให้บริการล่วงหน้า

เมื่อ auth choice บ่งชี้ผู้ให้บริการที่ต้องการ การตั้งค่าเริ่มต้นจะกรองตัวเลือก default-model และ allowlist ล่วงหน้าให้เหลือเฉพาะผู้ให้บริการนั้น สำหรับ Volcengine และ BytePlus สิ่งนี้จะจับคู่ตัวแปร coding-plan ด้วย (`volcengine-plan/*`, `byteplus-plan/*`)

หากตัวกรอง preferred-provider ยังไม่ให้โมเดลที่โหลดแล้ว การตั้งค่าเริ่มต้นจะ fallback ไปยังแค็ตตาล็อกที่ไม่ถูกกรองแทนการปล่อยให้ตัวเลือกว่าง

การถามต่อสำหรับ web-search

ผู้ให้บริการ web-search บางรายจะทริกเกอร์ prompt ติดตามผลเฉพาะผู้ให้บริการ:

  * **Grok** สามารถเสนอการตั้งค่า `x_search` แบบตัวเลือกด้วย `XAI_API_KEY` เดียวกันและตัวเลือกโมเดล `x_search`
  * **Kimi** สามารถถาม region ของ Moonshot API (`api.moonshot.ai` เทียบกับ `api.moonshot.cn`) และโมเดล web-search เริ่มต้นของ Kimi

พฤติกรรมอื่นๆ

  * พฤติกรรมขอบเขต DM ของการตั้งค่าเริ่มต้นแบบโลคัล: [เอกสารอ้างอิงการตั้งค่า CLI](</th/start/wizard-cli-reference#outputs-and-internals>)
  * แชตแรกที่เร็วที่สุด: `openclaw dashboard` (Control UI, ไม่ต้องตั้งค่าช่องทาง)
  * ผู้ให้บริการแบบกำหนดเอง: เชื่อมต่อ endpoint ที่เข้ากันได้กับ OpenAI หรือ Anthropic ใดก็ได้ รวมถึงผู้ให้บริการแบบ hosted ที่ไม่ได้อยู่ในรายการ ใช้ Unknown เพื่อตรวจหาอัตโนมัติ
  * หากตรวจพบสถานะ Hermes การตั้งค่าเริ่มต้นจะเสนอ migration flow ใช้ [Migrate](</th/cli/migrate>) สำหรับแผน dry-run, overwrite mode, reports และ mapping ที่แน่นอน


## คำสั่งติดตามผลทั่วไป

bashCopy code
[code]
    openclaw channels addopenclaw configureopenclaw agents add <name>
[/code]

ใช้ `openclaw setup` แทนเมื่อคุณต้องการเพียง config/พื้นที่ทำงานพื้นฐาน ใช้ `openclaw configure` ภายหลังสำหรับการเปลี่ยนแปลงเฉพาะจุด และ `openclaw channels add` สำหรับการตั้งค่าเฉพาะช่องทาง

Was this useful?YesNo