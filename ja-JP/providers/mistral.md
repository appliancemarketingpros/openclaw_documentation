---
title: Mistral
source_url: https://docs.openclaw.ai/ja-JP/providers/mistral
scraped_at: 2026-05-25
---

OpenClaw には、chat completions、メディア理解（Voxtral バッチ文字起こし）、Voice Call 向け realtime STT（Voxtral Realtime）、memory embeddings（`mistral-embed`）の 4 つの契約を登録する同梱 Mistral Plugin が含まれています。

プロパティ | 値  
---|---  
Provider id | `mistral`  
Plugin | 同梱、`enabledByDefault: true`  
認証 env var | `MISTRAL_API_KEY`  
Onboarding flag | `--auth-choice mistral-api-key`  
直接 CLI flag | `--mistral-api-key <key>`  
API | OpenAI 互換（`openai-completions`）  
Base URL | `https://api.mistral.ai/v1`  
既定モデル | `mistral/mistral-large-latest`  
埋め込みモデル | `mistral-embed`  
Voxtral batch | `voxtral-mini-latest`（音声文字起こし）  
Voxtral realtime | `voxtral-mini-transcribe-realtime-2602`  
  
## はじめに

* ### API キーを取得する

[Mistral Console](<https://console.mistral.ai/>) で API キーを作成します。

* ### オンボーディングを実行する

bashCopy code
[code]
    openclaw onboard --auth-choice mistral-api-key
[/code]

または、キーを直接渡します。

bashCopy code
[code]
    openclaw onboard --mistral-api-key "$MISTRAL_API_KEY"
[/code]

* ### 既定モデルを設定する

json5Copy code
[code]
    {  env: { MISTRAL_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "mistral/mistral-large-latest" } } },}
[/code]

* ### モデルが利用可能であることを確認する

bashCopy code
[code]
    openclaw models list --provider mistral
[/code]

## 組み込み LLM カタログ

[Mistral Medium 3.5](<https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04>) は、同梱カタログ内の現在の blended Medium モデルです。128B の dense weights、 テキストと画像の入力、256K コンテキスト、関数呼び出し、構造化出力、コーディング、 Chat Completions API を通じた調整可能な推論に対応しています。既定の `mistral/mistral-large-latest` ではなく、Mistral の新しい統合 agentic/coding モデルを使いたい場合は `mistral/mistral-medium-3-5` を使用します。

OpenClaw は現在、この同梱 Mistral カタログを出荷しています。

モデル ref | 入力 | コンテキスト | 最大出力 | 注記  
---|---|---|---|---  
`mistral/mistral-large-latest` | text, image | 262,144 | 16,384 | 既定モデル  
`mistral/mistral-medium-2508` | text, image | 262,144 | 8,192 | Mistral Medium 3.1  
`mistral/mistral-medium-3-5` | text, image | 262,144 | 8,192 | Mistral Medium 3.5、調整可能な推論  
`mistral/mistral-small-latest` | text, image | 128,000 | 16,384 | Mistral Small 4、API `reasoning_effort` 経由の調整可能な推論  
`mistral/pixtral-large-latest` | text, image | 128,000 | 32,768 | Pixtral  
`mistral/codestral-latest` | text | 256,000 | 4,096 | コーディング  
`mistral/devstral-medium-latest` | text | 262,144 | 32,768 | Devstral 2  
`mistral/magistral-small` | text | 128,000 | 40,000 | 推論対応  
  
オンボーディング後、Gateway を起動せずに Medium 3.5 をスモークテストします。

bashCopy code
[code]
    openclaw infer model run --local \  --model mistral/mistral-medium-3-5 \  --prompt "Reply with exactly: mistral-ok" \  --json
[/code]

設定を変更する前に、同梱カタログの行を確認するには次を実行します。

bashCopy code
[code]
    openclaw models list --all --provider mistral --plain
[/code]

## 音声文字起こし（Voxtral）

メディア理解パイプラインを通じたバッチ音声文字起こしには Voxtral を使用します。

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "mistral", model: "voxtral-mini-latest" }],      },    },  },}
[/code]

## Voice Call ストリーミング STT

同梱の `mistral` Plugin は、Voxtral Realtime を Voice Call ストリーミング STT provider として登録します。

設定 | 設定パス | 既定値  
---|---|---  
API キー | `plugins.entries.voice-call.config.streaming.providers.mistral.apiKey` | `MISTRAL_API_KEY` にフォールバック  
モデル | `...mistral.model` | `voxtral-mini-transcribe-realtime-2602`  
エンコーディング | `...mistral.encoding` | `pcm_mulaw`  
サンプルレート | `...mistral.sampleRate` | `8000`  
目標遅延 | `...mistral.targetStreamingDelayMs` | `800`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "mistral",            providers: {              mistral: {                apiKey: "${MISTRAL_API_KEY}",                targetStreamingDelayMs: 800,              },            },          },        },      },    },  },}
[/code]

## 高度な設定

調整可能な推論

`mistral/mistral-small-latest`（Mistral Small 4）と `mistral/mistral-medium-3-5` は、Chat Completions API で `reasoning_effort` 経由の [調整可能な推論](<https://docs.mistral.ai/studio-api/conversations/reasoning/adjustable>) に対応しています（`none` は出力内の追加の思考を最小化します。`high` は最終回答の前に完全な思考トレースを表示します）。Mistral は、Medium 3.5 の agentic およびコードのユースケースに `reasoning_effort="high"` を推奨しています。

OpenClaw はセッションの **thinking** レベルを Mistral の API にマップします。

OpenClaw thinking レベル | Mistral `reasoning_effort`  
---|---  
**off** / **minimal** | `none`  
**low** / **medium** / **high** / **xhigh** / **adaptive** / **max** | `high`  
  
Medium 3.5 reasoning のモデルスコープ設定例:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "mistral/mistral-medium-3-5" },      models: {        "mistral/mistral-medium-3-5": {          params: { thinking: "high" },        },      },    },  },}
[/code]

メモリ埋め込み

Mistral は `/v1/embeddings` 経由で memory embeddings を提供できます（既定モデル: `mistral-embed`）。

json5Copy code
[code]
    {  memorySearch: { provider: "mistral" },}
[/code]

認証と base URL

  * Mistral 認証は `MISTRAL_API_KEY`（Bearer header）を使用します。
  * Provider base URL の既定は `https://api.mistral.ai/v1` で、標準の OpenAI 互換 chat-completions request shape を受け付けます。
  * オンボーディングの既定モデルは `mistral/mistral-large-latest` です。
  * Mistral が必要な regional endpoint を明示的に公開している場合にのみ、`models.providers.mistral.baseUrl` で base URL を上書きしてください。


## 関連

[**モデル選択** providers、model refs、failover behavior の選択。 ](</ja-JP/concepts/model-providers>) [**メディア理解** 音声文字起こしの設定と provider 選択。 ](</ja-JP/nodes/media-understanding>)

Was this useful?YesNo