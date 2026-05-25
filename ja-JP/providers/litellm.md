---
title: LiteLLM
source_url: https://docs.openclaw.ai/ja-JP/providers/litellm
scraped_at: 2026-05-25
---

[LiteLLM](<https://litellm.ai>) は、100 以上のモデルプロバイダーに統一 API を提供するオープンソースの LLM Gateway です。OpenClaw を LiteLLM 経由でルーティングすると、コスト追跡、ロギング、OpenClaw 設定を変更せずにバックエンドを切り替えられる柔軟性を一元化できます。

## クイックスタート

### オンボーディング (推奨)

**最適な用途:** 動作する LiteLLM セットアップへの最短経路。

* ### オンボーディングを実行する

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

リモートプロキシに対する非対話型セットアップでは、プロキシ URL を明示的に渡します。

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### 手動セットアップ

**最適な用途:** インストールと設定を完全に制御する場合。

* ### LiteLLM Proxy を起動する

bashCopy code
[code]
    pip install 'litellm[proxy]'litellm --model claude-opus-4-6
[/code]

* ### OpenClaw を LiteLLM に向ける

bashCopy code
[code]
    export LITELLM_API_KEY="your-litellm-key" openclaw
[/code]

これで完了です。OpenClaw は LiteLLM 経由でルーティングされるようになります。

## 設定

### 環境変数

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### 設定ファイル

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## 高度な設定

### 画像生成

LiteLLM は、OpenAI 互換の `/images/generations` および `/images/edits` ルートを通じて、OpenClaw の `image_generate` ツールのバックエンドにもなれます。LiteLLM 画像 モデルを `agents.defaults.imageGenerationModel` の下に設定します。

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

`http://localhost:4000` のようなループバック LiteLLM URL は、グローバルな プライベートネットワーク上書きなしで動作します。LAN でホストされるプロキシの場合は、 API キーが設定済みのプロキシホストへ送信されるため、 `models.providers.litellm.request.allowPrivateNetwork: true` を設定します。

仮想キー

OpenClaw 用に支出上限付きの専用キーを作成します。

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

生成されたキーを `LITELLM_API_KEY` として使用します。

モデルルーティング

LiteLLM はモデルリクエストを異なるバックエンドにルーティングできます。LiteLLM の `config.yaml` で設定します。

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

OpenClaw は `claude-opus-4-6` をリクエストし続け、LiteLLM がルーティングを処理します。

使用状況の表示

LiteLLM のダッシュボードまたは API を確認します。

bashCopy code
[code]
    # Key infocurl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # Spend logscurl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

プロキシ動作の注記

  * LiteLLM はデフォルトで `http://localhost:4000` で動作します
  * OpenClaw は LiteLLM のプロキシ形式の OpenAI 互換 `/v1` エンドポイント経由で接続します
  * ネイティブ OpenAI 専用のリクエスト整形は LiteLLM 経由では適用されません: `service_tier` なし、Responses `store` なし、プロンプトキャッシュヒントなし、 OpenAI reasoning 互換ペイロード整形なし
  * 非表示の OpenClaw 帰属ヘッダー (`originator`、`version`、`User-Agent`) はカスタム LiteLLM ベース URL には注入されません


## 関連

[**LiteLLM ドキュメント** 公式 LiteLLM ドキュメントと API リファレンス。 ](<https://docs.litellm.ai>) [**モデル選択** すべてのプロバイダー、モデル参照、フェイルオーバー動作の概要。 ](</ja-JP/concepts/model-providers>) [**設定** 完全な設定リファレンス。 ](</ja-JP/gateway/configuration>) [**モデル選択** モデルの選択と設定方法。 ](</ja-JP/concepts/models>)

Was this useful?YesNo