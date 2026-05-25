---
title: Northflank
source_url: https://docs.openclaw.ai/zh-TW/install/northflank
scraped_at: 2026-05-25
---

# Northflank

使用一鍵式範本在 Northflank 上部署 OpenClaw，並透過網頁版控制 UI 存取。 這是最簡單的「伺服器上無需終端機」路徑：Northflank 會為你執行 Gateway。

## 如何開始

  1. 點選[部署 OpenClaw](<https://northflank.com/stacks/deploy-openclaw>) 以開啟範本。
  2. 如果你還沒有 Northflank 帳號，請建立一個 [Northflank 帳號](<https://app.northflank.com/signup>)。
  3. 點選 **Deploy OpenClaw now** 。
  4. 設定必要的環境變數：`OPENCLAW_GATEWAY_TOKEN`（使用強隨機值）。
  5. 點選 **Deploy stack** 以建置並執行 OpenClaw 範本。
  6. 等待部署完成，然後點選 **View resources** 。
  7. 開啟 OpenClaw 服務。
  8. 在 `/openclaw` 開啟公開的 OpenClaw URL，並使用已設定的共享密鑰連線。此範本預設使用 `OPENCLAW_GATEWAY_TOKEN`；如果你將它替換為密碼驗證，請改用該密碼。


## 你會取得的內容

  * 託管式 OpenClaw Gateway + 控制 UI
  * 透過 Northflank Volume (`/data`) 提供持久化儲存空間，讓 `openclaw.json`、 每個代理程式的 `auth-profiles.json`、頻道/提供者狀態、工作階段和 工作區在重新部署後仍能保留


## 連接頻道

使用 `/openclaw` 的控制 UI，或透過 SSH 執行 `openclaw onboard` 取得頻道設定說明：

  * [Telegram](</zh-TW/channels/telegram>)（最快，只需要機器人權杖）
  * [Discord](</zh-TW/channels/discord>)
  * [所有頻道](</zh-TW/channels>)


## 下一步

  * 設定訊息頻道：[頻道](</zh-TW/channels>)
  * 設定 Gateway：[Gateway 設定](</zh-TW/gateway/configuration>)
  * 讓 OpenClaw 保持最新：[更新](</zh-TW/install/updating>)


Was this useful?YesNo