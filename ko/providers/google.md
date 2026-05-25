---
title: Google (Gemini)
source_url: https://docs.openclaw.ai/ko/providers/google
scraped_at: 2026-05-25
---

Google Plugin은 Google AI Studio를 통해 Gemini 모델에 대한 접근을 제공하며, 이미지 생성, 미디어 이해(이미지/오디오/비디오), 텍스트 음성 변환, Gemini Grounding을 통한 웹 검색도 제공합니다.

  * 제공자: `google`
  * 인증: `GEMINI_API_KEY` 또는 `GOOGLE_API_KEY`
  * API: Google Gemini API
  * Runtime 옵션: provider/model `agentRuntime.id: "google-gemini-cli"`는 모델 참조를 `google/*`로 표준화된 상태로 유지하면서 Gemini CLI OAuth를 재사용합니다.


## 시작하기

선호하는 인증 방식을 선택하고 설정 단계를 따르세요.

### API 키

**적합한 용도:** Google AI Studio를 통한 표준 Gemini API 접근.

* ### 온보딩 실행

bashCopy code
[code]
    openclaw onboard --auth-choice gemini-api-key
[/code]

또는 키를 직접 전달합니다.

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY"
[/code]

* ### 기본 모델 설정

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "google/gemini-3.1-pro-preview" },    },  },}
[/code]

* ### 모델 사용 가능 여부 확인

bashCopy code
[code]
    openclaw models list --provider google
[/code]

### Gemini CLI (OAuth)

**적합한 용도:** 별도의 API 키 대신 PKCE OAuth를 통해 기존 Gemini CLI 로그인을 재사용.

* ### Gemini CLI 설치

로컬 `gemini` 명령은 `PATH`에서 사용할 수 있어야 합니다.

bashCopy code
[code]
    # Homebrewbrew install gemini-cli # or npmnpm install -g @google/gemini-cli
[/code]

OpenClaw는 일반적인 Windows/npm 레이아웃을 포함해 Homebrew 설치와 전역 npm 설치를 모두 지원합니다.

* ### OAuth로 로그인

bashCopy code
[code]
    openclaw models auth login --provider google-gemini-cli --set-default
[/code]

* ### 모델 사용 가능 여부 확인

bashCopy code
[code]
    openclaw models list --provider google
[/code]

  * 기본 모델: `google/gemini-3.1-pro-preview`
  * Runtime: `google-gemini-cli`
  * 별칭: `gemini-cli`


Gemini 3.1 Pro의 Gemini API 모델 ID는 `gemini-3.1-pro-preview`입니다. OpenClaw는 편의 별칭으로 더 짧은 `google/gemini-3.1-pro`를 허용하며, 제공자 호출 전에 이를 정규화합니다.

**환경 변수:**

  * `OPENCLAW_GEMINI_OAUTH_CLIENT_ID`
  * `OPENCLAW_GEMINI_OAUTH_CLIENT_SECRET`


(또는 `GEMINI_CLI_*` 변형.)

`google-gemini-cli/*` 모델 참조는 레거시 호환성 별칭입니다. 새 설정에서는 로컬 Gemini CLI 실행을 원할 때 `google/*` 모델 참조와 `google-gemini-cli` Runtime을 사용해야 합니다.

## 기능

기능 | 지원  
---|---  
채팅 완성 | 예  
이미지 생성 | 예  
음악 생성 | 예  
텍스트 음성 변환 | 예  
실시간 음성 | 예(Google Live API)  
이미지 이해 | 예  
오디오 전사 | 예  
비디오 이해 | 예  
웹 검색(Grounding) | 예  
사고/추론 | 예(Gemini 2.5+ / Gemini 3+)  
Gemma 4 모델 | 예  
  
## 웹 검색

번들된 `gemini` 웹 검색 제공자는 Gemini Google Search grounding을 사용합니다. `plugins.entries.google.config.webSearch` 아래에 전용 검색 키를 구성하거나, `GEMINI_API_KEY` 이후 `models.providers.google.apiKey`를 재사용하게 둘 수 있습니다.

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash",          },        },      },    },  },}
[/code]

자격 증명 우선순위는 전용 `webSearch.apiKey`, 그다음 `GEMINI_API_KEY`, 그다음 `models.providers.google.apiKey`입니다. `webSearch.baseUrl`은 선택 사항이며 운영자 프록시 또는 호환 Gemini API 엔드포인트를 위해 존재합니다. 생략하면 Gemini 웹 검색은 `models.providers.google.baseUrl`을 재사용합니다. 제공자별 도구 동작은 [Gemini 검색](</ko/tools/gemini-search>)을 참조하세요.

