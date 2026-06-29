---
title: Skill 워크숍
source_url: https://docs.openclaw.ai/ko/tools/skill-workshop
scraped_at: 2026-06-29
---

CapabilitiesSkills

Skill Workshop은 워크스페이스 Skills를 만들고 업데이트하기 위한 OpenClaw의 관리된 경로입니다.

에이전트와 운영자는 이 경로를 통해 활성 `SKILL.md` 파일을 직접 작성하지 않습니다. 먼저 **제안** 을 만듭니다. 제안은 제안된 skill 콘텐츠, 대상 바인딩, 스캐너 상태, 해시, 지원 파일 메타데이터, 롤백 메타데이터를 포함하는 보류 중인 초안입니다. 적용될 때만 실제 skill이 됩니다.

Skill Workshop은 워크스페이스 Skills만 작성합니다. 번들, Plugin, ClawHub, 추가 루트, 관리형, 개인 에이전트 또는 시스템 Skills는 변경하지 않습니다.

## 작동 방식

  * **제안 먼저:** 생성된 skill 콘텐츠는 `SKILL.md`가 아니라 `PROPOSAL.md`로 저장됩니다.
  * **적용만 실제 쓰기:** 만들기, 업데이트, 수정은 활성 Skills를 변경하지 않습니다.
  * **워크스페이스 범위:** 생성 대상은 워크스페이스 `skills/` 루트입니다. 업데이트는 쓰기 가능한 워크스페이스 Skills에만 허용됩니다.
  * **덮어쓰기 없음:** 대상 skill이 이미 있으면 생성이 실패합니다.
  * **해시 바인딩:** 업데이트 제안은 현재 대상 해시에 바인딩되며, 적용 전에 실제 skill이 변경되면 오래된 상태가 됩니다.
  * **스캐너 게이트:** 적용은 쓰기 전에 스캔을 다시 실행합니다.
  * **복구 가능:** 적용은 실제 파일을 변경하기 전에 롤백 메타데이터를 작성합니다.
  * **일관된 표면:** 채팅, CLI, Gateway는 모두 동일한 Skill Workshop 서비스를 호출합니다.


## 수명 주기

textCopy code
[code]
    create/update -> pendingrevise        -> pendingapply         -> appliedreject        -> rejectedquarantine    -> quarantinedtarget change -> stale
[/code]

`pending` 제안만 수정, 적용, 거부 또는 격리할 수 있습니다.

## 채팅

원하는 skill을 에이전트에게 요청하세요. 에이전트는 `skill_workshop`을 호출하고 제안 ID를 반환합니다.

생성:

textCopy code
[code]
    Make a skill called morning-catchup that runs my Monday inbox routine.
[/code]

기존 워크스페이스 skill 업데이트:

textCopy code
[code]
    Update trip-planning to also check seat maps before booking.
[/code]

보류 중인 제안 반복 작업:

textCopy code
[code]
    Show me the morning-catchup proposal.Revise it to also flag anything marked urgent.Apply the morning-catchup proposal.
[/code]

기본적으로 에이전트가 시작한 `apply`, `reject`, `quarantine`은 실행 전에 승인 프롬프트를 표시합니다. 신뢰할 수 있는 환경에서 프롬프트를 건너뛰려면 `skills.workshop.approvalPolicy`를 `"auto"`로 설정하세요.

## CLI

새 skill 제안 생성:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name morning-catchup \  --description "Daily inbox catch-up: triage, archive, surface, draft, plan" \  --proposal ./PROPOSAL.md
[/code]

기존 워크스페이스 skill에 대한 업데이트 제안 생성:

bashCopy code
[code]
    openclaw skills workshop propose-update trip-planning --proposal ./PROPOSAL.md
[/code]

목록 조회 및 검사:

bashCopy code
[code]
    openclaw skills workshop listopenclaw skills workshop inspect <proposal-id>
[/code]

승인 전 수정:

bashCopy code
[code]
    openclaw skills workshop revise <proposal-id> --proposal ./PROPOSAL.md
[/code]

제안 마무리:

bashCopy code
[code]
    openclaw skills workshop apply <proposal-id>openclaw skills workshop reject <proposal-id> --reason "Duplicate"openclaw skills workshop quarantine <proposal-id> --reason "Needs security review"
[/code]

## 제안 콘텐츠

보류 중일 때 제안은 제안 전용 frontmatter가 있는 `PROPOSAL.md`로 저장됩니다.

markdownCopy code
[code]
    ---name: "morning-catchup"description: "Daily inbox catch-up: triage, archive, surface, draft, plan"status: proposalversion: "v1"date: "2026-05-30T00:00:00.000Z"---
[/code]

적용 시 Skill Workshop은 활성 `SKILL.md`를 작성하고 제안 전용 필드인 `status`, 제안 `version`, 제안 `date`를 제거합니다.

## 지원 파일

제안된 skill에 `PROPOSAL.md` 옆 파일이 필요한 경우 `--proposal-dir`을 사용하세요.

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name weekly-update \  --description "Friday wrap-up: stats, highlights, next week's top three" \  --proposal-dir ./weekly-update-proposal
[/code]

디렉터리에는 `PROPOSAL.md`가 포함되어야 합니다. 지원 파일은 다음 아래에 있어야 합니다.

  * `assets/`
  * `examples/`
  * `references/`
  * `scripts/`
  * `templates/`


Skill Workshop은 지원 파일을 스캔하고 해시한 뒤 제안과 함께 저장합니다. 이 파일들은 적용 시에만 실제 `SKILL.md` 옆에 작성됩니다.

