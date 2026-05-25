---
title: 대시보드
source_url: https://docs.openclaw.ai/ko/cli/dashboard
scraped_at: 2026-05-25
---

# `openclaw dashboard`

현재 인증을 사용하여 제어 UI를 엽니다.

bashCopy code
[code]
    openclaw dashboardopenclaw dashboard --no-open
[/code]

참고:

  * 가능한 경우 `dashboard`는 구성된 `gateway.auth.token` SecretRefs를 확인합니다.
  * `dashboard`는 `gateway.tls.enabled`를 따릅니다. TLS가 활성화된 Gateway는 `https://` 제어 UI URL을 출력/열고 `wss://`를 통해 연결합니다.
  * 토큰 인증된 dashboard URL의 클립보드/브라우저 전달에 실패하면, `dashboard`는 토큰 값을 출력하지 않고 `OPENCLAW_GATEWAY_TOKEN`, `gateway.auth.token`, 프래그먼트 키 `token`을 명시하는 안전한 수동 인증 힌트를 로그에 남깁니다.
  * SecretRef로 관리되는 토큰(확인되었거나 확인되지 않은 경우 모두)에 대해, `dashboard`는 터미널 출력, 클립보드 기록 또는 브라우저 실행 인수에 외부 비밀이 노출되지 않도록 토큰이 포함되지 않은 URL을 출력/복사/엽니다.
  * `gateway.auth.token`이 SecretRef로 관리되지만 이 명령 경로에서 확인되지 않은 경우, 이 명령은 유효하지 않은 토큰 자리표시자를 포함하는 대신 토큰이 포함되지 않은 URL과 명시적인 해결 안내를 출력합니다.


## 관련 항목

  * [CLI 참조](</ko/cli>)
  * [Dashboard](</ko/web/dashboard>)


Was this useful?YesNo