---
title: ClickClack
source_url: https://docs.openclaw.ai/ja-JP/channels/clickclack
scraped_at: 2026-05-25
---

ClickClack は、ファーストクラスの ClickClack ボットトークンを通じて OpenClaw をセルフホストの ClickClack ワークスペースに接続します。

OpenClaw エージェントを ClickClack のボットユーザーとして表示したい場合に使用します。ClickClack は独立したサービスボットとユーザー所有ボットをサポートします。ユーザー所有ボットは `owner_user_id` を保持し、付与したトークンスコープのみを受け取ります。

## クイックセットアップ

ClickClack でボットトークンを作成します。

bashCopy code
[code]
    clickclack admin bot create \  --workspace <workspace_id_or_slug> \  --name "OpenClaw" \  --handle openclaw \  --scopes bot:write \  --plain
[/code]

ユーザー所有ボットの場合は、`--owner <user_id>` を追加します。

OpenClaw を設定します。

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      token: { source: "env", provider: "default", id: "CLICKCLACK_BOT_TOKEN" },      workspace: "default",      defaultTo: "channel:general",      agentId: "clickclack-bot",      replyMode: "model",    },  },}
[/code]

次に実行します。

bashCopy code
[code]
    export CLICKCLACK_BOT_TOKEN="ccb_..."openclaw gateway
[/code]

## 複数のボット

各アカウントは独自の ClickClack リアルタイム接続を開き、独自のボットトークンを使用します。

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      defaultAccount: "service",      accounts: {        service: {          token: { source: "env", provider: "default", id: "CLICKCLACK_SERVICE_BOT_TOKEN" },          workspace: "default",          defaultTo: "channel:general",          agentId: "service-bot",          replyMode: "model",        },        peter: {          token: { source: "env", provider: "default", id: "CLICKCLACK_PETER_BOT_TOKEN" },          workspace: "default",          defaultTo: "dm:usr_...",          agentId: "peter-bot",          replyMode: "model",        },      },    },  },}
[/code]

`replyMode: "model"` は、短いボット返信に `api.runtime.llm.complete` を直接使用します。 アカウントが `agentId` を設定する場合、OpenClaw は明示的な `plugins.entries.clickclack.llm.allowAgentIdOverride` 信頼ビットを要求します。これにより、この Plugin がそのボットエージェント用の補完を実行できます。デフォルトの エージェントルートだけを使用する場合は、オフのままにしてください。

## ターゲット

  * `channel:<name-or-id>` はワークスペースチャンネルに送信します。ベアターゲットのデフォルトは `channel:` です。
  * `dm:<user_id>` はそのユーザーとのダイレクト会話を作成するか再利用します。
  * `thread:<message_id>` は既存のスレッドに返信します。


例:

bashCopy code
[code]
    openclaw message send --channel clickclack --target channel:general --message "hello"openclaw message send --channel clickclack --target dm:usr_123 --message "hello"openclaw message send --channel clickclack --target thread:msg_123 --message "following up"
[/code]

## 権限

ClickClack トークンスコープは ClickClack API によって強制されます。

  * `bot:read`: ワークスペース、チャンネル、メッセージ、スレッド、DM、リアルタイム、プロフィールのデータを読み取ります。
  * `bot:write`: `bot:read` に加えて、チャンネルメッセージ、スレッド返信、DM、アップロードを扱います。
  * `bot:admin`: `bot:write` に加えて、チャンネル作成を扱います。


OpenClaw は通常のエージェントチャットには `bot:write` のみを必要とします。

## トラブルシューティング

  * `ClickClack is not configured`: `channels.clickclack.token` または `CLICKCLACK_BOT_TOKEN` を設定します。
  * `workspace not found`: `workspace` を ClickClack が返したワークスペース ID またはスラッグに設定します。
  * 受信返信がない: トークンにリアルタイム読み取りアクセスがあり、ボットが自分自身のメッセージに返信していないことを確認します。
  * チャンネル送信が失敗する: ボットがワークスペースのメンバーであり、`bot:write` を持っていることを確認します。


Was this useful?YesNo