---
title: チャネル受信 API
source_url: https://docs.openclaw.ai/ja-JP/plugins/sdk-channel-inbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Channel plugins は、受信パスを inbound と message の名詞でモデル化する必要があります。

textCopy code
[code]
    platform event -> inbound facts/context -> agent reply -> message delivery
[/code]

受信イベントの正規化、フォーマット、ルート、オーケストレーションには `openclaw/plugin-sdk/channel-inbound` を使用します。 ネイティブな送信、受領、永続的デリバリー、ライブプレビュー動作には `openclaw/plugin-sdk/channel-outbound` を使用します。

## コアヘルパー

tsCopy code
[code]
       buildChannelInboundEventContext,  runChannelInboundEvent,  dispatchChannelInboundReply,} from "openclaw/plugin-sdk/channel-inbound";
[/code]

  * `buildChannelInboundEventContext(...)`: 正規化されたチャンネルのファクトを プロンプト/セッションコンテキストへ投影します。`channelContext` を使用して、チャンネル所有の 送信者/チャットメタデータを Plugin hook `ctx.channelContext` に渡します。 チャンネル固有フィールドには、このサブパスの `PluginHookChannelSenderContext` または `PluginHookChannelChatContext` を拡張します。
  * `runChannelInboundEvent(...)`: 1 つの受信プラットフォームイベントについて、取り込み、分類、事前確認、解決、 記録、ディスパッチ、完了処理を実行します。
  * `dispatchChannelInboundReply(...)`: すでに組み立て済みの受信返信を、デリバリーアダプターで記録してディスパッチします。


注入された Plugin ランタイムは、すでにランタイムオブジェクトを受け取っているバンドル/ネイティブチャンネル向けに、 同じ高レベルヘルパーを `runtime.channel.inbound.*` の下で公開します。

tsCopy code
[code]
    await runtime.channel.inbound.run({  channel: "demo",  accountId,  raw: platformEvent,  adapter: {    ingest: normalizePlatformEvent,    resolveTurn: resolveInboundReply,  },});
[/code]

互換ディスパッチャーは `dispatchChannelInboundReply(...)` の入力を組み立て、 プラットフォームデリバリーはデリバリーアダプター内に保つ必要があります。新しい送信パスでは、 message アダプターと永続的 message ヘルパーを優先してください。

## 移行

古い `runtime.channel.turn.*` ランタイムエイリアスは削除されました。以下を使用してください。

  * 生の受信イベントには `runtime.channel.inbound.run(...)`。
  * 組み立て済み返信コンテキストには `runtime.channel.inbound.dispatchReply(...)`。
  * 受信コンテキストペイロードには `runtime.channel.inbound.buildContext(...)`。
  * すでに独自のディスパッチクロージャーを組み立てている、チャンネル所有の準備済み ディスパッチパスにのみ `runtime.channel.inbound.runPreparedReply(...)`。


新しい Plugin コードでは、`turn` という名前のチャンネル API を導入しないでください。モデルまたは agent turn の語彙は agent/provider コード内に保ち、channel plugins では inbound、 message、delivery、reply の用語を使用します。

Was this useful?YesNo

Open issue