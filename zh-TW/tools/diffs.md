---
title: 差異
source_url: https://docs.openclaw.ai/zh-TW/tools/diffs
scraped_at: 2026-05-25
---

`diffs` 是一個可選的 Plugin 工具，內建簡短的系統指引，並附帶一個配套 skill，可將變更內容轉換為供代理使用的唯讀 diff 成品。

它接受以下任一輸入：

  * `before` 與 `after` 文字
  * 統一格式的 `patch`


它可以回傳：

  * 用於 canvas 呈現的 Gateway 檢視器 URL
  * 用於訊息傳送的已算繪檔案路徑（PNG 或 PDF）
  * 在一次呼叫中同時回傳兩種輸出


啟用後，Plugin 會在系統提示空間前置簡潔的使用指引，也會公開詳細的 skill，供代理需要更完整說明時使用。

## 快速開始

* ### 安裝 Plugin

bashCopy code
[code]
    openclaw plugins install diffs
[/code]

* ### 啟用 Plugin

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,      },    },  },}
[/code]

* ### 選擇模式

### view

以 canvas 為優先的流程：代理使用 `mode: "view"` 呼叫 `diffs`，並透過 `canvas present` 開啟 `details.viewerUrl`。

### file

聊天檔案傳送：代理使用 `mode: "file"` 呼叫 `diffs`，並使用 `message` 搭配 `path` 或 `filePath` 傳送 `details.filePath`。

### both

合併模式：代理使用 `mode: "both"` 呼叫 `diffs`，在一次呼叫中取得兩種成品。

## 停用內建系統指引

如果你想保留啟用 `diffs` 工具，但停用其內建的系統提示指引，請將 `plugins.entries.diffs.hooks.allowPromptInjection` 設為 `false`：

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        hooks: {          allowPromptInjection: false,        },      },    },  },}
[/code]

這會封鎖 diffs Plugin 的 `before_prompt_build` hook，同時保留 Plugin、工具與配套 skill 可用。

如果你想同時停用指引與工具，請改為停用 Plugin。

## 典型代理工作流程

* ### 呼叫 diffs

代理使用輸入呼叫 `diffs` 工具。

* ### 讀取 details

代理從回應讀取 `details` 欄位。

* ### 呈現

代理可以透過 `canvas present` 開啟 `details.viewerUrl`，使用 `message` 搭配 `path` 或 `filePath` 傳送 `details.filePath`，或兩者都做。

## 輸入範例

### Before and after

jsonCopy code
[code]
    {  "before": "# Hello\n\nOne",  "after": "# Hello\n\nTwo",  "path": "docs/example.md",  "mode": "view"}
[/code]

### Patch

jsonCopy code
[code]
    {  "patch": "diff --git a/src/example.ts b/src/example.ts\n--- a/src/example.ts\n+++ b/src/example.ts\n@@ -1 +1 @@\n-const x = 1;\n+const x = 2;\n",  "mode": "both"}
[/code]

## 工具輸入參考

除非另有註明，所有欄位皆為選用。

原始文字。省略 `patch` 時，必須與 `after` 一起提供。

更新後文字。省略 `patch` 時，必須與 `before` 一起提供。

統一 diff 文字。與 `before` 和 `after` 互斥。

before and after 模式的顯示檔名。

before and after 模式的語言覆寫提示。未知值會退回純文字。

檢視器標題覆寫。

輸出模式。預設為 Plugin 預設值 `defaults.mode`。已棄用別名：`"image"` 的行為與 `"file"` 相同，且仍為了向後相容而接受。

檢視器主題。預設為 Plugin 預設值 `defaults.theme`。

Diff 版面配置。預設為 Plugin 預設值 `defaults.layout`。

當完整內容可用時，展開未變更區段。僅為單次呼叫選項（不是 Plugin 預設鍵）。

已算繪檔案格式。預設為 Plugin 預設值 `defaults.fileFormat`。

PNG 或 PDF 算繪的品質預設。

裝置縮放覆寫（`1`-`4`）。

CSS 像素中的最大算繪寬度（`640`-`2400`）。

檢視器與獨立檔案輸出的成品 TTL，以秒為單位。最大 21600。

檢視器 URL 來源覆寫。會覆寫 Plugin `viewerBaseUrl`。必須是 `http` 或 `https`，不可有查詢/雜湊。

舊版輸入別名

為了向後相容，仍然接受：

  * `format` -> `fileFormat`
  * `imageFormat` -> `fileFormat`
  * `imageQuality` -> `fileQuality`
  * `imageScale` -> `fileScale`
  * `imageMaxWidth` -> `fileMaxWidth`

