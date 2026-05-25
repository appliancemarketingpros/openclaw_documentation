---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/ko/providers/kilocode
scraped_at: 2026-05-25
---

Kilo Gateway는 단일 엔드포인트와 API 키 뒤에서 여러 모델로 요청을 라우팅하는 **통합 API** 를 제공합니다. OpenAI 호환이므로 대부분의 OpenAI SDK는 기본 URL만 바꾸면 작동합니다.

속성 | 값  
---|---  
제공자 | `kilocode`  
인증 | `KILOCODE_API_KEY`  
API | OpenAI 호환  
기본 URL | `https://api.kilo.ai/api/gateway/`  
  
## 시작하기

* ### 계정 만들기

[app.kilo.ai](<https://app.kilo.ai>)로 이동해 로그인하거나 계정을 만든 다음, API Keys로 이동해 새 키를 생성합니다.

* ### 온보딩 실행

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

또는 환경 변수를 직접 설정합니다.

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### 모델 사용 가능 여부 확인

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## 기본 모델

기본 모델은 Kilo Gateway가 관리하는 제공자 소유 스마트 라우팅 모델인 `kilocode/kilo/auto`입니다.

## 기본 제공 카탈로그

OpenClaw는 시작 시 Kilo Gateway에서 사용 가능한 모델을 동적으로 검색합니다. 계정에서 사용할 수 있는 전체 모델 목록을 보려면 `/models kilocode`를 사용하세요.

Gateway에서 사용할 수 있는 모든 모델은 `kilocode/` 접두사로 사용할 수 있습니다.

모델 참조 | 참고  
---|---  
`kilocode/kilo/auto` | 기본값 — 스마트 라우팅  
`kilocode/anthropic/claude-sonnet-4` | Kilo를 통한 Anthropic  
`kilocode/openai/gpt-5.5` | Kilo를 통한 OpenAI  
`kilocode/google/gemini-3.1-pro-preview` | Kilo를 통한 Google  
...그리고 더 많은 모델 | 전체 목록은 `/models kilocode` 사용  
  
## 구성 예시

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

전송 및 호환성

Kilo Gateway는 소스에서 OpenRouter 호환으로 문서화되어 있으므로, 네이티브 OpenAI 요청 형태 지정이 아니라 프록시 스타일의 OpenAI 호환 경로를 유지합니다.

  * Gemini 기반 Kilo 참조는 프록시-Gemini 경로에 유지되므로, OpenClaw는 네이티브 Gemini 재생 검증이나 부트스트랩 재작성은 활성화하지 않고 그곳에서 Gemini 사고 서명 정리를 유지합니다.
  * Kilo Gateway는 내부적으로 API 키와 함께 Bearer 토큰을 사용합니다.

스트림 래퍼 및 추론

Kilo의 공유 스트림 래퍼는 제공자 앱 헤더를 추가하고 지원되는 구체적 모델 참조에 대해 프록시 추론 페이로드를 정규화합니다.

문제 해결

  * 시작 시 모델 검색이 실패하면 OpenClaw는 `kilocode/kilo/auto`가 포함된 번들 정적 카탈로그로 대체합니다.
  * API 키가 유효하고 Kilo 계정에서 원하는 모델이 활성화되어 있는지 확인하세요.
  * Gateway가 데몬으로 실행되는 경우 해당 프로세스에서 `KILOCODE_API_KEY`를 사용할 수 있는지 확인하세요. 예를 들어 `~/.openclaw/.env` 또는 `env.shellEnv`를 사용할 수 있습니다.


## 관련 항목

[**모델 선택** 제공자, 모델 참조, 장애 조치 동작 선택. ](</ko/concepts/model-providers>) [**구성 참조** 전체 OpenClaw 구성 참조. ](</ko/gateway/configuration-reference>) [**Kilo Gateway** Kilo Gateway 대시보드, API 키, 계정 관리. ](<https://app.kilo.ai>)

Was this useful?YesNo