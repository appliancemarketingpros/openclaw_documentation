---
title: Qwen
source_url: https://docs.openclaw.ai/ko/providers/qwen
scraped_at: 2026-05-25
---

OpenClaw는 이제 Qwen을 정식 번들 Provider로 취급하며, 표준 id는 `qwen`입니다. 번들 Provider는 Qwen Cloud / Alibaba DashScope 및 Coding Plan 엔드포인트를 대상으로 하며, 레거시 `modelstudio` id가 호환성 별칭으로 계속 작동하도록 유지합니다.

  * Provider: `qwen`
  * 권장 env var: `QWEN_API_KEY`
  * 호환성을 위해 함께 허용됨: `MODELSTUDIO_API_KEY`, `DASHSCOPE_API_KEY`
  * API 스타일: OpenAI 호환


## 시작하기

플랜 유형을 선택하고 설정 단계를 따르세요.

### Coding Plan (구독)

**적합한 용도:** Qwen Coding Plan을 통한 구독 기반 액세스.

* ### API 키 가져오기

[home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>)에서 API 키를 만들거나 복사하세요.

* ### 온보딩 실행

**Global** 엔드포인트의 경우:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key
[/code]

**China** 엔드포인트의 경우:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key-cn
[/code]

* ### 기본 모델 설정

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### 모델을 사용할 수 있는지 확인

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

### Standard (사용량 기반 과금)

**적합한 용도:** Coding Plan에서 사용할 수 없을 수 있는 `qwen3.6-plus` 같은 모델을 포함하여 Standard Model Studio 엔드포인트를 통한 사용량 기반 과금 액세스.

* ### API 키 가져오기

[home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>)에서 API 키를 만들거나 복사하세요.

* ### 온보딩 실행

**Global** 엔드포인트의 경우:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key
[/code]

**China** 엔드포인트의 경우:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key-cn
[/code]

* ### 기본 모델 설정

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### 모델을 사용할 수 있는지 확인

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

## 플랜 유형과 엔드포인트

플랜 | 리전 | Auth choice | 엔드포인트  
---|---|---|---  
Standard (사용량 기반 과금) | China | `qwen-standard-api-key-cn` | `dashscope.aliyuncs.com/compatible-mode/v1`  
Standard (사용량 기반 과금) | Global | `qwen-standard-api-key` | `dashscope-intl.aliyuncs.com/compatible-mode/v1`  
Coding Plan (구독) | China | `qwen-api-key-cn` | `coding.dashscope.aliyuncs.com/v1`  
Coding Plan (구독) | Global | `qwen-api-key` | `coding-intl.dashscope.aliyuncs.com/v1`  
  
Provider는 auth choice에 따라 엔드포인트를 자동 선택합니다. 표준 선택지는 `qwen-*` 계열을 사용하며, `modelstudio-*`는 호환성 전용으로 남아 있습니다. config에서 사용자 지정 `baseUrl`로 재정의할 수 있습니다.

## 기본 제공 카탈로그

OpenClaw는 현재 이 번들 Qwen 카탈로그를 제공합니다. 구성된 카탈로그는 엔드포인트를 인식합니다. Coding Plan config는 Standard 엔드포인트에서만 작동하는 것으로 알려진 모델을 생략합니다.

모델 참조 | 입력 | 컨텍스트 | 참고  
---|---|---|---  
`qwen/qwen3.5-plus` | 텍스트, 이미지 | 1,000,000 | 기본 모델  
`qwen/qwen3.6-plus` | 텍스트, 이미지 | 1,000,000 | 이 모델이 필요하면 Standard 엔드포인트 권장  
`qwen/qwen3-max-2026-01-23` | 텍스트 | 262,144 | Qwen Max 라인  
`qwen/qwen3-coder-next` | 텍스트 | 262,144 | Coding  
`qwen/qwen3-coder-plus` | 텍스트 | 1,000,000 | Coding  
`qwen/MiniMax-M2.5` | 텍스트 | 1,000,000 | 추론 활성화  
`qwen/glm-5` | 텍스트 | 202,752 | GLM  
`qwen/glm-4.7` | 텍스트 | 202,752 | GLM  
`qwen/kimi-k2.5` | 텍스트, 이미지 | 262,144 | Alibaba를 통한 Moonshot AI  
  
## Thinking 제어

추론이 활성화된 Qwen Cloud 모델의 경우, 번들 Provider는 OpenClaw thinking 수준을 DashScope의 최상위 `enable_thinking` 요청 플래그에 매핑합니다. 비활성화된 thinking은 `enable_thinking: false`를 보내고, 다른 thinking 수준은 `enable_thinking: true`를 보냅니다.

## 멀티모달 애드온

`qwen` Plugin은 **Standard** DashScope 엔드포인트에서도 멀티모달 기능을 노출합니다(Coding Plan 엔드포인트는 제외).

  * `qwen-vl-max-latest`를 통한 **비디오 이해**
  * `wan2.6-t2v`(기본값), `wan2.6-i2v`, `wan2.6-r2v`, `wan2.6-r2v-flash`, `wan2.7-r2v`를 통한 **Wan 비디오 생성**


Qwen을 기본 비디오 Provider로 사용하려면:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: { primary: "qwen/wan2.6-t2v" },    },  },}
[/code]

## 고급 구성

이미지 및 비디오 이해

번들 Qwen Plugin은 **Standard** DashScope 엔드포인트에서 이미지와 비디오의 미디어 이해를 등록합니다(Coding Plan 엔드포인트는 제외).

