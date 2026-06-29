---
title: Zalo ClawBot
source_url: https://docs.openclaw.ai/zh-TW/channels/zaloclawbot
scraped_at: 2026-06-29
---

ChannelsRegional platforms

OpenClaw 透過目錄列出的外部 `@zalo-platforms/openclaw-zaloclawbot` 外掛連線到 Zalo ClawBot。登入會使用 Zalo Mini App QR code。

## 相容性

外掛版本 | OpenClaw 版本 | npm dist-tag | 狀態  
---|---|---|---  
0.1.x | >=2026.4.10 | `latest` | 啟用中 / Beta  
  
## 先決條件

  * Node.js **> = 22**
  * 必須已安裝 [OpenClaw](<https://docs.openclaw.ai/install>)（可使用 `openclaw` 命令列介面）。
  * 行動裝置上的 Zalo 帳號，用於掃描登入 QR code。


## 使用 onboard 安裝（建議）

執行 OpenClaw onboarding 精靈，並從 channel 選單選擇 **Zalo ClawBot** ：

bashCopy code
[code]
    openclaw onboard
[/code]

精靈會從官方目錄安裝外掛（已驗證完整性），直接在終端機中呈現登入 QR，並在你使用 Zalo app 掃描後完成 channel 設定。不需要額外命令。

## 手動安裝

若要將 channel 新增到已完成 onboard 的閘道，請依照下列步驟：

### 1\. 安裝外掛

bashCopy code
[code]
    openclaw plugins install "@zalo-platforms/openclaw-zaloclawbot@0.1.4"
[/code]

請使用上方顯示的精確釘選版本（它符合官方目錄項目），這樣 OpenClaw 就會在安裝期間根據目錄完整性雜湊驗證套件。

### 2\. 在 config 中啟用外掛

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-zaloclawbot.enabled true
[/code]

### 3\. 產生 QR code 並登入

bashCopy code
[code]
    openclaw channels login --channel openclaw-zaloclawbot
[/code]

使用 Zalo 行動 app 掃描終端機呈現的 QR code，在 Zalo Mini App 內接受使用條款，並授權 session。

### 4\. 重新啟動閘道

bashCopy code
[code]
    openclaw gateway restart
[/code]

* * *

## 運作方式

與標準開發者 Zalo channel 不同，後者需要你註冊自己的 Zalo Official Account (OA) 並貼上靜態開發者憑證；Zalo ClawBot 使用共用的官方基礎設施，作為**綁定擁有者的個人助理** 運作：

  1. **安全 Onboarding：** QR code 會解析到安全的 Zalo Mini App，將在共用官方 OA 下新佈建的私有 bot 直接綁定到你的 Zalo User ID。
  2. **綁定擁有者的隱私：** 依設計，bot 只限與其擁有者通訊。來自其他使用者的訊息會在平台層級被捨棄，使連線保持私密且安全。
  3. **官方 API 路徑：** 外掛使用 Zalo Bot Platform API，而不是 瀏覽器或 web-session 自動化。


## 內部機制

Zalo ClawBot 外掛透過持久的 long-polling message loop 與 Zalo API 通訊。為了維持乾淨且輕量的 runtime：

  * Long-poll 連線使用 `getUpdates` endpoint。
  * 對於本機桌面／終端機閘道執行，網路鉤子預設為停用。
  * 訊息會在 client-side 處理，並直接對應到你的本機 agent runtime。


此外部外掛會在 OpenClaw 狀態目錄下管理 bot 憑證。 請將該目錄視為敏感資料，並納入與其他 OpenClaw 狀態相同的存取控制與 備份政策。

* * *

## 疑難排解

  * **QR 登入逾時：** 基於安全原因，登入 token (`zbsk`) 會在 5 分鐘後過期。如果 QR code 在你掃描前過期，只要重新執行登入命令即可產生新的 QR code。
  * **閘道載入失敗：** 請確保你的 OpenClaw host 版本為 `2026.4.10` 或更高版本。較舊版本不支援外部 npm-plugin 安裝 ledger。


Was this useful?YesNo

Open issue