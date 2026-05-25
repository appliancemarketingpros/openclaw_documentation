---
title: Twitch
source_url: https://docs.openclaw.ai/ko/channels/twitch
scraped_at: 2026-05-25
---

IRC 연결을 통한 Twitch 채팅 지원. OpenClaw는 Twitch 사용자(봇 계정)로 연결하여 채널에서 메시지를 받고 보냅니다.

## 번들 Plugin

이전 빌드를 사용 중이거나 Twitch가 제외된 사용자 지정 설치를 사용하는 경우, npm 패키지를 직접 설치하세요.

### npm 레지스트리

bashCopy code
[code]
    openclaw plugins install @openclaw/twitch
[/code]

### 로컬 체크아웃

bashCopy code
[code]
    openclaw plugins install ./path/to/local/twitch-plugin
[/code]

현재 공식 릴리스 태그를 따르려면 기본 패키지를 사용하세요. 재현 가능한 설치가 필요할 때만 정확한 버전을 고정하세요.

세부 정보: [Plugins](</ko/tools/plugin>)

## 빠른 설정(초보자)

* ### Plugin 사용 가능 여부 확인

현재 패키징된 OpenClaw 릴리스에는 이미 포함되어 있습니다. 이전/사용자 지정 설치에서는 위 명령으로 수동 추가할 수 있습니다.

* ### Twitch 봇 계정 생성

봇 전용 Twitch 계정을 생성하세요(또는 기존 계정을 사용하세요).

* ### 자격 증명 생성

[Twitch Token Generator](<https://twitchtokengenerator.com/>)를 사용하세요.

  * **Bot Token** 을 선택합니다
  * `chat:read` 및 `chat:write` 범위가 선택되어 있는지 확인합니다
  * **Client ID** 및 **Access Token** 을 복사합니다


* ### Twitch 사용자 ID 찾기

<https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/>를 사용하여 사용자 이름을 Twitch 사용자 ID로 변환하세요.

* ### 토큰 구성

  * Env: `OPENCLAW_TWITCH_ACCESS_TOKEN=...`(기본 계정만)
  * 또는 구성: `channels.twitch.accessToken`


둘 다 설정된 경우 구성 값이 우선합니다(env 대체는 기본 계정 전용).

* ### Gateway 시작

구성된 채널로 Gateway를 시작하세요.

최소 구성:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw", // Bot's Twitch account      accessToken: "oauth:abc123...", // OAuth Access Token (or use OPENCLAW_TWITCH_ACCESS_TOKEN env var)      clientId: "xyz789...", // Client ID from Token Generator      channel: "vevisk", // Which Twitch channel's chat to join (required)      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only - get it from https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/    },  },}
[/code]

## 개요

  * Gateway가 소유한 Twitch 채널입니다.
  * 결정적 라우팅: 응답은 항상 Twitch로 돌아갑니다.
  * 각 계정은 격리된 세션 키 `agent:<agentId>:twitch:<accountName>`에 매핑됩니다.
  * `username`은 봇 계정(인증 주체)이고, `channel`은 참여할 채팅방입니다.


## 설정(자세히)

### 자격 증명 생성

[Twitch Token Generator](<https://twitchtokengenerator.com/>)를 사용하세요.

  * **Bot Token** 을 선택합니다
  * `chat:read` 및 `chat:write` 범위가 선택되어 있는지 확인합니다
  * **Client ID** 및 **Access Token** 을 복사합니다


### 봇 구성

### Env var(기본 계정만)

bashCopy code
[code]
    OPENCLAW_TWITCH_ACCESS_TOKEN=oauth:abc123...
[/code]

### 구성

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",    },  },}
[/code]

env와 구성이 둘 다 설정된 경우 구성이 우선합니다.

### 액세스 제어(권장)

json5Copy code
[code]
    {  channels: {    twitch: {      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only    },  },}
[/code]

강력한 허용 목록에는 `allowFrom`을 선호하세요. 역할 기반 액세스를 원하면 대신 `allowedRoles`를 사용하세요.

**사용 가능한 역할:** `"moderator"`, `"owner"`, `"vip"`, `"subscriber"`, `"all"`.

## 토큰 갱신(선택 사항)

[Twitch Token Generator](<https://twitchtokengenerator.com/>)의 토큰은 자동으로 갱신할 수 없습니다. 만료되면 다시 생성하세요.

자동 토큰 갱신을 사용하려면 [Twitch Developer Console](<https://dev.twitch.tv/console>)에서 직접 Twitch 애플리케이션을 만들고 구성에 추가하세요.

json5Copy code
[code]
    {  channels: {    twitch: {      clientSecret: "your_client_secret",      refreshToken: "your_refresh_token",    },  },}
[/code]

봇은 만료 전에 토큰을 자동으로 갱신하고 갱신 이벤트를 로그에 기록합니다.

## 다중 계정 지원

계정별 토큰과 함께 `channels.twitch.accounts`를 사용하세요. 공유 패턴은 [구성](</ko/gateway/configuration>)을 참조하세요.

예시(두 채널의 봇 계정 하나):

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        channel1: {          username: "openclaw",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "vevisk",        },        channel2: {          username: "openclaw",          accessToken: "oauth:def456...",          clientId: "uvw012...",          channel: "secondchannel",        },      },    },  },}
[/code]

## 액세스 제어

### 사용자 ID 허용 목록(가장 안전)

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowFrom: ["123456789", "987654321"],        },      },    },  },}
[/code]

