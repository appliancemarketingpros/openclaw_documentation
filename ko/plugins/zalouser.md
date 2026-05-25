---
title: Zalo 개인용 Plugin
source_url: https://docs.openclaw.ai/ko/plugins/zalouser
scraped_at: 2026-05-25
---

OpenClaw용 Zalo Personal 지원을 Plugin을 통해 제공합니다. 일반 Zalo 사용자 계정을 자동화하기 위해 네이티브 `zca-js`를 사용합니다.

## 이름 지정

채널 ID는 **개인 Zalo 사용자 계정**(비공식)을 자동화한다는 점을 명확히 하기 위해 `zalouser`입니다. `zalo`는 향후 공식 Zalo API 통합 가능성을 위해 예약해 둡니다.

## 실행 위치

이 Plugin은 **Gateway 프로세스 내부** 에서 실행됩니다.

원격 Gateway를 사용하는 경우 **Gateway를 실행하는 머신** 에 설치/구성한 다음 Gateway를 다시 시작하세요.

외부 `zca`/`openzca` CLI 바이너리는 필요하지 않습니다.

## 설치

### 옵션 A: npm에서 설치

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

현재 공식 릴리스 태그를 따르려면 버전을 붙이지 않은 패키지를 사용하세요. 재현 가능한 설치가 필요할 때만 정확한 버전을 고정하세요.

이후 Gateway를 다시 시작하세요.

### 옵션 B: 로컬 폴더에서 설치(개발)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

이후 Gateway를 다시 시작하세요.

## 구성

채널 구성은 `channels.zalouser` 아래에 위치합니다(`plugins.entries.*`가 아님).

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## 에이전트 도구

도구 이름: `zalouser`

작업: `send`, `image`, `link`, `friends`, `groups`, `me`, `status`

채널 메시지 작업은 메시지 반응을 위한 `react`도 지원합니다.

## 관련

  * [Plugin 빌드](</ko/plugins/building-plugins>)
  * [ClawHub](</ko/clawhub>)


Was this useful?YesNo