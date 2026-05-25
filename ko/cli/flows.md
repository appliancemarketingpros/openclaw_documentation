---
title: 플로우(리디렉션)
source_url: https://docs.openclaw.ai/ko/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

최상위 `openclaw flows` 명령은 없습니다. 영속적 TaskFlow 검사는 `openclaw tasks flow` 아래에 있습니다.

## 하위 명령

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

하위 명령 | 설명 | 인수 / 옵션  
---|---|---  
`list` | 추적 중인 TaskFlow를 나열합니다. | `--json` 기계 판독 가능 출력; `--status <name>` 필터(아래 상태 값 참조).  
`show` | 하나의 TaskFlow를 표시합니다. | `<lookup>` flow ID 또는 소유자 키; `--json` 기계 판독 가능 출력.  
`cancel` | 실행 중인 TaskFlow를 취소합니다. | `<lookup>` flow ID 또는 소유자 키.  
  
`<lookup>`은 flow ID(`list` / `show`에서 반환됨) 또는 flow의 소유자 키(flow를 추적하기 위해 소유 하위 시스템이 사용하는 안정적인 식별자)를 허용합니다.

### 상태 필터 값

`list`의 `--status`는 다음 중 하나를 허용합니다.

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## 예시

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

전체 TaskFlow 개념 및 작성 방법은 [TaskFlow](</ko/automation/taskflow>)를 참조하세요. 상위 `tasks` 명령은 [tasks CLI 참조](</ko/cli/tasks>)를 참조하세요.

## 관련 항목

  * [CLI 참조](</ko/cli>)
  * [자동화](</ko/automation>)
  * [TaskFlow](</ko/automation/taskflow>)


Was this useful?YesNo