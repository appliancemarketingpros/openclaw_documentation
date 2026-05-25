---
title: WhatsApp Plugin
source_url: https://docs.openclaw.ai/ko/plugins/reference/whatsapp
scraped_at: 2026-05-25
---

# WhatsApp Plugin

OpenClaw 메시지를 보내고 받기 위한 WhatsApp 채널 인터페이스를 추가합니다.

## 배포

  * 패키지: `@openclaw/whatsapp`
  * 설치 경로: npm; ClawHub


## 인터페이스

channels: whatsapp

## Windows 설치 참고 사항

Windows에서는 npm 설치 중 WhatsApp Plugin에 `PATH`의 Git이 필요합니다. Baileys/libsignal 의존성 중 하나를 git URL에서 가져오기 때문입니다. Git for Windows를 설치한 다음 셸을 다시 시작하고 설치를 다시 실행하세요.

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

Portable Git도 해당 `bin` 디렉터리가 `PATH`에 있으면 동작합니다.

## 관련 문서

  * [whatsapp](</ko/channels/whatsapp>)


Was this useful?YesNo