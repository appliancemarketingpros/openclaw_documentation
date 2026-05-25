---
title: macOS 上的 Gateway
source_url: https://docs.openclaw.ai/zh-TW/platforms/mac/bundled-gateway
scraped_at: 2026-05-25
---

OpenClaw.app 不再內建 Node/Bun 或 Gateway runtime。macOS app 預期使用**外部** `openclaw` CLI 安裝，不會將 Gateway 作為 子行程啟動，並會管理每位使用者的 launchd 服務，以保持 Gateway 持續執行（或在已有本機 Gateway 執行時連接至該 Gateway）。

## 安裝 CLI（本機模式必要）

Node 24 是 Mac 上的預設 runtime。Node 22 LTS，目前為 `22.16+`，仍可相容運作。接著全域安裝 `openclaw`：

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

macOS app 的 **安裝 CLI** 按鈕會執行 app 內部使用的相同全域安裝流程：它會優先使用 npm，接著是 pnpm，若 bun 是唯一 偵測到的套件管理器，才會使用 bun。Node 仍是建議的 Gateway runtime。

## Launchd（Gateway 作為 LaunchAgent）

標籤：

  * `ai.openclaw.gateway`（或 `ai.openclaw.<profile>`；舊版 `com.openclaw.*` 可能仍會保留）


Plist 位置（每位使用者）：

  * `~/Library/LaunchAgents/ai.openclaw.gateway.plist` （或 `~/Library/LaunchAgents/ai.openclaw.<profile>.plist`）


管理器：

  * macOS app 在本機模式中負責 LaunchAgent 的安裝/更新。
  * CLI 也可以安裝它：`openclaw gateway install`。


行為：

  * 「OpenClaw 啟用」會啟用/停用 LaunchAgent。
  * 結束 app **不會** 停止 gateway（launchd 會讓它保持執行）。
  * 如果 Gateway 已在設定的連接埠上執行，app 會連接至 該 Gateway，而不是啟動新的 Gateway。


記錄：

  * launchd stdout/err：`/tmp/openclaw/openclaw-gateway.log`


## 版本相容性

macOS app 會檢查 gateway 版本是否與自身版本相符。如果兩者 不相容，請更新全域 CLI 以符合 app 版本。

## 冒煙檢查

bashCopy code
[code]
    openclaw --version OPENCLAW_SKIP_CHANNELS=1 \OPENCLAW_SKIP_CANVAS_HOST=1 \openclaw gateway --port 18999 --bind loopback
[/code]

接著：

bashCopy code
[code]
    openclaw gateway call health --url ws://127.0.0.1:18999 --timeout 3000
[/code]

## 相關

  * [macOS app](</zh-TW/platforms/macos>)
  * [Gateway runbook](</zh-TW/gateway>)


Was this useful?YesNo