---
title: Codex Supervisor 插件
source_url: https://docs.openclaw.ai/zh-CN/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

快速开始

# Codex Supervisor 插件

从 OpenClaw 监督 Codex app-server 会话。

## 分发

  * 软件包：`@openclaw/codex-supervisor`
  * 安装方式：包含在 OpenClaw 中


## 表面

contracts: tools

## 会话列表

`codex_sessions_list` 默认仅返回已加载的 Codex 会话。设置 `include_stored` 可包含已存储的历史记录；该插件使用 Codex app-server 的仅 state-DB 列表路径，并默认将已存储结果限制为 200 条。传入 `max_stored_sessions` 可降低或提高该上限，最高为 1000。

Was this useful?YesNo

Open issue