속성 | 값  
---|---  
모델 | `qwen-vl-max-latest`  
지원 입력 | 이미지, 비디오  
  
미디어 이해는 구성된 Qwen auth에서 자동으로 해석되며, 추가 config는 필요하지 않습니다. 미디어 이해 지원을 위해 Standard (사용량 기반 과금) 엔드포인트를 사용하고 있는지 확인하세요.

Qwen 3.6 Plus 가용성

`qwen3.6-plus`는 Standard (사용량 기반 과금) Model Studio 엔드포인트에서 사용할 수 있습니다.

  * China: `dashscope.aliyuncs.com/compatible-mode/v1`
  * Global: `dashscope-intl.aliyuncs.com/compatible-mode/v1`


Coding Plan 엔드포인트가 `qwen3.6-plus`에 대해 "unsupported model" 오류를 반환하면 Coding Plan 엔드포인트/키 쌍 대신 Standard (사용량 기반 과금)로 전환하세요.

OpenClaw의 번들 Qwen 카탈로그는 Coding Plan 엔드포인트에서 `qwen3.6-plus`를 표시하지 않지만, `models.providers.qwen.models` 아래에 명시적으로 구성된 `qwen/qwen3.6-plus` 항목은 Coding Plan baseUrls에서 존중되므로 Aliyun이 구독에서 이 모델을 활성화하면 직접 선택할 수 있습니다. 호출 성공 여부는 여전히 upstream API가 결정합니다.

기능 계획

`qwen` Plugin은 코딩/텍스트 모델뿐 아니라 전체 Qwen Cloud 표면을 위한 벤더 홈으로 자리 잡고 있습니다.

  * **텍스트/채팅 모델:** 현재 번들 제공
  * **도구 호출, 구조화된 출력, thinking:** OpenAI 호환 전송에서 상속
  * **이미지 생성:** Provider-Plugin 레이어에서 계획됨
  * **이미지/비디오 이해:** Standard 엔드포인트에서 현재 번들 제공
  * **음성/오디오:** Provider-Plugin 레이어에서 계획됨
  * **Memory 임베딩/재랭킹:** 임베딩 어댑터 표면을 통해 계획됨
  * **비디오 생성:** 공유 비디오 생성 기능을 통해 현재 번들 제공

비디오 생성 세부 정보

비디오 생성의 경우, OpenClaw는 작업을 제출하기 전에 구성된 Qwen 리전을 일치하는 DashScope AIGC 호스트에 매핑합니다.

  * Global/Intl: `https://dashscope-intl.aliyuncs.com`
  * China: `https://dashscope.aliyuncs.com`


즉, Coding Plan 또는 Standard Qwen 호스트 중 하나를 가리키는 일반적인 `models.providers.qwen.baseUrl`도 비디오 생성을 올바른 리전별 DashScope 비디오 엔드포인트에 유지합니다.

현재 번들 Qwen 비디오 생성 제한:

  * 요청당 최대 **1** 개의 출력 비디오
  * 최대 **1** 개의 입력 이미지
  * 최대 **4** 개의 입력 비디오
  * 최대 **10초** 길이
  * `size`, `aspectRatio`, `resolution`, `audio`, `watermark` 지원
  * 참조 이미지/비디오 모드는 현재 **원격 http(s) URL** 이 필요합니다. DashScope 비디오 엔드포인트가 해당 참조에 대해 업로드된 로컬 버퍼를 허용하지 않기 때문에 로컬 파일 경로는 사전에 거부됩니다.

스트리밍 사용량 호환성

네이티브 Model Studio 엔드포인트는 공유 `openai-completions` 전송에서 스트리밍 사용량 호환성을 표시합니다. OpenClaw는 이제 이를 엔드포인트 기능을 기준으로 판단하므로, 동일한 네이티브 호스트를 대상으로 하는 DashScope 호환 사용자 지정 Provider id는 특정한 기본 제공 `qwen` Provider id가 필요하지 않고도 동일한 스트리밍 사용량 동작을 상속합니다.

네이티브 스트리밍 사용량 호환성은 Coding Plan 호스트와 Standard DashScope 호환 호스트 모두에 적용됩니다.

  * `https://coding.dashscope.aliyuncs.com/v1`
  * `https://coding-intl.dashscope.aliyuncs.com/v1`
  * `https://dashscope.aliyuncs.com/compatible-mode/v1`
  * `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`

멀티모달 엔드포인트 리전

멀티모달 표면(비디오 이해 및 Wan 비디오 생성)은 Coding Plan 엔드포인트가 아니라 **Standard** DashScope 엔드포인트를 사용합니다.

  * Global/Intl Standard 기본 URL: `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`
  * China Standard 기본 URL: `https://dashscope.aliyuncs.com/compatible-mode/v1`

환경 및 데몬 설정

Gateway가 데몬(launchd/systemd)으로 실행되는 경우 `QWEN_API_KEY`를 해당 프로세스에서 사용할 수 있는지 확인하세요(예: `~/.openclaw/.env` 또는 `env.shellEnv`를 통해).

## 관련 항목

[**모델 선택** 공급자, 모델 참조, 장애 조치 동작을 선택합니다. ](</ko/concepts/model-providers>) [**동영상 생성** 공유 동영상 도구 매개변수 및 공급자 선택입니다. ](</ko/tools/video-generation>) [**Alibaba (ModelStudio)** 기존 ModelStudio 공급자 및 마이그레이션 참고 사항입니다. ](</ko/providers/alibaba>) [**문제 해결** 일반적인 문제 해결 및 FAQ입니다. ](</ko/help/troubleshooting>)

Was this useful?YesNo