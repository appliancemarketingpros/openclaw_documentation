---
title: Moonshot AI
source_url: https://docs.openclaw.ai/ko/providers/moonshot
scraped_at: 2026-05-25
---

Moonshot은 OpenAI 호환 엔드포인트로 Kimi API를 제공합니다. 공급자를 구성하고 기본 모델을 `moonshot/kimi-k2.6`으로 설정하거나, `kimi/kimi-for-coding`으로 Kimi Coding을 사용하세요.

## 내장 모델 카탈로그

모델 참조 | 이름 | 추론 | 입력 | 컨텍스트 | 최대 출력  
---|---|---|---|---|---  
`moonshot/kimi-k2.6` | Kimi K2.6 | 아니요 | 텍스트, 이미지 | 262,144 | 262,144  
`moonshot/kimi-k2.5` | Kimi K2.5 | 아니요 | 텍스트, 이미지 | 262,144 | 262,144  
`moonshot/kimi-k2-thinking` | Kimi K2 Thinking | 예 | 텍스트 | 262,144 | 262,144  
`moonshot/kimi-k2-thinking-turbo` | Kimi K2 Thinking Turbo | 예 | 텍스트 | 262,144 | 262,144  
`moonshot/kimi-k2-turbo` | Kimi K2 Turbo | 아니요 | 텍스트 | 256,000 | 16,384  
  
현재 Moonshot 호스팅 K2 모델에 대한 번들 비용 추정치는 Moonshot이 게시한 종량제 요금을 사용합니다. Kimi K2.6은 캐시 적중 $0.16/MTok, 입력 $0.95/MTok, 출력 $4.00/MTok이고, Kimi K2.5는 캐시 적중 $0.10/MTok, 입력 $0.60/MTok, 출력 $3.00/MTok입니다. 다른 레거시 카탈로그 항목은 구성에서 재정의하지 않는 한 비용이 0인 자리 표시자를 유지합니다.

## 시작하기

공급자를 선택하고 설정 단계를 따르세요.

### Moonshot API

**가장 적합한 용도:** Moonshot Open Platform을 통한 Kimi K2 모델.

* ### Choose your endpoint region

인증 선택 | 엔드포인트 | 지역  
---|---|---  
`moonshot-api-key` | `https://api.moonshot.ai/v1` | 국제  
`moonshot-api-key-cn` | `https://api.moonshot.cn/v1` | 중국  
* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key
[/code]

또는 중국 엔드포인트의 경우:

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },    },  },}
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider moonshot
[/code]

* ### Run a live smoke test

일반 세션을 건드리지 않고 모델 접근과 비용 추적을 확인하려면 격리된 상태 디렉터리를 사용하세요.

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=/tmp/openclaw-kimi/openclaw.json \OPENCLAW_STATE_DIR=/tmp/openclaw-kimi \openclaw agent --local \  --session-id live-kimi-cost \  --message 'Reply exactly: KIMI_LIVE_OK' \  --thinking off \  --json
[/code]

JSON 응답은 `provider: "moonshot"` 및 `model: "kimi-k2.6"`을 보고해야 합니다. Moonshot이 사용량 메타데이터를 반환하면 어시스턴트 트랜스크립트 항목은 정규화된 토큰 사용량과 추정 비용을 `usage.cost` 아래에 저장합니다.

### 구성 예시

json5Copy code
[code]
    {  env: { MOONSHOT_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },      models: {        // moonshot-kimi-k2-aliases:start        "moonshot/kimi-k2.6": { alias: "Kimi K2.6" },        "moonshot/kimi-k2.5": { alias: "Kimi K2.5" },        "moonshot/kimi-k2-thinking": { alias: "Kimi K2 Thinking" },        "moonshot/kimi-k2-thinking-turbo": { alias: "Kimi K2 Thinking Turbo" },        "moonshot/kimi-k2-turbo": { alias: "Kimi K2 Turbo" },        // moonshot-kimi-k2-aliases:end      },    },  },  models: {    mode: "merge",    providers: {      moonshot: {        baseUrl: "https://api.moonshot.ai/v1",        apiKey: "${MOONSHOT_API_KEY}",        api: "openai-completions",        models: [          // moonshot-kimi-k2-models:start          {            id: "kimi-k2.6",            name: "Kimi K2.6",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.95, output: 4, cacheRead: 0.16, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2.5",            name: "Kimi K2.5",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.6, output: 3, cacheRead: 0.1, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking",            name: "Kimi K2 Thinking",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking-turbo",            name: "Kimi K2 Thinking Turbo",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-turbo",            name: "Kimi K2 Turbo",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 256000,            maxTokens: 16384,          },          // moonshot-kimi-k2-models:end        ],      },    },  },}
[/code]

### Kimi Coding

**가장 적합한 용도:** Kimi Coding 엔드포인트를 통한 코드 중심 작업.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kimi-code-api-key
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider kimi
[/code]

### 구성 예시

json5Copy code
[code]
    {  env: { KIMI_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },      models: {        "kimi/kimi-for-coding": { alias: "Kimi" },      },    },  },}
[/code]

## Kimi 웹 검색

OpenClaw는 Moonshot 웹 검색을 기반으로 하는 `web_search` 제공자로 **Kimi** 도 제공합니다.

* ### 대화형 웹 검색 설정 실행

bashCopy code
[code]
    openclaw configure --section web
