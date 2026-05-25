---
title: Deepgram
source_url: https://docs.openclaw.ai/ko/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram은 speech-to-text API입니다. OpenClaw에서는 `tools.media.audio`를 통한 인바운드 오디오/음성 노트 transcription과 `plugins.entries.voice-call.config.streaming`을 통한 Voice Call 스트리밍 STT에 사용됩니다.

배치 transcription의 경우, OpenClaw는 전체 오디오 파일을 Deepgram에 업로드하고 transcript를 응답 파이프라인에 주입합니다(`{{Transcript}}` \+ `[Audio]` 블록). Voice Call 스트리밍의 경우, OpenClaw는 실시간 G.711 u-law 프레임을 Deepgram의 WebSocket `listen` 엔드포인트로 전달하고, Deepgram이 반환하는 partial 또는 final transcript를 내보냅니다.

상세 | 값  
---|---  
웹사이트 | [deepgram.com](<https://deepgram.com>)  
문서 | [developers.deepgram.com](<https://developers.deepgram.com>)  
인증 | `DEEPGRAM_API_KEY`  
기본 모델 | `nova-3`  
  
## 시작하기

* ### API 키 설정

Deepgram API 키를 환경 변수에 추가하세요:

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### 오디오 provider 활성화

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### 음성 노트 보내기

연결된 아무 채널에서나 오디오 메시지를 보내세요. OpenClaw가 이를 Deepgram으로 transcription한 뒤 transcript를 응답 파이프라인에 주입합니다.

## 구성 옵션

옵션 | 경로 | 설명  
---|---|---  
`model` | `tools.media.audio.models[].model` | Deepgram 모델 id (기본값: `nova-3`)  
`language` | `tools.media.audio.models[].language` | 언어 힌트 (선택 사항)  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | 언어 감지 활성화 (선택 사항)  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | 문장 부호 활성화 (선택 사항)  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | 스마트 서식 활성화 (선택 사항)  
  
### 언어 힌트 포함

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### Deepgram 옵션 포함

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## Voice Call 스트리밍 STT

번들 `deepgram` Plugin은 Voice Call Plugin용 실시간 transcription provider도 등록합니다.

설정 | config 경로 | 기본값  
---|---|---  
API 키 | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | `DEEPGRAM_API_KEY`로 폴백  
모델 | `...deepgram.model` | `nova-3`  
언어 | `...deepgram.language` | (unset)  
인코딩 | `...deepgram.encoding` | `mulaw`  
샘플 레이트 | `...deepgram.sampleRate` | `8000`  
Endpointing | `...deepgram.endpointingMs` | `800`  
Interim 결과 | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## 참고

인증

인증은 표준 provider auth 순서를 따릅니다. 가장 간단한 경로는 `DEEPGRAM_API_KEY`입니다.

프록시 및 사용자 지정 엔드포인트

proxy를 사용하는 경우 `tools.media.audio.baseUrl`과 `tools.media.audio.headers`로 엔드포인트나 헤더를 override하세요.

출력 동작

출력은 다른 provider와 동일한 오디오 규칙(크기 제한, 타임아웃, transcript 주입)을 따릅니다.

## 관련 항목

[**미디어 도구** 오디오, 이미지, 비디오 처리 파이프라인 개요. ](</ko/tools/media-overview>) [**구성** 미디어 도구 설정을 포함한 전체 config 참조. ](</ko/gateway/configuration>) [**문제 해결** 일반적인 문제와 디버깅 단계. ](</ko/help/troubleshooting>) [**FAQ** OpenClaw 설정에 관한 자주 묻는 질문. ](</ko/help/faq>)

Was this useful?YesNo