## 이미지 생성

번들된 `google` 이미지 생성 제공자의 기본값은 `google/gemini-3.1-flash-image-preview`입니다.

  * `google/gemini-3-pro-image-preview`도 지원
  * 생성: 요청당 최대 4개 이미지
  * 편집 모드: 활성화됨, 입력 이미지 최대 5개
  * 기하 제어: `size`, `aspectRatio`, `resolution`


Google을 기본 이미지 제공자로 사용하려면:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

## 비디오 생성

번들된 `google` Plugin은 공유 `video_generate` 도구를 통해 비디오 생성도 등록합니다.

  * 기본 비디오 모델: `google/veo-3.1-fast-generate-preview`
  * 모드: 텍스트-비디오, 이미지-비디오, 단일 비디오 참조 흐름
  * `aspectRatio`(`16:9`, `9:16`)와 `resolution`(`720P`, `1080P`)을 지원합니다. Veo는 현재 오디오 출력을 지원하지 않습니다.
  * 지원 기간: **4, 6 또는 8초**(다른 값은 허용되는 가장 가까운 값으로 맞춰짐)


Google을 기본 비디오 제공자로 사용하려면:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",      },    },  },}
[/code]

## 음악 생성

번들된 `google` Plugin은 공유 `music_generate` 도구를 통해 음악 생성도 등록합니다.

  * 기본 음악 모델: `google/lyria-3-clip-preview`
  * `google/lyria-3-pro-preview`도 지원
  * 프롬프트 제어: `lyrics` 및 `instrumental`
  * 출력 형식: 기본값은 `mp3`, `google/lyria-3-pro-preview`에서는 `wav`도 지원
  * 참조 입력: 최대 10개 이미지
  * 세션 기반 실행은 `action: "status"`를 포함한 공유 작업/상태 흐름을 통해 분리됩니다.


Google을 기본 음악 제공자로 사용하려면:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

## 텍스트 음성 변환

번들된 `google` 음성 제공자는 `gemini-3.1-flash-tts-preview`와 함께 Gemini API TTS 경로를 사용합니다.

  * 기본 음성: `Kore`
  * 인증: `messages.tts.providers.google.apiKey`, `models.providers.google.apiKey`, `GEMINI_API_KEY` 또는 `GOOGLE_API_KEY`
  * 출력: 일반 TTS 첨부 파일은 WAV, 음성 메모 대상은 Opus, Talk/전화 통신은 PCM
  * 음성 메모 출력: Google PCM은 WAV로 래핑되고 `ffmpeg`를 사용해 48 kHz Opus로 트랜스코딩됩니다.


Google의 배치 Gemini TTS 경로는 완료된 `generateContent` 응답에서 생성된 오디오를 반환합니다. 가장 낮은 지연 시간의 음성 대화에는 배치 TTS 대신 Gemini Live API가 지원하는 Google 실시간 음성 제공자를 사용하세요.

Google을 기본 TTS 제공자로 사용하려면:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "google",      providers: {        google: {          model: "gemini-3.1-flash-tts-preview",          voiceName: "Kore",          audioProfile: "Speak professionally with a calm tone.",        },      },    },  },}
[/code]

Gemini API TTS는 스타일 제어에 자연어 프롬프트를 사용합니다. 발화 텍스트 앞에 재사용 가능한 스타일 프롬프트를 추가하려면 `audioProfile`을 설정하세요. 프롬프트 텍스트가 이름이 지정된 화자를 참조할 때는 `speakerName`을 설정하세요.

Gemini API TTS는 텍스트 안의 `[whispers]` 또는 `[laughs]` 같은 표현형 대괄호 오디오 태그도 허용합니다. 태그를 TTS로 보내면서도 표시되는 채팅 답변에는 나타나지 않게 하려면 `[[tts:text]]...[[/tts:text]]` 블록 안에 넣으세요.

textCopy code
[code]
    Here is the clean reply text. [[tts:text]][whispers] Here is the spoken version.[[/tts:text]]
[/code]

## 실시간 음성

번들된 `google` Plugin은 Voice Call 및 Google Meet 같은 백엔드 오디오 브리지를 위해 Gemini Live API가 지원하는 실시간 음성 제공자를 등록합니다.

