---
title: WhatsApp Plugin
source_url: https://docs.openclaw.ai/zh-TW/plugins/reference/whatsapp
scraped_at: 2026-05-25
---

# WhatsApp Plugin

新增 WhatsApp 通道介面，用於傳送和接收 OpenClaw 訊息。

## 發行

  * 套件：`@openclaw/whatsapp`
  * 安裝路徑：npm；ClawHub


## 介面

channels: whatsapp

## Windows 安裝注意事項

在 Windows 上，WhatsApp Plugin 在 npm 安裝期間需要 `PATH` 中有 Git，因為它的一個 Baileys/libsignal 相依項是從 git URL 擷取。請安裝 Git for Windows，然後重新啟動 shell 並重新執行安裝：

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

如果 Portable Git 的 `bin` 目錄位於 `PATH` 中，也可以使用。

## 相關文件

  * [whatsapp](</zh-TW/channels/whatsapp>)


Was this useful?YesNo