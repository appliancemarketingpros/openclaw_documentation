---
title: Honcho 記憶
source_url: https://docs.openclaw.ai/zh-TW/concepts/memory-honcho
scraped_at: 2026-05-25
---

[Honcho](<https://honcho.dev>) 為 OpenClaw 加入 AI 原生記憶。它會將對話持久化到專用服務，並隨時間建立使用者與代理模型，讓你的代理取得跨工作階段的脈絡，超越工作區 Markdown 檔案所能提供的範圍。

## 它提供的功能

  * **跨工作階段記憶** \-- 每一輪之後都會持久化對話，因此脈絡可在工作階段重設、Compaction 和切換頻道時延續。
  * **使用者建模** \-- Honcho 會為每位使用者維護設定檔（偏好、事實、溝通風格），也會為代理維護設定檔（個性、已學習的行為）。
  * **語意搜尋** \-- 搜尋過去對話中的觀察，而不只是目前工作階段。
  * **多代理感知** \-- 父代理會自動追蹤產生的子代理，並在子工作階段中將父代理加入為觀察者。


## 可用工具

Honcho 會註冊代理可在對話期間使用的工具：

**資料擷取（快速，無需 LLM 呼叫）：**

工具 | 功能  
---|---  
`honcho_context` | 跨工作階段的完整使用者表示  
`honcho_search_conclusions` | 對已儲存結論進行語意搜尋  
`honcho_search_messages` | 跨工作階段尋找訊息（依傳送者、日期篩選）  
`honcho_session` | 目前工作階段歷史與摘要  
  
**問答（由 LLM 驅動）：**

工具 | 功能  
---|---  
`honcho_ask` | 詢問關於使用者的問題。`depth='quick'` 用於事實，`'thorough'` 用於綜合分析  
  
## 開始使用

安裝 Plugin 並執行設定：

bashCopy code
[code]
    openclaw plugins install @honcho-ai/openclaw-honchoopenclaw honcho setupopenclaw gateway --force
[/code]

設定指令會提示輸入你的 API 認證、寫入設定，並可選擇遷移現有工作區記憶檔案。

## 設定

設定位於 `plugins.entries["openclaw-honcho"].config` 下：

json5Copy code
[code]
    {  plugins: {    entries: {      "openclaw-honcho": {        config: {          apiKey: "your-api-key", // omit for self-hosted          workspaceId: "openclaw", // memory isolation          baseUrl: "https://api.honcho.dev",        },      },    },  },}
[/code]

若使用自架執行個體，請將 `baseUrl` 指向你的本機伺服器（例如 `http://localhost:8000`），並省略 API 金鑰。

## 遷移現有記憶

如果你已有現有的工作區記憶檔案（`USER.md`、`MEMORY.md`、`IDENTITY.md`、`memory/`、`canvas/`），`openclaw honcho setup` 會偵測並提供遷移選項。

## 運作方式

每次 AI 回合之後，對話都會持久化到 Honcho。使用者與代理訊息都會被觀察，讓 Honcho 能夠隨時間建立並改進其模型。

在對話期間，Honcho 工具會在 `before_prompt_build` 階段查詢服務，在模型看到提示之前注入相關脈絡。這可確保準確的回合邊界與相關回憶。

## Honcho 與內建記憶比較

| 內建 / QMD | Honcho  
---|---|---  
**儲存** | 工作區 Markdown 檔案 | 專用服務（本機或代管）  
**跨工作階段** | 透過記憶檔案 | 自動、內建  
**使用者建模** | 手動（寫入 [MEMORY.md](<http://MEMORY.md>)） | 自動設定檔  
**搜尋** | 向量 + 關鍵字（混合） | 對觀察進行語意搜尋  
**多代理** | 未追蹤 | 父/子感知  
**相依性** | 無（內建）或 QMD 二進位檔 | 安裝 Plugin  
  
Honcho 與內建記憶系統可以搭配運作。設定 QMD 後，會提供額外工具，可在搜尋本機 Markdown 檔案的同時，使用 Honcho 的跨工作階段記憶。

## CLI 指令

bashCopy code
[code]
    openclaw honcho setup                        # Configure API key and migrate filesopenclaw honcho status                       # Check connection statusopenclaw honcho ask <question>               # Query Honcho about the useropenclaw honcho search <query> [-k N] [-d D] # Semantic search over memory
[/code]

## 延伸閱讀

  * [Plugin 原始碼](<https://github.com/plastic-labs/openclaw-honcho>)
  * [Honcho 文件](<https://docs.honcho.dev>)
  * [Honcho OpenClaw 整合指南](<https://docs.honcho.dev/v3/guides/integrations/openclaw>)
  * [記憶](</zh-TW/concepts/memory>) \-- OpenClaw 記憶概觀
  * [Context Engines](</zh-TW/concepts/context-engine>) \-- Plugin 脈絡引擎的運作方式


## 相關

  * [記憶概觀](</zh-TW/concepts/memory>)
  * [內建記憶引擎](</zh-TW/concepts/memory-builtin>)
  * [QMD 記憶引擎](</zh-TW/concepts/memory-qmd>)


Was this useful?YesNo