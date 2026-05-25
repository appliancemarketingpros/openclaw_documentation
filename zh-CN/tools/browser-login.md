---
title: 浏览器登录
source_url: https://docs.openclaw.ai/zh-CN/tools/browser-login
scraped_at: 2026-05-25
---

## 手动登录（推荐）

当网站要求登录时，请在**主机** 浏览器配置文件（openclaw 浏览器）中**手动登录** 。

不要把你的凭证交给模型。自动登录通常会触发反机器人防护，并可能锁定账户。

返回主浏览器文档：[浏览器](</zh-CN/tools/browser>)。

## 使用哪个 Chrome 配置文件？

OpenClaw 控制一个**专用 Chrome 配置文件** （名为 `openclaw`，橙色调界面）。它与你日常使用的浏览器配置文件相互独立。

对于智能体浏览器工具调用：

  * 默认选择：智能体应使用其隔离的 `openclaw` 浏览器。
  * 仅当现有已登录会话很重要，且用户在电脑前可以点击/批准任何附加提示时，才使用 `profile="user"`。
  * 如果你有多个用户浏览器配置文件，请显式指定配置文件，而不是猜测。


有两种简单访问方式：

  1. **让智能体打开浏览器** ，然后你自己登录。
  2. **通过 CLI 打开** ：

bashCopy code
[code]
    openclaw browser startopenclaw browser open https://x.com
[/code]

如果你有多个配置文件，请传入 `--browser-profile <name>`（默认值为 `openclaw`）。

## X/Twitter：推荐流程

  * **阅读/搜索/帖子串：**使用** 主机**浏览器（手动登录）。
  * **发布更新：**使用** 主机**浏览器（手动登录）。


## 沙箱隔离 + 主机浏览器访问

沙箱隔离的浏览器会话**更可能** 触发机器人检测。对于 X/Twitter（以及其他严格的网站），优先使用**主机** 浏览器。

如果智能体处于沙箱隔离中，浏览器工具默认使用沙箱。要允许控制主机：

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main",        browser: {          allowHostControl: true,        },      },    },  },}
[/code]

然后你自己打开主机浏览器（CLI 调用始终针对主机浏览器运行）：

bashCopy code
[code]
    openclaw browser open https://x.com --browser-profile openclaw
[/code]

设置 `sandbox.browser.allowHostControl: true` 后，智能体的 `browser` 工具调用就可以指向主机。或者，也可以为发布更新的智能体禁用沙箱隔离。

## 相关

  * [浏览器](</zh-CN/tools/browser>)
  * [浏览器 Linux 故障排除](</zh-CN/tools/browser-linux-troubleshooting>)
  * [浏览器 WSL2 故障排除](</zh-CN/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo