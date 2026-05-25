---
title: Together AI
source_url: https://docs.openclaw.ai/ko/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>)는 통합 API를 통해 Llama, DeepSeek, Kimi 등 주요 오픈 소스 모델에 대한 액세스를 제공합니다.

속성 | 값  
---|---  
Provider | `together`  
인증 | `TOGETHER_API_KEY`  
API | OpenAI 호환  
기본 URL | `https://api.together.xyz/v1`  
  
## 시작하기

* ### API 키 받기

[api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>)에서 API 키를 생성합니다.

* ### 온보딩 실행

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### 기본 모델 설정

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### 비대화형 예시

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## 기본 제공 카탈로그

OpenClaw에는 다음 Together 카탈로그가 번들로 제공됩니다.

모델 참조 | 이름 | 입력 | 컨텍스트 | 참고 사항  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | 텍스트, 이미지 | 262,144 | 기본 모델; 추론 활성화  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | 텍스트 | 202,752 | 범용 텍스트 모델  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | 텍스트 | 131,072 | 빠른 지시 모델  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | 텍스트, 이미지 | 10,000,000 | 멀티모달  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | 텍스트, 이미지 | 20,000,000 | 멀티모달  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | 텍스트 | 131,072 | 범용 텍스트 모델  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | 텍스트 | 131,072 | 추론 모델  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | 텍스트 | 262,144 | 보조 Kimi 텍스트 모델  
  
## 동영상 생성

번들로 제공되는 `together` Plugin은 공유 `video_generate` 도구를 통한 동영상 생성도 등록합니다.

속성 | 값  
---|---  
기본 동영상 모델 | `together/Wan-AI/Wan2.2-T2V-A14B`  
모드 | 텍스트-동영상, 단일 이미지 참조  
지원되는 매개변수 | `aspectRatio`, `resolution`  
  
Together를 기본 동영상 Provider로 사용하려면 다음과 같이 설정합니다.

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

환경 참고 사항

Gateway가 데몬(launchd/systemd)으로 실행되는 경우 해당 프로세스에서 `TOGETHER_API_KEY`를 사용할 수 있는지 확인하세요(예: `~/.openclaw/.env` 또는 `env.shellEnv`를 통해).

문제 해결

  * 키가 작동하는지 확인하세요: `openclaw models list --provider together`
  * 모델이 나타나지 않으면 Gateway 프로세스에 맞는 올바른 환경에 API 키가 설정되어 있는지 확인하세요.
  * 모델 참조는 `together/<model-id>` 형식을 사용합니다.


## 관련 항목

[**모델 선택** Provider 규칙, 모델 참조, 장애 조치 동작. ](</ko/concepts/model-providers>) [**동영상 생성** 공유 동영상 생성 도구 매개변수와 Provider 선택. ](</ko/tools/video-generation>) [**구성 참조** Provider 설정을 포함한 전체 구성 스키마. ](</ko/gateway/configuration-reference>) [**Together AI** Together AI 대시보드, API 문서, 가격. ](<https://together.ai>)

Was this useful?YesNo