---
title: xAI
source_url: https://docs.openclaw.ai/ko/providers/xai
scraped_at: 2026-05-25
---

OpenClaw는 Grok 모델을 위한 번들 `xai` 제공자 Plugin과 함께 제공됩니다.

## 시작하기

* ### API 키 만들기

[xAI 콘솔](<https://console.x.ai/>)에서 API 키를 만드세요.

* ### API 키 설정

`XAI_API_KEY`를 설정하거나 다음을 실행하세요.

bashCopy code
[code]
    openclaw onboard --auth-choice xai-api-key
[/code]

* ### 모델 선택

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "xai/grok-4.3" } } },}
[/code]

## 내장 카탈로그

OpenClaw에는 다음 xAI 모델 제품군이 기본 포함되어 있습니다.

제품군 | 모델 ID  
---|---  
Grok 3 | `grok-3`, `grok-3-fast`, `grok-3-mini`, `grok-3-mini-fast`  
Grok 4.3 | `grok-4.3`  
Grok 4 | `grok-4`, `grok-4-0709`  
Grok 4 Fast | `grok-4-fast`, `grok-4-fast-non-reasoning`  
Grok 4.1 Fast | `grok-4-1-fast`, `grok-4-1-fast-non-reasoning`  
Grok 4.20 Beta | `grok-4.20-beta-latest-reasoning`, `grok-4.20-beta-latest-non-reasoning`  
Grok Code | `grok-code-fast-1`  
  
Plugin은 더 새로운 `grok-4*` 및 `grok-code-fast*` ID가 동일한 API 형태를 따르는 경우에도 이를 앞으로 해석합니다.

## OpenClaw 기능 적용 범위

번들 Plugin은 xAI의 현재 공개 API 표면을 OpenClaw의 공유 제공자 및 도구 계약에 매핑합니다. 공유 계약에 맞지 않는 기능 (예: 스트리밍 TTS 및 실시간 음성)은 노출되지 않습니다. 아래 표를 참조하세요.

xAI 기능 | OpenClaw 표면 | 상태  
---|---|---  
채팅 / Responses | `xai/<model>` 모델 제공자 | 예  
서버 측 웹 검색 | `web_search` 제공자 `grok` | 예  
서버 측 X 검색 | `x_search` 도구 | 예  
서버 측 코드 실행 | `code_execution` 도구 | 예  
이미지 | `image_generate` | 예  
동영상 | `video_generate` | 예  
배치 텍스트 음성 변환 | `messages.tts.provider: "xai"` / `tts` | 예  
스트리밍 TTS | - | 노출되지 않음; OpenClaw의 TTS 계약은 완전한 오디오 버퍼를 반환합니다  
배치 음성 텍스트 변환 | `tools.media.audio` / 미디어 이해 | 예  
스트리밍 음성 텍스트 변환 | Voice Call `streaming.provider: "xai"` | 예  
실시간 음성 | - | 아직 노출되지 않음; 다른 세션/WebSocket 계약  
파일 / 배치 | 일반 모델 API 호환성만 | 일급 OpenClaw 도구가 아님  
  
### 빠른 모드 매핑

`/fast on` 또는 `agents.defaults.models["xai/<model>"].params.fastMode: true`는 네이티브 xAI 요청을 다음과 같이 다시 씁니다.

원본 모델 | 빠른 모드 대상  
---|---  
`grok-3` | `grok-3-fast`  
`grok-3-mini` | `grok-3-mini-fast`  
`grok-4` | `grok-4-fast`  
`grok-4-0709` | `grok-4-fast`  
  
### 레거시 호환성 별칭

레거시 별칭은 여전히 정식 번들 ID로 정규화됩니다.

레거시 별칭 | 정식 ID  
---|---  
`grok-4-fast-reasoning` | `grok-4-fast`  
`grok-4-1-fast-reasoning` | `grok-4-1-fast`  
`grok-4.20-reasoning` | `grok-4.20-beta-latest-reasoning`  
`grok-4.20-non-reasoning` | `grok-4.20-beta-latest-non-reasoning`  
  
## 기능

웹 검색

번들 `grok` 웹 검색 제공자는 `XAI_API_KEY` 또는 Plugin 웹 검색 키를 사용할 수 있습니다.

bashCopy code
[code]
    openclaw config set tools.web.search.provider grok
[/code]

동영상 생성

