---
title: 시작하기
source_url: https://docs.openclaw.ai/ko/start/getting-started
scraped_at: 2026-05-25
---

OpenClaw를 설치하고, 온보딩을 실행한 다음, AI 어시스턴트와 채팅하세요. 모두 약 5분이면 됩니다. 완료하면 실행 중인 Gateway, 구성된 인증, 그리고 작동하는 채팅 세션을 갖게 됩니다.

## 필요한 것

  * **Node.js** — Node 24 권장(Node 22.16+도 지원)
  * 모델 제공업체(Anthropic, OpenAI, Google 등)의 **API 키** — 온보딩 중 입력하라는 메시지가 표시됩니다


## 빠른 설정

* ### OpenClaw 설치

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![설치 스크립트 프로세스](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### 온보딩 실행

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

마법사가 모델 제공업체 선택, API 키 설정, Gateway 구성 과정을 안내합니다. 약 2분이 걸립니다.

전체 참조는 [온보딩(CLI)](</ko/start/wizard>)을 참조하세요.

* ### Gateway 실행 확인

bashCopy code
[code]
    openclaw gateway status
[/code]

Gateway가 포트 18789에서 수신 대기 중인 것을 볼 수 있어야 합니다.

* ### 대시보드 열기

bashCopy code
[code]
    openclaw dashboard
[/code]

브라우저에서 Control UI가 열립니다. 로드되면 모든 것이 정상 작동 중입니다.

* ### 첫 메시지 보내기

Control UI 채팅에 메시지를 입력하면 AI 답변을 받을 수 있습니다.

대신 휴대폰에서 채팅하고 싶나요? 가장 빠르게 설정할 수 있는 채널은 [Telegram](</ko/channels/telegram>)입니다(봇 토큰만 있으면 됩니다). 모든 옵션은 [채널](</ko/channels>)을 참조하세요.

고급: 사용자 지정 Control UI 빌드 마운트

현지화되었거나 사용자 지정된 대시보드 빌드를 유지 관리하는 경우, `gateway.controlUi.root`가 빌드된 정적 에셋과 `index.html`이 포함된 디렉터리를 가리키도록 설정하세요.

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# 빌드된 정적 파일을 해당 디렉터리로 복사합니다.
[/code]

그런 다음 다음을 설정하세요.

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

gateway를 다시 시작하고 대시보드를 다시 여세요.

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## 다음에 할 일

[**채널 연결** Discord, Feishu, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo 등. ](</ko/channels>) [**페어링 및 안전** 에이전트에게 메시지를 보낼 수 있는 사람을 제어하세요. ](</ko/channels/pairing>) [**Gateway 구성** 모델, 도구, sandbox, 고급 설정. ](</ko/gateway/configuration>) [**도구 탐색** 브라우저, exec, 웹 검색, Skills, Plugin. ](</ko/tools>)

고급: 환경 변수

OpenClaw를 서비스 계정으로 실행하거나 사용자 지정 경로를 사용하려는 경우:

  * `OPENCLAW_HOME` — 내부 경로 확인을 위한 홈 디렉터리
  * `OPENCLAW_STATE_DIR` — 상태 디렉터리 재정의
  * `OPENCLAW_CONFIG_PATH` — 구성 파일 경로 재정의


전체 참조: [환경 변수](</ko/help/environment>).

## 관련 항목

  * [설치 개요](</ko/install>)
  * [채널 개요](</ko/channels>)
  * [설정](</ko/start/setup>)


Was this useful?YesNo