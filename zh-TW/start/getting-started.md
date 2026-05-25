---
title: 開始使用
source_url: https://docs.openclaw.ai/zh-TW/start/getting-started
scraped_at: 2026-05-25
---

安裝 OpenClaw、執行入門設定，並與你的 AI 助理聊天，全程約 5 分鐘。完成後，你將擁有執行中的 Gateway、已設定的驗證，以及可用的聊天工作階段。

## 你需要準備

  * **Node.js** — 建議使用 Node 24（也支援 Node 22.16+）
  * **模型供應商的 API 金鑰** （Anthropic、OpenAI、Google 等）— 入門設定會提示你輸入


## 快速設定

* ### 安裝 OpenClaw

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![安裝腳本流程](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### 執行入門設定

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

精靈會引導你選擇模型供應商、設定 API 金鑰，並設定 Gateway。大約需要 2 分鐘。

如需完整參考，請參閱[入門設定（CLI）](</zh-TW/start/wizard>)。

* ### 確認 Gateway 正在執行

bashCopy code
[code]
    openclaw gateway status
[/code]

你應該會看到 Gateway 正在連接埠 18789 上監聽。

* ### 開啟儀表板

bashCopy code
[code]
    openclaw dashboard
[/code]

這會在瀏覽器中開啟 Control UI。如果能載入，就表示一切正常。

* ### 傳送你的第一則訊息

在 Control UI 聊天中輸入訊息，你應該會收到 AI 回覆。

想改用手機聊天嗎？最快設定的頻道是 [Telegram](</zh-TW/channels/telegram>)（只需要一個機器人權杖）。所有選項請參閱[頻道](</zh-TW/channels>)。

進階：掛載自訂 Control UI 建置

如果你維護在地化或自訂的儀表板建置，請將 `gateway.controlUi.root` 指向包含已建置靜態 資產與 `index.html` 的目錄。

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

接著設定：

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

重新啟動 Gateway 並重新開啟儀表板：

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## 接下來做什麼

[**連接頻道** Discord、Feishu、iMessage、Matrix、Microsoft Teams、Signal、Slack、Telegram、WhatsApp、Zalo，以及更多。 ](</zh-TW/channels>) [**配對與安全性** 控制誰可以傳訊息給你的代理。 ](</zh-TW/channels/pairing>) [**設定 Gateway** 模型、工具、沙盒與進階設定。 ](</zh-TW/gateway/configuration>) [**瀏覽工具** 瀏覽器、exec、網頁搜尋、Skills 與 Plugins。 ](</zh-TW/tools>)

進階：環境變數

如果你以服務帳號執行 OpenClaw，或想使用自訂路徑：

  * `OPENCLAW_HOME` — 內部路徑解析的主目錄
  * `OPENCLAW_STATE_DIR` — 覆寫狀態目錄
  * `OPENCLAW_CONFIG_PATH` — 覆寫設定檔路徑


完整參考：[環境變數](</zh-TW/help/environment>)。

## 相關內容

  * [安裝概覽](</zh-TW/install>)
  * [頻道概覽](</zh-TW/channels>)
  * [設定](</zh-TW/start/setup>)


Was this useful?YesNo