번들 `xai` Plugin은 공유 `video_generate` 도구를 통해 동영상 생성을 등록합니다.

  * 기본 동영상 모델: `xai/grok-imagine-video`
  * 모드: 텍스트-동영상, 이미지-동영상, 참조 이미지 생성, 원격 동영상 편집, 원격 동영상 확장
  * 화면 비율: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`
  * 해상도: `480P`, `720P`
  * 길이: 생성/이미지-동영상의 경우 1-15초, `reference_image` 역할을 사용할 때는 1-10초, 확장의 경우 2-10초
  * 참조 이미지 생성: 제공된 모든 이미지에 대해 `imageRoles`를 `reference_image`로 설정하세요. xAI는 이러한 이미지를 최대 7개까지 허용합니다.


xAI를 기본 동영상 제공자로 사용하려면:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "xai/grok-imagine-video",      },    },  },}
[/code]

이미지 생성

번들 `xai` Plugin은 공유 `image_generate` 도구를 통해 이미지 생성을 등록합니다.

  * 기본 이미지 모델: `xai/grok-imagine-image`
  * 추가 모델: `xai/grok-imagine-image-pro`
  * 모드: 텍스트-이미지 및 참조 이미지 편집
  * 참조 입력: `image` 하나 또는 최대 다섯 개의 `images`
  * 화면 비율: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `2:3`, `3:2`
  * 해상도: `1K`, `2K`
  * 개수: 최대 4개 이미지


OpenClaw는 생성된 미디어를 일반 채널 첨부 경로를 통해 저장하고 전달할 수 있도록 xAI에 `b64_json` 이미지 응답을 요청합니다. 로컬 참조 이미지는 데이터 URL로 변환되며, 원격 `http(s)` 참조는 그대로 전달됩니다.

xAI를 기본 이미지 제공자로 사용하려면:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "xai/grok-imagine-image",      },    },  },}
[/code]

텍스트 음성 변환

번들 `xai` Plugin은 공유 `tts` 제공자 표면을 통해 텍스트 음성 변환을 등록합니다.

  * 음성: `eve`, `ara`, `rex`, `sal`, `leo`, `una`
  * 기본 음성: `eve`
  * 형식: `mp3`, `wav`, `pcm`, `mulaw`, `alaw`
  * 언어: BCP-47 코드 또는 `auto`
  * 속도: 제공자 네이티브 속도 재정의
  * 네이티브 Opus 음성 메모 형식은 지원되지 않음


xAI를 기본 TTS 제공자로 사용하려면:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "xai",      providers: {        xai: {          voiceId: "eve",        },      },    },  },}
[/code]

음성 텍스트 변환

번들 `xai` Plugin은 OpenClaw의 미디어 이해 전사 표면을 통해 배치 음성 텍스트 변환을 등록합니다.

  * 기본 모델: `grok-stt`
  * 엔드포인트: xAI REST `/v1/stt`
  * 입력 경로: multipart 오디오 파일 업로드
  * Discord 음성 채널 세그먼트 및 채널 오디오 첨부를 포함하여, 인바운드 오디오 전사가 `tools.media.audio`를 사용하는 모든 OpenClaw 위치에서 지원됨


인바운드 오디오 전사에 xAI를 강제하려면:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [          {            type: "provider",            provider: "xai",            model: "grok-stt",          },        ],      },    },  },}
[/code]

언어는 공유 오디오 미디어 구성 또는 호출별 전사 요청을 통해 제공할 수 있습니다. 프롬프트 힌트는 공유 OpenClaw 표면에서 허용되지만, xAI REST STT 통합은 파일, 모델, 언어만 전달합니다. 이들이 현재 공개 xAI 엔드포인트에 명확하게 매핑되기 때문입니다.

스트리밍 음성 텍스트 변환

번들 `xai` Plugin은 라이브 음성 통화 오디오용 실시간 전사 제공자도 등록합니다.

  * 엔드포인트: xAI WebSocket `wss://api.x.ai/v1/stt`
  * 기본 인코딩: `mulaw`
  * 기본 샘플링 레이트: `8000`
  * 기본 엔드포인팅: `800ms`
  * 중간 전사: 기본적으로 활성화됨


Voice Call의 Twilio 미디어 스트림은 G.711 µ-law 오디오 프레임을 전송하므로, xAI 제공자는 트랜스코딩 없이 해당 프레임을 직접 전달할 수 있습니다.

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "xai",            providers: {              xai: {                apiKey: "${XAI_API_KEY}",                endpointingMs: 800,                language: "en",              },            },          },        },      },    },  },}
[/code]

제공자 소유 구성은 `plugins.entries.voice-call.config.streaming.providers.xai` 아래에 있습니다. 지원되는 키는 `apiKey`, `baseUrl`, `sampleRate`, `encoding`(`pcm`, `mulaw` 또는 `alaw`), `interimResults`, `endpointingMs`, `language`입니다.

x_search 구성

번들된 xAI Plugin은 Grok을 통해 X(이전 Twitter) 콘텐츠를 검색하기 위한 OpenClaw 도구로 `x_search`를 노출합니다.

구성 경로: `plugins.entries.xai.config.xSearch`

키 | 유형 | 기본값 | 설명  
---|---|---|---  
`enabled` | boolean | - | x_search 활성화 또는 비활성화  
`model` | string | `grok-4-1-fast` | x_search 요청에 사용되는 모델  
`baseUrl` | string | - | xAI Responses 기본 URL 재정의  
`inlineCitations` | boolean | - | 결과에 인라인 인용 포함  
`maxTurns` | number | - | 최대 대화 턴 수  
`timeoutSeconds` | number | - | 요청 제한 시간(초)  
`cacheTtlMinutes` | number | - | 캐시 유효 시간(분)  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast",            baseUrl: "https://api.x.ai/v1",            inlineCitations: true,          },        },      },    },  },}
[/code]

