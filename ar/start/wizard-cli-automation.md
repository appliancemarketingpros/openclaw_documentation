---
title: أتمتة CLI
source_url: https://docs.openclaw.ai/ar/start/wizard-cli-automation
scraped_at: 2026-05-25
---

استخدم `--non-interactive` لأتمتة `openclaw onboard`.

## مثال أساسي غير تفاعلي

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --secret-input-mode plaintext \  --gateway-port 18789 \  --gateway-bind loopback \  --install-daemon \  --daemon-runtime node \  --skip-bootstrap \  --skip-skills
[/code]

أضف `--json` للحصول على ملخص قابل للقراءة آليًا.

استخدم `--skip-bootstrap` عندما تجهّز الأتمتة ملفات مساحة العمل مسبقًا ولا تريد أن ينشئ الإعداد الأولي ملفات bootstrap الافتراضية.

استخدم `--secret-input-mode ref` لتخزين مراجع مدعومة بمتغيرات البيئة في ملفات تعريف المصادقة بدلًا من قيم النص الصريح. يتوفر الاختيار التفاعلي بين مراجع البيئة ومراجع المزوّد المكوّنة (`file` أو `exec`) في تدفق الإعداد الأولي.

في وضع `ref` غير التفاعلي، يجب ضبط متغيرات بيئة المزوّد في بيئة العملية. يمثل تمرير أعلام المفاتيح المضمنة دون متغير البيئة المطابق فشلًا سريعًا الآن.

مثال:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

## أمثلة خاصة بالمزوّدين

مثال مفتاح Anthropic API bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

مثال Gemini bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

مثال Z.AI bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice zai-api-key \  --zai-api-key "$ZAI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

مثال Vercel AI Gateway bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

مثال Cloudflare AI Gateway bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

مثال Moonshot bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice moonshot-api-key \  --moonshot-api-key "$MOONSHOT_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

مثال Mistral bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

مثال Synthetic bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice synthetic-api-key \  --synthetic-api-key "$SYNTHETIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

مثال OpenCode bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice opencode-zen \  --opencode-zen-api-key "$OPENCODE_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

بدّل إلى `--auth-choice opencode-go --opencode-go-api-key "$OPENCODE_API_KEY"` لاستخدام كتالوج Go.

مثال Ollama bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ollama \  --custom-model-id "qwen3.5:27b" \  --accept-risk \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

مثال مزوّد مخصص bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

`--custom-api-key` اختياري. إذا حُذف، يتحقق الإعداد الأولي من `CUSTOM_API_KEY`. يعلّم OpenClaw معرفات نماذج الرؤية الشائعة على أنها تدعم الصور تلقائيًا. أضف `--custom-image-input` لمعرفات الرؤية المخصصة غير المعروفة، أو `--custom-text-input` لفرض بيانات وصفية نصية فقط.

متغير وضع المرجع:

bashCopy code
[code]
    export CUSTOM_API_KEY="your-key"openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --secret-input-mode ref \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

في هذا الوضع، يخزّن الإعداد الأولي `apiKey` على هيئة `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`.

يبقى رمز إعداد Anthropic متاحًا كمسار رمز إعداد أولي مدعوم، لكن OpenClaw يفضّل الآن إعادة استخدام Claude CLI عند توفره. للإنتاج، فضّل مفتاح Anthropic API.

## إضافة وكيل آخر

استخدم `openclaw agents add <name>` لإنشاء وكيل منفصل له مساحة العمل الخاصة به، والجلسات، وملفات تعريف المصادقة. يؤدي التشغيل دون `--workspace` إلى تشغيل المعالج.

bashCopy code
[code]
    openclaw agents add work \  --workspace ~/.openclaw/workspace-work \  --model openai/gpt-5.5 \  --bind whatsapp:biz \  --non-interactive \  --json
[/code]

ما يضبطه:

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


ملاحظات:

  * تتبع مساحات العمل الافتراضية النمط `~/.openclaw/workspace-<agentId>`.
  * أضف `bindings` لتوجيه الرسائل الواردة (يمكن للمعالج فعل ذلك).
  * أعلام الوضع غير التفاعلي: `--model`، و`--agent-dir`، و`--bind`، و`--non-interactive`.


## المستندات ذات الصلة

  * مركز الإعداد الأولي: [الإعداد الأولي (CLI)](</ar/start/wizard>)
  * المرجع الكامل: [مرجع إعداد CLI](</ar/start/wizard-cli-reference>)
  * مرجع الأوامر: [`openclaw onboard`](</ar/cli/onboard>)


Was this useful?YesNo