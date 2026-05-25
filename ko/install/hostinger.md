---
title: Hostinger
source_url: https://docs.openclaw.ai/ko/install/hostinger
scraped_at: 2026-05-25
---

[Hostinger](<https://www.hostinger.com/openclaw>)에서 **1-Click** 관리형 배포 또는 **VPS** 설치를 통해 지속 실행되는 OpenClaw Gateway를 운영할 수 있습니다.

## 사전 요구 사항

  * Hostinger 계정([가입](<https://www.hostinger.com/openclaw>))
  * 약 5~10분


## 옵션 A: 1-Click OpenClaw

가장 빠르게 시작하는 방법입니다. Hostinger가 인프라, Docker, 자동 업데이트를 처리합니다.

* ### 구매 및 실행

  1. [Hostinger OpenClaw 페이지](<https://www.hostinger.com/openclaw>)에서 Managed OpenClaw 플랜을 선택하고 결제를 완료합니다.


* ### 메시징 채널 선택

연결할 채널을 하나 이상 선택합니다.

  * **WhatsApp** \-- 설정 마법사에 표시되는 QR 코드를 스캔합니다.
  * **Telegram** \-- [BotFather](<https://t.me/BotFather>)에서 받은 봇 토큰을 붙여넣습니다.


* ### 설치 완료

**Finish** 를 클릭해 인스턴스를 배포합니다. 준비가 완료되면 hPanel의 **OpenClaw Overview** 에서 OpenClaw 대시보드에 접속합니다.

## 옵션 B: VPS에서 OpenClaw 실행

서버를 더 세밀하게 제어할 수 있습니다. Hostinger는 VPS에 Docker를 통해 OpenClaw를 배포하고, 사용자는 hPanel의 **Docker Manager** 를 통해 이를 관리합니다.

* ### VPS 구매

  1. [Hostinger OpenClaw 페이지](<https://www.hostinger.com/openclaw>)에서 OpenClaw on VPS 플랜을 선택하고 결제를 완료합니다.


* ### OpenClaw 구성

VPS가 프로비저닝되면 다음 구성 필드를 입력합니다.

  * **Gateway token** \-- 자동 생성됩니다. 나중에 사용할 수 있도록 저장해 두세요.
  * **WhatsApp number** \-- 국가 코드가 포함된 사용자 번호(선택 사항)
  * **Telegram bot token** \-- [BotFather](<https://t.me/BotFather>)에서 발급(선택 사항)
  * **API keys** \-- 결제 중 Ready-to-Use AI 크레딧을 선택하지 않은 경우에만 필요합니다.


* ### OpenClaw 시작

**Deploy** 를 클릭합니다. 실행이 시작되면 hPanel에서 **Open** 을 클릭해 OpenClaw 대시보드를 엽니다.

로그, 재시작, 업데이트는 모두 hPanel의 Docker Manager 인터페이스에서 직접 관리합니다. 업데이트하려면 Docker Manager에서 **Update** 를 누르면 최신 이미지를 가져옵니다.

## 설정 확인

연결한 채널에서 Assistant에게 "Hi"를 보내세요. OpenClaw가 응답하고 초기 선호 설정 과정을 안내합니다.

## 문제 해결

**대시보드가 로드되지 않음** \-- 컨테이너 프로비저닝이 완료될 때까지 몇 분 기다리세요. hPanel의 Docker Manager 로그를 확인하세요.

**Docker 컨테이너가 계속 재시작됨** \-- Docker Manager 로그를 열고 config 오류(누락된 토큰, 잘못된 API 키)를 확인하세요.

**Telegram 봇이 응답하지 않음** \-- 연결을 완료하려면 Telegram에서 받은 pairing 코드 메시지를 OpenClaw 채팅 안에 직접 메시지로 보내세요.

## 다음 단계

  * [Channels](</ko/channels>) \-- Telegram, WhatsApp, Discord 등 연결
  * [Gateway configuration](</ko/gateway/configuration>) \-- 모든 config 옵션


## 관련

  * [Install overview](</ko/install>)
  * [VPS hosting](</ko/vps>)
  * [DigitalOcean](</ko/install/digitalocean>)


Was this useful?YesNo