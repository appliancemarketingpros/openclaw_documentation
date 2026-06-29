---
title: 成熟度分類法
source_url: https://docs.openclaw.ai/zh-TW/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# 成熟度分類法

評分卡背後的模型

面向 > 類別 > 能力 > 證據。

50 個面向分為 4 個系列，每個類別都對應到標準文件與 QA 覆蓋 ID。

瀏覽產品領域 / 開啟詳細分類法 / [檢視分數](</zh-TW/maturity/scorecard>)

## 如何閱讀本頁

面向是指產品領域，例如閘道執行階段、Discord 或 macOS 應用程式。每個面向包含多個類別，而每個類別包含 QA 情境所涵蓋的能力層級檢查。使用評分卡進行發布層級判斷；使用本頁檢視其底層模型。

## 成熟度等級

M0已規劃方向已知，但尚無受支援的使用者路徑。晉升：設計議題、負責人與目標面向皆已存在。

M1實驗性已實作，但受限於注意事項、旗標、原始碼建置，或僅維護者可用的流程。晉升：維護者可從目前主分支執行情境。

M2Alpha 版實際使用者可以試用，但預期會有破壞性變更與不完整的使用者體驗。晉升：有文件化設定、基本測試、已知注意事項，以及至少一項真實環境證明。

M3Beta 版已有公開路徑，且主要工作流程可在有限注意事項下使用。晉升：安裝/更新文件、迴歸測試、支援執行手冊，以及在預期環境中的成功情境證明。

M4穩定版一般使用者的建議路徑。失敗會被視為迴歸。晉升：發布關卡、doctor/疑難排解路徑、完整文件，以及反覆的真實世界證明。

M5卓越完善精緻、令人愉悅、具備完善儀表化，且可與最佳同類工作流程競爭。晉升：穩定版，加上代表性使用者通過使用者評分卡。

## 產品領域

### 核心

命令列介面 M4穩定版7 個領域 - 已完成 90% 閘道執行階段 M4穩定版13 個領域 - 已完成 89% 代理程式執行階段 M3Beta 版9 個領域 - 已完成 79% 工作階段、記憶與情境引擎 M3Beta 版9 個領域 - 已完成 79% 頻道框架 M3Beta 版8 個領域 - 已完成 79% 可觀測性 M3Beta 版5 個領域 - 已完成 79% 閘道 Web 應用程式 M3Beta 版6 個領域 - 已完成 79% 外掛 M3測試版9 個領域 - 完成 79% 安全性、驗證、配對與機密 M3測試版6 個領域 - 完成 79% 自動化：排程、鉤子、任務、輪詢 M3測試版6 個領域 - 完成 79% 媒體理解與媒體生成 M2早期版6 個領域 - 完成 68% 語音與即時對話 M2早期版6 個領域 - 完成 68% 終端介面 M2早期版5 個領域 - 完成 66% ClawHub M2早期版4 個領域 - 完成 62% OpenClaw 應用程式 SDK M2早期版6 個領域 - 完成 53%

### 平台

Linux 閘道主機 M4穩定版5 個領域 - 完成 89% macOS 閘道主機 M4穩定版7 個領域 - 完成 88% Docker 與 Podman 託管 M3測試版4 個領域 - 完成 79% 透過 WSL2 使用 Windows M3測試版6 個領域 - 完成 79% Raspberry Pi 與小型 Linux 裝置 M3測試版4 個領域 - 完成 79% macOS 輔助應用程式 M3測試版8 個領域 - 完成 78% Android 應用程式 M2早期版7 個領域 - 完成 66% 原生 Windows M2Alpha4 個領域 - 完成 66% Kubernetes 託管 M2Alpha4 個領域 - 完成 61% iOS 應用程式 M1實驗性8 個領域 - 完成 44% Nix 安裝路徑 M1實驗性5 個領域 - 完成 44% watchOS 伴隨介面 M1實驗性5 個領域 - 完成 44% Linux 伴隨應用程式 M0已規劃5 個領域 - 完成 21% 原生 Windows 伴隨應用程式 M0已規劃5 個領域 - 完成 21%

### 頻道

Discord M4穩定6 個領域 - 完成 87% Telegram M3Beta5 個領域 - 完成 78% Slack M3Beta5 個領域 - 完成 78% iMessage 與 BlueBubbles M3Beta5 個領域 - 完成 78% WhatsApp M3Beta5 個領域 - 完成 78% Matrix M2Alpha6 個領域 - 完成 67% Google Chat M2Alpha5 個領域 - 完成 66% Microsoft Teams M2Alpha5 個領域 - 完成 66% Signal M2Alpha5 個領域 - 完成 66% Feishu、QQ Bot、微信、騰訊元寶、Zalo、Zalo Personal、區域頻道 M2Alpha4 個領域 - 完成 58% Mattermost、LINE、IRC、Nextcloud Talk、Nostr、Twitch、Tlon、Synology Chat M2Alpha4 個領域 - 完成 54% 語音通話頻道 M1實驗性5 個領域 - 完成 44%

### 提供者與工具

瀏覽器自動化、exec 與沙箱工具 M3Beta3 個領域 - 完成 79% OpenAI 與 Codex 提供者路徑 M3Beta5 個領域 - 完成 79% 網頁搜尋工具 M3Beta4 個領域 - 完成 79% Anthropic 提供者路徑 M3Beta5 個領域 - 完成 78% Google 提供者路徑 M3Beta5 個領域 - 完成 78% OpenRouter 提供者路徑 M3Beta4 個領域 - 完成 78% 圖片、影片與音樂生成工具 M2Alpha5 個領域 - 完成 68% 本機模型提供者：Ollama、vLLM、SGLang、LM Studio M2Alpha5 個領域 - 完成 68% 長尾託管提供者 M2Alpha3 個領域 - 完成 68%

## 詳細資訊

### 核心

命令列介面 - M4 穩定 - 7 個領域

一般設定與修復路徑已記錄於安裝、命令列介面與閘道文件中。特定平台的 Windows 路徑則在 Windows via WSL2 與原生 Windows 列中追蹤。

涵蓋範圍 實驗性 - 4%品質 穩定 - 83%完整性 穩定 - 90%部分 - 6

命令列介面設定 6 項能力 / 支援 LTS

實驗性17%

穩定版89%

穩定版90%

[索引](</zh-TW/install>), [安裝程式](</zh-TW/install/installer>), [節點](</zh-TW/install/node>), [更新](</zh-TW/install/updating>)

導覽與驗證設定 5 項能力 / 支援 LTS

實驗性0%

Beta75%

穩定版89%

[導覽](</zh-TW/cli/onboard>), [設定](</zh-TW/cli/configure>), [導覽概覽](</zh-TW/start/onboarding-overview>)

外掛與通道設定 5 項能力

實驗性0%

Beta75%

穩定版89%

[導覽](</zh-TW/cli/onboard>), [外掛](</zh-TW/cli/plugins>), [通道](</zh-TW/cli/channels>)

閘道服務管理 5 項能力 / 支援 LTS

實驗性14%

穩定版87%

穩定版90%

[閘道](</zh-TW/cli/gateway>), [更新](</zh-TW/install/updating>), [疑難排解](</zh-TW/gateway/troubleshooting>)

命令列介面可觀測性 5 項能力 / 支援 LTS

實驗性0%

穩定版89%

穩定版90%

[狀態](</zh-TW/cli/status>), [健康狀態](</zh-TW/cli/health>), [記錄](</zh-TW/cli/logs>), [診斷](</zh-TW/gateway/diagnostics>)

診斷 10 項能力 / 支援 LTS

實驗性0%

穩定版89%

穩定版90%

[診斷](</zh-TW/cli/doctor>), [診斷](</zh-TW/gateway/doctor>), [密鑰](</zh-TW/gateway/secrets>), [疑難排解](</zh-TW/gateway/troubleshooting>)

更新與升級 5 項能力 / 支援 LTS

實驗性0%

Beta75%

穩定版89%

[更新](</zh-TW/install/updating>), [更新](</zh-TW/cli/update>), [疑難排解](</zh-TW/gateway/troubleshooting>)

閘道執行階段 - M4 穩定版 - 13 個領域

核心架構、驗證、配對、通訊協定文件、守護程式文件，以及命令列介面執行手冊皆涵蓋廣泛且保持最新。

涵蓋範圍實驗性 - 6%品質穩定版 - 81%完整度穩定版 - 89%部分 - 12

核准與遠端執行 6 項功能 / LTS 支援

實驗性0%

測試版75%

穩定版89%

[協定](</zh-TW/gateway/protocol>), [索引](</zh-TW/gateway/security>)

HTTP API 4 項功能 / LTS 支援

實驗性25%

穩定版90%

穩定版90%

[索引](</zh-TW/gateway>), [OpenAI HTTP API](</zh-TW/gateway/openai-http-api>), [OpenResponses HTTP API](</zh-TW/gateway/openresponses-http-api>), [工具叫用 HTTP API](</zh-TW/gateway/tools-invoke-http-api>), [鉤子](</zh-TW/automation/hooks>), [索引](</zh-TW/web>)

託管網頁介面 4 項功能 / LTS 支援

實驗性0%

穩定版89%

穩定版90%

[索引](</zh-TW/gateway>), [架構](</zh-TW/concepts/architecture>), [控制介面](</zh-TW/web/control-ui>), [網頁聊天](</zh-TW/web/webchat>), [畫布](</zh-TW/refactor/canvas>)

閘道 RPC API 與事件 20 項功能 / LTS 支援

實驗性9%

穩定版90%

穩定版90%

[協定](</zh-TW/gateway/protocol>), [索引](</zh-TW/gateway>), [架構](</zh-TW/concepts/architecture>)

裝置驗證與配對 10 項功能 / LTS 支援

實驗性0%

測試版75%

穩定版89%

[協定](</zh-TW/gateway/protocol>), [配對](</zh-TW/gateway/pairing>), [索引](</zh-TW/gateway/security>)

網路存取與探索 6 項功能 / LTS 支援

實驗性0%

測試版75%

穩定版89%

[索引](</zh-TW/gateway>), [探索](</zh-TW/gateway/discovery>), [協定](</zh-TW/gateway/protocol>)

節點與遠端功能 8 項功能

實驗性0%

測試版75%

穩定版89%

[協定](</zh-TW/gateway/protocol>), [架構](</zh-TW/concepts/architecture>), [索引](</zh-TW/nodes>)

健康狀態、診斷與修復 7 項功能 / LTS 支援

實驗性0%

測試版75%

穩定版89%

[索引](</zh-TW/gateway>), [診斷](</zh-TW/gateway/diagnostics>), [Doctor](</zh-TW/gateway/doctor>)

通訊協定相容性 7 項功能 / LTS 支援

實驗性0%

Beta75%

穩定版89%

[通訊協定](</zh-TW/gateway/protocol>), [架構](</zh-TW/concepts/architecture>), [Typebox](</zh-TW/concepts/typebox>), [橋接通訊協定](</zh-TW/gateway/bridge-protocol>)

角色與權限 5 項功能 / LTS 支援

實驗性0%

Beta75%

穩定版89%

[通訊協定](</zh-TW/gateway/protocol>), [索引](</zh-TW/gateway/security>)

閘道生命週期 7 項功能 / LTS 支援

實驗性33%

穩定版90%

穩定版90%

[索引](</zh-TW/gateway>), [架構](</zh-TW/concepts/architecture>)

安全控制 6 項功能 / LTS 支援

實驗性0%

Beta75%

穩定版89%

[索引](</zh-TW/gateway/security>), [通訊協定](</zh-TW/gateway/protocol>), [探索](</zh-TW/gateway/discovery>)

WebSocket 連線 8 項功能 / LTS 支援

實驗性13%

穩定版90%

穩定版90%

[通訊協定](</zh-TW/gateway/protocol>), [架構](</zh-TW/concepts/architecture>)

Agent 執行階段 - M3 Beta - 9 個領域

主迴圈、模型、供應商路由與工具串流是一級功能，但供應商行為每週都會變動，因此每次發布都需要情境證明。

覆蓋率 實驗性 - 33%品質 Beta - 78%完整度 Beta - 79%部分 - 6

代理回合執行 3 項能力 / 支援 LTS

實驗性29%

Beta 版79%

Beta 版79%

[代理迴圈](</zh-TW/concepts/agent-loop>), [代理](</zh-TW/cli/agent>), [代理執行階段](</zh-TW/concepts/agent-runtimes>)

外部執行階段與子代理 4 項能力

實驗性30%

Beta 版79%

Beta 版79%

[代理執行階段](</zh-TW/concepts/agent-runtimes>), [Anthropic](</zh-TW/providers/anthropic>), [Google](</zh-TW/providers/google>), [子代理](</zh-TW/tools/subagents>)

