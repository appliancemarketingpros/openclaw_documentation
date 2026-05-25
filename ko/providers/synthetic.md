---
title: Synthetic
source_url: https://docs.openclaw.ai/ko/providers/synthetic
scraped_at: 2026-05-25
---

[Synthetic](<https://synthetic.new>)는 Anthropic 호환 엔드포인트를 제공합니다. OpenClaw는 이를 `synthetic` provider로 등록하고 Anthropic Messages API를 사용합니다.

Property | Value  
---|---  
Provider | `synthetic`  
Auth | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
Base URL | `https://api.synthetic.new/anthropic`  
  
## 시작하기

* ### API 키 받기

Synthetic 계정에서 `SYNTHETIC_API_KEY`를 발급받거나, 온보딩 마법사가 이를 묻도록 하세요.

* ### 온보딩 실행

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### 기본 모델 확인

온보딩 후 기본 모델은 다음으로 설정됩니다.

CodeCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## config 예시

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## 내장 카탈로그

모든 Synthetic 모델은 비용이 `0`입니다(input/output/cache).

Model ID | Context window | Max tokens | Reasoning | Input  
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
  
모델 allowlist

모델 allowlist(`agents.defaults.models`)를 활성화하면, 사용할 계획인 모든 Synthetic 모델을 추가하세요. allowlist에 없는 모델은 에이전트에서 숨겨집니다.

Base URL 재정의

Synthetic가 API 엔드포인트를 변경하면 config에서 base URL을 재정의하세요.

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

OpenClaw가 `/v1`을 자동으로 붙인다는 점을 기억하세요.

## 관련 항목

[**모델 선택** Provider 규칙, 모델 ref, failover 동작. ](</ko/concepts/model-providers>) [**구성 참조** provider 설정을 포함한 전체 config 스키마. ](</ko/gateway/configuration-reference>) [**Synthetic** Synthetic 대시보드 및 API 문서. ](<https://synthetic.new>)

Was this useful?YesNo