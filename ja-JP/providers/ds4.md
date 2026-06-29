---
title: ds4
source_url: https://docs.openclaw.ai/ja-JP/providers/ds4
scraped_at: 2026-06-29
---

ModelsProviders

[ds4](<https://github.com/antirez/ds4>) は、ローカルの Metal バックエンドから、OpenAI 互換の `/v1` API で DeepSeek V4 Flash を提供します。OpenClaw は汎用の `openai-completions` プロバイダーファミリーを通じて ds4 に接続します。

ds4 は OpenClaw に同梱されるプロバイダー Plugin ではありません。 `models.providers.ds4` の下で構成し、`ds4/deepseek-v4-flash` を選択します。

  * プロバイダー ID: `ds4`
  * Plugin: なし
  * API: OpenAI 互換 Chat Completions (`openai-completions`)
  * 推奨ベース URL: `http://127.0.0.1:18000/v1`
  * モデル ID: `deepseek-v4-flash`
  * ツール呼び出し: OpenAI 形式の `tools` と `tool_calls` により対応
  * 推論: DeepSeek 形式の `thinking` と `reasoning_effort`


## 要件

  * Metal 対応の macOS。
  * `ds4-server` と DeepSeek V4 Flash GGUF ファイルを含む、動作する ds4 チェックアウト。
  * 選択するコンテキストに十分なメモリ。大きな `--ctx` 値では、サーバー起動時により多くの KV メモリが割り当てられます。


## クイックスタート

* ### Start ds4-server

`&lt;DS4_DIR&gt;` を ds4 のチェックアウトパスに置き換えます。

bashCopy code
[code]
    &lt;DS4_DIR&gt;/ds4-server \  --model &lt;DS4_DIR&gt;/ds4flash.gguf \  --host 127.0.0.1 \  --port 18000 \  --ctx 32768 \  --tokens 128
[/code]

* ### Verify the OpenAI-compatible endpoint

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

レスポンスに `deepseek-v4-flash` が含まれている必要があります。

* ### Add the OpenClaw provider config

完全な設定 の設定を追加し、ワンショットのモデルチェックを実行します。

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

## 完全な設定

ds4 がすでに `127.0.0.1:18000` で実行されている場合は、この設定を使用します。

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "ds4/deepseek-v4-flash" },      models: {        "ds4/deepseek-v4-flash": {          alias: "DS4 local",        },      },    },  },  models: {    mode: "merge",    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

`contextWindow` は `ds4-server --ctx` の値と合わせてください。OpenClaw にサーバーのデフォルトより少ない出力を意図的に要求させたい場合を除き、`maxTokens` は `--tokens` と合わせてください。

## オンデマンド起動

OpenClaw は、`ds4/...` モデルが選択された場合にのみ ds4 を起動できます。同じプロバイダーエントリに `localService` を追加します。

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "&lt;DS4_DIR&gt;/ds4-server",          args: [            "--model",            "&lt;DS4_DIR&gt;/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "32768",            "--tokens",            "128",          ],          cwd: "&lt;DS4_DIR&gt;",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

`command` は絶対実行ファイルパスである必要があります。シェル検索と `~` 展開は使用されません。すべての `localService` フィールドについては、[ローカルモデルサービス](</ja-JP/gateway/local-model-services>) を参照してください。

## Think Max

ds4 は、次の両方の条件が真の場合にのみ Think Max を適用します。

  * `ds4-server` が `--ctx 393216` 以上で起動している。
  * リクエストが `reasoning_effort: "max"` または同等の ds4 effort フィールドを使用している。


その大きなコンテキストを実行する場合は、サーバーフラグと OpenClaw モデルメタデータの両方を更新します。

json5Copy code
[code]
    {  contextWindow: 393216,  maxTokens: 384000,  compat: {    supportsUsageInStreaming: true,    supportsReasoningEffort: true,    maxTokensField: "max_tokens",    supportsStrictMode: false,    thinkingFormat: "deepseek",    supportedReasoningEfforts: ["low", "medium", "high", "xhigh", "max"],  },}
[/code]

## テスト

直接の HTTP チェックから始めます。

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"Reply with exactly: ds4-ok"}],"max_tokens":16,"stream":false,"thinking":{"type":"disabled"}}'
[/code]

次に OpenClaw のモデルルーティングをテストします。

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

完全なエージェントとツール呼び出しのスモークテストには、少なくとも 32768 のコンテキストを使用します。

bashCopy code
[code]
    openclaw agent \  --local \  --session-id ds4-tool-smoke \  --model ds4/deepseek-v4-flash \  --thinking off \  --message "Use the shell command pwd once, then reply exactly: tool-ok <output>" \  --json \  --timeout 240
[/code]

期待される結果:

  * `executionTrace.winnerProvider` は `ds4`
  * `executionTrace.winnerModel` は `deepseek-v4-flash`
  * `toolSummary.calls` は少なくとも `1`
  * `finalAssistantVisibleText` は `tool-ok` で始まる


## トラブルシューティング

curl /v1/models cannot connect

ds4 が実行されていないか、`baseUrl` のホストとポートにバインドされていません。`ds4-server` を起動してから再試行します。

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

500 prompt exceeds context

構成された `--ctx` が OpenClaw のターンには小さすぎます。`ds4-server --ctx` を増やし、`models.providers.ds4.models[].contextWindow` を一致するように更新してください。ツールを含む完全なエージェントターンには、直接の 1 メッセージ curl リクエストよりも大幅に多くのコンテキストが必要です。

Think Max does not activate

ds4 が Think Max を使用するのは、`--ctx` が少なくとも `393216` で、リクエストが `reasoning_effort: "max"` を要求している場合のみです。より小さいコンテキストでは high reasoning にフォールバックします。

The first request is slow

ds4 には Metal 常駐のコールドスタートとモデルウォームアップの段階があります。OpenClaw がオンデマンドでサーバーを起動する場合は、`localService.readyTimeoutMs: 300000` を使用してください。

## 関連

[**Local model services** モデルリクエストの前に、ローカルモデルサーバーをオンデマンドで起動します。 ](</ja-JP/gateway/local-model-services>) [**Local models** ローカルモデルバックエンドを選択して運用します。 ](</ja-JP/gateway/local-models>) [**Model providers** プロバイダー参照、認証、フェイルオーバーを構成します。 ](</ja-JP/concepts/model-providers>) [**DeepSeek** ネイティブ DeepSeek プロバイダーの動作と思考制御。 ](</ja-JP/providers/deepseek>)

Was this useful?YesNo

Open issue