### 역할 기반

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowedRoles: ["moderator", "vip"],        },      },    },  },}
[/code]

`allowFrom`은 강력한 허용 목록입니다. 설정하면 해당 사용자 ID만 허용됩니다. 역할 기반 액세스를 원하면 `allowFrom`을 설정하지 말고 대신 `allowedRoles`를 구성하세요.

### @mention 요구 사항 비활성화

기본적으로 `requireMention`은 `true`입니다. 비활성화하고 모든 메시지에 응답하려면:

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          requireMention: false,        },      },    },  },}
[/code]

## 문제 해결

먼저 진단 명령을 실행하세요.

bashCopy code
[code]
    openclaw doctoropenclaw channels status --probe
[/code]

봇이 메시지에 응답하지 않음

  * **액세스 제어 확인:** 사용자 ID가 `allowFrom`에 있는지 확인하거나, 테스트를 위해 일시적으로 `allowFrom`을 제거하고 `allowedRoles: ["all"]`을 설정하세요.
  * **봇이 채널에 있는지 확인:** 봇은 `channel`에 지정된 채널에 참여해야 합니다.

토큰 문제

"연결 실패" 또는 인증 오류:

  * `accessToken`이 OAuth 액세스 토큰 값인지 확인하세요(일반적으로 `oauth:` 접두사로 시작)
  * 토큰에 `chat:read` 및 `chat:write` 범위가 있는지 확인하세요
  * 토큰 갱신을 사용하는 경우 `clientSecret` 및 `refreshToken`이 설정되어 있는지 확인하세요

토큰 갱신이 작동하지 않음

갱신 이벤트가 있는지 로그를 확인하세요.

CodeCopy code
[code]
    Using env token source for mybotAccess token refreshed for user 123456 (expires in 14400s)
[/code]

"토큰 갱신 비활성화됨(갱신 토큰 없음)"이 표시되는 경우:

  * `clientSecret`이 제공되었는지 확인하세요
  * `refreshToken`이 제공되었는지 확인하세요


## 구성

### 계정 구성

봇 사용자 이름입니다.

`chat:read` 및 `chat:write`가 포함된 OAuth 액세스 토큰입니다.

Twitch Client ID입니다(Token Generator 또는 앱에서 가져옴).

참여할 채널입니다.

이 계정을 활성화합니다.

선택 사항: 자동 토큰 갱신용입니다.

선택 사항: 자동 토큰 갱신용입니다.

토큰 만료 시간(초)입니다.

토큰 획득 타임스탬프입니다.

사용자 ID 허용 목록입니다.

@mention을 요구합니다.

### Provider 옵션

  * `channels.twitch.enabled` \- 채널 시작 활성화/비활성화
  * `channels.twitch.username` \- 봇 사용자 이름(간소화된 단일 계정 구성)
  * `channels.twitch.accessToken` \- OAuth 액세스 토큰(간소화된 단일 계정 구성)
  * `channels.twitch.clientId` \- Twitch Client ID(간소화된 단일 계정 구성)
  * `channels.twitch.channel` \- 참여할 채널(간소화된 단일 계정 구성)
  * `channels.twitch.accounts.<accountName>` \- 다중 계정 구성(위의 모든 계정 필드)


전체 예시:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",      clientSecret: "secret123...",      refreshToken: "refresh456...",      allowFrom: ["123456789"],      allowedRoles: ["moderator", "vip"],      accounts: {        default: {          username: "mybot",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "your_channel",          enabled: true,          clientSecret: "secret123...",          refreshToken: "refresh456...",          expiresIn: 14400,          obtainmentTimestamp: 1706092800000,          allowFrom: ["123456789", "987654321"],          allowedRoles: ["moderator"],        },      },    },  },}
[/code]

## 도구 작업

에이전트는 다음 작업으로 `twitch`를 호출할 수 있습니다.

  * `send` \- 채널에 메시지 보내기


예시:

json5Copy code
[code]
    {  action: "twitch",  params: {    message: "Hello Twitch!",    to: "#mychannel",  },}
[/code]

## 안전 및 운영

  * **토큰을 비밀번호처럼 취급하세요** — 토큰을 git에 절대 커밋하지 마세요.
  * 장기 실행 봇에는 **자동 토큰 갱신을 사용하세요**.
  * 액세스 제어에는 사용자 이름 대신 **사용자 ID 허용 목록을 사용하세요**.
  * 토큰 갱신 이벤트와 연결 상태를 위해 **로그를 모니터링하세요**.
  * **토큰 범위를 최소화하세요** — `chat:read` 및 `chat:write`만 요청하세요.
  * **막혔다면** : 다른 프로세스가 세션을 소유하지 않는지 확인한 후 Gateway를 다시 시작하세요.


## 제한

  * 메시지당 **500자**(단어 경계에서 자동 분할).
  * Markdown은 분할 전에 제거됩니다.
  * 속도 제한 없음(Twitch의 내장 속도 제한 사용).


## 관련 항목

  * [채널 라우팅](</ko/channels/channel-routing>) — 메시지의 세션 라우팅
  * [채널 개요](</ko/channels>) — 지원되는 모든 채널
  * [그룹](</ko/channels/groups>) — 그룹 채팅 동작 및 멘션 게이팅
  * [페어링](</ko/channels/pairing>) — DM 인증 및 페어링 흐름
  * [보안](</ko/gateway/security>) — 액세스 모델 및 강화


Was this useful?YesNo