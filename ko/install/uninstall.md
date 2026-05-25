---
title: 제거하기
source_url: https://docs.openclaw.ai/ko/install/uninstall
scraped_at: 2026-05-25
---

두 가지 경로가 있습니다.

  * `openclaw`가 아직 설치되어 있다면 **쉬운 경로**
  * CLI는 사라졌지만 서비스가 아직 실행 중이라면 **수동 서비스 제거**


## 쉬운 경로(CLI가 아직 설치된 경우)

권장: 내장 제거기를 사용하세요.

bashCopy code
[code]
    openclaw uninstall
[/code]

비대화형(자동화 / npx):

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

수동 단계(동일한 결과):

  1. gateway 서비스 중지:

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. gateway 서비스 제거(launchd/systemd/schtasks):

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. 상태 + config 삭제:

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

상태 디렉터리 밖의 사용자 지정 위치에 `OPENCLAW_CONFIG_PATH`를 설정했다면 그 파일도 삭제하세요.

  4. 워크스페이스 삭제(선택 사항, 에이전트 파일 제거):

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. CLI 설치 제거(사용한 방식 선택):

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. macOS 앱을 설치했다면:

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

참고:

  * profile(`--profile` / `OPENCLAW_PROFILE`)을 사용했다면 각 상태 디렉터리마다 3단계를 반복하세요(기본값은 `~/.openclaw-<profile>`).
  * 원격 모드에서는 상태 디렉터리가 **gateway 호스트** 에 있으므로 1-4단계도 그곳에서 실행하세요.


## 수동 서비스 제거(CLI가 설치되지 않은 경우)

gateway 서비스가 계속 실행되는데 `openclaw`가 없는 경우 이 방법을 사용하세요.

### macOS (launchd)

기본 레이블은 `ai.openclaw.gateway`입니다(또는 `ai.openclaw.<profile>`, 레거시 `com.openclaw.*`가 여전히 남아 있을 수 있음).

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

profile을 사용했다면 레이블과 plist 이름을 `ai.openclaw.<profile>`로 바꾸세요. 레거시 `com.openclaw.*` plist가 있으면 그것도 제거하세요.

### Linux (systemd 사용자 unit)

기본 unit 이름은 `openclaw-gateway.service`입니다(또는 `openclaw-gateway-<profile>.service`).

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows (예약 작업)

기본 작업 이름은 `OpenClaw Gateway`입니다(또는 `OpenClaw Gateway (<profile>)`). 작업 스크립트는 상태 디렉터리 아래에 있습니다.

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
[/code]

profile을 사용했다면 해당 작업 이름과 `~\.openclaw-<profile>\gateway.cmd`를 삭제하세요.

## 일반 설치 vs 소스 체크아웃

### 일반 설치([install.sh](<http://install.sh>) / npm / pnpm / bun)

`https://openclaw.ai/install.sh` 또는 `install.ps1`를 사용했다면 CLI는 `npm install -g openclaw@latest`로 설치되었습니다. `npm rm -g openclaw`로 제거하세요(`pnpm` 또는 `bun`으로 설치했다면 `pnpm remove -g` / `bun remove -g` 사용).

### 소스 체크아웃(git clone)

repo 체크아웃에서 실행하는 경우(`git clone` \+ `openclaw ...` / `bun run openclaw ...`):

  1. repo를 삭제하기 **전에** gateway 서비스를 제거하세요(위의 쉬운 경로 또는 수동 서비스 제거 사용).
  2. repo 디렉터리를 삭제하세요.
  3. 위에서 설명한 대로 상태 + 워크스페이스를 제거하세요.


## 관련 항목

  * [설치 개요](</ko/install>)
  * [마이그레이션 가이드](</ko/install/migrating>)


Was this useful?YesNo