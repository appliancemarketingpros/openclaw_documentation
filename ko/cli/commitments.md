---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/ko/cli/commitments
scraped_at: 2026-05-25
---

후속 추론 약속을 나열하고 관리합니다.

약속은 대화 맥락에서 생성되는, 사용자가 동의한 단기 후속 메모리입니다. 개념 안내서는 [추론된 약속](</ko/concepts/commitments>)을 참조하세요.

하위 명령 없이 `openclaw commitments`를 실행하면 대기 중인 약속이 나열됩니다.

## 사용법

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## 옵션

  * `--all`: 대기 중인 약속만이 아니라 모든 상태를 표시합니다.
  * `--agent <id>`: 하나의 에이전트 ID로 필터링합니다.
  * `--status <status>`: 상태별로 필터링합니다. 값: `pending`, `sent`, `dismissed`, `snoozed` 또는 `expired`.
  * `--json`: 기계가 읽을 수 있는 JSON을 출력합니다.


## 예시

대기 중인 약속 나열:

bashCopy code
[code]
    openclaw commitments
[/code]

저장된 모든 약속 나열:

bashCopy code
[code]
    openclaw commitments --all
[/code]

하나의 에이전트로 필터링:

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

일시 중지된 약속 찾기:

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

하나 이상의 약속 해제:

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

JSON으로 내보내기:

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## 출력

텍스트 출력에는 다음이 포함됩니다.

  * 약속 ID
  * 상태
  * 종류
  * 가장 이른 기한
  * 범위
  * 제안된 확인 메시지


JSON 출력에는 약속 저장소 경로와 저장된 전체 레코드도 포함됩니다.

## 관련 항목

  * [추론된 약속](</ko/concepts/commitments>)
  * [메모리 개요](</ko/concepts/memory>)
  * [Heartbeat](</ko/gateway/heartbeat>)
  * [예약된 작업](</ko/automation/cron-jobs>)


Was this useful?YesNo