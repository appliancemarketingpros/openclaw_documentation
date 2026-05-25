---
title: 샌드박스 CLI
source_url: https://docs.openclaw.ai/ko/cli/sandbox
scraped_at: 2026-05-25
---

격리된 에이전트 실행을 위한 샌드박스 런타임을 관리합니다.

## 개요

OpenClaw는 보안을 위해 격리된 샌드박스 런타임에서 에이전트를 실행할 수 있습니다. `sandbox` 명령은 업데이트나 구성 변경 후 이러한 런타임을 점검하고 다시 생성하는 데 도움이 됩니다.

현재 이는 보통 다음을 의미합니다.

  * Docker 샌드박스 컨테이너
  * `agents.defaults.sandbox.backend = "ssh"`일 때 SSH 샌드박스 런타임
  * `agents.defaults.sandbox.backend = "openshell"`일 때 OpenShell 샌드박스 런타임


`ssh` 및 OpenShell `remote`의 경우, 다시 생성은 Docker보다 더 중요합니다.

  * 원격 워크스페이스는 초기 시드 이후 표준 원본입니다.
  * `openclaw sandbox recreate`는 선택한 범위의 해당 표준 원격 워크스페이스를 삭제합니다.
  * 다음 사용 시 현재 로컬 워크스페이스에서 다시 시드합니다.


## 명령

### `openclaw sandbox explain`

**유효한** 샌드박스 모드/범위/워크스페이스 액세스, 샌드박스 도구 정책, 승격 게이트를 점검합니다(수정용 구성 키 경로 포함).

bashCopy code
[code]
    openclaw sandbox explainopenclaw sandbox explain --session agent:main:mainopenclaw sandbox explain --agent workopenclaw sandbox explain --json
[/code]

### `openclaw sandbox list`

모든 샌드박스 런타임을 상태 및 구성과 함께 나열합니다.

bashCopy code
[code]
    openclaw sandbox listopenclaw sandbox list --browser  # List only browser containersopenclaw sandbox list --json     # JSON output
[/code]

**출력에 포함되는 항목:**

  * 런타임 이름 및 상태
  * 백엔드(`docker`, `openshell` 등)
  * 구성 레이블 및 현재 구성과 일치하는지 여부
  * 수명(생성 이후 경과 시간)
  * 유휴 시간(마지막 사용 이후 경과 시간)
  * 연결된 세션/에이전트


### `openclaw sandbox recreate`

업데이트된 구성으로 다시 생성되도록 샌드박스 런타임을 제거합니다.

bashCopy code
[code]
    openclaw sandbox recreate --all                # Recreate all containersopenclaw sandbox recreate --session main       # Specific sessionopenclaw sandbox recreate --agent mybot        # Specific agentopenclaw sandbox recreate --browser            # Only browser containersopenclaw sandbox recreate --all --force        # Skip confirmation
[/code]

**옵션:**

  * `--all`: 모든 샌드박스 컨테이너를 다시 생성
  * `--session <key>`: 특정 세션의 컨테이너를 다시 생성
  * `--agent <id>`: 특정 에이전트의 컨테이너를 다시 생성
  * `--browser`: 브라우저 컨테이너만 다시 생성
  * `--force`: 확인 프롬프트 건너뛰기


## 사용 사례

### Docker 이미지를 업데이트한 후

bashCopy code
[code]
    # Pull new imagedocker pull openclaw-sandbox:latestdocker tag openclaw-sandbox:latest openclaw-sandbox:bookworm-slim # Update config to use new image# Edit config: agents.defaults.sandbox.docker.image (or agents.list[].sandbox.docker.image) # Recreate containersopenclaw sandbox recreate --all
[/code]

### 샌드박스 구성을 변경한 후

bashCopy code
[code]
    # Edit config: agents.defaults.sandbox.* (or agents.list[].sandbox.*) # Recreate to apply new configopenclaw sandbox recreate --all
[/code]

### SSH 대상 또는 SSH 인증 자료를 변경한 후

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - agents.defaults.sandbox.ssh.target# - agents.defaults.sandbox.ssh.workspaceRoot# - agents.defaults.sandbox.ssh.identityFile / certificateFile / knownHostsFile# - agents.defaults.sandbox.ssh.identityData / certificateData / knownHostsData openclaw sandbox recreate --all
[/code]

핵심 `ssh` 백엔드의 경우, 다시 생성은 SSH 대상의 범위별 원격 워크스페이스 루트를 삭제합니다. 다음 실행 시 로컬 워크스페이스에서 다시 시드합니다.

### OpenShell 소스, 정책 또는 모드를 변경한 후

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - plugins.entries.openshell.config.from# - plugins.entries.openshell.config.mode# - plugins.entries.openshell.config.policy openclaw sandbox recreate --all
[/code]

OpenShell `remote` 모드의 경우, 다시 생성은 해당 범위의 표준 원격 워크스페이스를 삭제합니다. 다음 실행 시 로컬 워크스페이스에서 다시 시드합니다.

### setupCommand를 변경한 후

bashCopy code
[code]
    openclaw sandbox recreate --all# or just one agent:openclaw sandbox recreate --agent family
[/code]

### 특정 에이전트만 대상으로 하는 경우

bashCopy code
[code]
    # Update only one agent's containersopenclaw sandbox recreate --agent alfred
[/code]

## 이것이 필요한 이유

샌드박스 구성을 업데이트하면:

  * 기존 런타임은 이전 설정으로 계속 실행됩니다.
  * 런타임은 24시간 동안 비활성 상태인 후에만 정리됩니다.
  * 정기적으로 사용되는 에이전트는 이전 런타임을 계속 유지합니다.


`openclaw sandbox recreate`를 사용하여 이전 런타임을 강제로 제거하세요. 런타임은 다음에 필요할 때 현재 설정으로 자동으로 다시 생성됩니다.

## 레지스트리 마이그레이션

OpenClaw는 샌드박스 상태 디렉터리 아래에 컨테이너/브라우저 항목당 하나의 JSON 샤드로 샌드박스 런타임 메타데이터를 저장합니다. 이전 설치에는 여전히 단일형 레거시 파일이 있을 수 있습니다.

  * `~/.openclaw/sandbox/containers.json`
  * `~/.openclaw/sandbox/browsers.json`


일반 샌드박스 런타임 읽기는 해당 파일을 다시 쓰지 않습니다. 유효한 레거시 항목을 샤드 레지스트리 디렉터리로 마이그레이션하려면 `openclaw doctor --fix`를 실행하세요. 잘못된 레거시 파일은 격리되어 하나의 잘못된 이전 레지스트리가 현재 런타임 항목을 숨기지 못하게 합니다.

## 구성

샌드박스 설정은 `~/.openclaw/openclaw.json`의 `agents.defaults.sandbox` 아래에 있습니다(에이전트별 재정의는 `agents.list[].sandbox`에 둡니다).

jsoncCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "all", // off, non-main, all        "backend": "docker", // docker, ssh, openshell        "scope": "agent", // session, agent, shared        "docker": {          "image": "openclaw-sandbox:bookworm-slim",          "containerPrefix": "openclaw-sbx-",          // ... more Docker options        },        "prune": {          "idleHours": 24, // Auto-prune after 24h idle          "maxAgeDays": 7, // Auto-prune after 7 days        },      },    },  },}
[/code]

## 관련

  * [CLI 참조](</ko/cli>)
  * [샌드박싱](</ko/gateway/sandboxing>)
  * [에이전트 워크스페이스](</ko/concepts/agent-workspace>)
  * [Doctor](</ko/gateway/doctor>): 샌드박스 설정을 확인합니다.


Was this useful?YesNo