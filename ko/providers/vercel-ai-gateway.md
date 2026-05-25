---
title: Vercel AI Gateway
source_url: https://docs.openclaw.ai/ko/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

[Vercel AI Gateway](<https://vercel.com/ai-gateway>)는 단일 엔드포인트를 통해 수백 개의 모델에 접근할 수 있는 통합 API를 제공합니다.

속성 | 값  
---|---  
제공자 | `vercel-ai-gateway`  
인증 | `AI_GATEWAY_API_KEY`  
API | Anthropic Messages 호환  
모델 카탈로그 | `/v1/models`를 통해 자동 발견됨  
  
## 시작하기

* ### API 키 설정

온보딩을 실행하고 AI Gateway 인증 옵션을 선택합니다.

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### 기본 모델 설정

OpenClaw 구성에 모델을 추가합니다.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### 모델 사용 가능 여부 확인

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## 비대화형 예시

스크립트 또는 CI 설정의 경우 명령줄에서 모든 값을 전달합니다.

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## 모델 ID 축약형

OpenClaw는 Vercel Claude 축약형 모델 참조를 허용하며 런타임에 정규화합니다.

축약 입력 | 정규화된 모델 참조  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## 고급 구성

데몬 프로세스용 환경 변수

OpenClaw Gateway가 데몬(launchd/systemd)으로 실행되는 경우 해당 프로세스에서 `AI_GATEWAY_API_KEY`를 사용할 수 있는지 확인합니다.

제공자 라우팅

Vercel AI Gateway는 모델 참조 접두사를 기준으로 요청을 업스트림 제공자로 라우팅합니다. 예를 들어 `vercel-ai-gateway/anthropic/claude-opus-4.6`은 Anthropic을 통해 라우팅되고, `vercel-ai-gateway/openai/gpt-5.5`는 OpenAI를 통해, `vercel-ai-gateway/moonshotai/kimi-k2.6`은 MoonshotAI를 통해 라우팅됩니다. 단일 `AI_GATEWAY_API_KEY`가 모든 업스트림 제공자의 인증을 처리합니다.

Thinking 수준

OpenClaw가 업스트림 제공자 계약을 알고 있는 경우 `/think` 옵션은 신뢰할 수 있는 업스트림 모델 접두사를 따릅니다. `vercel-ai-gateway/anthropic/...`은 Claude 4.6 모델의 적응형 기본값을 포함한 Claude thinking 프로필을 사용합니다. `vercel-ai-gateway/openai/gpt-5.4`, `gpt-5.5`, Codex 스타일 참조는 직접 OpenAI/OpenAI Codex 제공자와 마찬가지로 `/think xhigh`를 노출합니다. 다른 네임스페이스 참조는 해당 카탈로그 메타데이터가 더 많은 항목을 선언하지 않는 한 일반 reasoning 수준을 유지합니다.

## 관련 항목

[**모델 선택** 제공자, 모델 참조, 장애 조치 동작 선택. ](</ko/concepts/model-providers>) [**문제 해결** 일반적인 문제 해결 및 FAQ. ](</ko/help/troubleshooting>)

Was this useful?YesNo