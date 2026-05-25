---
title: Автоматизація CLI
source_url: https://docs.openclaw.ai/uk/start/wizard-cli-automation
scraped_at: 2026-05-25
---

Використовуйте `--non-interactive`, щоб автоматизувати `openclaw onboard`.

## Базовий неінтерактивний приклад

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --secret-input-mode plaintext \  --gateway-port 18789 \  --gateway-bind loopback \  --install-daemon \  --daemon-runtime node \  --skip-bootstrap \  --skip-skills
[/code]

Додайте `--json` для машинно-зчитуваного підсумку.

Використовуйте `--skip-bootstrap`, коли ваша автоматизація заздалегідь створює файли робочого простору й не хоче, щоб початкове налаштування створювало стандартні bootstrap-файли.

Використовуйте `--secret-input-mode ref`, щоб зберігати посилання на основі env у профілях автентифікації замість plaintext-значень. Інтерактивний вибір між посиланнями env і налаштованими посиланнями постачальника (`file` або `exec`) доступний у процесі початкового налаштування.

У неінтерактивному режимі `ref` змінні середовища постачальника мають бути встановлені в середовищі процесу. Передавання inline-прапорців ключа без відповідної змінної середовища тепер швидко завершується помилкою.

Приклад:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

## Приклади для окремих постачальників

Anthropic API key example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Gemini example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Z.AI example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice zai-api-key \  --zai-api-key "$ZAI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Vercel AI Gateway example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Cloudflare AI Gateway example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Moonshot example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice moonshot-api-key \  --moonshot-api-key "$MOONSHOT_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Mistral example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Synthetic example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice synthetic-api-key \  --synthetic-api-key "$SYNTHETIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

OpenCode example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice opencode-zen \  --opencode-zen-api-key "$OPENCODE_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Перейдіть на `--auth-choice opencode-go --opencode-go-api-key "$OPENCODE_API_KEY"` для каталогу Go.

Ollama example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ollama \  --custom-model-id "qwen3.5:27b" \  --accept-risk \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Custom provider example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

`--custom-api-key` є необов’язковим. Якщо його пропущено, початкове налаштування перевіряє `CUSTOM_API_KEY`. OpenClaw автоматично позначає поширені ідентифікатори моделей із підтримкою зору як здатні обробляти зображення. Додайте `--custom-image-input` для невідомих користувацьких ідентифікаторів моделей із підтримкою зору або `--custom-text-input`, щоб примусово встановити метадані лише для тексту.

Варіант режиму посилань:

bashCopy code
[code]
    export CUSTOM_API_KEY="your-key"openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --secret-input-mode ref \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

У цьому режимі початкове налаштування зберігає `apiKey` як `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`.

setup-token Anthropic залишається доступним як підтримуваний шлях токена початкового налаштування, але OpenClaw тепер віддає перевагу повторному використанню Claude CLI, коли воно доступне. Для production використовуйте ключ API Anthropic.

## Додайте іншого агента

Використовуйте `openclaw agents add <name>`, щоб створити окремого агента з власним робочим простором, сесіями та профілями автентифікації. Запуск без `--workspace` відкриває майстер.

bashCopy code
[code]
    openclaw agents add work \  --workspace ~/.openclaw/workspace-work \  --model openai/gpt-5.5 \  --bind whatsapp:biz \  --non-interactive \  --json
[/code]

Що він задає:

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


Примітки:

  * Стандартні робочі простори відповідають `~/.openclaw/workspace-<agentId>`.
  * Додайте `bindings`, щоб спрямовувати вхідні повідомлення (майстер може це зробити).
  * Неінтерактивні прапорці: `--model`, `--agent-dir`, `--bind`, `--non-interactive`.


## Пов’язана документація

  * Центр початкового налаштування: [Початкове налаштування (CLI)](</uk/start/wizard>)
  * Повний довідник: [Довідник із налаштування CLI](</uk/start/wizard-cli-reference>)
  * Довідник команд: [`openclaw onboard`](</uk/cli/onboard>)


Was this useful?YesNo