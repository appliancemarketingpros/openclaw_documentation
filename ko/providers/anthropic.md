---
title: Anthropic
source_url: https://docs.openclaw.ai/ko/providers/anthropic
scraped_at: 2026-05-25
---

Anthropic은 **Claude** 모델 제품군을 만듭니다. OpenClaw는 두 가지 인증 경로를 지원합니다.

  * **API 키** — 사용량 기반 과금으로 Anthropic API에 직접 액세스(`anthropic/*` 모델)
  * **Claude CLI** — 같은 호스트의 기존 Claude CLI 로그인을 재사용


## 시작하기

### API 키

**권장 대상:** 표준 API 액세스 및 사용량 기반 과금.

* ### API 키 받기

[Anthropic Console](<https://console.anthropic.com/>)에서 API 키를 만듭니다.

* ### 온보딩 실행

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

또는 키를 직접 전달합니다.

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### 모델 사용 가능 여부 확인

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### 구성 예시

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "sk-ant-..." },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### Claude CLI

**권장 대상:** 별도의 API 키 없이 기존 Claude CLI 로그인을 재사용.

* ### Claude CLI가 설치되어 있고 로그인되어 있는지 확인

다음으로 확인합니다.

bashCopy code
[code]
    claude --version
[/code]

* ### 온보딩 실행

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

OpenClaw는 기존 Claude CLI 자격 증명을 감지하고 재사용합니다.

* ### 모델 사용 가능 여부 확인

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### 구성 예시

표준 Anthropic 모델 참조와 CLI 런타임 오버라이드를 함께 사용하는 것을 권장합니다.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-7" },      models: {        "anthropic/claude-opus-4-7": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

기존 `claude-cli/claude-opus-4-7` 모델 참조는 호환성을 위해 계속 작동하지만, 새 구성에서는 provider/model 선택을 `anthropic/*`로 유지하고 실행 백엔드를 provider/model 런타임 정책에 넣어야 합니다.

## 사고 기본값(Claude 4.6)

Claude 4.6 모델은 명시적인 사고 수준이 설정되지 않은 경우 OpenClaw에서 기본적으로 `adaptive` 사고를 사용합니다.

메시지별로 `/think:<level>`을 사용하거나 모델 파라미터에서 오버라이드합니다.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { thinking: "adaptive" },        },      },    },  },}
[/code]

## 프롬프트 캐싱

OpenClaw는 API 키 인증에 대해 Anthropic의 프롬프트 캐싱 기능을 지원합니다.

값 | 캐시 기간 | 설명  
---|---|---  
`"short"` (기본값) | 5분 | API 키 인증에 자동 적용  
`"long"` | 1시간 | 확장 캐시  
`"none"` | 캐싱 없음 | 프롬프트 캐싱 비활성화  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

에이전트별 캐시 오버라이드

모델 수준 파라미터를 기준값으로 사용한 다음, `agents.list[].params`를 통해 특정 에이전트를 오버라이드합니다.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

구성 병합 순서:

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params`(일치하는 `id`, 키별 오버라이드)


이렇게 하면 같은 모델을 사용하는 한 에이전트는 장기 캐시를 유지하면서 다른 에이전트는 급증형/낮은 재사용 트래픽에 대해 캐싱을 비활성화할 수 있습니다.

Bedrock Claude 참고 사항

  * Bedrock의 Anthropic Claude 모델(`amazon-bedrock/*anthropic.claude*`)은 구성된 경우 `cacheRetention` 패스스루를 허용합니다.
  * Anthropic이 아닌 Bedrock 모델은 런타임에 `cacheRetention: "none"`으로 강제됩니다.
  * 명시적인 값이 설정되지 않은 경우 API 키 스마트 기본값은 Claude-on-Bedrock 참조에도 `cacheRetention: "short"`를 시드합니다.


## 고급 구성

빠른 모드

OpenClaw의 공유 `/fast` 토글은 직접 Anthropic 트래픽(API 키 및 `api.anthropic.com`에 대한 OAuth)을 지원합니다.

명령 | 매핑 대상  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

미디어 이해(이미지 및 PDF)

번들 Anthropic Plugin은 이미지 및 PDF 이해를 등록합니다. OpenClaw는 구성된 Anthropic 인증에서 미디어 기능을 자동으로 해석하므로 추가 구성이 필요하지 않습니다.

속성 | 값  
---|---  
기본 모델 | `claude-opus-4-7`  
지원 입력 | 이미지, PDF 문서  
  
이미지 또는 PDF가 대화에 첨부되면 OpenClaw는 이를 Anthropic 미디어 이해 provider를 통해 자동으로 라우팅합니다.

1M 컨텍스트 창(베타)

Anthropic의 1M 컨텍스트 창은 베타 게이트가 적용되어 있습니다. 모델별로 활성화합니다.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { context1m: true },        },      },    },  },}
[/code]

OpenClaw는 요청에서 이를 `anthropic-beta: context-1m-2025-08-07`로 매핑합니다.

`params.context1m: true`는 적격 Opus 및 Sonnet 모델의 Claude CLI 백엔드 (`claude-cli/*`)에도 적용되어, 해당 CLI 세션의 런타임 컨텍스트 창을 직접 API 동작과 일치하도록 확장합니다.

Claude Opus 4.7 1M 컨텍스트

`anthropic/claude-opus-4.7` 및 해당 `claude-cli` 변형은 기본적으로 1M 컨텍스트 창을 가지므로 `params.context1m: true`가 필요하지 않습니다.

## 문제 해결

401 오류 / 토큰이 갑자기 유효하지 않음

Anthropic 토큰 인증은 만료될 수 있으며 취소될 수 있습니다. 새 설정의 경우 Anthropic API 키를 대신 사용하세요.

provider "anthropic"에 대한 API 키를 찾을 수 없음

Anthropic 인증은 **에이전트별** 입니다. 새 에이전트는 메인 에이전트의 키를 상속하지 않습니다. 해당 에이전트에 대해 온보딩을 다시 실행하거나 Gateway 호스트에 API 키를 구성한 다음 `openclaw models status`로 확인하세요.

profile "anthropic:default"에 대한 자격 증명을 찾을 수 없음

`openclaw models status`를 실행하여 어떤 인증 프로필이 활성 상태인지 확인하세요. 온보딩을 다시 실행하거나 해당 프로필 경로에 대한 API 키를 구성하세요.

사용 가능한 인증 프로필 없음(모두 쿨다운 중)

`openclaw models status --json`에서 `auth.unusableProfiles`를 확인하세요. Anthropic 속도 제한 쿨다운은 모델 범위일 수 있으므로, 같은 Anthropic 계열의 다른 모델은 여전히 사용할 수 있을 수 있습니다. 다른 Anthropic 프로필을 추가하거나 쿨다운이 끝날 때까지 기다리세요.

## 관련 항목

[**모델 선택** provider, 모델 참조, 장애 조치 동작 선택. ](</ko/concepts/model-providers>) [**CLI 백엔드** Claude CLI 백엔드 설정 및 런타임 세부 정보. ](</ko/gateway/cli-backends>) [**프롬프트 캐싱** provider 전반에서 프롬프트 캐싱이 작동하는 방식. ](</ko/reference/prompt-caching>) [**OAuth 및 인증** 인증 세부 정보 및 자격 증명 재사용 규칙. ](</ko/gateway/authentication>)

Was this useful?YesNo