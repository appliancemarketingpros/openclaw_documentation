---
title: Cerebras
source_url: https://docs.openclaw.ai/ja-JP/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>) は、カスタム推論ハードウェア上で高速な OpenAI 互換推論を提供します。OpenClaw には、静的な 4 モデルのカタログを持つバンドル済み Cerebras プロバイダー Plugin が含まれています。

プロパティ | 値  
---|---  
プロバイダー ID | `cerebras`  
Plugin | バンドル済み、`enabledByDefault: true`  
認証環境変数 | `CEREBRAS_API_KEY`  
オンボーディングフラグ | `--auth-choice cerebras-api-key`  
直接指定 CLI フラグ | `--cerebras-api-key <key>`  
API | OpenAI 互換 (`openai-completions`)  
ベース URL | `https://api.cerebras.ai/v1`  
デフォルトモデル | `cerebras/zai-glm-4.7`  
  
## はじめに

* ### API キーを取得する

[Cerebras Cloud Console](<https://cloud.cerebras.ai>) で API キーを作成します。

* ### オンボーディングを実行する

OnboardingCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

Env onlyCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### モデルが利用可能であることを確認する

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

リストには、バンドル済みの 4 つのモデルがすべて含まれている必要があります。`CEREBRAS_API_KEY` が解決されていない場合、`openclaw models status --json` は不足している認証情報を `auth.unusableProfiles` の下に報告します。

## 非対話型セットアップ

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## 組み込みカタログ

OpenClaw は、公開 OpenAI 互換エンドポイントを反映した静的な Cerebras カタログを同梱しています。4 つのモデルはすべて 128k コンテキストと 8,192 の最大出力トークンを共有します。

モデル参照 | 名前 | 推論 | 注記  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | はい | デフォルトモデル、プレビュー推論モデル  
`cerebras/gpt-oss-120b` | GPT OSS 120B | はい | 本番用推論モデル  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | いいえ | プレビュー非推論モデル  
`cerebras/llama3.1-8b` | Llama 3.1 8B | いいえ | 本番用の速度重視モデル  
  
## 手動設定

通常、バンドル済み Plugin により必要なのは API キーだけです。モデルメタデータを上書きしたい場合、または静的カタログに対して `mode: "merge"` で実行したい場合は、明示的な `models.providers.cerebras` 設定を使用します。

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## 関連

[**モデルプロバイダー** プロバイダー、モデル参照、フェイルオーバー動作の選択。 ](</ja-JP/concepts/model-providers>) [**思考モード** 推論に対応した 2 つの Cerebras モデルの推論エフォートレベル。 ](</ja-JP/tools/thinking>) [**設定リファレンス** エージェントのデフォルトとモデル設定。 ](</ja-JP/gateway/config-agents#agent-defaults>) [**モデル FAQ** 認証プロファイル、モデルの切り替え、「no profile」エラーの解決。 ](</ja-JP/help/faq-models>)

Was this useful?YesNo