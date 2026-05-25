---
title: ComfyUI
source_url: https://docs.openclaw.ai/ko/providers/comfy
scraped_at: 2026-05-25
---

OpenClaw는 워크플로 기반 ComfyUI 실행을 위한 번들 `comfy` Plugin을 제공합니다. 이 Plugin은 전적으로 워크플로 기반이므로, OpenClaw는 일반적인 `size`, `aspectRatio`, `resolution`, `durationSeconds`, 또는 TTS 스타일 제어를 그래프에 매핑하려고 하지 않습니다.

속성 | 세부 정보  
---|---  
Provider | `comfy`  
모델 | `comfy/workflow`  
공유 표면 | `image_generate`, `video_generate`, `music_generate`  
인증 | 로컬 ComfyUI에는 없음, Comfy Cloud에는 `COMFY_API_KEY` 또는 `COMFY_CLOUD_API_KEY`  
API | ComfyUI `/prompt` / `/history` / `/view` 및 Comfy Cloud `/api/*`  
  
## 지원 항목

  * 워크플로 JSON을 통한 이미지 생성
  * 업로드된 참조 이미지 1개를 사용한 이미지 편집
  * 워크플로 JSON을 통한 비디오 생성
  * 업로드된 참조 이미지 1개를 사용한 비디오 생성
  * 공유 `music_generate` 도구를 통한 음악 또는 오디오 생성
  * 구성된 노드 또는 일치하는 모든 출력 노드에서 결과 다운로드


## 시작하기

자신의 머신에서 ComfyUI를 실행할지, Comfy Cloud를 사용할지 선택하세요.

### 로컬

**가장 적합한 경우:** 자신의 머신 또는 LAN에서 ComfyUI 인스턴스를 직접 실행할 때.

* ### 로컬에서 ComfyUI 시작

로컬 ComfyUI 인스턴스가 실행 중인지 확인하세요(기본값 `http://127.0.0.1:8188`).

* ### 워크플로 JSON 준비

ComfyUI 워크플로 JSON 파일을 내보내거나 만드세요. 프롬프트 입력 노드와 OpenClaw가 읽어야 할 출력 노드의 노드 ID를 기록해 두세요.

* ### Provider 구성

`mode: "local"`을 설정하고 워크플로 파일을 가리키세요. 아래는 최소 이미지 예시입니다:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### 기본 모델 설정

구성한 capability에 대해 OpenClaw가 `comfy/workflow` 모델을 가리키도록 설정하세요:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### 검증

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

### Comfy Cloud

**가장 적합한 경우:** 로컬 GPU 리소스를 관리하지 않고 Comfy Cloud에서 워크플로를 실행할 때.

* ### API 키 받기

[comfy.org](<https://comfy.org>)에서 가입하고 계정 대시보드에서 API 키를 생성하세요.

* ### API 키 설정

다음 방법 중 하나로 키를 제공하세요:

bashCopy code
[code]
    # 환경 변수(권장)export COMFY_API_KEY="your-key" # 대체 환경 변수export COMFY_CLOUD_API_KEY="your-key" # 또는 config에 직접 입력openclaw config set plugins.entries.comfy.config.apiKey "your-key"
[/code]

* ### 워크플로 JSON 준비

ComfyUI 워크플로 JSON 파일을 내보내거나 만드세요. 프롬프트 입력 노드와 출력 노드의 노드 ID를 기록해 두세요.

* ### Provider 구성

`mode: "cloud"`를 설정하고 워크플로 파일을 가리키세요:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "cloud",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### 기본 모델 설정

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### 검증

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

## 구성

Comfy는 공유 최상위 연결 설정과 capability별 워크플로 섹션(`image`, `video`, `music`)을 지원합니다:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },          video: {            workflowPath: "./workflows/video-api.json",            promptNodeId: "12",            outputNodeId: "21",          },          music: {            workflowPath: "./workflows/music-api.json",            promptNodeId: "3",            outputNodeId: "18",          },        },      },    },  },}
[/code]

### 공유 키

