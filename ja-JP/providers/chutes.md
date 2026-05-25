---
title: Chutes
source_url: https://docs.openclaw.ai/ja-JP/providers/chutes
scraped_at: 2026-05-25
---

[Chutes](<https://chutes.ai>) は、オープンソースのモデルカタログを OpenAI互換 API を通じて公開します。OpenClaw は、同梱の `chutes` provider 向けに ブラウザー OAuth と直接 APIキー認証の両方をサポートします。

プロパティ | 値  
---|---  
Provider | `chutes`  
API | OpenAI互換  
ベース URL | `https://llm.chutes.ai/v1`  
認証 | OAuth または APIキー（下記参照）  
  
## はじめに

### OAuth

* ### Run the OAuth onboarding flow

bashCopy code
[code]
    openclaw onboard --auth-choice chutes
[/code]

OpenClaw はブラウザーフローをローカルで起動するか、リモートまたはヘッドレスホストでは URL とリダイレクト貼り付け フローを表示します。OAuth トークンは OpenClaw 認証 プロファイルを通じて自動更新されます。

* ### Verify the default model

オンボーディング後、デフォルトモデルは `chutes/zai-org/GLM-4.7-TEE` に設定され、同梱の Chutes カタログが 登録されます。

### API key

* ### Get an API key

[chutes.ai/settings/api-keys](<https://chutes.ai/settings/api-keys>) でキーを作成します。

* ### Run the API key onboarding flow

bashCopy code
[code]
    openclaw onboard --auth-choice chutes-api-key
[/code]

* ### Verify the default model

オンボーディング後、デフォルトモデルは `chutes/zai-org/GLM-4.7-TEE` に設定され、同梱の Chutes カタログが 登録されます。

## 検出の動作

Chutes 認証が利用可能な場合、OpenClaw はその認証情報を使って Chutes カタログを照会し、 検出されたモデルを使用します。検出に失敗した場合、OpenClaw は 同梱の静的カタログにフォールバックするため、オンボーディングと起動は引き続き動作します。

## デフォルトエイリアス

OpenClaw は、同梱の Chutes カタログに対して 3 つの便利なエイリアスを登録します。

エイリアス | 対象モデル  
---|---  
`chutes-fast` | `chutes/zai-org/GLM-4.7-FP8`  
`chutes-pro` | `chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes-vision` | `chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
  
## 組み込みスターターカタログ

同梱のフォールバックカタログには、現在の Chutes refs が含まれます。

モデル ref  
---  
`chutes/zai-org/GLM-4.7-TEE`  
`chutes/zai-org/GLM-5-TEE`  
`chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes/deepseek-ai/DeepSeek-R1-0528-TEE`  
`chutes/moonshotai/Kimi-K2.5-TEE`  
`chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
`chutes/Qwen/Qwen3-Coder-Next-TEE`  
`chutes/openai/gpt-oss-120b-TEE`  
  
## 設定例

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "chutes/zai-org/GLM-4.7-TEE" },      models: {        "chutes/zai-org/GLM-4.7-TEE": { alias: "Chutes GLM 4.7" },        "chutes/deepseek-ai/DeepSeek-V3.2-TEE": { alias: "Chutes DeepSeek V3.2" },      },    },  },}
[/code]

OAuth overrides

任意の環境変数で OAuth フローをカスタマイズできます。

変数 | 目的  
---|---  
`CHUTES_CLIENT_ID` | カスタム OAuth クライアント ID  
`CHUTES_CLIENT_SECRET` | カスタム OAuth クライアントシークレット  
`CHUTES_OAUTH_REDIRECT_URI` | カスタムリダイレクト URI  
`CHUTES_OAUTH_SCOPES` | カスタム OAuth スコープ  
  
リダイレクトアプリの要件とヘルプについては、[Chutes OAuth docs](<https://chutes.ai/docs/sign-in-with-chutes/overview>) を参照してください。

Notes

  * APIキーと OAuth 検出はどちらも同じ `chutes` provider id を使用します。
  * Chutes モデルは `chutes/<model-id>` として登録されます。
  * 起動時に検出に失敗した場合、同梱の静的カタログが自動的に使用されます。


## 関連

[**Model selection** Provider ルール、モデル refs、フェイルオーバー動作。 ](</ja-JP/concepts/model-providers>) [**Configuration reference** provider 設定を含む完全な設定スキーマ。 ](</ja-JP/gateway/configuration-reference>) [**Chutes** Chutes ダッシュボードと API ドキュメント。 ](<https://chutes.ai>) [**Chutes API keys** Chutes APIキーを作成および管理します。 ](<https://chutes.ai/settings/api-keys>)

Was this useful?YesNo