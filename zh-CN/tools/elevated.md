---
title: 提升权限模式
source_url: https://docs.openclaw.ai/zh-CN/tools/elevated
scraped_at: 2026-05-25
---

当智能体在沙箱内运行时，它的 `exec` 命令会被限制在沙箱环境中。**提升模式** 允许智能体改为跳出沙箱，在沙箱外运行命令，并带有可配置的审批门禁。

## 指令

使用斜杠命令按会话控制提升模式：

指令 | 作用  
---|---  
`/elevated on` | 在配置的主机路径上于沙箱外运行，保留审批  
`/elevated ask` | 与 `on` 相同（别名）  
`/elevated full` | 在配置的主机路径上于沙箱外运行，并跳过审批  
`/elevated off` | 返回到受沙箱限制的执行  
  
也可以使用 `/elev on|off|ask|full`。

发送不带参数的 `/elevated` 可查看当前级别。

## 工作原理

* ### 检查可用性

必须在配置中启用提升模式，并且发送者必须在允许列表中：

json5Copy code
[code]
    {  tools: {    elevated: {      enabled: true,      allowFrom: {        discord: ["user-id-123"],        whatsapp: ["+15555550123"],      },    },  },}
[/code]

* ### 设置级别

发送仅包含指令的消息来设置会话默认值：

CodeCopy code
[code]
    /elevated full
[/code]

或者内联使用它（仅应用于该消息）：

CodeCopy code
[code]
    /elevated on run the deployment script
[/code]

* ### 命令在沙箱外运行

启用提升模式后，`exec` 调用会离开沙箱。有效主机默认为 `gateway`，或者当配置的/会话的 exec 目标为 `node` 时为 `node`。在 `full` 模式下，会跳过 exec 审批。在 `on`/`ask` 模式下，配置的审批规则仍然适用。

## 解析顺序

  1. 消息上的**内联指令** （仅应用于该消息）
  2. **会话覆盖** （通过发送仅包含指令的消息设置）
  3. **全局默认值** （配置中的 `agents.defaults.elevatedDefault`）


## 可用性和允许列表

  * **全局门禁** ：`tools.elevated.enabled`（必须为 `true`）
  * **发送者允许列表** ：`tools.elevated.allowFrom`，按渠道列出
  * **每智能体门禁** ：`agents.list[].tools.elevated.enabled`（只能进一步限制）
  * **每智能体允许列表** ：`agents.list[].tools.elevated.allowFrom`（发送者必须同时匹配全局 + 每智能体）
  * **Discord 回退** ：如果省略 `tools.elevated.allowFrom.discord`，则使用 `channels.discord.allowFrom` 作为回退
  * **所有门禁都必须通过** ；否则提升模式会被视为不可用


允许列表条目格式：

前缀 | 匹配项  
---|---  
（无） | 发送者 ID、E.164 或 From 字段  
`name:` | 发送者显示名称  
`username:` | 发送者用户名  
`tag:` | 发送者标签  
`id:`, `from:`, `e164:` | 显式身份定位  
  
## 提升模式不控制什么

  * **工具策略** ：如果工具策略拒绝 `exec`，提升模式无法覆盖它。
  * **主机选择策略** ：提升模式不会把 `auto` 变成不受限制的跨主机覆盖。它使用配置的/会话的 exec 目标规则，只有当目标已经是 `node` 时才选择 `node`。
  * **独立于`/exec`**：`/exec` 指令会为授权发送者调整每会话 exec 默认值，并且不需要提升模式。


## 相关内容

[**Exec 工具** 来自智能体的 Shell 命令执行。 ](</zh-CN/tools/exec>) [**Exec 审批** `exec` 的审批和允许列表系统。 ](</zh-CN/tools/exec-approvals>) [**沙箱隔离** Gateway 网关级沙箱配置。 ](</zh-CN/gateway/sandboxing>) [**沙箱、工具策略与提升模式** 三个门禁在工具调用期间如何组合。 ](</zh-CN/gateway/sandbox-vs-tool-policy-vs-elevated>)

Was this useful?YesNo