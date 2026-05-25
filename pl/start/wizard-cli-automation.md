---
title: Automatyzacja CLI
source_url: https://docs.openclaw.ai/pl/start/wizard-cli-automation
scraped_at: 2026-05-25
---

Użyj `--non-interactive`, aby zautomatyzować `openclaw onboard`.

## Bazowy przykład nieinteraktywny

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --secret-input-mode plaintext \  --gateway-port 18789 \  --gateway-bind loopback \  --install-daemon \  --daemon-runtime node \  --skip-bootstrap \  --skip-skills
[/code]

Dodaj `--json`, aby uzyskać podsumowanie czytelne maszynowo.

Użyj `--skip-bootstrap`, gdy automatyzacja wstępnie tworzy pliki obszaru roboczego i nie ma tworzyć domyślnych plików startowych podczas onboardingu.

Użyj `--secret-input-mode ref`, aby przechowywać referencje oparte na zmiennych środowiskowych w profilach uwierzytelniania zamiast wartości w postaci zwykłego tekstu. Interaktywny wybór między referencjami env a skonfigurowanymi referencjami dostawcy (`file` lub `exec`) jest dostępny w przepływie onboardingu.

W nieinteraktywnym trybie `ref` zmienne środowiskowe dostawcy muszą być ustawione w środowisku procesu. Przekazanie flag kluczy inline bez pasującej zmiennej środowiskowej kończy się teraz szybkim błędem.

Przykład:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

## Przykłady specyficzne dla dostawców

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

Przełącz na `--auth-choice opencode-go --opencode-go-api-key "$OPENCODE_API_KEY"` dla katalogu Go.

Ollama example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ollama \  --custom-model-id "qwen3.5:27b" \  --accept-risk \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Custom provider example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

`--custom-api-key` jest opcjonalne. Jeśli zostanie pominięte, onboarding sprawdza `CUSTOM_API_KEY`. OpenClaw automatycznie oznacza typowe identyfikatory modeli wizyjnych jako obsługujące obrazy. Dodaj `--custom-image-input` dla nieznanych niestandardowych identyfikatorów wizyjnych albo `--custom-text-input`, aby wymusić metadane tylko tekstowe.

Wariant w trybie ref:

bashCopy code
[code]
    export CUSTOM_API_KEY="your-key"openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --secret-input-mode ref \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

W tym trybie onboarding przechowuje `apiKey` jako `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`.

Token konfiguracyjny Anthropic pozostaje dostępny jako obsługiwana ścieżka tokenu onboardingu, ale OpenClaw preferuje teraz ponowne użycie Claude CLI, gdy jest dostępne. W środowisku produkcyjnym preferuj klucz API Anthropic.

## Dodaj kolejnego agenta

Użyj `openclaw agents add <name>`, aby utworzyć osobnego agenta z własnym obszarem roboczym, sesjami i profilami uwierzytelniania. Uruchomienie bez `--workspace` włącza kreatora.

bashCopy code
[code]
    openclaw agents add work \  --workspace ~/.openclaw/workspace-work \  --model openai/gpt-5.5 \  --bind whatsapp:biz \  --non-interactive \  --json
[/code]

Co ustawia:

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


Uwagi:

  * Domyślne obszary robocze używają wzorca `~/.openclaw/workspace-<agentId>`.
  * Dodaj `bindings`, aby kierować wiadomości przychodzące (kreator może to zrobić).
  * Flagi nieinteraktywne: `--model`, `--agent-dir`, `--bind`, `--non-interactive`.


## Powiązana dokumentacja

  * Centrum onboardingu: [Onboarding (CLI)](</pl/start/wizard>)
  * Pełna dokumentacja: [Dokumentacja konfiguracji CLI](</pl/start/wizard-cli-reference>)
  * Dokumentacja polecenia: [`openclaw onboard`](</pl/cli/onboard>)


Was this useful?YesNo