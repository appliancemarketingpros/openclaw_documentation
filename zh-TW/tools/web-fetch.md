---
title: 網頁擷取
source_url: https://docs.openclaw.ai/zh-TW/tools/web-fetch
scraped_at: 2026-05-25
---

`web_fetch` 工具會執行一般 HTTP GET，並擷取可讀內容 （將 HTML 轉為 markdown 或文字）。它**不會** 執行 JavaScript。

對於大量使用 JS 的網站或受登入保護的頁面，請改用 [網頁瀏覽器](</zh-TW/tools/browser>)。

## 快速開始

`web_fetch` **預設啟用** ，不需要設定。Agent 可以立即呼叫它：

javascriptCopy code
[code]
    await web_fetch({ url: "https://example.com/article" });
[/code]

## 工具參數

要擷取的 URL。僅限 `http(s)`。

主要內容擷取後的輸出格式。

將輸出截斷為此字元數。

## 運作方式

* ### Fetch

使用類似 Chrome 的 User-Agent 和 `Accept-Language` 標頭傳送 HTTP GET。阻擋私有/內部主機名稱，並重新檢查重新導向。

* ### Extract

對 HTML 回應執行 Readability（主要內容擷取）。

* ### Fallback (optional)

如果 Readability 失敗且已設定 Firecrawl，會透過 Firecrawl API 以繞過機器人防護模式重試。

* ### Cache

結果會快取 15 分鐘（可設定），以減少重複擷取相同 URL。

## 設定

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        enabled: true, // default: true        provider: "firecrawl", // optional; omit for auto-detect        maxChars: 50000, // max output chars        maxCharsCap: 50000, // hard cap for maxChars param        maxResponseBytes: 2000000, // max download size before truncation        timeoutSeconds: 30,        cacheTtlMinutes: 15,        maxRedirects: 3,        useTrustedEnvProxy: false, // let a trusted HTTP(S) env proxy resolve DNS        readability: true, // use Readability extraction        userAgent: "Mozilla/5.0 ...", // override User-Agent        ssrfPolicy: {          allowRfc2544BenchmarkRange: true, // opt-in for trusted fake-IP proxies using 198.18.0.0/15          allowIpv6UniqueLocalRange: true, // opt-in for trusted fake-IP proxies using fc00::/7        },      },    },  },}
[/code]

## Firecrawl 後備

如果 Readability 擷取失敗，`web_fetch` 可以後備使用 [Firecrawl](</zh-TW/tools/firecrawl>) 來繞過機器人防護並取得更好的擷取效果：

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        provider: "firecrawl", // optional; omit for auto-detect from available credentials      },    },  },  plugins: {    entries: {      firecrawl: {        enabled: true,        config: {          webFetch: {            apiKey: "fc-...", // optional if FIRECRAWL_API_KEY is set            baseUrl: "https://api.firecrawl.dev",            onlyMainContent: true,            maxAgeMs: 86400000, // cache duration (1 day)            timeoutSeconds: 60,          },        },      },    },  },}
[/code]

`plugins.entries.firecrawl.config.webFetch.apiKey` 支援 SecretRef 物件。 舊版 `tools.web.fetch.firecrawl.*` 設定會由 `openclaw doctor --fix` 自動遷移。

目前的執行階段行為：

  * `tools.web.fetch.provider` 會明確選取擷取後備提供者。
  * 如果省略 `provider`，OpenClaw 會從可用憑證中自動偵測第一個就緒的網頁擷取 提供者。非沙箱化的 `web_fetch` 可以使用已安裝、宣告 `contracts.webFetchProviders` 並在執行階段註冊相符提供者的 plugins。 目前內建提供者是 Firecrawl。
  * 沙箱化的 `web_fetch` 呼叫仍限制為內建提供者。
  * 如果停用 Readability，`web_fetch` 會直接跳到選定的 提供者後備。如果沒有可用提供者，它會以封閉方式失敗。


## 受信任環境代理

如果你的部署需要讓 `web_fetch` 透過受信任的對外 HTTP(S) 代理，請設定 `tools.web.fetch.useTrustedEnvProxy: true`。

在此模式中，OpenClaw 仍會在送出請求前套用基於主機名稱的 SSRF 檢查， 但會讓代理解析 DNS，而不是執行本機 DNS 釘選。只有在代理由操作員控制，且會在 DNS 解析後強制執行 對外政策時，才啟用此選項。

## 限制與安全性

  * `maxChars` 會被限制在 `tools.web.fetch.maxCharsCap` 內
  * 回應本文會在剖析前被限制為 `maxResponseBytes`；過大的 回應會被截斷並附上警告
  * 私有/內部主機名稱會被阻擋
  * `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` 和 `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` 是狹義的選擇加入， 用於受信任的假 IP 代理堆疊；除非你的代理擁有 這些合成範圍並強制執行自己的目的地政策，否則請保持未設定
  * 重新導向會被檢查，並受 `maxRedirects` 限制
  * `useTrustedEnvProxy` 是明確的選擇加入，且只應針對 操作員控制、並仍會在 DNS 解析後強制執行對外政策的代理啟用
  * `web_fetch` 是盡力而為的工具，有些網站需要使用[網頁瀏覽器](</zh-TW/tools/browser>)


## 工具設定檔

如果你使用工具設定檔或允許清單，請加入 `web_fetch` 或 `group:web`：

json5Copy code
[code]
    {  tools: {    allow: ["web_fetch"],    // or: allow: ["group:web"]  (includes web_fetch, web_search, and x_search)  },}
[/code]

## 相關

  * [網頁搜尋](</zh-TW/tools/web>) \-- 使用多個提供者搜尋網路
  * [網頁瀏覽器](</zh-TW/tools/browser>) \-- 針對大量使用 JS 的網站進行完整瀏覽器自動化
  * [Firecrawl](</zh-TW/tools/firecrawl>) \-- Firecrawl 搜尋與擷取工具


Was this useful?YesNo