거부되는 지원 파일 경로에는 절대 경로, 숨김 경로 세그먼트, 경로 순회, 겹치는 경로, 제안 디렉터리의 실행 파일, 비 UTF-8 텍스트, 널 바이트, 표준 지원 폴더 밖의 파일이 포함됩니다.

## 에이전트 도구

모델은 `skill_workshop`을 사용합니다.

textCopy code
[code]
    action: create | update | revise | list | inspect | apply | reject | quarantine
[/code]

에이전트는 생성된 skill 작업에 `skill_workshop`을 사용해야 합니다. `write`, `edit`, `exec`, 셸 명령 또는 직접 파일 시스템 작업을 통해 제안 파일을 생성하거나 변경해서는 안 됩니다.

## 승인 및 자율성

json5Copy code
[code]
    {  skills: {    workshop: {      autonomous: {        enabled: false,      },      allowSymlinkTargetWrites: false,      approvalPolicy: "pending",      maxPending: 50,      maxSkillBytes: 40000,    },  },}
[/code]

  * `autonomous.enabled`: 성공적인 턴 이후 지속적인 대화 신호를 바탕으로 OpenClaw가 보류 중인 제안을 만들 수 있게 합니다. 기본값: `false`.
  * `allowSymlinkTargetWrites`: 실제 대상이 `skills.load.allowSymlinkTargets`에 나열된 워크스페이스 skill 심볼릭 링크를 통해 적용이 쓰기 작업을 수행할 수 있게 합니다. 기본값: `false`.
  * `approvalPolicy: "pending"`: 에이전트가 시작한 `apply`, `reject`, `quarantine` 전에 승인 프롬프트가 필요합니다.
  * `approvalPolicy: "auto"`: 해당 승인 프롬프트를 건너뜁니다. 에이전트는 여전히 작업을 호출해야 합니다.
  * `maxPending`: 워크스페이스당 보류 중 및 격리된 제안 수를 제한합니다.
  * `maxSkillBytes`: 제안 본문 크기를 제한합니다. 기본값: `40000`.


제안 설명은 항상 160바이트로 제한됩니다.

## Gateway 메서드

textCopy code
[code]
    skills.proposals.listskills.proposals.inspectskills.proposals.createskills.proposals.updateskills.proposals.reviseskills.proposals.applyskills.proposals.rejectskills.proposals.quarantine
[/code]

읽기 전용 메서드에는 `operator.read`가 필요합니다. 변경 메서드에는 `operator.admin`이 필요합니다.

## 스토리지

textCopy code
[code]
    &lt;OPENCLAW_STATE_DIR&gt;/skill-workshop/  proposals.json  proposals/<proposal-id>/    proposal.json    PROPOSAL.md    rollback.json    assets/    examples/    references/    scripts/    templates/
[/code]

기본 상태 디렉터리: `~/.openclaw`.

  * `proposal.json`: 표준 제안 레코드입니다.
  * `proposals.json`: 빠른 목록 인덱스이며, 제안 폴더에서 다시 빌드할 수 있습니다.
  * `PROPOSAL.md`: 보류 중인 skill 제안입니다.
  * `rollback.json`: 적용이 실제 파일을 변경하기 전에 작성되는 복구 메타데이터입니다.


## 제한

  * 설명: 160바이트.
  * 제안 본문: `skills.workshop.maxSkillBytes`(기본값 40,000).
  * 지원 파일: 제안당 64개.
  * 지원 파일 크기: 각각 256KB, 총 2MB.
  * 보류 중 및 격리된 제안: 워크스페이스당 `skills.workshop.maxPending`(기본값 50).


## 문제 해결

문제 | 해결 방법  
---|---  
`Skill proposal description is too large` | `description`을 160바이트 이하로 줄이세요.  
`Skill proposal content is too large` | 제안 본문을 줄이거나 `skills.workshop.maxSkillBytes`를 높이세요.  
`Target skill changed after proposal creation` | 현재 대상에 맞춰 제안을 수정하거나 새 제안을 만드세요.  
`Proposal scan failed` | 스캐너 결과를 검사한 다음 제안을 수정하거나 격리하세요.  
`untrusted symlink target` | 의도적인 공유 skill 루트에 대해서만 `skills.load.allowSymlinkTargets`를 구성하고 `skills.workshop.allowSymlinkTargetWrites`를 활성화하세요.  
`Support file paths must be under one of...` | 지원 파일을 `assets/`, `examples/`, `references/`, `scripts/` 또는 `templates/` 아래로 이동하세요.  
제안이 목록에 표시되지 않음 | 선택한 `--agent` 워크스페이스와 `OPENCLAW_STATE_DIR`을 확인하세요.  
에이전트가 `skill_workshop`을 호출할 수 없음 | 활성 도구 정책과 실행 모드를 확인하세요. `coding`에는 이 도구가 포함됩니다. 제한적인 `tools.allow` 정책은 이를 명시적으로 나열해야 하며, 샌드박스 실행은 일반 호스트 측 에이전트 세션 또는 CLI를 사용해야 합니다.  
  
## 관련 항목

  * 로드 순서, 우선순위, 가시성은 [Skills](</ko/tools/skills>)를 참조하세요
  * 손으로 작성한 `SKILL.md` 기본 사항은 [Skills 만들기](</ko/tools/creating-skills>)를 참조하세요
  * 전체 `skills.workshop` 스키마는 [Skills config](</ko/tools/skills-config>)를 참조하세요
  * `openclaw skills` 명령은 [Skills CLI](</ko/cli/skills>)를 참조하세요


Was this useful?YesNo

Open issue