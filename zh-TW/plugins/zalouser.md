---
title: Zalo 個人 Plugin
source_url: https://docs.openclaw.ai/zh-TW/plugins/zalouser
scraped_at: 2026-05-25
---

透過 Plugin 為 OpenClaw 提供 Zalo Personal 支援，使用原生 `zca-js` 自動化一般 Zalo 使用者帳戶。

## 命名

通道 ID 是 `zalouser`，以明確表示這會自動化 **個人 Zalo 使用者帳戶** （非官方）。我們保留 `zalo` 供未來可能的官方 Zalo API 整合使用。

## 執行位置

此 Plugin 在 **Gateway 程序內部** 執行。

如果你使用遠端 Gateway，請在 **執行 Gateway 的機器** 上安裝/設定它，然後重新啟動 Gateway。

不需要外部 `zca`/`openzca` CLI 二進位檔。

## 安裝

### 選項 A：從 npm 安裝

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

使用裸套件可跟隨目前的官方發行標籤。只有在需要可重現安裝時，才釘選確切版本。

之後重新啟動 Gateway。

### 選項 B：從本機資料夾安裝（開發）

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

之後重新啟動 Gateway。

## 設定

通道設定位於 `channels.zalouser` 之下（不是 `plugins.entries.*`）：

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## Agent 工具

工具名稱：`zalouser`

動作：`send`、`image`、`link`、`friends`、`groups`、`me`、`status`

通道訊息動作也支援 `react`，用於訊息反應。

## 相關內容

  * [建置 Plugin](</zh-TW/plugins/building-plugins>)
  * [ClawHub](</zh-TW/clawhub>)


Was this useful?YesNo