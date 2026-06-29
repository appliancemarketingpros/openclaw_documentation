---
title: OpenCode
source_url: https://docs.openclaw.ai/hi/providers/opencode
scraped_at: 2026-06-29
---

ModelsProviders

OpenCode, OpenClaw में दो hosted catalog उजागर करता है:

Catalog | Prefix | Runtime provider  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
दोनों catalog एक ही OpenCode API key का उपयोग करते हैं। OpenClaw runtime provider ids को अलग रखता है ताकि upstream per-model routing सही रहे, लेकिन onboarding और docs उन्हें एक OpenCode setup के रूप में देखते हैं।

## शुरू करना

### Zen catalog

**इसके लिए सर्वोत्तम:** curated OpenCode multi-model proxy (Claude, GPT, Gemini, GLM).

* ### onboarding चलाएँ

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

या key सीधे पास करें:

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### एक Zen model को default के रूप में सेट करें

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### सत्यापित करें कि models उपलब्ध हैं

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Go catalog

**इसके लिए सर्वोत्तम:** OpenCode-hosted Kimi, GLM, और MiniMax lineup.

* ### onboarding चलाएँ

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

या key सीधे पास करें:

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### एक Go model को default के रूप में सेट करें

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### सत्यापित करें कि models उपलब्ध हैं

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Config उदाहरण

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## अंतर्निहित catalog

### Zen

गुण | मान  
---|---  
Runtime provider | `opencode`  
उदाहरण models | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3.1-pro`, `opencode/glm-5.2`  
  
### Go

गुण | मान  
---|---  
Runtime provider | `opencode-go`  
उदाहरण models | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## उन्नत configuration

API key aliases

`OPENCODE_ZEN_API_KEY`, `OPENCODE_API_KEY` के alias के रूप में भी समर्थित है।

साझा credentials

setup के दौरान एक OpenCode key दर्ज करने से दोनों runtime providers के लिए credentials संग्रहीत हो जाते हैं। आपको प्रत्येक catalog को अलग से onboard करने की आवश्यकता नहीं है।

Billing और dashboard

आप OpenCode में sign in करते हैं, billing details जोड़ते हैं, और अपनी API key copy करते हैं। Billing और catalog availability OpenCode dashboard से manage की जाती है।

Gemini replay behavior

Gemini-backed OpenCode refs proxy-Gemini path पर रहते हैं, इसलिए OpenClaw वहाँ Gemini thought-signature sanitation रखता है, native Gemini replay validation या bootstrap rewrites enable किए बिना।

Non-Gemini replay behavior

Non-Gemini OpenCode refs न्यूनतम OpenAI-compatible replay policy रखते हैं।

## संबंधित

[**Model selection** providers, model refs, और failover behavior चुनना। ](</hi/concepts/model-providers>) [**Configuration reference** agents, models, और providers के लिए पूरा config reference। ](</hi/gateway/configuration-reference>)

Was this useful?YesNo

Open issue