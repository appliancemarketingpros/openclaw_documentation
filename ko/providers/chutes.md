---
title: Chutes
source_url: https://docs.openclaw.ai/ko/providers/chutes
scraped_at: 2026-05-25
---

[Chutes](<https://chutes.ai>)는 OpenAI 호환 API를 통해 오픈 소스 모델 카탈로그를 제공합니다. OpenClaw는 번들된 `chutes` 제공자에 대해 브라우저 OAuth와 직접 API 키 인증을 모두 지원합니다.

속성 | 값  
---|---  
제공자 | `chutes`  
API | OpenAI 호환  
기본 URL | `https://llm.chutes.ai/v1`  
인증 | OAuth 또는 API 키(아래 참조)  
  
## 시작하기

### OAuth

* ### OAuth 온보딩 흐름 실행

bashCopy code
[code]
    openclaw onboard --auth-choice chutes
[/code]

OpenClaw는 브라우저 흐름을 로컬에서 실행하거나, 원격/헤드리스 호스트에서는 URL + 리디렉션 붙여넣기 흐름을 표시합니다. OAuth 토큰은 OpenClaw 인증 프로필을 통해 자동으로 갱신됩니다.

* ### 기본 모델 확인

온보딩 후 기본 모델은 `chutes/zai-org/GLM-4.7-TEE`로 설정되고 번들된 Chutes 카탈로그가 등록됩니다.

### API 키

* ### API 키 받기

[chutes.ai/settings/api-keys](<https://chutes.ai/settings/api-keys>)에서 키를 생성합니다.

* ### API 키 온보딩 흐름 실행

bashCopy code
[code]
    openclaw onboard --auth-choice chutes-api-key
[/code]

* ### 기본 모델 확인

온보딩 후 기본 모델은 `chutes/zai-org/GLM-4.7-TEE`로 설정되고 번들된 Chutes 카탈로그가 등록됩니다.

## 검색 동작

Chutes 인증을 사용할 수 있으면 OpenClaw는 해당 자격 증명으로 Chutes 카탈로그를 조회하고 검색된 모델을 사용합니다. 검색이 실패하면 OpenClaw는 번들된 정적 카탈로그로 대체하여 온보딩과 시작이 계속 작동하도록 합니다.

## 기본 별칭

OpenClaw는 번들된 Chutes 카탈로그에 대해 세 가지 편의 별칭을 등록합니다.

별칭 | 대상 모델  
---|---  
`chutes-fast` | `chutes/zai-org/GLM-4.7-FP8`  
`chutes-pro` | `chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes-vision` | `chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
  
## 내장 시작 카탈로그

번들된 대체 카탈로그에는 현재 Chutes 참조가 포함됩니다.

모델 참조  
---  
`chutes/zai-org/GLM-4.7-TEE`  
`chutes/zai-org/GLM-5-TEE`  
`chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes/deepseek-ai/DeepSeek-R1-0528-TEE`  
`chutes/moonshotai/Kimi-K2.5-TEE`  
`chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
`chutes/Qwen/Qwen3-Coder-Next-TEE`  
`chutes/openai/gpt-oss-120b-TEE`  
  
## 설정 예시

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "chutes/zai-org/GLM-4.7-TEE" },      models: {        "chutes/zai-org/GLM-4.7-TEE": { alias: "Chutes GLM 4.7" },        "chutes/deepseek-ai/DeepSeek-V3.2-TEE": { alias: "Chutes DeepSeek V3.2" },      },    },  },}
[/code]

OAuth 재정의

선택적 환경 변수로 OAuth 흐름을 사용자 지정할 수 있습니다.

변수 | 목적  
---|---  
`CHUTES_CLIENT_ID` | 사용자 지정 OAuth 클라이언트 ID  
`CHUTES_CLIENT_SECRET` | 사용자 지정 OAuth 클라이언트 시크릿  
`CHUTES_OAUTH_REDIRECT_URI` | 사용자 지정 리디렉션 URI  
`CHUTES_OAUTH_SCOPES` | 사용자 지정 OAuth 범위  
  
리디렉션 앱 요구 사항과 도움말은 [Chutes OAuth 문서](<https://chutes.ai/docs/sign-in-with-chutes/overview>)를 참조하세요.

참고 사항

  * API 키 및 OAuth 검색은 모두 동일한 `chutes` 제공자 ID를 사용합니다.
  * Chutes 모델은 `chutes/<model-id>` 형식으로 등록됩니다.
  * 시작 시 검색이 실패하면 번들된 정적 카탈로그가 자동으로 사용됩니다.


## 관련 항목

[**모델 선택** 제공자 규칙, 모델 참조, 장애 조치 동작. ](</ko/concepts/model-providers>) [**설정 참조** 제공자 설정을 포함한 전체 설정 스키마. ](</ko/gateway/configuration-reference>) [**Chutes** Chutes 대시보드 및 API 문서. ](<https://chutes.ai>) [**Chutes API 키** Chutes API 키를 생성하고 관리합니다. ](<https://chutes.ai/settings/api-keys>)

Was this useful?YesNo