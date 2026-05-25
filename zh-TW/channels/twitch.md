---
title: Twitch
source_url: https://docs.openclaw.ai/zh-TW/channels/twitch
scraped_at: 2026-05-25
---

Twitch 透過 IRC 連線支援聊天。OpenClaw 會以 Twitch 使用者（機器人帳號）身分連線，以便在頻道中接收與傳送訊息。

## 內建 Plugin

如果你使用較舊的建置，或是排除 Twitch 的自訂安裝，請直接安裝 npm 套件：

### npm registry

bashCopy code
[code]
    openclaw plugins install @openclaw/twitch
[/code]

### 本機 checkout

bashCopy code
[code]
    openclaw plugins install ./path/to/local/twitch-plugin
[/code]

使用裸套件以跟隨目前的官方發行標籤。只有在需要可重現安裝時，才釘選精確版本。

詳情：[Plugins](</zh-TW/tools/plugin>)

## 快速設定（初學者）

* ### 確認 Plugin 可用

目前封裝的 OpenClaw 版本已經內建它。較舊或自訂安裝可使用上述命令手動加入。

* ### 建立 Twitch 機器人帳號

為機器人建立專用 Twitch 帳號（或使用現有帳號）。

* ### 產生憑證

使用 [Twitch Token Generator](<https://twitchtokengenerator.com/>)：

  * 選取 **Bot Token**
  * 確認已選取範圍 `chat:read` 和 `chat:write`
  * 複製 **Client ID** 和 **Access Token**


* ### 尋找你的 Twitch 使用者 ID

使用 <https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/> 將使用者名稱轉換為 Twitch 使用者 ID。

* ### 設定權杖

  * 環境變數：`OPENCLAW_TWITCH_ACCESS_TOKEN=...`（僅限預設帳號）
  * 或設定：`channels.twitch.accessToken`


如果兩者皆已設定，設定檔優先（環境變數備援僅適用於預設帳號）。

* ### 啟動 Gateway

使用已設定的頻道啟動 Gateway。

最小設定：

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw", // Bot's Twitch account      accessToken: "oauth:abc123...", // OAuth Access Token (or use OPENCLAW_TWITCH_ACCESS_TOKEN env var)      clientId: "xyz789...", // Client ID from Token Generator      channel: "vevisk", // Which Twitch channel's chat to join (required)      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only - get it from https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/    },  },}
[/code]

## 它是什麼

  * 由 Gateway 擁有的 Twitch 頻道。
  * 確定性路由：回覆一律回到 Twitch。
  * 每個帳號會對應到隔離的工作階段金鑰 `agent:<agentId>:twitch:<accountName>`。
  * `username` 是機器人的帳號（用於驗證），`channel` 是要加入的聊天室。


## 設定（詳細）

### 產生憑證

使用 [Twitch Token Generator](<https://twitchtokengenerator.com/>)：

  * 選取 **Bot Token**
  * 確認已選取範圍 `chat:read` 和 `chat:write`
  * 複製 **Client ID** 和 **Access Token**


### 設定機器人

### 環境變數（僅限預設帳號）

bashCopy code
[code]
    OPENCLAW_TWITCH_ACCESS_TOKEN=oauth:abc123...
[/code]

### 設定

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",    },  },}
[/code]

如果環境變數和設定皆已設定，設定檔優先。

### 存取控制（建議）

json5Copy code
[code]
    {  channels: {    twitch: {      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only    },  },}
[/code]

偏好使用 `allowFrom` 作為硬性允許清單。如果你想要以角色為基礎的存取，請改用 `allowedRoles`。

**可用角色：** `"moderator"`、`"owner"`、`"vip"`、`"subscriber"`、`"all"`。

## 權杖重新整理（選用）

來自 [Twitch Token Generator](<https://twitchtokengenerator.com/>) 的權杖無法自動重新整理，過期時請重新產生。

若要自動重新整理權杖，請在 [Twitch Developer Console](<https://dev.twitch.tv/console>) 建立你自己的 Twitch 應用程式，並加入設定：

json5Copy code
[code]
    {  channels: {    twitch: {      clientSecret: "your_client_secret",      refreshToken: "your_refresh_token",    },  },}
[/code]

機器人會在過期前自動重新整理權杖，並記錄重新整理事件。

## 多帳號支援

使用 `channels.twitch.accounts` 搭配各帳號專屬權杖。共享模式請參閱[設定](</zh-TW/gateway/configuration>)。

範例（一個機器人帳號在兩個頻道中）：

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        channel1: {          username: "openclaw",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "vevisk",        },        channel2: {          username: "openclaw",          accessToken: "oauth:def456...",          clientId: "uvw012...",          channel: "secondchannel",        },      },    },  },}
[/code]

## 存取控制

