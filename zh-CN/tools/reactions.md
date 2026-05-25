---
title: 表情回应
source_url: https://docs.openclaw.ai/zh-CN/tools/reactions
scraped_at: 2026-05-25
---

智能体可以使用带有 `react` 动作的 `message` 工具在消息上添加和移除 emoji 反应。反应行为因渠道和传输协议而异。

## 工作方式

jsonCopy code
[code]
    {  "action": "react",  "messageId": "msg-123",  "emoji": "thumbsup"}
[/code]

  * 添加反应时必须提供 `emoji`。
  * 将 `emoji` 设为空字符串（`""`）以移除机器人的反应。
  * 设置 `remove: true` 以移除特定 emoji（需要非空 `emoji`）。
  * 在支持状态反应的渠道上，反应中的 `trackToolCalls: true` 会让运行时在同一轮次中将该被反应的消息用于后续工具进度反应。


## 渠道行为

Discord and Slack

  * 空 `emoji` 会移除机器人在该消息上的所有反应。
  * `remove: true` 只会移除指定 emoji。

Google Chat

  * 空 `emoji` 会移除应用在该消息上的反应。
  * `remove: true` 只会移除指定 emoji。

Telegram

  * 空 `emoji` 会移除机器人的反应。
  * `remove: true` 也会移除反应，但为了通过工具验证仍需要非空 `emoji`。

WhatsApp

  * 空 `emoji` 会移除机器人反应。
  * `remove: true` 会在内部映射为空 emoji（工具调用中仍需要 `emoji`）。

Zalo Personal (zalouser)

  * 需要非空 `emoji`。
  * `remove: true` 会移除该特定 emoji 反应。

Feishu/Lark

  * 使用带有 `add`、`remove` 和 `list` 动作的 `feishu_reaction` 工具。
  * 添加/移除需要 `emoji_type`；移除还需要 `reaction_id`。

Signal

  * 入站反应通知由 `channels.signal.reactionNotifications` 控制：`"off"` 会禁用它们，`"own"`（默认）会在用户对机器人消息做出反应时发出事件，`"all"` 会为所有反应发出事件。

iMessage

  * 出站反应是 iMessage tapback（`love`、`like`、`dislike`、`laugh`、`emphasize` 和 `question`）。
  * 入站 tapback 通知由 `channels.imessage.reactionNotifications` 控制：`"off"` 会禁用它们，`"own"`（默认）会在用户对机器人撰写的消息做出反应时发出事件，`"all"` 会为来自已授权发送者的所有 tapback 发出事件。


## 反应级别

按渠道配置的 `reactionLevel` 控制智能体使用反应的范围。值通常为 `off`、`ack`、`minimal` 或 `extensive`。

  * [Telegram reactionLevel](</zh-CN/channels/telegram#reaction-notifications>) — `channels.telegram.reactionLevel`
  * [WhatsApp reactionLevel](</zh-CN/channels/whatsapp#reaction-level>) — `channels.whatsapp.reactionLevel`


在各个渠道上设置 `reactionLevel`，以调整智能体在每个平台上对消息做出反应的活跃程度。

## 相关内容

  * [Agent Send](</zh-CN/tools/agent-send>) — 包含 `react` 的 `message` 工具
  * [渠道](</zh-CN/channels>) — 特定于渠道的配置


Was this useful?YesNo