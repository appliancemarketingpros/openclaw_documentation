---
title: Codex Supervisor 外掛
source_url: https://docs.openclaw.ai/zh-TW/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Codex Supervisor 外掛

從 OpenClaw 監督 Codex app-server 工作階段。

## 發行

  * 套件：`@openclaw/codex-supervisor`
  * 安裝途徑：包含於 OpenClaw


## 介面

合約：工具

## 工作階段列表

`codex_sessions_list` 預設只列出已載入的 Codex 工作階段。設定 `include_stored` 可包含已儲存的歷史記錄；此外掛會使用 Codex app-server 僅限狀態資料庫的列表路徑，並預設將已儲存結果上限設為 200。傳入 `max_stored_sessions` 可降低或提高該上限，最高可達 1000。

Was this useful?YesNo

Open issue