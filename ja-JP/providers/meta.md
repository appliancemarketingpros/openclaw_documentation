---
title: メタ
source_url: https://docs.openclaw.ai/ja-JP/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

**Meta API** は、`muse-spark-1.1` 推論モデル向けに OpenAI 互換の **Responses API** （`POST /v1/responses`）を使用します。このプロバイダーは、OpenClaw にバンドルされた Plugin として提供されます。

プロパティ | 値  
---|---  
プロバイダー ID | `meta`  
Plugin | バンドル済みプロバイダー  
認証環境変数 | `MODEL_API_KEY`  
オンボーディングフラグ | `--auth-choice meta-api-key`  
直接指定する CLI フラグ | `--meta-api-key <key>`  
API | Responses API (`openai-responses`)  
ベース URL | `https://api.meta.ai/v1`  
デフォルトモデル | `meta/muse-spark-1.1`  
デフォルト推論レベル | `high` (`reasoning.effort`)  
  
## はじめに

* ### API キーを設定する

OnboardingCopy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

Env onlyCopy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### モデルが利用可能であることを確認する

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

静的な `muse-spark-1.1` カタログエントリを一覧表示します。`MODEL_API_KEY` を解決できない場合、`openclaw models status --json` は不足している認証情報を `auth.unusableProfiles` の下に報告します。

## 非対話型セットアップ

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## 組み込みカタログ

モデル参照 | 名前 | 推論 | コンテキストウィンドウ | 最大出力  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | あり | 1,048,576 | 131,072  
  
機能:

  * テキストと画像の入力
  * ツール呼び出しとストリーミング
  * 推論レベル: `minimal`、`low`、`medium`、`high`、`xhigh`（デフォルト: `high`）
  * ステートレスな暗号化済み推論の再利用（`store: false`、`include: ["reasoning.encrypted_content"]`）


## 手動設定

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## スモークテスト

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

ライブテストでは、`POST /v1/responses` に対して `muse-spark-1.1` を使用します。

## 関連項目

[**モデルプロバイダー** プロバイダー、モデル参照、フェイルオーバー動作の選択。 ](</ja-JP/concepts/model-providers>) [**思考モード** muse-spark-1.1 の推論レベル。 ](</ja-JP/tools/thinking>) [**設定リファレンス** エージェントのデフォルトとモデル設定。 ](</ja-JP/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue