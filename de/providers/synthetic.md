---
title: Synthetic
source_url: https://docs.openclaw.ai/de/providers/synthetic
scraped_at: 2026-05-25
---

[Synthetic](<https://synthetic.new>) stellt Anthropic-kompatible Endpunkte bereit. OpenClaw registriert es als Provider `synthetic` und verwendet die Anthropic Messages API.

Eigenschaft | Wert  
---|---  
Provider | `synthetic`  
Auth | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
Base URL | `https://api.synthetic.new/anthropic`  
  
## Erste Schritte

* ### Einen API-Schlüssel holen

Besorgen Sie sich einen `SYNTHETIC_API_KEY` über Ihr Synthetic-Konto, oder lassen Sie sich im Onboarding-Assistenten danach fragen.

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### Das Standardmodell prüfen

Nach dem Onboarding ist das Standardmodell gesetzt auf:

CodeCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## Konfigurationsbeispiel

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## Integrierter Katalog

Alle Synthetic-Modelle verwenden Kosten `0` (Eingabe/Ausgabe/Cache).

Modell-ID | Kontextfenster | Max Tokens | Reasoning | Eingabe  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192,000 | 65,536 | nein | Text  
`hf:moonshotai/Kimi-K2-Thinking` | 256,000 | 8,192 | ja | Text  
`hf:zai-org/GLM-4.7` | 198,000 | 128,000 | nein | Text  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128,000 | 8,192 | nein | Text  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128,000 | 8,192 | nein | Text  
`hf:deepseek-ai/DeepSeek-V3.1` | 128,000 | 8,192 | nein | Text  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128,000 | 8,192 | nein | Text  
`hf:deepseek-ai/DeepSeek-V3.2` | 159,000 | 8,192 | nein | Text  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128,000 | 8,192 | nein | Text  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524,000 | 8,192 | nein | Text  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256,000 | 8,192 | nein | Text  
`hf:moonshotai/Kimi-K2.5` | 256,000 | 8,192 | ja | Text + Bild  
`hf:openai/gpt-oss-120b` | 128,000 | 8,192 | nein | Text  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256,000 | 8,192 | nein | Text  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256,000 | 8,192 | nein | Text  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250,000 | 8,192 | nein | Text + Bild  
`hf:zai-org/GLM-4.5` | 128,000 | 128,000 | nein | Text  
`hf:zai-org/GLM-4.6` | 198,000 | 128,000 | nein | Text  
`hf:zai-org/GLM-5` | 256,000 | 128,000 | ja | Text + Bild  
`hf:deepseek-ai/DeepSeek-V3` | 128,000 | 8,192 | nein | Text  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256,000 | 8,192 | ja | Text  
  
Modell-Allowlist

Wenn Sie eine Modell-Allowlist aktivieren (`agents.defaults.models`), fügen Sie jedes Synthetic-Modell hinzu, das Sie verwenden möchten. Modelle, die nicht in der Allowlist stehen, werden vor dem Agenten verborgen.

Überschreibung der Base URL

Wenn Synthetic seinen API-Endpunkt ändert, überschreiben Sie die Base URL in Ihrer Konfiguration:

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

Denken Sie daran, dass OpenClaw `/v1` automatisch anhängt.

## Verwandt

[**Modellauswahl** Provider-Regeln, Modell-Refs und Failover-Verhalten. ](</de/concepts/model-providers>) [**Konfigurationsreferenz** Vollständiges Konfigurationsschema einschließlich Provider-Einstellungen. ](</de/gateway/configuration-reference>) [**Synthetic** Synthetic-Dashboard und API-Dokumentation. ](<https://synthetic.new>)

Was this useful?YesNo