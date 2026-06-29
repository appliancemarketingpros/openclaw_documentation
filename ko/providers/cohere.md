---
title: Cohere
source_url: https://docs.openclaw.ai/ko/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>)는 Compatibility API를 통해 OpenAI 호환 추론을 제공합니다. OpenClaw는 외부화 전환 기간 동안 Cohere 제공자를 함께 제공하며, Command A 모델 카탈로그가 포함된 공식 외부 Plugin으로도 게시합니다.

속성 | 값  
---|---  
제공자 ID | `cohere`  
Plugin | 전환 기간 동안 번들로 제공; 공식 외부 패키지  
인증 환경 변수 | `COHERE_API_KEY`  
온보딩 플래그 | `--auth-choice cohere-api-key`  
직접 CLI 플래그 | `--cohere-api-key <key>`  
API | OpenAI 호환 (`openai-completions`)  
기본 URL | `https://api.cohere.ai/compatibility/v1`  
기본 모델 | `cohere/command-a-03-2025`  
  
## 시작하기

  1. Cohere는 현재 OpenClaw 패키지에 포함되어 있습니다. 사용할 수 없는 경우 외부 패키지를 설치하고 Gateway를 다시 시작하세요.

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. Cohere API 키를 만듭니다.
  3. 온보딩을 실행합니다.

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. 카탈로그를 사용할 수 있는지 확인합니다.

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

기본 모델은 기본 모델이 아직 구성되어 있지 않은 경우에만 설정됩니다.

## 환경 변수만 사용하는 설정

`COHERE_API_KEY`를 Gateway 프로세스에서 사용할 수 있게 한 다음 Cohere 모델을 선택하세요.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## 관련 항목

  * [모델 제공자](</ko/concepts/model-providers>)
  * [모델 CLI](</ko/cli/models>)
  * [제공자 디렉터리](</ko/providers>)


Was this useful?YesNo

Open issue