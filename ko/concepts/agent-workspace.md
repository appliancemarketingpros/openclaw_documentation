---
title: 에이전트 작업 공간
source_url: https://docs.openclaw.ai/ko/concepts/agent-workspace
scraped_at: 2026-05-25
---

작업공간은 에이전트의 홈입니다. 파일 도구와 작업공간 컨텍스트에 사용되는 유일한 작업 디렉터리입니다. 비공개로 유지하고 메모리처럼 다루세요.

이는 구성, 자격 증명, 세션을 저장하는 `~/.openclaw/`와는 별개입니다.

## 기본 위치

  * 기본값: `~/.openclaw/workspace`
  * `OPENCLAW_PROFILE`이 설정되어 있고 `"default"`가 아니면, 기본값은 `~/.openclaw/workspace-<profile>`이 됩니다.
  * `~/.openclaw/openclaw.json`에서 재정의:

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

`openclaw onboard`, `openclaw configure`, 또는 `openclaw setup`은 작업공간을 만들고, 부트스트랩 파일이 없으면 시드합니다.

작업공간 파일을 이미 직접 관리하고 있다면, 부트스트랩 파일 생성을 비활성화할 수 있습니다.

json5Copy code
[code]
    { agents: { defaults: { skipBootstrap: true } } }
[/code]

## 추가 작업공간 폴더

이전 설치에서는 `~/openclaw`가 만들어졌을 수 있습니다. 여러 작업공간 디렉터리를 남겨두면 한 번에 하나의 작업공간만 활성화되기 때문에 인증이나 상태가 혼동되거나 드리프트될 수 있습니다.

## 작업공간 파일 맵

다음은 OpenClaw가 작업공간 안에 있을 것으로 기대하는 표준 파일입니다.

AGENTS.md - 운영 지침

에이전트의 운영 지침과 메모리 사용 방법입니다. 모든 세션 시작 시 로드됩니다. 규칙, 우선순위, "행동 방식" 세부 사항을 두기에 좋은 위치입니다.

SOUL.md - 페르소나와 톤

페르소나, 톤, 경계입니다. 모든 세션에서 로드됩니다. 가이드: [SOUL.md 성격 가이드](</ko/concepts/soul>).

USER.md - 사용자가 누구인지

사용자가 누구이며 어떻게 호칭해야 하는지입니다. 모든 세션에서 로드됩니다.

IDENTITY.md - 이름, 분위기, 이모지

에이전트의 이름, 분위기, 이모지입니다. 부트스트랩 의식 중에 생성/업데이트됩니다.

TOOLS.md - 로컬 도구 규칙

로컬 도구와 규칙에 대한 참고 사항입니다. 도구 사용 가능 여부를 제어하지 않으며, 지침일 뿐입니다.

HEARTBEAT.md - Heartbeat 체크리스트

Heartbeat 실행을 위한 선택적이고 작은 체크리스트입니다. 토큰 소모를 피하려면 짧게 유지하세요.

BOOT.md - 시작 체크리스트

Gateway 재시작 시([내부 훅](</ko/automation/hooks>)이 활성화된 경우) 자동으로 실행되는 선택적 시작 체크리스트입니다. 짧게 유지하고, 외부 전송에는 메시지 도구를 사용하세요.

BOOTSTRAP.md - 첫 실행 의식

1회성 첫 실행 의식입니다. 완전히 새로운 작업공간에만 생성됩니다. 의식이 완료되면 삭제하세요.

memory/YYYY-MM-DD.md - 일일 메모리 로그

일일 메모리 로그입니다(하루에 파일 하나). 세션 시작 시 오늘 + 어제를 읽는 것을 권장합니다.

MEMORY.md - 선별된 장기 메모리(선택 사항)

선별된 장기 메모리: 지속적인 사실, 선호 사항, 결정, 짧은 요약입니다. 자세한 로그는 `memory/YYYY-MM-DD.md`에 유지하여 메모리 도구가 필요할 때 모든 프롬프트에 주입하지 않고 검색할 수 있게 하세요. `MEMORY.md`는 메인 비공개 세션에서만 로드하세요(공유/그룹 컨텍스트는 제외). 워크플로와 자동 메모리 플러시는 [Memory](</ko/concepts/memory>)를 참조하세요.

skills/ - 작업공간 Skills(선택 사항)

작업공간별 Skills입니다. 해당 작업공간에서 가장 높은 우선순위를 갖는 스킬 위치입니다. 이름이 충돌하면 프로젝트 에이전트 Skills, 개인 에이전트 Skills, 관리형 Skills, 번들 Skills, `skills.load.extraDirs`를 재정의합니다.

