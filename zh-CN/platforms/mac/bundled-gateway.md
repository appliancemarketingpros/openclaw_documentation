---
title: macOS 上的 Gateway 网关
source_url: https://docs.openclaw.ai/zh-CN/platforms/mac/bundled-gateway
scraped_at: 2026-05-25
---

OpenClaw.app 不再内置 Node/Bun 或 Gateway 网关运行时。macOS 应用需要**外部** `openclaw` CLI 安装，不会将 Gateway 网关作为子进程启动，并会管理每用户的 launchd 服务来保持 Gateway 网关运行（如果已有本地 Gateway 网关正在运行，则附加到现有 Gateway 网关）。

## 安装 CLI（本地模式必需）

Node 24 是 Mac 上的默认运行时。Node 22 LTS（当前为 `22.16+`）仍可用于兼容。然后全局安装 `openclaw`：

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

macOS 应用中的**安装 CLI** 按钮会运行与应用内部使用相同的全局安装流程：它优先使用 npm，其次是 pnpm，如果 bun 是唯一检测到的包管理器，则使用 bun。Node 仍是推荐的 Gateway 网关运行时。

## Launchd（作为 LaunchAgent 的 Gateway 网关）

标签：

  * `ai.openclaw.gateway`（或 `ai.openclaw.<profile>`；旧版 `com.openclaw.*` 可能仍会保留）


Plist 位置（每用户）：

  * `~/Library/LaunchAgents/ai.openclaw.gateway.plist` （或 `~/Library/LaunchAgents/ai.openclaw.<profile>.plist`）


管理器：

  * macOS 应用在本地模式下负责 LaunchAgent 的安装/更新。
  * CLI 也可以安装它：`openclaw gateway install`。


行为：

  * “OpenClaw 已启用”会启用/停用 LaunchAgent。
  * 退出应用**不会** 停止 Gateway 网关（launchd 会保持其存活）。
  * 如果 Gateway 网关已在配置的端口上运行，应用会附加到它，而不是启动新的 Gateway 网关。


日志：

  * launchd stdout/err：`/tmp/openclaw/openclaw-gateway.log`


## 版本兼容性

macOS 应用会检查 Gateway 网关版本是否与自身版本匹配。如果二者不兼容，请更新全局 CLI，使其与应用版本一致。

## 冒烟检查

bashCopy code
[code]
    openclaw --version OPENCLAW_SKIP_CHANNELS=1 \OPENCLAW_SKIP_CANVAS_HOST=1 \openclaw gateway --port 18999 --bind loopback
[/code]

然后：

bashCopy code
[code]
    openclaw gateway call health --url ws://127.0.0.1:18999 --timeout 3000
[/code]

## 相关内容

  * [macOS 应用](</zh-CN/platforms/macos>)
  * [Gateway 网关运行手册](</zh-CN/gateway>)


Was this useful?YesNo