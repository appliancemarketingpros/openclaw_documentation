---
title: 频道出站 API
source_url: https://docs.openclaw.ai/zh-CN/plugins/sdk-channel-outbound
scraped_at: 2026-06-29
---

快速开始

渠道插件应从 `openclaw/plugin-sdk/channel-outbound` 暴露出站消息行为。使用 `openclaw/plugin-sdk/channel-inbound` 进行接收/上下文/分发编排。

核心负责排队、持久性、通用重试策略、钩子、回执，以及共享的 `message` 工具。插件负责原生发送/编辑/删除调用、目标规范化、平台线程、选中的引用、通知标志、账户状态，以及平台特定副作用。

## 适配器

大多数插件会定义一个 `message` 适配器：

tsCopy code
[code]
       defineChannelMessageAdapter,  createMessageReceiptFromOutboundResults,} from "openclaw/plugin-sdk/channel-outbound"; export const demoMessageAdapter = defineChannelMessageAdapter({  id: "demo",  durableFinal: {    capabilities: {      text: true,      replyTo: true,      thread: true,      messageSendingHooks: true,    },  },  send: {    text: async ({ cfg, to, text, accountId, replyToId, threadId, signal }) => {      const sent = await sendDemoMessage({        cfg,        to,        text,        accountId: accountId ?? undefined,        replyToId: replyToId ?? undefined,        threadId: threadId == null ? undefined : String(threadId),        signal,      });       return {        receipt: createMessageReceiptFromOutboundResults({          results: [{ channel: "demo", messageId: sent.id, conversationId: to }],          kind: "text",          threadId: threadId == null ? undefined : String(threadId),          replyToId: replyToId ?? undefined,        }),      };    },  },});
[/code]

只声明原生传输实际会保留的能力。使用此子路径导出的契约辅助函数覆盖每个已声明的发送、回执、实时预览和接收确认能力。

## 现有出站适配器

如果该渠道已经有兼容的 `outbound` 适配器，请派生消息适配器，而不是重复发送代码：

tsCopy code
[code]
     export const messageAdapter = createChannelMessageAdapterFromOutbound({  id: "demo",  outbound,  durableFinal: {    capabilities: {      text: true,      media: true,    },  },});
[/code]

## 持久发送

运行时发送辅助函数也位于 `channel-outbound`：

  * `sendDurableMessageBatch(...)`
  * `withDurableMessageSendContext(...)`
  * `deliverInboundReplyWithMessageSendContext(...)`
  * draft 流式传输/进度辅助函数，例如 `resolveChannelDraftStreamingChunking(...)`


`sendDurableMessageBatch(...)` 返回一个明确结果：

  * `sent`：至少一条可见的平台消息已送达。
  * `suppressed`：不应将没有平台消息视为缺失。
  * `partial_failed`：至少一条平台消息已送达，但后续载荷或副作用失败。
  * `failed`：未生成平台回执。


当一个批次混合了已发送、已抑制和失败的载荷时，使用 `payloadOutcomes`。不要根据空的旧版直接投递结果推断钩子取消。

## 兼容性分发

入站回复分发应通过 `channel-inbound` 中的 `dispatchChannelInboundReply(...)` 组装。将平台投递保留在投递适配器中；使用 `channel-outbound` 处理消息适配器、持久发送、回执、实时预览和回复管道选项。

Was this useful?YesNo

Open issue