canvas/ - Canvas UI 파일(선택 사항)

노드 표시를 위한 Canvas UI 파일입니다(예: `canvas/index.html`).

## 작업공간에 포함되지 않는 것

다음은 `~/.openclaw/` 아래에 있으며 작업공간 저장소에 커밋하면 안 됩니다.

  * `~/.openclaw/openclaw.json`(구성)
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`(모델 인증 프로필: OAuth + API 키)
  * `~/.openclaw/agents/<agentId>/agent/codex-home/`(에이전트별 Codex 런타임 계정, 구성, Skills, 플러그인, 네이티브 스레드 상태)
  * `~/.openclaw/credentials/`(채널/프로바이더 상태 및 레거시 OAuth 가져오기 데이터)
  * `~/.openclaw/agents/<agentId>/sessions/`(세션 트랜스크립트 + 메타데이터)
  * `~/.openclaw/skills/`(관리형 Skills)


세션이나 구성을 마이그레이션해야 한다면 별도로 복사하고 버전 관리에서 제외하세요.

## Git 백업(권장, 비공개)

작업공간을 비공개 메모리처럼 다루세요. 백업과 복구가 가능하도록 **비공개** git 저장소에 넣으세요.

다음 단계는 Gateway가 실행되는 머신에서 실행하세요(그곳에 작업공간이 있습니다).

* ### 저장소 초기화

git이 설치되어 있으면 완전히 새로운 작업공간은 자동으로 초기화됩니다. 이 작업공간이 아직 저장소가 아니라면 다음을 실행하세요.

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md memory/git commit -m "Add agent workspace"
[/code]

* ### 비공개 원격 추가

### GitHub 웹 UI

  1. GitHub에서 새 **비공개** 저장소를 만드세요.
  2. README로 초기화하지 마세요(병합 충돌 방지).
  3. HTTPS 원격 URL을 복사하세요.
  4. 원격을 추가하고 푸시하세요.

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

### GitHub CLI (gh)

bashCopy code
[code]
    gh auth logingh repo create openclaw-workspace --private --source . --remote origin --push
[/code]

### GitLab 웹 UI

  1. GitLab에서 새 **비공개** 저장소를 만드세요.
  2. README로 초기화하지 마세요(병합 충돌 방지).
  3. HTTPS 원격 URL을 복사하세요.
  4. 원격을 추가하고 푸시하세요.

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

* ### 지속적인 업데이트

bashCopy code
[code]
    git statusgit add .git commit -m "Update memory"git push
[/code]

## 비밀 정보를 커밋하지 마세요

제안 `.gitignore` 시작점:

gitignoreCopy code
[code]
    .DS_Store.env**/*.key**/*.pem**/secrets*
[/code]

## 작업공간을 새 머신으로 이동

* ### 저장소 클론

원하는 경로(기본값 `~/.openclaw/workspace`)에 저장소를 클론하세요.

* ### 구성 업데이트

`~/.openclaw/openclaw.json`에서 `agents.defaults.workspace`를 해당 경로로 설정하세요.

* ### 누락된 파일 시드

누락된 파일을 시드하려면 `openclaw setup --workspace <path>`를 실행하세요.

* ### 세션 복사(선택 사항)

세션이 필요하면 이전 머신의 `~/.openclaw/agents/<agentId>/sessions/`를 별도로 복사하세요.

## 고급 참고 사항

  * 다중 에이전트 라우팅은 에이전트별로 서로 다른 작업공간을 사용할 수 있습니다. 라우팅 구성은 [채널 라우팅](</ko/channels/channel-routing>)을 참조하세요.
  * `agents.defaults.sandbox`가 활성화되어 있으면, 메인이 아닌 세션은 `agents.defaults.sandbox.workspaceRoot` 아래의 세션별 샌드박스 작업공간을 사용할 수 있습니다.


## 관련 항목

  * [Heartbeat](</ko/gateway/heartbeat>) \- [HEARTBEAT.md](<http://HEARTBEAT.md>) 작업공간 파일
  * [샌드박싱](</ko/gateway/sandboxing>) \- 샌드박스 환경에서의 작업공간 접근
  * [세션](</ko/concepts/session>) \- 세션 저장 경로
  * [상시 지시](</ko/automation/standing-orders>) \- 작업공간 파일의 지속적 지침


Was this useful?YesNo