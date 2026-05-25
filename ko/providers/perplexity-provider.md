---
title: Perplexity
source_url: https://docs.openclaw.ai/ko/providers/perplexity-provider
scraped_at: 2026-05-25
---

Perplexity Plugin은 Perplexity Search API 또는 OpenRouter를 통한 Perplexity Sonar를 통해 웹 검색 기능을 제공합니다.

속성 | 값  
---|---  
유형 | 웹 검색 제공자(모델 제공자 아님)  
인증 | `PERPLEXITY_API_KEY`(직접) 또는 `OPENROUTER_API_KEY`(OpenRouter 경유)  
설정 경로 | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## 시작하기

* ### Set the API key

대화형 웹 검색 설정 흐름을 실행합니다.

bashCopy code
[code]
    openclaw configure --section web
[/code]

또는 키를 직접 설정합니다.

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### Start searching

키가 설정되면 에이전트가 웹 검색에 Perplexity를 자동으로 사용합니다. 추가 단계는 필요하지 않습니다.

## 검색 모드

Plugin은 API 키 접두사를 기준으로 전송 방식을 자동 선택합니다.

### Native Perplexity API (pplx-)

키가 `pplx-`로 시작하면 OpenClaw는 네이티브 Perplexity Search API를 사용합니다. 이 전송 방식은 구조화된 결과를 반환하고 도메인, 언어, 날짜 필터를 지원합니다(아래 필터링 옵션 참조).

### OpenRouter / Sonar (sk-or-)

키가 `sk-or-`로 시작하면 OpenClaw는 Perplexity Sonar 모델을 사용해 OpenRouter를 통해 라우팅합니다. 이 전송 방식은 인용이 포함된 AI 합성 답변을 반환합니다.

키 접두사 | 전송 방식 | 기능  
---|---|---  
`pplx-` | 네이티브 Perplexity Search API | 구조화된 결과, 도메인/언어/날짜 필터  
`sk-or-` | OpenRouter(Sonar) | 인용이 포함된 AI 합성 답변  
  
## 네이티브 API 필터링

네이티브 Perplexity API를 사용할 때 검색은 다음 필터를 지원합니다.

필터 | 설명 | 예시  
---|---|---  
국가 | 2글자 국가 코드 | `us`, `de`, `jp`  
언어 | ISO 639-1 언어 코드 | `en`, `fr`, `zh`  
날짜 범위 | 최신성 기간 | `day`, `week`, `month`, `year`  
도메인 필터 | 허용 목록 또는 거부 목록(최대 20개 도메인) | `example.com`  
콘텐츠 예산 | 응답별/페이지별 토큰 제한 | `max_tokens`, `max_tokens_per_page`  
  
## 고급 설정

Environment variable for daemon processes

OpenClaw Gateway가 데몬(launchd/systemd)으로 실행되는 경우 해당 프로세스에서 `PERPLEXITY_API_KEY`를 사용할 수 있는지 확인하세요.

OpenRouter proxy setup

OpenRouter를 통해 Perplexity 검색을 라우팅하려면 네이티브 Perplexity 키 대신 `OPENROUTER_API_KEY`(접두사 `sk-or-`)를 설정하세요. OpenClaw는 접두사를 감지하고 Sonar 전송 방식으로 자동 전환합니다.

## 관련 항목

[**Perplexity search tool** 에이전트가 Perplexity 검색을 호출하고 결과를 해석하는 방식입니다. ](</ko/tools/perplexity-search>) [**Configuration reference** Plugin 항목을 포함한 전체 설정 참조입니다. ](</ko/gateway/configuration-reference>)

Was this useful?YesNo