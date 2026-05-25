---
title: Hugging Face（inference）
source_url: https://docs.openclaw.ai/ja-JP/providers/huggingface
scraped_at: 2026-05-25
---

[Hugging Face Inference Providers](<https://huggingface.co/docs/inference-providers>) は、単一のルーター API を通じて OpenAI 互換の chat completions を提供します。1 つの token で多数のモデル（DeepSeek、Llama など）にアクセスできます。OpenClaw は **OpenAI 互換エンドポイント** （chat completions のみ）を使います。text-to-image、embeddings、speech には、代わりに [HF inference clients](<https://huggingface.co/docs/api-inference/quicktour>) を直接使ってください。

  * プロバイダ: `huggingface`
  * 認証: `HUGGINGFACE_HUB_TOKEN` または `HF_TOKEN`（**Make calls to Inference Providers** 権限を持つ fine-grained token）
  * API: OpenAI 互換（`https://router.huggingface.co/v1`）
  * 課金: 単一の HF token。[pricing](<https://huggingface.co/docs/inference-providers/pricing>) は free tier 付きで provider 料金に従います。


## はじめに

* ### fine-grained token を作成

[Hugging Face Settings Tokens](<https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained>) にアクセスし、新しい fine-grained token を作成してください。

* ### オンボーディングを実行

プロバイダのドロップダウンで **Hugging Face** を選び、求められたら API キーを入力してください:

bashCopy code
[code]
    openclaw onboard --auth-choice huggingface-api-key
[/code]

* ### デフォルトモデルを選ぶ

**Default Hugging Face model** ドロップダウンで、使いたいモデルを選んでください。有効な token がある場合は Inference API から一覧が読み込まれ、そうでなければ組み込み一覧が表示されます。選択内容はデフォルトモデルとして保存されます。

後から config でデフォルトモデルを設定または変更することもできます:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/deepseek-ai/DeepSeek-R1" },    },  },}
[/code]

* ### モデルが利用可能か確認

bashCopy code
[code]
    openclaw models list --provider huggingface
[/code]

### 非対話セットアップ

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice huggingface-api-key \  --huggingface-api-key "$HF_TOKEN"
[/code]

これにより `huggingface/deepseek-ai/DeepSeek-R1` がデフォルトモデルとして設定されます。

## モデル ID

モデル参照は `huggingface/<org>/<model>` 形式（Hub 形式 ID）です。以下の一覧は **GET** `https://router.huggingface.co/v1/models` に基づくものです。あなたのカタログにはさらに多く含まれている場合があります。

モデル | 参照（`huggingface/` を先頭に付ける）  
---|---  
DeepSeek R1 | `deepseek-ai/DeepSeek-R1`  
DeepSeek V3.2 | `deepseek-ai/DeepSeek-V3.2`  
Qwen3 8B | `Qwen/Qwen3-8B`  
Qwen2.5 7B Instruct | `Qwen/Qwen2.5-7B-Instruct`  
Qwen3 32B | `Qwen/Qwen3-32B`  
Llama 3.3 70B Instruct | `meta-llama/Llama-3.3-70B-Instruct`  
Llama 3.1 8B Instruct | `meta-llama/Llama-3.1-8B-Instruct`  
GPT-OSS 120B | `openai/gpt-oss-120b`  
GLM 4.7 | `zai-org/GLM-4.7`  
Kimi K2.5 | `moonshotai/Kimi-K2.5`  
  
## 高度な設定

モデル検出とオンボーディングのドロップダウン

OpenClaw は **Inference エンドポイントを直接呼び出して** モデルを検出します:

bashCopy code
[code]
    GET https://router.huggingface.co/v1/models
[/code]

（任意: 完全一覧を得るには `Authorization: Bearer $HUGGINGFACE_HUB_TOKEN` または `$HF_TOKEN` を送ってください。一部エンドポイントは認証なしだと部分集合しか返しません。）レスポンスは OpenAI 形式の `{ "object": "list", "data": [ { "id": "Qwen/Qwen3-8B", "owned_by": "Qwen", ... }, ... ] }` です。

Hugging Face API キー（オンボーディング、`HUGGINGFACE_HUB_TOKEN`、または `HF_TOKEN` 経由）を設定すると、OpenClaw はこの GET を使って利用可能な chat-completion モデルを検出します。**対話セットアップ** 中では、token を入力した後に **Default Hugging Face model** ドロップダウンが表示され、この一覧（またはリクエスト失敗時は組み込みカタログ）から埋められます。ランタイム中（たとえば Gateway 起動時）も、キーが存在すれば OpenClaw は再び **GET** `https://router.huggingface.co/v1/models` を呼び出してカタログを更新します。この一覧は、組み込みカタログ（コンテキストウィンドウやコストなどのメタデータ用）とマージされます。リクエストが失敗した場合、またはキーが設定されていない場合は、組み込みカタログのみが使われます。

モデル名、エイリアス、ポリシーサフィックス

  * **API 由来の名前:** モデル表示名は、API が `name`, `title`, `display_name` を返した場合、それを **GET /v1/models** から hydrate します。そうでない場合はモデル ID から導出されます（例: `deepseek-ai/DeepSeek-R1` は「DeepSeek R1」になります）。
  * **表示名を上書き:** config でモデルごとにカスタムラベルを設定すると、CLI や UI 上で好きな表示名にできます:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1 (fast)" },        "huggingface/deepseek-ai/DeepSeek-R1:cheapest": { alias: "DeepSeek R1 (cheap)" },      },    },  },}
[/code]

  * **ポリシーサフィックス:** OpenClaw の同梱 Hugging Face ドキュメントと helper は現在、この 2 つのサフィックスを組み込みポリシーバリアントとして扱います:

    * **`:fastest`** — 最大スループット
    * **`:cheapest`** — 出力トークン単価が最安

これらは `models.providers.huggingface.models` に別エントリとして追加することも、`model.primary` にサフィックス付きで設定することもできます。デフォルトの provider 順序は [Inference Provider settings](<https://hf.co/settings/inference-providers>) でも設定できます（サフィックスなし = その順序を使う）。

  * **Config merge:** `models.providers.huggingface.models` 内の既存エントリ（例: `models.json` 内）は、config マージ時に保持されます。そのため、そこに設定したカスタム `name`, `alias`, またはモデルオプションは保持されます。


環境と daemon セットアップ

Gateway を daemon（launchd / systemd）として動かす場合、`HUGGINGFACE_HUB_TOKEN` または `HF_TOKEN` がそのプロセスから利用可能であることを確認してください（たとえば `~/.openclaw/.env` または `env.shellEnv` 経由）。

Config: Qwen fallback 付き DeepSeek R1 json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-R1",        fallbacks: ["huggingface/Qwen/Qwen3-8B"],      },      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1" },        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },      },    },  },}
[/code]

