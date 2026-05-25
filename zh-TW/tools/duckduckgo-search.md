---
title: DuckDuckGo 搜尋
source_url: https://docs.openclaw.ai/zh-TW/tools/duckduckgo-search
scraped_at: 2026-05-25
---

OpenClaw 支援 DuckDuckGo 作為**免金鑰** 的 `web_search` 提供者。不需要 API 金鑰或帳戶。

## 設定

不需要 API 金鑰，只要將 DuckDuckGo 設為你的提供者：

* ### 設定

bashCopy code
[code]
    openclaw configure --section web# Select "duckduckgo" as the provider
[/code]

## 設定

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

Plugin 層級的選用地區與 SafeSearch 設定：

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo region code            safeSearch: "moderate", // "strict", "moderate", or "off"          },        },      },    },  },}
[/code]

## 工具參數

搜尋查詢。

要傳回的結果數量（1-10）。

DuckDuckGo 地區代碼（例如 `us-en`、`uk-en`、`de-de`）。

SafeSearch 等級。

地區與 SafeSearch 也可以在 Plugin 設定中設定（見上方）；工具參數會依每次查詢覆寫設定值。

## 注意事項

  * **不需要 API 金鑰** \- 開箱即用，零設定
  * **實驗性** \- 從 DuckDuckGo 的非 JavaScript HTML 搜尋頁面收集結果，而不是使用官方 API 或 SDK
  * **機器人驗證風險** \- 在大量或自動化使用時，DuckDuckGo 可能會提供 CAPTCHA 或封鎖請求
  * **HTML 解析** \- 結果取決於頁面結構，而頁面結構可能會在未通知的情況下變更
  * **自動偵測順序** \- DuckDuckGo 是第一個免金鑰備援選項（順序 100）。已設定金鑰的 API 支援提供者會先執行，接著是 Ollama Web Search（順序 110），再來是 SearXNG（順序 200）
  * **未設定時，SafeSearch 預設為 moderate**


## 相關內容

  * [Web Search 概觀](</zh-TW/tools/web>) \-- 所有提供者與自動偵測
  * [Brave Search](</zh-TW/tools/brave-search>) \-- 提供免費層級的結構化結果
  * [Exa Search](</zh-TW/tools/exa-search>) \-- 具備內容擷取的神經搜尋


Was this useful?YesNo