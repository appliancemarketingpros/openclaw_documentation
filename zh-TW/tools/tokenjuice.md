---
title: Tokenjuice
source_url: https://docs.openclaw.ai/zh-TW/tools/tokenjuice
scraped_at: 2026-05-25
---

`tokenjuice` 是選用的內建 Plugin，會在命令已經執行後，壓縮雜訊較多的 `exec` 與 `bash` 工具結果。

它變更的是回傳的 `tool_result`，不是命令本身。Tokenjuice 不會 重寫 shell 輸入、重新執行命令，或變更退出代碼。

目前這適用於 Codex app-server harness 中的 PI embedded runs 和 OpenClaw dynamic tools。Tokenjuice 會掛接 OpenClaw 的 tool-result middleware，並在輸出回到 active harness session 之前 修剪輸出。

## 啟用 Plugin

快速方式：

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled true
[/code]

等效方式：

bashCopy code
[code]
    openclaw plugins enable tokenjuice
[/code]

OpenClaw 已經隨附此 Plugin。不需要另外執行 `plugins install` 或 `tokenjuice install openclaw` 步驟。

如果你偏好直接編輯設定：

json5Copy code
[code]
    {  plugins: {    entries: {      tokenjuice: {        enabled: true,      },    },  },}
[/code]

## tokenjuice 會變更什麼

  * 在雜訊較多的 `exec` 與 `bash` 結果被送回 session 之前壓縮它們。
  * 保持原始命令執行不變。
  * 保留精確的檔案內容讀取，以及其他 tokenjuice 應保持原始輸出的命令。
  * 維持選擇性啟用：如果你想在所有地方取得逐字輸出，請停用此 Plugin。


## 驗證它正在運作

  1. 啟用 Plugin。
  2. 啟動可以呼叫 `exec` 的 session。
  3. 執行雜訊較多的命令，例如 `git status`。
  4. 檢查回傳的工具結果是否比原始 shell 輸出更短且更有結構。


## 停用 Plugin

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled false
[/code]

或：

bashCopy code
[code]
    openclaw plugins disable tokenjuice
[/code]

## 相關內容

  * [Exec 工具](</zh-TW/tools/exec>)
  * [Thinking levels](</zh-TW/tools/thinking>)
  * [Context engine](</zh-TW/concepts/context-engine>)


Was this useful?YesNo