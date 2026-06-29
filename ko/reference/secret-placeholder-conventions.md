---
title: 비밀 자리표시자 규칙
source_url: https://docs.openclaw.ai/ko/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# 비밀 값 자리표시자 규칙

실제 비밀 값처럼 보이지 않으면서 사람이 읽을 수 있는 자리표시자를 사용하세요.

## 권장 스타일

  * `example-openai-key-not-real` 또는 `example-discord-bot-token`처럼 설명적인 값을 선호하세요.
  * 셸 스니펫에서는 인라인 토큰처럼 보이는 문자열보다 `${OPENAI_API_KEY}`를 선호하세요.
  * 예시는 명백히 가짜이며 목적(제공자, 채널, 인증 유형)에 맞게 범위가 지정되도록 유지하세요.


## 문서에서 피해야 할 패턴

  * 리터럴 PEM 개인 키 헤더 또는 푸터 텍스트.
  * 실제 자격 증명처럼 보이는 접두사, 예: `sk-...`, `xoxb-...`, `AKIA...`.
  * 런타임 로그에서 복사한 실제처럼 보이는 bearer 토큰.


## 예시

bashCopy code
[code]
    # Goodexport OPENAI_API_KEY="example-openai-key-not-real" # Better (when the doc is about env wiring)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue