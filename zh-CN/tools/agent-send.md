---
title: 智能体发送
source_url: https://docs.openclaw.ai/zh-CN/tools/agent-send
scraped_at: 2026-05-25
---

`openclaw agent` 会从命令行运行单个智能体轮次，无需传入聊天消息。可用于脚本化工作流、测试和程序化投递。

## 快速开始

* ### 运行一个简单的智能体轮次

bashCopy code
[code]
    openclaw agent --message "What is the weather today?"
[/code]

这会通过 Gateway 网关发送消息并打印回复。

* ### 指定特定智能体或会话

bashCopy code
[code]
    # Target a specific agentopenclaw agent --agent ops --message "Summarize logs" # Target a phone number (derives session key)openclaw agent --to +15555550123 --message "Status update" # Reuse an existing sessionopenclaw agent --session-id abc123 --message "Continue the task"
[/code]

* ### 将回复投递到渠道

bashCopy code
[code]
    # Deliver to WhatsApp (default channel)openclaw agent --to +15555550123 --message "Report ready" --deliver # Deliver to Slackopenclaw agent --agent ops --message "Generate report" \  --deliver --reply-channel slack --reply-to "#reports"
[/code]

## 标志

标志 | 描述  
---|---  
`--message \<text\>` | 要发送的消息（必需）  
`--to \<dest\>` | 从目标（电话、聊天 ID）派生会话键  
`--agent \<id\>` | 指定已配置的智能体（使用其 `main` 会话）  
`--session-id \<id\>` | 按 ID 复用现有会话  
`--local` | 强制使用本地嵌入式运行时（跳过 Gateway 网关）  
`--deliver` | 将回复发送到聊天渠道  
`--channel \<name\>` | 投递渠道（whatsapp、telegram、discord、slack 等）  
`--reply-to \<target\>` | 覆盖投递目标  
`--reply-channel \<name\>` | 覆盖投递渠道  
`--reply-account \<id\>` | 覆盖投递账号 ID  
`--thinking \<level\>` | 为所选模型配置文件设置思考级别  
`--verbose \<on|full|off\>` | 设置详细输出级别  
`--timeout \<seconds\>` | 覆盖智能体超时时间  
`--json` | 输出结构化 JSON  
  
## 行为

  * 默认情况下，CLI 会**通过 Gateway 网关** 。添加 `--local` 可强制使用当前机器上的嵌入式运行时。
  * 如果 Gateway 网关不可达，CLI 会**回退** 到本地嵌入式运行。
  * 会话选择：`--to` 派生会话键（群组/渠道目标会保留隔离；直接聊天会合并到 `main`）。
  * 思考和详细输出标志会持久化到会话存储。
  * 输出：默认是纯文本，或使用 `--json` 输出结构化载荷 + 元数据。
  * 使用 `--json --deliver` 时，JSON 会包含已发送、已抑制、部分发送和发送失败的投递状态。参见 [JSON 投递状态](</zh-CN/cli/agent#json-delivery-status>)。


## 示例

bashCopy code
[code]
    # Simple turn with JSON outputopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --json # Turn with thinking levelopenclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium # Deliver to a different channel than the sessionopenclaw agent --agent ops --message "Alert" --deliver --reply-channel telegram --reply-to "@admin"
[/code]

## 相关内容

[**智能体 CLI 参考** 完整的 `openclaw agent` 标志和选项参考。 ](</zh-CN/cli/agent>) [**子智能体** 后台子智能体生成。 ](</zh-CN/tools/subagents>) [**会话** 会话键的工作方式，以及 `--to`、`--agent` 和 `--session-id` 如何解析它们。 ](</zh-CN/concepts/session>) [**斜杠命令** 在智能体会话中使用的原生命令目录。 ](</zh-CN/tools/slash-commands>)

Was this useful?YesNo