---
title: 入門設定（macOS 應用程式）
source_url: https://docs.openclaw.ai/zh-TW/start/onboarding
scraped_at: 2026-05-25
---

這份文件描述**目前** 的首次執行設定流程。目標是提供順暢的「第 0 天」體驗：選擇 Gateway 的執行位置、連接驗證、執行精靈，並讓代理自行啟動。 如需 onboarding 路徑的一般概覽，請參閱 [Onboarding 概覽](</zh-TW/start/onboarding-overview>)。

* ### 核准 macOS 警告

![](/assets/macos-onboarding/01-macos-warning.jpeg)
* ### 核准尋找本機網路

![](/assets/macos-onboarding/02-local-networks.jpeg)
* ### 歡迎與安全性通知

閱讀顯示的安全性通知，並據此決定 ![](/assets/macos-onboarding/03-security-notice.png)

安全性信任模型：

  * 預設情況下，OpenClaw 是個人代理：單一受信任操作員邊界。
  * 共享/多使用者設定需要鎖定（拆分信任邊界、盡量縮小工具存取權限，並遵循 [安全性](</zh-TW/gateway/security>)）。
  * 本機 onboarding 現在會將新設定預設為 `tools.profile: "coding"`，因此全新的本機設定能保留檔案系統/執行階段工具，而不會強制使用不受限制的 `full` 設定檔。
  * 如果啟用了 hooks/webhooks 或其他不受信任的內容來源，請使用強大的現代模型層級，並維持嚴格的工具政策/沙箱。


* ### 本機與遠端

![](/assets/macos-onboarding/04-choose-gateway.png)

**Gateway** 在哪裡執行？

  * **這台 Mac（僅限本機）：** onboarding 可以設定驗證並在本機寫入憑證。
  * **遠端（透過 SSH/Tailnet）：** onboarding **不會** 設定本機驗證；憑證必須存在於 Gateway 主機上。
  * **稍後設定：** 跳過設定，讓應用程式保持未設定狀態。


* ### 權限

選擇你想授予 OpenClaw 的權限 ![](/assets/macos-onboarding/05-permissions.png)

Onboarding 會要求下列用途所需的 TCC 權限：

  * 自動化（AppleScript）
  * 通知
  * 輔助使用
  * 螢幕錄製
  * 麥克風
  * 語音辨識
  * 相機
  * 位置


* ### CLI

* ### Onboarding 聊天（專用工作階段）

設定完成後，應用程式會開啟專用的 onboarding 聊天工作階段，讓代理能夠 自我介紹並引導後續步驟。這會將首次執行引導與你的正常對話分開。 如需了解首次代理執行期間 Gateway 主機上會發生什麼，請參閱 [啟動](</zh-TW/start/bootstrapping>)。

## 相關

  * [Onboarding 概覽](</zh-TW/start/onboarding-overview>)
  * [開始使用](</zh-TW/start/getting-started>)


Was this useful?YesNo