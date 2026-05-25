---
title: Cloudflare AI Gateway
source_url: https://docs.openclaw.ai/ko/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

Cloudflare AI Gateway는 제공자 API 앞단에 위치하여 분석, 캐싱, 제어 기능을 추가할 수 있게 해줍니다. Anthropic의 경우 OpenClaw는 Gateway 엔드포인트를 통해 Anthropic Messages API를 사용합니다.

속성 | 값  
---|---  
제공자 | `cloudflare-ai-gateway`  
기본 URL | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
기본 모델 | `cloudflare-ai-gateway/claude-sonnet-4-6`  
API 키 | `CLOUDFLARE_AI_GATEWAY_API_KEY` (Gateway를 통한 요청에 사용하는 제공자 API 키)  
  
Anthropic Messages 모델에서 thinking이 활성화된 경우, OpenClaw는 Cloudflare AI Gateway를 통해 페이로드를 보내기 전에 끝부분의 assistant prefill 턴을 제거합니다. Anthropic은 extended thinking과 함께 response prefilling을 거부하지만, 일반적인 non-thinking prefill은 계속 사용할 수 있습니다.

## 시작하기

* ### 제공자 API 키와 Gateway 세부 정보 설정

온보딩을 실행하고 Cloudflare AI Gateway 인증 옵션을 선택합니다.

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

계정 ID, Gateway ID, API 키를 입력하라는 메시지가 표시됩니다.

* ### 기본 모델 설정

OpenClaw 구성에 모델을 추가합니다.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### 모델을 사용할 수 있는지 확인

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## 비대화형 예시

스크립트 또는 CI 설정에서는 모든 값을 명령줄에 전달합니다.

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## 고급 구성

인증된 Gateway

Cloudflare에서 Gateway 인증을 활성화한 경우 `cf-aig-authorization` 헤더를 추가합니다. 이는 제공자 API 키에 **추가로** 필요합니다.

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

환경 참고 사항

Gateway가 데몬(launchd/systemd)으로 실행되는 경우 해당 프로세스에서 `CLOUDFLARE_AI_GATEWAY_API_KEY`를 사용할 수 있는지 확인하세요.

## 관련 항목

[**모델 선택** 제공자, 모델 참조, 장애 조치 동작을 선택합니다. ](</ko/concepts/model-providers>) [**문제 해결** 일반적인 문제 해결 및 FAQ입니다. ](</ko/help/troubleshooting>)

Was this useful?YesNo