Config: cheapest と fastest バリアント付き Qwen json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen3-8B" },      models: {        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },        "huggingface/Qwen/Qwen3-8B:cheapest": { alias: "Qwen3 8B (cheapest)" },        "huggingface/Qwen/Qwen3-8B:fastest": { alias: "Qwen3 8B (fastest)" },      },    },  },}
[/code]

Config: エイリアス付き DeepSeek + Llama + GPT-OSS json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-V3.2",        fallbacks: [          "huggingface/meta-llama/Llama-3.3-70B-Instruct",          "huggingface/openai/gpt-oss-120b",        ],      },      models: {        "huggingface/deepseek-ai/DeepSeek-V3.2": { alias: "DeepSeek V3.2" },        "huggingface/meta-llama/Llama-3.3-70B-Instruct": { alias: "Llama 3.3 70B" },        "huggingface/openai/gpt-oss-120b": { alias: "GPT-OSS 120B" },      },    },  },}
[/code]

Config: ポリシーサフィックス付き複数の Qwen と DeepSeek json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest" },      models: {        "huggingface/Qwen/Qwen2.5-7B-Instruct": { alias: "Qwen2.5 7B" },        "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest": { alias: "Qwen2.5 7B (cheap)" },        "huggingface/deepseek-ai/DeepSeek-R1:fastest": { alias: "DeepSeek R1 (fast)" },        "huggingface/meta-llama/Llama-3.1-8B-Instruct": { alias: "Llama 3.1 8B" },      },    },  },}
[/code]

## 関連

[**モデル選択** すべてのプロバイダ、モデル参照、failover 動作の概要。 ](</ja-JP/concepts/model-providers>) [**モデル選択** モデルの選び方と設定方法。 ](</ja-JP/concepts/models>) [**Inference Providers docs** 公式 Hugging Face Inference Providers ドキュメント。 ](<https://huggingface.co/docs/inference-providers>) [**設定** 完全な設定リファレンス。 ](</ja-JP/gateway/configuration>)

Was this useful?YesNo