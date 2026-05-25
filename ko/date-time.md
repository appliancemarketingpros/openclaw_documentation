---
title: 날짜 및 시간
source_url: https://docs.openclaw.ai/ko/date-time
scraped_at: 2026-05-25
---

OpenClaw는 기본적으로 **전송 타임스탬프에 호스트 로컬 시간을 사용** 하고, **시스템 프롬프트에서만 사용자 시간대를 사용** 합니다. 제공자 타임스탬프는 보존되므로 도구는 고유한 의미 체계를 유지합니다(현재 시간은 `session_status`를 통해 사용할 수 있음).

## 메시지 엔벌로프(기본값: 로컬)

수신 메시지는 타임스탬프(분 단위 정밀도)로 래핑됩니다.

CodeCopy code
[code]
    [Provider ... 2026-01-05 16:26 PST] message text
[/code]

이 엔벌로프 타임스탬프는 제공자 시간대와 관계없이 **기본적으로 호스트 로컬** 입니다.

이 동작을 재정의할 수 있습니다.

json5Copy code
[code]
    {  agents: {    defaults: {      envelopeTimezone: "local", // "utc" | "local" | "user" | IANA timezone      envelopeTimestamp: "on", // "on" | "off"      envelopeElapsed: "on", // "on" | "off"    },  },}
[/code]

  * `envelopeTimezone: "utc"`는 UTC를 사용합니다.
  * `envelopeTimezone: "local"`은 호스트 시간대를 사용합니다.
  * `envelopeTimezone: "user"`는 `agents.defaults.userTimezone`을 사용합니다(호스트 시간대로 대체됨).
  * 고정 시간대에는 명시적인 IANA 시간대(예: `"America/Chicago"`)를 사용하세요.
  * `envelopeTimestamp: "off"`는 엔벌로프 헤더에서 절대 타임스탬프를 제거합니다.
  * `envelopeElapsed: "off"`는 경과 시간 접미사(`+2m` 스타일)를 제거합니다.


### 예시

**로컬(기본값):**

CodeCopy code
[code]
    [WhatsApp +1555 2026-01-18 00:19 PST] hello
[/code]

**사용자 시간대:**

CodeCopy code
[code]
    [WhatsApp +1555 2026-01-18 00:19 CST] hello
[/code]

**경과 시간 활성화:**

CodeCopy code
[code]
    [WhatsApp +1555 +30s 2026-01-18T05:19Z] follow-up
[/code]

## 시스템 프롬프트: 현재 날짜 및 시간

사용자 시간대를 알고 있으면 시스템 프롬프트에는 프롬프트 캐싱을 안정적으로 유지하기 위해 **시간대만** 포함하는(시계/시간 형식 없음) 전용 **현재 날짜 및 시간** 섹션이 포함됩니다.

CodeCopy code
[code]
    Time zone: America/Chicago
[/code]

에이전트가 현재 시간이 필요할 때는 `session_status` 도구를 사용하세요. 상태 카드에는 타임스탬프 줄이 포함됩니다.

## 시스템 이벤트 줄(기본값: 로컬)

에이전트 컨텍스트에 삽입되는 대기 중인 시스템 이벤트에는 메시지 엔벌로프와 동일한 시간대 선택(기본값: 호스트 로컬)을 사용하는 타임스탬프가 접두사로 붙습니다.

CodeCopy code
[code]
    System: [2026-01-12 12:19:17 PST] Model switched.
[/code]

### 사용자 시간대 및 형식 구성

json5Copy code
[code]
    {  agents: {    defaults: {      userTimezone: "America/Chicago",      timeFormat: "auto", // auto | 12 | 24    },  },}
[/code]

  * `userTimezone`은 프롬프트 컨텍스트의 **사용자 로컬 시간대** 를 설정합니다.
  * `timeFormat`은 프롬프트의 **12시간/24시간 표시** 를 제어합니다. `auto`는 OS 환경설정을 따릅니다.


## 시간 형식 감지(auto)

`timeFormat: "auto"`이면 OpenClaw는 OS 환경설정(macOS/Windows)을 검사하고 로캘 형식으로 대체합니다. 감지된 값은 반복적인 시스템 호출을 피하기 위해 **프로세스별로 캐시** 됩니다.

## 도구 페이로드 및 커넥터(원시 제공자 시간 + 정규화된 필드)

채널 도구는 **제공자 고유 타임스탬프** 를 반환하고 일관성을 위해 정규화된 필드를 추가합니다.

  * `timestampMs`: 에포크 밀리초(UTC)
  * `timestampUtc`: ISO 8601 UTC 문자열


손실되는 정보가 없도록 원시 제공자 필드는 보존됩니다.

  * Slack: API의 에포크 유사 문자열
  * Discord: UTC ISO 타임스탬프
  * Telegram/WhatsApp: 제공자별 숫자/ISO 타임스탬프


로컬 시간이 필요하면 알려진 시간대를 사용해 다운스트림에서 변환하세요.

## 관련 문서

  * [시스템 프롬프트](</ko/concepts/system-prompt>)
  * [시간대](</ko/concepts/timezone>)
  * [메시지](</ko/concepts/messages>)


Was this useful?YesNo