키 | 타입 | 설명  
---|---|---  
`mode` | `"local"` 또는 `"cloud"` | 연결 모드입니다.  
`baseUrl` | string | 로컬은 기본값 `http://127.0.0.1:8188`, cloud는 `https://cloud.comfy.org`입니다.  
`apiKey` | string | 선택적 인라인 키이며, `COMFY_API_KEY` / `COMFY_CLOUD_API_KEY` env vars의 대안입니다.  
`allowPrivateNetwork` | boolean | cloud 모드에서 사설망/LAN `baseUrl`을 허용합니다.  
  
### capability별 키

이 키들은 `image`, `video`, 또는 `music` 섹션 내부에 적용됩니다:

키 | 필수 여부 | 기본값 | 설명  
---|---|---|---  
`workflow` 또는 `workflowPath` | 예 | \-- | ComfyUI 워크플로 JSON 파일 경로입니다.  
`promptNodeId` | 예 | \-- | 텍스트 프롬프트를 받는 노드 ID입니다.  
`promptInputName` | 아니요 | `"text"` | 프롬프트 노드의 입력 이름입니다.  
`outputNodeId` | 아니요 | \-- | 출력 결과를 읽을 노드 ID입니다. 생략하면 일치하는 모든 출력 노드를 사용합니다.  
`pollIntervalMs` | 아니요 | \-- | 작업 완료를 위한 폴링 간격(밀리초)입니다.  
`timeoutMs` | 아니요 | \-- | 워크플로 실행 제한 시간(밀리초)입니다.  
  
`image`와 `video` 섹션은 다음도 지원합니다:

키 | 필수 여부 | 기본값 | 설명  
---|---|---|---  
`inputImageNodeId` | 예 (참조 이미지를 전달할 때) | \-- | 업로드된 참조 이미지를 받는 노드 ID입니다.  
`inputImageInputName` | 아니요 | `"image"` | 이미지 노드의 입력 이름입니다.  
  
## 워크플로 세부 정보

이미지 워크플로

기본 이미지 모델을 `comfy/workflow`로 설정하세요:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

**참조 이미지 편집 예시:**

업로드된 참조 이미지를 사용한 이미지 편집을 활성화하려면 이미지 config에 `inputImageNodeId`를 추가하세요:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          image: {            workflowPath: "./workflows/edit-api.json",            promptNodeId: "6",            inputImageNodeId: "7",            inputImageInputName: "image",            outputNodeId: "9",          },        },      },    },  },}
[/code]

비디오 워크플로

기본 비디오 모델을 `comfy/workflow`로 설정하세요:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

Comfy 비디오 워크플로는 구성된 그래프를 통해 text-to-video와 image-to-video를 지원합니다.

음악 워크플로

번들 Plugin은 워크플로로 정의된 오디오 또는 음악 출력을 위한 음악 생성 provider를 등록하며, 이는 공유 `music_generate` 도구를 통해 노출됩니다:

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

오디오 워크플로 JSON과 출력 노드를 가리키도록 `music` config 섹션을 사용하세요.

하위 호환성

중첩된 `image` 섹션 없이 기존 최상위 이미지 config도 계속 작동합니다:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          workflowPath: "./workflows/flux-api.json",          promptNodeId: "6",          outputNodeId: "9",        },      },    },  },}
[/code]

OpenClaw는 이 레거시 형태를 이미지 워크플로 config로 취급합니다. 즉시 마이그레이션할 필요는 없지만, 새 설정에는 중첩된 `image` / `video` / `music` 섹션을 권장합니다.

Live 테스트

번들 Plugin에 대한 opt-in live coverage가 있습니다:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

matching Comfy 워크플로 섹션이 구성되지 않은 경우, live 테스트는 개별 이미지, 비디오, 또는 음악 케이스를 건너뜁니다.

## 관련 항목

[**이미지 생성** 이미지 생성 도구 구성 및 사용법입니다. ](</ko/tools/image-generation>) [**비디오 생성** 비디오 생성 도구 구성 및 사용법입니다. ](</ko/tools/video-generation>) [**음악 생성** 음악 및 오디오 생성 도구 설정입니다. ](</ko/tools/music-generation>) [**Provider 디렉터리** 모든 provider 및 모델 참조 개요입니다. ](</ko/providers>) [**구성 참조** 에이전트 기본값을 포함한 전체 구성 참조입니다. ](</ko/gateway/config-agents#agent-defaults>)

Was this useful?YesNo