驗證與限制

  * `before` 和 `after` 各自最大 512 KiB。
  * `patch` 最大 2 MiB。
  * `path` 最大 2048 位元組。
  * `lang` 最大 128 位元組。
  * `title` 最大 1024 位元組。
  * Patch 複雜度上限：最多 128 個檔案與 120000 總行數。
  * 同時提供 `patch` 與 `before` 或 `after` 會遭拒。
  * 已算繪檔案安全限制（適用於 PNG 和 PDF）： 
    * `fileQuality: "standard"`：最多 8 MP（8,000,000 個算繪像素）。
    * `fileQuality: "hq"`：最多 14 MP（14,000,000 個算繪像素）。
    * `fileQuality: "print"`：最多 24 MP（24,000,000 個算繪像素）。
    * PDF 另有最多 50 頁的限制。


## 輸出 details 合約

工具會在 `details` 下回傳結構化中繼資料。

檢視器欄位

建立檢視器的模式所共用的欄位：

  * `artifactId`
  * `viewerUrl`
  * `viewerPath`
  * `title`
  * `expiresAt`
  * `inputKind`
  * `fileCount`
  * `mode`
  * `context`（可用時包含 `agentId`、`sessionId`、`messageChannel`、`agentAccountId`）

檔案欄位

算繪 PNG 或 PDF 時的檔案欄位：

  * `artifactId`
  * `expiresAt`
  * `filePath`
  * `path`（與 `filePath` 相同的值，用於 message 工具相容性）
  * `fileBytes`
  * `fileFormat`
  * `fileQuality`
  * `fileScale`
  * `fileMaxWidth`

相容性別名

也會為既有呼叫端回傳：

  * `format`（與 `fileFormat` 相同的值）
  * `imagePath`（與 `filePath` 相同的值）
  * `imageBytes`（與 `fileBytes` 相同的值）
  * `imageQuality`（與 `fileQuality` 相同的值）
  * `imageScale`（與 `fileScale` 相同的值）
  * `imageMaxWidth`（與 `fileMaxWidth` 相同的值）


模式行為摘要：

模式 | 回傳內容  
---|---  
`"view"` | 僅檢視器欄位。  
`"file"` | 僅檔案欄位，沒有檢視器成品。  
`"both"` | 檢視器欄位加上檔案欄位。如果檔案算繪失敗，檢視器仍會回傳，並帶有 `fileError` 與 `imageError` 別名。  
  
## 已摺疊的未變更區段

  * 檢視器可以顯示如 `N unmodified lines` 的列。
  * 這些列上的展開控制項是有條件的，並不保證每種輸入類型都有。
  * 當已算繪 diff 具有可展開的內容資料時，會出現展開控制項；這通常見於 before and after 輸入。
  * 對於許多統一 patch 輸入，省略的內容主體在已解析的 patch hunk 中不可用，因此該列可能會在沒有展開控制項的情況下出現。這是預期行為。
  * `expandUnchanged` 僅在存在可展開內容時適用。


## Plugin 預設值

在 `~/.openclaw/openclaw.json` 中設定整個 Plugin 的預設值：

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          defaults: {            fontFamily: "Fira Code",            fontSize: 15,            lineSpacing: 1.6,            layout: "unified",            showLineNumbers: true,            diffIndicators: "bars",            wordWrap: true,            background: true,            theme: "dark",            fileFormat: "png",            fileQuality: "standard",            fileScale: 2,            fileMaxWidth: 960,            mode: "both",            ttlSeconds: 21600,          },        },      },    },  },}
[/code]

支援的預設值：

  * `fontFamily`
  * `fontSize`
  * `lineSpacing`
  * `layout`
  * `showLineNumbers`
  * `diffIndicators`
  * `wordWrap`
  * `background`
  * `theme`
  * `fileFormat`
  * `fileQuality`
  * `fileScale`
  * `fileMaxWidth`
  * `mode`
  * `ttlSeconds`


明確的工具參數會覆寫這些預設值。

### 持久化檢視器 URL 設定

當工具呼叫未傳入 `baseUrl` 時，由 Plugin 擁有、用於回傳檢視器連結的備援值。必須是 `http` 或 `https`，不可有查詢/雜湊。

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          viewerBaseUrl: "https://gateway.example.com/openclaw",        },      },    },  },}
[/code]

## 安全性設定

`false`：拒絕對檢視器路由的非 loopback 請求。`true`：如果 token 化路徑有效，允許遠端檢視器。

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          security: {            allowRemoteViewer: false,          },        },      },    },  },}
[/code]

## 成品生命週期與儲存

  * 成品會儲存在暫存子資料夾下：`$TMPDIR/openclaw-diffs`。
  * 檢視器成品中繼資料包含： 
    * 隨機成品 ID（20 個十六進位字元）
    * 隨機 token（48 個十六進位字元）
    * `createdAt` 與 `expiresAt`
    * 已儲存的 `viewer.html` 路徑
  * 未指定時，預設成品 TTL 為 30 分鐘。
  * 接受的最大檢視器 TTL 為 6 小時。
  * 清理會在成品建立後伺機執行。
  * 過期成品會被刪除。
  * 當中繼資料缺失時，備援清理會移除超過 24 小時的陳舊資料夾。


## 檢視器 URL 與網路行為

檢視器路由：

  * `/plugins/diffs/view/{artifactId}/{token}`


