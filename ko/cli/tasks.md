---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/ko/cli/tasks
scraped_at: 2026-05-25
---

영속적인 백그라운드 작업과 Task Flow 상태를 검사합니다. 하위 명령이 없으면 `openclaw tasks`는 `openclaw tasks list`와 동일합니다.

수명 주기 및 전달 모델은 [백그라운드 작업](</ko/automation/tasks>)을 참조하세요.

## 사용법

bashCopy code
[code]
    openclaw tasksopenclaw tasks listopenclaw tasks list --runtime acpopenclaw tasks list --status runningopenclaw tasks show <lookup>openclaw tasks notify <lookup> state_changesopenclaw tasks cancel <lookup>openclaw tasks auditopenclaw tasks maintenanceopenclaw tasks maintenance --applyopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## 루트 옵션

  * `--json`: JSON을 출력합니다.
  * `--runtime <name>`: 종류별로 필터링합니다: `subagent`, `acp`, `cron`, 또는 `cli`.
  * `--status <name>`: 상태별로 필터링합니다: `queued`, `running`, `succeeded`, `failed`, `timed_out`, `cancelled`, 또는 `lost`.


## 하위 명령

### `list`

bashCopy code
[code]
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
[/code]

추적 중인 백그라운드 작업을 최신순으로 나열합니다.

### `show`

bashCopy code
[code]
    openclaw tasks show <lookup> [--json]
[/code]

작업 ID, 실행 ID 또는 세션 키로 작업 하나를 표시합니다.

### `notify`

bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

실행 중인 작업의 알림 정책을 변경합니다.

### `cancel`

bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

실행 중인 백그라운드 작업을 취소합니다.

### `audit`

bashCopy code
[code]
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
[/code]

오래되었거나, 유실되었거나, 전달에 실패했거나, 그 밖에 일관성이 없는 작업 및 Task Flow 레코드를 드러냅니다. `cleanupAfter`까지 유지되는 유실 작업은 경고이며, 만료되었거나 스탬프가 없는 유실 작업은 오류입니다.

### `maintenance`

bashCopy code
[code]
    openclaw tasks maintenance [--apply] [--json]
[/code]

작업 및 Task Flow 조정, 정리 스탬핑, 가지치기, 오래된 cron 실행 세션 레지스트리 정리를 미리 보거나 적용합니다. cron 작업의 경우, 조정은 오래된 활성 작업을 `lost`로 표시하기 전에 영구 저장된 실행 로그/작업 상태를 사용하므로, 완료된 cron 실행은 인메모리 Gateway 런타임 상태가 사라졌다는 이유만으로 잘못된 감사 오류가 되지 않습니다. 오프라인 CLI 감사는 Gateway의 프로세스 로컬 cron 활성 작업 집합에 대한 권위 있는 정보가 아닙니다. 실행 ID/소스 ID가 있는 CLI 작업은 오래된 하위 세션 행이 남아 있더라도 실시간 Gateway 실행 컨텍스트가 사라지면 `lost`로 표시됩니다. 적용하면 maintenance는 현재 실행 중인 cron 작업을 보존하고 cron이 아닌 세션 행은 그대로 둔 채, 7일보다 오래된 `cron:<jobId>:run:<uuid>` 세션 레지스트리 행도 가지치기합니다.

### `flow`

bashCopy code
[code]
    openclaw tasks flow list [--status <name>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

작업 원장 아래의 영속적인 Task Flow 상태를 검사하거나 취소합니다.

## 관련 항목

  * [CLI 참조](</ko/cli>)
  * [백그라운드 작업](</ko/automation/tasks>)


Was this useful?YesNo