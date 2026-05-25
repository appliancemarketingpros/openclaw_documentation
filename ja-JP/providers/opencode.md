---
title: OpenCode
source_url: https://docs.openclaw.ai/ja-JP/providers/opencode
scraped_at: 2026-05-25
---

OpenClaw では OpenCode は 2 つのホスト型カタログを公開しています。

カタログ | プレフィックス | ランタイム provider  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
どちらのカタログも同じ OpenCode API キーを使用します。OpenClaw は、上流のモデルごとのルーティングを正しく保つためにランタイム provider ID を分けていますが、オンボーディングとドキュメントでは 1 つの OpenCode セットアップとして扱います。

## はじめに

### Zen catalog

**最適な用途:** 厳選された OpenCode マルチモデルプロキシ（Claude、GPT、Gemini）。

* ### オンボーディングを実行

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

または、キーを直接渡します。

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### Zen モデルをデフォルトに設定

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### モデルが利用可能であることを確認

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Go catalog

**最適な用途:** OpenCode がホストする Kimi、GLM、MiniMax のラインアップ。

* ### オンボーディングを実行

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

または、キーを直接渡します。

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Go モデルをデフォルトに設定

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### モデルが利用可能であることを確認

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## config の例

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## 組み込みカタログ

### Zen

プロパティ | 値  
---|---  
ランタイム provider | `opencode`  
モデル例 | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3-pro`  
  
### Go

プロパティ | 値  
---|---  
ランタイム provider | `opencode-go`  
モデル例 | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## 高度な設定

API キーのエイリアス

`OPENCODE_ZEN_API_KEY` も `OPENCODE_API_KEY` のエイリアスとしてサポートされています。

共有認証情報

セットアップ時に 1 つの OpenCode キーを入力すると、両方のランタイム provider の認証情報が保存されます。各カタログを個別にオンボーディングする必要はありません。

課金とダッシュボード

OpenCode にサインインし、課金情報を追加して、API キーをコピーします。課金とカタログの利用可否は OpenCode ダッシュボードから管理します。

Gemini のリプレイ動作

Gemini ベースの OpenCode ref はプロキシ Gemini パスに留まるため、OpenClaw はそこで Gemini の思考シグネチャのサニタイズを維持しつつ、ネイティブ Gemini のリプレイ検証やブートストラップ書き換えは有効にしません。

非 Gemini のリプレイ動作

非 Gemini の OpenCode ref は最小限の OpenAI 互換リプレイポリシーを維持します。

## 関連

[**Model selection** provider、モデル ref、フェイルオーバー動作の選択。 ](</ja-JP/concepts/model-providers>) [**Configuration reference** エージェント、モデル、provider の完全な config リファレンス。 ](</ja-JP/gateway/configuration-reference>)

Was this useful?YesNo