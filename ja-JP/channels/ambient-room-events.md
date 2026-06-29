---
title: 周囲のルームイベント
source_url: https://docs.openclaw.ai/ja-JP/channels/ambient-room-events
scraped_at: 2026-06-29
---

ChannelsConfiguration

アンビエントルームイベントにより、OpenClaw はメンションされていないグループやチャンネルの会話を静かなコンテキストとして処理できます。エージェントはメモリとセッション状態を更新できますが、エージェントが明示的に `message` ツールを呼び出さない限り、ルームは沈黙したままです。

常時オンのグループチャットでは、これが推奨モードです。`messages.groupChat.unmentionedInbound: "room_event"` と `messages.groupChat.visibleReplies: "message_tool"` を組み合わせます。エージェントが聞き取り、返信が有用なタイミングを判断し、`NO_REPLY` と答える古いプロンプトパターンを避けるべき場合に使用します。

現在サポートされているもの: Discord ギルドチャンネル、Slack チャンネルとプライベートチャンネル、Slack 複数人 DM、Telegram グループまたはスーパーグループ。他のグループチャンネルは、そのチャンネルページにアンビエントルームイベントをサポートすると記載されていない限り、既存のグループ動作を維持します。

## 推奨セットアップ

グローバルなグループチャット動作を設定します。

json5Copy code
[code]
    {  messages: {    groupChat: {      unmentionedInbound: "room_event",      visibleReplies: "message_tool",      historyLimit: 50,    },  },}
[/code]

次に、そのルームのメンションゲートを無効にして、ルーム自体を常時オンとして設定します。チャンネルは引き続き、通常の `groupPolicy`、ルーム許可リスト、送信者許可リストで許可されている必要があります。

設定を保存すると、Gateway は `messages` 設定をホットリロードします。ファイル監視または設定リロードが無効な場合のみ再起動してください。

## 変更されること

`messages.groupChat.unmentionedInbound: "room_event"` の場合:

  * メンションされていない、許可済みのグループまたはチャンネルメッセージは静かなルームイベントになります
  * メンションされたメッセージはユーザーリクエストのままです
  * テキストコマンドとネイティブコマンドはユーザーリクエストのままです
  * 中止または停止リクエストはユーザーリクエストのままです
  * ダイレクトメッセージはユーザーリクエストのままです


ルームイベントは厳格な可視配信を使用します。最終的なアシスタントテキストは非公開です。エージェントはルームに投稿するために `message(action=send)` を呼び出す必要があります。

## Discord の例

json5Copy code
[code]
    {  messages: {    groupChat: {      unmentionedInbound: "room_event",      visibleReplies: "message_tool",      historyLimit: 50,    },  },  channels: {    discord: {      groupPolicy: "allowlist",      guilds: {        "&lt;DISCORD_SERVER_ID&gt;": {          requireMention: false,          users: ["&lt;YOUR_DISCORD_USER_ID&gt;"],        },      },    },  },}
[/code]

1 つのチャンネルだけをアンビエントにする場合は、チャンネルごとの Discord 設定を使用します。

json5Copy code
[code]
    {  channels: {    discord: {      guilds: {        "&lt;DISCORD_SERVER_ID&gt;": {          channels: {            "&lt;DISCORD_CHANNEL_ID_OR_NAME&gt;": {              allow: true,              requireMention: false,            },          },        },      },    },  },}
[/code]

## Slack の例

Slack チャンネル許可リストは ID 優先です。`#channel-name` ではなく、`C12345678` のようなチャンネル ID を使用します。

json5Copy code
[code]
    {  messages: {    groupChat: {      unmentionedInbound: "room_event",      visibleReplies: "message_tool",      historyLimit: 50,    },  },  channels: {    slack: {      groupPolicy: "allowlist",      channels: {        "&lt;SLACK_CHANNEL_ID&gt;": {          allow: true,          requireMention: false,        },      },    },  },}
[/code]

## Telegram の例

Telegram グループでは、ボットが通常のグループメッセージを見られる必要があります。`requireMention: false` の場合は、BotFather のプライバシーモードを無効にするか、ボットへ完全なグループトラフィックを配信する別の Telegram セットアップを使用します。

json5Copy code
[code]
    {  messages: {    groupChat: {      unmentionedInbound: "room_event",      visibleReplies: "message_tool",      historyLimit: 50,    },  },  channels: {    telegram: {      groups: {        "&lt;TELEGRAM_GROUP_CHAT_ID&gt;": {          groupPolicy: "open",          requireMention: false,        },      },    },  },}
