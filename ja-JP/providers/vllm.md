---
title: vLLM
source_url: https://docs.openclaw.ai/ja-JP/providers/vllm
scraped_at: 2026-05-25
---

vLLM は、**OpenAI 互換** HTTP API 経由でオープンソースモデル（および一部のカスタムモデル）を提供できます。OpenClaw は `openai-completions` API を使って vLLM に接続します。

OpenClaw は、`VLLM_API_KEY` でオプトインすると、vLLM から利用可能なモデルを**自動検出** することもできます（サーバーが認証を強制しない場合は任意の値で動作します）。カスタム vLLM ベース URL も設定する場合は、`agents.defaults.models` で `vllm/*` を使うと検出を動的に保てます。

OpenClaw は `vllm` を、ストリーミングされた使用量計算をサポートするローカルの OpenAI 互換プロバイダーとして扱うため、ステータス/コンテキストのトークン数は `stream_options.include_usage` レスポンスから更新できます。

プロパティ | 値  
---|---  
プロバイダー ID | `vllm`  
API | `openai-completions`（OpenAI 互換）  
認証 | `VLLM_API_KEY` 環境変数  
デフォルトベース URL | `http://127.0.0.1:8000/v1`  
  
## はじめに

* ### OpenAI 互換サーバーで vLLM を起動する

ベース URL は `/v1` エンドポイント（例: `/v1/models`、`/v1/chat/completions`）を公開している必要があります。vLLM は一般的に次で動作します。

CodeCopy code
[code]
    http://127.0.0.1:8000/v1
[/code]

* ### API キー環境変数を設定する

サーバーが認証を強制しない場合は任意の値で動作します。

bashCopy code
[code]
    export VLLM_API_KEY="vllm-local"
[/code]

* ### モデルを選択する

自分の vLLM モデル ID のいずれかに置き換えます。

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vllm/your-model-id" },    },  },}
[/code]

* ### モデルが利用可能であることを確認する

bashCopy code
[code]
    openclaw models list --provider vllm
[/code]

## モデル検出（暗黙的プロバイダー）

`VLLM_API_KEY` が設定されている（または認証プロファイルが存在する）状態で、`models.providers.vllm` を定義して**いない** 場合、OpenClaw は次を問い合わせます。

CodeCopy code
[code]
    GET http://127.0.0.1:8000/v1/models
[/code]

そして返された ID をモデルエントリに変換します。

## 明示的な設定（手動モデル）

次の場合は明示的な設定を使います。

  * vLLM が別のホストまたはポートで動作している
  * `contextWindow` または `maxTokens` の値を固定したい
  * サーバーが実際の API キーを必要とする（またはヘッダーを制御したい）
  * 信頼済みのループバック、LAN、または Tailscale vLLM エンドポイントに接続する

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://127.0.0.1:8000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300, // Optional: extend connect/header/body/request timeout for slow local models        models: [          {            id: "your-model-id",            name: "Local vLLM Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

