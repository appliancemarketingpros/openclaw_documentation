---
title: Perplexity
source_url: https://docs.openclaw.ai/zh-TW/providers/perplexity-provider
scraped_at: 2026-05-25
---

Perplexity Plugin 透過 Perplexity Search API 或經由 OpenRouter 使用 Perplexity Sonar，提供網頁搜尋功能。

屬性 | 值  
---|---  
類型 | 網頁搜尋供應器（不是模型供應器）  
驗證 | `PERPLEXITY_API_KEY`（直接）或 `OPENROUTER_API_KEY`（透過 OpenRouter）  
設定路徑 | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## 開始使用

* ### 設定 API 金鑰

執行互動式網頁搜尋設定流程：

bashCopy code
[code]
    openclaw configure --section web
[/code]

或直接設定金鑰：

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### 開始搜尋

金鑰設定完成後，代理會自動使用 Perplexity 進行網頁搜尋。不需要其他步驟。

## 搜尋模式

Plugin 會根據 API 金鑰前綴自動選擇傳輸方式：

### 原生 Perplexity API (pplx-)

當你的金鑰以 `pplx-` 開頭時，OpenClaw 會使用原生 Perplexity Search API。此傳輸方式會傳回結構化結果，並支援網域、語言與日期篩選器（請參閱下方的篩選選項）。

### OpenRouter / Sonar (sk-or-)

當你的金鑰以 `sk-or-` 開頭時，OpenClaw 會透過 OpenRouter，使用 Perplexity Sonar 模型進行路由。此傳輸方式會傳回帶有引用來源的 AI 綜合答案。

金鑰前綴 | 傳輸方式 | 功能  
---|---|---  
`pplx-` | 原生 Perplexity Search API | 結構化結果、網域/語言/日期篩選器  
`sk-or-` | OpenRouter (Sonar) | 帶有引用來源的 AI 綜合答案  
  
## 原生 API 篩選

使用原生 Perplexity API 時，搜尋支援下列篩選器：

篩選器 | 說明 | 範例  
---|---|---  
國家 | 2 個字母的國家代碼 | `us`, `de`, `jp`  
語言 | ISO 639-1 語言代碼 | `en`, `fr`, `zh`  
日期範圍 | 近期時間範圍 | `day`, `week`, `month`, `year`  
網域篩選器 | 允許清單或封鎖清單（最多 20 個網域） | `example.com`  
內容預算 | 每次回應 / 每頁的 Token 限制 | `max_tokens`, `max_tokens_per_page`  
  
## 進階設定

Daemon 程序的環境變數

如果 OpenClaw Gateway 以 daemon（launchd/systemd）方式執行，請確認該程序可使用 `PERPLEXITY_API_KEY`。

OpenRouter 代理設定

如果你偏好透過 OpenRouter 路由 Perplexity 搜尋，請設定 `OPENROUTER_API_KEY`（前綴 `sk-or-`），而不是原生 Perplexity 金鑰。OpenClaw 會偵測此前綴，並自動切換到 Sonar 傳輸方式。

## 相關

[**Perplexity search tool** 代理如何叫用 Perplexity 搜尋並解讀結果。 ](</zh-TW/tools/perplexity-search>) [**設定參考** 包含 Plugin entries 的完整設定參考。 ](</zh-TW/gateway/configuration-reference>)

Was this useful?YesNo