---
title: Bun（實驗性）
source_url: https://docs.openclaw.ai/zh-TW/install/bun
scraped_at: 2026-05-25
---

Bun 是可選的本機執行階段，可直接執行 TypeScript（`bun run ...`、`bun --watch ...`）。預設套件管理器仍為 `pnpm`，它受到完整支援，且由文件工具使用。Bun 無法使用 `pnpm-lock.yaml`，並會忽略它。

## 安裝

* ### 安裝相依性

shCopy code
[code]
    bun install
[/code]

`bun.lock` / `bun.lockb` 已加入 gitignore，因此不會造成儲存庫變動。若要完全略過 lockfile 寫入：

shCopy code
[code]
    bun install --no-save
[/code]

* ### 建置與測試

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## 生命週期腳本

Bun 會封鎖相依性的生命週期腳本，除非明確信任。對此儲存庫而言，常見被封鎖的腳本並非必要：

  * `baileys` `preinstall` \-- 檢查 Node 主版號 >= 20（OpenClaw 預設使用 Node 24，且仍支援 Node 22 LTS，目前為 `22.16+`）
  * `protobufjs` `postinstall` \-- 發出關於不相容版本配置的警告（沒有建置產物）


如果遇到需要這些腳本的執行階段問題，請明確信任它們：

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## 注意事項

部分腳本目前仍硬編碼 pnpm（例如 `docs:build`、`ui:*`、`protocol:check`）。目前請透過 pnpm 執行這些腳本。

## 相關

  * [安裝概覽](</zh-TW/install>)
  * [Node.js](</zh-TW/install/node>)
  * [更新](</zh-TW/install/updating>)


Was this useful?YesNo