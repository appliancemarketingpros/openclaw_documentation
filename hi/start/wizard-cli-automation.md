---
title: CLI स्वचालन
source_url: https://docs.openclaw.ai/hi/start/wizard-cli-automation
scraped_at: 2026-06-29
---

Get startedGuides

`openclaw onboard` को स्वचालित करने के लिए `--non-interactive` का उपयोग करें।

## आधारभूत non-interactive उदाहरण

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --secret-input-mode plaintext \  --gateway-port 18789 \  --gateway-bind loopback \  --install-daemon \  --daemon-runtime node \  --skip-bootstrap \  --skip-skills
[/code]

मशीन-पठनीय सारांश के लिए `--json` जोड़ें।

जब आपकी automation workspace फ़ाइलों को पहले से seed करती है और onboarding से default bootstrap फ़ाइलें बनवाना नहीं चाहती, तब `--skip-bootstrap` का उपयोग करें।

plaintext values के बजाय auth profiles में env-backed refs store करने के लिए `--secret-input-mode ref` का उपयोग करें। env refs और configured provider refs (`file` या `exec`) के बीच interactive selection onboarding flow में उपलब्ध है।

non-interactive `ref` मोड में, provider env vars process environment में set होने चाहिए। matching env var के बिना inline key flags पास करने पर अब तुरंत fail होता है।

उदाहरण:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

## Provider-specific उदाहरण

Anthropic API key उदाहरण bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Gemini उदाहरण bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Z.AI उदाहरण bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice zai-api-key \  --zai-api-key "$ZAI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Vercel AI Gateway उदाहरण bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Cloudflare AI Gateway उदाहरण bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Moonshot उदाहरण bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice moonshot-api-key \  --moonshot-api-key "$MOONSHOT_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Mistral उदाहरण bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Synthetic उदाहरण bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice synthetic-api-key \  --synthetic-api-key "$SYNTHETIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

OpenCode उदाहरण bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice opencode-zen \  --opencode-zen-api-key "$OPENCODE_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Go catalog के लिए `--auth-choice opencode-go --opencode-go-api-key "$OPENCODE_API_KEY"` पर switch करें।

Ollama उदाहरण bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ollama \  --custom-model-id "qwen3.5:27b" \  --accept-risk \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Custom provider उदाहरण bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

`--custom-api-key` वैकल्पिक है। यदि इसे छोड़ा गया है, तो onboarding `CUSTOM_API_KEY` जांचता है। OpenClaw सामान्य vision model IDs को image-capable के रूप में स्वचालित रूप से mark करता है। अज्ञात custom vision IDs के लिए `--custom-image-input` जोड़ें, या केवल-text metadata को force करने के लिए `--custom-text-input` जोड़ें।

Ref-mode variant:

bashCopy code
[code]
    export CUSTOM_API_KEY="your-key"openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --secret-input-mode ref \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

इस मोड में, onboarding `apiKey` को `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }` के रूप में store करता है।

Anthropic setup-token समर्थित onboarding token path के रूप में उपलब्ध रहता है, लेकिन OpenClaw अब उपलब्ध होने पर Claude CLI reuse को प्राथमिकता देता है। production के लिए, Anthropic API key को प्राथमिकता दें।

## एक और agent जोड़ें

अपने workspace, sessions, और auth profiles वाले अलग agent को बनाने के लिए `openclaw agents add <name>` का उपयोग करें। `--workspace` के बिना चलाने पर wizard launch होता है।

bashCopy code
[code]
    openclaw agents add work \  --workspace ~/.openclaw/workspace-work \  --model openai/gpt-5.5 \  --bind whatsapp:biz \  --non-interactive \  --json
[/code]

यह क्या set करता है:

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


नोट्स:

  * Default workspaces `~/.openclaw/workspace-<agentId>` का अनुसरण करते हैं।
  * inbound messages route करने के लिए `bindings` जोड़ें (wizard यह कर सकता है)।
  * Non-interactive flags: `--model`, `--agent-dir`, `--bind`, `--non-interactive`।


## संबंधित दस्तावेज़

  * Onboarding hub: [Onboarding (CLI)](</hi/start/wizard>)
  * पूर्ण reference: [CLI Setup Reference](</hi/start/wizard-cli-reference>)
  * Command reference: [`openclaw onboard`](</hi/cli/onboard>)


Was this useful?YesNo

Open issue