---
title: Nextcloud Talk
source_url: https://docs.openclaw.ai/zh-TW/channels/nextcloud-talk
scraped_at: 2026-05-25
---

Status：內建 Plugin（Webhook 機器人）。支援直接訊息、聊天室、反應和 Markdown 訊息。

## 內建 Plugin

Nextcloud Talk 在目前的 OpenClaw 版本中作為內建 Plugin 隨附，因此 一般封裝建置不需要另外安裝。

如果你使用的是較舊的建置，或自訂安裝中排除了 Nextcloud Talk， 請直接安裝 npm 套件：

透過 CLI 安裝（npm registry）：

bashCopy code
[code]
    openclaw plugins install @openclaw/nextcloud-talk
[/code]

使用裸套件可跟隨目前的官方發行標籤。只有在需要可重現安裝時， 才釘選精確版本。

本機 checkout（從 git repo 執行時）：

bashCopy code
[code]
    openclaw plugins install ./path/to/local/nextcloud-talk-plugin
[/code]

詳細資訊：[Plugins](</zh-TW/tools/plugin>)

## 快速設定（初學者）

  1. 確認 Nextcloud Talk Plugin 可用。

     * 目前封裝的 OpenClaw 版本已內建。
     * 較舊/自訂安裝可以使用上述命令手動新增。
  2. 在你的 Nextcloud 伺服器上建立機器人：

bashCopy code
[code]./occ talk:bot:install "OpenClaw" "<shared-secret>" "<webhook-url>" --feature webhook --feature response --feature reaction
[/code]

  3. 在目標聊天室設定中啟用機器人。

  4. 設定 OpenClaw：

     * 設定：`channels.nextcloud-talk.baseUrl` \+ `channels.nextcloud-talk.botSecret`
     * 或 env：`NEXTCLOUD_TALK_BOT_SECRET`（僅限預設帳號）

CLI 設定：

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --url https://cloud.example.com \  --token "<shared-secret>"
[/code]

等效的明確欄位：

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --base-url https://cloud.example.com \  --secret "<shared-secret>"
[/code]

檔案支援的 secret：

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --base-url https://cloud.example.com \  --secret-file /path/to/nextcloud-talk-secret
[/code]

  5. 重新啟動 Gateway（或完成設定）。


最小設定：

json5Copy code
[code]
    {  channels: {    "nextcloud-talk": {      enabled: true,      baseUrl: "https://cloud.example.com",      botSecret: "shared-secret",      dmPolicy: "pairing",    },  },}
[/code]

## 注意事項

  * 機器人無法主動發起 DM。使用者必須先傳訊息給機器人。
  * Webhook URL 必須能由 Gateway 存取；如果位於 proxy 後方，請設定 `webhookPublicUrl`。
  * 機器人 API 不支援媒體上傳；媒體會以 URL 傳送。
  * Webhook payload 不會區分 DM 與聊天室；設定 `apiUser` \+ `apiPassword` 以啟用聊天室類型查詢（否則 DM 會被視為聊天室）。


## 存取控制（DM）

  * 預設：`channels.nextcloud-talk.dmPolicy = "pairing"`。未知寄件者會取得配對碼。
  * 透過以下方式核准： 
    * `openclaw pairing list nextcloud-talk`
    * `openclaw pairing approve nextcloud-talk &lt;CODE&gt;`
  * 公開 DM：`channels.nextcloud-talk.dmPolicy="open"` 加上 `channels.nextcloud-talk.allowFrom=["*"]`。
  * `allowFrom` 只會比對 Nextcloud 使用者 ID；顯示名稱會被忽略。


## 聊天室（群組）

  * 預設：`channels.nextcloud-talk.groupPolicy = "allowlist"`（需要提及）。
  * 使用 `channels.nextcloud-talk.rooms` 將聊天室加入 allowlist：

json5Copy code
[code]
    {  channels: {    "nextcloud-talk": {      rooms: {        "room-token": { requireMention: true },      },    },  },}
[/code]

  * 若不允許任何聊天室，請保持 allowlist 為空，或設定 `channels.nextcloud-talk.groupPolicy="disabled"`。


## 功能

功能 | 狀態  
---|---  
直接訊息 | 支援  
聊天室 | 支援  
執行緒 | 不支援  
媒體 | 僅限 URL  
反應 | 支援  
原生命令 | 不支援  
  
## 設定參考（Nextcloud Talk）

完整設定：[Configuration](</zh-TW/gateway/configuration>)

Provider 選項：

  * `channels.nextcloud-talk.enabled`：啟用/停用頻道啟動。
  * `channels.nextcloud-talk.baseUrl`：Nextcloud instance URL。
  * `channels.nextcloud-talk.botSecret`：機器人共用 secret。
  * `channels.nextcloud-talk.botSecretFile`：一般檔案 secret 路徑。Symlink 會被拒絕。
  * `channels.nextcloud-talk.apiUser`：用於聊天室查詢的 API 使用者（DM 偵測）。
  * `channels.nextcloud-talk.apiPassword`：用於聊天室查詢的 API/app 密碼。
  * `channels.nextcloud-talk.apiPasswordFile`：API 密碼檔案路徑。
  * `channels.nextcloud-talk.webhookPort`：Webhook listener port（預設：8788）。
  * `channels.nextcloud-talk.webhookHost`：Webhook host（預設：0.0.0.0）。
  * `channels.nextcloud-talk.webhookPath`：Webhook path（預設：/nextcloud-talk-webhook）。
  * `channels.nextcloud-talk.webhookPublicUrl`：外部可存取的 Webhook URL。
  * `channels.nextcloud-talk.dmPolicy`：`pairing | allowlist | open | disabled`。
  * `channels.nextcloud-talk.allowFrom`：DM allowlist（使用者 ID）。`open` 需要 `"*"`。
  * `channels.nextcloud-talk.groupPolicy`：`allowlist | open | disabled`。
  * `channels.nextcloud-talk.groupAllowFrom`：群組 allowlist（使用者 ID）。
  * `channels.nextcloud-talk.rooms`：每個聊天室的設定和 allowlist。
  * 靜態寄件者存取群組可透過 `accessGroup:<name>` 從 `allowFrom` 和 `groupAllowFrom` 參照。
  * `channels.nextcloud-talk.historyLimit`：群組歷史記錄限制（0 會停用）。
  * `channels.nextcloud-talk.dmHistoryLimit`：DM 歷史記錄限制（0 會停用）。
  * `channels.nextcloud-talk.dms`：每個 DM 的覆寫（historyLimit）。
  * `channels.nextcloud-talk.textChunkLimit`：傳出文字 chunk 大小（字元）。
  * `channels.nextcloud-talk.chunkMode`：`length`（預設）或 `newline`，在依長度分塊前先依空白行（段落邊界）分割。
  * `channels.nextcloud-talk.blockStreaming`：停用此頻道的區塊串流。
  * `channels.nextcloud-talk.blockStreamingCoalesce`：區塊串流合併調校。
  * `channels.nextcloud-talk.mediaMaxMb`：傳入媒體上限（MB）。


## 相關

  * [Channels Overview](</zh-TW/channels>) — 所有支援的頻道
  * [Pairing](</zh-TW/channels/pairing>) — DM 驗證與配對流程
  * [Groups](</zh-TW/channels/groups>) — 群組聊天行為與提及門檻
  * [Channel Routing](</zh-TW/channels/channel-routing>) — 訊息的 session 路由
  * [Security](</zh-TW/gateway/security>) — 存取模型與強化


Was this useful?YesNo