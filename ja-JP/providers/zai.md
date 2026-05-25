---
title: Z.AI
source_url: https://docs.openclaw.ai/ja-JP/providers/zai
scraped_at: 2026-05-25
---

[Z.AI](<http://Z.AI>) は **GLM** モデル向けの API プラットフォームです。GLM 用の REST API を提供し、認証には API キーを使用します。[Z.AI](<http://Z.AI>) コンソールで API キーを作成してください。OpenClaw は [Z.AI](<http://Z.AI>) API キーとともに `zai` プロバイダーを使用します。

  * プロバイダー: `zai`
  * 認証: `ZAI_API_KEY`
  * API: [Z.AI](<http://Z.AI>) Chat Completions (Bearer 認証)


## はじめに

### エンドポイントの自動検出

**最適な用途:** ほとんどのユーザー。OpenClaw はキーから一致する [Z.AI](<http://Z.AI>) エンドポイントを検出し、正しいベース URL を自動的に適用します。

* ### オンボーディングを実行する

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### デフォルトモデルを設定する

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### モデルが一覧に表示されることを確認する

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### 明示的なリージョンエンドポイント

**最適な用途:** 特定の Coding Plan または汎用 API サーフェスを強制したいユーザー。

* ### 適切なオンボーディングの選択肢を選ぶ

bashCopy code
[code]
    # Coding Plan Global (recommended for Coding Plan users)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (China region)openclaw onboard --auth-choice zai-coding-cn # General APIopenclaw onboard --auth-choice zai-global # General API CN (China region)openclaw onboard --auth-choice zai-cn
[/code]

* ### デフォルトモデルを設定する

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### モデルが一覧に表示されることを確認する

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## 組み込みカタログ

OpenClaw はバンドルされた `zai` プロバイダーカタログを Plugin マニフェストで同梱しているため、読み取り専用の一覧表示ではプロバイダーランタイムを読み込まずに既知の GLM 行を表示できます。

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

マニフェストに基づくカタログには現在、次が含まれます。

モデル参照 | 注記  
---|---  
`zai/glm-5.1` | デフォルトモデル  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## 高度な設定

未知の GLM-5 モデルの前方解決

未知の `glm-5*` ID も、その ID が現在の GLM-5 ファミリーの形状に一致する場合、`glm-4.7` テンプレートからプロバイダー所有のメタデータを合成することで、バンドルされたプロバイダーパス上で引き続き前方解決されます。

ツール呼び出しストリーミング

[Z.AI](<http://Z.AI>) のツール呼び出しストリーミングでは、`tool_stream` がデフォルトで有効になっています。無効にするには、次のようにします。

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

Thinking と保持された thinking

[Z.AI](<http://Z.AI>) thinking は OpenClaw の `/think` コントロールに従います。thinking がオフの場合、OpenClaw は、表示テキストの前に `reasoning_content` で出力予算を消費する応答を避けるために、`thinking: { type: "disabled" }` を送信します。

保持された thinking はオプトインです。これは、[Z.AI](<http://Z.AI>) が完全な履歴 `reasoning_content` の再生を必要とし、プロンプトトークンが増えるためです。モデルごとに有効化します。

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.1": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

有効化され、thinking がオンの場合、OpenClaw は `thinking: { type: "enabled", clear_thinking: false }` を送信し、同じ OpenAI 互換トランスクリプトについて以前の `reasoning_content` を再生します。

上級ユーザーは、`params.extra_body.thinking` で正確なプロバイダーペイロードを引き続き上書きできます。

画像理解

バンドルされた [Z.AI](<http://Z.AI>) Plugin は画像理解を登録します。

プロパティ | 値  
---|---  
モデル | `glm-4.6v`  
  
画像理解は、設定済みの [Z.AI](<http://Z.AI>) 認証から自動解決されます。追加設定は不要です。

認証の詳細

  * [Z.AI](<http://Z.AI>) は API キーによる Bearer 認証を使用します。
  * `zai-api-key` オンボーディングの選択肢は、キーのプレフィックスから一致する [Z.AI](<http://Z.AI>) エンドポイントを自動検出します。
  * 特定の API サーフェスを強制したい場合は、明示的なリージョン選択肢 (`zai-coding-global`, `zai-coding-cn`, `zai-global`, `zai-cn`) を使用します。


## 関連

[**GLM モデルファミリー** GLM のモデルファミリー概要。 ](</ja-JP/providers/glm>) [**モデル選択** プロバイダー、モデル参照、フェイルオーバー動作の選択。 ](</ja-JP/concepts/model-providers>)

Was this useful?YesNo