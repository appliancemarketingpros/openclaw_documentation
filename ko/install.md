---
title: 설치
source_url: https://docs.openclaw.ai/ko/install
scraped_at: 2026-05-25
---

## 시스템 요구 사항

  * **Node 24**(권장) 또는 Node 22.16+ - 설치 스크립트가 이를 자동으로 처리합니다
  * **macOS, Linux 또는 Windows** \- 네이티브 Windows와 WSL2가 모두 지원되며, WSL2가 더 안정적입니다. [Windows](</ko/platforms/windows>)를 참조하세요.
  * 소스에서 빌드하는 경우에만 `pnpm`이 필요합니다


## 권장: 설치 스크립트

가장 빠른 설치 방법입니다. OS를 감지하고, 필요한 경우 Node를 설치하며, OpenClaw를 설치한 뒤 온보딩을 시작합니다.

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

온보딩을 실행하지 않고 설치하려면:

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

모든 플래그와 CI/자동화 옵션은 [설치 프로그램 내부 구조](</ko/install/installer>)를 참조하세요.

## 대체 설치 방법

### 로컬 prefix 설치 프로그램(`install-cli.sh`)

시스템 전역 Node 설치에 의존하지 않고, OpenClaw와 Node를 `~/.openclaw` 같은 로컬 prefix 아래에 두고 싶을 때 사용하세요.

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

기본적으로 npm 설치를 지원하며, 같은 prefix 흐름에서 git-checkout 설치도 지원합니다. 전체 참조: [설치 프로그램 내부 구조](</ko/install/installer#install-clish>).

이미 설치되어 있나요? `openclaw update --channel dev` 및 `openclaw update --channel stable`로 패키지 설치와 git 설치를 전환하세요. [업데이트](</ko/install/updating#switch-between-npm-and-git-installs>)를 참조하세요.

### npm, pnpm 또는 bun

Node를 직접 관리하고 있다면:

### npm

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

### pnpm

bashCopy code
[code]
    pnpm add -g openclaw@latestpnpm approve-builds -gopenclaw onboard --install-daemon
[/code]

### bun

bashCopy code
[code]
    bun add -g openclaw@latestopenclaw onboard --install-daemon
[/code]

문제 해결: sharp 빌드 오류(npm)

전역으로 설치된 libvips 때문에 `sharp`가 실패하는 경우:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### 소스에서 설치

기여자 또는 로컬 체크아웃에서 실행하려는 사용자를 위한 방법:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

또는 링크를 건너뛰고 리포지토리 내부에서 `pnpm openclaw ...`를 사용하세요. 전체 개발 워크플로는 [설정](</ko/start/setup>)을 참조하세요.

### GitHub main에서 설치

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### 컨테이너 및 패키지 관리자

[**Docker** 컨테이너화되었거나 헤드리스인 배포. ](</ko/install/docker>) [**Podman** Docker를 대체하는 루트리스 컨테이너. ](</ko/install/podman>) [**Nix** Nix flake를 통한 선언적 설치. ](</ko/install/nix>) [**Ansible** 자동화된 플릿 프로비저닝. ](</ko/install/ansible>) [**Bun** Bun 런타임을 통한 CLI 전용 사용. ](</ko/install/bun>)

## 설치 확인

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

설치 후 관리형 시작을 원한다면:

  * macOS: `openclaw onboard --install-daemon` 또는 `openclaw gateway install`을 통한 LaunchAgent
  * Linux/WSL2: 같은 명령을 통한 systemd 사용자 서비스
  * 네이티브 Windows: 먼저 Scheduled Task를 사용하고, 작업 생성이 거부되면 사용자별 Startup 폴더 로그인 항목으로 대체


## 호스팅 및 배포

클라우드 서버 또는 VPS에 OpenClaw를 배포하세요.

[**VPS** [**Docker VM** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii9rby9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** 업데이트, 마이그레이션 또는 제거 [**업데이트** OpenClaw를 최신 상태로 유지하세요. ](</ko/install/updating>) [**마이그레이션** 새 머신으로 이동하세요. ](</ko/install/migrating>) [**제거** OpenClaw를 완전히 제거하세요. ](</ko/install/uninstall>) 문제 해결: `openclaw`를 찾을 수 없음 설치가 성공했지만 터미널에서 `openclaw`를 찾을 수 없다면: bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

`$(npm prefix -g)/bin`이 `$PATH`에 없다면, 셸 시작 파일(`~/.zshrc` 또는 `~/.bashrc`)에 추가하세요. bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

그런 다음 새 터미널을 여세요. 자세한 내용은 [Node 설정](</ko/install/node>)을 참조하세요. ](</ko/install/northflank>) Was this useful?YesNo ](</ko/install/render>)](</ko/install/railway>)](</ko/install/azure>)](</ko/install/gcp>)](</ko/install/hetzner>)](</ko/install/kubernetes>)](</ko/install/docker-vm-runtime>)](</ko/vps>)