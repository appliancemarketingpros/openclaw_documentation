---
title: WeChat
source_url: https://docs.openclaw.ai/ko/channels/wechat
scraped_at: 2026-05-25
---

OpenClaw는 Tencent의 외부 `@tencent-weixin/openclaw-weixin` 채널 Plugin을 통해 WeChat에 연결합니다.

상태: 외부 Plugin. 직접 채팅과 미디어가 지원됩니다. 그룹 채팅은 현재 Plugin 기능 메타데이터에 광고되지 않습니다.

## 명명

  * **WeChat** 은 이 문서에서 사용자에게 표시되는 이름입니다.
  * **Weixin** 은 Tencent 패키지와 Plugin ID에서 사용하는 이름입니다.
  * `openclaw-weixin`은 OpenClaw 채널 ID입니다.
  * `@tencent-weixin/openclaw-weixin`은 npm 패키지입니다.


CLI 명령과 설정 경로에서는 `openclaw-weixin`을 사용하세요.

## 작동 방식

WeChat 코드는 OpenClaw 코어 리포지토리에 포함되어 있지 않습니다. OpenClaw는 범용 채널 Plugin 계약을 제공하고, 외부 Plugin은 WeChat 전용 런타임을 제공합니다.

  1. `openclaw plugins install`이 `@tencent-weixin/openclaw-weixin`을 설치합니다.
  2. Gateway가 Plugin 매니페스트를 발견하고 Plugin 진입점을 로드합니다.
  3. Plugin이 채널 ID `openclaw-weixin`을 등록합니다.
  4. `openclaw channels login --channel openclaw-weixin`이 QR 로그인을 시작합니다.
  5. Plugin이 OpenClaw 상태 디렉터리 아래에 계정 자격 증명을 저장합니다.
  6. Gateway가 시작되면 Plugin이 설정된 각 계정에 대해 Weixin 모니터를 시작합니다.
  7. 수신 WeChat 메시지는 채널 계약을 통해 정규화되고, 선택된 OpenClaw 에이전트로 라우팅된 뒤, Plugin의 발신 경로를 통해 다시 전송됩니다.


이 분리는 중요합니다. OpenClaw 코어는 채널에 구애받지 않아야 합니다. WeChat 로그인, Tencent iLink API 호출, 미디어 업로드/다운로드, 컨텍스트 토큰, 계정 모니터링은 외부 Plugin이 소유합니다.

## 설치

빠른 설치:

bashCopy code
[code]
    npx -y @tencent-weixin/openclaw-weixin-cli install
[/code]

수동 설치:

bashCopy code
[code]
    openclaw plugins install "@tencent-weixin/openclaw-weixin"openclaw config set plugins.entries.openclaw-weixin.enabled true
[/code]

설치 후 Gateway를 다시 시작하세요.

bashCopy code
[code]
    openclaw gateway restart
[/code]

## 로그인

Gateway가 실행되는 동일한 머신에서 QR 로그인을 실행하세요.

bashCopy code
[code]
    openclaw channels login --channel openclaw-weixin
[/code]

휴대폰의 WeChat으로 QR 코드를 스캔하고 로그인을 확인하세요. 스캔이 성공하면 Plugin이 계정 토큰을 로컬에 저장합니다.

다른 WeChat 계정을 추가하려면 동일한 로그인 명령을 다시 실행하세요. 여러 계정의 경우 계정, 채널, 발신자별로 직접 메시지 세션을 격리하세요.

bashCopy code
[code]
    openclaw config set session.dmScope per-account-channel-peer
[/code]

## 접근 제어

직접 메시지는 채널 Plugin에 일반 OpenClaw 페어링 및 허용 목록 모델을 사용합니다.

새 발신자를 승인하세요.

bashCopy code
[code]
    openclaw pairing list openclaw-weixinopenclaw pairing approve openclaw-weixin &lt;CODE&gt;
[/code]

전체 접근 제어 모델은 [페어링](</ko/channels/pairing>)을 참조하세요.

## 호환성

Plugin은 시작 시 호스트 OpenClaw 버전을 확인합니다.

Plugin 라인 | OpenClaw 버전 | npm 태그  
---|---|---  
`2.x` | `>=2026.3.22` | `latest`  
`1.x` | `>=2026.1.0 <2026.3.22` | `legacy`  
  
Plugin이 OpenClaw 버전이 너무 오래되었다고 보고하면 OpenClaw를 업데이트하거나 레거시 Plugin 라인을 설치하세요.

bashCopy code
[code]
    openclaw plugins install @tencent-weixin/openclaw-weixin@legacy
[/code]

## 사이드카 프로세스

WeChat Plugin은 Tencent iLink API를 모니터링하는 동안 Gateway 옆에서 헬퍼 작업을 실행할 수 있습니다. 이슈 #68451에서 이 헬퍼 경로는 OpenClaw의 범용 오래된 Gateway 정리에서 버그를 드러냈습니다. 자식 프로세스가 부모 Gateway 프로세스를 정리하려고 시도할 수 있었고, systemd 같은 프로세스 관리자 아래에서 재시작 루프가 발생했습니다.

현재 OpenClaw 시작 정리는 현재 프로세스와 그 상위 프로세스를 제외하므로, 채널 헬퍼는 자신을 시작한 Gateway를 종료해서는 안 됩니다. 이 수정은 범용입니다. 코어의 WeChat 전용 경로가 아닙니다.

## 문제 해결

설치 및 상태를 확인하세요.

bashCopy code
[code]
    openclaw plugins listopenclaw channels status --probeopenclaw --version
[/code]

채널이 설치된 것으로 표시되지만 연결되지 않으면 Plugin이 활성화되어 있는지 확인하고 다시 시작하세요.

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled trueopenclaw gateway restart
[/code]

WeChat을 활성화한 후 Gateway가 반복적으로 다시 시작되면 OpenClaw와 Plugin을 모두 업데이트하세요.

bashCopy code
[code]
    npm view @tencent-weixin/openclaw-weixin versionopenclaw plugins install "@tencent-weixin/openclaw-weixin" --forceopenclaw gateway restart
[/code]

시작 시 설치된 Plugin 패키지가 `requires compiled runtime output for TypeScript entry`라고 보고하면, npm 패키지가 OpenClaw에 필요한 컴파일된 JavaScript 런타임 파일 없이 게시된 것입니다. Plugin 게시자가 수정된 패키지를 출시한 뒤 업데이트/재설치하거나, 임시로 Plugin을 비활성화/제거하세요.

임시 비활성화:

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled falseopenclaw gateway restart
[/code]

## 관련 문서

  * 채널 개요: [채팅 채널](</ko/channels>)
  * 페어링: [페어링](</ko/channels/pairing>)
  * 채널 라우팅: [채널 라우팅](</ko/channels/channel-routing>)
  * Plugin 아키텍처: [Plugin 아키텍처](</ko/plugins/architecture>)
  * 채널 Plugin SDK: [채널 Plugin SDK](</ko/plugins/sdk-channel-plugins>)
  * 외부 패키지: [@tencent-weixin/openclaw-weixin](<https://www.npmjs.com/package/@tencent-weixin/openclaw-weixin>)


Was this useful?YesNo