すべてのモデルを手動で列挙せずにこのプロバイダーを動的に保つには、可視モデルカタログにプロバイダーのワイルドカードを追加します。

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/*": {},      },    },  },}
[/code]

## 高度な設定

プロキシ形式の動作

vLLM は、ネイティブの OpenAI エンドポイントではなく、プロキシ形式の OpenAI 互換 `/v1` バックエンドとして扱われます。つまり次のようになります。

動作 | 適用されるか  
---|---  
ネイティブ OpenAI リクエスト整形 | いいえ  
`service_tier` | 送信されません  
Responses `store` | 送信されません  
プロンプトキャッシュヒント | 送信されません  
OpenAI 推論互換ペイロード整形 | 適用されません  
非表示の OpenClaw 帰属ヘッダー | カスタムベース URL には注入されません  
Qwen の thinking 制御

vLLM 経由で提供される Qwen モデルでは、サーバーが Qwen chat-template kwargs を想定している場合、モデルエントリに `params.qwenThinkingFormat: "chat-template"` を設定します。OpenClaw は `/think off` を次にマップします。

jsonCopy code
[code]
    {  "chat_template_kwargs": {    "enable_thinking": false,    "preserve_thinking": true  }}
[/code]

`off` 以外の thinking レベルでは `enable_thinking: true` が送信されます。エンドポイントが代わりに DashScope 形式のトップレベルフラグを想定している場合は、`params.qwenThinkingFormat: "top-level"` を使ってリクエストルートに `enable_thinking` を送信します。スネークケースの `params.qwen_thinking_format` も受け付けられます。

Nemotron 3 の thinking 制御

vLLM/Nemotron 3 は chat-template kwargs を使って、推論を非表示の推論として返すか、表示される回答テキストとして返すかを制御できます。OpenClaw セッションが thinking off で `vllm/nemotron-3-*` を使う場合、同梱の vLLM Plugin は次を送信します。

jsonCopy code
[code]
    {  "chat_template_kwargs": {    "enable_thinking": false,    "force_nonempty_content": true  }}
[/code]

これらの値をカスタマイズするには、モデル params の下に `chat_template_kwargs` を設定します。`params.extra_body.chat_template_kwargs` も設定している場合は、`extra_body` が最後のリクエストボディ上書きであるため、その値が最終的に優先されます。

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/nemotron-3-super": {          params: {            chat_template_kwargs: {              enable_thinking: false,              force_nonempty_content: true,            },          },        },      },    },  },}
[/code]

Qwen ツール呼び出しがテキストとして表示される

まず、vLLM がそのモデルに適したツール呼び出しパーサーとチャットテンプレートで起動されていることを確認します。たとえば、vLLM は Qwen2.5 モデル向けに `hermes`、Qwen3-Coder モデル向けに `qwen3_xml` を文書化しています。

症状:

  * skills またはツールが一切実行されない
  * アシスタントが `{"name":"read","arguments":...}` のような生の JSON/XML を表示する
  * OpenClaw が `tool_choice: "auto"` を送信したとき、vLLM が空の `tool_calls` 配列を返す


一部の Qwen/vLLM の組み合わせでは、リクエストで `tool_choice: "required"` を使った場合にのみ構造化されたツール呼び出しを返します。そのようなモデルエントリでは、`params.extra_body` で OpenAI 互換リクエストフィールドを強制します。

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/Qwen-Qwen2.5-Coder-32B-Instruct": {          params: {            extra_body: {              tool_choice: "required",            },          },        },      },    },  },}
[/code]

`Qwen-Qwen2.5-Coder-32B-Instruct` は、次で返される正確な ID に置き換えてください。

bashCopy code
[code]
    openclaw models list --provider vllm
[/code]

CLI から同じ上書きを適用できます。

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"vllm/Qwen-Qwen2.5-Coder-32B-Instruct":{"params":{"extra_body":{"tool_choice":"required"}}}}' --strict-json --merge
[/code]

これはオプトインの互換性回避策です。ツールを含むすべてのモデルターンでツール呼び出しが必須になるため、その動作が許容できる専用のローカルモデルエントリでのみ使用してください。すべての vLLM モデルのグローバルデフォルトとして使用しないでください。また、任意のアシスタントテキストを実行可能なツール呼び出しに無差別に変換するプロキシは使用しないでください。

カスタムベース URL

vLLM サーバーがデフォルト以外のホストまたはポートで動作している場合は、明示的なプロバイダー設定で `baseUrl` を設定します。

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://192.168.1.50:9000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300,        models: [          {            id: "my-custom-model",            name: "Remote vLLM Model",            reasoning: false,            input: ["text"],            contextWindow: 64000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## トラブルシューティング

最初のレスポンスが遅い、またはリモートサーバーがタイムアウトする

大きなローカルモデル、リモート LAN ホスト、または tailnet リンクでは、プロバイダースコープのリクエストタイムアウトを設定します。

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://192.168.1.50:8000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300,        models: [{ id: "your-model-id", name: "Local vLLM Model" }],      },    },  },}
[/code]

`timeoutSeconds` は、接続セットアップ、レスポンスヘッダー、ボディストリーミング、保護された fetch 全体の中止を含む、vLLM モデル HTTP リクエストのみに適用されます。エージェント実行全体を制御する `agents.defaults.timeoutSeconds` を増やす前に、こちらを優先してください。

サーバーに到達できない

vLLM サーバーが実行中でアクセス可能であることを確認します。

bashCopy code
[code]
    curl http://127.0.0.1:8000/v1/models
[/code]

接続エラーが表示される場合は、ホスト、ポート、および vLLM が OpenAI 互換サーバーモードで起動されていることを確認します。 明示的なループバック、LAN、または Tailscale エンドポイントでは、`models.providers.vllm.request.allowPrivateNetwork: true` も設定してください。プロバイダーが明示的に信頼されていない限り、プロバイダーリクエストはデフォルトでプライベートネットワーク URL をブロックします。

リクエストで認証エラーが発生する

リクエストが認証エラーで失敗する場合は、サーバー設定に一致する実際の `VLLM_API_KEY` を設定するか、`models.providers.vllm` の下でプロバイダーを明示的に設定します。

モデルが検出されない

自動検出には `VLLM_API_KEY` の設定が必要です。`models.providers.vllm` を定義している場合、`agents.defaults.models` に `"vllm/*": {}` が含まれていない限り、OpenClaw は宣言済みモデルのみを使用します。

ツールが生テキストとしてレンダリングされる

Qwen モデルが skill の実行ではなく JSON/XML ツール構文を表示する場合は、上記の高度な設定にある Qwen ガイダンスを確認してください。通常の修正は次のとおりです。

  * そのモデルに適したパーサー/テンプレートで vLLM を起動する
  * `openclaw models list --provider vllm` で正確なモデル ID を確認する
  * `tool_choice: "auto"` で引き続き空またはテキストのみのツール呼び出しが返される場合に限り、専用のモデルごとの `params.extra_body.tool_choice: "required"` 上書きを追加する


## 関連

[**モデル選択** プロバイダー、モデル参照、フェイルオーバー動作の選択。 ](</ja-JP/concepts/model-providers>) [**OpenAI** ネイティブ OpenAI プロバイダーと OpenAI 互換ルートの動作。 ](</ja-JP/providers/openai>) [**OAuth と認証** 認証の詳細と認証情報の再利用ルール。 ](</ja-JP/gateway/authentication>) [**トラブルシューティング** よくある問題とその解決方法。 ](</ja-JP/help/troubleshooting>)

Was this useful?YesNo