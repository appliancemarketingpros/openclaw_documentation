---
title: Z.AI
source_url: https://docs.openclaw.ai/ko/providers/zai
scraped_at: 2026-05-25
---

Z.AI는 **GLM** 모델용 API 플랫폼입니다. GLM용 REST API를 제공하며 인증에는 API 키를 사용합니다. [Z.AI](<http://Z.AI>) 콘솔에서 API 키를 생성하세요. OpenClaw는 [Z.AI](<http://Z.AI>) API 키와 함께 `zai` provider를 사용합니다.

  * Provider: `zai`
  * Auth: `ZAI_API_KEY`
  * API: [Z.AI](<http://Z.AI>) Chat Completions (Bearer auth)


## 시작하기

### 엔드포인트 자동 감지

**권장 대상:** 대부분의 사용자. OpenClaw는 키에서 일치하는 [Z.AI](<http://Z.AI>) 엔드포인트를 감지하고 올바른 기본 URL을 자동으로 적용합니다.

* ### 온보딩 실행

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### 기본 모델 설정

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### 모델이 목록에 표시되는지 확인

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### 명시적 지역 엔드포인트

**권장 대상:** 특정 Coding Plan 또는 일반 API 표면을 강제로 사용하려는 사용자.

* ### 올바른 온보딩 선택지 고르기

bashCopy code
[code]
    # Coding Plan Global (Coding Plan 사용자에게 권장)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (중국 지역)openclaw onboard --auth-choice zai-coding-cn # 일반 APIopenclaw onboard --auth-choice zai-global # 일반 API CN (중국 지역)openclaw onboard --auth-choice zai-cn
[/code]

* ### 기본 모델 설정

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### 모델이 목록에 표시되는지 확인

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## 기본 제공 카탈로그

OpenClaw는 Plugin 매니페스트에 번들된 `zai` provider 카탈로그를 포함하므로, 읽기 전용 목록 표시에서 provider 런타임을 로드하지 않고도 알려진 GLM 행을 표시할 수 있습니다.

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

매니페스트 기반 카탈로그에는 현재 다음이 포함됩니다.

모델 참조 | 참고  
---|---  
`zai/glm-5.1` | 기본 모델  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## 고급 구성

알 수 없는 GLM-5 모델의 전방 해석

알 수 없는 `glm-5*` ID도 현재 GLM-5 제품군 형태와 일치하면 `glm-4.7` 템플릿에서 provider 소유 메타데이터를 합성하여 번들 provider 경로에서 계속 전방 해석됩니다.

도구 호출 스트리밍

[Z.AI](<http://Z.AI>) 도구 호출 스트리밍에는 기본적으로 `tool_stream`이 활성화됩니다. 비활성화하려면:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

사고 및 보존된 사고

[Z.AI](<http://Z.AI>) 사고는 OpenClaw의 `/think` 제어를 따릅니다. 사고가 꺼져 있으면 OpenClaw는 표시 텍스트보다 먼저 `reasoning_content`에 출력 예산을 쓰는 응답을 피하기 위해 `thinking: { type: "disabled" }`를 보냅니다.

보존된 사고는 Z.AI가 전체 과거 `reasoning_content`를 다시 재생하도록 요구하여 프롬프트 토큰이 늘어나므로 옵트인 방식입니다. 모델별로 활성화하세요.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.1": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

활성화되어 있고 사고가 켜져 있으면 OpenClaw는 `thinking: { type: "enabled", clear_thinking: false }`를 보내고 동일한 OpenAI 호환 transcript에 대해 이전 `reasoning_content`를 다시 재생합니다.

고급 사용자는 여전히 `params.extra_body.thinking`으로 정확한 provider 페이로드를 재정의할 수 있습니다.

이미지 이해

번들 [Z.AI](<http://Z.AI>) Plugin은 이미지 이해를 등록합니다.

속성 | 값  
---|---  
모델 | `glm-4.6v`  
  
이미지 이해는 구성된 [Z.AI](<http://Z.AI>) 인증에서 자동으로 해석되므로 추가 구성이 필요하지 않습니다.

인증 세부 정보

  * Z.AI는 API 키와 함께 Bearer auth를 사용합니다.
  * `zai-api-key` 온보딩 선택지는 키 접두사에서 일치하는 [Z.AI](<http://Z.AI>) 엔드포인트를 자동 감지합니다.
  * 특정 API 표면을 강제로 사용하려면 명시적 지역 선택지(`zai-coding-global`, `zai-coding-cn`, `zai-global`, `zai-cn`)를 사용하세요.


## 관련 항목

[**GLM 모델 제품군** GLM의 모델 제품군 개요입니다. ](</ko/providers/glm>) [**모델 선택** provider, 모델 참조, 장애 조치 동작 선택. ](</ko/concepts/model-providers>)

Was this useful?YesNo