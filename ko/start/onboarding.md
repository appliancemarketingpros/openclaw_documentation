---
title: 온보딩(macOS 앱)
source_url: https://docs.openclaw.ai/ko/start/onboarding
scraped_at: 2026-05-25
---

이 문서는 **현재** 최초 실행 설정 흐름을 설명합니다. 목표는 매끄러운 "0일차" 경험입니다. Gateway 실행 위치를 선택하고, 인증을 연결하고, 마법사를 실행한 다음 에이전트가 스스로 부트스트랩하도록 합니다. 온보딩 경로에 대한 일반적인 개요는 [온보딩 개요](</ko/start/onboarding-overview>)를 참조하세요.

* ### macOS 경고 승인

![](/assets/macos-onboarding/01-macos-warning.jpeg)
* ### 로컬 네트워크 찾기 승인

![](/assets/macos-onboarding/02-local-networks.jpeg)
* ### 환영 및 보안 안내

표시된 보안 안내를 읽고 그에 따라 결정하세요 ![](/assets/macos-onboarding/03-security-notice.png)

보안 신뢰 모델:

  * 기본적으로 OpenClaw는 개인 에이전트입니다. 하나의 신뢰할 수 있는 운영자 경계입니다.
  * 공유/다중 사용자 설정에는 잠금 강화가 필요합니다. 신뢰 경계를 분리하고, 도구 접근을 최소화하며, [보안](</ko/gateway/security>)을 따르세요.
  * 이제 로컬 온보딩은 새 구성을 기본적으로 `tools.profile: "coding"`으로 설정하므로, 새로운 로컬 설정이 무제한 `full` 프로필을 강제하지 않고도 파일 시스템/런타임 도구를 유지합니다.
  * 훅/Webhook 또는 기타 신뢰할 수 없는 콘텐츠 피드가 활성화된 경우, 강력한 최신 모델 등급을 사용하고 엄격한 도구 정책/샌드박싱을 유지하세요.


* ### 로컬과 원격

![](/assets/macos-onboarding/04-choose-gateway.png)

**Gateway** 는 어디에서 실행되나요?

  * **이 Mac(로컬 전용):** 온보딩에서 인증을 구성하고 자격 증명을 로컬에 쓸 수 있습니다.
  * **원격(SSH/Tailnet 경유):** 온보딩은 로컬 인증을 구성하지 않습니다. 자격 증명은 Gateway 호스트에 있어야 합니다.
  * **나중에 구성:** 설정을 건너뛰고 앱을 구성되지 않은 상태로 둡니다.


* ### 권한

OpenClaw에 부여할 권한을 선택하세요 ![](/assets/macos-onboarding/05-permissions.png)

온보딩은 다음에 필요한 TCC 권한을 요청합니다.

  * 자동화(AppleScript)
  * 알림
  * 손쉬운 사용
  * 화면 기록
  * 마이크
  * 음성 인식
  * 카메라
  * 위치


* ### CLI

* ### 온보딩 채팅(전용 세션)

설정 후 앱은 전용 온보딩 채팅 세션을 열어 에이전트가 자신을 소개하고 다음 단계를 안내할 수 있게 합니다. 이렇게 하면 최초 실행 안내가 일반 대화와 분리됩니다. 첫 에이전트 실행 중 Gateway 호스트에서 어떤 일이 일어나는지는 [부트스트래핑](</ko/start/bootstrapping>)을 참조하세요.

## 관련 항목

  * [온보딩 개요](</ko/start/onboarding-overview>)
  * [시작하기](</ko/start/getting-started>)


Was this useful?YesNo