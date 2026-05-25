---
title: Hostinger
source_url: https://docs.openclaw.ai/zh-TW/install/hostinger
scraped_at: 2026-05-25
---

透過 **一鍵式** 受管理部署或 **VPS** 安裝，在 [Hostinger](<https://www.hostinger.com/openclaw>) 上執行持久的 OpenClaw Gateway。

## 先決條件

  * Hostinger 帳戶（[註冊](<https://www.hostinger.com/openclaw>)）
  * 約 5-10 分鐘


## 選項 A：一鍵式 OpenClaw

最快的開始方式。Hostinger 會處理基礎架構、Docker 和自動更新。

* ### 購買並啟動

  1. 從 [Hostinger OpenClaw 頁面](<https://www.hostinger.com/openclaw>) 選擇受管理的 OpenClaw 方案並完成結帳。


* ### 選取訊息通道

選擇一個或多個要連接的通道：

  * **WhatsApp** \-- 掃描設定精靈中顯示的 QR code。
  * **Telegram** \-- 貼上來自 [BotFather](<https://t.me/BotFather>) 的 bot token。


* ### 完成安裝

按一下 **完成** 以部署執行個體。準備就緒後，從 hPanel 中的 **OpenClaw 概觀** 存取 OpenClaw 儀表板。

## 選項 B：VPS 上的 OpenClaw

對你的伺服器擁有更多控制權。Hostinger 會透過 Docker 在你的 VPS 上部署 OpenClaw，而你可以透過 hPanel 中的 **Docker 管理員** 來管理它。

* ### 購買 VPS

  1. 從 [Hostinger OpenClaw 頁面](<https://www.hostinger.com/openclaw>) 選擇 VPS 上的 OpenClaw 方案並完成結帳。


* ### 設定 OpenClaw

VPS 佈建完成後，填寫設定欄位：

  * **Gateway token** \-- 自動產生；儲存起來供稍後使用。
  * **WhatsApp 號碼** \-- 你的號碼，包含國碼（選填）。
  * **Telegram bot token** \-- 來自 [BotFather](<https://t.me/BotFather>)（選填）。
  * **API 金鑰** \-- 只有在結帳期間未選擇即用型 AI 額度時才需要。


* ### 啟動 OpenClaw

按一下 **部署** 。執行後，在 hPanel 中按一下 **開啟** 來開啟 OpenClaw 儀表板。

日誌、重新啟動和更新會直接從 hPanel 中的 Docker 管理員介面管理。若要更新，請在 Docker 管理員中按下 **更新** ，這會拉取最新映像。

## 驗證你的設定

在你連接的通道上傳送「Hi」給你的助理。OpenClaw 會回覆並引導你完成初始偏好設定。

## 疑難排解

**儀表板未載入** \-- 等待幾分鐘，讓容器完成佈建。檢查 hPanel 中的 Docker 管理員日誌。

**Docker 容器持續重新啟動** \-- 開啟 Docker 管理員日誌，尋找設定錯誤（缺少 token、無效的 API 金鑰）。

**Telegram bot 沒有回應** \-- 直接從 Telegram 將你的配對碼訊息作為 OpenClaw 聊天中的訊息傳送，以完成連線。

## 後續步驟

  * [通道](</zh-TW/channels>) \-- 連接 Telegram、WhatsApp、Discord 等更多服務
  * [Gateway 設定](</zh-TW/gateway/configuration>) \-- 所有設定選項


## 相關內容

  * [安裝概觀](</zh-TW/install>)
  * [VPS 託管](</zh-TW/vps>)
  * [DigitalOcean](</zh-TW/install/digitalocean>)


Was this useful?YesNo