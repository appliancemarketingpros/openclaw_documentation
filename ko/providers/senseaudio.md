---
title: SenseAudio
source_url: https://docs.openclaw.ai/ko/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio는 OpenClaw의 공유 `tools.media.audio` 파이프라인을 통해 수신 오디오 및 음성 메모 첨부 파일을 전사할 수 있습니다. OpenClaw는 멀티파트 오디오를 OpenAI 호환 전사 엔드포인트에 게시하고, 반환된 텍스트를 `{{Transcript}}` 및 `[Audio]` 블록으로 삽입합니다.

속성 | 값  
---|---  
공급자 id | `senseaudio`  
Plugin | 번들 포함, `enabledByDefault: true`  
계약 | `mediaUnderstandingProviders`(오디오)  
인증 환경 변수 | `SENSEAUDIO_API_KEY`  
기본 모델 | `senseaudio-asr-pro-1.5-260319`  
기본 URL | `https://api.senseaudio.cn/v1`  
웹사이트 | [senseaudio.cn](<https://senseaudio.cn>)  
문서 | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## 시작하기

* ### API 키 설정

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### 오디오 공급자 활성화

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### 음성 메모 전송

연결된 채널을 통해 오디오 메시지를 보냅니다. OpenClaw는 오디오를 SenseAudio에 업로드하고 응답 파이프라인에서 전사문을 사용합니다.

## 옵션

옵션 | 경로 | 설명  
---|---|---  
`model` | `tools.media.audio.models[].model` | SenseAudio ASR 모델 id  
`language` | `tools.media.audio.models[].language` | 선택적 언어 힌트  
`prompt` | `tools.media.audio.prompt` | 선택적 전사 프롬프트  
`baseUrl` | `tools.media.audio.baseUrl` 또는 모델 | OpenAI 호환 기본 주소 재정의  
`headers` | `tools.media.audio.request.headers` | 추가 요청 헤더  
  
## 관련 항목

  * [미디어 이해(오디오)](</ko/nodes/audio>)
  * [모델 공급자](</ko/concepts/model-providers>)


Was this useful?YesNo