[/code]

웹 검색 섹션에서 **Kimi** 를 선택하여 `plugins.entries.moonshot.config.webSearch.*`를 저장합니다.

* ### 웹 검색 리전 및 모델 구성

대화형 설정에서는 다음을 묻습니다.

설정 | 옵션  
---|---  
API 리전 | `https://api.moonshot.ai/v1`(국제) 또는 `https://api.moonshot.cn/v1`(중국)  
웹 검색 모델 | 기본값은 `kimi-k2.6`  
  
구성은 `plugins.entries.moonshot.config.webSearch` 아래에 있습니다.

json5Copy code
[code]
    {  plugins: {    entries: {      moonshot: {        config: {          webSearch: {            apiKey: "sk-...", // or use KIMI_API_KEY / MOONSHOT_API_KEY            baseUrl: "https://api.moonshot.ai/v1",            model: "kimi-k2.6",          },        },      },    },  },  tools: {    web: {      search: {        provider: "kimi",      },    },  },}
[/code]

## 고급 구성

네이티브 사고 모드

Moonshot Kimi는 이진 네이티브 사고를 지원합니다.

  * `thinking: { type: "enabled" }`
  * `thinking: { type: "disabled" }`


`agents.defaults.models.<provider/model>.params`를 통해 모델별로 구성합니다.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "disabled" },          },        },      },    },  },}
[/code]

OpenClaw는 Moonshot에 대한 런타임 `/think` 수준도 매핑합니다.

`/think` 수준 | Moonshot 동작  
---|---  
`/think off` | `thinking.type=disabled`  
off가 아닌 모든 수준 | `thinking.type=enabled`  
  
Kimi K2.6은 `reasoning_content`의 여러 턴 보존을 제어하는 선택적 `thinking.keep` 필드도 허용합니다. 턴 간 전체 추론을 유지하려면 `"all"`로 설정하고, 서버 기본 전략을 사용하려면 생략하거나 `null`로 둡니다. OpenClaw는 `moonshot/kimi-k2.6`에 대해서만 `thinking.keep`을 전달하고 다른 모델에서는 제거합니다.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "enabled", keep: "all" },          },        },      },    },  },}
[/code]

도구 호출 ID 정리

Moonshot Kimi는 `functions.<name>:<index>` 형식의 tool_call ID를 제공합니다. OpenClaw는 여러 턴 도구 호출이 계속 작동하도록 이를 변경하지 않고 보존합니다.

사용자 지정 OpenAI 호환 제공자에서 엄격한 정리를 강제하려면 `sanitizeToolCallIds: true`를 설정합니다.

json5Copy code
[code]
    {  models: {    providers: {      "my-kimi-proxy": {        api: "openai-completions",        sanitizeToolCallIds: true,      },    },  },}
[/code]

스트리밍 사용량 호환성

네이티브 Moonshot 엔드포인트(`https://api.moonshot.ai/v1` 및 `https://api.moonshot.cn/v1`)는 공유 `openai-completions` 전송에서 스트리밍 사용량 호환성을 알립니다. OpenClaw는 이를 엔드포인트 기능을 기준으로 판단하므로, 동일한 네이티브 Moonshot 호스트를 대상으로 하는 호환 사용자 지정 제공자 ID도 동일한 스트리밍 사용량 동작을 상속합니다.

번들된 K2.6 가격 책정을 사용하면 입력, 출력 및 캐시 읽기 토큰을 포함하는 스트리밍 사용량도 `/status`, `/usage full`, `/usage cost` 및 트랜스크립트 기반 세션 회계를 위한 로컬 예상 USD 비용으로 변환됩니다.

엔드포인트 및 모델 참조 레퍼런스 Provider | 모델 참조 접두사 | 엔드포인트 | 인증 환경 변수  
---|---|---|---  
Moonshot | `moonshot/` | `https://api.moonshot.ai/v1` | `MOONSHOT_API_KEY`  
Moonshot CN | `moonshot/` | `https://api.moonshot.cn/v1` | `MOONSHOT_API_KEY`  
Kimi Coding | `kimi/` | Kimi Coding 엔드포인트 | `KIMI_API_KEY`  
웹 검색 | N/A | Moonshot API 리전과 동일 | `KIMI_API_KEY` 또는 `MOONSHOT_API_KEY`  
  
  * Kimi 웹 검색은 `KIMI_API_KEY` 또는 `MOONSHOT_API_KEY`를 사용하며, 기본값은 모델 `kimi-k2.6`과 함께 `https://api.moonshot.ai/v1`입니다.
  * 필요한 경우 `models.providers`에서 가격 및 컨텍스트 메타데이터를 재정의하세요.
  * Moonshot이 모델에 대해 다른 컨텍스트 제한을 게시하는 경우 그에 맞게 `contextWindow`를 조정하세요.


## 관련 항목

[**모델 선택** 제공자, 모델 참조, 장애 조치 동작 선택. ](</ko/concepts/model-providers>) [**웹 검색** Kimi를 포함한 웹 검색 제공자 구성. ](</ko/tools/web>) [**구성 레퍼런스** 제공자, 모델, Plugin에 대한 전체 구성 스키마. ](</ko/gateway/configuration-reference>) [**Moonshot Open Platform** Moonshot API 키 관리 및 문서. ](<https://platform.moonshot.ai>)

Was this useful?YesNo