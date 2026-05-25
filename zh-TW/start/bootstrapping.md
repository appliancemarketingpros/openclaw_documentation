---
title: 代理程式啟動程序
source_url: https://docs.openclaw.ai/zh-TW/start/bootstrapping
scraped_at: 2026-05-25
---

啟動設定是 **首次執行** 的準備流程，會準備代理程式工作區並收集身分詳細資料。它會在入門設定之後、代理程式第一次啟動時發生。

## 啟動設定會做什麼

在第一次代理程式執行時，OpenClaw 會啟動設定工作區（預設為 `~/.openclaw/workspace`）：

  * 建立初始 `AGENTS.md`、`BOOTSTRAP.md`、`IDENTITY.md`、`USER.md`。
  * 執行簡短的問答流程（一次一個問題）。
  * 將身分資料與偏好設定寫入 `IDENTITY.md`、`USER.md`、`SOUL.md`。
  * 完成後移除 `BOOTSTRAP.md`，讓它只執行一次。


對於嵌入式/本機模型執行，OpenClaw 會讓 `BOOTSTRAP.md` 保持在具特權的系統內容脈絡之外。在主要互動式首次執行時，它仍會在使用者提示中傳入檔案內容，讓無法可靠呼叫 `read` 工具的模型也能完成此流程。如果目前執行無法安全存取工作區，代理程式會收到有限的啟動設定說明，而不是一般問候語。

## 略過啟動設定

若要對已預先建立內容的工作區略過此步驟，請執行 `openclaw onboard --skip-bootstrap`。

## 執行位置

啟動設定一律在 **gateway 主機** 上執行。如果 macOS app 連線到遠端 Gateway，工作區與啟動設定檔案會位於該遠端機器上。

## 相關文件

  * macOS app 入門設定：[入門設定](</zh-TW/start/onboarding>)
  * 工作區版面配置：[代理程式工作區](</zh-TW/concepts/agent-workspace>)


Was this useful?YesNo