### 使用者 ID 允許清單（最安全）

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowFrom: ["123456789", "987654321"],        },      },    },  },}
[/code]

### 以角色為基礎

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowedRoles: ["moderator", "vip"],        },      },    },  },}
[/code]

`allowFrom` 是硬性允許清單。設定後，只允許這些使用者 ID。如果你想要以角色為基礎的存取，請不要設定 `allowFrom`，改為設定 `allowedRoles`。

### 停用 @mention 要求

預設情況下，`requireMention` 為 `true`。若要停用並回應所有訊息：

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          requireMention: false,        },      },    },  },}
[/code]

## 疑難排解

首先，執行診斷命令：

bashCopy code
[code]
    openclaw doctoropenclaw channels status --probe
[/code]

機器人未回應訊息

  * **檢查存取控制：** 確認你的使用者 ID 位於 `allowFrom` 中，或暫時移除 `allowFrom` 並設定 `allowedRoles: ["all"]` 來測試。
  * **檢查機器人是否在頻道中：** 機器人必須加入 `channel` 中指定的頻道。

權杖問題

「連線失敗」或驗證錯誤：

  * 確認 `accessToken` 是 OAuth 存取權杖值（通常以 `oauth:` 前綴開頭）
  * 檢查權杖是否具有 `chat:read` 和 `chat:write` 範圍
  * 如果使用權杖重新整理，請確認已設定 `clientSecret` 和 `refreshToken`

權杖重新整理無法運作

檢查記錄中的重新整理事件：

CodeCopy code
[code]
    Using env token source for mybotAccess token refreshed for user 123456 (expires in 14400s)
[/code]

如果你看到「token refresh disabled (no refresh token)」：

  * 確認已提供 `clientSecret`
  * 確認已提供 `refreshToken`


## 設定

### 帳號設定

機器人使用者名稱。

具有 `chat:read` 和 `chat:write` 的 OAuth 存取權杖。

Twitch Client ID（來自 Token Generator 或你的應用程式）。

要加入的頻道。

啟用此帳號。

選用：用於自動權杖重新整理。

選用：用於自動權杖重新整理。

權杖有效期限，以秒為單位。

權杖取得時間戳記。

使用者 ID 允許清單。

要求 @mention。

### 提供者選項

  * `channels.twitch.enabled` \- 啟用/停用頻道啟動
  * `channels.twitch.username` \- 機器人使用者名稱（簡化的單帳號設定）
  * `channels.twitch.accessToken` \- OAuth 存取權杖（簡化的單帳號設定）
  * `channels.twitch.clientId` \- Twitch Client ID（簡化的單帳號設定）
  * `channels.twitch.channel` \- 要加入的頻道（簡化的單帳號設定）
  * `channels.twitch.accounts.<accountName>` \- 多帳號設定（上述所有帳號欄位）


完整範例：

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",      clientSecret: "secret123...",      refreshToken: "refresh456...",      allowFrom: ["123456789"],      allowedRoles: ["moderator", "vip"],      accounts: {        default: {          username: "mybot",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "your_channel",          enabled: true,          clientSecret: "secret123...",          refreshToken: "refresh456...",          expiresIn: 14400,          obtainmentTimestamp: 1706092800000,          allowFrom: ["123456789", "987654321"],          allowedRoles: ["moderator"],        },      },    },  },}
[/code]

## 工具動作

代理可以使用下列動作呼叫 `twitch`：

  * `send` \- 將訊息傳送到頻道


範例：

json5Copy code
[code]
    {  action: "twitch",  params: {    message: "Hello Twitch!",    to: "#mychannel",  },}
[/code]

## 安全與維運

  * **將權杖視為密碼** — 絕不要將權杖提交到 git。
  * **使用自動權杖重新整理** 供長時間執行的機器人使用。
  * **使用使用者 ID 允許清單** ，而非使用者名稱，來進行存取控制。
  * **監控記錄** 以查看權杖重新整理事件與連線狀態。
  * **最小化權杖範圍** — 只要求 `chat:read` 和 `chat:write`。
  * **如果卡住** ：確認沒有其他處理程序擁有該工作階段後，重新啟動 Gateway。


## 限制

  * 每則訊息 **500 個字元** （會在字詞邊界自動分段）。
  * Markdown 會在分段前移除。
  * 無速率限制（使用 Twitch 內建的速率限制）。


## 相關

  * [頻道路由](</zh-TW/channels/channel-routing>) — 訊息的工作階段路由
  * [頻道概觀](</zh-TW/channels>) — 所有支援的頻道
  * [群組](</zh-TW/channels/groups>) — 群組聊天行為與提及閘控
  * [配對](</zh-TW/channels/pairing>) — DM 驗證與配對流程
  * [安全性](</zh-TW/gateway/security>) — 存取模型與強化


Was this useful?YesNo