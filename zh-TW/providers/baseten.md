---
title: Baseten
source_url: https://docs.openclaw.ai/zh-TW/providers/baseten
scraped_at: 2026-07-20
---

Get started

[Baseten 模型 API](<https://docs.baseten.co/inference/model-apis/overview>) 提供由託管服務代管、與 OpenAI 相容的前沿模型存取方式。官方外部外掛會使用經過驗證的探索機制，因此 OpenClaw 會採用你 Baseten 帳戶所啟用的完整模型集合。其離線備援包含此 OpenClaw 版本建置時可用的所有模型 API。

屬性 | 值  
---|---  
提供者 ID | `baseten`  
外掛 | 官方外部套件（`@openclaw/baseten-provider`）  
驗證環境變數 | `BASETEN_API_KEY`  
初始設定旗標 | `--auth-choice baseten-api-key`  
直接命令列旗標 | `--baseten-api-key <key>`  
API | 與 OpenAI 相容（`openai-completions`）  
基礎 URL | `https://inference.baseten.co/v1`  
預設模型 | `baseten/thinkingmachines/inkling`  
  
## 安裝外掛

bashCopy code
[code]
    openclaw plugins install @openclaw/baseten-provideropenclaw gateway restart
[/code]

## 開始使用

* ### 建立 Baseten 帳戶和 API 金鑰

Baseten 的 Basic 方案不收取每月平台費用；模型 API 呼叫依用量計費。請在 [Baseten API 金鑰設定](<https://app.baseten.co/settings/api_keys>)中建立金鑰，並在[定價頁面](<https://www.baseten.co/pricing>)查看目前費率。

* ### 執行初始設定

初始設定Copy code
[code]
    openclaw onboard --auth-choice baseten-api-key
[/code]

直接旗標Copy code
[code]
    openclaw onboard --non-interactive \--auth-choice baseten-api-key \--baseten-api-key "$BASETEN_API_KEY"
[/code]

僅使用環境變數Copy code
[code]
    export BASETEN_API_KEY=...
[/code]

* ### 驗證即時目錄

bashCopy code
[code]
    openclaw models list --provider baseten
[/code]

若有可用的驗證資訊，外掛會請求 `GET /v1/models`，並列出帳戶所傳回的每個模型。若沒有驗證資訊，外掛會維持離線狀態並使用內建備援。

## Inkling

[Thinking Machines Lab 的 Inkling](<https://thinkingmachines.ai/news/introducing-inkling/>) 是預設模型。在 OpenClaw 中，它支援文字和圖片輸入、工具呼叫、結構化工具綱要、可設定的推理強度、1.048M token 的上下文視窗，以及最多 32k 個輸出 token：

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "baseten/thinkingmachines/inkling" },    },  },}
[/code]

使用 `/model baseten/thinkingmachines/inkling` 切換現有聊天的模型。

## 內建備援目錄

經過驗證的即時目錄是權威來源。在探索成功前，下列資料列可讓設定和模型選擇功能保持可用：

模型參照 | 輸入 | 上下文 | 最大輸出  
---|---|---|---  
`baseten/deepseek-ai/DeepSeek-V4-Pro` | 文字 | 262k | 262k  
`baseten/zai-org/GLM-4.7` | 文字 | 200k | 200k  
`baseten/zai-org/GLM-5` | 文字 | 202k | 202k  
`baseten/zai-org/GLM-5.1` | 文字 | 202k | 202k  
`baseten/zai-org/GLM-5.2` | 文字 | 202k | 202k  
`baseten/thinkingmachines/inkling` | 文字、圖片 | 1.048M | 32k  
`baseten/moonshotai/Kimi-K2.5` | 文字、圖片 | 262k | 262k  
`baseten/moonshotai/Kimi-K2.6` | 文字、圖片 | 262k | 262k  
`baseten/moonshotai/Kimi-K2.7-Code` | 文字、圖片 | 262k | 262k  
`baseten/nvidia/Nemotron-120B-A12B` | 文字 | 202k | 202k  
`baseten/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B` | 文字 | 202k | 202k  
`baseten/openai/gpt-oss-120b` | 文字 | 128k | 128k  
  
所有內建模型都支援工具呼叫和推理。OpenClaw 會將其思考層級對應至原生支援 `reasoning_effort` 的模型。Baseten 的選用式 GLM、Kimi 和 Nemotron 模型預設關閉思考；多數模型提供關閉／開啟二元控制，而 GLM 5.2 則提供關閉、高和最大。OpenClaw 會透過 Baseten 的 `chat_template_args.enable_thinking` 控制項傳送這些選擇；若為 GLM 5.2，還會使用經過驗證的頂層 `reasoning_effort` 參數。

## 手動設定

多數設定只需要 API 金鑰。若要明確固定使用此提供者：

json5Copy code
[code]
    {  env: { BASETEN_API_KEY: "..." },  agents: {    defaults: {      model: { primary: "baseten/thinkingmachines/inkling" },    },  },  models: {    mode: "merge",    providers: {      baseten: {        baseUrl: "https://inference.baseten.co/v1",        apiKey: "${BASETEN_API_KEY}",        api: "openai-completions",        models: [          {            id: "thinkingmachines/inkling",            name: "Inkling",            reasoning: true,            input: ["text", "image"],            contextWindow: 1048000,            maxTokens: 32000,            compat: {              supportsStore: false,              supportsDeveloperRole: false,              supportsUsageInStreaming: true,              supportsStrictMode: true,              supportsTools: true,              supportsReasoningEffort: true,              supportedReasoningEfforts: ["none", "minimal", "low", "medium", "high", "xhigh"],              reasoningEffortMap: {                off: "none",                none: "none",                adaptive: "xhigh",                max: "xhigh",              },              maxTokensField: "max_tokens",            },          },        ],      },    },  },}
[/code]

## 相關內容

[**模型提供者** 選擇提供者、模型參照和容錯移轉行為。 ](</zh-TW/concepts/model-providers>) [**思考模式** 選取 OpenClaw 的推理強度層級。 ](</zh-TW/tools/thinking>) [**模型命令列介面** 列出、檢查並選取探索到的模型。 ](</zh-TW/cli/models>) [**模型常見問題** 驗證設定檔與模型選擇疑難排解。 ](</zh-TW/help/faq-models>)

Was this useful?YesNo

Open issue