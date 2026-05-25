---
title: Perplexity 搜尋
source_url: https://docs.openclaw.ai/zh-TW/tools/perplexity-search
scraped_at: 2026-05-25
---

OpenClaw 支援 Perplexity Search API 作為 `web_search` 提供者。 它會傳回包含 `title`、`url` 與 `snippet` 欄位的結構化結果。

為了相容性，OpenClaw 也支援舊版 Perplexity Sonar/OpenRouter 設定。 如果你使用 `OPENROUTER_API_KEY`、在 `plugins.entries.perplexity.config.webSearch.apiKey` 中使用 `sk-or-...` 金鑰，或設定 `plugins.entries.perplexity.config.webSearch.baseUrl` / `model`，提供者會切換到 chat-completions 路徑，並傳回帶有引用的 AI 合成答案，而不是結構化的 Search API 結果。

## 取得 Perplexity API 金鑰

  1. 在 [perplexity.ai/settings/api](<https://www.perplexity.ai/settings/api>) 建立 Perplexity 帳號
  2. 在儀表板中產生 API 金鑰
  3. 將金鑰儲存在設定中，或在 Gateway 環境中設定 `PERPLEXITY_API_KEY`。


## OpenRouter 相容性

如果你已經使用 OpenRouter 搭配 Perplexity Sonar，請保留 `provider: "perplexity"`，並在 Gateway 環境中設定 `OPENROUTER_API_KEY`，或在 `plugins.entries.perplexity.config.webSearch.apiKey` 中儲存 `sk-or-...` 金鑰。

選用相容性控制項：

  * `plugins.entries.perplexity.config.webSearch.baseUrl`
  * `plugins.entries.perplexity.config.webSearch.model`


## 設定範例

### 原生 Perplexity Search API

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "pplx-...",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

### OpenRouter / Sonar 相容性

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "<openrouter-api-key>",            baseUrl: "https://openrouter.ai/api/v1",            model: "perplexity/sonar-pro",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

## 要在哪裡設定金鑰

**透過設定：** 執行 `openclaw configure --section web`。它會將金鑰儲存在 `~/.openclaw/openclaw.json` 的 `plugins.entries.perplexity.config.webSearch.apiKey` 下。 該欄位也接受 SecretRef 物件。

**透過環境：** 在 Gateway 程序環境中設定 `PERPLEXITY_API_KEY` 或 `OPENROUTER_API_KEY`。 若是 Gateway 安裝，請將它放在 `~/.openclaw/.env`（或你的服務環境）中。請參閱[環境變數](</zh-TW/help/faq#env-vars-and-env-loading>)。

如果已設定 `provider: "perplexity"`，且 Perplexity 金鑰 SecretRef 未解析且沒有環境備援，啟動/重新載入會快速失敗。

## 工具參數

這些參數適用於原生 Perplexity Search API 路徑。

搜尋查詢。

要傳回的結果數量 (1-10)。

2 字母 ISO 國家/地區代碼（例如 `US`、`DE`）。

ISO 639-1 語言代碼（例如 `en`、`de`、`fr`）。

時間篩選器 - `day` 為 24 小時。

只包含此日期之後發布的結果 (`YYYY-MM-DD`)。

只包含此日期之前發布的結果 (`YYYY-MM-DD`)。

網域允許清單/拒絕清單陣列（最多 20 個）。

總內容預算（最多 1000000）。

每頁 token 限制。

對於舊版 Sonar/OpenRouter 相容性路徑：

  * 接受 `query`、`count` 與 `freshness`
  * `count` 在此僅用於相容性；回應仍是一個帶有引用的合成答案，而不是 N 筆結果清單
  * 只適用於 Search API 的篩選器，例如 `country`、`language`、`date_after`、`date_before`、`domain_filter`、`max_tokens` 與 `max_tokens_per_page`，會傳回明確錯誤


**範例：**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (allowlist)await web_search({  query: "climate research",  domain_filter: ["nature.com", "science.org", ".edu"],}); // Domain filtering (denylist - prefix with -)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],}); // More content extractionawait web_search({  query: "detailed AI research",  max_tokens: 50000,  max_tokens_per_page: 4096,});
[/code]

### 網域篩選規則

  * 每個篩選器最多 20 個網域
  * 不能在同一個請求中混用允許清單與拒絕清單
  * 對拒絕清單項目使用 `-` 前綴（例如 `["-reddit.com"]`）


## 注意事項

  * Perplexity Search API 會傳回結構化網頁搜尋結果 (`title`、`url`、`snippet`)
  * OpenRouter 或明確的 `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` 會將 Perplexity 切回 Sonar chat completions 以維持相容性
  * Sonar/OpenRouter 相容性會傳回一個帶有引用的合成答案，而不是結構化結果列
  * 結果預設會快取 15 分鐘（可透過 `cacheTtlMinutes` 設定）


## 相關

[**Web search overview** 所有提供者與自動偵測規則。 ](</zh-TW/tools/web>) [**Brave search** 提供國家/地區與語言篩選器的結構化結果。 ](</zh-TW/tools/brave-search>) [**Exa search** 具內容擷取功能的神經搜尋。 ](</zh-TW/tools/exa-search>) [**Perplexity Search API docs** 官方 Perplexity Search API 快速入門與參考。 ](<https://docs.perplexity.ai/docs/search/quickstart>)

Was this useful?YesNo