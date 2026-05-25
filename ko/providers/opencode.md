---
title: OpenCode
source_url: https://docs.openclaw.ai/ko/providers/opencode
scraped_at: 2026-05-25
---

OpenCode는 OpenClaw에서 두 가지 호스팅 카탈로그를 제공합니다:

카탈로그 | 접두사 | 런타임 provider  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
두 카탈로그 모두 동일한 OpenCode API 키를 사용합니다. OpenClaw는 업스트림 모델별 라우팅이 올바르게 유지되도록 런타임 provider id를 분리해 두지만, 온보딩과 문서에서는 이를 하나의 OpenCode setup으로 취급합니다.

## 시작하기

### Zen 카탈로그

**적합한 경우:** 엄선된 OpenCode 멀티 모델 프록시(Claude, GPT, Gemini).

* ### 온보딩 실행

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

또는 키를 직접 전달합니다:

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### Zen 모델을 기본값으로 설정

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### 모델 사용 가능 여부 확인

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Go 카탈로그

**적합한 경우:** OpenCode가 호스팅하는 Kimi, GLM, MiniMax 라인업.

* ### 온보딩 실행

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

또는 키를 직접 전달합니다:

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Go 모델을 기본값으로 설정

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### 모델 사용 가능 여부 확인

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## config 예시

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## 내장 카탈로그

### Zen

속성 | 값  
---|---  
런타임 provider | `opencode`  
예시 모델 | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3-pro`  
  
### Go

속성 | 값  
---|---  
런타임 provider | `opencode-go`  
예시 모델 | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## 고급 구성

API 키 별칭

`OPENCODE_ZEN_API_KEY`도 `OPENCODE_API_KEY`의 별칭으로 지원됩니다.

공유 자격 증명

setup 중에 하나의 OpenCode 키를 입력하면 두 런타임 provider 모두에 대한 자격 증명이 저장됩니다. 각 카탈로그를 따로 온보딩할 필요는 없습니다.

청구 및 대시보드

OpenCode에 로그인하고 청구 정보를 추가한 뒤 API 키를 복사합니다. 청구 및 카탈로그 가용성은 OpenCode 대시보드에서 관리됩니다.

Gemini 재생 동작

Gemini 기반 OpenCode ref는 프록시-Gemini 경로에 유지되므로, OpenClaw는 네이티브 Gemini 재생 검증이나 bootstrap 재작성을 활성화하지 않고도 그 경로에서 Gemini thought-signature 정리를 유지합니다.

비-Gemini 재생 동작

비-Gemini OpenCode ref는 최소 OpenAI 호환 재생 정책을 유지합니다.

## 관련

[**모델 선택** provider, 모델 ref, failover 동작 선택하기. ](</ko/concepts/model-providers>) [**구성 참조** 에이전트, 모델, provider에 대한 전체 config 참조. ](</ko/gateway/configuration-reference>)

Was this useful?YesNo