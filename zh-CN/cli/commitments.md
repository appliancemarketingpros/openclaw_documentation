---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/zh-CN/cli/commitments
scraped_at: 2026-05-25
---

列出并管理推断式跟进承诺。

跟进承诺是选择启用的短期跟进记忆，由会话上下文创建。请参阅[推断式跟进承诺](</zh-CN/concepts/commitments>)了解概念指南。

没有子命令时，`openclaw commitments` 会列出待处理的跟进承诺。

## 用法

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## 选项

  * `--all`：显示所有状态，而不是只显示待处理的跟进承诺。
  * `--agent <id>`：筛选到一个智能体 ID。
  * `--status <status>`：按状态筛选。取值：`pending`、`sent`、`dismissed`、`snoozed` 或 `expired`。
  * `--json`：输出机器可读的 JSON。


## 示例

列出待处理的跟进承诺：

bashCopy code
[code]
    openclaw commitments
[/code]

列出所有已存储的跟进承诺：

bashCopy code
[code]
    openclaw commitments --all
[/code]

筛选到一个智能体：

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

查找已推迟的跟进承诺：

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

解除一个或多个跟进承诺：

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

导出为 JSON：

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## 输出

文本输出包括：

  * 跟进承诺 ID
  * 状态
  * 类型
  * 最早到期时间
  * 作用域
  * 建议的跟进消息文本


JSON 输出还包括跟进承诺存储路径和完整的已存储记录。

## 相关内容

  * [推断式跟进承诺](</zh-CN/concepts/commitments>)
  * [记忆概览](</zh-CN/concepts/memory>)
  * [Heartbeat](</zh-CN/gateway/heartbeat>)
  * [定时任务](</zh-CN/automation/cron-jobs>)


Was this useful?YesNo