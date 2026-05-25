---
title: StepFun
source_url: https://docs.openclaw.ai/ja-JP/providers/stepfun
scraped_at: 2026-05-25
---

OpenClaw には、2 つのプロバイダー ID を持つ StepFun プロバイダー Plugin がバンドルされています。

  * 標準エンドポイント用の `stepfun`
  * Step Plan エンドポイント用の `stepfun-plan`


## リージョンとエンドポイントの概要

エンドポイント | 中国（`.com`） | グローバル（`.ai`）  
---|---|---  
標準 | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
認証環境変数: `STEPFUN_API_KEY`

## 組み込みカタログ

標準（`stepfun`）:

モデル参照 | コンテキスト | 最大出力 | 備考  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | デフォルトの標準モデル  
  
Step Plan（`stepfun-plan`）:

モデル参照 | コンテキスト | 最大出力 | 備考  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | デフォルトの Step Plan モデル  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | 追加の Step Plan モデル  
  
## はじめに

プロバイダーサーフェスを選択し、セットアップ手順に従います。

### 標準

**最適な用途:** 標準 StepFun エンドポイントを介した汎用利用。

* ### エンドポイントリージョンを選択する

認証選択 | エンドポイント | リージョン  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | 国際  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | 中国  
* ### オンボーディングを実行する

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

または中国エンドポイントの場合:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-cn
[/code]

* ### 非対話型の代替手段

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### モデルが利用可能であることを確認する

bashCopy code
[code]
    openclaw models list --provider stepfun
[/code]

### モデル参照

  * デフォルトモデル: `stepfun/step-3.5-flash`


### Step Plan

**最適な用途:** Step Plan 推論エンドポイント。

* ### エンドポイントリージョンを選択する

認証選択 | エンドポイント | リージョン  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | 国際  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | 中国  
* ### オンボーディングを実行する

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

または中国エンドポイントの場合:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-cn
[/code]

* ### 非対話型の代替手段

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### モデルが利用可能であることを確認する

bashCopy code
[code]
    openclaw models list --provider stepfun-plan
[/code]

### モデル参照

  * デフォルトモデル: `stepfun-plan/step-3.5-flash`
  * 代替モデル: `stepfun-plan/step-3.5-flash-2603`


## 高度な設定

完全な設定: 標準プロバイダー json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

完全な設定: Step Plan プロバイダー json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

備考

  * プロバイダーは OpenClaw にバンドルされているため、別途 Plugin をインストールする手順はありません。
  * `step-3.5-flash-2603` は現在 `stepfun-plan` でのみ公開されています。
  * 単一の認証フローが `stepfun` と `stepfun-plan` の両方にリージョン一致のプロファイルを書き込むため、両方のサーフェスをまとめて検出できます。
  * モデルを確認または切り替えるには、`openclaw models list` と `openclaw models set <provider/model>` を使います。


## 関連

[**モデル選択** すべてのプロバイダー、モデル参照、フェイルオーバー動作の概要。 ](</ja-JP/concepts/model-providers>) [**設定リファレンス** プロバイダー、モデル、plugins の完全な設定スキーマ。 ](</ja-JP/gateway/configuration-reference>) [**モデル選択** モデルを選択して設定する方法。 ](</ja-JP/concepts/models>) [**StepFun プラットフォーム** StepFun API キー管理とドキュメント。 ](<https://platform.stepfun.com>)

Was this useful?YesNo