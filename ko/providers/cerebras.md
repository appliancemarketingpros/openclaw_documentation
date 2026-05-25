---
title: Cerebras
source_url: https://docs.openclaw.ai/ko/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>)는 맞춤형 추론 하드웨어에서 고속 OpenAI 호환 추론을 제공합니다. OpenClaw에는 정적 4개 모델 카탈로그가 포함된 번들 Cerebras 제공자 Plugin이 포함되어 있습니다.

속성 | 값  
---|---  
제공자 ID | `cerebras`  
Plugin | 번들, `enabledByDefault: true`  
인증 환경 변수 | `CEREBRAS_API_KEY`  
온보딩 플래그 | `--auth-choice cerebras-api-key`  
직접 CLI 플래그 | `--cerebras-api-key <key>`  
API | OpenAI 호환 (`openai-completions`)  
기본 URL | `https://api.cerebras.ai/v1`  
기본 모델 | `cerebras/zai-glm-4.7`  
  
## 시작하기

* ### API 키 받기

[Cerebras Cloud Console](<https://cloud.cerebras.ai>)에서 API 키를 생성합니다.

* ### 온보딩 실행

OnboardingCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

Env onlyCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### 모델 사용 가능 여부 확인

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

목록에는 번들 모델 4개가 모두 포함되어야 합니다. `CEREBRAS_API_KEY`가 확인되지 않으면 `openclaw models status --json`이 누락된 자격 증명을 `auth.unusableProfiles` 아래에 보고합니다.

## 비대화형 설정

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## 내장 카탈로그

OpenClaw는 공개 OpenAI 호환 엔드포인트를 반영하는 정적 Cerebras 카탈로그를 제공합니다. 네 모델 모두 128k 컨텍스트와 최대 출력 토큰 8,192개를 공유합니다.

모델 ref | 이름 | 추론 | 참고 사항  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | 예 | 기본 모델; 프리뷰 추론 모델  
`cerebras/gpt-oss-120b` | GPT OSS 120B | 예 | 프로덕션 추론 모델  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | 아니요 | 프리뷰 비추론 모델  
`cerebras/llama3.1-8b` | Llama 3.1 8B | 아니요 | 프로덕션 속도 중심 모델  
  
## 수동 구성

번들 Plugin 덕분에 일반적으로 API 키만 있으면 됩니다. 모델 메타데이터를 재정의하거나 정적 카탈로그에 대해 `mode: "merge"`로 실행하려는 경우 명시적인 `models.providers.cerebras` 구성을 사용하세요.

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## 관련 항목

[**모델 제공자** 제공자, 모델 refs, 장애 조치 동작 선택. ](</ko/concepts/model-providers>) [**사고 모드** 추론 가능 Cerebras 모델 2개에 대한 추론 노력 수준. ](</ko/tools/thinking>) [**구성 참조** 에이전트 기본값 및 모델 구성. ](</ko/gateway/config-agents#agent-defaults>) [**모델 FAQ** 인증 프로필, 모델 전환, "no profile" 오류 해결. ](</ko/help/faq-models>)

Was this useful?YesNo