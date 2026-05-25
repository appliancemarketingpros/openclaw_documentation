---
title: SearXNG 搜尋
source_url: https://docs.openclaw.ai/zh-TW/tools/searxng-search
scraped_at: 2026-05-25
---

OpenClaw 支援 [SearXNG](<https://docs.searxng.org/>) 作為**自託管、 免金鑰** 的 `web_search` 提供者。SearXNG 是一個開源的元搜尋引擎， 會彙整來自 Google、Bing、DuckDuckGo 和其他來源的結果。

優點：

  * **免費且不限量** \-- 不需要 API 金鑰或商業訂閱
  * **隱私 / 空氣隔離** \-- 查詢永遠不會離開你的網路
  * **可在任何地方使用** \-- 不受商業搜尋 API 的區域限制


## 設定

* ### 執行 SearXNG 執行個體

bashCopy code
[code]
    docker run -d -p 8888:8080 searxng/searxng
[/code]

或使用任何你有權存取的現有 SearXNG 部署。請參閱 [SearXNG 文件](<https://docs.searxng.org/>)以了解正式環境設定。

* ### 設定

bashCopy code
[code]
    openclaw configure --section web# Select "searxng" as the provider
[/code]

或設定環境變數，讓自動偵測找到它：

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

## 設定

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "searxng",      },    },  },}
[/code]

SearXNG 執行個體的 Plugin 層級設定：

json5Copy code
[code]
    {  plugins: {    entries: {      searxng: {        config: {          webSearch: {            baseUrl: "http://localhost:8888",            categories: "general,news", // optional            language: "en", // optional          },        },      },    },  },}
[/code]

`baseUrl` 欄位也接受 SecretRef 物件。

傳輸規則：

  * `https://` 可用於公開或私有 SearXNG 主機
  * `http://` 僅接受用於受信任的私有網路或回送主機
  * 公開 SearXNG 主機必須使用 `https://`
  * 私有/內部主機使用自託管網路防護；公開 `https://` 主機會保留嚴格的網路搜尋防護，且不能重新導向到私有 位址


## 環境變數

設定 `SEARXNG_BASE_URL` 作為設定的替代方式：

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

設定 `SEARXNG_BASE_URL` 且未設定明確提供者時，自動偵測 會自動選擇 SearXNG（優先順序最低 -- 任何有 金鑰的 API 型提供者都會優先勝出）。

## Plugin 設定參考

欄位 | 說明  
---|---  
`baseUrl` | 你的 SearXNG 執行個體基底 URL（必填）  
`categories` | 以逗號分隔的分類，例如 `general`、`news` 或 `science`  
`language` | 結果的語言代碼，例如 `en`、`de` 或 `fr`  
  
## 備註

  * **JSON API** \-- 使用 SearXNG 原生 `format=json` 端點，而非 HTML 擷取
  * **圖片結果 URL** \-- 當 SearXNG 回傳直接圖片 URL 時，圖片分類結果會包含 `img_src`
  * **不需要 API 金鑰** \-- 可直接搭配任何 SearXNG 執行個體使用
  * **基底 URL 驗證** \-- `baseUrl` 必須是有效的 `http://` 或 `https://` URL；公開主機必須使用 `https://`
  * **網路防護** \-- 私有/內部 SearXNG 端點可選擇加入 私有網路存取；公開 `https://` SearXNG 端點則保留嚴格的 SSRF 保護
  * **自動偵測順序** \-- SearXNG 在自動偵測中最後檢查（順序 200）。 已設定金鑰的 API 型提供者會先執行，接著是 DuckDuckGo（順序 100），再來是 Ollama Web Search（順序 110）
  * **自託管** \-- 你控制執行個體、查詢和上游搜尋引擎
  * **分類** 未設定時預設為 `general`
  * **分類後援** \-- 如果非 `general` 分類請求成功但 回傳零筆結果，OpenClaw 會在回傳空結果集之前，使用 `general` 對相同查詢重試一次


## 相關

  * [網路搜尋概觀](</zh-TW/tools/web>) \-- 所有提供者和自動偵測
  * [DuckDuckGo 搜尋](</zh-TW/tools/duckduckgo-search>) \-- 另一個免金鑰後援
  * [Brave Search](</zh-TW/tools/brave-search>) \-- 提供免費層級的結構化結果


Was this useful?YesNo