---
title: Vydra
source_url: https://docs.openclaw.ai/ko/providers/vydra
scraped_at: 2026-05-25
---

번들된 Vydra Plugin은 다음을 추가합니다.

  * `vydra/grok-imagine`을 통한 이미지 생성
  * `vydra/veo3` 및 `vydra/kling`을 통한 동영상 생성
  * Vydra의 ElevenLabs 기반 TTS 경로를 통한 음성 합성


OpenClaw는 세 기능 모두에 동일한 `VYDRA_API_KEY`를 사용합니다.

속성 | 값  
---|---  
공급자 id | `vydra`  
Plugin | 번들됨, `enabledByDefault: true`  
인증 env var | `VYDRA_API_KEY`  
온보딩 플래그 | `--auth-choice vydra-api-key`  
직접 CLI 플래그 | `--vydra-api-key <key>`  
계약 | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
기본 URL | `https://www.vydra.ai/api/v1` (`www` 호스트 사용)  
  
## 설정

* ### 대화형 온보딩 실행

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

또는 env var를 직접 설정합니다.

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### 기본 기능 선택

아래 기능(이미지, 동영상 또는 음성) 중 하나 이상을 선택하고 일치하는 구성을 적용합니다.

## 기능

이미지 생성

기본 이미지 모델:

  * `vydra/grok-imagine`


기본 이미지 공급자로 설정합니다.

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

현재 번들 지원은 텍스트-이미지 변환만 제공합니다. Vydra의 호스팅된 편집 경로는 원격 이미지 URL을 기대하며, OpenClaw는 아직 번들된 Plugin에 Vydra 전용 업로드 브리지를 추가하지 않습니다.

동영상 생성

등록된 동영상 모델:

  * 텍스트-동영상 변환용 `vydra/veo3`
  * 이미지-동영상 변환용 `vydra/kling`


Vydra를 기본 동영상 공급자로 설정합니다.

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

참고:

  * `vydra/veo3`은 텍스트-동영상 변환 전용으로 번들되어 있습니다.
  * `vydra/kling`은 현재 원격 이미지 URL 참조가 필요합니다. 로컬 파일 업로드는 사전에 거부됩니다.
  * Vydra의 현재 `kling` HTTP 경로는 `image_url` 또는 `video_url` 중 무엇을 요구하는지 일관되지 않았습니다. 번들된 공급자는 동일한 원격 이미지 URL을 두 필드 모두에 매핑합니다.
  * 번들된 Plugin은 보수적으로 동작하며 종횡비, 해상도, 워터마크 또는 생성된 오디오 같은 문서화되지 않은 스타일 조정값을 전달하지 않습니다.

동영상 라이브 테스트

공급자별 라이브 커버리지:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

번들된 Vydra 라이브 파일은 이제 다음을 다룹니다.

  * `vydra/veo3` 텍스트-동영상 변환
  * 원격 이미지 URL을 사용하는 `vydra/kling` 이미지-동영상 변환


필요할 때 원격 이미지 픽스처를 재정의합니다.

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

음성 합성

Vydra를 음성 공급자로 설정합니다.

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          voiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

기본값:

  * 모델: `elevenlabs/tts`
  * 음성 id: `21m00Tcm4TlvDq8ikWAM`


번들된 Plugin은 현재 검증된 기본 음성 하나를 노출하며 MP3 오디오 파일을 반환합니다.

## 관련 항목

[**공급자 디렉터리** 사용 가능한 모든 공급자를 살펴봅니다. ](</ko/providers>) [**이미지 생성** 공유 이미지 도구 매개변수 및 공급자 선택. ](</ko/tools/image-generation>) [**동영상 생성** 공유 동영상 도구 매개변수 및 공급자 선택. ](</ko/tools/video-generation>) [**구성 참조** 에이전트 기본값 및 모델 구성. ](</ko/gateway/config-agents#agent-defaults>)

Was this useful?YesNo