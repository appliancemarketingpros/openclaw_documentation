---
title: 屏幕
source_url: https://docs.openclaw.ai/zh-CN/tools/screen
scraped_at: 2026-10-12
---

工具内置工具

`screen` 工具可让智能体编排基于浏览器的 Control UI。它是一个 类型化的布局和导航界面，并非用于截取屏幕截图或进行浏览器 自动化。

仅当发起请求的客户端声明 `ui-commands` 能力时，才会提供该工具。 工具运行时，必须仍有至少一个具备此能力的 Control UI 保持连接； 否则，Gateway 网关将返回 `UNAVAILABLE`。

## 操作

操作 | 效果 | 可选输入  
---|---|---  
`split_right` | 将目标会话窗格向右拆分 | `sessionKey`（默认为当前会话）  
`split_down` | 将目标会话窗格向下拆分 | `sessionKey`（默认为当前会话）  
`close_pane` | 关闭目标会话窗格 | `sessionKey`（默认为当前会话）  
`focus` | 聚焦目标会话窗格 | `sessionKey`（默认为当前会话）  
`navigate` | 打开目标会话 | `sessionKey`（默认为当前会话）  
`sidebar_show` / `sidebar_hide` | 显示或隐藏主侧边栏 | -  
`terminal_show` / `terminal_hide` | 显示或隐藏操作员终端面板 | 显示时使用 `dock`（`bottom` 或 `right`）  
`browser_show` / `browser_hide` | 显示或隐藏浏览器面板 | 显示时使用 `dock`（`bottom` 或 `right`）  
  
命令成功执行后，Gateway 网关会广播类型化的 `ui.command` 事件， 随后返回 `{ "ok": true }`。

## 路由与安全

协议 v1 有意将命令发送给每个已连接且声明 `ui-commands` 的 Control UI；它不会以某个浏览器标签页为目标。当同一 操作员打开了多个仪表板时，这一点很重要。

Gateway 网关 RPC 要求 `operator.write`。该工具只能更改呈现 状态：它无法读取像素、截取屏幕截图、点击任意页面 内容，也无法绕过所选会话和操作员 面板的权限。

## 相关内容

  * [Control UI](</web/control-ui>)
  * [Gateway 协议](</zh-CN/gateway/protocol#method-families>)
  * [浏览器工具](</zh-CN/tools/browser>)


Was this useful?YesNo

Open issue