[/code]

Telegram グループ ID は通常、`-1001234567890` のような負の数です。`openclaw logs --follow` から `chat.id` を読み取るか、グループメッセージを ID ヘルパーボットへ転送するか、Bot API の `getUpdates` を調べます。

## エージェント固有ポリシー

複数のエージェントが同じルームを共有しているが、メンションされていない会話をアンビエントコンテキストとして扱うべきエージェントが 1 つだけの場合は、エージェントのオーバーライドを使用します。

json5Copy code
[code]
    {  messages: {    groupChat: {      visibleReplies: "message_tool",    },  },  agents: {    list: [      {        id: "main",        groupChat: {          unmentionedInbound: "room_event",          mentionPatterns: ["@openclaw", "openclaw"],        },      },    ],  },}
[/code]

エージェント固有の `agents.list[].groupChat.unmentionedInbound` 値は、そのエージェントの `messages.groupChat.unmentionedInbound` を上書きします。

## 可視返信モード

`messages.groupChat.visibleReplies` のデフォルトは、通常のグループまたはチャンネルのユーザーリクエストでは `"automatic"` です。明示的なメッセージツール呼び出しを要求せずに、最終的なアシスタントテキストを可視状態で投稿したい場合は、このデフォルトを維持します。

アンビエントな常時オンルームでは、特に GPT 5.5 のような最新世代のツール信頼性が高いモデルと組み合わせる場合、`messages.groupChat.visibleReplies: "message_tool"` が引き続き推奨されます。これにより、エージェントはメッセージツールを呼び出して、いつ発言するかを判断できます。モデルがツールを呼び出さずに最終テキストを返した場合、OpenClaw はその最終テキストを非公開に保ち、抑制された配信メタデータをログに記録します。

他のグループリクエストが自動返信を使用している場合でも、ルームイベントは厳格なままです。メンションされていないアンビエントルームイベントでは、可視出力のために引き続き `message(action=send)` が必要です。

## 履歴

`messages.groupChat.historyLimit` は、グローバルなグループ履歴のデフォルトを制御します。チャンネルは `channels.<channel>.historyLimit` でこれを上書きでき、一部のチャンネルはアカウントごとの履歴制限もサポートします。

グループ履歴コンテキストを無効にするには、`historyLimit: 0` を設定します。

サポートされているルームイベントチャンネルは、最近のアンビエントルームメッセージをコンテキストとして保持します。Discord は可視の Discord 送信が成功するまでルームイベント履歴を保持するため、メッセージツール配信の前に静かなコンテキストが失われることはありません。

## トラブルシューティング

ルームに入力中表示やトークン使用量が出るのに可視メッセージがない場合:

  1. ルームがチャンネル許可リストと送信者許可リストで許可されていることを確認します。
  2. 期待するルームレベルで `requireMention: false` が設定されていることを確認します。
  3. `messages.groupChat.unmentionedInbound` またはエージェントのオーバーライドが `"room_event"` かどうかを確認します。
  4. 抑制された最終ペイロードメタデータまたは `didSendViaMessagingTool: false` がログにないか確認します。
  5. 通常のグループリクエストでは、最終返信を自動投稿したい場合、`messages.groupChat.visibleReplies: "automatic"` を維持または復元します。`message_tool` を使用するアンビエントルームでは、ツールを確実に呼び出すモデルまたはランタイムを使用します。


Telegram のアンビエントルームがまったくトリガーされない場合は、BotFather のプライバシーモードを確認し、Gateway が通常のグループメッセージを受信していることを検証します。

Slack のアンビエントルームがトリガーされない場合は、チャンネルキーが Slack チャンネル ID であり、アプリにそのルームタイプに必要な `channels:history` または `groups:history` スコープがあることを検証します。

## 関連

  * [グループ](</ja-JP/channels/groups>)
  * [Discord](</ja-JP/channels/discord>)
  * [Slack](</ja-JP/channels/slack>)
  * [Telegram](</ja-JP/channels/telegram>)
  * [チャンネルのトラブルシューティング](</ja-JP/channels/troubleshooting>)
  * [チャンネル設定リファレンス](</ja-JP/gateway/config-channels>)


Was this useful?YesNo

Open issue