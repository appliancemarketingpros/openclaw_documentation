---
title: DeepSeek
source_url: https://docs.openclaw.ai/zh-TW/providers/deepseek
scraped_at: 2026-05-25
---

[DeepSeek](<https://www.deepseek.com>) 提供強大的 AI 模型，並具備與 OpenAI 相容的 API。

屬性 | 值  
---|---  
提供者 | `deepseek`  
驗證 | `DEEPSEEK_API_KEY`  
API | 與 OpenAI 相容  
基底 URL | `https://api.deepseek.com`  
  
## 開始使用

* ### 取得你的 API 金鑰

在 [platform.deepseek.com](<https://platform.deepseek.com/api_keys>) 建立 API 金鑰。

* ### 執行 onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice deepseek-api-key
[/code]

這會提示你輸入 API 金鑰，並將 `deepseek/deepseek-v4-flash` 設為預設模型。

* ### 確認模型可用

bashCopy code
[code]
    openclaw models list --provider deepseek
[/code]

若要在不需要執行中 Gateway 的情況下檢查內建的靜態目錄， 請使用：

bashCopy code
[code]
    openclaw models list --all --provider deepseek
[/code]

非互動式設定

對於指令碼化或無介面安裝，請直接傳入所有旗標：

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice deepseek-api-key \  --deepseek-api-key "$DEEPSEEK_API_KEY" \  --skip-health \  --accept-risk
[/code]

## 內建目錄

模型參照 | 名稱 | 輸入 | 上下文 | 最大輸出 | 備註  
---|---|---|---|---|---  
`deepseek/deepseek-v4-flash` | DeepSeek V4 Flash | text | 1,000,000 | 384,000 | 預設模型；支援 V4 思考能力的介面  
`deepseek/deepseek-v4-pro` | DeepSeek V4 Pro | text | 1,000,000 | 384,000 | 支援 V4 思考能力的介面  
`deepseek/deepseek-chat` | DeepSeek Chat | text | 131,072 | 8,192 | DeepSeek V3.2 非思考介面  
`deepseek/deepseek-reasoner` | DeepSeek Reasoner | text | 131,072 | 65,536 | 啟用推理的 V3.2 介面  
  
## 思考與工具

相較於大多數與 OpenAI 相容的提供者，DeepSeek V4 思考工作階段有更嚴格的重播契約：啟用思考的回合使用工具後，DeepSeek 會期望該回合中重播的 assistant 訊息在後續請求中包含 `reasoning_content`。OpenClaw 會在 DeepSeek Plugin 內處理這一點，因此一般的多回合工具使用可搭配 `deepseek/deepseek-v4-flash` 和 `deepseek/deepseek-v4-pro` 正常運作。

如果你將既有工作階段從另一個與 OpenAI 相容的提供者切換到 DeepSeek V4 模型，較舊的 assistant 工具呼叫回合可能沒有原生的 DeepSeek `reasoning_content`。OpenClaw 會在 DeepSeek V4 思考請求中，為重播的 assistant 訊息補上該缺少的欄位，讓提供者可接受歷史記錄，而不需要 `/new`。

在 OpenClaw 中停用思考時（包含 UI 的 **無** 選項）， OpenClaw 會傳送 DeepSeek `thinking: { type: "disabled" }`，並從傳出的歷史記錄中移除重播的 `reasoning_content`。這會讓已停用思考的工作階段維持在 DeepSeek 的非思考路徑。

預設快速路徑請使用 `deepseek/deepseek-v4-flash`。如果你想要更強的 V4 模型，且可以接受 較高成本或延遲，請使用 `deepseek/deepseek-v4-pro`。

## 即時測試

直接即時模型套件在現代模型集合中包含 DeepSeek V4。若要 只執行 DeepSeek V4 直接模型檢查：

bashCopy code
[code]
    OPENCLAW_LIVE_PROVIDERS=deepseek \OPENCLAW_LIVE_MODELS="deepseek/deepseek-v4-flash,deepseek/deepseek-v4-pro" \pnpm test:live src/agents/models.profiles.live.test.ts
[/code]

該即時檢查會驗證兩個 V4 模型都能完成，並確認思考/工具 後續回合會保留 DeepSeek 所需的重播酬載。

## 設定範例

json5Copy code
[code]
    {  env: { DEEPSEEK_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "deepseek/deepseek-v4-flash" },    },  },}
[/code]

## 相關

[**模型選擇** 選擇提供者、模型參照與容錯移轉行為。 ](</zh-TW/concepts/model-providers>) [**設定參考** agent、模型與提供者的完整設定參考。 ](</zh-TW/gateway/configuration-reference>)

Was this useful?YesNo