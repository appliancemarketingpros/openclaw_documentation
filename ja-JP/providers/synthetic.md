---
title: Synthetic
source_url: https://docs.openclaw.ai/ja-JP/providers/synthetic
scraped_at: 2026-05-25
---

[Synthetic](<https://synthetic.new>)はAnthropic互換エンドポイントを公開しています。 OpenClawはこれを`synthetic`プロバイダーとして登録し、Anthropic Messages APIを使用します。

プロパティ | 値  
---|---  
プロバイダー | `synthetic`  
認証 | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
Base URL | `https://api.synthetic.new/anthropic`  
  
## はじめに

* ### API keyを取得する

Syntheticアカウントから`SYNTHETIC_API_KEY`を取得するか、 オンボーディングウィザードに入力を促させてください。

* ### オンボーディングを実行する

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### デフォルトモデルを確認する

オンボーディング後、デフォルトモデルは次に設定されます:

CodeCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## 設定例

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## 組み込みカタログ

すべてのSyntheticモデルはコスト`0`（input/output/cache）を使用します。

モデルID | コンテキストウィンドウ | 最大トークン | Reasoning | 入力  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192,000 | 65,536 | no | text  
`hf:moonshotai/Kimi-K2-Thinking` | 256,000 | 8,192 | yes | text  
`hf:zai-org/GLM-4.7` | 198,000 | 128,000 | no | text  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3.1` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3.2` | 159,000 | 8,192 | no | text  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128,000 | 8,192 | no | text  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524,000 | 8,192 | no | text  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256,000 | 8,192 | no | text  
`hf:moonshotai/Kimi-K2.5` | 256,000 | 8,192 | yes | text + image  
`hf:openai/gpt-oss-120b` | 128,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250,000 | 8,192 | no | text + image  
`hf:zai-org/GLM-4.5` | 128,000 | 128,000 | no | text  
`hf:zai-org/GLM-4.6` | 198,000 | 128,000 | no | text  
`hf:zai-org/GLM-5` | 256,000 | 128,000 | yes | text + image  
`hf:deepseek-ai/DeepSeek-V3` | 128,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256,000 | 8,192 | yes | text  
  
モデルallowlist

モデルallowlist（`agents.defaults.models`）を有効にする場合は、 使用予定のSyntheticモデルをすべて追加してください。allowlistにないモデルは、 エージェントから見えなくなります。

Base URL上書き

SyntheticがAPIエンドポイントを変更した場合は、設定内でbase URLを上書きしてください。

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

OpenClawは自動的に`/v1`を追加することを忘れないでください。

## 関連

[**Model selection** プロバイダールール、モデル参照、およびフェイルオーバー動作。 ](</ja-JP/concepts/model-providers>) [**Configuration reference** プロバイダー設定を含む完全な設定スキーマ。 ](</ja-JP/gateway/configuration-reference>) [**Synthetic** SyntheticダッシュボードとAPIドキュメント。 ](<https://synthetic.new>)

Was this useful?YesNo