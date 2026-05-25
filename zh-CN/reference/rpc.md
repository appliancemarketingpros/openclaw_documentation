---
title: RPC 适配器
source_url: https://docs.openclaw.ai/zh-CN/reference/rpc
scraped_at: 2026-05-25
---

OpenClaw 通过 JSON-RPC 集成外部 CLI。目前使用两种模式。

## 模式 A：HTTP 守护进程（signal-cli）

  * `signal-cli` 作为守护进程运行，通过 HTTP 提供 JSON-RPC。
  * 事件流是 SSE（`/api/v1/events`）。
  * 健康探针：`/api/v1/check`。
  * 当 `channels.signal.autoStart=true` 时，OpenClaw 拥有生命周期管理。


请参阅 [Signal](</zh-CN/channels/signal>) 了解设置和端点。

## 模式 B：标准输入/输出子进程（imsg）

  * OpenClaw 为 [iMessage](</zh-CN/channels/imessage>) 将 `imsg rpc` 作为子进程启动。
  * JSON-RPC 通过 stdin/stdout 按行分隔传输（每行一个 JSON 对象）。
  * 不需要 TCP 端口，也不需要守护进程。


使用的核心方法：

  * `watch.subscribe` → 通知（`method: "message"`）
  * `watch.unsubscribe`
  * `send`
  * `chats.list`（探针/诊断）


请参阅 [iMessage](</zh-CN/channels/imessage>) 了解旧版设置和寻址（推荐使用 `chat_id`）。

## 适配器指南

  * Gateway 网关拥有该进程（启动/停止绑定到提供商生命周期）。
  * 保持 RPC 客户端有韧性：超时、退出时重启。
  * 优先使用稳定 ID（例如 `chat_id`），而不是显示字符串。


## 相关

  * [Gateway 网关协议](</zh-CN/gateway/protocol>)


Was this useful?YesNo