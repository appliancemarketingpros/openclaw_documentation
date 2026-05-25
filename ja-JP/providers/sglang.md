---
title: SGLang
source_url: https://docs.openclaw.ai/ja-JP/providers/sglang
scraped_at: 2026-05-25
---

SGLang は、OpenAI 互換の HTTP API 経由でオープンウェイトモデルを提供します。OpenClaw は、利用可能なモデルの自動検出付きで `openai-completions` プロバイダーファミリーを使用して SGLang に接続します。

プロパティ | 値  
---|---  
プロバイダー ID | `sglang`  
Plugin | バンドル済み、`enabledByDefault: true`  
認証環境変数 | `SGLANG_API_KEY` (サーバーに認証がない場合は任意の空でない値)  
オンボーディングフラグ | `--auth-choice sglang`  
API | OpenAI 互換 (`openai-completions`)  
デフォルトのベース URL | `http://127.0.0.1:30000/v1`  
デフォルトモデルのプレースホルダー | `sglang/Qwen/Qwen3-8B`  
ストリーミング使用量 | はい (`supportsStreamingUsage: true`)  
価格 | 外部無料としてマーク (`modelPricing.external: false`)  
  
OpenClaw は、`SGLANG_API_KEY` でオプトインした場合、SGLang から利用可能なモデルも**自動検出** します。カスタム SGLang ベース URL も設定する場合は、`agents.defaults.models` で `sglang/*` を使用して検出を動的なままにします。下のモデル検出 (暗黙のプロバイダー)を参照してください。

## はじめに

* ### SGLang を起動する

OpenAI 互換サーバーで SGLang を起動します。ベース URL は `/v1` エンドポイント (例: `/v1/models`, `/v1/chat/completions`) を公開している必要があります。SGLang は 通常、次で実行されます。

  * `http://127.0.0.1:30000/v1`


* ### API キーを設定する

サーバーに認証が設定されていない場合は、任意の値で動作します。

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

* ### オンボーディングを実行するか、モデルを直接設定する

bashCopy code
[code]
    openclaw onboard
[/code]

または、モデルを手動で設定します。

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "sglang/your-model-id" },    },  },}
[/code]

## モデル検出 (暗黙のプロバイダー)

`SGLANG_API_KEY` が設定されている (または認証プロファイルが存在する) かつ `models.providers.sglang` を定義して**いない** 場合、OpenClaw は次をクエリします。

  * `GET http://127.0.0.1:30000/v1/models`


そして、返された ID をモデルエントリに変換します。

## 明示的な設定 (手動モデル)

次の場合は明示的な設定を使用します。

  * SGLang が別のホスト/ポートで実行されている。
  * `contextWindow`/`maxTokens` 値を固定したい。
  * サーバーが実際の API キーを必要とする (またはヘッダーを制御したい)。

json5Copy code
[code]
    {  models: {    providers: {      sglang: {        baseUrl: "http://127.0.0.1:30000/v1",        apiKey: "${SGLANG_API_KEY}",        api: "openai-completions",        models: [          {            id: "your-model-id",            name: "Local SGLang Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## 高度な設定

プロキシスタイルの動作

SGLang はネイティブな OpenAI エンドポイントではなく、プロキシスタイルの OpenAI 互換 `/v1` バックエンドとして扱われます。

動作 | SGLang  
---|---  
OpenAI 専用のリクエスト整形 | 適用されません  
`service_tier`、Responses `store`、プロンプトキャッシュヒント | 送信されません  
推論互換ペイロード整形 | 適用されません  
隠し帰属ヘッダー (`originator`, `version`, `User-Agent`) | カスタム SGLang ベース URL には注入されません  
トラブルシューティング

**サーバーに到達できない**

サーバーが実行中で応答していることを確認します。

bashCopy code
[code]
    curl http://127.0.0.1:30000/v1/models
[/code]

**認証エラー**

リクエストが認証エラーで失敗する場合は、サーバー設定と一致する実際の `SGLANG_API_KEY` を設定するか、 `models.providers.sglang` の下でプロバイダーを明示的に設定します。

## 関連

[**モデル選択** プロバイダー、モデル参照、フェイルオーバー動作を選択します。 ](</ja-JP/concepts/model-providers>) [**設定リファレンス** プロバイダーエントリを含む完全な設定スキーマ。 ](</ja-JP/gateway/configuration-reference>)

Was this useful?YesNo