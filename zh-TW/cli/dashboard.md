---
title: 儀表板
source_url: https://docs.openclaw.ai/zh-TW/cli/dashboard
scraped_at: 2026-05-25
---

# `openclaw dashboard`

使用目前的驗證資訊開啟控制 UI。

bashCopy code
[code]
    openclaw dashboardopenclaw dashboard --no-open
[/code]

注意事項：

  * `dashboard` 會在可行時解析已設定的 `gateway.auth.token` SecretRef。
  * `dashboard` 會遵循 `gateway.tls.enabled`：啟用 TLS 的 Gateway 會列印/開啟 `https://` 控制 UI URL，並透過 `wss://` 連線。
  * 如果已透過 token 驗證的 dashboard URL 無法傳送到剪貼簿/瀏覽器， `dashboard` 會記錄一則安全的手動驗證提示，指出 `OPENCLAW_GATEWAY_TOKEN`、 `gateway.auth.token` 和片段鍵 `token`，但不會列印 token 值。
  * 對於由 SecretRef 管理的 token（無論已解析或未解析），`dashboard` 會列印/複製/開啟不含 token 的 URL，以避免在終端機輸出、剪貼簿歷史記錄或瀏覽器啟動引數中暴露外部密鑰。
  * 如果 `gateway.auth.token` 是由 SecretRef 管理，但在此命令路徑中尚未解析，該命令會列印不含 token 的 URL 和明確的修復指引，而不是嵌入無效的 token 預留位置。


## 相關

  * [CLI 參考](</zh-TW/cli>)
  * [Dashboard](</zh-TW/web/dashboard>)


Was this useful?YesNo