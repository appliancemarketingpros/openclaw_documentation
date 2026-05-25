---
title: OpenClaw
source_url: https://docs.openclaw.ai/ko
scraped_at: 2026-05-25
---

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _"각질 제거! 각질 제거!"_ — 아마도 우주 바닷가재

**Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo 등에서 AI 에이전트를 위한 모든 OS Gateway.**

메시지를 보내면 주머니 속에서 에이전트 응답을 받을 수 있습니다. 기본 제공 채널, 번들 채널 Plugin, WebChat, 모바일 Node 전반에서 하나의 Gateway를 실행하세요.

[**시작하기** OpenClaw를 설치하고 몇 분 만에 Gateway를 실행하세요. ](</ko/start/getting-started>) [**온보딩 실행** `openclaw onboard`와 페어링 플로우로 안내형 설정을 진행합니다. ](</ko/start/wizard>) [**제어 UI 열기** 채팅, 설정, 세션을 위한 브라우저 대시보드를 실행합니다. ](</ko/web/control-ui>)

## OpenClaw란 무엇인가요?

OpenClaw는 즐겨 쓰는 채팅 앱과 채널 표면을 Pi 같은 AI 코딩 에이전트에 연결하는 **셀프 호스팅 Gateway** 입니다. 기본 제공 채널과 Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo 등 번들 또는 외부 채널 Plugin을 지원합니다. 자체 머신이나 서버에서 단일 Gateway 프로세스를 실행하면, 메시징 앱과 항상 사용 가능한 AI 어시스턴트 사이의 다리가 됩니다.

**누구를 위한 것인가요?** 호스팅 서비스에 의존하거나 데이터 제어권을 포기하지 않고, 어디서나 메시지를 보낼 수 있는 개인 AI 어시스턴트를 원하는 개발자와 고급 사용자에게 적합합니다.

**무엇이 다른가요?**

  * **셀프 호스팅** : 사용자의 하드웨어에서 사용자의 규칙대로 실행됩니다
  * **멀티채널** : 하나의 Gateway가 기본 제공 채널과 번들 또는 외부 채널 Plugin을 동시에 제공합니다
  * **에이전트 네이티브** : 도구 사용, 세션, 메모리, 다중 에이전트 라우팅을 갖춘 코딩 에이전트용으로 구축되었습니다
  * **오픈 소스** : MIT 라이선스, 커뮤니티 중심


**무엇이 필요한가요?** Node 24(권장), 또는 호환성을 위한 Node 22 LTS(`22.16+`), 선택한 공급자의 API 키, 그리고 5분이면 됩니다. 최상의 품질과 보안을 위해 사용 가능한 가장 강력한 최신 세대 모델을 사용하세요.

## 작동 방식
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["Pi agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

Gateway는 세션, 라우팅, 채널 연결의 단일 정보 출처입니다.

## 주요 기능

[**멀티채널 Gateway** 단일 Gateway 프로세스로 Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat 등을 사용할 수 있습니다. ](</ko/channels>) [**Plugin 채널** 번들 Plugin은 일반적인 최신 릴리스에서 Matrix, Nostr, Twitch, Zalo 등을 추가합니다. ](</ko/tools/plugin>) [**다중 에이전트 라우팅** 에이전트, 워크스페이스, 발신자별 격리 세션입니다. ](</ko/concepts/multi-agent>) [**미디어 지원** 이미지, 오디오, 문서를 보내고 받을 수 있습니다. ](</ko/nodes/images>) [**웹 제어 UI** 채팅, 설정, 세션, Node를 위한 브라우저 대시보드입니다. ](</ko/web/control-ui>) [**모바일 Node** Canvas, 카메라, 음성 지원 워크플로우를 위해 iOS 및 Android Node를 페어링합니다. ](</ko/nodes>)

## 빠른 시작

* ### OpenClaw 설치

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### 온보딩 및 서비스 설치

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### 채팅

브라우저에서 제어 UI를 열고 메시지를 보내세요.

bashCopy code
[code]
    openclaw dashboard
[/code]

또는 채널을 연결하고([Telegram](</ko/channels/telegram>)이 가장 빠릅니다) 휴대폰에서 채팅하세요.

전체 설치 및 개발 설정이 필요한가요? [시작하기](</ko/start/getting-started>)를 참조하세요.

## 대시보드

Gateway가 시작된 뒤 브라우저 제어 UI를 엽니다.

  * 로컬 기본값: <http://127.0.0.1:18789/>
  * 원격 액세스: [웹 표면](</ko/web>) 및 [Tailscale](</ko/gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## 구성(선택 사항)

구성은 `~/.openclaw/openclaw.json`에 있습니다.

  * **아무것도 하지 않으면** , OpenClaw는 발신자별 세션과 함께 번들 Pi 바이너리를 RPC 모드로 사용합니다.
  * 잠그고 싶다면 `channels.whatsapp.allowFrom` 및 그룹의 경우 멘션 규칙부터 시작하세요.


예:

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## 여기서 시작하세요

[**문서 허브** 사용 사례별로 정리된 모든 문서와 가이드입니다. ](</ko/start/hubs>) [**구성** 핵심 Gateway 설정, 토큰, 공급자 구성입니다. ](</ko/gateway/configuration>) [**원격 액세스** SSH 및 tailnet 액세스 패턴입니다. ](</ko/gateway/remote>) [**채널** Feishu, Microsoft Teams, WhatsApp, Telegram, Discord 등을 위한 채널별 설정입니다. ](</ko/channels/telegram>) [**Node** 페어링, Canvas, 카메라, 기기 작업을 지원하는 iOS 및 Android Node입니다. ](</ko/nodes>) [**도움말** 일반적인 수정 사항과 문제 해결 진입점입니다. ](</ko/help>)

## 더 알아보기

[**전체 기능 목록** 전체 채널, 라우팅, 미디어 기능입니다. ](</ko/concepts/features>) [**다중 에이전트 라우팅** 워크스페이스 격리와 에이전트별 세션입니다. ](</ko/concepts/multi-agent>) [**보안** 토큰, 허용 목록, 안전 제어입니다. ](</ko/gateway/security>) [**문제 해결** Gateway 진단과 일반적인 오류입니다. ](</ko/gateway/troubleshooting>) [**정보 및 크레딧** 프로젝트 기원, 기여자, 라이선스입니다. ](</ko/reference/credits>)

Was this useful?YesNo