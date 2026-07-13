---
title: 메타
source_url: https://docs.openclaw.ai/ko/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

**Meta API** 는 `muse-spark-1.1` 추론 모델에 OpenAI 호환 **Responses API**(`POST /v1/responses`)를 사용합니다. 이 제공자는 번들 OpenClaw Plugin으로 제공됩니다.

속성 | 값  
---|---  
제공자 ID | `meta`  
Plugin | 번들 제공자  
인증 환경 변수 | `MODEL_API_KEY`  
온보딩 플래그 | `--auth-choice meta-api-key`  
직접 CLI 플래그 | `--meta-api-key <key>`  
API | Responses API (`openai-responses`)  
기본 URL | `https://api.meta.ai/v1`  
기본 모델 | `meta/muse-spark-1.1`  
기본 추론 수준 | `high` (`reasoning.effort`)  
  
## 시작하기

* ### API 키 설정

OnboardingCopy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

Env onlyCopy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### 모델 사용 가능 여부 확인

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

정적 `muse-spark-1.1` 카탈로그 항목을 나열합니다. `MODEL_API_KEY`를 확인할 수 없으면 `openclaw models status --json`이 `auth.unusableProfiles` 아래에 누락된 자격 증명을 보고합니다.

## 비대화형 설정

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## 기본 제공 카탈로그

모델 참조 | 이름 | 추론 | 컨텍스트 창 | 최대 출력  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | 예 | 1,048,576 | 131,072  
  
기능:

  * 텍스트 및 이미지 입력
  * 도구 호출 및 스트리밍
  * 추론 수준: `minimal`, `low`, `medium`, `high`, `xhigh`(기본값: `high`)
  * 상태 비저장 암호화 추론 재생(`store: false`, `include: ["reasoning.encrypted_content"]`)


## 수동 구성

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## 스모크 테스트

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

라이브 테스트는 `POST /v1/responses`에 대해 `muse-spark-1.1`을 사용합니다.

## 관련 항목

[**모델 제공자** 제공자, 모델 참조 및 장애 조치 동작을 선택합니다. ](</ko/concepts/model-providers>) [**사고 모드** muse-spark-1.1의 추론 수준입니다. ](</ko/tools/thinking>) [**구성 참조** 에이전트 기본값 및 모델 구성입니다. ](</ko/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue