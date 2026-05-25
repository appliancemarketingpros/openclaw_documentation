---
title: Synthetic
source_url: https://docs.openclaw.ai/tr/providers/synthetic
scraped_at: 2026-05-25
---

[Synthetic](<https://synthetic.new>), Anthropic uyumlu uç noktalar sunar. OpenClaw bunu `synthetic` sağlayıcısı olarak kaydeder ve Anthropic Messages API'yi kullanır.

Özellik | Değer  
---|---  
Sağlayıcı | `synthetic`  
Auth | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
Base URL | `https://api.synthetic.new/anthropic`  
  
## Başlangıç

* ### Bir API anahtarı alın

Synthetic hesabınızdan bir `SYNTHETIC_API_KEY` alın veya onboarding sihirbazının sizden bunu istemesine izin verin.

* ### Onboarding çalıştırın

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### Varsayılan modeli doğrulayın

Onboarding sonrasında varsayılan model şu olarak ayarlanır:

CodeCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## Yapılandırma örneği

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## Yerleşik katalog

Tüm Synthetic modelleri maliyet olarak `0` kullanır (giriş/çıkış/önbellek).

Model ID | Bağlam penceresi | Azami token | Akıl yürütme | Girdi  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192,000 | 65,536 | no | text  
`hf:moonshotai/Kimi-K2-Thinking` | 256,000 | 8,192 | yes | text  
`hf:zai-org/GLM-4.7` | 198,000 | 128,000 | no | text  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3.1` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3.2` | 159,000 | 8,192 | no | text  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128,000 | 8,192 | no | text  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524,000 | 8,192 | no | text  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256,000 | 8,192 | no | text  
`hf:moonshotai/Kimi-K2.5` | 256,000 | 8,192 | yes | text + image  
`hf:openai/gpt-oss-120b` | 128,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250,000 | 8,192 | no | text + image  
`hf:zai-org/GLM-4.5` | 128,000 | 128,000 | no | text  
`hf:zai-org/GLM-4.6` | 198,000 | 128,000 | no | text  
`hf:zai-org/GLM-5` | 256,000 | 128,000 | yes | text + image  
`hf:deepseek-ai/DeepSeek-V3` | 128,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256,000 | 8,192 | yes | text  
  
Model izin listesi

Bir model izin listesi (`agents.defaults.models`) etkinleştirirseniz kullanmayı planladığınız her Synthetic modelini ekleyin. İzin listesinde olmayan modeller ajandan gizlenir.

Base URL geçersiz kılması

Synthetic API uç noktasını değiştirirse base URL'yi yapılandırmanızda geçersiz kılın:

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

OpenClaw'ın `/v1` otomatik eklediğini unutmayın.

## İlgili

[**Model seçimi** Sağlayıcı kuralları, model ref'leri ve failover davranışı. ](</tr/concepts/model-providers>) [**Yapılandırma başvurusu** Sağlayıcı ayarları dahil tam yapılandırma şeması. ](</tr/gateway/configuration-reference>) [**Synthetic** Synthetic panosu ve API belgeleri. ](<https://synthetic.new>)

Was this useful?YesNo