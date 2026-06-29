---
title: 채널 아웃바운드 API
source_url: https://docs.openclaw.ai/ko/plugins/sdk-channel-outbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Channel Plugin은 아웃바운드 메시지 동작을 `openclaw/plugin-sdk/channel-outbound`에서 노출해야 합니다. 수신/컨텍스트/디스패치 오케스트레이션에는 `openclaw/plugin-sdk/channel-inbound`를 사용하세요.

코어는 큐잉, 내구성, 일반 재시도 정책, 훅, 수신 확인, 공유 `message` 도구를 소유합니다. Plugin은 네이티브 send/edit/delete 호출, 대상 정규화, 플랫폼 스레딩, 선택된 인용, 알림 플래그, 계정 상태, 플랫폼별 부수 효과를 소유합니다.

## 어댑터

대부분의 Plugin은 하나의 `message` 어댑터를 정의합니다.

tsCopy code
[code]
       defineChannelMessageAdapter,  createMessageReceiptFromOutboundResults,} from "openclaw/plugin-sdk/channel-outbound"; export const demoMessageAdapter = defineChannelMessageAdapter({  id: "demo",  durableFinal: {    capabilities: {      text: true,      replyTo: true,      thread: true,      messageSendingHooks: true,    },  },  send: {    text: async ({ cfg, to, text, accountId, replyToId, threadId, signal }) => {      const sent = await sendDemoMessage({        cfg,        to,        text,        accountId: accountId ?? undefined,        replyToId: replyToId ?? undefined,        threadId: threadId == null ? undefined : String(threadId),        signal,      });       return {        receipt: createMessageReceiptFromOutboundResults({          results: [{ channel: "demo", messageId: sent.id, conversationId: to }],          kind: "text",          threadId: threadId == null ? undefined : String(threadId),          replyToId: replyToId ?? undefined,        }),      };    },  },});
[/code]

네이티브 전송이 실제로 보존하는 기능만 선언하세요. 선언한 각 전송, 수신 확인, 라이브 미리보기, 수신 확인 응답 기능은 이 하위 경로에서 내보낸 계약 헬퍼로 포괄하세요.

## 기존 아웃바운드 어댑터

채널에 이미 호환되는 `outbound` 어댑터가 있다면, 전송 코드를 중복하지 말고 메시지 어댑터를 파생하세요.

tsCopy code
[code]
     export const messageAdapter = createChannelMessageAdapterFromOutbound({  id: "demo",  outbound,  durableFinal: {    capabilities: {      text: true,      media: true,    },  },});
[/code]

## 내구성 전송

런타임 전송 헬퍼도 `channel-outbound`에 있습니다.

  * `sendDurableMessageBatch(...)`
  * `withDurableMessageSendContext(...)`
  * `deliverInboundReplyWithMessageSendContext(...)`
  * `resolveChannelDraftStreamingChunking(...)` 같은 초안 스트리밍/진행률 헬퍼


`sendDurableMessageBatch(...)`는 하나의 명시적 결과를 반환합니다.

  * `sent`: 표시되는 플랫폼 메시지가 하나 이상 전달되었습니다.
  * `suppressed`: 플랫폼 메시지가 없는 것으로 처리되어서는 안 됩니다.
  * `partial_failed`: 이후 페이로드 또는 부수 효과가 실패하기 전에 플랫폼 메시지가 하나 이상 전달되었습니다.
  * `failed`: 플랫폼 수신 확인이 생성되지 않았습니다.


배치에 전송, 억제, 실패 페이로드가 섞여 있으면 `payloadOutcomes`를 사용하세요. 빈 레거시 직접 전달 결과에서 훅 취소를 추론하지 마세요.

## 호환성 디스패치

인바운드 답장 디스패치는 `channel-inbound`의 `dispatchChannelInboundReply(...)`를 통해 조립해야 합니다. 플랫폼 전달은 전달 어댑터에 두고, 메시지 어댑터, 내구성 전송, 수신 확인, 라이브 미리보기, 답장 파이프라인 옵션에는 `channel-outbound`를 사용하세요.

Was this useful?YesNo

Open issue