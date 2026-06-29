---
title: Upstash Box
source_url: https://docs.openclaw.ai/zh-CN/install/upstash
scraped_at: 2026-06-29
---

快速开始

在 Upstash Box 上运行持久化的 OpenClaw Gateway 网关，这是一个托管 Linux 环境，支持保活生命周期。

使用 SSH 隧道访问仪表盘。不要将 Gateway 网关端口直接暴露到公共互联网。

## 前提条件

  * Upstash 账号
  * 保活 Upstash Box
  * 本地机器上的 SSH 客户端


## 创建 Box

在 Upstash Console 中创建一个保活 Box。记下 Box ID，例如 `right-flamingo-14486`，以及你的 Box API key。

Upstash 在以下位置维护当前的 OpenClaw Box 演练： [OpenClaw Setup](<https://upstash.com/docs/box/guides/openclaw-setup>)。

## 使用 SSH 隧道连接

将 OpenClaw 仪表盘端口转发到你的本地机器。提示时使用你的 Box API key 作为 SSH 密码：

bashCopy code
[code]
    ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

这些 keepalive 选项可以减少新手引导期间空闲隧道断开。

## 安装 OpenClaw

在 Box 内部：

bashCopy code
[code]
    sudo npm install -g openclaw
[/code]

## 运行新手引导

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

按照提示操作。新手引导完成后，复制仪表盘 URL 和令牌。

## 启动 Gateway 网关

为 Box 网络配置 Gateway 网关，并在后台启动它：

bashCopy code
[code]
    openclaw config set gateway.bind lannohup openclaw gateway > gateway.log 2>&1 &
[/code]

保持 SSH 隧道处于活动状态，在本地打开仪表盘 URL：

textCopy code
[code]
    http://127.0.0.1:18789/#token=<your-token>
[/code]

## 自动重启

将此命令设置为 Box init script，以便 Gateway 网关在 Box 启动时重启：

bashCopy code
[code]
    nohup openclaw gateway > gateway.log 2>&1 &
[/code]

## 故障排除

如果 SSH 在新手引导期间卡住，请使用干净的 SSH 配置和 keepalive 重新连接：

bashCopy code
[code]
    ssh -F /dev/null -o ControlMaster=no -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

这会绕过过期的本地 `~/.ssh/config` 设置，并在网络空闲期间保持隧道处于活动状态。

## 相关内容

  * [远程访问](</zh-CN/gateway/remote>)
  * [Gateway 网关安全](</zh-CN/gateway/security>)
  * [更新 OpenClaw](</zh-CN/install/updating>)


Was this useful?YesNo

Open issue