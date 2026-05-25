---
title: QA 頻道
source_url: https://docs.openclaw.ai/zh-TW/channels/qa-channel
scraped_at: 2026-05-25
---

`qa-channel` 是一個隨附的合成訊息傳輸，用於自動化 OpenClaw QA。它不是生產用途通道；它存在的目的是在保持狀態具決定性且可完整檢查的同時，演練真實傳輸所使用的相同通道 Plugin 邊界。

## 它的作用

  * Slack 類目標語法： 
    * `dm:<user>`
    * `channel:<room>`
    * `group:<room>`
    * `thread:<room>/<thread>`
  * 共用的 `channel:` 和 `group:` 對話會作為群組/通道聊天室回合呈現給代理，因此它們會演練 Discord、Slack、Telegram 和類似傳輸所使用的相同可見回覆與訊息工具路由政策。
  * 以 HTTP 為基礎的合成匯流排，用於注入傳入訊息、擷取傳出逐字稿、建立執行緒、反應、編輯、刪除，以及搜尋/讀取動作。
  * 主機端自我檢查執行器，會將 Markdown 報告寫入 `.artifacts/qa-e2e/`。


## 設定

jsonCopy code
[code]
    {  "channels": {    "qa-channel": {      "baseUrl": "http://127.0.0.1:43123",      "botUserId": "openclaw",      "botDisplayName": "OpenClaw QA",      "allowFrom": ["*"],      "pollTimeoutMs": 1000    }  }}
[/code]

帳戶鍵：

  * `enabled` \- 此帳戶的主要切換開關。
  * `name` \- 選用的顯示標籤。
  * `baseUrl` \- 合成匯流排 URL。
  * `botUserId` \- 目標語法中使用的 Matrix 風格機器人使用者 ID。
  * `botDisplayName` \- 傳出訊息的顯示名稱。
  * `pollTimeoutMs` \- 長輪詢等待視窗。介於 100 到 30000 之間的整數。
  * `allowFrom` \- 傳送者允許清單（使用者 ID 或 `"*"`）。直接訊息與 允許清單群組政策都使用這些合成傳送者 ID。
  * `groupPolicy` \- 共用聊天室政策：`"open"`（預設）、`"allowlist"` 或 `"disabled"`。
  * `groupAllowFrom` \- 選用的共用聊天室傳送者允許清單。當在 `"allowlist"` 下省略時，QA Channel 會退回使用 `allowFrom`。
  * `groups.<room>.requireMention` \- 要求在特定群組/通道聊天室中回覆前 必須提及機器人。`groups."*"` 會設定預設值。
  * `defaultTo` \- 未提供目標時的備用目標。
  * `actions.messages` / `actions.reactions` / `actions.search` / `actions.threads` \- 依動作設定的工具閘控。


最上層的多帳戶鍵：

  * `accounts` \- 以帳戶 ID 為鍵的具名逐帳戶覆寫記錄。
  * `defaultAccount` \- 設定多個帳戶時偏好的帳戶 ID。


## 執行器

主機端自我檢查（會在 `.artifacts/qa-e2e/` 下寫入 Markdown 報告）：

bashCopy code
[code]
    pnpm qa:e2e
[/code]

這會透過 `qa-lab` 路由、啟動儲存庫內的 QA 匯流排、啟動隨附的 `qa-channel` 執行階段切片，並執行具決定性的自我檢查。

以完整儲存庫為基礎的情境套件：

bashCopy code
[code]
    pnpm openclaw qa suite
[/code]

會針對 QA gateway 通道並行執行情境。情境、設定檔和提供者模式請參閱 [QA 概覽](</zh-TW/concepts/qa-e2e-automation>)。

以 Docker 為基礎的 QA 站台（gateway + QA Lab 除錯器 UI 位於同一堆疊中）：

bashCopy code
[code]
    pnpm qa:lab:up
[/code]

建置 QA 站台、啟動以 Docker 為基礎的 gateway + QA Lab 堆疊，並列印 QA Lab URL。之後你可以挑選情境、選擇模型通道、啟動個別執行，並即時觀看結果。QA Lab 除錯器與已出貨的 Control UI 套件是分開的。

## 相關

  * [QA 概覽](</zh-TW/concepts/qa-e2e-automation>) \- 整體堆疊、傳輸配接器、情境撰寫
  * [Matrix QA](</zh-TW/concepts/qa-matrix>) \- 驅動真實通道的即時傳輸執行器範例
  * [配對](</zh-TW/channels/pairing>)
  * [群組](</zh-TW/channels/groups>)
  * [通道概覽](</zh-TW/channels>)


Was this useful?YesNo