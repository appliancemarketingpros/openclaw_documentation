---
title: NVIDIA
source_url: https://docs.openclaw.ai/ko/providers/nvidia
scraped_at: 2026-05-25
---

NVIDIA는 오픈 모델을 무료로 사용할 수 있는 OpenAI 호환 API를 `https://integrate.api.nvidia.com/v1`에서 제공합니다. [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>)에서 발급한 API 키로 인증하세요.

## 시작하기

* ### API 키 가져오기

[build.nvidia.com](<https://build.nvidia.com/settings/api-keys>)에서 API 키를 생성합니다.

* ### 키 내보내기 및 온보딩 실행

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### NVIDIA 모델 설정

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

비대화형 설정의 경우 키를 직접 전달할 수도 있습니다.

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## Config 예시

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## 기본 제공 카탈로그

모델 ref | 이름 | 컨텍스트 | 최대 출력  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## 고급 구성

자동 활성화 동작

`NVIDIA_API_KEY` 환경 변수가 설정되어 있으면 provider가 자동으로 활성화됩니다. 키 외에는 명시적인 provider 구성이 필요하지 않습니다.

카탈로그 및 가격

번들 카탈로그는 정적입니다. NVIDIA가 현재 나열된 모델에 대해 무료 API 액세스를 제공하므로 소스의 비용 기본값은 `0`입니다.

OpenAI 호환 endpoint

NVIDIA는 표준 `/v1` completions endpoint를 사용합니다. 모든 OpenAI 호환 도구는 NVIDIA 기본 URL로 바로 작동해야 합니다.

느린 사용자 지정 provider 응답

일부 NVIDIA 호스팅 사용자 지정 모델은 첫 응답 청크를 내보내기 전에 기본 모델 idle watchdog보다 더 오래 걸릴 수 있습니다. 사용자 지정 NVIDIA provider 항목의 경우 전체 agent 런타임 timeout을 높이지 말고 provider timeout을 높이세요.

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## 관련 항목

[**모델 선택** provider, 모델 ref, failover 동작 선택. ](</ko/concepts/model-providers>) [**구성 참조** agent, 모델, provider에 대한 전체 config 참조. ](</ko/gateway/configuration-reference>)

Was this useful?YesNo