託管供應商執行 5 項能力 / 支援 LTS

實驗性20%

Beta 版79%

Beta 版79%

[Openai](</zh-TW/providers/openai>), [Anthropic](</zh-TW/providers/anthropic>), [Google](</zh-TW/providers/google>), [模型](</zh-TW/concepts/models>)

本機與自託管供應商 5 項能力

實驗性0%

Alpha 版68%

Beta 版79%

[Ollama](</zh-TW/providers/ollama>), [模型](</zh-TW/concepts/models>), [代理](</zh-TW/cli/agent>)

模型與執行階段選擇 4 項能力 / 支援 LTS

實驗性25%

Beta 版79%

Beta 版79%

[模型](</zh-TW/concepts/models>), [模型](</zh-TW/cli/models>), [Openai](</zh-TW/providers/openai>), [代理執行階段](</zh-TW/concepts/agent-runtimes>)

供應商驗證 10 項能力 / 支援 LTS

實驗性24%

Beta 版79%

Beta 版79%

[模型](</zh-TW/concepts/models>), [代理](</zh-TW/cli/agent>), [模型](</zh-TW/cli/models>), [Openai](</zh-TW/providers/openai>), [Anthropic](</zh-TW/providers/anthropic>), [Google](</zh-TW/providers/google>), [子代理](</zh-TW/tools/subagents>)

串流與進度 2 項能力

Alpha 版56%

Beta 版79%

Beta 版79%

[串流](</zh-TW/concepts/streaming>), [代理迴圈](</zh-TW/concepts/agent-loop>)

工具呼叫與回應處理 3 項能力 / 支援 LTS

Alpha 版65%

Beta 版79%

Beta 版79%

[代理迴圈](</zh-TW/concepts/agent-loop>), [Ollama](</zh-TW/providers/ollama>)

工具執行控制 6 項能力 / LTS 支援

Alpha 版50%

Beta 版79%

Beta 版79%

[沙盒與工具政策與提升權限](</zh-TW/gateway/sandbox-vs-tool-policy-vs-elevated>), [代理迴圈](</zh-TW/concepts/agent-loop>), [子代理](</zh-TW/tools/subagents>)

工作階段、記憶與情境引擎 - M3 Beta - 9 個領域

文件完善且實作積極進行中。成熟度取決於逐字稿持久性、壓縮品質，以及跨用戶端一致性。

涵蓋範圍 實驗性 - 30%品質 Beta - 77%完整度 Beta - 79%部分 - 6

命令列介面工作階段與轉錄管理 2 項能力 / LTS 支援

實驗性0%

Alpha68%

Beta79%

[工作階段](</zh-TW/concepts/session>), [工作階段管理壓縮](</zh-TW/reference/session-management-compaction>), [工作階段](</zh-TW/cli/sessions>)

權杖管理 3 項能力 / LTS 支援

實驗性20%

Beta79%

Beta79%

[壓縮](</zh-TW/concepts/compaction>), [上下文](</zh-TW/concepts/context>), [工作階段管理壓縮](</zh-TW/reference/session-management-compaction>)

上下文引擎 2 項能力 / LTS 支援

Alpha57%

Beta79%

Beta79%

[上下文](</zh-TW/concepts/context>), [上下文引擎](</zh-TW/concepts/context-engine>), [Codex 上下文引擎測試框架](</zh-TW/plan/codex-context-engine-harness>)

跨用戶端歷史記錄與工作階段一致性 2 項能力

實驗性40%

Beta79%

Beta79%

[網頁聊天](</zh-TW/web/webchat>), [Android](</zh-TW/platforms/android>), [頻道路由](</zh-TW/channels/channel-routing>)

診斷、維護與復原 3 項能力

實驗性40%

Beta79%

Beta79%

[診斷](</zh-TW/gateway/diagnostics>), [工作階段管理壓縮](</zh-TW/reference/session-management-compaction>), [旗標](</zh-TW/diagnostics/flags>)

核心提示與上下文 2 項能力 / LTS 支援

實驗性38%

Beta79%

Beta79%

[上下文](</zh-TW/concepts/context>), [轉錄衛生](</zh-TW/reference/transcript-hygiene>), [Discord](</zh-TW/channels/discord>)

記憶 5 項能力

實驗性46%

Beta79%

Beta79%

[記憶設定](</zh-TW/reference/memory-config>), [記憶 Qmd](</zh-TW/concepts/memory-qmd>), [記憶](</zh-TW/concepts/memory>), [Discord](</zh-TW/channels/discord>)

工作階段路由 2 項能力 / LTS 支援

實驗性25%

Beta79%

Beta79%

[工作階段](</zh-TW/concepts/session>), [頻道路由](</zh-TW/channels/channel-routing>), [Discord](</zh-TW/channels/discord>)

逐字稿持久化 2 項功能 / LTS 支援

實驗性0%

Alpha 版68%

Beta 版79%

[工作階段管理壓縮](</zh-TW/reference/session-management-compaction>), [逐字稿衛生](</zh-TW/reference/transcript-hygiene>)

頻道框架 - M3 測試版 - 8 個領域

許多頻道共用閘道傳遞與路由合約，但頻道行為會因上游 API 與帳號政策限制而異。

涵蓋範圍實驗性 - 13%品質測試版 - 76%完整性測試版 - 79%部分 - 5

頻道動作、命令與核准 5 項能力

實驗性0%

Beta 版79%

Beta 版79%

[群組](</zh-TW/channels/groups>), [Discord](</zh-TW/channels/discord>), [Googlechat](</zh-TW/channels/googlechat>), [Signal](</zh-TW/channels/signal>), [Matrix](</zh-TW/channels/matrix>)

頻道設定 5 項能力 / LTS 支援

實驗性14%

Beta 版79%

Beta 版79%

[索引](</zh-TW/channels>), [配對](</zh-TW/channels/pairing>), [疑難排解](</zh-TW/channels/troubleshooting>), [SDK 頻道外掛](</zh-TW/plugins/sdk-channel-plugins>)

群組討論串與環境聊天室行為 5 項能力

實驗性36%

Beta 版79%

Beta 版79%

[群組](</zh-TW/channels/groups>), [群組訊息](</zh-TW/channels/group-messages>), [環境聊天室事件](</zh-TW/channels/ambient-room-events>), [廣播群組](</zh-TW/channels/broadcast-groups>), [Discord](</zh-TW/channels/discord>)

傳入存取與身分閘門 5 項能力 / LTS 支援

實驗性0%

Alpha 版68%

Beta 版79%

[存取群組](</zh-TW/channels/access-groups>), [群組](</zh-TW/channels/groups>), [Discord](</zh-TW/channels/discord>), [LINE](</zh-TW/channels/line>)

媒體附件與豐富頻道資料 4 項能力

實驗性0%

Alpha 版68%

Beta 版79%

[LINE](</zh-TW/channels/line>), [Signal](</zh-TW/channels/signal>), [Googlechat](</zh-TW/channels/googlechat>), [Matrix](</zh-TW/channels/matrix>), [Discord](</zh-TW/channels/discord>)

傳出傳遞與回覆管線 4 項能力 / LTS 支援

實驗性38%

Beta 版79%

Beta 版79%

[群組](</zh-TW/channels/groups>), [環境聊天室事件](</zh-TW/channels/ambient-room-events>), [Discord](</zh-TW/channels/discord>), [Matrix](</zh-TW/channels/matrix>), [設定頻道](</zh-TW/gateway/config-channels>)

對話路由與傳遞 10 項能力 / LTS 支援

實驗性19%

Beta 版79%

Beta 版79%

[頻道路由](</zh-TW/channels/channel-routing>), [群組](</zh-TW/channels/groups>), [Discord](</zh-TW/channels/discord>), [Matrix](</zh-TW/channels/matrix>), [疑難排解](</zh-TW/channels/troubleshooting>), [設定參考](</zh-TW/gateway/configuration-reference>)

狀態健康與操作者控制 4 項能力 / LTS 支援

實驗性0%

Beta 版79%

Beta79%

[健康狀態](</zh-TW/gateway/health>), [設定參考](</zh-TW/gateway/configuration-reference>), [疑難排解](</zh-TW/channels/troubleshooting>), [Discord](</zh-TW/channels/discord>)

可觀測性 - M3 Beta - 5 個領域

OTel、Prometheus、記錄與診斷文件已存在。需要一次公開的「維運人員應先查看什麼」成熟度修訂。

涵蓋率實驗性 - 18%品質 Beta - 75%完整性 Beta - 79%部分 - 3

健康狀態與修復 12 項能力 / LTS 支援

實驗性28%

Beta79%

Beta79%

[健康狀態](</zh-TW/gateway/health>), [Telegram](</zh-TW/channels/telegram>), [Doctor](</zh-TW/cli/doctor>), [Doctor](</zh-TW/gateway/doctor>), [SDK 子路徑](</zh-TW/plugins/sdk-subpaths>), [健康狀態](</zh-TW/cli/health>), [協定](</zh-TW/gateway/protocol>)

記錄 5 項能力 / LTS 支援

實驗性0%

Alpha68%

Beta79%

[記錄](</zh-TW/logging>), [記錄](</zh-TW/gateway/logging>), [紀錄](</zh-TW/cli/logs>)

診斷收集 8 項能力

實驗性30%

Beta79%

Beta79%

[診斷](</zh-TW/gateway/diagnostics>), [健康狀態](</zh-TW/gateway/health>), [Codex Harness](</zh-TW/plugins/codex-harness>), [協定](</zh-TW/gateway/protocol>)

遙測匯出 13 項能力

實驗性33%

Beta79%

Beta79%

[鉤子](</zh-TW/plugins/hooks>), [OpenTelemetry](</zh-TW/gateway/opentelemetry>), [記錄](</zh-TW/logging>), [SDK 子路徑](</zh-TW/plugins/sdk-subpaths>), [Diagnostics Otel](</zh-TW/plugins/reference/diagnostics-otel>), [Prometheus](</zh-TW/gateway/prometheus>), [Diagnostics Prometheus](</zh-TW/plugins/reference/diagnostics-prometheus>)

工作階段診斷 4 項能力 / LTS 支援

實驗性0%

Alpha68%

Beta79%

[OpenTelemetry](</zh-TW/gateway/opentelemetry>), [Prometheus](</zh-TW/gateway/prometheus>), [診斷](</zh-TW/gateway/diagnostics>), [協定](</zh-TW/gateway/protocol>)

閘道 Web App - M3 Beta - 6 個領域

Web UI 已記錄配對、聊天、PWA、Talk、推送與遠端閘道流程。完成跨瀏覽器與行動 PWA 評分卡後再升級。

涵蓋率實驗性 - 4%品質 Beta - 74%完整性 Beta - 79%無

瀏覽器即時通話 5 項能力

實驗性0%

Alpha 版68%

Beta 版79%

[控制介面](</zh-TW/web/control-ui>), [協定](</zh-TW/gateway/protocol>), [通話](</zh-TW/nodes/talk>)

瀏覽器存取與信任 5 項能力

實驗性0%

Alpha 版68%

Beta 版79%

[控制介面](</zh-TW/web/control-ui>), [儀表板](</zh-TW/web/dashboard>), [Tailscale](</zh-TW/gateway/tailscale>), [遠端](</zh-TW/gateway/remote>)

設定 5 項能力

實驗性0%

Alpha 版68%

Beta 版79%

[控制介面](</zh-TW/web/control-ui>), [設定](</zh-TW/gateway/configuration>)

瀏覽器使用者介面 10 項能力

實驗性8%

Beta 版79%

Beta 版79%

[控制介面](</zh-TW/web/control-ui>), [索引](</zh-TW/web>), [儀表板](</zh-TW/web/dashboard>), [協定](</zh-TW/gateway/protocol>)

網頁聊天對話 15 項能力

實驗性10%

Beta 版79%

Beta 版79%

[控制介面](</zh-TW/web/control-ui>), [網頁聊天](</zh-TW/web/webchat>), [開始使用](</zh-TW/start/getting-started>), [頻道路由](</zh-TW/channels/channel-routing>), [安全檔案操作](</zh-TW/gateway/security/secure-file-operations>)

操作員主控台 10 項能力

實驗性8%

Beta 版79%

Beta 版79%

[控制介面](</zh-TW/web/control-ui>), [健康狀態](</zh-TW/gateway/health>), [協定](</zh-TW/gateway/protocol>), [儀表板](</zh-TW/web/dashboard>)

外掛 - M3 Beta 版 - 9 個區域

在資訊清單、探索、載入、提供者／工具架構與核准邊界方面，已有廣泛文件與強大的內部執行階段證據。請將此列維持在 Beta 版，直到公開 SDK API／子路徑與外部分發證據更強為止。

涵蓋範圍 實驗性 - 12%品質 Beta 版 - 72%完整度 Beta 版 - 79%部分 - 7

