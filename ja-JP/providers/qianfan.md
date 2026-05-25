---
title: Qianfan
source_url: https://docs.openclaw.ai/ja-JP/providers/qianfan
scraped_at: 2026-05-25
---

Qianfan は Baidu の MaaS プラットフォームで、単一のエンドポイントと API キーの背後にある多数のモデルへリクエストをルーティングする **統一 API** を提供します。OpenAI 互換のため、ほとんどの OpenAI SDK はベース URL を切り替えるだけで動作します。

プロパティ | 値  
---|---  
プロバイダー | `qianfan`  
認証 | `QIANFAN_API_KEY`  
API | OpenAI 互換  
ベース URL | `https://qianfan.baidubce.com/v2`  
  
## はじめに

* ### Baidu Cloud アカウントを作成する

[Qianfan Console](<https://console.bce.baidu.com/qianfan/ais/console/apiKey>) でサインアップまたはログインし、Qianfan API アクセスが有効になっていることを確認します。

* ### API キーを生成する

新しいアプリケーションを作成するか既存のものを選択し、API キーを生成します。キーの形式は `bce-v3/ALTAK-...` です。

* ### オンボーディングを実行する

bashCopy code
[code]
    openclaw onboard --auth-choice qianfan-api-key
[/code]

* ### モデルが利用可能であることを確認する

bashCopy code
[code]
    openclaw models list --provider qianfan
[/code]

## 組み込みカタログ

モデル参照 | 入力 | コンテキスト | 最大出力 | 推論 | 注記  
---|---|---|---|---|---  
`qianfan/deepseek-v3.2` | テキスト | 98,304 | 32,768 | はい | デフォルトモデル  
`qianfan/ernie-5.0-thinking-preview` | テキスト、画像 | 119,000 | 64,000 | はい | マルチモーダル  
  
## 設定例

json5Copy code
[code]
    {  env: { QIANFAN_API_KEY: "bce-v3/ALTAK-..." },  agents: {    defaults: {      model: { primary: "qianfan/deepseek-v3.2" },      models: {        "qianfan/deepseek-v3.2": { alias: "QIANFAN" },      },    },  },  models: {    providers: {      qianfan: {        baseUrl: "https://qianfan.baidubce.com/v2",        api: "openai-completions",        models: [          {            id: "deepseek-v3.2",            name: "DEEPSEEK V3.2",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 98304,            maxTokens: 32768,          },          {            id: "ernie-5.0-thinking-preview",            name: "ERNIE-5.0-Thinking-Preview",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 119000,            maxTokens: 64000,          },        ],      },    },  },}
[/code]

トランスポートと互換性

Qianfan は、ネイティブの OpenAI リクエスト整形ではなく、OpenAI 互換のトランスポート経路を通じて実行されます。つまり、標準の OpenAI SDK 機能は動作しますが、プロバイダー固有のパラメーターは転送されない場合があります。

カタログと上書き

バンドル済みカタログには現在、`deepseek-v3.2` と `ernie-5.0-thinking-preview` が含まれています。カスタムのベース URL またはモデルメタデータが必要な場合にのみ、`models.providers.qianfan` を追加または上書きしてください。

トラブルシューティング

  * API キーが `bce-v3/ALTAK-` で始まり、Baidu Cloud コンソールで Qianfan API アクセスが有効になっていることを確認します。
  * モデルが一覧表示されない場合は、アカウントで Qianfan サービスが有効化されていることを確認してください。
  * デフォルトのベース URL は `https://qianfan.baidubce.com/v2` です。カスタムエンドポイントまたはプロキシを使用する場合にのみ変更してください。


## 関連

[**モデル選択** プロバイダー、モデル参照、フェイルオーバー動作の選択。 ](</ja-JP/concepts/model-providers>) [**設定リファレンス** OpenClaw 設定の完全なリファレンス。 ](</ja-JP/gateway/configuration-reference>) [**エージェントのセットアップ** エージェントのデフォルトとモデル割り当ての設定。 ](</ja-JP/concepts/agent>) [**Qianfan API ドキュメント** 公式 Qianfan API ドキュメント。 ](<https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb>)

Was this useful?YesNo