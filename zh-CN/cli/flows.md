---
title: 流程（重定向）
source_url: https://docs.openclaw.ai/zh-CN/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

没有顶层的 `openclaw flows` 命令。持久化 TaskFlow 检查位于 `openclaw tasks flow` 下。

## 子命令

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

子命令 | 说明 | 参数 / 选项  
---|---|---  
`list` | 列出已跟踪的 TaskFlow。 | `--json` 机器可读输出；`--status <name>` 过滤器（见下方状态值）。  
`show` | 显示一个 TaskFlow。 | `<lookup>` flow id 或 owner key；`--json` 机器可读输出。  
`cancel` | 取消正在运行的 TaskFlow。 | `<lookup>` flow id 或 owner key。  
  
`<lookup>` 接受 flow id（由 `list` / `show` 返回）或该 flow 的 owner key（所属子系统用来跟踪该 flow 的稳定标识符）。

### 状态过滤器值

`list` 上的 `--status` 接受以下值之一：

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## 示例

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

完整的 TaskFlow 概念和编写说明见 [TaskFlow](</zh-CN/automation/taskflow>)。父级 `tasks` 命令见 [tasks CLI 参考](</zh-CN/cli/tasks>)。

## 相关

  * [CLI 参考](</zh-CN/cli>)
  * [自动化](</zh-CN/automation>)
  * [TaskFlow](</zh-CN/automation/taskflow>)


Was this useful?YesNo