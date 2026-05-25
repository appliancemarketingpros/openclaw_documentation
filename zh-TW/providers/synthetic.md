---
title: 合成
source_url: https://docs.openclaw.ai/zh-TW/providers/synthetic
scraped_at: 2026-05-25
---

[Synthetic](<https://synthetic.new>) 提供與 Anthropic 相容的端點。 OpenClaw 將其註冊為 `synthetic` 提供者，並使用 Anthropic Messages API。

屬性 | 值  
---|---  
提供者 | `synthetic`  
驗證 | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
基礎 URL | `https://api.synthetic.new/anthropic`  
  
## 開始使用

* ### 取得 API 金鑰

從你的 Synthetic 帳戶取得 `SYNTHETIC_API_KEY`，或讓 入門設定精靈提示你輸入一組金鑰。

* ### 執行入門設定

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### 驗證預設模型

完成入門設定後，預設模型會設為：

CodeCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## 設定範例

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## 內建目錄

所有 Synthetic 模型都使用成本 `0`（輸入/輸出/快取）。

模型 ID | 脈絡視窗 | 最大 Token 數 | 推理 | 輸入  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192,000 | 65,536 | 否 | text  
`hf:moonshotai/Kimi-K2-Thinking` | 256,000 | 8,192 | 是 | text  
`hf:zai-org/GLM-4.7` | 198,000 | 128,000 | 否 | text  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128,000 | 8,192 | 否 | text  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128,000 | 8,192 | 否 | text  
`hf:deepseek-ai/DeepSeek-V3.1` | 128,000 | 8,192 | 否 | text  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128,000 | 8,192 | 否 | text  
`hf:deepseek-ai/DeepSeek-V3.2` | 159,000 | 8,192 | 否 | text  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128,000 | 8,192 | 否 | text  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524,000 | 8,192 | 否 | text  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256,000 | 8,192 | 否 | text  
`hf:moonshotai/Kimi-K2.5` | 256,000 | 8,192 | 是 | text + image  
`hf:openai/gpt-oss-120b` | 128,000 | 8,192 | 否 | text  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256,000 | 8,192 | 否 | text  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256,000 | 8,192 | 否 | text  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250,000 | 8,192 | 否 | text + image  
`hf:zai-org/GLM-4.5` | 128,000 | 128,000 | 否 | text  
`hf:zai-org/GLM-4.6` | 198,000 | 128,000 | 否 | text  
`hf:zai-org/GLM-5` | 256,000 | 128,000 | 是 | text + image  
`hf:deepseek-ai/DeepSeek-V3` | 128,000 | 8,192 | 否 | text  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256,000 | 8,192 | 是 | text  
  
模型允許清單

如果你啟用模型允許清單（`agents.defaults.models`），請加入你計畫使用的每個 Synthetic 模型。不在允許清單中的模型會從代理程式中隱藏。

基礎 URL 覆寫

如果 Synthetic 變更其 API 端點，請在你的設定中覆寫基礎 URL：

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

請記得 OpenClaw 會自動附加 `/v1`。

## 相關

[**模型選擇** 提供者規則、模型參照，以及故障轉移行為。 ](</zh-TW/concepts/model-providers>) [**設定參考** 完整設定結構描述，包含提供者設定。 ](</zh-TW/gateway/configuration-reference>) [**Synthetic** Synthetic 儀表板與 API 文件。 ](<https://synthetic.new>)

Was this useful?YesNo