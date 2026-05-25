---
title: Fireworks
source_url: https://docs.openclaw.ai/ko/providers/fireworks
scraped_at: 2026-05-25
---

[Fireworks](<https://fireworks.ai>)는 OpenAI 호환 API를 통해 오픈 웨이트 모델과 라우팅된 모델을 제공합니다. OpenClaw에는 사전 카탈로그화된 Kimi 모델 두 개와 함께 제공되며 런타임에 모든 Fireworks 모델 또는 라우터 ID를 허용하는 번들 Fireworks 제공자 Plugin이 포함되어 있습니다.

속성 | 값  
---|---  
제공자 ID | `fireworks` (별칭: `fireworks-ai`)  
Plugin | 번들, `enabledByDefault: true`  
인증 환경 변수 | `FIREWORKS_API_KEY`  
온보딩 플래그 | `--auth-choice fireworks-api-key`  
직접 CLI 플래그 | `--fireworks-api-key <key>`  
API | OpenAI 호환 (`openai-completions`)  
기본 URL | `https://api.fireworks.ai/inference/v1`  
기본 모델 | `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`  
기본 별칭 | `Kimi K2.5 Turbo`  
  
## 시작하기

* ### Fireworks API 키 설정

온보딩Copy code
[code]
    openclaw onboard --auth-choice fireworks-api-key
[/code]

직접 플래그Copy code
[code]
    openclaw onboard --non-interactive \--auth-choice fireworks-api-key \--fireworks-api-key "$FIREWORKS_API_KEY"
[/code]

환경 변수만Copy code
[code]
    export FIREWORKS_API_KEY=fw-...
[/code]

온보딩은 인증 프로필의 `fireworks` 제공자에 키를 저장하고 **Fire Pass** Kimi K2.5 Turbo 라우터를 기본 모델로 설정합니다.

* ### 모델을 사용할 수 있는지 확인

bashCopy code
[code]
    openclaw models list --provider fireworks
[/code]

목록에는 `Kimi K2.6` 및 `Kimi K2.5 Turbo (Fire Pass)`가 포함되어야 합니다. `FIREWORKS_API_KEY`를 확인할 수 없으면 `openclaw models status --json`이 `auth.unusableProfiles` 아래에 누락된 자격 증명을 보고합니다.

## 비대화형 설정

스크립트 또는 CI 설치의 경우 모든 값을 명령줄로 전달합니다.

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice fireworks-api-key \  --fireworks-api-key "$FIREWORKS_API_KEY" \  --skip-health \  --accept-risk
[/code]

## 내장 카탈로그

모델 참조 | 이름 | 입력 | 컨텍스트 | 최대 출력 | Thinking  
---|---|---|---|---|---  
`fireworks/accounts/fireworks/models/kimi-k2p6` | Kimi K2.6 | 텍스트 + 이미지 | 262,144 | 262,144 | 강제로 끔  
`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo` | Kimi K2.5 Turbo (Fire Pass) | 텍스트 + 이미지 | 256,000 | 256,000 | 강제로 끔 (기본값)  
  
## 사용자 지정 Fireworks 모델 ID

OpenClaw는 런타임에 모든 Fireworks 모델 또는 라우터 ID를 허용합니다. Fireworks에 표시된 정확한 ID를 사용하고 `fireworks/`를 접두사로 붙이세요. 동적 확인은 Fire Pass 템플릿(텍스트 + 이미지 입력, OpenAI 호환 API, 기본 비용 0)을 복제하고 ID가 Kimi 패턴과 일치하면 thinking을 자동으로 비활성화합니다.

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "fireworks/accounts/fireworks/models/<your-model-id>",      },    },  },}
[/code]

모델 ID 접두사가 작동하는 방식

OpenClaw의 모든 Fireworks 모델 참조는 `fireworks/`로 시작하며, 그 뒤에는 Fireworks 플랫폼의 정확한 ID 또는 라우터 경로가 옵니다. 예:

  * 라우터 모델: `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`
  * 직접 모델: `fireworks/accounts/fireworks/models/<model-name>`


OpenClaw는 API 요청을 구성할 때 `fireworks/` 접두사를 제거하고, 남은 경로를 OpenAI 호환 `model` 필드로 Fireworks 엔드포인트에 전송합니다.

Kimi에서 thinking이 강제로 꺼지는 이유

Kimi가 Moonshot 자체 API를 통해 thinking을 지원하더라도, 요청에 `reasoning_*` 매개변수가 포함되어 있으면 Fireworks K2.6은 400을 반환합니다. 번들 정책(`extensions/fireworks/thinking-policy.ts`)은 Kimi 모델 ID에 대해 `off` thinking 수준만 알리므로 수동 `/think` 전환과 제공자 정책 표면이 런타임 계약과 일치합니다.

Kimi 추론을 엔드투엔드로 사용하려면 [Moonshot 제공자](</ko/providers/moonshot>)를 구성하고 같은 모델을 통해 라우팅하세요.

데몬의 환경 가용성

Gateway가 관리형 서비스(launchd, systemd, Docker)로 실행되는 경우 Fireworks 키는 대화형 셸뿐 아니라 해당 프로세스에서도 보여야 합니다.

macOS에서 `openclaw gateway install`은 이미 `~/.openclaw/.env`를 LaunchAgent 환경 파일에 연결합니다. 키를 교체한 후 install을 다시 실행하거나 `openclaw doctor --fix`를 실행하세요.

## 관련 항목

[**모델 제공자** 제공자, 모델 참조, 장애 조치 동작 선택. ](</ko/concepts/model-providers>) [**Thinking 모드** `/think` 수준, 제공자 정책, 추론 가능 모델 라우팅. ](</ko/tools/thinking>) [**Moonshot** Moonshot 자체 API를 통해 네이티브 thinking 출력으로 Kimi를 실행합니다. ](</ko/providers/moonshot>) [**문제 해결** 일반적인 문제 해결 및 FAQ. ](</ko/help/troubleshooting>)

Was this useful?YesNo