---
title: Channel 送信 API
source_url: https://docs.openclaw.ai/ja-JP/plugins/sdk-channel-outbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Channel Plugin は、アウトバウンドメッセージ動作を `openclaw/plugin-sdk/channel-outbound` から公開する必要があります。受信/コンテキスト/ディスパッチのオーケストレーションには `openclaw/plugin-sdk/channel-inbound` を使用します。

core は、キューイング、耐久性、汎用 retry ポリシー、hook、receipt、および共有 `message` tool を所有します。Plugin は、ネイティブの送信/編集/削除呼び出し、ターゲットの正規化、プラットフォームのスレッド処理、選択された引用、通知フラグ、アカウント状態、およびプラットフォーム固有の副作用を所有します。

## アダプター

ほとんどの Plugin は 1 つの `message` アダプターを定義します。

tsCopy code
[code]
       defineChannelMessageAdapter,  createMessageReceiptFromOutboundResults,} from "openclaw/plugin-sdk/channel-outbound"; export const demoMessageAdapter = defineChannelMessageAdapter({  id: "demo",  durableFinal: {    capabilities: {      text: true,      replyTo: true,      thread: true,      messageSendingHooks: true,    },  },  send: {    text: async ({ cfg, to, text, accountId, replyToId, threadId, signal }) => {      const sent = await sendDemoMessage({        cfg,        to,        text,        accountId: accountId ?? undefined,        replyToId: replyToId ?? undefined,        threadId: threadId == null ? undefined : String(threadId),        signal,      });       return {        receipt: createMessageReceiptFromOutboundResults({          results: [{ channel: "demo", messageId: sent.id, conversationId: to }],          kind: "text",          threadId: threadId == null ? undefined : String(threadId),          replyToId: replyToId ?? undefined,        }),      };    },  },});
[/code]

ネイティブ transport が実際に保持する capability のみを宣言してください。このサブパスからエクスポートされる contract helper で、宣言した各送信、receipt、ライブプレビュー、および受信 ack capability をカバーしてください。

## 既存のアウトバウンドアダプター

Channel に互換性のある `outbound` アダプターがすでにある場合は、送信コードを重複させずに message アダプターを派生させます。

tsCopy code
[code]
     export const messageAdapter = createChannelMessageAdapterFromOutbound({  id: "demo",  outbound,  durableFinal: {    capabilities: {      text: true,      media: true,    },  },});
[/code]

## 永続的送信

Runtime の送信 helper も `channel-outbound` にあります。

  * `sendDurableMessageBatch(...)`
  * `withDurableMessageSendContext(...)`
  * `deliverInboundReplyWithMessageSendContext(...)`
  * `resolveChannelDraftStreamingChunking(...)` などのドラフトストリーミング/進捗 helper


`sendDurableMessageBatch(...)` は 1 つの明示的な outcome を返します。

  * `sent`: 少なくとも 1 つの表示可能なプラットフォームメッセージが配信された。
  * `suppressed`: プラットフォームメッセージがないことを欠落として扱うべきではない。
  * `partial_failed`: 後続の payload または副作用が失敗する前に、少なくとも 1 つのプラットフォームメッセージが配信された。
  * `failed`: プラットフォーム receipt が生成されなかった。


batch に送信済み、抑制済み、失敗した payload が混在する場合は `payloadOutcomes` を使用します。空のレガシー直接配信結果から hook cancellation を推測しないでください。

## 互換性ディスパッチ

Inbound reply dispatch は、`channel-inbound` の `dispatchChannelInboundReply(...)` を通じて組み立てる必要があります。プラットフォーム配信は delivery アダプターに保持し、message アダプター、永続的送信、receipt、ライブプレビュー、および reply pipeline option には `channel-outbound` を使用します。

Was this useful?YesNo

Open issue