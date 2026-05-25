---
title: OpenCode Go
source_url: https://docs.openclaw.ai/ja-JP/providers/opencode-go
scraped_at: 2026-05-25
---

OpenCode Go は [OpenCode](</ja-JP/providers/opencode>) 内の Go カタログです。 Zen カタログと同じ `OPENCODE_API_KEY` を使用しますが、ランタイムの provider id は `opencode-go` のままなので、上流のモデルごとのルーティングが 正しく維持されます。

Property | Value  
---|---  
ランタイム provider | `opencode-go`  
認証 | `OPENCODE_API_KEY`  
親セットアップ | [OpenCode](</ja-JP/providers/opencode>)  
  
## 組み込みカタログ

OpenClaw は Go カタログの大半の行をバンドル済みの pi モデルレジストリから取得し、 レジストリが追いつくまで現在の上流行を補完します。現在のモデル一覧は `openclaw models list --provider opencode-go` を実行してください。

この provider には次が含まれます。

Model ref | 名前  
---|---  
`opencode-go/glm-5` | GLM-5  
`opencode-go/glm-5.1` | GLM-5.1  
`opencode-go/kimi-k2.5` | Kimi K2.5  
`opencode-go/kimi-k2.6` | Kimi K2.6 (3x 上限)  
`opencode-go/deepseek-v4-pro` | DeepSeek V4 Pro  
`opencode-go/deepseek-v4-flash` | DeepSeek V4 Flash  
`opencode-go/mimo-v2-omni` | MiMo V2 Omni  
`opencode-go/mimo-v2-pro` | MiMo V2 Pro  
`opencode-go/minimax-m2.5` | MiniMax M2.5  
`opencode-go/minimax-m2.7` | MiniMax M2.7  
`opencode-go/qwen3.5-plus` | Qwen3.5 Plus  
`opencode-go/qwen3.6-plus` | Qwen3.6 Plus  
  
## はじめに

### 対話式

* ### オンボーディングを実行する

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

* ### Go モデルをデフォルトに設定する

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### モデルが利用可能であることを確認する

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

### 非対話式

* ### キーを直接渡す

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### モデルが利用可能であることを確認する

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## config の例

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "YOUR_API_KEY_HERE" }, // pragma: allowlist secret  agents: { defaults: { model: { primary: "opencode-go/kimi-k2.6" } } },}
[/code]

## 高度な設定

ルーティング動作

モデル ref が `opencode-go/...` を使用している場合、OpenClaw はモデルごとのルーティングを自動的に処理します。追加の provider config は不要です。

ランタイム ref 規約

ランタイム ref は明示的なままです: Zen は `opencode/...`、Go は `opencode-go/...`。 これにより、両方のカタログで上流のモデルごとのルーティングを正しく維持できます。

共有認証情報

同じ `OPENCODE_API_KEY` が Zen と Go の両方のカタログで使用されます。セットアップ中にキーを入力すると、両方のランタイム provider 用の認証情報が保存されます。

## 関連

[**OpenCode (親)** 共有オンボーディング、カタログ概要、高度な注記。 ](</ja-JP/providers/opencode>) [**モデル選択** provider、model ref、フェイルオーバー動作の選び方。 ](</ja-JP/concepts/model-providers>)

Was this useful?YesNo