코드 실행 구성

번들된 xAI Plugin은 xAI의 샌드박스 환경에서 원격 코드 실행을 위한 OpenClaw 도구로 `code_execution`을 노출합니다.

구성 경로: `plugins.entries.xai.config.codeExecution`

키 | 유형 | 기본값 | 설명  
---|---|---|---  
`enabled` | boolean | `true`(키가 있는 경우) | 코드 실행 활성화 또는 비활성화  
`model` | string | `grok-4-1-fast` | 코드 실행 요청에 사용되는 모델  
`maxTurns` | number | - | 최대 대화 턴 수  
`timeoutSeconds` | number | - | 요청 제한 시간(초)  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast",          },        },      },    },  },}
[/code]

알려진 제한 사항

  * 현재 인증은 API 키만 지원합니다. API 키는 xAI 인증 프로필, 환경 변수 또는 Plugin 구성에 저장할 수 있습니다. 아직 OpenClaw에는 xAI OAuth 또는 device-code 흐름이 없습니다.
  * `grok-4.20-multi-agent-experimental-beta-0304`는 표준 OpenClaw xAI 전송과 다른 업스트림 API 표면이 필요하므로 일반 xAI 제공자 경로에서 지원되지 않습니다.
  * xAI Realtime 음성은 아직 OpenClaw 제공자로 등록되어 있지 않습니다. 배치 STT 또는 스트리밍 전사와는 다른 양방향 음성 세션 계약이 필요합니다.
  * xAI 이미지 `quality`, 이미지 `mask`, 추가 네이티브 전용 화면비는 공유 `image_generate` 도구에 대응하는 제공자 간 제어가 생길 때까지 노출되지 않습니다.

고급 참고 사항

  * OpenClaw는 공유 실행기 경로에서 xAI 전용 도구 스키마 및 도구 호출 호환성 수정을 자동으로 적용합니다.
  * 네이티브 xAI 요청의 기본값은 `tool_stream: true`입니다. 비활성화하려면 `agents.defaults.models["xai/<model>"].params.tool_stream`을 `false`로 설정하세요.
  * 번들된 xAI 래퍼는 네이티브 xAI 요청을 보내기 전에 지원되지 않는 엄격한 도구 스키마 플래그와 reasoning 페이로드 키를 제거합니다.
  * `web_search`, `x_search`, `code_execution`은 OpenClaw 도구로 노출됩니다. OpenClaw는 모든 네이티브 도구를 모든 채팅 턴에 연결하는 대신 각 도구 요청 안에서 필요한 특정 xAI 내장 기능을 활성화합니다.
  * Grok `web_search`는 `plugins.entries.xai.config.webSearch.baseUrl`을 읽습니다. `x_search`는 `plugins.entries.xai.config.xSearch.baseUrl`을 읽은 다음 Grok 웹 검색 기본 URL로 폴백합니다.
  * `x_search`와 `code_execution`은 핵심 모델 런타임에 하드코딩되지 않고 번들된 xAI Plugin이 소유합니다.
  * `code_execution`은 원격 xAI 샌드박스 실행이며, 로컬 [`exec`](</ko/tools/exec>)가 아닙니다.


## 라이브 테스트

xAI 미디어 경로는 단위 테스트와 선택 실행 라이브 스위트에서 다룹니다. 라이브 명령은 `XAI_API_KEY`를 확인하기 전에 `~/.profile`을 포함해 로그인 셸에서 비밀 값을 로드합니다.

bashCopy code
[code]
    pnpm test extensions/xaiOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 pnpm test:live -- extensions/xai/xai.live.test.tsOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 OPENCLAW_LIVE_IMAGE_GENERATION_PROVIDERS=xai pnpm test:live -- test/image-generation.runtime.live.test.ts
[/code]

제공자별 라이브 파일은 일반 TTS, 전화 통화에 적합한 PCM TTS를 합성하고, xAI 배치 STT로 오디오를 전사하며, 동일한 PCM을 xAI 실시간 STT로 스트리밍하고, 텍스트-이미지 출력을 생성하며, 참조 이미지를 편집합니다. 공유 이미지 라이브 파일은 OpenClaw의 런타임 선택, 폴백, 정규화, 미디어 첨부 경로를 통해 동일한 xAI 제공자를 검증합니다.

## 관련 항목

[**모델 선택** 제공자, 모델 참조, 장애 조치 동작 선택. ](</ko/concepts/model-providers>) [**비디오 생성** 공유 비디오 도구 매개변수와 제공자 선택. ](</ko/tools/video-generation>) [**모든 제공자** 더 넓은 제공자 개요. ](</ko/providers>) [**문제 해결** 일반적인 문제와 수정 방법. ](</ko/help/troubleshooting>)

Was this useful?YesNo