---
title: Fal
source_url: https://docs.openclaw.ai/ko/providers/fal
scraped_at: 2026-05-25
---

OpenClaw은 호스팅 이미지 및 비디오 생성을 위한 번들 `fal` 제공자를 제공합니다.

속성 | 값  
---|---  
제공자 | `fal`  
인증 | `FAL_KEY`(표준; `FAL_API_KEY`도 대체 수단으로 동작)  
API | fal 모델 엔드포인트  
  
## 시작하기

* ### Set the API key

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### Set a default image model

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## 이미지 생성

번들 `fal` 이미지 생성 제공자의 기본값은 `fal/fal-ai/flux/dev`입니다.

기능 | 값  
---|---  
최대 이미지 수 | 요청당 4개  
편집 모드 | Flux: 참조 이미지 1개; GPT Image 2: 10개; Nano Banana 2: 14개  
크기 재정의 | 지원됨  
종횡비 | 생성 및 GPT Image 2/Nano Banana 2 편집에서 지원됨  
해상도 | 지원됨  
출력 형식 | `png` 또는 `jpeg`  
  
PNG 출력을 원할 때는 `outputFormat: "png"`를 사용하세요. fal은 OpenClaw에서 명시적인 투명 배경 제어를 선언하지 않으므로, fal 모델에서는 `background: "transparent"`가 무시된 재정의로 보고됩니다.

fal을 기본 이미지 제공자로 사용하려면:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## 비디오 생성

번들 `fal` 비디오 생성 제공자의 기본값은 `fal/fal-ai/minimax/video-01-live`입니다.

기능 | 값  
---|---  
모드 | 텍스트-투-비디오, 단일 이미지 참조, Seedance 참조-투-비디오  
런타임 | 장기 실행 작업을 위한 큐 기반 제출/상태/결과 흐름  
  
Available video models

**HeyGen video-agent:**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0:**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

Seedance 2.0 config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

Seedance 2.0 reference-to-video config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

참조-투-비디오는 공유 `video_generate` `images`, `videos`, `audioRefs` 매개변수를 통해 최대 9개의 이미지, 3개의 비디오, 3개의 오디오 참조를 허용하며, 총 참조 파일은 최대 12개입니다.

HeyGen video-agent config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## 관련 항목

[**Image generation** 공유 이미지 도구 매개변수 및 제공자 선택입니다. ](</ko/tools/image-generation>) [**Video generation** 공유 비디오 도구 매개변수 및 제공자 선택입니다. ](</ko/tools/video-generation>) [**Configuration reference** 이미지 및 비디오 모델 선택을 포함한 Agent 기본값입니다. ](</ko/gateway/config-agents#agent-defaults>)

Was this useful?YesNo