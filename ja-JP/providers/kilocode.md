---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/ja-JP/providers/kilocode
scraped_at: 2026-05-25
---

Kilo Gateway は、単一のエンドポイントと API キーの背後で多数のモデルにリクエストをルーティングする **統合 API** を提供します。OpenAI 互換なので、ほとんどの OpenAI SDK はベース URL を切り替えるだけで動作します。

プロパティ | 値  
---|---  
プロバイダー | `kilocode`  
認証 | `KILOCODE_API_KEY`  
API | OpenAI 互換  
ベース URL | `https://api.kilo.ai/api/gateway/`  
  
## はじめに

* ### アカウントを作成する

[app.kilo.ai](<https://app.kilo.ai>) に移動し、サインインするかアカウントを作成してから、API Keys に移動して新しいキーを生成します。

* ### オンボーディングを実行する

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

または、環境変数を直接設定します。

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### モデルが利用可能であることを確認する

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## デフォルトモデル

デフォルトモデルは `kilocode/kilo/auto` です。これは Kilo Gateway によって管理される、プロバイダー所有のスマートルーティングモデルです。

## 組み込みカタログ

OpenClaw は起動時に Kilo Gateway から利用可能なモデルを動的に検出します。アカウントで利用可能なモデルの完全な一覧を表示するには、`/models kilocode` を使用します。

Gateway で利用可能な任意のモデルは、`kilocode/` プレフィックス付きで使用できます。

モデル参照 | 注記  
---|---  
`kilocode/kilo/auto` | デフォルト — スマートルーティング  
`kilocode/anthropic/claude-sonnet-4` | Kilo 経由の Anthropic  
`kilocode/openai/gpt-5.5` | Kilo 経由の OpenAI  
`kilocode/google/gemini-3.1-pro-preview` | Kilo 経由の Google  
...ほか多数 | すべてを一覧するには `/models kilocode` を使用  
  
## 設定例

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

トランスポートと互換性

Kilo Gateway はソース上で OpenRouter 互換として文書化されているため、ネイティブ OpenAI リクエスト整形ではなく、プロキシ形式の OpenAI 互換パスに留まります。

  * Gemini backed の Kilo 参照はプロキシ Gemini パスに留まるため、OpenClaw はネイティブ Gemini のリプレイ検証やブートストラップ書き換えを有効にせず、そこで Gemini の thought-signature サニタイズを維持します。
  * Kilo Gateway は内部的に、API キーを Bearer トークンとして使用します。

ストリームラッパーと推論

Kilo の共有ストリームラッパーは、プロバイダーアプリヘッダーを追加し、サポートされている具体的なモデル参照に対してプロキシ推論ペイロードを正規化します。

トラブルシューティング

  * 起動時にモデル検出に失敗した場合、OpenClaw は `kilocode/kilo/auto` を含むバンドル済み静的カタログにフォールバックします。
  * API キーが有効であり、Kilo アカウントで目的のモデルが有効になっていることを確認してください。
  * Gateway がデーモンとして実行される場合は、`KILOCODE_API_KEY` がそのプロセスで利用可能であることを確認してください（たとえば `~/.openclaw/.env` 内、または `env.shellEnv` 経由）。


## 関連

[**モデル選択** プロバイダー、モデル参照、フェイルオーバー動作の選択。 ](</ja-JP/concepts/model-providers>) [**設定リファレンス** OpenClaw 設定の完全なリファレンス。 ](</ja-JP/gateway/configuration-reference>) [**Kilo Gateway** Kilo Gateway ダッシュボード、API キー、アカウント管理。 ](<https://app.kilo.ai>)

Was this useful?YesNo