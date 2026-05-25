---
title: 目录
source_url: https://docs.openclaw.ai/zh-CN/cli/directory
scraped_at: 2026-05-25
---

# `openclaw directory`

用于支持目录查找的渠道（联系人/对等方、群组和 `"me"`）的目录查找。

## 常用标志

  * `--channel <name>`：渠道 ID/别名（配置了多个渠道时必需；仅配置一个渠道时自动使用）
  * `--account <id>`：账户 ID（默认：渠道默认值）
  * `--json`：输出 JSON


## 说明

  * `directory` 旨在帮助你找到可粘贴到其他命令中的 ID（尤其是 `openclaw message send --target ...`）。
  * 对许多渠道来说，结果由配置支持（允许列表/已配置群组），而不是来自实时提供商目录。
  * 已安装的渠道插件仍可省略目录支持；在这种情况下，命令会报告不支持的目录操作，而不是重新安装插件。
  * 默认输出为 `id`（有时还有 `name`），用制表符分隔；脚本使用请加 `--json`。


## 将结果用于 `message send`

bashCopy code
[code]
    openclaw directory peers list --channel slack --query "U0"openclaw message send --channel slack --target user:U012ABCDEF --message "hello"
[/code]

## ID 格式（按渠道）

  * WhatsApp：`+15551234567`（私信）、`1234567890-1234567890@g.us`（群组）、`120363123456789@newsletter`（频道/Newsletter 出站目标）
  * Telegram：`@username` 或数字聊天 ID；群组是数字 ID
  * Slack：`user:U…` 和 `channel:C…`
  * Discord：`user:<id>` 和 `channel:<id>`
  * Matrix（插件）：`user:@user:server`、`room:!roomId:server` 或 `#alias:server`
  * Microsoft Teams（插件）：`user:<id>` 和 `conversation:<id>`
  * Zalo（插件）：用户 ID（Bot API）
  * Zalo Personal / `zalouser`（插件）：来自 `zca`（`me`、`friend list`、`group list`）的线程 ID（私信/群组）


## 自己（"me"）

bashCopy code
[code]
    openclaw directory self --channel zalouser
[/code]

## 对等方（联系人/用户）

bashCopy code
[code]
    openclaw directory peers list --channel zalouseropenclaw directory peers list --channel zalouser --query "name"openclaw directory peers list --channel zalouser --limit 50
[/code]

## 群组

bashCopy code
[code]
    openclaw directory groups list --channel zalouseropenclaw directory groups list --channel zalouser --query "work"openclaw directory groups members --channel zalouser --group-id <id>
[/code]

## 相关

  * [CLI 参考](</zh-CN/cli>)


Was this useful?YesNo