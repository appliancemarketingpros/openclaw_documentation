---
title: 상태
source_url: https://docs.openclaw.ai/ko/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

실행 중인 Gateway에서 상태를 가져옵니다.

## 옵션

플래그 | 기본값 | 설명  
---|---|---  
`--json` | `false` | 텍스트 대신 기계가 읽을 수 있는 JSON을 출력합니다.  
`--timeout <ms>` | `10000` | 연결 제한 시간(밀리초)입니다.  
`--verbose` | `false` | 자세한 로깅입니다. 실시간 프로브를 강제하고 에이전트별 출력을 확장합니다.  
`--debug` | `false` | `--verbose`의 별칭입니다.  
  
예시:

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

참고:

  * 기본 `openclaw health`는 실행 중인 Gateway에 상태 스냅샷을 요청합니다. Gateway에 이미 최신 캐시 스냅샷이 있으면 캐시된 페이로드를 반환하고 백그라운드에서 새로 고칠 수 있습니다.
  * `--verbose`는 실시간 프로브를 강제하고, Gateway 연결 세부 정보를 출력하며, 사람이 읽을 수 있는 출력을 구성된 모든 계정과 에이전트로 확장합니다.
  * 여러 에이전트가 구성된 경우 출력에는 에이전트별 세션 저장소가 포함됩니다.


## 관련

  * [CLI 참조](</ko/cli>)
  * [Gateway 상태](</ko/gateway/health>)


Was this useful?YesNo