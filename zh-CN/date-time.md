---
title: 日期和时间
source_url: https://docs.openclaw.ai/zh-CN/date-time
scraped_at: 2026-05-25
---

OpenClaw 默认对 **传输时间戳使用主机本地时间** ，并且 **仅在系统提示词中使用用户时区** 。 会保留提供商时间戳，以便工具保持其原生语义（当前时间可通过 `session_status` 获取）。

## 消息封套（默认本地）

入站消息会包装一个时间戳（精确到分钟）：

CodeCopy code
[code]
    [Provider ... 2026-01-05 16:26 PST] message text
[/code]

无论提供商时区是什么，此封套时间戳 **默认使用主机本地时间** 。

你可以覆盖此行为：

json5Copy code
[code]
    {  agents: {    defaults: {      envelopeTimezone: "local", // "utc" | "local" | "user" | IANA timezone      envelopeTimestamp: "on", // "on" | "off"      envelopeElapsed: "on", // "on" | "off"    },  },}
[/code]

  * `envelopeTimezone: "utc"` 使用 UTC。
  * `envelopeTimezone: "local"` 使用主机时区。
  * `envelopeTimezone: "user"` 使用 `agents.defaults.userTimezone`（回退到主机时区）。
  * 使用显式 IANA 时区（例如 `"America/Chicago"`）来指定固定时区。
  * `envelopeTimestamp: "off"` 会从封套标头中移除绝对时间戳。
  * `envelopeElapsed: "off"` 会移除已用时间后缀（`+2m` 样式）。


### 示例

**本地（默认）：**

CodeCopy code
[code]
    [WhatsApp +1555 2026-01-18 00:19 PST] hello
[/code]

**用户时区：**

CodeCopy code
[code]
    [WhatsApp +1555 2026-01-18 00:19 CST] hello
[/code]

**启用已用时间：**

CodeCopy code
[code]
    [WhatsApp +1555 +30s 2026-01-18T05:19Z] follow-up
[/code]

## 系统提示词：当前日期和时间

如果已知用户时区，系统提示词会包含一个专用的 **当前日期和时间** 部分，其中 **仅包含时区** （不包含时钟/时间格式）， 以保持提示词缓存稳定：

CodeCopy code
[code]
    Time zone: America/Chicago
[/code]

当智能体需要当前时间时，请使用 `session_status` 工具；Status 卡片包含一行时间戳。

## 系统事件行（默认本地）

插入到智能体上下文中的排队系统事件会带有时间戳前缀，并使用与消息封套相同的 时区选择（默认：主机本地）。

CodeCopy code
[code]
    System: [2026-01-12 12:19:17 PST] Model switched.
[/code]

### 配置用户时区 + 格式

json5Copy code
[code]
    {  agents: {    defaults: {      userTimezone: "America/Chicago",      timeFormat: "auto", // auto | 12 | 24    },  },}
[/code]

  * `userTimezone` 设置提示词上下文中的 **用户本地时区** 。
  * `timeFormat` 控制提示词中的 **12 小时制/24 小时制显示** 。`auto` 跟随操作系统偏好设置。


## 时间格式检测（auto）

当 `timeFormat: "auto"` 时，OpenClaw 会检查操作系统偏好设置（macOS/Windows）， 并回退到区域设置格式。检测到的值会 **按进程缓存** ， 以避免重复系统调用。

## 工具载荷 + 连接器（原始提供商时间 + 规范化字段）

渠道工具会返回 **提供商原生时间戳** ，并添加规范化字段以保持一致性：

  * `timestampMs`：纪元毫秒数（UTC）
  * `timestampUtc`：ISO 8601 UTC 字符串


会保留原始提供商字段，确保不会丢失任何信息。

  * Slack：来自 API 的类纪元字符串
  * Discord：UTC ISO 时间戳
  * Telegram/WhatsApp：提供商特定的数字/ISO 时间戳


如果你需要本地时间，请在下游使用已知时区进行转换。

## 相关文档

  * [系统提示词](</zh-CN/concepts/system-prompt>)
  * [时区](</zh-CN/concepts/timezone>)
  * [消息](</zh-CN/concepts/messages>)


Was this useful?YesNo