---
title: Plugin 安裝覆寫
source_url: https://docs.openclaw.ai/zh-TW/plugins/install-overrides
scraped_at: 2026-05-25
---

Plugin 安裝覆寫可讓維護者針對特定 npm 套件或本機 npm-pack 壓縮封存檔，測試設定期間的 Plugin 安裝。它們僅供 E2E 與套件驗證使用。一般使用者應使用 [`openclaw plugins install`](</zh-TW/cli/plugins>) 安裝 Plugin。

## 環境

除非同時設定兩個變數，否則覆寫會停用：

bashCopy code
[code]
    export OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1export OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{  "codex": "npm-pack:/tmp/openclaw-codex-2026.5.8.tgz",  "openclaw-web-search": "npm:@openclaw/web-search@2026.5.8"}'
[/code]

覆寫對應表是以 Plugin id 作為鍵的 JSON。值支援：

  * `npm:<registry-spec>` 用於登錄套件與精確版本或標籤
  * `npm-pack:<path.tgz>` 用於由 `npm pack` 產生的本機壓縮封存檔


相對 `npm-pack:` 路徑會從目前工作目錄解析。

## 行為

當設定期間的流程要求安裝某個 Plugin，且其 id 出現在對應表中時，OpenClaw 會使用覆寫來源，而非目錄、內建或預設 npm 來源。這適用於入門設定，以及其他使用共用設定期間 Plugin 安裝器的流程。

覆寫仍會強制要求預期的 Plugin id。對應到 `codex` 的壓縮封存檔必須安裝 manifest id 為 `codex` 的 Plugin。

覆寫不會繼承官方受信任來源狀態。即使目錄項目通常代表 OpenClaw 擁有的套件，覆寫也會被視為操作者提供的測試輸入。

工作區 `.env` 檔案無法啟用安裝覆寫。請在啟動 OpenClaw 的受信任殼層、CI 作業或遠端測試命令中設定這些變數。

## 套件 E2E

使用隔離的狀態目錄，讓套件安裝與安裝記錄不會影響你的一般 OpenClaw 狀態：

bashCopy code
[code]
    npm pack extensions/codex --pack-destination /tmp OPENCLAW_STATE_DIR="$(mktemp -d)" \OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1 \OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{"codex":"npm-pack:/tmp/openclaw-codex-2026.5.8.tgz"}' \pnpm openclaw onboard --mode local
[/code]

驗證狀態目錄下已安裝的套件：

bashCopy code
[code]
    find "$OPENCLAW_STATE_DIR/npm/node_modules" -maxdepth 3 -name package.json -printgrep -R '"@openclaw/codex"' "$OPENCLAW_STATE_DIR/npm/package-lock.json"
[/code]

對於即時提供者 E2E，請在啟動測試命令前，從受信任殼層或 CI 密鑰載入真實 API 金鑰。不要印出金鑰；只回報來源以及金鑰是否存在。

Was this useful?YesNo