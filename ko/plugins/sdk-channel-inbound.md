---
title: 채널 인바운드 API
source_url: https://docs.openclaw.ai/ko/plugins/sdk-channel-inbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Channel Plugin은 수신 경로를 인바운드 및 메시지 명사로 모델링해야 합니다.

textCopy code
[code]
    platform event -> inbound facts/context -> agent reply -> message delivery
[/code]

인바운드 이벤트 정규화, 형식 지정, 루트, 오케스트레이션에는 `openclaw/plugin-sdk/channel-inbound`를 사용하세요. 네이티브 전송, 수신 확인, 내구성 있는 전달, 실시간 미리보기 동작에는 `openclaw/plugin-sdk/channel-outbound`를 사용하세요.

## 핵심 헬퍼

tsCopy code
[code]
       buildChannelInboundEventContext,  runChannelInboundEvent,  dispatchChannelInboundReply,} from "openclaw/plugin-sdk/channel-inbound";
[/code]

  * `buildChannelInboundEventContext(...)`: 정규화된 채널 사실을 프롬프트/세션 컨텍스트로 투영합니다. 채널 소유 발신자/채팅 메타데이터를 Plugin hook `ctx.channelContext`로 전달하려면 `channelContext`를 사용하세요. 채널별 필드에는 이 하위 경로의 `PluginHookChannelSenderContext` 또는 `PluginHookChannelChatContext`를 확장하세요.
  * `runChannelInboundEvent(...)`: 하나의 인바운드 플랫폼 이벤트에 대해 수집, 분류, 사전 검사, 해석, 기록, 디스패치, 마무리를 실행합니다.
  * `dispatchChannelInboundReply(...)`: 전달 어댑터를 사용해 이미 조립된 인바운드 응답을 기록하고 디스패치합니다.


주입된 Plugin 런타임은 이미 런타임 객체를 받는 번들/네이티브 채널을 위해 `runtime.channel.inbound.*` 아래에 동일한 고수준 헬퍼를 노출합니다.

tsCopy code
[code]
    await runtime.channel.inbound.run({  channel: "demo",  accountId,  raw: platformEvent,  adapter: {    ingest: normalizePlatformEvent,    resolveTurn: resolveInboundReply,  },});
[/code]

호환성 디스패처는 `dispatchChannelInboundReply(...)` 입력을 조립하고 플랫폼 전달은 전달 어댑터에 유지해야 합니다. 새 전송 경로는 메시지 어댑터와 내구성 있는 메시지 헬퍼를 우선 사용해야 합니다.

## 마이그레이션

이전 `runtime.channel.turn.*` 런타임 별칭은 제거되었습니다. 다음을 사용하세요.

  * 원시 인바운드 이벤트에는 `runtime.channel.inbound.run(...)`.
  * 조립된 응답 컨텍스트에는 `runtime.channel.inbound.dispatchReply(...)`.
  * 인바운드 컨텍스트 페이로드에는 `runtime.channel.inbound.buildContext(...)`.
  * 자체 디스패치 클로저를 이미 조립하는 채널 소유 준비된 디스패치 경로에만 `runtime.channel.inbound.runPreparedReply(...)`.


새 Plugin 코드는 `turn`이라는 이름의 채널 API를 도입하지 않아야 합니다. 모델 또는 에이전트 턴 어휘는 에이전트/Provider 코드 안에 두고, Channel Plugin은 인바운드, 메시지, 전달, 응답 용어를 사용합니다.

Was this useful?YesNo

Open issue