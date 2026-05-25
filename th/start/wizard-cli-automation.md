---
title: การทำงานอัตโนมัติของ CLI
source_url: https://docs.openclaw.ai/th/start/wizard-cli-automation
scraped_at: 2026-05-25
---

ใช้ `--non-interactive` เพื่อทำให้ `openclaw onboard` ทำงานอัตโนมัติ

## ตัวอย่างพื้นฐานแบบไม่โต้ตอบ

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --secret-input-mode plaintext \  --gateway-port 18789 \  --gateway-bind loopback \  --install-daemon \  --daemon-runtime node \  --skip-bootstrap \  --skip-skills
[/code]

เพิ่ม `--json` เพื่อรับสรุปที่เครื่องอ่านได้

ใช้ `--skip-bootstrap` เมื่อระบบอัตโนมัติของคุณเตรียมไฟล์พื้นที่ทำงานไว้ล่วงหน้า และไม่ต้องการให้ onboarding สร้างไฟล์ bootstrap เริ่มต้น

ใช้ `--secret-input-mode ref` เพื่อจัดเก็บการอ้างอิงที่รองรับด้วย env ในโปรไฟล์การรับรองความถูกต้องแทนค่าข้อความธรรมดา การเลือกแบบโต้ตอบระหว่างการอ้างอิง env และการอ้างอิงผู้ให้บริการที่กำหนดค่าไว้ (`file` หรือ `exec`) มีให้ใช้ในโฟลว์ onboarding

ในโหมด `ref` แบบไม่โต้ตอบ ต้องตั้งค่าตัวแปร env ของผู้ให้บริการในสภาพแวดล้อมของกระบวนการ การส่งแฟล็กคีย์แบบอินไลน์โดยไม่มีตัวแปร env ที่ตรงกันจะล้มเหลวทันที

ตัวอย่าง:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

## ตัวอย่างเฉพาะผู้ให้บริการ

ตัวอย่างคีย์ Anthropic API bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

ตัวอย่าง Gemini bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

ตัวอย่าง Z.AI bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice zai-api-key \  --zai-api-key "$ZAI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

ตัวอย่าง Vercel AI Gateway bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

ตัวอย่าง Cloudflare AI Gateway bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

ตัวอย่าง Moonshot bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice moonshot-api-key \  --moonshot-api-key "$MOONSHOT_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

ตัวอย่าง Mistral bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

ตัวอย่าง Synthetic bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice synthetic-api-key \  --synthetic-api-key "$SYNTHETIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

ตัวอย่าง OpenCode bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice opencode-zen \  --opencode-zen-api-key "$OPENCODE_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

เปลี่ยนเป็น `--auth-choice opencode-go --opencode-go-api-key "$OPENCODE_API_KEY"` สำหรับแค็ตตาล็อก Go

ตัวอย่าง Ollama bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ollama \  --custom-model-id "qwen3.5:27b" \  --accept-risk \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

ตัวอย่างผู้ให้บริการแบบกำหนดเอง bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

`--custom-api-key` เป็นตัวเลือก หากละไว้ onboarding จะตรวจสอบ `CUSTOM_API_KEY` OpenClaw ทำเครื่องหมาย ID โมเดล vision ทั่วไปว่าใช้งานรูปภาพได้โดยอัตโนมัติ เพิ่ม `--custom-image-input` สำหรับ ID vision แบบกำหนดเองที่ไม่รู้จัก หรือ `--custom-text-input` เพื่อบังคับ metadata แบบข้อความเท่านั้น

ตัวแปรโหมด ref:

bashCopy code
[code]
    export CUSTOM_API_KEY="your-key"openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --secret-input-mode ref \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

ในโหมดนี้ onboarding จะจัดเก็บ `apiKey` เป็น `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`

setup-token ของ Anthropic ยังคงมีให้ใช้เป็นเส้นทางโทเค็น onboarding ที่รองรับ แต่ตอนนี้ OpenClaw ต้องการนำ Claude CLI กลับมาใช้เมื่อพร้อมใช้งาน สำหรับการใช้งานจริง ให้ใช้คีย์ Anthropic API เป็นหลัก

## เพิ่มเอเจนต์อีกตัว

ใช้ `openclaw agents add <name>` เพื่อสร้างเอเจนต์แยกต่างหากที่มีพื้นที่ทำงาน, เซสชัน และโปรไฟล์การรับรองความถูกต้องของตัวเอง การรันโดยไม่มี `--workspace` จะเปิดตัวช่วยตั้งค่า

bashCopy code
[code]
    openclaw agents add work \  --workspace ~/.openclaw/workspace-work \  --model openai/gpt-5.5 \  --bind whatsapp:biz \  --non-interactive \  --json
[/code]

สิ่งที่ตั้งค่า:

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


หมายเหตุ:

  * พื้นที่ทำงานเริ่มต้นใช้รูปแบบ `~/.openclaw/workspace-<agentId>`
  * เพิ่ม `bindings` เพื่อกำหนดเส้นทางข้อความขาเข้า (ตัวช่วยตั้งค่าสามารถทำสิ่งนี้ได้)
  * แฟล็กแบบไม่โต้ตอบ: `--model`, `--agent-dir`, `--bind`, `--non-interactive`


## เอกสารที่เกี่ยวข้อง

  * ศูนย์กลาง onboarding: [Onboarding (CLI)](</th/start/wizard>)
  * เอกสารอ้างอิงฉบับเต็ม: [เอกสารอ้างอิงการตั้งค่า CLI](</th/start/wizard-cli-reference>)
  * เอกสารอ้างอิงคำสั่ง: [`openclaw onboard`](</th/cli/onboard>)


Was this useful?YesNo