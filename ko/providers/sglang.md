---
title: SGLang
source_url: https://docs.openclaw.ai/ko/providers/sglang
scraped_at: 2026-05-25
---

SGLang은 OpenAI 호환 HTTP API를 통해 오픈 웨이트 모델을 제공합니다. OpenClaw는 사용 가능한 모델 자동 발견 기능과 함께 `openai-completions` provider family를 사용해 SGLang에 연결합니다.

속성 | 값  
---|---  
Provider id | `sglang`  
Plugin | 번들, `enabledByDefault: true`  
인증 env var | `SGLANG_API_KEY` (서버에 인증이 없으면 비어 있지 않은 아무 값)  
온보딩 플래그 | `--auth-choice sglang`  
API | OpenAI 호환 (`openai-completions`)  
기본 base URL | `http://127.0.0.1:30000/v1`  
기본 모델 placeholder | `sglang/Qwen/Qwen3-8B`  
스트리밍 사용량 | 예 (`supportsStreamingUsage: true`)  
가격 책정 | external-free로 표시됨 (`modelPricing.external: false`)  
  
또한 `SGLANG_API_KEY`로 옵트인하면 OpenClaw가 SGLang에서 사용 가능한 모델을 **자동 발견** 합니다. 사용자 지정 SGLang base URL도 구성하는 경우 발견을 동적으로 유지하려면 `agents.defaults.models`에서 `sglang/*`를 사용하세요. 아래 모델 발견(암시적 provider)을 참조하세요.

## 시작하기

* ### SGLang 시작

OpenAI 호환 서버로 SGLang을 실행하세요. base URL은 `/v1` endpoint를 노출해야 합니다(예: `/v1/models`, `/v1/chat/completions`). SGLang은 일반적으로 다음에서 실행됩니다.

  * `http://127.0.0.1:30000/v1`


* ### API 키 설정

서버에 인증이 구성되어 있지 않으면 아무 값이나 사용할 수 있습니다.

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

* ### 온보딩을 실행하거나 모델을 직접 설정

bashCopy code
[code]
    openclaw onboard
[/code]

또는 모델을 수동으로 구성하세요.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "sglang/your-model-id" },    },  },}
[/code]

## 모델 발견(암시적 provider)

`SGLANG_API_KEY`가 설정되어 있거나 auth profile이 존재하고, `models.providers.sglang`을 정의하지 **않은** 경우 OpenClaw는 다음을 쿼리합니다.

  * `GET http://127.0.0.1:30000/v1/models`


그리고 반환된 ID를 모델 항목으로 변환합니다.

## 명시적 구성(수동 모델)

다음 경우 명시적 config를 사용하세요.

  * SGLang이 다른 호스트/포트에서 실행됩니다.
  * `contextWindow`/`maxTokens` 값을 고정하려고 합니다.
  * 서버에 실제 API 키가 필요하거나, 헤더를 제어하려고 합니다.

json5Copy code
[code]
    {  models: {    providers: {      sglang: {        baseUrl: "http://127.0.0.1:30000/v1",        apiKey: "${SGLANG_API_KEY}",        api: "openai-completions",        models: [          {            id: "your-model-id",            name: "Local SGLang Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## 고급 구성

프록시 스타일 동작

SGLang은 네이티브 OpenAI endpoint가 아니라 프록시 스타일의 OpenAI 호환 `/v1` backend로 취급됩니다.

동작 | SGLang  
---|---  
OpenAI 전용 요청 shaping | 적용되지 않음  
`service_tier`, Responses `store`, prompt-cache hints | 전송되지 않음  
Reasoning 호환 payload shaping | 적용되지 않음  
숨겨진 attribution headers (`originator`, `version`, `User-Agent`) | 사용자 지정 SGLang base URL에는 삽입되지 않음  
문제 해결

**서버에 연결할 수 없음**

서버가 실행 중이고 응답하는지 확인하세요.

bashCopy code
[code]
    curl http://127.0.0.1:30000/v1/models
[/code]

**인증 오류**

요청이 인증 오류로 실패하면 서버 구성과 일치하는 실제 `SGLANG_API_KEY`를 설정하거나, `models.providers.sglang` 아래에서 provider를 명시적으로 구성하세요.

## 관련 항목

[**모델 선택** provider, 모델 참조, failover 동작 선택. ](</ko/concepts/model-providers>) [**구성 참조** provider 항목을 포함한 전체 config schema. ](</ko/gateway/configuration-reference>)

Was this useful?YesNo