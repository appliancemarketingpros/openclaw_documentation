---
title: Zalo 个人插件
source_url: https://docs.openclaw.ai/zh-CN/plugins/zalouser
scraped_at: 2026-05-25
---

通过插件为 OpenClaw 提供 Zalo Personal 支持，使用原生 `zca-js` 自动化普通 Zalo 用户账号。

## 命名

渠道 ID 是 `zalouser`，用于明确表示这会自动化一个**个人 Zalo 用户账号** （非官方）。我们保留 `zalo`，以备未来可能的官方 Zalo API 集成使用。

## 运行位置

此插件在 **Gateway 网关进程内部** 运行。

如果你使用远程 Gateway 网关，请在**运行 Gateway 网关的机器** 上安装/配置它，然后重启 Gateway 网关。

不需要外部 `zca`/`openzca` CLI 二进制文件。

## 安装

### 选项 A：从 npm 安装

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

使用裸包名可跟随当前官方发布标签。仅在你需要可复现安装时，才固定精确版本。

之后重启 Gateway 网关。

### 选项 B：从本地文件夹安装（开发）

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

之后重启 Gateway 网关。

## 配置

渠道配置位于 `channels.zalouser` 下（不是 `plugins.entries.*`）：

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

工具名称：`zalouser`

操作：`send`、`image`、`link`、`friends`、`groups`、`me`、`status`

渠道消息操作还支持用于消息回应的 `react`。

## 相关内容

  * [构建插件](</zh-CN/plugins/building-plugins>)
  * [ClawHub](</zh-CN/clawhub>)


Was this useful?YesNo