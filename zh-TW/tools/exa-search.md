---
title: Exa 搜尋
source_url: https://docs.openclaw.ai/zh-TW/tools/exa-search
scraped_at: 2026-05-25
---

OpenClaw 支援 [Exa AI](<https://exa.ai/>) 作為 `web_search` 提供者。Exa 提供神經、關鍵字與混合搜尋模式，並內建內容擷取 （重點、文字、摘要）。

## 取得 API 金鑰

* ### 建立帳戶

在 [exa.ai](<https://exa.ai/>) 註冊，並從你的 儀表板產生 API 金鑰。

* ### 儲存金鑰

在 Gateway 環境中設定 `EXA_API_KEY`，或透過以下方式設定：

bashCopy code
[code]
    openclaw configure --section web
[/code]

## 設定

json5Copy code
[code]
    {  plugins: {    entries: {      exa: {        config: {          webSearch: {            apiKey: "exa-...", // optional if EXA_API_KEY is set            baseUrl: "https://api.exa.ai", // optional; OpenClaw appends /search          },        },      },    },  },  tools: {    web: {      search: {        provider: "exa",      },    },  },}
[/code]

**環境替代方案：**在 Gateway 環境中設定 `EXA_API_KEY`。 若是 gateway 安裝，請將其放在 `~/.openclaw/.env`。

## 覆寫基底 URL

當 Exa 搜尋請求應透過相容代理或替代 Exa 端點時， 設定 `plugins.entries.exa.config.webSearch.baseUrl`。OpenClaw 會透過在裸主機前加上 `https://` 來正規化，並附加 `/search`，除非 路徑已經以該處結尾。解析後的端點會包含在搜尋快取 金鑰中，因此來自不同 Exa 端點的結果不會共用。

## 工具參數

搜尋查詢。

要傳回的結果數量（1–100）。

搜尋模式。

時間篩選器。

此日期之後的結果（`YYYY-MM-DD`）。

此日期之前的結果（`YYYY-MM-DD`）。

內容擷取選項（見下方）。

### 內容擷取

Exa 可以在搜尋結果旁傳回擷取出的內容。傳入 `contents` 物件以啟用：

javascriptCopy code
[code]
    await web_search({  query: "transformer architecture explained",  type: "neural",  contents: {    text: true, // full page text    highlights: { numSentences: 3 }, // key sentences    summary: true, // AI summary  },});
[/code]

內容選項 | 型別 | 說明  
---|---|---  
`text` | `boolean | { maxCharacters }` | 擷取完整頁面文字  
`highlights` | `boolean | { maxCharacters, query, numSentences, highlightsPerUrl }` | 擷取關鍵句子  
`summary` | `boolean | { query }` | AI 產生的摘要  
  
### 搜尋模式

模式 | 說明  
---|---  
`auto` | Exa 選擇最佳模式（預設）  
`neural` | 語意／基於意義的搜尋  
`fast` | 快速關鍵字搜尋  
`deep` | 深入完整的深度搜尋  
`deep-reasoning` | 具推理能力的深度搜尋  
`instant` | 最快的結果  
  
## 備註

  * 如果未提供 `contents` 選項，Exa 預設為 `{ highlights: true }`， 因此結果會包含關鍵句子摘錄
  * 可用時，結果會保留 Exa API 回應中的 `highlightScores` 與 `summary` 欄位
  * 結果描述會先從重點解析，接著是摘要，再來是 完整文字，以可用者為準
  * `freshness` 與 `date_after`/`date_before` 無法合併使用，請使用一種 時間篩選模式
  * 每個查詢最多可傳回 100 筆結果（受 Exa 搜尋類型 限制約束）
  * 結果預設快取 15 分鐘（可透過 `cacheTtlMinutes` 設定）
  * Exa 是官方 API 整合，具備結構化 JSON 回應


## 相關

  * [Web Search 概觀](</zh-TW/tools/web>) \-- 所有提供者與自動偵測
  * [Brave Search](</zh-TW/tools/brave-search>) \-- 具國家／語言篩選器的結構化結果
  * [Perplexity Search](</zh-TW/tools/perplexity-search>) \-- 具網域篩選的結構化結果


Was this useful?YesNo