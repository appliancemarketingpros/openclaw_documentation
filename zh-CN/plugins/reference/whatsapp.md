---
title: WhatsApp 插件
source_url: https://docs.openclaw.ai/zh-CN/plugins/reference/whatsapp
scraped_at: 2026-05-25
---

# WhatsApp 插件

添加 WhatsApp 渠道界面，用于发送和接收 OpenClaw 消息。

## 分发

  * 包：`@openclaw/whatsapp`
  * 安装路径：npm；ClawHub


## 界面

channels: whatsapp

## Windows 安装注意事项

在 Windows 上，WhatsApp 插件在 npm 安装期间需要 `PATH` 中存在 Git，因为它的一个 Baileys/libsignal 依赖是从 git URL 获取的。安装 Git for Windows，然后重启 shell 并重新运行安装：

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

如果 Portable Git 的 `bin` 目录在 `PATH` 中，也可以使用 Portable Git。

## 相关文档

  * [whatsapp](</zh-CN/channels/whatsapp>)


Was this useful?YesNo