檢視器資產：

  * `/plugins/diffs/assets/viewer.js`
  * `/plugins/diffs/assets/viewer-runtime.js`


檢視器文件會相對於檢視器 URL 解析這些資產，因此選用的 `baseUrl` 路徑前綴也會同時保留給兩個資產請求。

URL 建構行為：

  * 如果提供了工具呼叫的 `baseUrl`，會在嚴格驗證後使用它。
  * 否則，如果已設定 Plugin `viewerBaseUrl`，會使用它。
  * 若兩者都沒有覆寫，檢視器 URL 預設為 loopback `127.0.0.1`。
  * 如果 Gateway 繫結模式為 `custom` 且已設定 `gateway.customBindHost`，會使用該主機。


`baseUrl` 規則：

  * 必須是 `http://` 或 `https://`。
  * 會拒絕查詢與雜湊。
  * 允許來源加上選用的基底路徑。


## 安全性模型

檢視器強化

  * 預設僅允許回送。
  * 具權杖的檢視器路徑，並嚴格驗證 ID 與權杖。
  * 檢視器回應 CSP： 
    * `default-src 'none'`
    * 指令碼與資產僅來自自身
    * 不允許外送 `connect-src`
  * 啟用遠端存取時，會對遠端未命中進行節流： 
    * 每 60 秒 40 次失敗
    * 60 秒鎖定（`429 Too Many Requests`）

檔案算繪強化

  * 螢幕截圖瀏覽器請求路由預設拒絕。
  * 僅允許來自 `http://127.0.0.1/plugins/diffs/assets/*` 的本機檢視器資產。
  * 外部網路請求會被封鎖。


## 檔案模式的瀏覽器需求

`mode: "file"` 與 `mode: "both"` 需要 Chromium 相容瀏覽器。

解析順序：

* ### 設定

OpenClaw 設定中的 `browser.executablePath`。

* ### 環境變數

  * `OPENCLAW_BROWSER_EXECUTABLE_PATH`
  * `BROWSER_EXECUTABLE_PATH`
  * `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH`


* ### 平台後援

平台命令／路徑探索後援。

常見失敗文字：

  * `Diff PNG/PDF rendering requires a Chromium-compatible browser...`


修正方式是安裝 Chrome、Chromium、Edge 或 Brave，或設定上述其中一個可執行檔路徑選項。

## 疑難排解

輸入驗證錯誤

  * `Provide patch or both before and after text.` — 同時包含 `before` 與 `after`，或提供 `patch`。
  * `Provide either patch or before/after input, not both.` — 不要混用輸入模式。
  * `Invalid baseUrl: ...` — 使用 `http(s)` 來源，可含選用路徑，但不可含查詢／雜湊。
  * `{field} exceeds maximum size (...)` — 縮減酬載大小。
  * 大型修補檔遭拒 — 減少修補檔案數量或總行數。

檢視器可存取性

  * 檢視器 URL 預設解析為 `127.0.0.1`。
  * 對於遠端存取情境，請擇一： 
    * 設定 Plugin `viewerBaseUrl`，或
    * 在每次工具呼叫傳入 `baseUrl`，或
    * 使用 `gateway.bind=custom` 與 `gateway.customBindHost`
  * 如果 `gateway.trustedProxies` 包含同主機 Proxy 的回送位址（例如 Tailscale Serve），未帶轉送用戶端 IP 標頭的原始回送檢視器請求，會依設計以失敗關閉。
  * 對於該 Proxy 拓撲： 
    * 當你只需要附件時，偏好使用 `mode: "file"` 或 `mode: "both"`，或
    * 當你需要可分享的檢視器 URL 時，明確啟用 `security.allowRemoteViewer`，並設定 Plugin `viewerBaseUrl` 或傳入 Proxy／公開的 `baseUrl`
  * 只有在你確實打算允許外部檢視器存取時，才啟用 `security.allowRemoteViewer`。

未修改行資料列沒有展開按鈕

當修補檔輸入未攜帶可展開的內容脈絡時，可能會發生這種情況。這是預期行為，不代表檢視器失敗。

找不到成品

  * 成品因 TTL 到期。
  * 權杖或路徑已變更。
  * 清理程序移除了過期資料。


## 操作指引

  * 對於畫布中的本機互動式檢閱，偏好使用 `mode: "view"`。
  * 對於需要附件的外送聊天管道，偏好使用 `mode: "file"`。
  * 除非你的部署需要遠端檢視器 URL，否則請保持停用 `allowRemoteViewer`。
  * 針對敏感差異設定明確且短的 `ttlSeconds`。
  * 不需要時，避免在差異輸入中傳送秘密。
  * 如果你的管道會大幅壓縮圖片（例如 Telegram 或 WhatsApp），請偏好 PDF 輸出（`fileFormat: "pdf"`）。


## 相關

  * [瀏覽器](</zh-TW/tools/browser>)
  * [Plugin](</zh-TW/tools/plugin>)
  * [工具總覽](</zh-TW/tools>)


Was this useful?YesNo