---
title: Node.js
source_url: https://docs.openclaw.ai/ko/install/node
scraped_at: 2026-05-25
---

OpenClaw에는 **Node 22.16 이상** 이 필요합니다. **Node 24는 설치, CI, 릴리스 워크플로의 기본 및 권장 런타임** 입니다. Node 22는 활성 LTS 라인을 통해 계속 지원됩니다. [설치 스크립트](</ko/install#alternative-install-methods>)는 Node를 자동으로 감지하고 설치합니다. 이 페이지는 Node를 직접 설정하고 모든 것이 올바르게 연결되었는지(버전, PATH, 전역 설치) 확인하려는 경우를 위한 것입니다.

## 버전 확인

bashCopy code
[code]
    node -v
[/code]

이 명령이 `v24.x.x` 이상을 출력하면 권장 기본값을 사용 중입니다. `v22.16.x` 이상을 출력하면 지원되는 Node 22 LTS 경로를 사용 중이지만, 가능할 때 Node 24로 업그레이드하는 것을 권장합니다. Node가 설치되어 있지 않거나 버전이 너무 오래되었다면 아래 설치 방법 중 하나를 선택하세요.

## Node 설치

### macOS

**Homebrew**(권장):

bashCopy code
[code]
    brew install node
[/code]

또는 [nodejs.org](<https://nodejs.org/>)에서 macOS 설치 프로그램을 다운로드하세요.

### Linux

**Ubuntu / Debian:**

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt-get install -y nodejs
[/code]

**Fedora / RHEL:**

bashCopy code
[code]
    sudo dnf install nodejs
[/code]

또는 버전 관리자를 사용하세요(아래 참조).

### Windows

**winget**(권장):

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey:**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

또는 [nodejs.org](<https://nodejs.org/>)에서 Windows 설치 프로그램을 다운로드하세요.

Using a version manager (nvm, fnm, mise, asdf)

버전 관리자를 사용하면 Node 버전 간에 쉽게 전환할 수 있습니다. 인기 있는 옵션:

  * [**fnm**](<https://github.com/Schniz/fnm>) \- 빠르고 크로스 플랫폼 지원
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- macOS/Linux에서 널리 사용됨
  * [**mise**](<https://mise.jdx.dev/>) \- 다중 언어 지원(Node, Python, Ruby 등)


fnm 예시:

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## 문제 해결

### `openclaw: command not found`

이는 거의 항상 npm의 전역 bin 디렉터리가 PATH에 없다는 뜻입니다.

* ### Find your global npm prefix

bashCopy code
[code]
    npm prefix -g
[/code]

* ### Check if it's on your PATH

bashCopy code
[code]
    echo "$PATH"
[/code]

출력에서 `<npm-prefix>/bin`(macOS/Linux) 또는 `<npm-prefix>`(Windows)를 찾으세요.

* ### Add it to your shell startup file

### macOS / Linux

`~/.zshrc` 또는 `~/.bashrc`에 추가하세요:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

그런 다음 새 터미널을 열거나 zsh에서는 `rehash`, bash에서는 `hash -r`을 실행하세요.

### Windows

설정 → 시스템 → 환경 변수를 통해 `npm prefix -g`의 출력을 시스템 PATH에 추가하세요.

### `npm install -g`에서 권한 오류(Linux)

`EACCES` 오류가 표시되면 npm의 전역 prefix를 사용자가 쓸 수 있는 디렉터리로 변경하세요:

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

영구 적용하려면 `export PATH=...` 줄을 `~/.bashrc` 또는 `~/.zshrc`에 추가하세요.

## 관련 항목

  * [설치 개요](</ko/install>) \- 모든 설치 방법
  * [업데이트](</ko/install/updating>) \- OpenClaw를 최신 상태로 유지
  * [시작하기](</ko/start/getting-started>) \- 설치 후 첫 단계


Was this useful?YesNo