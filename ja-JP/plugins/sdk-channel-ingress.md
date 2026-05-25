---
title: チャネル受信 API
source_url: https://docs.openclaw.ai/ja-JP/plugins/sdk-channel-ingress
scraped_at: 2026-05-25
---

# チャネル ingress API

チャネル ingress は、受信チャネルイベントの実験的なアクセス制御境界です。 受信パスには `openclaw/plugin-sdk/channel-ingress-runtime` を使用します。 古い `openclaw/plugin-sdk/channel-ingress` サブパスは、サードパーティ Plugin 向けの 非推奨の互換 facade として引き続きエクスポートされます。

Plugin はプラットフォームの事実と副作用を所有します。コアは汎用ポリシーを所有します: DM/グループ allowlist、ペアリングストアの DM エントリ、ルートゲート、コマンドゲート、イベント認可、 メンションによるアクティベーション、秘匿済み診断、許可判定です。

## ランタイムリゾルバー

tsCopy code
[code]
       defineStableChannelIngressIdentity,  resolveChannelMessageIngress,} from "openclaw/plugin-sdk/channel-ingress-runtime"; const identity = defineStableChannelIngressIdentity({  key: "platform-user-id",  normalize: normalizePlatformUserId,  sensitivity: "pii",}); const result = await resolveChannelMessageIngress({  channelId: "my-channel",  accountId,  identity,  subject: { stableId: platformUserId },  conversation: { kind: isGroup ? "group" : "direct", id: conversationId },  event: { kind: "message", authMode: "inbound", mayPair: !isGroup },  policy: {    dmPolicy: config.dmPolicy,    groupPolicy: config.groupPolicy,    groupAllowFromFallbackToAllowFrom: true,  },  allowFrom: config.allowFrom,  groupAllowFrom: config.groupAllowFrom,  accessGroups: cfg.accessGroups,  route,  readStoreAllowFrom,  command: hasControlCommand ? { allowTextCommands: true, hasControlCommand } : undefined,});
[/code]

有効な allowlist、コマンド所有者、コマンドグループを事前計算しないでください。 リゾルバーはそれらを、生の allowlist、ストアコールバック、ルート記述子、 アクセスグループ、ポリシー、会話種別から導出します。

## 結果

バンドルされた Plugin は、モダンな projection を直接消費するべきです:

  * `ingress`: 順序付きのゲート判定と許可
  * `senderAccess`: 送信者/会話の認可のみ
  * `routeAccess`: ルートおよびルート送信者 projection
  * `commandAccess`: コマンド認可。コマンドゲートが実行されなかった場合は false
  * `activationAccess`: メンション/アクティベーション結果


イベント認可は、順序付きの `ingress.graph` と決定的な `ingress.reasonCode` で引き続き利用できます。 個別のイベント projection は出力されません。

非推奨のサードパーティ SDK ヘルパーは、古い形状を内部で再構築する場合があります。 新しいバンドル済み受信パスは、モダンな結果をローカル DTO に戻して変換するべきではありません。

## アクセスグループ

`accessGroup:<name>` エントリは秘匿されたままです。コアは静的な `message.senders` グループを自ら解決し、プラットフォーム検索を必要とする動的グループに対してのみ `resolveAccessGroupMembership` を呼び出します。欠落、未サポート、失敗したグループは閉じた状態で失敗します。

## イベントモード

`authMode` | 意味  
---|---  
`inbound` | 通常の受信送信者ゲート  
`command` | コールバックまたはスコープ付きボタン用のコマンドゲート  
`origin-subject` | アクターは元のメッセージ subject と一致する必要がある  
`route-only` | ルートスコープの信頼済みイベント専用のルートゲート  
`none` | Plugin 所有の内部イベントは共有認可をバイパスする  
  
リアクション、ボタン、コールバック、ネイティブコマンドには `mayPair: false` を使用します。

## ルートとアクティベーション

ルーム、トピック、ギルド、スレッド、またはネストされたルートポリシーにはルート記述子を使用します:

tsCopy code
[code]
    route: {  id: "room",  allowed: roomAllowed,  enabled: roomEnabled,  senderPolicy: "replace",  senderAllowFrom: roomAllowFrom,  blockReason: "room_sender_not_allowlisted",}
[/code]

Plugin に複数の任意ルート記述子がある場合は `channelIngressRoutes(...)` を使用します。 これは、ルートの事実を汎用的に保ち、各記述子の `precedence` 順に並べたまま、 無効な分岐をフィルタリングします。

メンションゲートはアクティベーションゲートです。メンションが一致しない場合は `admission: "skip"` を返すため、ターンカーネルは observe-only ターンを処理しません。 ほとんどのチャネルでは、送信者ゲートとコマンドゲートの後にアクティベーションを残すべきです。 送信者 allowlist のノイズの前に、メンションされていないトラフィックを静かにする必要がある公開チャットサーフェスは、 テキストコマンドのバイパスが無効な場合に `activation.order: "before-sender"` を選択できます。 bot スレッド内の返信など、暗黙のアクティベーションを持つチャネルは `activation.allowedImplicitMentionKinds` を渡すことができます。その場合、project された `activationAccess.shouldBypassMention` は、コマンドまたは暗黙のアクティベーションが 明示的なメンションをバイパスしたタイミングを報告します。

## 秘匿

生の送信者値と生の allowlist エントリは、リゾルバー入力専用です。それらは 解決済み状態、判定、診断、スナップショット、互換性ファクトに出現してはなりません。 不透明な subject ID、エントリ ID、ルート ID、診断 ID を使用してください。

## 検証

bashCopy code
[code]
    pnpm test src/channels/message-access/message-access.test.ts src/plugin-sdk/channel-ingress-runtime.test.tspnpm plugin-sdk:api:check
[/code]

Was this useful?YesNo