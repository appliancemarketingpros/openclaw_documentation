---
title: DeepSeek
source_url: https://docs.openclaw.ai/ja-JP/providers/deepseek
scraped_at: 2026-05-25
---

[DeepSeek](<https://www.deepseek.com>) は、OpenAI 互換 API を備えた強力な AI モデルを提供します。

プロパティ | 値  
---|---  
プロバイダー | `deepseek`  
認証 | `DEEPSEEK_API_KEY`  
API | OpenAI 互換  
ベース URL | `https://api.deepseek.com`  
  
## はじめに

* ### API キーを取得する

[platform.deepseek.com](<https://platform.deepseek.com/api_keys>) で API キーを作成します。

* ### オンボーディングを実行する

bashCopy code
[code]
    openclaw onboard --auth-choice deepseek-api-key
[/code]

これにより API キーの入力を求められ、`deepseek/deepseek-v4-flash` がデフォルトモデルとして設定されます。

* ### モデルが利用可能であることを確認する

bashCopy code
[code]
    openclaw models list --provider deepseek
[/code]

実行中の Gateway を必要とせずにバンドルされた静的カタログを調べるには、 次を使用します。

bashCopy code
[code]
    openclaw models list --all --provider deepseek
[/code]

非対話型セットアップ

スクリプト化されたインストールやヘッドレスインストールでは、すべてのフラグを直接渡します。

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice deepseek-api-key \  --deepseek-api-key "$DEEPSEEK_API_KEY" \  --skip-health \  --accept-risk
[/code]

## 組み込みカタログ

モデル参照 | 名前 | 入力 | コンテキスト | 最大出力 | 注記  
---|---|---|---|---|---  
`deepseek/deepseek-v4-flash` | DeepSeek V4 Flash | text | 1,000,000 | 384,000 | デフォルトモデル。V4 の thinking 対応サーフェス  
`deepseek/deepseek-v4-pro` | DeepSeek V4 Pro | text | 1,000,000 | 384,000 | V4 の thinking 対応サーフェス  
`deepseek/deepseek-chat` | DeepSeek Chat | text | 131,072 | 8,192 | DeepSeek V3.2 の非 thinking サーフェス  
`deepseek/deepseek-reasoner` | DeepSeek Reasoner | text | 131,072 | 65,536 | 推論対応の V3.2 サーフェス  
  
## Thinking とツール

DeepSeek V4 の thinking セッションには、ほとんどの OpenAI 互換プロバイダーよりも厳格な再生契約があります。thinking が有効なターンでツールを使用した後、DeepSeek は後続リクエストで、そのターンから再生された assistant メッセージに `reasoning_content` が含まれることを期待します。OpenClaw はこれを DeepSeek Plugin 内で処理するため、通常の複数ターンのツール使用は `deepseek/deepseek-v4-flash` と `deepseek/deepseek-v4-pro` で機能します。

既存のセッションを別の OpenAI 互換プロバイダーから DeepSeek V4 モデルに切り替えると、古い assistant ツール呼び出しターンにはネイティブの DeepSeek `reasoning_content` がない場合があります。OpenClaw は DeepSeek V4 thinking リクエストのために、再生された assistant メッセージ上のその欠落フィールドを補完するため、プロバイダーは `/new` を必要とせずに履歴を受け入れられます。

OpenClaw で thinking が無効になっている場合 (UI の **None** 選択を含む)、 OpenClaw は DeepSeek `thinking: { type: "disabled" }` を送信し、送信履歴から再生された `reasoning_content` を取り除きます。これにより、thinking 無効セッションは非 thinking の DeepSeek パスに維持されます。

デフォルトの高速パスには `deepseek/deepseek-v4-flash` を使用します。 より強力な V4 モデルが必要で、より高いコストやレイテンシを許容できる場合は `deepseek/deepseek-v4-pro` を使用します。

## ライブテスト

直接ライブモデルスイートには、モダンモデルセットの DeepSeek V4 が含まれています。 DeepSeek V4 の直接モデルチェックのみを実行するには、次を使用します。

bashCopy code
[code]
    OPENCLAW_LIVE_PROVIDERS=deepseek \OPENCLAW_LIVE_MODELS="deepseek/deepseek-v4-flash,deepseek/deepseek-v4-pro" \pnpm test:live src/agents/models.profiles.live.test.ts
[/code]

このライブチェックでは、両方の V4 モデルが完了できることと、thinking/ツールの後続ターンで DeepSeek が必要とする再生ペイロードが保持されることを確認します。

## 設定例

json5Copy code
[code]
    {  env: { DEEPSEEK_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "deepseek/deepseek-v4-flash" },    },  },}
[/code]

## 関連

[**モデル選択** プロバイダー、モデル参照、フェイルオーバー動作の選択。 ](</ja-JP/concepts/model-providers>) [**設定リファレンス** agents、models、providers の完全な設定リファレンス。 ](</ja-JP/gateway/configuration-reference>)

Was this useful?YesNo