撰寫與封裝外掛 8 項能力 / LTS 支援

實驗性0%

Alpha 版68%

Beta 版79%

[建置外掛](</zh-TW/plugins/building-plugins>), [SDK 概觀](</zh-TW/plugins/sdk-overview>), [SDK 進入點](</zh-TW/plugins/sdk-entrypoints>), [SDK 子路徑](</zh-TW/plugins/sdk-subpaths>), [Manifest](</zh-TW/plugins/manifest>), [參考資料](</zh-TW/plugins/reference>)

內建外掛 5 項能力 / LTS 支援

實驗性0%

Alpha 版68%

Beta 版79%

[外掛清單](</zh-TW/plugins/plugin-inventory>), [外掛](</zh-TW/cli/plugins>), [架構內部](</zh-TW/plugins/architecture-internals>)

畫布外掛 6 項能力

實驗性0%

Alpha 版68%

Beta 版79%

[畫布](</zh-TW/plugins/reference/canvas>), [畫布](</zh-TW/refactor/canvas>), [設定參考資料](</zh-TW/gateway/configuration-reference>)

安裝與執行外掛 6 項能力 / LTS 支援

實驗性35%

Beta 版79%

Beta 版79%

[架構](</zh-TW/plugins/architecture>), [架構內部](</zh-TW/plugins/architecture-internals>), [外掛](</zh-TW/cli/plugins>)

頻道外掛 5 項能力 / LTS 支援

實驗性0%

Alpha 版68%

Beta 版79%

[SDK 頻道外掛](</zh-TW/plugins/sdk-channel-plugins>), [SDK 頻道入站](</zh-TW/plugins/sdk-channel-inbound>), [SDK 頻道出站](</zh-TW/plugins/sdk-channel-outbound>)

供應商與工具外掛 6 項能力 / LTS 支援

實驗性43%

Beta 版79%

Beta 版79%

[SDK 供應商外掛](</zh-TW/plugins/sdk-provider-plugins>), [工具外掛](</zh-TW/plugins/tool-plugins>), [新增能力](</zh-TW/plugins/adding-capabilities>)

外掛核准 6 項能力 / LTS 支援

實驗性0%

Alpha 版68%

Beta 版79%

[外掛權限請求](</zh-TW/plugins/plugin-permission-requests>), [Exec 核准](</zh-TW/tools/exec-approvals>), [SDK 頻道外掛](</zh-TW/plugins/sdk-channel-plugins>)

發布外掛 6 項能力 / LTS 支援

實驗性0%

Alpha 版68%

Beta79%

[外掛](</zh-TW/cli/plugins>), [相容性](</zh-TW/plugins/compatibility>), [發布](</zh-TW/clawhub/publishing>)

測試外掛 6 項能力

實驗性27%

Beta79%

Beta79%

[SDK 測試](</zh-TW/plugins/sdk-testing>), [SDK 設定](</zh-TW/plugins/sdk-setup>), [Codex Harness](</zh-TW/plugins/codex-harness>)

安全性、驗證、配對與祕密 - M3 Beta - 6 個領域

已有良好的文件與強化介面。等定期升級與安全性情境執行證明沒有設定回歸後再提升。

覆蓋率 實驗性 - 16%品質 Beta 版 - 72%完整性 Beta 版 - 79%部分 - 5

核准政策與工具防護措施 2 項能力 / LTS 支援

Alpha 版50%

Beta 版79%

Beta 版79%

[執行核准](</zh-TW/tools/exec-approvals>), [核准](</zh-TW/cli/approvals>), [外掛權限請求](</zh-TW/plugins/plugin-permission-requests>), [稽核檢查](</zh-TW/gateway/security/audit-checks>)

閘道驗證與遠端存取 9 項能力 / LTS 支援

實驗性0%

Alpha 版68%

Beta 版79%

[索引](</zh-TW/gateway/security>), [曝露作業手冊](</zh-TW/gateway/security/exposure-runbook>), [受信任代理驗證](</zh-TW/gateway/trusted-proxy-auth>), [Tailscale](</zh-TW/gateway/tailscale>), [遠端](</zh-TW/gateway/remote>), [設定參考](</zh-TW/gateway/configuration-reference>), [閘道](</zh-TW/cli/gateway>), [Doctor](</zh-TW/cli/doctor>), [控制 UI](</zh-TW/web/control-ui>), [瀏覽器控制](</zh-TW/tools/browser-control>), [稽核檢查](</zh-TW/gateway/security/audit-checks>)

頻道存取控制 3 項能力 / LTS 支援

實驗性0%

Alpha 版68%

Beta 版79%

[配對](</zh-TW/channels/pairing>), [Telegram](</zh-TW/channels/telegram>), [存取群組](</zh-TW/channels/access-groups>), [稽核檢查](</zh-TW/gateway/security/audit-checks>)

裝置與節點配對 11 項能力 / LTS 支援

實驗性0%

Alpha 版68%

Beta 版79%

[協定](</zh-TW/gateway/protocol>), [裝置](</zh-TW/cli/devices>), [配對](</zh-TW/channels/pairing>), [配對](</zh-TW/gateway/pairing>), [操作者範圍](</zh-TW/gateway/operator-scopes>), [控制 UI](</zh-TW/web/control-ui>), [網頁聊天](</zh-TW/web/webchat>), [核准](</zh-TW/cli/approvals>)

外掛信任 2 項能力

實驗性0%

Alpha 版68%

Beta 版79%

[Manifest](</zh-TW/plugins/manifest>), [外掛權限請求](</zh-TW/plugins/plugin-permission-requests>), [管理外掛](</zh-TW/plugins/manage-plugins>), [稽核檢查](</zh-TW/gateway/security/audit-checks>)

憑證與祕密衛生 5 項能力 / LTS 支援

實驗性46%

Beta 版79%

Beta 版79%

[驗證](</zh-TW/gateway/authentication>), [模型](</zh-TW/cli/models>), [Openai](</zh-TW/providers/openai>), [Oauth](</zh-TW/concepts/oauth>), [祕密](</zh-TW/gateway/secrets>), [祕密](</zh-TW/cli/secrets>), [Secretref 憑證介面](</zh-TW/reference/secretref-credential-surface>), [稽核檢查](</zh-TW/gateway/security/audit-checks>)

自動化：排程、鉤子、工作、輪詢 - M3 Beta - 6 個領域

已有文件且可使用，但情境證明應涵蓋無人值守傳遞、重試與失敗可見性。

覆蓋率 實驗性 - 2%品質 Beta 版 - 72%完整性 Beta 版 - 79%無

排程工作 15 項能力

實驗性0%

Beta79%

Beta79%

[排程工作](</zh-TW/automation/cron-jobs>), [排程](</zh-TW/cli/cron>), [協定](</zh-TW/gateway/protocol>), [任務](</zh-TW/automation/tasks>), [Discord](</zh-TW/channels/discord>)

事件進入 15 項能力

實驗性0%

Alpha68%

Beta79%

