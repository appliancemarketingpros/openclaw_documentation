---
title: Groq
source_url: https://docs.openclaw.ai/ja-JP/providers/groq
scraped_at: 2026-05-25
---

[Groq](<https://groq.com>) は、カスタム LPU ハードウェアを使用して、オープンウェイトモデル (Llama、Gemma、Kimi、Qwen、GPT OSS など) で超高速推論を提供します。OpenClaw には、OpenAI 互換のチャットプロバイダーと音声メディア理解プロバイダーの両方を登録する、バンドル済みの Groq Plugin が含まれています。

プロパティ | 値  
---|---  
プロバイダー ID | `groq`  
Plugin | バンドル済み、`enabledByDefault: true`  
認証環境変数 | `GROQ_API_KEY`  
オンボーディングフラグ | `--auth-choice groq-api-key`  
API | OpenAI 互換 (`openai-completions`)  
ベース URL | `https://api.groq.com/openai/v1`  
音声文字起こし | `whisper-large-v3-turbo` (デフォルト)  
推奨チャットデフォルト | `groq/llama-3.3-70b-versatile`  
  
## はじめに

* ### API キーを取得する

[console.groq.com/keys](<https://console.groq.com/keys>) で API キーを作成します。

* ### API キーを設定する

オンボーディングCopy code
[code]
    openclaw onboard --auth-choice groq-api-key
[/code]

環境変数のみCopy code
[code]
    export GROQ_API_KEY=gsk_...
[/code]

* ### デフォルトモデルを設定する

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

* ### カタログに到達できることを確認する

bashCopy code
[code]
    openclaw models list --provider groq
[/code]

### 設定ファイルの例

json5Copy code
[code]
    {  env: { GROQ_API_KEY: "gsk_..." },  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

## 組み込みカタログ

OpenClaw は、推論ありと推論なしの両方の項目を含む、マニフェストに基づく Groq カタログを同梱しています。インストール済みバージョンにバンドルされている行を確認するには `openclaw models list --provider groq` を実行し、Groq の正式な一覧については [console.groq.com/docs/models](<https://console.groq.com/docs/models>) を確認してください。

モデル参照 | 名前 | 推論 | 入力 | コンテキスト  
---|---|---|---|---  
`groq/llama-3.3-70b-versatile` | Llama 3.3 70B Versatile | なし | text | 131,072  
`groq/llama-3.1-8b-instant` | Llama 3.1 8B Instant | なし | text | 131,072  
`groq/meta-llama/llama-4-maverick-17b-128e-instruct` | Llama 4 Maverick 17B | なし | text + image | 131,072  
`groq/meta-llama/llama-4-scout-17b-16e-instruct` | Llama 4 Scout 17B | なし | text + image | 131,072  
`groq/llama3-70b-8192` | Llama 3 70B | なし | text | 8,192  
`groq/llama3-8b-8192` | Llama 3 8B | なし | text | 8,192  
`groq/gemma2-9b-it` | Gemma 2 9B | なし | text | 8,192  
`groq/mistral-saba-24b` | Mistral Saba 24B | なし | text | 32,768  
`groq/moonshotai/kimi-k2-instruct` | Kimi K2 Instruct | なし | text | 131,072  
`groq/moonshotai/kimi-k2-instruct-0905` | Kimi K2 Instruct 0905 | なし | text | 262,144  
`groq/openai/gpt-oss-120b` | GPT OSS 120B | あり | text | 131,072  
`groq/openai/gpt-oss-20b` | GPT OSS 20B | あり | text | 131,072  
`groq/openai/gpt-oss-safeguard-20b` | Safety GPT OSS 20B | あり | text | 131,072  
`groq/qwen-qwq-32b` | Qwen QwQ 32B | あり | text | 131,072  
`groq/qwen/qwen3-32b` | Qwen3 32B | あり | text | 131,072  
`groq/deepseek-r1-distill-llama-70b` | DeepSeek R1 Distill Llama 70B | あり | text | 131,072  
`groq/groq/compound` | Compound | あり | text | 131,072  
`groq/groq/compound-mini` | Compound Mini | あり | text | 131,072  
  
## 推論モデル

OpenClaw は共有の `/think` レベルを Groq のモデル固有の `reasoning_effort` 値にマッピングします。

  * `qwen/qwen3-32b` では、思考を無効にすると `none` を送信し、思考を有効にすると `default` を送信します。
  * Groq GPT OSS 推論モデル (`openai/gpt-oss-*`) では、OpenClaw は `/think` レベルに基づいて `low`、`medium`、または `high` を送信します。これらのモデルは無効値をサポートしないため、思考を無効にすると `reasoning_effort` は省略されます。
  * DeepSeek R1 Distill、Qwen QwQ、Compound は Groq のネイティブな推論サーフェスを使用します。`/think` は可視性を制御しますが、モデルは常に推論します。


共有の `/think` レベルと、OpenClaw がプロバイダーごとにそれらをどのように変換するかについては、[思考モード](</ja-JP/tools/thinking>) を参照してください。

## 音声文字起こし

Groq のバンドル済み Plugin は **音声メディア理解プロバイダー** も登録するため、音声メッセージを共有の `tools.media.audio` サーフェス経由で文字起こしできます。

プロパティ | 値  
---|---  
共有設定パス | `tools.media.audio`  
デフォルトベース URL | `https://api.groq.com/openai/v1`  
デフォルトモデル | `whisper-large-v3-turbo`  
自動優先度 | 20  
API エンドポイント | OpenAI 互換 `/audio/transcriptions`  
  
Groq をデフォルトの音声バックエンドにするには:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [{ provider: "groq" }],      },    },  },}
[/code]

デーモンでの環境の可用性

Gateway が管理サービス (launchd、systemd、Docker) として実行される場合、`GROQ_API_KEY` は対話型シェルだけでなく、そのプロセスから見える必要があります。

カスタム Groq モデル ID

OpenClaw は実行時に任意の Groq モデル ID を受け入れます。Groq が表示する正確な ID を使用し、先頭に `groq/` を付けてください。バンドル済みカタログは一般的なケースをカバーします。カタログにない ID はデフォルトの OpenAI 互換テンプレートにフォールスルーします。

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/<your-model-id>" },    },  },}
[/code]

## 関連

[**モデルプロバイダー** プロバイダー、モデル参照、フェイルオーバー動作の選択。 ](</ja-JP/concepts/model-providers>) [**思考モード** 推論エフォートレベルとプロバイダーポリシーの相互作用。 ](</ja-JP/tools/thinking>) [**設定リファレンス** プロバイダーと音声設定を含む完全な設定スキーマ。 ](</ja-JP/gateway/configuration-reference>) [**Groq Console** Groq ダッシュボード、API ドキュメント、価格。 ](<https://console.groq.com>)

Was this useful?YesNo