설정 | 구성 경로 | 기본값  
---|---|---  
모델 | `plugins.entries.voice-call.config.realtime.providers.google.model` | `gemini-2.5-flash-native-audio-preview-12-2025`  
음성 | `...google.voice` | `Kore`  
온도 | `...google.temperature` | (설정되지 않음)  
VAD 시작 민감도 | `...google.startSensitivity` | (설정되지 않음)  
VAD 종료 민감도 | `...google.endSensitivity` | (설정되지 않음)  
무음 지속 시간 | `...google.silenceDurationMs` | (설정되지 않음)  
활동 처리 | `...google.activityHandling` | Google 기본값, `start-of-activity-interrupts`  
턴 범위 | `...google.turnCoverage` | Google 기본값, `only-activity`  
자동 VAD 비활성화 | `...google.automaticActivityDetectionDisabled` | `false`  
세션 재개 | `...google.sessionResumption` | `true`  
컨텍스트 압축 | `...google.contextWindowCompression` | `true`  
API 키 | `...google.apiKey` | `models.providers.google.apiKey`, `GEMINI_API_KEY` 또는 `GOOGLE_API_KEY`로 대체됩니다  
  
Voice Call 실시간 구성 예:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          realtime: {            enabled: true,            provider: "google",            providers: {              google: {                model: "gemini-2.5-flash-native-audio-preview-12-2025",                voice: "Kore",                activityHandling: "start-of-activity-interrupts",                turnCoverage: "only-activity",              },            },          },        },      },    },  },}
[/code]

maintainer live verification의 경우 `OPENAI_API_KEY=... GEMINI_API_KEY=... node --import tsx scripts/dev/realtime-talk-live-smoke.ts`를 실행하세요. 이 smoke는 OpenAI 백엔드/WebRTC 경로도 포함합니다. Google 단계는 Control UI Talk에서 사용하는 것과 동일한 제한된 Live API 토큰 형태를 발급하고, 브라우저 WebSocket 엔드포인트를 열고, 초기 setup payload를 전송한 뒤 `setupComplete`를 기다립니다.

## 고급 구성

직접 Gemini 캐시 재사용

직접 Gemini API 실행(`api: "google-generative-ai"`)의 경우 OpenClaw는 구성된 `cachedContent` 핸들을 Gemini 요청으로 전달합니다.

  * 모델별 또는 전역 params를 `cachedContent` 또는 레거시 `cached_content` 중 하나로 구성합니다
  * 둘 다 있으면 `cachedContent`가 우선합니다
  * 예시 값: `cachedContents/prebuilt-context`
  * Gemini 캐시 적중 사용량은 업스트림 `cachedContentTokenCount`에서 OpenClaw `cacheRead`로 정규화됩니다

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "google/gemini-2.5-pro": {          params: {            cachedContent: "cachedContents/prebuilt-context",          },        },      },    },  },}
[/code]

Gemini CLI JSON 사용 참고 사항

`google-gemini-cli` OAuth provider를 사용할 때 OpenClaw는 CLI JSON 출력을 다음과 같이 정규화합니다.

  * 응답 텍스트는 CLI JSON `response` 필드에서 가져옵니다.
  * CLI가 `usage`를 비워 두면 사용량은 `stats`로 대체됩니다.
  * `stats.cached`는 OpenClaw `cacheRead`로 정규화됩니다.
  * `stats.input`이 없으면 OpenClaw는 `stats.input_tokens - stats.cached`에서 입력 토큰을 도출합니다.

환경 및 daemon 설정

Gateway가 daemon(launchd/systemd)으로 실행되는 경우 `GEMINI_API_KEY`가 해당 프로세스에서 사용할 수 있는지 확인하세요. 예를 들어 `~/.openclaw/.env`에 두거나 `env.shellEnv`를 통해 제공할 수 있습니다.

## 관련 항목

[**모델 선택** provider, 모델 ref, failover 동작 선택. ](</ko/concepts/model-providers>) [**이미지 생성** 공유 이미지 도구 매개변수와 provider 선택. ](</ko/tools/image-generation>) [**비디오 생성** 공유 비디오 도구 매개변수와 provider 선택. ](</ko/tools/video-generation>) [**음악 생성** 공유 음악 도구 매개변수와 provider 선택. ](</ko/tools/music-generation>)

Was this useful?YesNo