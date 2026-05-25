---
title: 目錄
source_url: https://docs.openclaw.ai/zh-TW/cli/directory
scraped_at: 2026-05-25
---

# `openclaw directory`

針對支援目錄查詢的頻道進行查詢（聯絡人/對等端、群組，以及「我」）。

## 常用旗標

  * `--channel <name>`：頻道 ID/別名（設定多個頻道時為必填；只設定一個頻道時會自動使用）
  * `--account <id>`：帳號 ID（預設：頻道預設值）
  * `--json`：輸出 JSON


## 注意事項

  * `directory` 旨在協助你找到可貼到其他命令中的 ID（尤其是 `openclaw message send --target ...`）。
  * 對許多頻道而言，結果是由設定支援（允許清單 / 已設定群組），而不是即時的提供者目錄。
  * 已安裝的頻道 Plugin 仍可省略目錄支援；在這種情況下，命令會回報不支援的目錄操作，而不是重新安裝 Plugin。
  * 預設輸出是以定位字元分隔的 `id`（有時也包含 `name`）；請使用 `--json` 進行指令碼處理。


## 將結果搭配 `message send` 使用

bashCopy code
[code]
    openclaw directory peers list --channel slack --query "U0"openclaw message send --channel slack --target user:U012ABCDEF --message "hello"
[/code]

## ID 格式（依頻道）

  * WhatsApp：`+15551234567`（私訊）、`1234567890-1234567890@g.us`（群組）、`120363123456789@newsletter`（頻道/電子報對外傳送目標）
  * Telegram：`@username` 或數字聊天 ID；群組是數字 ID
  * Slack：`user:U…` 和 `channel:C…`
  * Discord：`user:<id>` 和 `channel:<id>`
  * Matrix（Plugin）：`user:@user:server`、`room:!roomId:server` 或 `#alias:server`
  * Microsoft Teams（Plugin）：`user:<id>` 和 `conversation:<id>`
  * Zalo（Plugin）：使用者 ID（Bot API）
  * Zalo Personal / `zalouser`（Plugin）：來自 `zca` 的對話串 ID（私訊/群組）（`me`、`friend list`、`group list`）


## 自己（「我」）

bashCopy code
[code]
    openclaw directory self --channel zalouser
[/code]

## 對等端（聯絡人/使用者）

bashCopy code
[code]
    openclaw directory peers list --channel zalouseropenclaw directory peers list --channel zalouser --query "name"openclaw directory peers list --channel zalouser --limit 50
[/code]

## 群組

bashCopy code
[code]
    openclaw directory groups list --channel zalouseropenclaw directory groups list --channel zalouser --query "work"openclaw directory groups members --channel zalouser --group-id <id>
[/code]

## 相關

  * [CLI 參考](</zh-TW/cli>)


Was this useful?YesNo