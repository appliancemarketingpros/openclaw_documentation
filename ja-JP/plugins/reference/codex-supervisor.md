---
title: Codex Supervisor Plugin
source_url: https://docs.openclaw.ai/ja-JP/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Codex Supervisor Plugin

OpenClaw から Codex app-server セッションを監督します。

## 配布

  * パッケージ: `@openclaw/codex-supervisor`
  * インストール経路: OpenClaw に含まれます


## サーフェス

contracts: tools

## セッション一覧

`codex_sessions_list` は既定で、読み込まれた Codex セッションのみを対象にします。保存済み履歴を含めるには `include_stored` を設定します。この Plugin は Codex app-server の state DB のみの一覧取得パスを使用し、保存済み結果の上限を既定で 200 件にします。その上限を下げる、または最大 1000 件まで上げるには、`max_stored_sessions` を渡します。

Was this useful?YesNo

Open issue