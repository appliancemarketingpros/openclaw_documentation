---
title: Anthropic
source_url: https://docs.openclaw.ai/ja-JP/providers/anthropic
scraped_at: 2026-05-25
---

Anthropic は **Claude** モデルファミリーを構築しています。OpenClaw は 2 つの認証ルートをサポートします。

  * **API key** — 使用量ベースの課金による Anthropic API への直接アクセス（`anthropic/*` モデル）
  * **Claude CLI** — 同じホスト上の既存の Claude CLI ログインを再利用


## はじめに

### API key

**最適な用途:** 標準的な API アクセスと使用量ベースの課金。

* ### API key を取得する

[Anthropic Console](<https://console.anthropic.com/>) で API key を作成します。

* ### オンボーディングを実行する

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

または、キーを直接渡します。

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### モデルが利用可能であることを確認する

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### 設定例

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "sk-ant-..." },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### Claude CLI

**最適な用途:** 別の API key なしで既存の Claude CLI ログインを再利用する。

* ### Claude CLI がインストール済みでログイン済みであることを確認する

次で確認します。

bashCopy code
[code]
    claude --version
[/code]

* ### オンボーディングを実行する

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

OpenClaw は既存の Claude CLI 認証情報を検出して再利用します。

* ### モデルが利用可能であることを確認する

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### 設定例

正規の Anthropic モデル参照に CLI ランタイムのオーバーライドを組み合わせることを推奨します。

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-7" },      models: {        "anthropic/claude-opus-4-7": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

互換性のため、従来の `claude-cli/claude-opus-4-7` モデル参照も引き続き機能しますが、 新しい設定では provider/model 選択を `anthropic/*` のままにし、実行バックエンドは provider/model ランタイムポリシーに置くべきです。

## thinking のデフォルト（Claude 4.6）

Claude 4.6 モデルは、明示的な thinking レベルが設定されていない場合、OpenClaw でデフォルトで `adaptive` thinking になります。

メッセージごとに `/think:<level>` で、またはモデルパラメータでオーバーライドします。

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { thinking: "adaptive" },        },      },    },  },}
[/code]

## プロンプトキャッシュ

OpenClaw は、API-key 認証向けに Anthropic のプロンプトキャッシュ機能をサポートします。

値 | キャッシュ期間 | 説明  
---|---|---  
`"short"` (デフォルト) | 5 分 | API-key 認証で自動的に適用されます  
`"long"` | 1 時間 | 拡張キャッシュ  
`"none"` | キャッシュなし | プロンプトキャッシュを無効化  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

エージェントごとのキャッシュオーバーライド

モデルレベルのパラメータを基準として使用し、その後 `agents.list[].params` で特定のエージェントをオーバーライドします。

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

設定のマージ順序:

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params`（`id` が一致するもの。キーごとにオーバーライド）


これにより、あるエージェントは長期間有効なキャッシュを保持し、同じモデル上の別のエージェントはバースト的または再利用の少ないトラフィック向けにキャッシュを無効化できます。

Bedrock Claude の注記

  * Bedrock 上の Anthropic Claude モデル（`amazon-bedrock/*anthropic.claude*`）は、設定されている場合 `cacheRetention` のパススルーを受け入れます。
  * Anthropic 以外の Bedrock モデルは、ランタイムで `cacheRetention: "none"` に強制されます。
  * API-key のスマートデフォルトは、明示的な値が設定されていない場合、Claude-on-Bedrock 参照にも `cacheRetention: "short"` をシードします。


## 高度な設定

高速モード

OpenClaw の共有 `/fast` トグルは、Anthropic への直接トラフィック（API-key と `api.anthropic.com` への OAuth）をサポートします。

コマンド | 対応先  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

メディア理解（画像と PDF）

同梱の Anthropic plugin は、画像と PDF の理解を登録します。OpenClaw は 設定された Anthropic 認証からメディア機能を自動解決します。追加の 設定は不要です。

プロパティ | 値  
---|---  
デフォルトモデル | `claude-opus-4-7`  
サポート入力 | 画像、PDF ドキュメント  
  
画像または PDF が会話に添付されると、OpenClaw は自動的に Anthropic メディア理解プロバイダー経由でルーティングします。

1M コンテキストウィンドウ（ベータ）

Anthropic の 1M コンテキストウィンドウはベータゲート付きです。モデルごとに有効化します。

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { context1m: true },        },      },    },  },}
[/code]

OpenClaw はリクエスト上でこれを `anthropic-beta: context-1m-2025-08-07` にマップします。

`params.context1m: true` は、対象となる Opus および Sonnet モデルの Claude CLI バックエンド （`claude-cli/*`）にも適用され、それらの CLI セッションのランタイム コンテキストウィンドウを直接 API の挙動に合わせて拡張します。

Claude Opus 4.7 1M コンテキスト

`anthropic/claude-opus-4.7` とその `claude-cli` バリアントは、デフォルトで 1M コンテキスト ウィンドウを持ちます。`params.context1m: true` は不要です。

## トラブルシューティング

401 エラー / トークンが突然無効になった

Anthropic トークン認証は期限切れになり、取り消される場合があります。新しいセットアップでは、代わりに Anthropic API key を使用してください。

provider "anthropic" の API key が見つかりません

Anthropic 認証は**エージェントごと** です。新しいエージェントはメインエージェントのキーを継承しません。そのエージェントでオンボーディングを再実行するか（または Gateway ホストで API key を設定し）、その後 `openclaw models status` で確認してください。

profile "anthropic:default" の認証情報が見つかりません

`openclaw models status` を実行して、どの認証プロファイルがアクティブかを確認してください。オンボーディングを再実行するか、そのプロファイルパスに API key を設定してください。

利用可能な認証プロファイルがありません（すべてクールダウン中）

`openclaw models status --json` で `auth.unusableProfiles` を確認してください。Anthropic のレート制限クールダウンはモデルスコープの場合があるため、同系統の別の Anthropic モデルはまだ利用できる場合があります。別の Anthropic プロファイルを追加するか、クールダウンを待ってください。

## 関連

[**モデル選択** プロバイダー、モデル参照、フェイルオーバー挙動の選択。 ](</ja-JP/concepts/model-providers>) [**CLI バックエンド** Claude CLI バックエンドのセットアップとランタイム詳細。 ](</ja-JP/gateway/cli-backends>) [**プロンプトキャッシュ** プロバイダー全体でプロンプトキャッシュがどのように機能するか。 ](</ja-JP/reference/prompt-caching>) [**OAuth と認証** 認証の詳細と認証情報の再利用ルール。 ](</ja-JP/gateway/authentication>)

Was this useful?YesNo