[Telegram](</zh-TW/channels/telegram>), [Zalo](</zh-TW/channels/zalo>), [疑難排解](</zh-TW/channels/troubleshooting>), [來自 Bluebubbles 的 iMessage](</zh-TW/channels/imessage-from-bluebubbles>), [Gmail Pubsub 整合](</zh-TW/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pubsub](</zh-TW/automation/cron-jobs>), [網路鉤子](</zh-TW/cli/webhooks>), [網路鉤子](</zh-TW/automation/cron-jobs#webhooks>), [網路鉤子](</zh-TW/automation/cron-jobs>)

自動化掛鉤 11 項能力

實驗性0%

Alpha68%

Beta79%

[掛鉤](</zh-TW/automation/hooks>), [掛鉤](</zh-TW/cli/hooks>), [掛鉤](</zh-TW/plugins/hooks>), [外掛權限請求](</zh-TW/plugins/plugin-permission-requests>), [SDK 子路徑](</zh-TW/plugins/sdk-subpaths>)

背景任務與流程 10 項能力

實驗性0%

Alpha68%

Beta79%

[任務](</zh-TW/automation/tasks>), [索引](</zh-TW/automation>), [任務](</zh-TW/cli/tasks>), [TaskFlow](</zh-TW/automation/taskflow>), [SDK 執行階段](</zh-TW/plugins/sdk-runtime>)

心跳偵測 5 項能力

實驗性14%

Beta79%

Beta79%

[索引](</zh-TW/automation>), [心跳偵測](</zh-TW/gateway/heartbeat>), [承諾事項](</zh-TW/concepts/commitments>)

輪詢控制 10 項能力

實驗性0%

Alpha68%

Beta79%

[輪詢](</zh-TW/cli/message>), [訊息](</zh-TW/cli/message>), [Telegram](</zh-TW/channels/telegram>), [Microsoft Teams](</zh-TW/channels/msteams>), [背景程序](</zh-TW/gateway/background-process>)

媒體理解與媒體生成 - M2 Alpha - 6 個領域

廣泛的能力表面已存在，但提供者差異、檔案限制，以及節點/應用程式一致性使其尚未穩定。

涵蓋範圍 實驗性 - 2%品質 Alpha - 64%完整度 Alpha - 68%無

媒體匯入與存取 8 項能力

實驗性0%

Alpha61%

Alpha68%

[媒體概覽](</zh-TW/tools/media-overview>), [媒體理解](</zh-TW/nodes/media-understanding>), [安全檔案操作](</zh-TW/gateway/security/secure-file-operations>), [Pdf](</zh-TW/tools/pdf>), [影像生成](</zh-TW/tools/image-generation>), [Qr](</zh-TW/cli/qr>), [LINE](</zh-TW/channels/line>), [WhatsApp](</zh-TW/channels/whatsapp>)

頻道媒體處理 5 項能力

實驗性0%

Alpha61%

Alpha68%

[影像](</zh-TW/nodes/images>), [媒體概覽](</zh-TW/tools/media-overview>), [Discord](</zh-TW/channels/discord>)

媒體設定 1 項能力

實驗性0%

Alpha61%

Alpha68%

[媒體概覽](</zh-TW/tools/media-overview>), [影像生成](</zh-TW/tools/image-generation>), [資訊清單](</zh-TW/plugins/manifest>), [Codex Harness](</zh-TW/plugins/codex-harness>)

文字轉語音傳遞 2 項能力

實驗性0%

Alpha61%

Alpha68%

[Tts](</zh-TW/tools/tts>), [媒體概覽](</zh-TW/tools/media-overview>), [Discord](</zh-TW/channels/discord>)

媒體理解 12 項能力

實驗性7%

Alpha69%

Alpha69%

[音訊](</zh-TW/nodes/audio>), [媒體理解](</zh-TW/nodes/media-understanding>), [媒體概覽](</zh-TW/tools/media-overview>), [WhatsApp](</zh-TW/channels/whatsapp>), [影像](</zh-TW/nodes/images>), [推論](</zh-TW/cli/infer>), [Pdf](</zh-TW/tools/pdf>)

媒體生成 17 項能力

實驗性5%

Alpha69%

Alpha69%

[影像生成](</zh-TW/tools/image-generation>), [媒體概覽](</zh-TW/tools/media-overview>), [Skills](</zh-TW/tools/skills>), [音樂生成](</zh-TW/tools/music-generation>), [影片生成](</zh-TW/tools/video-generation>)

語音與即時對話 - M2 Alpha - 6 個領域

Control UI、應用程式與提供者之間存在多種實作。進入 beta 前需要延遲、失敗模式與設定評分卡。

涵蓋範圍 實驗性 - 0%品質 Alpha - 61%完整度 Alpha - 68%無

對話提供者 7 項能力

實驗性0%

Alpha61%

Alpha68%

[Openai](</zh-TW/providers/openai>), [Google](</zh-TW/providers/google>), [Sdk 提供者外掛](</zh-TW/plugins/sdk-provider-plugins>), [對話](</zh-TW/nodes/talk>), [控制介面](</zh-TW/web/control-ui>)

即時對話工作階段 11 項能力

實驗性0%

Alpha61%

Alpha68%

[對話](</zh-TW/nodes/talk>), [控制介面](</zh-TW/web/control-ui>)

語音與轉錄 5 項能力

實驗性0%

Alpha61%

Alpha68%

[對話](</zh-TW/nodes/talk>), [Openai](</zh-TW/providers/openai>), [Google](</zh-TW/providers/google>)

原生應用程式對話 4 項能力

實驗性0%

Alpha61%

Alpha68%

[對話](</zh-TW/nodes/talk>), [Voicewake](</zh-TW/platforms/mac/voicewake>)

語音喚醒與路由 4 項能力

實驗性0%

Alpha61%

Alpha68%

[Voicewake](</zh-TW/nodes/voicewake>), [Voicewake](</zh-TW/platforms/mac/voicewake>), [語音覆疊](</zh-TW/platforms/mac/voice-overlay>)

對話可觀測性 5 項能力

實驗性0%

Alpha61%

Alpha68%

[控制介面](</zh-TW/web/control-ui>), [語音覆疊](</zh-TW/platforms/mac/voice-overlay>), [對話](</zh-TW/nodes/talk>)

終端介面 - M2 Alpha - 5 個範圍

存在於文件與原始碼中，但作為主要使用者工作流程較不明顯。需要明確的情境定義。

涵蓋率 實驗性 - 0%品質 Alpha - 59%完整度 Alpha - 66%無

執行階段模式 14 項能力

實驗性0%

Alpha59%

Alpha66%

[終端介面](</zh-TW/cli/tui>), [終端介面](</zh-TW/web/tui>), [索引](</zh-TW/cli>)

輸入與命令 8 項能力

實驗性0%

Alpha59%

Alpha66%

[終端介面](</zh-TW/web/tui>)

工作階段管理 3 項能力

實驗性0%

Alpha59%

Alpha66%

[終端介面](</zh-TW/web/tui>), [工作階段](</zh-TW/cli/sessions>)

本機 Shell 執行 4 項能力

實驗性0%

Alpha59%

Alpha66%

[終端介面](</zh-TW/web/tui>), [終端介面](</zh-TW/cli/tui>)

算繪與輸出安全性 4 項能力

實驗性0%

Alpha59%

Alpha66%

[終端介面](</zh-TW/web/tui>), [QR](</zh-TW/cli/qr>), [記錄](</zh-TW/cli/logs>), [補全](</zh-TW/cli/completion>)

ClawHub - M2 Alpha - 4 個範圍

公開文件與生態系概念已存在。需要安裝、信任、更新、復原與相容性評分表。

覆蓋率 實驗性 - 0%品質 Alpha - 58%完整度 Alpha - 62%無

發布 7 項能力

實驗性0%

Alpha54%

Alpha55%

[發布](</zh-TW/clawhub/publishing>), [建立 Skills](</zh-TW/tools/creating-skills>), [社群](</zh-TW/plugins/community>)

目錄探索 5 項能力

實驗性0%

Alpha61%

Alpha68%

[外掛](</zh-TW/tools/plugin>), [外掛](</zh-TW/cli/plugins>), [Skills](</zh-TW/cli/skills>), [Skills](</zh-TW/tools/skills>), [社群](</zh-TW/plugins/community>)

相容性與信任 12 項能力

實驗性0%

Alpha55%

Alpha56%

[外掛](</zh-TW/tools/plugin>), [外掛](</zh-TW/cli/plugins>), [相容性](</zh-TW/plugins/compatibility>), [外掛清單](</zh-TW/plugins/plugin-inventory>), [發布](</zh-TW/clawhub/publishing>), [Skills](</zh-TW/tools/skills>), [Skills 設定](</zh-TW/tools/skills-config>)

外掛生命週期與健康狀態 26 項能力

實驗性0%

Alpha61%

Alpha68%

[外掛](</zh-TW/tools/plugin>), [外掛](</zh-TW/cli/plugins>), [Skills](</zh-TW/cli/skills>), [Skills](</zh-TW/tools/skills>), [協定](</zh-TW/gateway/protocol>), [套件組合](</zh-TW/plugins/bundles>), [依賴解析](</zh-TW/plugins/dependency-resolution>)

OpenClaw App SDK - M2 Alpha - 6 個領域

OpenClaw App SDK 是獨立的外部應用程式合約，與 Gateway 執行階段和外掛 SDK 分開。目前評分顯示已有實際的 `@openclaw/sdk` 路徑，但在公開封裝、自動探索、核准、輔助工具與相容性方面仍有缺口。

涵蓋範圍 實驗性 - 3%品質 Alpha - 54%完整性 Alpha - 53%無

用戶端 API 4 項能力

實驗性0%

Alpha51%

Alpha50%

[OpenClaw SDK](</zh-TW/gateway/external-apps>), [OpenClaw SDK API 設計](</zh-TW/gateway/external-apps>)

閘道存取 5 項能力

實驗性0%

Alpha53%

Alpha54%

[OpenClaw SDK](</zh-TW/gateway/external-apps>), [OpenClaw SDK API 設計](</zh-TW/gateway/external-apps>), [通訊協定](</zh-TW/gateway/protocol>), [索引](</zh-TW/gateway/security>)

代理對話 6 項能力

實驗性0%

Alpha52%

Alpha52%

[OpenClaw SDK](</zh-TW/gateway/external-apps>), [OpenClaw SDK API 設計](</zh-TW/gateway/external-apps>), [通訊協定](</zh-TW/gateway/protocol>)

事件與核准 5 項能力

實驗性0%

Alpha52%

Alpha52%

[OpenClaw SDK](</zh-TW/gateway/external-apps>), [OpenClaw SDK API 設計](</zh-TW/gateway/external-apps>), [通訊協定](</zh-TW/gateway/protocol>)

資源輔助工具 5 項能力

實驗性17%

Alpha62%

Alpha53%

[OpenClaw SDK](</zh-TW/gateway/external-apps>), [OpenClaw SDK API 設計](</zh-TW/gateway/external-apps>)

相容性 5 項能力

實驗性0%

Alpha54%

Alpha55%

[OpenClaw SDK API 設計](</zh-TW/gateway/external-apps>), [Typebox](</zh-TW/concepts/typebox>), [通訊協定](</zh-TW/gateway/protocol>)

### 平台

Linux 閘道主機 - M4 穩定版 - 5 個領域

建議使用節點執行階段，已記錄 systemd 使用者服務，且 VPS/容器指引涵蓋範圍廣泛。

涵蓋範圍：實驗性 - 0%品質：Beta - 75%完整性：穩定版 - 89%部分 - 4

主機設定與更新 4 項能力 / LTS 支援

實驗性0%

Beta75%

穩定版89%

[索引](</zh-TW/install>), [更新](</zh-TW/install/updating>), [Linux](</zh-TW/platforms/linux>), [索引](</zh-TW/platforms>)

閘道執行階段與服務控制 6 項能力 / LTS 支援

實驗性0%

Beta75%

穩定版89%

[索引](</zh-TW/gateway>), [閘道](</zh-TW/cli/gateway>), [Linux](</zh-TW/platforms/linux>), [Vps](</zh-TW/vps>)

遠端存取與安全性 6 項能力 / LTS 支援

實驗性0%

Beta75%

穩定版89%

[遠端](</zh-TW/gateway/remote>), [Tailscale](</zh-TW/gateway/tailscale>), [暴露執行手冊](</zh-TW/gateway/security/exposure-runbook>), [驗證](</zh-TW/gateway/authentication>), [祕密](</zh-TW/gateway/secrets>)

診斷與修復 4 項能力 / LTS 支援

實驗性0%

Beta75%

穩定版89%

[狀態](</zh-TW/cli/status>), [日誌](</zh-TW/cli/logs>), [Doctor](</zh-TW/cli/doctor>), [診斷](</zh-TW/gateway/diagnostics>), [索引](</zh-TW/gateway>)

部署目標 3 項能力

實驗性0%

Beta75%

穩定版89%

[Vps](</zh-TW/vps>), [Docker](</zh-TW/install/docker>), [Hetzner](</zh-TW/install/hetzner>), [Digitalocean](</zh-TW/install/digitalocean>), [Kubernetes](</zh-TW/install/kubernetes>), [Podman](</zh-TW/install/podman>)

macOS 閘道主機 - M4 穩定版 - 7 個領域

LaunchAgent 服務路徑、本機/遠端閘道模式、命令列介面安裝，以及應用程式整合皆已有文件說明。

涵蓋範圍 實驗性 - 0%品質 Beta - 74%完整性 穩定版 - 88%無

命令列介面設定 4 項能力

實驗性0%

Beta74%

穩定版88%

[Macos](</zh-TW/platforms/macos>), [內建閘道](</zh-TW/platforms/mac/bundled-gateway>), [安裝程式](</zh-TW/install/installer>), [節點](</zh-TW/install/node>)

本機閘道整合 9 項能力

實驗性0%

Beta74%

穩定版88%

[Macos](</zh-TW/platforms/macos>), [內建閘道](</zh-TW/platforms/mac/bundled-gateway>), [遠端](</zh-TW/platforms/mac/remote>), [索引](</zh-TW/gateway>), [閘道](</zh-TW/cli/gateway>), [Bonjour](</zh-TW/gateway/bonjour>)

遠端閘道模式 5 項能力

實驗性0%

Beta74%

穩定版88%

[遠端](</zh-TW/platforms/mac/remote>), [遠端](</zh-TW/gateway/remote>), [Tailscale](</zh-TW/gateway/tailscale>)

閘道服務生命週期 10 項能力

實驗性0%

Beta74%

穩定版88%

[Macos](</zh-TW/platforms/macos>), [內建閘道](</zh-TW/platforms/mac/bundled-gateway>), [閘道](</zh-TW/cli/gateway>), [索引](</zh-TW/gateway>), [更新](</zh-TW/cli/update>), [更新中](</zh-TW/install/updating>), [解除安裝](</zh-TW/install/uninstall>), [疑難排解](</zh-TW/gateway/troubleshooting>)

診斷與可觀測性 4 項能力

實驗性0%

Beta74%

穩定版88%

[內建閘道](</zh-TW/platforms/mac/bundled-gateway>), [Macos](</zh-TW/platforms/macos>), [閘道](</zh-TW/cli/gateway>), [Doctor](</zh-TW/gateway/doctor>), [疑難排解](</zh-TW/gateway/troubleshooting>)

權限與原生能力 4 項能力

實驗性0%

Beta74%

穩定版88%

[Macos](</zh-TW/platforms/macos>), [遠端](</zh-TW/platforms/mac/remote>)

設定檔與隔離 5 項能力

實驗性0%

Beta74%

穩定版88%

[多重閘道](</zh-TW/gateway/multiple-gateways>), [索引](</zh-TW/gateway>), [閘道](</zh-TW/cli/gateway>)

Docker 與 Podman 託管 - M3 Beta - 4 個領域

安裝文件已存在，且是常見的部署路徑。在週期性發布煙霧測試涵蓋升級與磁碟區行為後再提升成熟度。

涵蓋範圍 實驗性 - 7%品質 Beta - 71%完整度 Beta - 79%無

容器設定 6 項能力

實驗性0%

Alpha68%

Beta79%

[Docker](</zh-TW/install/docker>), [Podman](</zh-TW/install/podman>)

容器操作 11 項能力

實驗性0%

Alpha68%

Beta79%

[Podman](</zh-TW/install/podman>), [Docker VM 執行階段](</zh-TW/install/docker-vm-runtime>), [Docker](</zh-TW/install/docker>), [Hetzner](</zh-TW/install/hetzner>), [Hostinger](</zh-TW/install/hostinger>)

映像檔發布與驗證 5 項能力

實驗性29%

Beta79%

Beta79%

[Docker](</zh-TW/install/docker>), [Docker VM 執行階段](</zh-TW/install/docker-vm-runtime>), [完整發布驗證](</zh-TW/reference/full-release-validation>)

代理程式沙箱與工具 3 項能力

實驗性0%

Alpha68%

Beta79%

[Docker](</zh-TW/install/docker>), [Docker VM 執行階段](</zh-TW/install/docker-vm-runtime>)

透過 WSL2 使用 Windows - M3 Beta - 6 個領域

建議的 Windows 路徑，包含 systemd/使用者服務指引與啟動鏈文件。經過重複安裝/更新評分卡驗證後再推進。

涵蓋範圍 實驗性 - 6%品質 Alpha - 69%完整性 Beta - 79%部分 - 5

WSL 設定 6 項能力 / LTS 支援

實驗性0%

Alpha 版67%

Beta 版79%

[Windows](</zh-TW/platforms/windows>), [入門](</zh-TW/start/getting-started>)

命令列介面 8 項能力 / LTS 支援

實驗性0%

Alpha 版67%

Beta 版79%

[Windows](</zh-TW/platforms/windows>), [入門](</zh-TW/start/getting-started>), [更新](</zh-TW/install/updating>), [初始設定](</zh-TW/cli/onboard>), [診斷](</zh-TW/cli/doctor>), [狀態](</zh-TW/cli/status>), [日誌](</zh-TW/cli/logs>)

閘道服務生命週期 10 項能力 / LTS 支援

實驗性0%

Alpha 版67%

Beta 版79%

[Windows](</zh-TW/platforms/windows>), [索引](</zh-TW/gateway>), [診斷](</zh-TW/gateway/doctor>)

閘道存取與暴露 11 項能力 / LTS 支援

實驗性0%

Alpha 版67%

Beta 版79%

[身分驗證](</zh-TW/gateway/authentication>), [密鑰](</zh-TW/gateway/secrets>), [遠端](</zh-TW/gateway/remote>), [暴露操作手冊](</zh-TW/gateway/security/exposure-runbook>), [Windows](</zh-TW/platforms/windows>)

診斷與修復 6 項能力 / LTS 支援

實驗性38%

Beta 版79%

Beta 版79%

[Windows](</zh-TW/platforms/windows>), [狀態](</zh-TW/cli/status>), [日誌](</zh-TW/cli/logs>), [診斷](</zh-TW/cli/doctor>), [診斷](</zh-TW/gateway/doctor>)

瀏覽器與控制介面 6 項能力

實驗性0%

Alpha 版67%

Beta 版79%

[瀏覽器 WSL2 Windows 遠端 CDP 疑難排解](</zh-TW/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [瀏覽器](</zh-TW/tools/browser>), [控制介面](</zh-TW/web/control-ui>)

Raspberry Pi 與小型 Linux 裝置 - M3 Beta 版 - 4 個範圍

平台文件已存在，且閘道路徑以 Linux 為基礎。需要硬體特定的發行 smoke proof 才能提升成熟度。

覆蓋率 實驗性 - 0%品質 Alpha 版 - 67%完整性 Beta 版 - 79%無

設定與相容性 12 項能力

實驗性0%

Alpha67%

Beta79%

[Raspberry Pi](</zh-TW/install/raspberry-pi>), [索引](</zh-TW/install>), [首次執行常見問題](</zh-TW/help/faq-first-run>), [常見問題](</zh-TW/help/faq>), [Linux](</zh-TW/platforms/linux>), [安裝程式](</zh-TW/install/installer>)

遠端存取與驗證 9 項能力

實驗性0%

Alpha67%

Beta79%

[Raspberry Pi](</zh-TW/install/raspberry-pi>), [驗證](</zh-TW/gateway/authentication>), [祕密](</zh-TW/gateway/secrets>), [配對](</zh-TW/gateway/pairing>), [裝置](</zh-TW/cli/devices>), [遠端](</zh-TW/gateway/remote>), [Tailscale](</zh-TW/gateway/tailscale>)

閘道執行環境 10 項能力

實驗性0%

Alpha67%

Beta79%

[索引](</zh-TW/gateway>), [閘道](</zh-TW/cli/gateway>), [Raspberry Pi](</zh-TW/install/raspberry-pi>), [Linux](</zh-TW/platforms/linux>), [Vps](</zh-TW/vps>)

效能與診斷 5 項能力

實驗性0%

Alpha67%

Beta79%

[Raspberry Pi](</zh-TW/install/raspberry-pi>), [Linux](</zh-TW/platforms/linux>), [健康狀態](</zh-TW/gateway/health>), [診斷](</zh-TW/gateway/diagnostics>)

macOS companion app - M3 Beta - 8 個領域

功能完整的選單列應用程式、權限、節點模式、Canvas、語音喚醒、WebChat 與遠端模式皆已存在。仍然變動夠快，因此避免列為穩定版。

涵蓋範圍 實驗性 - 0%品質 Alpha - 66%完整度 Beta - 78%無

畫布 4 項能力

實驗性0%

Alpha 版66%

Beta 版78%

[畫布](</zh-TW/platforms/mac/canvas>), [macOS](</zh-TW/platforms/macos>), [網頁聊天](</zh-TW/web/webchat>)

本機設定 7 項能力

實驗性0%

Alpha 版66%

Beta 版78%

[內建閘道](</zh-TW/platforms/mac/bundled-gateway>), [macOS](</zh-TW/platforms/macos>), [子程序](</zh-TW/platforms/mac/child-process>), [開發設定](</zh-TW/platforms/mac/dev-setup>)

狀態與設定 5 項能力

實驗性0%

Alpha 版66%

Beta 版78%

[選單列](</zh-TW/platforms/mac/menu-bar>), [圖示](</zh-TW/platforms/mac/icon>), [macOS](</zh-TW/platforms/macos>), [健康狀態](</zh-TW/platforms/mac/health>), [記錄](</zh-TW/platforms/mac/logging>), [遠端](</zh-TW/platforms/mac/remote>)

原生能力 5 項能力

實驗性0%

Alpha 版66%

Beta 版78%

[macOS](</zh-TW/platforms/macos>), [XPC](</zh-TW/platforms/mac/xpc>), [權限](</zh-TW/platforms/mac/permissions>), [簽署](</zh-TW/platforms/mac/signing>), [Peekaboo](</zh-TW/platforms/mac/peekaboo>)

遠端連線 3 項能力

實驗性0%

Alpha 版66%

Beta 版78%

[遠端](</zh-TW/platforms/mac/remote>), [macOS](</zh-TW/platforms/macos>), [遠端](</zh-TW/gateway/remote>)

語音與對話 3 項能力

實驗性0%

Alpha 版66%

Beta 版78%

[Voicewake](</zh-TW/platforms/mac/voicewake>), [語音覆蓋層](</zh-TW/platforms/mac/voice-overlay>), [對話](</zh-TW/nodes/talk>), [macOS](</zh-TW/platforms/macos>)

網頁聊天 3 項能力

實驗性0%

Alpha 版66%

Beta 版78%

[網頁聊天](</zh-TW/platforms/mac/webchat>), [macOS](</zh-TW/platforms/macos>), [網頁聊天](</zh-TW/web/webchat>)

遠端網頁聊天 5 項能力

實驗性0%

Alpha 版66%

Beta 版78%

[網頁聊天](</zh-TW/platforms/mac/webchat>), [遠端](</zh-TW/gateway/remote>), [遠端](</zh-TW/platforms/mac/remote>)

Android app - M2 Alpha - 7 areas

公開的 Google Play 路徑已存在，但應用程式文件仍將重建描述為極早期 Alpha，並指出發行強化工作。

覆蓋範圍 實驗性 - 0%品質 Alpha - 59%完整度 Alpha - 66%無

媒體擷取 1 項能力

實驗性0%

Alpha 版59%

Alpha 版66%

[Android](</zh-TW/platforms/android>), [攝影機](</zh-TW/nodes/camera>)

行動聊天 1 項能力

實驗性0%

Alpha 版59%

Alpha 版66%

[Android](</zh-TW/platforms/android>)

連線設定 1 項能力

實驗性0%

Alpha 版59%

Alpha 版66%

[Android](</zh-TW/platforms/android>), [Bonjour](</zh-TW/gateway/bonjour>), [配對](</zh-TW/gateway/pairing>)

發佈 3 項能力

實驗性0%

Alpha 版59%

Alpha 版66%

[Android](</zh-TW/platforms/android>)

設定 1 項能力

實驗性0%

Alpha 版59%

Alpha 版66%

[Android](</zh-TW/platforms/android>)

語音 1 項能力

實驗性0%

Alpha 版59%

Alpha 版66%

[Android](</zh-TW/platforms/android>), [對話](</zh-TW/nodes/talk>)

裝置執行環境 2 項能力

實驗性0%

Alpha 版59%

Alpha 版66%

[Android](</zh-TW/platforms/android>), [疑難排解](</zh-TW/nodes/troubleshooting>), [協定](</zh-TW/gateway/protocol>)

原生 Windows - M2 Alpha 版 - 4 個領域

核心命令列介面/閘道流程可運作，但文件仍建議使用 WSL2 以取得完整體驗，並列出原生環境的注意事項。

覆蓋率 實驗性 - 0%品質 Alpha 版 - 58%完整度 Alpha 版 - 66%部分 - 1

命令列介面 9 項能力 / LTS 支援

實驗性0%

Alpha54%

Alpha64%

[索引](</zh-TW/install>), [安裝程式](</zh-TW/install/installer>), [Windows](</zh-TW/platforms/windows>), [開始使用](</zh-TW/start/getting-started>), [Onboard](</zh-TW/cli/onboard>)

閘道管理 11 項能力

實驗性0%

Alpha59%

Alpha66%

[Windows](</zh-TW/platforms/windows>), [索引](</zh-TW/gateway>), [閘道](</zh-TW/cli/gateway>), [Doctor](</zh-TW/cli/doctor>)

網路 4 項能力

實驗性0%

Alpha59%

Alpha66%

[Windows](</zh-TW/platforms/windows>), [索引](</zh-TW/gateway>), [閘道](</zh-TW/cli/gateway>)

更新 4 項能力

實驗性0%

Alpha59%

Alpha66%

[更新](</zh-TW/install/updating>), [CI](</zh-TW/ci>)

Kubernetes 託管 - M2 Alpha - 4 個領域

Kubernetes 託管是一條獨立、以 Kustomize 為基礎的叢集部署路徑。目前評分顯示已有真正的最小部署路徑，但在 Kubernetes 專用 CI、ingress/TLS/NetworkPolicy 封裝、備份/還原，以及生產環境暴露面的強化方面仍有缺口。

涵蓋率實驗性 - 0%品質 Alpha - 55%完整性 Alpha - 61%無

部署設定 5 項功能

實驗性0%

Alpha55%

Alpha61%

[Kubernetes](</zh-TW/install/kubernetes>), [索引](</zh-TW/install>)

設定與秘密 5 項功能

實驗性0%

Alpha55%

Alpha61%

[Kubernetes](</zh-TW/install/kubernetes>), [秘密](</zh-TW/gateway/secrets>), [環境](</zh-TW/help/environment>)

存取與暴露 5 項功能

實驗性0%

Alpha55%

Alpha61%

[Kubernetes](</zh-TW/install/kubernetes>), [驗證](</zh-TW/gateway/authentication>), [遠端](</zh-TW/gateway/remote>), [暴露執行手冊](</zh-TW/gateway/security/exposure-runbook>)

叢集生命週期 5 項功能

實驗性0%

Alpha55%

Alpha61%

[Kubernetes](</zh-TW/install/kubernetes>), [索引](</zh-TW/gateway>)

iOS 應用程式 - M1 實驗性 - 8 個領域

內部預覽 / 超早期 Alpha。TestFlight 與由中繼支援的推播流程已存在，但尚未公開發行。

覆蓋率 實驗性 - 0%品質 實驗性 - 41%完整度 實驗性 - 44%無

媒體與分享 1 項能力

實驗性0%

實驗性41%

實驗性44%

[Ios](</zh-TW/platforms/ios>), [相機](</zh-TW/nodes/camera>)

畫布與螢幕 1 項能力

實驗性0%

實驗性41%

實驗性44%

[Ios](</zh-TW/platforms/ios>), [畫布](</zh-TW/plugins/reference/canvas>)

聊天與工作階段 1 項能力

實驗性0%

實驗性41%

實驗性44%

[Ios](</zh-TW/platforms/ios>), [網頁聊天](</zh-TW/web/webchat>), [協定](</zh-TW/gateway/protocol>)

閘道設定與診斷 7 項能力

實驗性0%

實驗性41%

實驗性44%

[Ios](</zh-TW/platforms/ios>), [配對](</zh-TW/channels/pairing>)

發佈 1 項能力

實驗性0%

實驗性41%

實驗性44%

[Ios](</zh-TW/platforms/ios>)

裝置命令 2 項能力

實驗性0%

實驗性41%

實驗性44%

[Ios](</zh-TW/platforms/ios>), [協定](</zh-TW/gateway/protocol>)

通知與背景 1 項能力

實驗性0%

實驗性41%

實驗性44%

[Ios](</zh-TW/platforms/ios>), [設定](</zh-TW/gateway/configuration>)

語音 1 項能力

實驗性0%

實驗性41%

實驗性44%

[Ios](</zh-TW/platforms/ios>), [通話](</zh-TW/nodes/talk>)

Nix install path - M1 Experimental - 5 areas

選用安裝流程。在升級為 alpha/beta 之前，需要更清楚的支援承諾。

涵蓋範圍 實驗性 - 0%品質 實驗性 - 41%完整性 實驗性 - 44%無

安裝交接 4 項能力

實驗性0%

實驗性41%

實驗性44%

[Nix](</zh-TW/install/nix>), [索引](</zh-TW/install>), [文件目錄](</zh-TW/start/docs-directory>)

外掛生命週期 4 項能力

實驗性0%

實驗性41%

實驗性44%

[管理外掛](</zh-TW/plugins/manage-plugins>), [外掛](</zh-TW/tools/plugin>), [Nix](</zh-TW/install/nix>)

啟用與應用程式使用體驗 7 項能力

實驗性0%

實驗性41%

實驗性44%

[Nix](</zh-TW/install/nix>)

設定與狀態 7 項能力

實驗性0%

實驗性41%

實驗性44%

[Nix](</zh-TW/install/nix>), [設定](</zh-TW/cli/setup>), [環境](</zh-TW/help/environment>)

服務執行階段與防護機制 8 項能力

實驗性0%

實驗性41%

實驗性44%

[Nix](</zh-TW/install/nix>), [設定](</zh-TW/cli/setup>), [Doctor](</zh-TW/cli/doctor>), [更新](</zh-TW/cli/update>)

watchOS companion surfaces - M1 實驗性 - 5 個領域

來源包含 Watch app/extension 介面；公開文件尚未將此呈現為使用者功能。

涵蓋範圍 實驗性 - 0%品質 實驗性 - 41%完整度 實驗性 - 44%無

傳遞與復原 7 項功能

實驗性0%

實驗性41%

實驗性44%

[iOS](</zh-TW/platforms/ios>)

執行核准 3 項功能

實驗性0%

實驗性41%

實驗性44%

[執行核准](</zh-TW/tools/exec-approvals>), [iOS](</zh-TW/platforms/ios>)

發佈與支援 6 項功能

實驗性0%

實驗性41%

實驗性44%

[iOS](</zh-TW/platforms/ios>)

通知與回覆 7 項功能

實驗性0%

實驗性41%

實驗性44%

[iOS](</zh-TW/platforms/ios>)

手錶 App UI 3 項功能

實驗性0%

實驗性41%

實驗性44%

[iOS](</zh-TW/platforms/ios>)

Linux companion app - M0 Planned - 5 areas

文件說原生 Linux companion app 仍在規劃中；閘道是目前支援的 Linux 路徑。

覆蓋率實驗性 - 0%品質實驗性 - 19%完整度實驗性 - 21%無

應用程式發佈 3 項能力

實驗性0%

實驗性19%

實驗性21%

[Linux](</zh-TW/platforms/linux>), [索引](</zh-TW/platforms>), [索引](</zh-TW/install>)

閘道連線 4 項能力

實驗性0%

實驗性19%

實驗性21%

[Linux](</zh-TW/platforms/linux>), [索引](</zh-TW/gateway>), [配對](</zh-TW/gateway/pairing>), [遠端](</zh-TW/gateway/remote>)

聊天與工作階段 3 項能力

實驗性0%

實驗性19%

實驗性21%

[Linux](</zh-TW/platforms/linux>), [協定](</zh-TW/gateway/protocol>), [網頁聊天](</zh-TW/web/webchat>)

桌面能力 9 項能力

實驗性0%

實驗性19%

實驗性21%

[Linux](</zh-TW/platforms/linux>), [執行核准](</zh-TW/tools/exec-approvals>), [機密](</zh-TW/gateway/secrets>), [索引](</zh-TW/nodes>), [執行](</zh-TW/tools/exec>), [對話](</zh-TW/nodes/talk>), [相機](</zh-TW/nodes/camera>)

狀態與診斷 7 項能力

實驗性0%

實驗性19%

實驗性21%

[Linux](</zh-TW/platforms/linux>), [Openclaw](</zh-TW/start/openclaw>), [診斷工具](</zh-TW/gateway/doctor>)

原生 Windows 伴隨應用程式 - M0 規劃中 - 5 個領域

僅規劃中。

涵蓋範圍實驗性 - 0%品質實驗性 - 19%完整度實驗性 - 21%無

安裝與更新 4 項能力

實驗性0%

實驗性19%

實驗性21%

[Windows](</zh-TW/platforms/windows>), [索引](</zh-TW/install>)

閘道連線 3 項能力

實驗性0%

實驗性19%

實驗性21%

[Windows](</zh-TW/platforms/windows>), [索引](</zh-TW/gateway>), [配對](</zh-TW/gateway/pairing>), [遠端](</zh-TW/gateway/remote>)

聊天工作階段 2 項能力

實驗性0%

實驗性19%

實驗性21%

[Windows](</zh-TW/platforms/windows>), [協定](</zh-TW/gateway/protocol>)

狀態與修復 5 項能力

實驗性0%

實驗性19%

實驗性21%

[Windows](</zh-TW/platforms/windows>), [Doctor](</zh-TW/gateway/doctor>), [索引](</zh-TW/gateway>)

桌面工具與權限 10 項能力

實驗性0%

實驗性19%

實驗性21%

[Windows](</zh-TW/platforms/windows>), [索引](</zh-TW/nodes>), [Exec](</zh-TW/tools/exec>), [Exec 核准](</zh-TW/tools/exec-approvals>), [索引](</zh-TW/gateway/security>)

### 頻道

Discord - M4 穩定 - 6 個領域

深入文件與廣泛功能涵蓋。語音／委派路徑應維持獨立評分為 beta/alpha。

涵蓋範圍實驗性 - 0%品質 Beta - 73%完整性穩定 - 87%部分 - 4

頻道設定與操作 10 項能力 / LTS 支援

實驗性0%

Beta73%

穩定版87%

[Discord](</zh-TW/channels/discord>), [Discord](</zh-TW/plugins/reference/discord>), [Fly](</zh-TW/install/fly>), [斜線命令](</zh-TW/tools/slash-commands>), [健康狀態](</zh-TW/gateway/health>), [頻道](</zh-TW/cli/channels>), [設定頻道](</zh-TW/gateway/config-channels>)

存取與身分 6 項能力 / LTS 支援

實驗性0%

Beta73%

穩定版87%

[Discord](</zh-TW/channels/discord>), [配對](</zh-TW/channels/pairing>), [存取群組](</zh-TW/channels/access-groups>), [群組](</zh-TW/channels/groups>)

對話路由與傳遞 12 項能力 / LTS 支援

實驗性0%

Beta73%

穩定版87%

[Discord](</zh-TW/channels/discord>), [頻道路由](</zh-TW/channels/channel-routing>), [群組](</zh-TW/channels/groups>), [存取群組](</zh-TW/channels/access-groups>), [ACP 代理](</zh-TW/tools/acp-agents>), [子代理](</zh-TW/tools/subagents>)

媒體與豐富內容 1 項能力 / LTS 支援

實驗性0%

Beta73%

穩定版87%

[Discord](</zh-TW/channels/discord>)

原生控制與核准 5 項能力

實驗性0%

Beta73%

穩定版87%

[Discord](</zh-TW/channels/discord>), [斜線命令](</zh-TW/tools/slash-commands>)

即時語音與通話 5 項能力

實驗性0%

Beta73%

穩定版87%

[Discord](</zh-TW/channels/discord>), [Openai](</zh-TW/providers/openai>), [Elevenlabs](</zh-TW/providers/elevenlabs>), [QA E2E 自動化](</zh-TW/concepts/qa-e2e-automation>), [設定頻道](</zh-TW/gateway/config-channels>)

Telegram - M3 Beta - 5 個領域

核心頻道已成熟到足以供一般使用，但高變異的使用者體驗與媒體邊界案例需要定期的情境驗證。

覆蓋範圍實驗性 - 0%品質 Alpha - 68%完整性 Beta - 78%完整 - 5

通道設定與操作 10 項能力 / LTS 支援

實驗性0%

Alpha66%

Beta78%

[Telegram](</zh-TW/channels/telegram>), [設定通道](</zh-TW/gateway/config-channels>), [通道](</zh-TW/cli/channels>)

存取與身分 10 項能力 / LTS 支援

實驗性0%

Alpha66%

Beta78%

[Telegram](</zh-TW/channels/telegram>), [配對](</zh-TW/channels/pairing>), [存取群組](</zh-TW/channels/access-groups>), [群組](</zh-TW/channels/groups>), [多代理](</zh-TW/concepts/multi-agent>)

對話路由與傳遞 1 項能力 / LTS 支援

實驗性0%

Alpha66%

Beta78%

[Telegram](</zh-TW/channels/telegram>), [群組](</zh-TW/channels/groups>), [多代理](</zh-TW/concepts/multi-agent>)

媒體與豐富內容 1 項能力 / LTS 支援

實驗性0%

Alpha66%

Beta78%

[Telegram](</zh-TW/channels/telegram>), [位置](</zh-TW/channels/location>)

原生控制與核准 9 項能力 / LTS 支援

實驗性0%

Beta77%

Beta79%

[Telegram](</zh-TW/channels/telegram>), [執行核准](</zh-TW/tools/exec-approvals>), [回應](</zh-TW/tools/reactions>)

Slack - M3 Beta - 5 個領域

第一級通道文件與路由介面。需要工作區安裝/管理員情境評分卡。

涵蓋範圍 實驗性 - 0%品質 Alpha - 66%完整性 Beta - 78%完整 - 5

通道設定與操作 10 項能力 / LTS 支援

實驗性0%

Alpha 版66%

Beta 版78%

[Slack](</zh-TW/channels/slack>), [Slack](</zh-TW/plugins/reference/slack>), [密鑰](</zh-TW/gateway/secrets>), [QA E2E 自動化](</zh-TW/concepts/qa-e2e-automation>), [疑難排解](</zh-TW/channels/troubleshooting>)

存取與身分 1 項能力 / LTS 支援

實驗性0%

Alpha 版66%

Beta 版78%

[Slack](</zh-TW/channels/slack>), [配對](</zh-TW/channels/pairing>)

對話路由與傳遞 5 項能力 / LTS 支援

實驗性0%

Alpha 版66%

Beta 版78%

[Slack](</zh-TW/channels/slack>), [機器人迴圈保護](</zh-TW/channels/bot-loop-protection>), [配對](</zh-TW/channels/pairing>)

媒體與豐富內容 1 項能力 / LTS 支援

實驗性0%

Alpha 版66%

Beta 版78%

[Slack](</zh-TW/channels/slack>), [QA E2E 自動化](</zh-TW/concepts/qa-e2e-automation>)

原生控制與核准 8 項能力 / LTS 支援

實驗性0%

Alpha 版66%

Beta 版78%

[Slack](</zh-TW/channels/slack>), [斜線命令](</zh-TW/tools/slash-commands>), [執行核准](</zh-TW/tools/exec-approvals>)

iMessage 與 BlueBubbles - M3 Beta 版 - 5 個領域

受支援的 iMessage 透過已登入的 macOS Messages 主機上的 imsg 執行；舊版 BlueBubbles 設定需要遷移。請明確呈現 macOS 權限、SSH 包裝器、SIP/私有 API，以及遷移注意事項。

涵蓋率實驗性 - 0%品質 Alpha 版 - 66%完整度 Beta 版 - 78%無

通道設定與操作 11 項能力

實驗性0%

Alpha66%

Beta78%

[Bluebubbles Imessage](</zh-TW/announcements/bluebubbles-imessage>), [Bluebubbles 的 Imessage](</zh-TW/channels/imessage-from-bluebubbles>), [設定通道](</zh-TW/gateway/config-channels>), [Imessage](</zh-TW/channels/imessage>)

存取與身分 6 項能力

實驗性0%

Alpha66%

Beta78%

[Imessage](</zh-TW/channels/imessage>), [Bluebubbles 的 Imessage](</zh-TW/channels/imessage-from-bluebubbles>), [設定通道](</zh-TW/gateway/config-channels>)

對話路由與傳遞 4 項能力

實驗性0%

Alpha66%

Beta78%

[Imessage](</zh-TW/channels/imessage>)

媒體與豐富內容 7 項能力

實驗性0%

Alpha66%

Beta78%

[Imessage](</zh-TW/channels/imessage>), [Bluebubbles 的 Imessage](</zh-TW/channels/imessage-from-bluebubbles>), [設定通道](</zh-TW/gateway/config-channels>)

原生控制與核准 3 項能力

實驗性0%

Alpha66%

Beta78%

[Imessage](</zh-TW/channels/imessage>)

WhatsApp - M3 Beta - 5 個範圍

核心路徑很重要且已有文件說明；上游 Baileys/session 的波動性使其低於穩定版。

涵蓋率實驗性 - 0%品質 Alpha - 66%完整性 Beta - 78%無

通道設定與操作 5 項能力

實驗性0%

Alpha66%

Beta78%

[Whatsapp](</zh-TW/channels/whatsapp>), [設定通道](</zh-TW/gateway/config-channels>), [Whatsapp](</zh-TW/plugins/reference/whatsapp>), [QA E2E 自動化](</zh-TW/concepts/qa-e2e-automation>), [Doctor](</zh-TW/gateway/doctor>)

存取與身分 7 項能力

實驗性0%

Alpha66%

Beta78%

[Whatsapp](</zh-TW/channels/whatsapp>), [設定通道](</zh-TW/gateway/config-channels>), [QA E2E 自動化](</zh-TW/concepts/qa-e2e-automation>), [配對](</zh-TW/channels/pairing>)

對話路由與傳遞 4 項能力

實驗性0%

Alpha66%

Beta78%

[Whatsapp](</zh-TW/channels/whatsapp>), [群組訊息](</zh-TW/channels/group-messages>)

媒體與豐富內容 2 項能力

實驗性0%

Alpha66%

Beta78%

[Whatsapp](</zh-TW/channels/whatsapp>)

原生控制與核准 2 項能力

實驗性0%

Alpha66%

Beta78%

[Whatsapp](</zh-TW/channels/whatsapp>)

Matrix - M2 Alpha - 6 個領域

透過隨附外掛支援。需要橋接、驗證與聊天室生命週期評分卡。

涵蓋範圍 實驗性 - 0%品質 Alpha - 60%完整度 Alpha - 67%無

頻道設定與操作 5 項能力

實驗性0%

Alpha 版60%

Alpha 版67%

[Matrix](</zh-TW/channels/matrix>), [Matrix 遷移](</zh-TW/channels/matrix-migration>)

存取與身分 7 項能力

實驗性0%

Alpha 版60%

Alpha 版67%

[Matrix](</zh-TW/channels/matrix>), [群組](</zh-TW/channels/groups>), [Bot 迴圈防護](</zh-TW/channels/bot-loop-protection>)

對話路由與傳遞 1 項能力

實驗性0%

Alpha 版60%

Alpha 版67%

[Matrix](</zh-TW/channels/matrix>)

媒體與豐富內容 1 項能力

實驗性0%

Alpha 版60%

Alpha 版67%

[Matrix](</zh-TW/channels/matrix>)

原生控制與核准 6 項能力

實驗性0%

Alpha 版60%

Alpha 版67%

[Matrix](</zh-TW/channels/matrix>)

加密與驗證 3 項能力

實驗性0%

Alpha 版60%

Alpha 版67%

[Matrix](</zh-TW/channels/matrix>), [Matrix 遷移](</zh-TW/channels/matrix-migration>)

Google Chat - M2 Alpha 版 - 5 個領域

已記錄文件的頻道，但企業／管理員設定提高了成熟度風險。

涵蓋率 實驗性 - 0%品質 Alpha 版 - 59%完整度 Alpha 版 - 66%無

頻道設定與操作 16 項能力

實驗性0%

Alpha59%

Alpha66%

[Google Chat](</zh-TW/channels/googlechat>), [Google Chat](</zh-TW/plugins/reference/googlechat>), [設定頻道](</zh-TW/gateway/config-channels>), [精靈命令列介面參考](</zh-TW/start/wizard-cli-reference>), [密鑰](</zh-TW/gateway/secrets>), [Secretref 憑證介面](</zh-TW/reference/secretref-credential-surface>), [健康狀態](</zh-TW/gateway/health>), [外掛清單](</zh-TW/plugins/plugin-inventory>), [索引](</zh-TW/channels>)

存取與身分 11 項能力

實驗性0%

Alpha59%

Alpha66%

[Google Chat](</zh-TW/channels/googlechat>), [配對](</zh-TW/channels/pairing>), [存取群組](</zh-TW/channels/access-groups>), [設定頻道](</zh-TW/gateway/config-channels>), [機器人迴圈保護](</zh-TW/channels/bot-loop-protection>), [頻道路由](</zh-TW/channels/channel-routing>)

對話路由與傳遞 1 項能力

實驗性0%

Alpha59%

Alpha66%

[Google Chat](</zh-TW/channels/googlechat>), [機器人迴圈保護](</zh-TW/channels/bot-loop-protection>), [存取群組](</zh-TW/channels/access-groups>), [頻道路由](</zh-TW/channels/channel-routing>)

媒體與豐富內容 1 項能力

實驗性0%

Alpha59%

Alpha66%

[Google Chat](</zh-TW/channels/googlechat>), [訊息](</zh-TW/cli/message>), [媒體理解](</zh-TW/nodes/media-understanding>), [Secretref 憑證介面](</zh-TW/reference/secretref-credential-surface>)

原生控制項與核准 16 項能力

實驗性0%

Alpha59%

Alpha66%

[Google Chat](</zh-TW/channels/googlechat>), [訊息](</zh-TW/cli/message>), [媒體理解](</zh-TW/nodes/media-understanding>), [Secretref 憑證介面](</zh-TW/reference/secretref-credential-surface>), [反應](</zh-TW/tools/reactions>), [斜線命令](</zh-TW/tools/slash-commands>), [設定代理程式](</zh-TW/gateway/config-agents>), [訊息生命週期重構](</zh-TW/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alpha - 5 個領域

企業驗證/管理流程需要明確的情境證明。

覆蓋率 實驗性 - 0%品質 Alpha - 59%完整度 Alpha - 66%無

頻道設定與操作 9 項能力

實驗性0%

Alpha 版59%

Alpha 版66%

[Msteams](</zh-TW/channels/msteams>), [Msteams](</zh-TW/plugins/reference/msteams>), [設定頻道](</zh-TW/gateway/config-channels>), [健康狀態](</zh-TW/gateway/health>)

存取與身分 9 項能力

實驗性0%

Alpha 版59%

Alpha 版66%

[Msteams](</zh-TW/channels/msteams>), [配對](</zh-TW/channels/pairing>), [存取群組](</zh-TW/channels/access-groups>)

對話路由與傳遞 5 項能力

實驗性0%

Alpha 版59%

Alpha 版66%

[Msteams](</zh-TW/channels/msteams>), [群組](</zh-TW/channels/groups>), [頻道路由](</zh-TW/channels/channel-routing>)

媒體與豐富內容 5 項能力

實驗性0%

Alpha 版59%

Alpha 版66%

[Msteams](</zh-TW/channels/msteams>)

原生控制與核准 5 項能力

實驗性0%

Alpha 版59%

Alpha 版66%

[Msteams](</zh-TW/channels/msteams>), [進階執行核准](</zh-TW/tools/exec-approvals-advanced>)

Signal - M2 Alpha 版 - 5 個領域

已有支援的頻道文件；仍需要更強的安裝與重新連線證明。

涵蓋範圍 實驗性 - 0%品質 Alpha 版 - 59%完整性 Alpha 版 - 66%無

頻道設定與操作 7 項能力

實驗性0%

Alpha 版59%

Alpha 版66%

[Signal](</zh-TW/channels/signal>), [Signal](</zh-TW/plugins/reference/signal>)

存取與身分識別 6 項能力

實驗性0%

Alpha 版59%

Alpha 版66%

[Signal](</zh-TW/channels/signal>)

對話路由與傳遞 1 項能力

實驗性0%

Alpha 版59%

Alpha 版66%

[Signal](</zh-TW/channels/signal>)

媒體與豐富內容 7 項能力

實驗性0%

Alpha 版59%

Alpha 版66%

[Signal](</zh-TW/channels/signal>)

原生控制項與核准 3 項能力

實驗性0%

Alpha 版59%

Alpha 版66%

[Signal](</zh-TW/channels/signal>)

Feishu、QQ Bot、微信、騰訊元寶、Zalo、Zalo Personal、區域頻道 - M2 Alpha 版 - 4 個領域

重要的區域涵蓋範圍，但公開支援等級應依帳號類型、上游核准與維護者證明進行校準。

涵蓋範圍 實驗性 - 0%品質 Alpha 版 - 55%完整度 Alpha 版 - 58%無

頻道設定與操作 6 項能力

實驗性0%

Alpha61%

Alpha68%

[索引](</zh-TW/channels>), [配對](</zh-TW/channels/pairing>), [Feishu](</zh-TW/plugins/reference/feishu>), [架構內部](</zh-TW/plugins/architecture-internals>)

存取與身分 1 項能力

實驗性0%

Alpha53%

Alpha54%

沒有連結的文件

對話路由與傳遞 1 項能力

實驗性0%

Alpha53%

Alpha54%

沒有連結的文件

媒體與豐富內容 1 項能力

實驗性0%

Alpha53%

Alpha54%

沒有連結的文件

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 Alpha - 4 個領域

已有支援的介面存在，但成熟度可能因上游與維護者涵蓋範圍而異。稍後再逐一評分。

涵蓋範圍 實驗性 - 0%品質 Alpha - 53%完整度 Alpha - 54%無

通道設定與營運 1 項能力

實驗性0%

Alpha53%

Alpha54%

沒有連結文件

存取與身分識別 1 項能力

實驗性0%

Alpha53%

Alpha54%

沒有連結文件

對話路由與傳遞 1 項能力

實驗性0%

Alpha53%

Alpha54%

沒有連結文件

媒體與豐富內容 1 項能力

實驗性0%

Alpha53%

Alpha54%

沒有連結文件

語音通話通道 - M1 實驗性 - 5 個領域

具有複雜即時行為的選用／外掛路徑。公開 beta 前需要情境評分卡。

涵蓋率 實驗性 - 0%品質 實驗性 - 41%完整性 實驗性 - 44%無

頻道設定與作業 2 項能力

實驗性0%

實驗性41%

實驗性44%

[語音通話](</zh-TW/cli/voicecall>), [語音通話](</zh-TW/plugins/voice-call>), [協定](</zh-TW/gateway/protocol>)

存取與身分 1 項能力

實驗性0%

實驗性41%

實驗性44%

[語音通話](</zh-TW/plugins/voice-call>), [語音通話](</zh-TW/cli/voicecall>)

對話路由與遞送 1 項能力

實驗性0%

實驗性41%

實驗性44%

[語音通話](</zh-TW/plugins/voice-call>)

媒體與豐富內容 2 項能力

實驗性0%

實驗性41%

實驗性44%

[語音通話](</zh-TW/plugins/voice-call>), [外掛清單](</zh-TW/plugins/plugin-inventory>)

即時語音與通話 2 項能力

實驗性0%

實驗性41%

實驗性44%

[語音通話](</zh-TW/plugins/voice-call>)

### 供應商與工具

瀏覽器自動化、exec 與沙盒工具 - M3 Beta - 3 個範圍

核心工具已有文件記載，但主機安全性與權限使用者體驗應持續納入計分卡檢視。

覆蓋率實驗性 - 21%品質 Beta - 75%完整性 Beta - 79%部分 - 2

瀏覽器自動化 8 項能力

實驗性13%

Beta79%

Beta79%

[瀏覽器控制](</zh-TW/tools/browser-control>), [測試](</zh-TW/help/testing>), [瀏覽器](</zh-TW/tools/browser>), [索引](</zh-TW/gateway/security>), [稽核檢查](</zh-TW/gateway/security/audit-checks>)

工具呼叫與執行 6 項能力 / LTS 支援

Alpha50%

Beta79%

Beta79%

[執行](</zh-TW/tools/exec>), [背景程序](</zh-TW/gateway/background-process>), [工具呼叫 HTTP API](</zh-TW/gateway/tools-invoke-http-api>), [操作員範圍](</zh-TW/gateway/operator-scopes>), [協定](</zh-TW/gateway/protocol>), [執行核准](</zh-TW/tools/exec-approvals>), [進階執行核准](</zh-TW/tools/exec-approvals-advanced>), [提升權限](</zh-TW/tools/elevated>)

沙箱與工具政策 6 項能力 / LTS 支援

實驗性0%

Alpha68%

Beta79%

[沙箱化](</zh-TW/gateway/sandboxing>), [沙箱與工具政策與提升權限](</zh-TW/gateway/sandbox-vs-tool-policy-vs-elevated>), [多代理沙箱工具](</zh-TW/tools/multi-agent-sandbox-tools>), [Codex Harness 參考](</zh-TW/plugins/codex-harness-reference>), [設定工具](</zh-TW/gateway/config-tools>)

OpenAI 與 Codex 提供者路徑 - M3 Beta - 5 個領域

深入文件、OAuth/訂閱路徑、即時語音、影像與相容性行為。提供者變動頻繁，若沒有發布評分卡證明，尚無法達到穩定版。

涵蓋範圍 實驗性 - 26%品質 Beta - 74%完整度 Beta - 79%部分 - 3

模型與驗證 6 項能力 / LTS 支援

實驗性44%

Beta79%

Beta79%

[Openai](</zh-TW/providers/openai>), [Codex Harness](</zh-TW/plugins/codex-harness>), [模型](</zh-TW/concepts/models>), [Oauth](</zh-TW/concepts/oauth>), [Codex Harness 參考](</zh-TW/plugins/codex-harness-reference>), [驗證監控](</zh-TW/gateway/authentication>)

回應與工具相容性 4 項能力 / LTS 支援

實驗性40%

Beta79%

Beta79%

[Openai](</zh-TW/providers/openai>), [Openresponses Http Api](</zh-TW/gateway/openresponses-http-api>), [Openai Http Api](</zh-TW/gateway/openai-http-api>), [Codex 原生外掛](</zh-TW/plugins/codex-native-plugins>)

原生 Codex Harness 2 項能力 / LTS 支援

實驗性44%

Beta79%

Beta79%

[Codex Harness](</zh-TW/plugins/codex-harness>), [Codex Harness 執行階段](</zh-TW/plugins/codex-harness-runtime>), [Codex Harness 參考](</zh-TW/plugins/codex-harness-reference>), [Codex 原生外掛](</zh-TW/plugins/codex-native-plugins>)

影像與多模態輸入 2 項能力

實驗性0%

Alpha67%

Beta79%

[Openai](</zh-TW/providers/openai>), [影像產生](</zh-TW/tools/image-generation>), [影像](</zh-TW/nodes/images>)

語音與即時音訊 2 項能力

實驗性0%

Alpha67%

Beta79%

[Openai](</zh-TW/providers/openai>), [Discord](</zh-TW/channels/discord>), [語音通話](</zh-TW/plugins/voice-call>)

網頁搜尋工具 - M3 Beta - 4 個領域

已有多個提供者與文件。需要針對每個提供者系列提供配額、錯誤與 SSRF 證明。

覆蓋率 實驗性 - 9%品質 Beta - 74%完整度 Beta - 79%無

搜尋提供者 19 項能力

實驗性11%

測試版79%

測試版79%

[網頁](</zh-TW/tools/web>), [Brave Search](</zh-TW/tools/brave-search>), [Tavily](</zh-TW/tools/tavily>), [Exa Search](</zh-TW/tools/exa-search>), [Firecrawl](</zh-TW/tools/firecrawl>), [Perplexity Search](</zh-TW/tools/perplexity-search>), [Duckduckgo Search](</zh-TW/tools/duckduckgo-search>), [Searxng Search](</zh-TW/tools/searxng-search>), [Gemini Search](</zh-TW/tools/gemini-search>), [Grok Search](</zh-TW/tools/grok-search>), [Kimi Search](</zh-TW/tools/kimi-search>), [Minimax Search](</zh-TW/tools/minimax-search>), [Ollama Search](</zh-TW/tools/ollama-search>), [SDK 子路徑](</zh-TW/plugins/sdk-subpaths>), [SDK 概觀](</zh-TW/plugins/sdk-overview>), [清單](</zh-TW/plugins/manifest>)

設定與診斷 9 項能力

實驗性0%

Alpha68%

測試版79%

[網頁](</zh-TW/tools/web>), [網頁擷取](</zh-TW/tools/web-fetch>), [常見問題](</zh-TW/help/faq>), [API 使用成本](</zh-TW/reference/api-usage-costs>), [Brave Search](</zh-TW/tools/brave-search>), [Perplexity Search](</zh-TW/tools/perplexity-search>), [Tavily](</zh-TW/tools/tavily>), [Firecrawl](</zh-TW/tools/firecrawl>)

網路安全 4 項能力

實驗性0%

Alpha68%

測試版79%

[網頁](</zh-TW/tools/web>), [網頁擷取](</zh-TW/tools/web-fetch>), [Firecrawl](</zh-TW/tools/firecrawl>), [Searxng Search](</zh-TW/tools/searxng-search>)

工具可用性與擷取 11 項能力

實驗性25%

測試版79%

測試版79%

[設定工具](</zh-TW/gateway/config-tools>), [網頁擷取](</zh-TW/tools/web-fetch>), [網頁](</zh-TW/tools/web>), [常見問題](</zh-TW/help/faq>)

Anthropic 提供者路徑 - M3 測試版 - 5 個領域

第一級模型提供者。需要定期提供驗證、目錄與工具呼叫情境的證明。

覆蓋範圍 實驗性 - 0%品質 測試版 - 71%完整度 測試版 - 78%無

供應商驗證與復原 9 項能力

實驗性0%

Alpha66%

Beta78%

[Anthropic](</zh-TW/providers/anthropic>), [Doctor](</zh-TW/gateway/doctor>), [設定範例](</zh-TW/gateway/configuration-examples>), [疑難排解](</zh-TW/gateway/troubleshooting>), [提示快取](</zh-TW/reference/prompt-caching>)

模型與執行階段選擇 10 項能力

實驗性0%

Beta78%

Beta79%

[Anthropic](</zh-TW/providers/anthropic>), [設定 Agent](</zh-TW/gateway/config-agents>), [模型](</zh-TW/concepts/models>), [命令列介面後端](</zh-TW/gateway/cli-backends>)

請求傳輸與回合語意 10 項能力

實驗性0%

Beta77%

Beta79%

[Anthropic](</zh-TW/providers/anthropic>), [提示快取](</zh-TW/reference/prompt-caching>), [疑難排解](</zh-TW/gateway/troubleshooting>), [命令列介面後端](</zh-TW/gateway/cli-backends>), [模型供應商](</zh-TW/concepts/model-providers>)

提示快取與上下文 5 項能力

實驗性0%

Alpha66%

Beta78%

[Anthropic](</zh-TW/providers/anthropic>), [提示快取](</zh-TW/reference/prompt-caching>), [疑難排解](</zh-TW/gateway/troubleshooting>), [心跳偵測](</zh-TW/gateway/heartbeat>)

媒體輸入 4 項能力

實驗性0%

Alpha66%

Beta78%

[Anthropic](</zh-TW/providers/anthropic>), [設定 Agent](</zh-TW/gateway/config-agents>)

Google 供應商路徑 - M3 Beta - 5 個領域

具備模型與即時介面的一級供應商。需要分開進行 Live/Talk 評分。

涵蓋率實驗性 - 0%品質 Alpha - 66%完整性 Beta - 78%無

供應商設定與憑證 10 項能力

實驗性0%

Alpha66%

Beta78%

[Google](</zh-TW/providers/google>), [模型供應商](</zh-TW/concepts/model-providers>)

模型路由與端點 10 項能力

實驗性0%

Alpha66%

Beta78%

[Google](</zh-TW/providers/google>), [模型供應商](</zh-TW/concepts/model-providers>), [Google](</zh-TW/plugins/reference/google>), [Gemini 搜尋](</zh-TW/tools/gemini-search>)

直接 Gemini 執行階段 9 項能力

實驗性0%

Alpha66%

Beta78%

[Google](</zh-TW/providers/google>), [模型供應商](</zh-TW/concepts/model-providers>), [模型常見問題](</zh-TW/help/faq-models>), [即時測試](</zh-TW/help/testing-live>)

媒體、搜尋與即時 10 項能力

實驗性0%

Alpha66%

Beta78%

[Google](</zh-TW/plugins/reference/google>), [Google](</zh-TW/providers/google>)

提示快取 5 項能力

實驗性0%

Alpha66%

Beta78%

[提示快取](</zh-TW/reference/prompt-caching>), [Google](</zh-TW/providers/google>), [模型供應商](</zh-TW/concepts/model-providers>), [權杖使用量](</zh-TW/reference/token-use>)

OpenRouter 供應商路徑 - M3 Beta - 4 個領域

統一供應商路徑已有文件記載且具備價值，但模型特定行為各有差異。

覆蓋範圍實驗性 - 0%品質 Alpha - 66%完整度 Beta - 78%無

提供者設定與驗證 14 項能力

實驗性0%

Alpha66%

Beta78%

[Openrouter](</zh-TW/providers/openrouter>), [模型提供者](</zh-TW/concepts/model-providers>), [設定](</zh-TW/cli/configure>), [驗證](</zh-TW/gateway/authentication>), [環境](</zh-TW/help/environment>), [模型](</zh-TW/cli/models>), [模型](</zh-TW/concepts/models>)

聊天執行階段與正規化 15 項能力

實驗性0%

Alpha66%

Beta78%

[Openrouter](</zh-TW/providers/openrouter>), [模型提供者](</zh-TW/concepts/model-providers>), [提示快取](</zh-TW/reference/prompt-caching>)

提供者復原與診斷 5 項能力

實驗性0%

Alpha66%

Beta78%

[模型容錯移轉](</zh-TW/concepts/model-failover>), [Openrouter](</zh-TW/providers/openrouter>), [模型](</zh-TW/cli/models>)

媒體生成與語音 7 項能力

實驗性0%

Alpha66%

Beta78%

[Openrouter](</zh-TW/providers/openrouter>), [圖片生成](</zh-TW/tools/image-generation>), [音樂生成](</zh-TW/tools/music-generation>), [媒體概覽](</zh-TW/tools/media-overview>), [影片生成](</zh-TW/tools/video-generation>), [Tts](</zh-TW/tools/tts>)

圖片、影片與音樂生成工具 - M2 Alpha - 5 個領域

各提供者都具備此能力，但品質、延遲與參數相容性差異過大；若沒有逐一提供者的證明，尚不足以進入 Beta。

涵蓋範圍 實驗性 - 0%品質 Alpha - 61%完整性 Alpha - 68%無

媒體路由與探索 4 項能力

實驗性0%

早期測試61%

早期測試68%

[設定代理](</zh-TW/gateway/config-agents>), [圖片生成](</zh-TW/tools/image-generation>), [影片生成](</zh-TW/tools/video-generation>), [音樂生成](</zh-TW/tools/music-generation>)

任務生命週期與交付 12 項能力

實驗性0%

早期測試61%

早期測試68%

[媒體概觀](</zh-TW/tools/media-overview>), [圖片生成](</zh-TW/tools/image-generation>), [影片生成](</zh-TW/tools/video-generation>), [音樂生成](</zh-TW/tools/music-generation>)

圖片生成 9 項能力

實驗性0%

早期測試61%

早期測試68%

[圖片生成](</zh-TW/tools/image-generation>), [推論](</zh-TW/cli/infer>), [媒體概觀](</zh-TW/tools/media-overview>)

影片生成 11 項能力

實驗性0%

早期測試61%

早期測試68%

[影片生成](</zh-TW/tools/video-generation>), [Runway](</zh-TW/providers/runway>), [Pixverse](</zh-TW/providers/pixverse>), [Fal](</zh-TW/providers/fal>), [Openrouter](</zh-TW/providers/openrouter>)

音樂生成 6 項能力

實驗性0%

早期測試61%

早期測試68%

[音樂生成](</zh-TW/tools/music-generation>)

本機模型提供者：Ollama、vLLM、SGLang、LM Studio - M2 早期測試 - 5 個領域

實用且已有文件說明，但環境差異很大。

覆蓋範圍 實驗性 - 0%品質 早期測試 - 61%完整度 早期測試 - 68%無

提供者設定、生命週期與診斷 12 項能力

實驗性0%

Alpha61%

Alpha68%

[本機模型](</zh-TW/gateway/local-models>), [Lmstudio](</zh-TW/providers/lmstudio>), [Ollama](</zh-TW/providers/ollama>), [Vllm](</zh-TW/providers/vllm>), [本機模型服務](</zh-TW/gateway/local-model-services>), [設定代理程式](</zh-TW/gateway/config-agents>), [疑難排解](</zh-TW/gateway/troubleshooting>), [Doctor](</zh-TW/gateway/doctor>)

原生提供者外掛 10 項能力

實驗性0%

Alpha61%

Alpha68%

[Ollama](</zh-TW/providers/ollama>), [Lmstudio](</zh-TW/providers/lmstudio>)

OpenAI 相容執行階段相容性 8 項能力

實驗性0%

Alpha61%

Alpha68%

[Vllm](</zh-TW/providers/vllm>), [Sglang](</zh-TW/providers/sglang>), [本機模型](</zh-TW/gateway/local-models>), [Lmstudio](</zh-TW/providers/lmstudio>)

本機記憶與嵌入 5 項能力

實驗性0%

Alpha61%

Alpha68%

[記憶](</zh-TW/concepts/memory>), [Doctor](</zh-TW/gateway/doctor>)

網路安全與提示詞控制 2 項能力

實驗性0%

Alpha61%

Alpha68%

[索引](</zh-TW/gateway/security>), [設定工具](</zh-TW/gateway/config-tools>), [本機模型](</zh-TW/gateway/local-models>)

長尾託管提供者 - M2 Alpha - 3 個領域

已有許多文件/參考頁面；分數應由提供者中繼資料加上即時冒煙測試涵蓋範圍產生。

覆蓋率 實驗性 - 0%品質 初期測試版 - 61%完整度 初期測試版 - 68%無

託管式 LLM 提供者 12 項能力

實驗性0%

初期測試版61%

初期測試版68%

[索引](</zh-TW/providers>), [模型提供者](</zh-TW/concepts/model-providers>), [即時測試](</zh-TW/help/testing-live>), [上線設定](</zh-TW/cli/onboard>)

託管式媒體提供者 8 項能力

實驗性0%

初期測試版61%

初期測試版68%

[清單](</zh-TW/plugins/manifest>), [即時測試](</zh-TW/help/testing-live>), [索引](</zh-TW/providers>)

提供者操作 12 項能力

實驗性0%

初期測試版61%

初期測試版68%

[索引](</zh-TW/providers>), [模型提供者](</zh-TW/concepts/model-providers>), [清單](</zh-TW/plugins/manifest>), [即時測試](</zh-TW/help/testing-live>), [模型](</zh-TW/cli/models>)

Was this useful?YesNo

Open issue