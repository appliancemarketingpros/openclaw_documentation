---
title: 成熟度分类法
source_url: https://docs.openclaw.ai/zh-CN/maturity/taxonomy
scraped_at: 2026-06-29
---

快速开始

# 成熟度分类法

评分卡背后的模型

功能面 > 类别 > 能力 > 证据。

50 个功能面分为 4 个族，每个类别都关联回规范文档和 QA 覆盖 ID。

浏览产品领域 / 打开详细分类法 / [查看评分](</zh-CN/maturity/scorecard>)

## 如何阅读此页面

功能面是一个产品领域，例如 Gateway 网关运行时、Discord 或 macOS 应用。每个功能面包含多个类别，每个类别包含 QA 场景覆盖的能力级检查。使用评分卡进行发布级判断；使用此页面检查其底层模型。

## 成熟度级别

M0已规划方向已知，但还没有受支持的用户路径。晋级：存在设计议题、负责人和目标功能面。

M1实验性已实现，但带有注意事项、标志、源码构建或仅维护者可用的流程。晋级：维护者可以从当前 main 运行该场景。

M2Alpha真实用户可以试用，但预期会有破坏性变更和不完整的用户体验。晋级：有文档化设置、基础测试、已知注意事项，以及至少一个真实环境证明。

M3Beta存在公开路径，主要工作流可用，且注意事项范围明确。晋级：安装/更新文档、回归测试、支持运行手册，以及在预期环境中成功的场景证明。

M4Stable推荐给普通用户的路径。故障会被视为回归。晋级：发布门禁、Doctor/故障排除路径、广泛文档，以及重复的真实世界证明。

M5Clawesome精致、愉悦、充分可观测，并且可与最佳同类工作流竞争。晋级：Stable 加上代表性用户的用户评分卡通过。

## 产品领域

### 核心

CLI M4Stable7 个领域 - 完成度 90% Gateway 网关运行时 M4Stable13 个领域 - 完成度 89% 智能体运行时 M3Beta9 个领域 - 完成度 79% 会话、记忆和上下文引擎 M3Beta9 个领域 - 完成度 79% 渠道框架 M3Beta8 个领域 - 完成度 79% 可观测性 M3Beta5 个领域 - 完成度 79% Gateway 网关 Web 应用 M3Beta6 个领域 - 完成度 79% 插件 M3测试版9 个领域 - 79% 完成 安全、认证、配对和密钥 M3测试版6 个领域 - 79% 完成 自动化：cron、钩子、任务、轮询 M3测试版6 个领域 - 79% 完成 媒体理解和媒体生成 M2Alpha 版6 个领域 - 68% 完成 语音和实时对话 M2Alpha 版6 个领域 - 68% 完成 TUI M2Alpha 版5 个领域 - 66% 完成 ClawHub M2Alpha 版4 个领域 - 62% 完成 OpenClaw 应用 SDK M2Alpha 版6 个领域 - 53% 完成

### 平台

Linux Gateway 网关主机 M4稳定版5 个领域 - 89% 完成 macOS Gateway 网关主机 M4稳定版7 个领域 - 88% 完成 Docker 和 Podman 托管 M3测试版4 个领域 - 79% 完成 通过 WSL2 使用 Windows M3测试版6 个领域 - 79% 完成 Raspberry Pi 和小型 Linux 设备 M3测试版4 个领域 - 79% 完成 macOS 配套应用 M3测试版8 个领域 - 78% 完成 Android 应用 M2Alpha 版7 个领域 - 66% 完成 原生 Windows M2Alpha4 个方面 - 完成 66% Kubernetes 托管 M2Alpha4 个方面 - 完成 61% iOS 应用 M1实验性8 个方面 - 完成 44% Nix 安装路径 M1实验性5 个方面 - 完成 44% watchOS 配套界面 M1实验性5 个方面 - 完成 44% Linux 配套应用 M0已规划5 个方面 - 完成 21% 原生 Windows 配套应用 M0已规划5 个方面 - 完成 21%

### 渠道

Discord M4稳定6 个方面 - 完成 87% Telegram M3Beta5 个方面 - 完成 78% Slack M3Beta5 个方面 - 完成 78% iMessage 和 BlueBubbles M3Beta5 个方面 - 完成 78% WhatsApp M3Beta5 个方面 - 完成 78% Matrix M2Alpha6 个方面 - 完成 67% Google Chat M2Alpha5 个方面 - 完成 66% Microsoft Teams M2Alpha5 个方面 - 完成 66% Signal M2Alpha5 个方面 - 完成 66% Feishu、QQ Bot、微信、腾讯元宝、Zalo、Zalo Personal、区域渠道 M2Alpha4 个方面 - 完成 58% Mattermost、LINE、IRC、Nextcloud Talk、Nostr、Twitch、Tlon、Synology Chat M2Alpha4 个方面 - 完成 54% 语音通话渠道 M1实验性5 个方面 - 完成 44%

### 提供商和工具

浏览器自动化、exec 和沙箱工具 M3Beta3 个方面 - 完成 79% OpenAI 和 Codex 提供商路径 M3Beta5 个方面 - 完成 79% Web 搜索工具 M3Beta4 个方面 - 完成 79% Anthropic 提供商路径 M3Beta5 个方面 - 完成 78% Google 提供商路径 M3Beta5 个方面 - 完成 78% OpenRouter 提供商路径 M3Beta4 个方面 - 完成 78% 图像、视频和音乐生成工具 M2Alpha5 个方面 - 完成 68% 本地模型提供商：Ollama、vLLM、SGLang、LM Studio M2Alpha5 个方面 - 完成 68% 长尾托管提供商 M2Alpha3 个方面 - 完成 68%

## 详情

### 核心

CLI - M4 稳定 - 7 个方面

常规设置和修复路径已在安装、CLI 和 Gateway 网关文档中说明。特定平台的 Windows 路径在 Windows via WSL2 和原生 Windows 行中跟踪。

覆盖率实验性 - 4%质量稳定 - 83%完整度稳定 - 90%部分 - 6

CLI 设置 6 项能力 / 受 LTS 支持

实验性17%

稳定89%

稳定90%

[索引](</zh-CN/install>), [安装器](</zh-CN/install/installer>), [Node](</zh-CN/install/node>), [更新](</zh-CN/install/updating>)

新手引导和凭证设置 5 项能力 / 受 LTS 支持

实验性0%

测试版75%

稳定89%

[新手引导](</zh-CN/cli/onboard>), [配置](</zh-CN/cli/configure>), [新手引导概览](</zh-CN/start/onboarding-overview>)

插件和渠道设置 5 项能力

实验性0%

测试版75%

稳定89%

[新手引导](</zh-CN/cli/onboard>), [插件](</zh-CN/cli/plugins>), [渠道](</zh-CN/cli/channels>)

Gateway 网关服务管理 5 项能力 / 受 LTS 支持

实验性14%

稳定87%

稳定90%

[Gateway 网关](</zh-CN/cli/gateway>), [更新](</zh-CN/install/updating>), [故障排除](</zh-CN/gateway/troubleshooting>)

CLI 可观测性 5 项能力 / 受 LTS 支持

实验性0%

稳定89%

稳定90%

[状态](</zh-CN/cli/status>), [健康](</zh-CN/cli/health>), [日志](</zh-CN/cli/logs>), [诊断](</zh-CN/gateway/diagnostics>)

Doctor 10 项能力 / 受 LTS 支持

实验性0%

稳定89%

稳定90%

[Doctor](</zh-CN/cli/doctor>), [Doctor](</zh-CN/gateway/doctor>), [密钥](</zh-CN/gateway/secrets>), [故障排除](</zh-CN/gateway/troubleshooting>)

更新和升级 5 项能力 / 受 LTS 支持

实验性0%

测试版75%

稳定89%

[更新](</zh-CN/install/updating>), [更新](</zh-CN/cli/update>), [故障排除](</zh-CN/gateway/troubleshooting>)

Gateway 网关运行时 - M4 稳定 - 13 个领域

核心架构、凭证、配对、协议文档、守护进程文档和 CLI 运行手册覆盖广泛且保持最新。

覆盖率实验性 - 6%质量稳定 - 81%完整性稳定 - 89%部分 - 12

审批和远程执行 6 项能力 / LTS 支持

实验性0%

测试版75%

稳定版89%

[协议](</zh-CN/gateway/protocol>), [索引](</zh-CN/gateway/security>)

HTTP API 4 项能力 / LTS 支持

实验性25%

稳定版90%

稳定版90%

[索引](</zh-CN/gateway>), [OpenAI HTTP API](</zh-CN/gateway/openai-http-api>), [OpenResponses HTTP API](</zh-CN/gateway/openresponses-http-api>), [工具调用 HTTP API](</zh-CN/gateway/tools-invoke-http-api>), [钩子](</zh-CN/automation/hooks>), [索引](</zh-CN/web>)

托管 Web 界面 4 项能力 / LTS 支持

实验性0%

稳定版89%

稳定版90%

[索引](</zh-CN/gateway>), [架构](</zh-CN/concepts/architecture>), [Control UI](</zh-CN/web/control-ui>), [Webchat](</zh-CN/web/webchat>), [Canvas](</zh-CN/refactor/canvas>)

Gateway 网关 RPC API 和事件 20 项能力 / LTS 支持

实验性9%

稳定版90%

稳定版90%

[协议](</zh-CN/gateway/protocol>), [索引](</zh-CN/gateway>), [架构](</zh-CN/concepts/architecture>)

设备认证和配对 10 项能力 / LTS 支持

实验性0%

测试版75%

稳定版89%

[协议](</zh-CN/gateway/protocol>), [配对](</zh-CN/gateway/pairing>), [索引](</zh-CN/gateway/security>)

网络访问和设备发现 6 项能力 / LTS 支持

实验性0%

测试版75%

稳定版89%

[索引](</zh-CN/gateway>), [设备发现](</zh-CN/gateway/discovery>), [协议](</zh-CN/gateway/protocol>)

节点和远程能力 8 项能力

实验性0%

测试版75%

稳定版89%

[协议](</zh-CN/gateway/protocol>), [架构](</zh-CN/concepts/architecture>), [索引](</zh-CN/nodes>)

健康、诊断和修复 7 项能力 / LTS 支持

实验性0%

测试版75%

稳定版89%

[索引](</zh-CN/gateway>), [诊断](</zh-CN/gateway/diagnostics>), [Doctor](</zh-CN/gateway/doctor>)

协议兼容性 7 项能力 / LTS 支持

实验性0%

Beta75%

稳定89%

[协议](</zh-CN/gateway/protocol>), [架构](</zh-CN/concepts/architecture>), [Typebox](</zh-CN/concepts/typebox>), [Bridge Protocol](</zh-CN/gateway/bridge-protocol>)

角色和权限 5 项能力 / LTS 支持

实验性0%

Beta75%

稳定89%

[协议](</zh-CN/gateway/protocol>), [索引](</zh-CN/gateway/security>)

Gateway 网关生命周期 7 项能力 / LTS 支持

实验性33%

稳定90%

稳定90%

[索引](</zh-CN/gateway>), [架构](</zh-CN/concepts/architecture>)

安全控制 6 项能力 / LTS 支持

实验性0%

Beta75%

稳定89%

[索引](</zh-CN/gateway/security>), [协议](</zh-CN/gateway/protocol>), [设备发现](</zh-CN/gateway/discovery>)

WebSocket 连接 8 项能力 / LTS 支持

实验性13%

稳定90%

稳定90%

[协议](</zh-CN/gateway/protocol>), [架构](</zh-CN/concepts/architecture>)

Agent Runtime - M3 Beta - 9 个领域

主循环、模型、提供商路由和工具流式传输是一等能力，但提供商行为每周都在变化，并且每个版本都需要场景验证。

覆盖率 实验性 - 33%质量 Beta - 78%完整性 Beta - 79%部分 - 6

智能体轮次执行 3 项能力 / LTS 支持

实验性29%

Beta 版79%

Beta 版79%

[Agent loop](</zh-CN/concepts/agent-loop>), [智能体](</zh-CN/cli/agent>), [Agent Runtimes](</zh-CN/concepts/agent-runtimes>)

外部运行时和子智能体 4 项能力

实验性30%

Beta 版79%

Beta 版79%

[Agent Runtimes](</zh-CN/concepts/agent-runtimes>), [Anthropic](</zh-CN/providers/anthropic>), [Google](</zh-CN/providers/google>), [子智能体](</zh-CN/tools/subagents>)

托管提供商执行 5 项能力 / LTS 支持

实验性20%

Beta 版79%

Beta 版79%

[OpenAI](</zh-CN/providers/openai>), [Anthropic](</zh-CN/providers/anthropic>), [Google](</zh-CN/providers/google>), [Models](</zh-CN/concepts/models>)

本地和自托管提供商 5 项能力

实验性0%

Alpha 版68%

Beta 版79%

[Ollama](</zh-CN/providers/ollama>), [Models](</zh-CN/concepts/models>), [智能体](</zh-CN/cli/agent>)

模型和运行时选择 4 项能力 / LTS 支持

实验性25%

Beta 版79%

Beta 版79%

[Models](</zh-CN/concepts/models>), [Models](</zh-CN/cli/models>), [OpenAI](</zh-CN/providers/openai>), [Agent Runtimes](</zh-CN/concepts/agent-runtimes>)

提供商认证 10 项能力 / LTS 支持

实验性24%

Beta 版79%

Beta 版79%

[Models](</zh-CN/concepts/models>), [智能体](</zh-CN/cli/agent>), [Models](</zh-CN/cli/models>), [OpenAI](</zh-CN/providers/openai>), [Anthropic](</zh-CN/providers/anthropic>), [Google](</zh-CN/providers/google>), [子智能体](</zh-CN/tools/subagents>)

流式传输和进度 2 项能力

Alpha 版56%

Beta 版79%

Beta 版79%

[流式传输](</zh-CN/concepts/streaming>), [Agent loop](</zh-CN/concepts/agent-loop>)

工具调用和响应处理 3 项能力 / LTS 支持

Alpha 版65%

Beta 版79%

Beta 版79%

[Agent loop](</zh-CN/concepts/agent-loop>), [Ollama](</zh-CN/providers/ollama>)

工具执行控制 6 项能力 / LTS 支持

早期版50%

测试版79%

测试版79%

[沙箱、工具策略和提升权限](</zh-CN/gateway/sandbox-vs-tool-policy-vs-elevated>), [Agent loop](</zh-CN/concepts/agent-loop>), [子智能体](</zh-CN/tools/subagents>)

会话、记忆和上下文引擎 - M3 Beta - 9 个领域

文档扎实且实现活跃。成熟度取决于转录记录持久性、压缩质量以及跨客户端一致性。

覆盖率 实验性 - 30%质量 Beta - 77%完整性 Beta - 79%部分 - 6

CLI 会话和转录管理 2 项能力 / LTS 支持

实验性0%

早期版68%

测试版79%

[会话](</zh-CN/concepts/session>), [会话管理压缩](</zh-CN/reference/session-management-compaction>), [会话](</zh-CN/cli/sessions>)

令牌管理 3 项能力 / LTS 支持

实验性20%

测试版79%

测试版79%

[压缩](</zh-CN/concepts/compaction>), [上下文](</zh-CN/concepts/context>), [会话管理压缩](</zh-CN/reference/session-management-compaction>)

上下文引擎 2 项能力 / LTS 支持

早期版57%

测试版79%

测试版79%

[上下文](</zh-CN/concepts/context>), [上下文引擎](</zh-CN/concepts/context-engine>), [Codex 上下文引擎 Harness](</zh-CN/plan/codex-context-engine-harness>)

跨客户端历史记录和会话一致性 2 项能力

实验性40%

测试版79%

测试版79%

[Webchat](</zh-CN/web/webchat>), [Android](</zh-CN/platforms/android>), [频道路由](</zh-CN/channels/channel-routing>)

诊断、维护和恢复 3 项能力

实验性40%

测试版79%

测试版79%

[诊断](</zh-CN/gateway/diagnostics>), [会话管理压缩](</zh-CN/reference/session-management-compaction>), [标志](</zh-CN/diagnostics/flags>)

核心提示词和上下文 2 项能力 / LTS 支持

实验性38%

测试版79%

测试版79%

[上下文](</zh-CN/concepts/context>), [转录卫生](</zh-CN/reference/transcript-hygiene>), [Discord](</zh-CN/channels/discord>)

记忆 5 项能力

实验性46%

测试版79%

测试版79%

[记忆配置](</zh-CN/reference/memory-config>), [Memory Qmd](</zh-CN/concepts/memory-qmd>), [记忆](</zh-CN/concepts/memory>), [Discord](</zh-CN/channels/discord>)

会话路由 2 项能力 / LTS 支持

实验性25%

测试版79%

测试版79%

[会话](</zh-CN/concepts/session>), [频道路由](</zh-CN/channels/channel-routing>), [Discord](</zh-CN/channels/discord>)

转录持久化 2 项能力 / LTS 支持

实验性0%

Alpha 阶段68%

Beta 阶段79%

[会话管理压缩](</zh-CN/reference/session-management-compaction>), [转录清理](</zh-CN/reference/transcript-hygiene>)

渠道框架 - M3 Beta - 8 个领域

许多渠道共享 Gateway 网关交付和路由契约，但渠道行为会因上游 API 和账号策略约束而异。

覆盖范围 实验性 - 13%质量 Beta - 76%完整性 Beta - 79%部分 - 5

频道操作命令和审批 5 项能力

实验性0%

Beta 版79%

Beta 版79%

[群组](</zh-CN/channels/groups>), [Discord](</zh-CN/channels/discord>), [Googlechat](</zh-CN/channels/googlechat>), [Signal](</zh-CN/channels/signal>), [Matrix](</zh-CN/channels/matrix>)

频道设置 5 项能力 / LTS 支持

实验性14%

Beta 版79%

Beta 版79%

[索引](</zh-CN/channels>), [配对](</zh-CN/channels/pairing>), [故障排除](</zh-CN/channels/troubleshooting>), [SDK 渠道插件](</zh-CN/plugins/sdk-channel-plugins>)

群组线程和环境房间行为 5 项能力

实验性36%

Beta 版79%

Beta 版79%

[群组](</zh-CN/channels/groups>), [群组消息](</zh-CN/channels/group-messages>), [环境房间事件](</zh-CN/channels/ambient-room-events>), [广播群组](</zh-CN/channels/broadcast-groups>), [Discord](</zh-CN/channels/discord>)

入站访问和身份门控 5 项能力 / LTS 支持

实验性0%

Alpha 版68%

Beta 版79%

[访问群组](</zh-CN/channels/access-groups>), [群组](</zh-CN/channels/groups>), [Discord](</zh-CN/channels/discord>), [LINE](</zh-CN/channels/line>)

媒体附件和丰富频道数据 4 项能力

实验性0%

Alpha 版68%

Beta 版79%

[LINE](</zh-CN/channels/line>), [Signal](</zh-CN/channels/signal>), [Googlechat](</zh-CN/channels/googlechat>), [Matrix](</zh-CN/channels/matrix>), [Discord](</zh-CN/channels/discord>)

出站投递和回复流水线 4 项能力 / LTS 支持

实验性38%

Beta 版79%

Beta 版79%

[群组](</zh-CN/channels/groups>), [环境房间事件](</zh-CN/channels/ambient-room-events>), [Discord](</zh-CN/channels/discord>), [Matrix](</zh-CN/channels/matrix>), [配置频道](</zh-CN/gateway/config-channels>)

对话路由和投递 10 项能力 / LTS 支持

实验性19%

Beta 版79%

Beta 版79%

[频道路由](</zh-CN/channels/channel-routing>), [群组](</zh-CN/channels/groups>), [Discord](</zh-CN/channels/discord>), [Matrix](</zh-CN/channels/matrix>), [故障排除](</zh-CN/channels/troubleshooting>), [配置参考](</zh-CN/gateway/configuration-reference>)

状态健康和操作员控制 4 项能力 / LTS 支持

实验性0%

Beta 版79%

测试版79%

[健康](</zh-CN/gateway/health>), [配置参考](</zh-CN/gateway/configuration-reference>), [故障排除](</zh-CN/channels/troubleshooting>), [Discord](</zh-CN/channels/discord>)

Observability - M3 Beta - 5 areas

OTel、Prometheus、日志和诊断文档已经存在。需要一次面向公开文档的“运维人员应优先查看什么”的成熟度完善。

覆盖率实验性 - 18%质量 Beta - 75%完整性 Beta - 79%部分 - 3

健康与修复 12 项能力 / LTS 支持

实验性28%

Beta79%

Beta79%

[健康](</zh-CN/gateway/health>), [Telegram](</zh-CN/channels/telegram>), [Doctor](</zh-CN/cli/doctor>), [Doctor](</zh-CN/gateway/doctor>), [Sdk 子路径](</zh-CN/plugins/sdk-subpaths>), [健康](</zh-CN/cli/health>), [协议](</zh-CN/gateway/protocol>)

日志 5 项能力 / LTS 支持

实验性0%

Alpha68%

Beta79%

[日志](</zh-CN/logging>), [日志](</zh-CN/gateway/logging>), [日志](</zh-CN/cli/logs>)

诊断收集 8 项能力

实验性30%

Beta79%

Beta79%

[诊断](</zh-CN/gateway/diagnostics>), [健康](</zh-CN/gateway/health>), [Codex harness](</zh-CN/plugins/codex-harness>), [协议](</zh-CN/gateway/protocol>)

遥测导出 13 项能力

实验性33%

Beta79%

Beta79%

[钩子](</zh-CN/plugins/hooks>), [Opentelemetry](</zh-CN/gateway/opentelemetry>), [日志](</zh-CN/logging>), [Sdk 子路径](</zh-CN/plugins/sdk-subpaths>), [诊断 Otel](</zh-CN/plugins/reference/diagnostics-otel>), [Prometheus](</zh-CN/gateway/prometheus>), [诊断 Prometheus](</zh-CN/plugins/reference/diagnostics-prometheus>)

会话诊断 4 项能力 / LTS 支持

实验性0%

Alpha68%

Beta79%

[Opentelemetry](</zh-CN/gateway/opentelemetry>), [Prometheus](</zh-CN/gateway/prometheus>), [诊断](</zh-CN/gateway/diagnostics>), [协议](</zh-CN/gateway/protocol>)

Gateway 网关 Web App - M3 Beta - 6 个领域

Web UI 已记录配对、聊天、PWA、Talk、推送和远程 Gateway 网关流程。待跨浏览器和移动端 PWA 评分卡完成后再升级。

覆盖率实验性 - 4%质量 Beta - 74%完整性 Beta - 79%无

浏览器实时 Talk 5 项能力

实验性0%

Alpha68%

Beta79%

[Control Ui](</zh-CN/web/control-ui>), [Protocol](</zh-CN/gateway/protocol>), [Talk](</zh-CN/nodes/talk>)

浏览器访问与信任 5 项能力

实验性0%

Alpha68%

Beta79%

[Control Ui](</zh-CN/web/control-ui>), [Dashboard](</zh-CN/web/dashboard>), [Tailscale](</zh-CN/gateway/tailscale>), [远程](</zh-CN/gateway/remote>)

配置 5 项能力

实验性0%

Alpha68%

Beta79%

[Control Ui](</zh-CN/web/control-ui>), [配置](</zh-CN/gateway/configuration>)

浏览器 UI 10 项能力

实验性8%

Beta79%

Beta79%

[Control Ui](</zh-CN/web/control-ui>), [索引](</zh-CN/web>), [Dashboard](</zh-CN/web/dashboard>), [Protocol](</zh-CN/gateway/protocol>)

WebChat 对话 15 项能力

实验性10%

Beta79%

Beta79%

[Control Ui](</zh-CN/web/control-ui>), [Webchat](</zh-CN/web/webchat>), [入门指南](</zh-CN/start/getting-started>), [频道路由](</zh-CN/channels/channel-routing>), [安全文件操作](</zh-CN/gateway/security/secure-file-operations>)

操作员控制台 10 项能力

实验性8%

Beta79%

Beta79%

[Control Ui](</zh-CN/web/control-ui>), [健康](</zh-CN/gateway/health>), [Protocol](</zh-CN/gateway/protocol>), [Dashboard](</zh-CN/web/dashboard>)

插件 - M3 Beta - 9 个领域

在清单、设备发现、加载、提供商/工具架构和审批边界方面，已有广泛文档和强内部运行时证据。在公共 SDK API/子路径和外部分发证明更强之前，将该行保持在 Beta。

覆盖率 实验性 - 12%质量 Beta - 72%完整性 Beta - 79%部分 - 7

创作和打包插件 8 项能力 / LTS 支持

实验性0%

内测版68%

测试版79%

[Building Plugins](</zh-CN/plugins/building-plugins>), [SDK 概览](</zh-CN/plugins/sdk-overview>), [SDK 入口点](</zh-CN/plugins/sdk-entrypoints>), [SDK 子路径](</zh-CN/plugins/sdk-subpaths>), [清单](</zh-CN/plugins/manifest>), [参考](</zh-CN/plugins/reference>)

内置插件 5 项能力 / LTS 支持

实验性0%

内测版68%

测试版79%

[插件清单](</zh-CN/plugins/plugin-inventory>), [插件](</zh-CN/cli/plugins>), [架构内部机制](</zh-CN/plugins/architecture-internals>)

Canvas 插件 6 项能力

实验性0%

内测版68%

测试版79%

[Canvas](</zh-CN/plugins/reference/canvas>), [Canvas](</zh-CN/refactor/canvas>), [配置参考](</zh-CN/gateway/configuration-reference>)

安装和运行插件 6 项能力 / LTS 支持

实验性35%

测试版79%

测试版79%

[架构](</zh-CN/plugins/architecture>), [架构内部机制](</zh-CN/plugins/architecture-internals>), [插件](</zh-CN/cli/plugins>)

渠道插件 5 项能力 / LTS 支持

实验性0%

内测版68%

测试版79%

[SDK 渠道插件](</zh-CN/plugins/sdk-channel-plugins>), [SDK 渠道入站](</zh-CN/plugins/sdk-channel-inbound>), [SDK 渠道出站](</zh-CN/plugins/sdk-channel-outbound>)

提供商和工具插件 6 项能力 / LTS 支持

实验性43%

测试版79%

测试版79%

[SDK 提供商插件](</zh-CN/plugins/sdk-provider-plugins>), [工具插件](</zh-CN/plugins/tool-plugins>), [添加能力](</zh-CN/plugins/adding-capabilities>)

插件审批 6 项能力 / LTS 支持

实验性0%

内测版68%

测试版79%

[插件权限请求](</zh-CN/plugins/plugin-permission-requests>), [Exec 审批](</zh-CN/tools/exec-approvals>), [SDK 渠道插件](</zh-CN/plugins/sdk-channel-plugins>)

发布插件 6 项能力 / LTS 支持

实验性0%

内测版68%

Beta 版79%

[插件](</zh-CN/cli/plugins>), [兼容性](</zh-CN/plugins/compatibility>), [发布](</zh-CN/clawhub/publishing>)

测试插件 6 项能力

实验性27%

Beta 版79%

Beta 版79%

[SDK 测试](</zh-CN/plugins/sdk-testing>), [SDK 设置](</zh-CN/plugins/sdk-setup>), [Codex Harness](</zh-CN/plugins/codex-harness>)

安全、凭证、配对和密钥 - M3 Beta - 6 个领域

已有完善的文档和加固表面。定期升级和安全场景运行证明没有设置回归后再提升。

覆盖率 Experimental - 16%质量 Beta - 72%完整性 Beta - 79%部分 - 5

审批策略和工具防护 2 项能力 / LTS 支持

Alpha50%

Beta79%

Beta79%

[Exec 审批](</zh-CN/tools/exec-approvals>), [审批](</zh-CN/cli/approvals>), [插件权限请求](</zh-CN/plugins/plugin-permission-requests>), [审计检查](</zh-CN/gateway/security/audit-checks>)

Gateway 网关凭证和远程访问 9 项能力 / LTS 支持

Experimental0%

Alpha68%

Beta79%

[索引](</zh-CN/gateway/security>), [暴露运行手册](</zh-CN/gateway/security/exposure-runbook>), [受信代理凭证](</zh-CN/gateway/trusted-proxy-auth>), [Tailscale](</zh-CN/gateway/tailscale>), [远程](</zh-CN/gateway/remote>), [配置参考](</zh-CN/gateway/configuration-reference>), [Gateway 网关](</zh-CN/cli/gateway>), [Doctor](</zh-CN/cli/doctor>), [Control Ui](</zh-CN/web/control-ui>), [浏览器控制](</zh-CN/tools/browser-control>), [审计检查](</zh-CN/gateway/security/audit-checks>)

频道访问控制 3 项能力 / LTS 支持

Experimental0%

Alpha68%

Beta79%

[配对](</zh-CN/channels/pairing>), [Telegram](</zh-CN/channels/telegram>), [访问组](</zh-CN/channels/access-groups>), [审计检查](</zh-CN/gateway/security/audit-checks>)

设备和节点配对 11 项能力 / LTS 支持

Experimental0%

Alpha68%

Beta79%

[协议](</zh-CN/gateway/protocol>), [设备](</zh-CN/cli/devices>), [配对](</zh-CN/channels/pairing>), [配对](</zh-CN/gateway/pairing>), [操作员作用域](</zh-CN/gateway/operator-scopes>), [Control Ui](</zh-CN/web/control-ui>), [Webchat](</zh-CN/web/webchat>), [审批](</zh-CN/cli/approvals>)

插件信任 2 项能力

Experimental0%

Alpha68%

Beta79%

[清单](</zh-CN/plugins/manifest>), [插件权限请求](</zh-CN/plugins/plugin-permission-requests>), [管理插件](</zh-CN/plugins/manage-plugins>), [审计检查](</zh-CN/gateway/security/audit-checks>)

凭据和密钥卫生 5 项能力 / LTS 支持

Experimental46%

Beta79%

Beta79%

[身份验证](</zh-CN/gateway/authentication>), [Models](</zh-CN/cli/models>), [Openai](</zh-CN/providers/openai>), [Oauth](</zh-CN/concepts/oauth>), [密钥](</zh-CN/gateway/secrets>), [密钥](</zh-CN/cli/secrets>), [Secretref 凭据表面](</zh-CN/reference/secretref-credential-surface>), [审计检查](</zh-CN/gateway/security/audit-checks>)

自动化：cron、钩子、任务、轮询 - M3 Beta - 6 个领域

已记录且可用，但场景证明应覆盖无人值守交付、重试和故障可见性。

覆盖率 Experimental - 2%质量 Beta - 72%完整性 Beta - 79%无

Cron Jobs 15 项能力

实验性0%

Beta79%

Beta79%

[Cron Jobs](</zh-CN/automation/cron-jobs>), [Cron](</zh-CN/cli/cron>), [协议](</zh-CN/gateway/protocol>), [任务](</zh-CN/automation/tasks>), [Discord](</zh-CN/channels/discord>)

事件入口 15 项能力

实验性0%

Alpha68%

Beta79%

[Telegram](</zh-CN/channels/telegram>), [Zalo](</zh-CN/channels/zalo>), [故障排除](</zh-CN/channels/troubleshooting>), [Imessage From Bluebubbles](</zh-CN/channels/imessage-from-bluebubbles>), [Gmail Pubsub 集成](</zh-CN/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pubsub](</zh-CN/automation/cron-jobs>), [Webhooks](</zh-CN/cli/webhooks>), [Webhooks](</zh-CN/automation/cron-jobs#webhooks>), [Webhook](</zh-CN/automation/cron-jobs>)

自动化钩子 11 项能力

实验性0%

Alpha68%

Beta79%

[钩子](</zh-CN/automation/hooks>), [钩子](</zh-CN/cli/hooks>), [钩子](</zh-CN/plugins/hooks>), [插件权限请求](</zh-CN/plugins/plugin-permission-requests>), [插件 SDK 子路径](</zh-CN/plugins/sdk-subpaths>)

后台任务和流程 10 项能力

实验性0%

Alpha68%

Beta79%

[任务](</zh-CN/automation/tasks>), [索引](</zh-CN/automation>), [任务](</zh-CN/cli/tasks>), [Taskflow](</zh-CN/automation/taskflow>), [SDK 运行时](</zh-CN/plugins/sdk-runtime>)

Heartbeat 5 项能力

实验性14%

Beta79%

Beta79%

[索引](</zh-CN/automation>), [Heartbeat](</zh-CN/gateway/heartbeat>), [跟进承诺](</zh-CN/concepts/commitments>)

轮询控制 10 项能力

实验性0%

Alpha68%

Beta79%

[轮询](</zh-CN/cli/message>), [消息](</zh-CN/cli/message>), [Telegram](</zh-CN/channels/telegram>), [Msteams](</zh-CN/channels/msteams>), [后台进程](</zh-CN/gateway/background-process>)

媒体理解和媒体生成 - M2 Alpha - 6 个领域

已有广泛的能力表面，但提供商差异、文件限制以及节点/应用一致性让它尚未稳定。

覆盖率 实验性 - 2%质量 Alpha - 64%完整性 Alpha - 68%无

媒体摄取与访问 8 项能力

实验性0%

Alpha 版61%

Alpha 版68%

[媒体概览](</zh-CN/tools/media-overview>), [媒体理解](</zh-CN/nodes/media-understanding>), [安全文件操作](</zh-CN/gateway/security/secure-file-operations>), [PDF](</zh-CN/tools/pdf>), [图像生成](</zh-CN/tools/image-generation>), [QR](</zh-CN/cli/qr>), [LINE](</zh-CN/channels/line>), [WhatsApp](</zh-CN/channels/whatsapp>)

渠道媒体处理 5 项能力

实验性0%

Alpha 版61%

Alpha 版68%

[图像](</zh-CN/nodes/images>), [媒体概览](</zh-CN/tools/media-overview>), [Discord](</zh-CN/channels/discord>)

媒体配置 1 项能力

实验性0%

Alpha 版61%

Alpha 版68%

[媒体概览](</zh-CN/tools/media-overview>), [图像生成](</zh-CN/tools/image-generation>), [清单](</zh-CN/plugins/manifest>), [Codex harness](</zh-CN/plugins/codex-harness>)

文本转语音交付 2 项能力

实验性0%

Alpha 版61%

Alpha 版68%

[TTS](</zh-CN/tools/tts>), [媒体概览](</zh-CN/tools/media-overview>), [Discord](</zh-CN/channels/discord>)

媒体理解 12 项能力

实验性7%

Alpha 版69%

Alpha 版69%

[音频](</zh-CN/nodes/audio>), [媒体理解](</zh-CN/nodes/media-understanding>), [媒体概览](</zh-CN/tools/media-overview>), [WhatsApp](</zh-CN/channels/whatsapp>), [图像](</zh-CN/nodes/images>), [推理](</zh-CN/cli/infer>), [PDF](</zh-CN/tools/pdf>)

媒体生成 17 项能力

实验性5%

Alpha 版69%

Alpha 版69%

[图像生成](</zh-CN/tools/image-generation>), [媒体概览](</zh-CN/tools/media-overview>), [Skills](</zh-CN/tools/skills>), [音乐生成](</zh-CN/tools/music-generation>), [视频生成](</zh-CN/tools/video-generation>)

语音和实时对话 - M2 Alpha 版 - 6 个领域

Control UI、应用和提供商中存在多个实现。进入 beta 版之前，需要完成延迟、故障模式和设置评分卡。

覆盖率 实验性 - 0%质量 Alpha 版 - 61%完整性 Alpha 版 - 68%无

对话提供商 7 项能力

实验性0%

Alpha61%

Alpha68%

[OpenAI](</zh-CN/providers/openai>), [Google](</zh-CN/providers/google>), [SDK 提供商插件](</zh-CN/plugins/sdk-provider-plugins>), [对话](</zh-CN/nodes/talk>), [Control UI](</zh-CN/web/control-ui>)

实时对话会话 11 项能力

实验性0%

Alpha61%

Alpha68%

[对话](</zh-CN/nodes/talk>), [Control UI](</zh-CN/web/control-ui>)

语音和转录 5 项能力

实验性0%

Alpha61%

Alpha68%

[对话](</zh-CN/nodes/talk>), [OpenAI](</zh-CN/providers/openai>), [Google](</zh-CN/providers/google>)

原生应用对话 4 项能力

实验性0%

Alpha61%

Alpha68%

[对话](</zh-CN/nodes/talk>), [Voicewake](</zh-CN/platforms/mac/voicewake>)

语音唤醒和路由 4 项能力

实验性0%

Alpha61%

Alpha68%

[Voicewake](</zh-CN/nodes/voicewake>), [Voicewake](</zh-CN/platforms/mac/voicewake>), [语音叠加层](</zh-CN/platforms/mac/voice-overlay>)

对话可观测性 5 项能力

实验性0%

Alpha61%

Alpha68%

[Control UI](</zh-CN/web/control-ui>), [语音叠加层](</zh-CN/platforms/mac/voice-overlay>), [对话](</zh-CN/nodes/talk>)

TUI - M2 Alpha - 5 个领域

文档和源码中已有，但作为主要用户工作流的可见性较低。需要明确的场景定义。

覆盖率：实验性 - 0%质量：Alpha - 59%完整性：Alpha - 66%无

运行时模式 14 项能力

实验性0%

Alpha59%

Alpha66%

[Tui](</zh-CN/cli/tui>), [Tui](</zh-CN/web/tui>), [索引](</zh-CN/cli>)

输入和命令 8 项能力

实验性0%

Alpha59%

Alpha66%

[Tui](</zh-CN/web/tui>)

会话管理 3 项能力

实验性0%

Alpha59%

Alpha66%

[Tui](</zh-CN/web/tui>), [会话](</zh-CN/cli/sessions>)

本地 Shell 执行 4 项能力

实验性0%

Alpha59%

Alpha66%

[Tui](</zh-CN/web/tui>), [Tui](</zh-CN/cli/tui>)

渲染和输出安全 4 项能力

实验性0%

Alpha59%

Alpha66%

[Tui](</zh-CN/web/tui>), [二维码](</zh-CN/cli/qr>), [日志](</zh-CN/cli/logs>), [补全](</zh-CN/cli/completion>)

ClawHub - M2 Alpha - 4 个领域

公共文档和生态系统概念已经存在。还需要安装、信任、更新、回滚和兼容性评分卡。

覆盖率：实验性 - 0%质量：Alpha - 58%完整性：Alpha - 62%无

发布 7 项能力

实验性0%

Alpha 版54%

Alpha 版55%

[发布](</zh-CN/clawhub/publishing>), [创建技能](</zh-CN/tools/creating-skills>), [社区](</zh-CN/plugins/community>)

目录发现 5 项能力

实验性0%

Alpha 版61%

Alpha 版68%

[插件](</zh-CN/tools/plugin>), [插件](</zh-CN/cli/plugins>), [Skills](</zh-CN/cli/skills>), [Skills](</zh-CN/tools/skills>), [社区](</zh-CN/plugins/community>)

兼容性与信任 12 项能力

实验性0%

Alpha 版55%

Alpha 版56%

[插件](</zh-CN/tools/plugin>), [插件](</zh-CN/cli/plugins>), [兼容性](</zh-CN/plugins/compatibility>), [插件清单](</zh-CN/plugins/plugin-inventory>), [发布](</zh-CN/clawhub/publishing>), [Skills](</zh-CN/tools/skills>), [Skills 配置](</zh-CN/tools/skills-config>)

插件生命周期和健康状况 26 项能力

实验性0%

Alpha 版61%

Alpha 版68%

[插件](</zh-CN/tools/plugin>), [插件](</zh-CN/cli/plugins>), [Skills](</zh-CN/cli/skills>), [Skills](</zh-CN/tools/skills>), [协议](</zh-CN/gateway/protocol>), [捆绑包](</zh-CN/plugins/bundles>), [依赖解析](</zh-CN/plugins/dependency-resolution>)

OpenClaw App SDK - M2 Alpha - 6 areas

OpenClaw App SDK 是一个独立的外部应用契约，区别于 Gateway 网关运行时和插件 SDK。当前评分显示存在真实的 `@openclaw/sdk` 路径，但在公开打包、自动发现、审批、辅助工具和兼容性方面仍有缺口。

覆盖率实验性 - 3%质量 Alpha - 54%完整性 Alpha - 53%无

客户端 API 4 项能力

实验性0%

Alpha51%

Alpha50%

[OpenClaw SDK](</zh-CN/gateway/external-apps>), [OpenClaw SDK API 设计](</zh-CN/gateway/external-apps>)

Gateway 网关访问 5 项能力

实验性0%

Alpha53%

Alpha54%

[OpenClaw SDK](</zh-CN/gateway/external-apps>), [OpenClaw SDK API 设计](</zh-CN/gateway/external-apps>), [协议](</zh-CN/gateway/protocol>), [索引](</zh-CN/gateway/security>)

Agent 对话 6 项能力

实验性0%

Alpha52%

Alpha52%

[OpenClaw SDK](</zh-CN/gateway/external-apps>), [OpenClaw SDK API 设计](</zh-CN/gateway/external-apps>), [协议](</zh-CN/gateway/protocol>)

事件与审批 5 项能力

实验性0%

Alpha52%

Alpha52%

[OpenClaw SDK](</zh-CN/gateway/external-apps>), [OpenClaw SDK API 设计](</zh-CN/gateway/external-apps>), [协议](</zh-CN/gateway/protocol>)

资源辅助工具 5 项能力

实验性17%

Alpha62%

Alpha53%

[OpenClaw SDK](</zh-CN/gateway/external-apps>), [OpenClaw SDK API 设计](</zh-CN/gateway/external-apps>)

兼容性 5 项能力

实验性0%

Alpha54%

Alpha55%

[OpenClaw SDK API 设计](</zh-CN/gateway/external-apps>), [Typebox](</zh-CN/concepts/typebox>), [协议](</zh-CN/gateway/protocol>)

### 平台

Linux Gateway 网关主机 - M4 稳定版 - 5 个领域

推荐使用 Node 运行时，已记录 systemd 用户服务，并且 VPS/容器指南覆盖较广。

覆盖范围 实验性 - 0%质量 Beta - 75%完整性 稳定版 - 89%部分 - 4

主机设置和更新 4 项能力 / LTS 支持

实验性0%

Beta75%

稳定89%

[索引](</zh-CN/install>), [更新](</zh-CN/install/updating>), [Linux](</zh-CN/platforms/linux>), [索引](</zh-CN/platforms>)

Gateway 网关运行时和服务控制 6 项能力 / LTS 支持

实验性0%

Beta75%

稳定89%

[索引](</zh-CN/gateway>), [Gateway 网关](</zh-CN/cli/gateway>), [Linux](</zh-CN/platforms/linux>), [VPS](</zh-CN/vps>)

远程访问和安全 6 项能力 / LTS 支持

实验性0%

Beta75%

稳定89%

[远程](</zh-CN/gateway/remote>), [Tailscale](</zh-CN/gateway/tailscale>), [暴露运行手册](</zh-CN/gateway/security/exposure-runbook>), [身份验证](</zh-CN/gateway/authentication>), [密钥](</zh-CN/gateway/secrets>)

诊断和修复 4 项能力 / LTS 支持

实验性0%

Beta75%

稳定89%

[状态](</zh-CN/cli/status>), [日志](</zh-CN/cli/logs>), [Doctor](</zh-CN/cli/doctor>), [诊断](</zh-CN/gateway/diagnostics>), [索引](</zh-CN/gateway>)

部署目标 3 项能力

实验性0%

Beta75%

稳定89%

[VPS](</zh-CN/vps>), [Docker](</zh-CN/install/docker>), [Hetzner](</zh-CN/install/hetzner>), [Digitalocean](</zh-CN/install/digitalocean>), [Kubernetes](</zh-CN/install/kubernetes>), [Podman](</zh-CN/install/podman>)

macOS Gateway host - M4 Stable - 7 areas

LaunchAgent 服务路径、本地/远程 Gateway 网关模式、CLI 安装和应用集成都已有文档说明。

覆盖率 实验性 - 0%质量 Beta - 74%完整性 稳定 - 88%无

CLI 设置 4 项能力

实验性0%

测试版74%

稳定版88%

[macOS](</zh-CN/platforms/macos>), [内置 Gateway 网关](</zh-CN/platforms/mac/bundled-gateway>), [安装器](</zh-CN/install/installer>), [Node](</zh-CN/install/node>)

本地 Gateway 网关集成 9 项能力

实验性0%

测试版74%

稳定版88%

[macOS](</zh-CN/platforms/macos>), [内置 Gateway 网关](</zh-CN/platforms/mac/bundled-gateway>), [远程](</zh-CN/platforms/mac/remote>), [索引](</zh-CN/gateway>), [Gateway 网关](</zh-CN/cli/gateway>), [Bonjour](</zh-CN/gateway/bonjour>)

远程 Gateway 网关模式 5 项能力

实验性0%

测试版74%

稳定版88%

[远程](</zh-CN/platforms/mac/remote>), [远程](</zh-CN/gateway/remote>), [Tailscale](</zh-CN/gateway/tailscale>)

Gateway 网关服务生命周期 10 项能力

实验性0%

测试版74%

稳定版88%

[macOS](</zh-CN/platforms/macos>), [内置 Gateway 网关](</zh-CN/platforms/mac/bundled-gateway>), [Gateway 网关](</zh-CN/cli/gateway>), [索引](</zh-CN/gateway>), [更新](</zh-CN/cli/update>), [更新](</zh-CN/install/updating>), [卸载](</zh-CN/install/uninstall>), [故障排除](</zh-CN/gateway/troubleshooting>)

诊断和可观测性 4 项能力

实验性0%

测试版74%

稳定版88%

[内置 Gateway 网关](</zh-CN/platforms/mac/bundled-gateway>), [macOS](</zh-CN/platforms/macos>), [Gateway 网关](</zh-CN/cli/gateway>), [Doctor](</zh-CN/gateway/doctor>), [故障排除](</zh-CN/gateway/troubleshooting>)

权限和原生能力 4 项能力

实验性0%

测试版74%

稳定版88%

[macOS](</zh-CN/platforms/macos>), [远程](</zh-CN/platforms/mac/remote>)

配置档和隔离 5 项能力

实验性0%

测试版74%

稳定版88%

[多个 Gateway 网关](</zh-CN/gateway/multiple-gateways>), [索引](</zh-CN/gateway>), [Gateway 网关](</zh-CN/cli/gateway>)

Docker 和 Podman 托管 - M3 测试版 - 4 个领域

安装文档已存在，并且是常见的部署路径。在持续发布冒烟测试捕获升级和卷行为后再提升成熟度。

覆盖率实验性 - 7%质量测试版 - 71%完整性测试版 - 79%无

容器设置 6 项能力

实验性0%

Alpha 版68%

Beta 版79%

[Docker](</zh-CN/install/docker>), [Podman](</zh-CN/install/podman>)

容器运维 11 项能力

实验性0%

Alpha 版68%

Beta 版79%

[Podman](</zh-CN/install/podman>), [Docker VM 运行时](</zh-CN/install/docker-vm-runtime>), [Docker](</zh-CN/install/docker>), [Hetzner](</zh-CN/install/hetzner>), [Hostinger](</zh-CN/install/hostinger>)

镜像发布和验证 5 项能力

实验性29%

Beta 版79%

Beta 版79%

[Docker](</zh-CN/install/docker>), [Docker VM 运行时](</zh-CN/install/docker-vm-runtime>), [完整发布验证](</zh-CN/reference/full-release-validation>)

Agent 沙箱和工具链 3 项能力

实验性0%

Alpha 版68%

Beta 版79%

[Docker](</zh-CN/install/docker>), [Docker VM 运行时](</zh-CN/install/docker-vm-runtime>)

通过 WSL2 使用 Windows - M3 Beta 版 - 6 个领域

推荐的 Windows 路径，包含 systemd/用户服务指导和启动链文档。在重复的安装/更新评分卡通过后再提升成熟度。

覆盖率 实验性 - 6%质量 Alpha 版 - 69%完整性 Beta 版 - 79%部分 - 5

WSL 设置 6 项能力 / LTS 支持

实验性0%

Alpha 版67%

Beta 版79%

[Windows](</zh-CN/platforms/windows>), [入门指南](</zh-CN/start/getting-started>)

CLI 8 项能力 / LTS 支持

实验性0%

Alpha 版67%

Beta 版79%

[Windows](</zh-CN/platforms/windows>), [入门指南](</zh-CN/start/getting-started>), [更新](</zh-CN/install/updating>), [新手引导](</zh-CN/cli/onboard>), [Doctor](</zh-CN/cli/doctor>), [状态](</zh-CN/cli/status>), [日志](</zh-CN/cli/logs>)

Gateway 网关服务生命周期 10 项能力 / LTS 支持

实验性0%

Alpha 版67%

Beta 版79%

[Windows](</zh-CN/platforms/windows>), [索引](</zh-CN/gateway>), [Doctor](</zh-CN/gateway/doctor>)

Gateway 网关访问和暴露 11 项能力 / LTS 支持

实验性0%

Alpha 版67%

Beta 版79%

[身份验证](</zh-CN/gateway/authentication>), [密钥](</zh-CN/gateway/secrets>), [远程](</zh-CN/gateway/remote>), [暴露运行手册](</zh-CN/gateway/security/exposure-runbook>), [Windows](</zh-CN/platforms/windows>)

诊断和修复 6 项能力 / LTS 支持

实验性38%

Beta 版79%

Beta 版79%

[Windows](</zh-CN/platforms/windows>), [状态](</zh-CN/cli/status>), [日志](</zh-CN/cli/logs>), [Doctor](</zh-CN/cli/doctor>), [Doctor](</zh-CN/gateway/doctor>)

浏览器和 Control UI 6 项能力

实验性0%

Alpha 版67%

Beta 版79%

[浏览器 WSL2 Windows 远程 CDP 故障排除](</zh-CN/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [浏览器](</zh-CN/tools/browser>), [Control UI](</zh-CN/web/control-ui>)

Raspberry Pi 和小型 Linux 设备 - M3 Beta 版 - 4 个领域

平台文档已存在，且 Gateway 网关路径基于 Linux。需要硬件特定的发布冒烟验证，才能提升到更高成熟度。

覆盖率实验性 - 0%质量 Alpha 版 - 67%完整度 Beta 版 - 79%无

设置与兼容性 12 项能力

实验性0%

Alpha67%

Beta79%

[Raspberry Pi](</zh-CN/install/raspberry-pi>), [索引](</zh-CN/install>), [首次运行常见问题](</zh-CN/help/faq-first-run>), [常见问题](</zh-CN/help/faq>), [Linux](</zh-CN/platforms/linux>), [安装程序](</zh-CN/install/installer>)

远程访问和认证 9 项能力

实验性0%

Alpha67%

Beta79%

[Raspberry Pi](</zh-CN/install/raspberry-pi>), [认证](</zh-CN/gateway/authentication>), [密钥](</zh-CN/gateway/secrets>), [配对](</zh-CN/gateway/pairing>), [设备](</zh-CN/cli/devices>), [远程](</zh-CN/gateway/remote>), [Tailscale](</zh-CN/gateway/tailscale>)

Gateway 网关运行时 10 项能力

实验性0%

Alpha67%

Beta79%

[索引](</zh-CN/gateway>), [Gateway 网关](</zh-CN/cli/gateway>), [Raspberry Pi](</zh-CN/install/raspberry-pi>), [Linux](</zh-CN/platforms/linux>), [VPS](</zh-CN/vps>)

性能和诊断 5 项能力

实验性0%

Alpha67%

Beta79%

[Raspberry Pi](</zh-CN/install/raspberry-pi>), [Linux](</zh-CN/platforms/linux>), [健康](</zh-CN/gateway/health>), [诊断](</zh-CN/gateway/diagnostics>)

macOS 配套应用 - M3 Beta - 8 个领域

丰富的菜单栏应用、权限、节点模式、Canvas、语音唤醒、WebChat 和远程模式已经存在。它仍然变化较快，因此尚不进入稳定版。

覆盖率 实验性 - 0%质量 Alpha - 66%完整性 Beta - 78%无

画布 4 项能力

实验性0%

Alpha 版66%

Beta 版78%

[画布](</zh-CN/platforms/mac/canvas>), [macOS](</zh-CN/platforms/macos>), [Webchat](</zh-CN/web/webchat>)

本地设置 7 项能力

实验性0%

Alpha 版66%

Beta 版78%

[内置 Gateway 网关](</zh-CN/platforms/mac/bundled-gateway>), [macOS](</zh-CN/platforms/macos>), [子进程](</zh-CN/platforms/mac/child-process>), [开发设置](</zh-CN/platforms/mac/dev-setup>)

状态和设置 5 项能力

实验性0%

Alpha 版66%

Beta 版78%

[菜单栏](</zh-CN/platforms/mac/menu-bar>), [图标](</zh-CN/platforms/mac/icon>), [macOS](</zh-CN/platforms/macos>), [健康](</zh-CN/platforms/mac/health>), [日志](</zh-CN/platforms/mac/logging>), [远程](</zh-CN/platforms/mac/remote>)

原生能力 5 项能力

实验性0%

Alpha 版66%

Beta 版78%

[macOS](</zh-CN/platforms/macos>), [XPC](</zh-CN/platforms/mac/xpc>), [权限](</zh-CN/platforms/mac/permissions>), [签名](</zh-CN/platforms/mac/signing>), [Peekaboo](</zh-CN/platforms/mac/peekaboo>)

远程连接 3 项能力

实验性0%

Alpha 版66%

Beta 版78%

[远程](</zh-CN/platforms/mac/remote>), [macOS](</zh-CN/platforms/macos>), [远程](</zh-CN/gateway/remote>)

语音和 Talk 3 项能力

实验性0%

Alpha 版66%

Beta 版78%

[语音唤醒](</zh-CN/platforms/mac/voicewake>), [语音叠加层](</zh-CN/platforms/mac/voice-overlay>), [Talk](</zh-CN/nodes/talk>), [macOS](</zh-CN/platforms/macos>)

WebChat 3 项能力

实验性0%

Alpha 版66%

Beta 版78%

[Webchat](</zh-CN/platforms/mac/webchat>), [macOS](</zh-CN/platforms/macos>), [Webchat](</zh-CN/web/webchat>)

远程 WebChat 5 项能力

实验性0%

Alpha 版66%

Beta 版78%

[Webchat](</zh-CN/platforms/mac/webchat>), [远程](</zh-CN/gateway/remote>), [远程](</zh-CN/platforms/mac/remote>)

Android 应用 - M2 Alpha - 7 个领域

已有公开的 Google Play 路径，但应用文档仍将这次重建描述为极早期 Alpha，并指出发布加固工作。

覆盖率 实验性 - 0%质量 Alpha - 59%完整性 Alpha - 66%无

媒体采集 1 项能力

实验性0%

Alpha59%

Alpha66%

[Android](</zh-CN/platforms/android>), [摄像头](</zh-CN/nodes/camera>)

移动聊天 1 项能力

实验性0%

Alpha59%

Alpha66%

[Android](</zh-CN/platforms/android>)

连接设置 1 项能力

实验性0%

Alpha59%

Alpha66%

[Android](</zh-CN/platforms/android>), [Bonjour](</zh-CN/gateway/bonjour>), [配对](</zh-CN/gateway/pairing>)

分发 3 项能力

实验性0%

Alpha59%

Alpha66%

[Android](</zh-CN/platforms/android>)

设置 1 项能力

实验性0%

Alpha59%

Alpha66%

[Android](</zh-CN/platforms/android>)

语音 1 项能力

实验性0%

Alpha59%

Alpha66%

[Android](</zh-CN/platforms/android>), [Talk](</zh-CN/nodes/talk>)

设备运行时 2 项能力

实验性0%

Alpha59%

Alpha66%

[Android](</zh-CN/platforms/android>), [故障排除](</zh-CN/nodes/troubleshooting>), [协议](</zh-CN/gateway/protocol>)

原生 Windows - M2 Alpha - 4 个领域

核心 CLI/Gateway 网关流程可用，但文档仍建议使用 WSL2 以获得完整体验，并列出了原生环境的注意事项。

覆盖率 实验性 - 0%质量 Alpha - 58%完整度 Alpha - 66%部分 - 1

CLI 9 项能力 / LTS 支持

实验性0%

Alpha 版54%

Alpha 版64%

[索引](</zh-CN/install>), [安装器](</zh-CN/install/installer>), [Windows](</zh-CN/platforms/windows>), [入门指南](</zh-CN/start/getting-started>), [新手引导](</zh-CN/cli/onboard>)

Gateway 网关管理 11 项能力

实验性0%

Alpha 版59%

Alpha 版66%

[Windows](</zh-CN/platforms/windows>), [索引](</zh-CN/gateway>), [Gateway 网关](</zh-CN/cli/gateway>), [Doctor](</zh-CN/cli/doctor>)

网络 4 项能力

实验性0%

Alpha 版59%

Alpha 版66%

[Windows](</zh-CN/platforms/windows>), [索引](</zh-CN/gateway>), [Gateway 网关](</zh-CN/cli/gateway>)

更新 4 项能力

实验性0%

Alpha 版59%

Alpha 版66%

[更新](</zh-CN/install/updating>), [CI](</zh-CN/ci>)

Kubernetes 托管 - M2 Alpha 版 - 4 个领域

Kubernetes 托管是一条独立的、基于 Kustomize 的集群部署路径。当前评分显示，它已经具备真实的最小部署路径，但在 Kubernetes 专用 CI、ingress/TLS/NetworkPolicy 打包、备份/恢复以及生产环境暴露加固方面仍存在缺口。

覆盖率 实验性 - 0%质量 Alpha - 55%完整性 Alpha - 61%无

部署设置 5 项能力

实验性0%

Alpha55%

Alpha61%

[Kubernetes](</zh-CN/install/kubernetes>), [索引](</zh-CN/install>)

配置和密钥 5 项能力

实验性0%

Alpha55%

Alpha61%

[Kubernetes](</zh-CN/install/kubernetes>), [密钥](</zh-CN/gateway/secrets>), [环境](</zh-CN/help/environment>)

访问和暴露 5 项能力

实验性0%

Alpha55%

Alpha61%

[Kubernetes](</zh-CN/install/kubernetes>), [身份验证](</zh-CN/gateway/authentication>), [远程](</zh-CN/gateway/remote>), [暴露运行手册](</zh-CN/gateway/security/exposure-runbook>)

集群生命周期 5 项能力

实验性0%

Alpha55%

Alpha61%

[Kubernetes](</zh-CN/install/kubernetes>), [索引](</zh-CN/gateway>)

iOS app - M1 实验性 - 8 个区域

内部预览 / 超早期 alpha。TestFlight 和基于中继的推送流程已存在，但尚未公开分发。

覆盖率实验性 - 0%质量实验性 - 41%完整性实验性 - 44%无

媒体和共享 1 项能力

实验性0%

实验性41%

实验性44%

[Ios](</zh-CN/platforms/ios>), [相机](</zh-CN/nodes/camera>)

画布和屏幕 1 项能力

实验性0%

实验性41%

实验性44%

[Ios](</zh-CN/platforms/ios>), [画布](</zh-CN/plugins/reference/canvas>)

聊天和会话 1 项能力

实验性0%

实验性41%

实验性44%

[Ios](</zh-CN/platforms/ios>), [网页聊天](</zh-CN/web/webchat>), [协议](</zh-CN/gateway/protocol>)

Gateway 网关设置和诊断 7 项能力

实验性0%

实验性41%

实验性44%

[Ios](</zh-CN/platforms/ios>), [配对](</zh-CN/channels/pairing>)

分发 1 项能力

实验性0%

实验性41%

实验性44%

[Ios](</zh-CN/platforms/ios>)

设备命令 2 项能力

实验性0%

实验性41%

实验性44%

[Ios](</zh-CN/platforms/ios>), [协议](</zh-CN/gateway/protocol>)

通知和后台 1 项能力

实验性0%

实验性41%

实验性44%

[Ios](</zh-CN/platforms/ios>), [配置](</zh-CN/gateway/configuration>)

语音 1 项能力

实验性0%

实验性41%

实验性44%

[Ios](</zh-CN/platforms/ios>), [Talk](</zh-CN/nodes/talk>)

Nix 安装路径 - M1 实验性 - 5 个区域

可选安装流程。在提升到 alpha/beta 之前，需要更清晰的支持承诺。

覆盖率 实验性 - 0%质量 实验性 - 41%完整性 实验性 - 44%无

安装交接 4 项能力

实验性0%

实验性41%

实验性44%

[Nix](</zh-CN/install/nix>), [索引](</zh-CN/install>), [文档目录](</zh-CN/start/docs-directory>)

插件生命周期 4 项能力

实验性0%

实验性41%

实验性44%

[管理插件](</zh-CN/plugins/manage-plugins>), [插件](</zh-CN/tools/plugin>), [Nix](</zh-CN/install/nix>)

激活和应用 UX 7 项能力

实验性0%

实验性41%

实验性44%

[Nix](</zh-CN/install/nix>)

配置和状态 7 项能力

实验性0%

实验性41%

实验性44%

[Nix](</zh-CN/install/nix>), [设置](</zh-CN/cli/setup>), [环境](</zh-CN/help/environment>)

服务运行时和防护 8 项能力

实验性0%

实验性41%

实验性44%

[Nix](</zh-CN/install/nix>), [设置](</zh-CN/cli/setup>), [Doctor](</zh-CN/cli/doctor>), [更新](</zh-CN/cli/update>)

watchOS 配套应用界面 - M1 实验性 - 5 个领域

源码包含 Watch 应用/扩展界面；公开文档尚未将其作为用户功能呈现。

覆盖率 实验性 - 0%质量 实验性 - 41%完整性 实验性 - 44%无

交付和恢复 7 项能力

实验性0%

实验性41%

实验性44%

[iOS](</zh-CN/platforms/ios>)

Exec 审批 3 项能力

实验性0%

实验性41%

实验性44%

[Exec 审批](</zh-CN/tools/exec-approvals>), [iOS](</zh-CN/platforms/ios>)

分发和支持 6 项能力

实验性0%

实验性41%

实验性44%

[iOS](</zh-CN/platforms/ios>)

通知和回复 7 项能力

实验性0%

实验性41%

实验性44%

[iOS](</zh-CN/platforms/ios>)

手表应用 UI 3 项能力

实验性0%

实验性41%

实验性44%

[iOS](</zh-CN/platforms/ios>)

Linux 配套应用 - M0 已计划 - 5 个领域

文档说明原生 Linux 配套应用已在计划中；Gateway 网关是目前支持的 Linux 路径。

覆盖率实验性 - 0%质量实验性 - 19%完整度实验性 - 21%无

应用分发 3 项能力

实验性0%

实验性19%

实验性21%

[Linux](</zh-CN/platforms/linux>), [索引](</zh-CN/platforms>), [索引](</zh-CN/install>)

Gateway 网关连接 4 项能力

实验性0%

实验性19%

实验性21%

[Linux](</zh-CN/platforms/linux>), [索引](</zh-CN/gateway>), [配对](</zh-CN/gateway/pairing>), [远程](</zh-CN/gateway/remote>)

聊天和会话 3 项能力

实验性0%

实验性19%

实验性21%

[Linux](</zh-CN/platforms/linux>), [协议](</zh-CN/gateway/protocol>), [Webchat](</zh-CN/web/webchat>)

桌面能力 9 项能力

实验性0%

实验性19%

实验性21%

[Linux](</zh-CN/platforms/linux>), [Exec 审批](</zh-CN/tools/exec-approvals>), [密钥](</zh-CN/gateway/secrets>), [索引](</zh-CN/nodes>), [Exec](</zh-CN/tools/exec>), [Talk](</zh-CN/nodes/talk>), [相机](</zh-CN/nodes/camera>)

状态和诊断 7 项能力

实验性0%

实验性19%

实验性21%

[Linux](</zh-CN/platforms/linux>), [OpenClaw](</zh-CN/start/openclaw>), [Doctor](</zh-CN/gateway/doctor>)

原生 Windows 配套应用 - M0 已计划 - 5 个领域

仅计划中。

覆盖率 实验性 - 0%质量 实验性 - 19%完整度 实验性 - 21%无

安装和更新 4 项能力

实验性0%

实验性19%

实验性21%

[Windows](</zh-CN/platforms/windows>), [索引](</zh-CN/install>)

Gateway 网关连接 3 项能力

实验性0%

实验性19%

实验性21%

[Windows](</zh-CN/platforms/windows>), [索引](</zh-CN/gateway>), [配对](</zh-CN/gateway/pairing>), [远程](</zh-CN/gateway/remote>)

聊天会话 2 项能力

实验性0%

实验性19%

实验性21%

[Windows](</zh-CN/platforms/windows>), [协议](</zh-CN/gateway/protocol>)

状态和修复 5 项能力

实验性0%

实验性19%

实验性21%

[Windows](</zh-CN/platforms/windows>), [Doctor](</zh-CN/gateway/doctor>), [索引](</zh-CN/gateway>)

桌面工具和权限 10 项能力

实验性0%

实验性19%

实验性21%

[Windows](</zh-CN/platforms/windows>), [索引](</zh-CN/nodes>), [Exec](</zh-CN/tools/exec>), [Exec 审批](</zh-CN/tools/exec-approvals>), [索引](</zh-CN/gateway/security>)

### 渠道

Discord - M4 稳定 - 6 个领域

深入的文档和广泛的功能覆盖。语音/委派路径应继续单独评为 beta/alpha。

覆盖率实验性 - 0%质量 Beta - 73%完整性稳定 - 87%部分 - 4

频道设置和运维 10 项能力 / LTS 支持

实验性0%

Beta73%

稳定87%

[Discord](</zh-CN/channels/discord>), [Discord](</zh-CN/plugins/reference/discord>), [Fly](</zh-CN/install/fly>), [斜杠命令](</zh-CN/tools/slash-commands>), [健康](</zh-CN/gateway/health>), [频道](</zh-CN/cli/channels>), [配置频道](</zh-CN/gateway/config-channels>)

访问和身份 6 项能力 / LTS 支持

实验性0%

Beta73%

稳定87%

[Discord](</zh-CN/channels/discord>), [配对](</zh-CN/channels/pairing>), [访问组](</zh-CN/channels/access-groups>), [群组](</zh-CN/channels/groups>)

会话路由和投递 12 项能力 / LTS 支持

实验性0%

Beta73%

稳定87%

[Discord](</zh-CN/channels/discord>), [频道路由](</zh-CN/channels/channel-routing>), [群组](</zh-CN/channels/groups>), [访问组](</zh-CN/channels/access-groups>), [Acp 智能体](</zh-CN/tools/acp-agents>), [子智能体](</zh-CN/tools/subagents>)

媒体和富内容 1 项能力 / LTS 支持

实验性0%

Beta73%

稳定87%

[Discord](</zh-CN/channels/discord>)

原生控制和审批 5 项能力

实验性0%

Beta73%

稳定87%

[Discord](</zh-CN/channels/discord>), [斜杠命令](</zh-CN/tools/slash-commands>)

实时语音和通话 5 项能力

实验性0%

Beta73%

稳定87%

[Discord](</zh-CN/channels/discord>), [Openai](</zh-CN/providers/openai>), [Elevenlabs](</zh-CN/providers/elevenlabs>), [Qa E2e 自动化](</zh-CN/concepts/qa-e2e-automation>), [配置频道](</zh-CN/gateway/config-channels>)

Telegram - M3 Beta - 5 个领域

核心频道已经足够成熟，可用于常规使用，但高差异性的用户体验和媒体边缘情况需要反复的场景证明。

覆盖率 实验性 - 0%质量 Alpha - 68%完整性 Beta - 78%完整 - 5

渠道设置和运维 10 项能力 / LTS 支持

实验性0%

早期版66%

测试版78%

[Telegram](</zh-CN/channels/telegram>), [配置渠道](</zh-CN/gateway/config-channels>), [渠道](</zh-CN/cli/channels>)

访问和身份 10 项能力 / LTS 支持

实验性0%

早期版66%

测试版78%

[Telegram](</zh-CN/channels/telegram>), [配对](</zh-CN/channels/pairing>), [访问组](</zh-CN/channels/access-groups>), [群组](</zh-CN/channels/groups>), [多 Agent](</zh-CN/concepts/multi-agent>)

对话路由和交付 1 项能力 / LTS 支持

实验性0%

早期版66%

测试版78%

[Telegram](</zh-CN/channels/telegram>), [群组](</zh-CN/channels/groups>), [多 Agent](</zh-CN/concepts/multi-agent>)

媒体和富内容 1 项能力 / LTS 支持

实验性0%

早期版66%

测试版78%

[Telegram](</zh-CN/channels/telegram>), [位置](</zh-CN/channels/location>)

原生控制和审批 9 项能力 / LTS 支持

实验性0%

测试版77%

测试版79%

[Telegram](</zh-CN/channels/telegram>), [Exec 审批](</zh-CN/tools/exec-approvals>), [回应](</zh-CN/tools/reactions>)

Slack - M3 Beta - 5 areas

一流的渠道文档和路由表面。需要工作区安装/管理员场景评分卡。

覆盖率实验性 - 0%质量早期版 - 66%完整性测试版 - 78%完整 - 5

频道设置和运维 10 项能力 / LTS 支持

实验性0%

阿尔法66%

Beta 版78%

[Slack](</zh-CN/channels/slack>), [Slack](</zh-CN/plugins/reference/slack>), [密钥](</zh-CN/gateway/secrets>), [QA E2E 自动化](</zh-CN/concepts/qa-e2e-automation>), [故障排除](</zh-CN/channels/troubleshooting>)

访问和身份 1 项能力 / LTS 支持

实验性0%

阿尔法66%

Beta 版78%

[Slack](</zh-CN/channels/slack>), [配对](</zh-CN/channels/pairing>)

对话路由和投递 5 项能力 / LTS 支持

实验性0%

阿尔法66%

Beta 版78%

[Slack](</zh-CN/channels/slack>), [机器人循环保护](</zh-CN/channels/bot-loop-protection>), [配对](</zh-CN/channels/pairing>)

媒体和富内容 1 项能力 / LTS 支持

实验性0%

阿尔法66%

Beta 版78%

[Slack](</zh-CN/channels/slack>), [QA E2E 自动化](</zh-CN/concepts/qa-e2e-automation>)

原生控制和审批 8 项能力 / LTS 支持

实验性0%

阿尔法66%

Beta 版78%

[Slack](</zh-CN/channels/slack>), [斜杠命令](</zh-CN/tools/slash-commands>), [Exec 审批](</zh-CN/tools/exec-approvals>)

iMessage 和 BlueBubbles - M3 Beta 版 - 5 个领域

受支持的 iMessage 通过已登录的 macOS Messages 主机上的 imsg 运行；旧版 BlueBubbles 配置需要迁移。保持 macOS 权限、SSH 包装器、SIP/私有 API 和迁移注意事项可见。

覆盖率 实验性 - 0%质量 阿尔法 - 66%完整性 Beta 版 - 78%无

频道设置和操作 11 项能力

实验性0%

阿尔法66%

测试版78%

[BlueBubbles iMessage](</zh-CN/announcements/bluebubbles-imessage>), [来自 BlueBubbles 的 iMessage](</zh-CN/channels/imessage-from-bluebubbles>), [配置频道](</zh-CN/gateway/config-channels>), [iMessage](</zh-CN/channels/imessage>)

访问和身份 6 项能力

实验性0%

阿尔法66%

测试版78%

[iMessage](</zh-CN/channels/imessage>), [来自 BlueBubbles 的 iMessage](</zh-CN/channels/imessage-from-bluebubbles>), [配置频道](</zh-CN/gateway/config-channels>)

对话路由和递送 4 项能力

实验性0%

阿尔法66%

测试版78%

[iMessage](</zh-CN/channels/imessage>)

媒体和富内容 7 项能力

实验性0%

阿尔法66%

测试版78%

[iMessage](</zh-CN/channels/imessage>), [来自 BlueBubbles 的 iMessage](</zh-CN/channels/imessage-from-bluebubbles>), [配置频道](</zh-CN/gateway/config-channels>)

原生控制和审批 3 项能力

实验性0%

阿尔法66%

测试版78%

[iMessage](</zh-CN/channels/imessage>)

WhatsApp - M3 测试版 - 5 个领域

核心路径很重要且已有文档记录；上游 Baileys/会话波动性使其低于稳定版。

覆盖率实验性 - 0%质量阿尔法 - 66%完整度测试版 - 78%无

频道设置和运维 5 项能力

实验性0%

Alpha 版66%

Beta 版78%

[WhatsApp](</zh-CN/channels/whatsapp>), [配置频道](</zh-CN/gateway/config-channels>), [WhatsApp](</zh-CN/plugins/reference/whatsapp>), [QA E2E 自动化](</zh-CN/concepts/qa-e2e-automation>), [Doctor](</zh-CN/gateway/doctor>)

访问和身份 7 项能力

实验性0%

Alpha 版66%

Beta 版78%

[WhatsApp](</zh-CN/channels/whatsapp>), [配置频道](</zh-CN/gateway/config-channels>), [QA E2E 自动化](</zh-CN/concepts/qa-e2e-automation>), [配对](</zh-CN/channels/pairing>)

对话路由和投递 4 项能力

实验性0%

Alpha 版66%

Beta 版78%

[WhatsApp](</zh-CN/channels/whatsapp>), [群组消息](</zh-CN/channels/group-messages>)

媒体和富内容 2 项能力

实验性0%

Alpha 版66%

Beta 版78%

[WhatsApp](</zh-CN/channels/whatsapp>)

原生控制和审批 2 项能力

实验性0%

Alpha 版66%

Beta 版78%

[WhatsApp](</zh-CN/channels/whatsapp>)

Matrix - M2 Alpha - 6 areas

通过内置插件支持。需要桥接、认证和房间生命周期评分卡。

覆盖率 实验性 - 0%质量 Alpha 版 - 60%完整性 Alpha 版 - 67%无

频道设置和运维 5 项能力

实验性0%

Alpha60%

Alpha67%

[Matrix](</zh-CN/channels/matrix>), [Matrix 迁移](</zh-CN/channels/matrix-migration>)

访问与身份 7 项能力

实验性0%

Alpha60%

Alpha67%

[Matrix](</zh-CN/channels/matrix>), [群组](</zh-CN/channels/groups>), [机器人循环保护](</zh-CN/channels/bot-loop-protection>)

对话路由和投递 1 项能力

实验性0%

Alpha60%

Alpha67%

[Matrix](</zh-CN/channels/matrix>)

媒体和富内容 1 项能力

实验性0%

Alpha60%

Alpha67%

[Matrix](</zh-CN/channels/matrix>)

原生控制和审批 6 项能力

实验性0%

Alpha60%

Alpha67%

[Matrix](</zh-CN/channels/matrix>)

加密和验证 3 项能力

实验性0%

Alpha60%

Alpha67%

[Matrix](</zh-CN/channels/matrix>), [Matrix 迁移](</zh-CN/channels/matrix-migration>)

Google Chat - M2 Alpha - 5 个领域

已记录文档的渠道，但企业/管理员设置会带来成熟度风险。

覆盖率实验性 - 0%质量 Alpha - 59%完整性 Alpha - 66%无

频道设置和操作 16 项能力

实验性0%

Alpha59%

Alpha66%

[Googlechat](</zh-CN/channels/googlechat>), [Googlechat](</zh-CN/plugins/reference/googlechat>), [配置频道](</zh-CN/gateway/config-channels>), [向导 CLI 参考](</zh-CN/start/wizard-cli-reference>), [密钥](</zh-CN/gateway/secrets>), [Secretref 凭据表面](</zh-CN/reference/secretref-credential-surface>), [健康](</zh-CN/gateway/health>), [插件清单](</zh-CN/plugins/plugin-inventory>), [索引](</zh-CN/channels>)

访问和身份 11 项能力

实验性0%

Alpha59%

Alpha66%

[Googlechat](</zh-CN/channels/googlechat>), [配对](</zh-CN/channels/pairing>), [访问组](</zh-CN/channels/access-groups>), [配置频道](</zh-CN/gateway/config-channels>), [Bot 循环保护](</zh-CN/channels/bot-loop-protection>), [频道路由](</zh-CN/channels/channel-routing>)

对话路由和投递 1 项能力

实验性0%

Alpha59%

Alpha66%

[Googlechat](</zh-CN/channels/googlechat>), [Bot 循环保护](</zh-CN/channels/bot-loop-protection>), [访问组](</zh-CN/channels/access-groups>), [频道路由](</zh-CN/channels/channel-routing>)

媒体和富内容 1 项能力

实验性0%

Alpha59%

Alpha66%

[Googlechat](</zh-CN/channels/googlechat>), [消息](</zh-CN/cli/message>), [媒体理解](</zh-CN/nodes/media-understanding>), [Secretref 凭据表面](</zh-CN/reference/secretref-credential-surface>)

原生控制和审批 16 项能力

实验性0%

Alpha59%

Alpha66%

[Googlechat](</zh-CN/channels/googlechat>), [消息](</zh-CN/cli/message>), [媒体理解](</zh-CN/nodes/media-understanding>), [Secretref 凭据表面](</zh-CN/reference/secretref-credential-surface>), [回应](</zh-CN/tools/reactions>), [斜杠命令](</zh-CN/tools/slash-commands>), [配置智能体](</zh-CN/gateway/config-agents>), [消息生命周期重构](</zh-CN/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alpha - 5 个领域

企业身份验证/管理员流程需要明确的场景证明。

覆盖率实验性 - 0%质量 Alpha - 59%完整性 Alpha - 66%无

渠道设置和运维 9 项能力

实验性0%

Alpha59%

Alpha66%

[Msteams](</zh-CN/channels/msteams>), [Msteams](</zh-CN/plugins/reference/msteams>), [配置渠道](</zh-CN/gateway/config-channels>), [健康](</zh-CN/gateway/health>)

访问和身份 9 项能力

实验性0%

Alpha59%

Alpha66%

[Msteams](</zh-CN/channels/msteams>), [配对](</zh-CN/channels/pairing>), [访问组](</zh-CN/channels/access-groups>)

对话路由和投递 5 项能力

实验性0%

Alpha59%

Alpha66%

[Msteams](</zh-CN/channels/msteams>), [群组](</zh-CN/channels/groups>), [频道路由](</zh-CN/channels/channel-routing>)

媒体和富内容 5 项能力

实验性0%

Alpha59%

Alpha66%

[Msteams](</zh-CN/channels/msteams>)

原生控制和审批 5 项能力

实验性0%

Alpha59%

Alpha66%

[Msteams](</zh-CN/channels/msteams>), [Exec 高级审批](</zh-CN/tools/exec-approvals-advanced>)

Signal - M2 Alpha - 5 个领域

已有受支持的渠道文档；需要更强的安装和重新连接证明。

覆盖率 实验性 - 0%质量 Alpha - 59%完整度 Alpha - 66%无

频道设置和运维 7 项能力

实验性0%

Alpha59%

Alpha66%

[Signal](</zh-CN/channels/signal>), [Signal](</zh-CN/plugins/reference/signal>)

访问和身份 6 项能力

实验性0%

Alpha59%

Alpha66%

[Signal](</zh-CN/channels/signal>)

会话路由和投递 1 项能力

实验性0%

Alpha59%

Alpha66%

[Signal](</zh-CN/channels/signal>)

媒体和富内容 7 项能力

实验性0%

Alpha59%

Alpha66%

[Signal](</zh-CN/channels/signal>)

原生控制和审批 3 项能力

实验性0%

Alpha59%

Alpha66%

[Signal](</zh-CN/channels/signal>)

Feishu、QQ Bot、微信、腾讯元宝、Zalo、Zalo Personal、区域频道 - M2 Alpha - 4 个领域

重要的区域覆盖，但公开支持级别应根据账号类型、上游批准和维护者证明逐项校准。

覆盖率实验性 - 0%质量 Alpha - 55%完整性 Alpha - 58%无

频道设置和运维 6 项能力

实验性0%

Alpha 版61%

Alpha 版68%

[索引](</zh-CN/channels>), [配对](</zh-CN/channels/pairing>), [Feishu](</zh-CN/plugins/reference/feishu>), [架构内部机制](</zh-CN/plugins/architecture-internals>)

访问和身份 1 项能力

实验性0%

Alpha 版53%

Alpha 版54%

没有关联文档

对话路由和投递 1 项能力

实验性0%

Alpha 版53%

Alpha 版54%

没有关联文档

媒体和富内容 1 项能力

实验性0%

Alpha 版53%

Alpha 版54%

没有关联文档

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 Alpha - 4 areas

已存在受支持的表面，但成熟度可能因上游和维护者覆盖范围而异。之后再逐项评分。

覆盖率为实验性 - 0%质量为 Alpha 版 - 53%完整性为 Alpha 版 - 54%无

渠道设置和运维 1 项能力

实验性0%

Alpha53%

Alpha54%

无关联文档

访问和身份 1 项能力

实验性0%

Alpha53%

Alpha54%

无关联文档

对话路由和交付 1 项能力

实验性0%

Alpha53%

Alpha54%

无关联文档

媒体和富内容 1 项能力

实验性0%

Alpha53%

Alpha54%

无关联文档

语音通话渠道 - M1 实验性 - 5 个领域

可选/插件路径，具有复杂的实时行为。公开 beta 前需要场景评分卡。

覆盖率 实验性 - 0%质量 实验性 - 41%完整性 实验性 - 44%无

频道设置和操作 2 项能力

实验性0%

实验性41%

实验性44%

[Voicecall](</zh-CN/cli/voicecall>), [Voice Call](</zh-CN/plugins/voice-call>), [协议](</zh-CN/gateway/protocol>)

访问和身份 1 项能力

实验性0%

实验性41%

实验性44%

[Voice Call](</zh-CN/plugins/voice-call>), [Voicecall](</zh-CN/cli/voicecall>)

对话路由和投递 1 项能力

实验性0%

实验性41%

实验性44%

[Voice Call](</zh-CN/plugins/voice-call>)

媒体和富内容 2 项能力

实验性0%

实验性41%

实验性44%

[Voice Call](</zh-CN/plugins/voice-call>), [插件清单](</zh-CN/plugins/plugin-inventory>)

实时语音和通话 2 项能力

实验性0%

实验性41%

实验性44%

[Voice Call](</zh-CN/plugins/voice-call>)

### 提供商和工具

浏览器自动化、exec 和沙箱工具 - M3 Beta - 3 个领域

核心工具已有文档，但主机安全和权限用户体验应继续接受活跃的评分卡审查。

覆盖率实验性 - 21%质量 Beta - 75%完整性 Beta - 79%部分 - 2

浏览器自动化 8 项能力

实验性13%

Beta79%

Beta79%

[浏览器控制](</zh-CN/tools/browser-control>), [测试](</zh-CN/help/testing>), [浏览器](</zh-CN/tools/browser>), [索引](</zh-CN/gateway/security>), [审计检查](</zh-CN/gateway/security/audit-checks>)

工具调用和执行 6 项能力 / LTS 支持

Alpha50%

Beta79%

Beta79%

[Exec](</zh-CN/tools/exec>), [后台进程](</zh-CN/gateway/background-process>), [工具调用 HTTP API](</zh-CN/gateway/tools-invoke-http-api>), [操作员作用域](</zh-CN/gateway/operator-scopes>), [协议](</zh-CN/gateway/protocol>), [Exec 审批](</zh-CN/tools/exec-approvals>), [Exec 高级审批](</zh-CN/tools/exec-approvals-advanced>), [提升权限](</zh-CN/tools/elevated>)

沙箱和工具策略 6 项能力 / LTS 支持

实验性0%

Alpha68%

Beta79%

[沙箱隔离](</zh-CN/gateway/sandboxing>), [沙箱、工具策略和提升权限](</zh-CN/gateway/sandbox-vs-tool-policy-vs-elevated>), [多 Agent 沙盒工具](</zh-CN/tools/multi-agent-sandbox-tools>), [Codex harness reference](</zh-CN/plugins/codex-harness-reference>), [配置工具](</zh-CN/gateway/config-tools>)

OpenAI 和 Codex 提供商路径 - M3 Beta - 5 个领域

深入文档、OAuth/订阅路径、实时语音、图像和兼容性行为。提供商变动频繁，因此在没有发布评分卡证明的情况下无法达到 Stable。

覆盖率 实验性 - 26%质量 Beta - 74%完整性 Beta - 79%部分 - 3

模型和凭证 6 项能力 / LTS 支持

实验性44%

Beta 版79%

Beta 版79%

[OpenAI](</zh-CN/providers/openai>), [Codex harness](</zh-CN/plugins/codex-harness>), [Models](</zh-CN/concepts/models>), [OAuth](</zh-CN/concepts/oauth>), [Codex harness reference](</zh-CN/plugins/codex-harness-reference>), [凭证监控](</zh-CN/gateway/authentication>)

响应和工具兼容性 4 项能力 / LTS 支持

实验性40%

Beta 版79%

Beta 版79%

[OpenAI](</zh-CN/providers/openai>), [OpenResponses HTTP API](</zh-CN/gateway/openresponses-http-api>), [OpenAI HTTP API](</zh-CN/gateway/openai-http-api>), [Native Codex plugins](</zh-CN/plugins/codex-native-plugins>)

原生 Codex harness 2 项能力 / LTS 支持

实验性44%

Beta 版79%

Beta 版79%

[Codex harness](</zh-CN/plugins/codex-harness>), [Codex harness runtime](</zh-CN/plugins/codex-harness-runtime>), [Codex harness reference](</zh-CN/plugins/codex-harness-reference>), [Native Codex plugins](</zh-CN/plugins/codex-native-plugins>)

图像和多模态输入 2 项能力

实验性0%

Alpha 版67%

Beta 版79%

[OpenAI](</zh-CN/providers/openai>), [图像生成](</zh-CN/tools/image-generation>), [图像](</zh-CN/nodes/images>)

语音和实时音频 2 项能力

实验性0%

Alpha 版67%

Beta 版79%

[OpenAI](</zh-CN/providers/openai>), [Discord](</zh-CN/channels/discord>), [语音通话](</zh-CN/plugins/voice-call>)

Web 搜索工具 - M3 Beta 版 - 4 个领域

已有多个提供商和文档。需要按提供商系列提供配额、错误和 SSRF 证明。

覆盖率实验性 - 9%质量 Beta 版 - 74%完整性 Beta 版 - 79%无

搜索提供商 19 项能力

实验性11%

测试版79%

测试版79%

[Web](</zh-CN/tools/web>), [Brave Search](</zh-CN/tools/brave-search>), [Tavily](</zh-CN/tools/tavily>), [Exa Search](</zh-CN/tools/exa-search>), [Firecrawl](</zh-CN/tools/firecrawl>), [Perplexity Search](</zh-CN/tools/perplexity-search>), [Duckduckgo Search](</zh-CN/tools/duckduckgo-search>), [Searxng Search](</zh-CN/tools/searxng-search>), [Gemini Search](</zh-CN/tools/gemini-search>), [Grok Search](</zh-CN/tools/grok-search>), [Kimi Search](</zh-CN/tools/kimi-search>), [Minimax Search](</zh-CN/tools/minimax-search>), [Ollama Search](</zh-CN/tools/ollama-search>), [SDK 子路径](</zh-CN/plugins/sdk-subpaths>), [SDK 概览](</zh-CN/plugins/sdk-overview>), [清单](</zh-CN/plugins/manifest>)

设置和诊断 9 项能力

实验性0%

Alpha 版68%

测试版79%

[Web](</zh-CN/tools/web>), [Web 获取](</zh-CN/tools/web-fetch>), [常见问题](</zh-CN/help/faq>), [API 使用成本](</zh-CN/reference/api-usage-costs>), [Brave Search](</zh-CN/tools/brave-search>), [Perplexity Search](</zh-CN/tools/perplexity-search>), [Tavily](</zh-CN/tools/tavily>), [Firecrawl](</zh-CN/tools/firecrawl>)

网络安全 4 项能力

实验性0%

Alpha 版68%

测试版79%

[Web](</zh-CN/tools/web>), [Web 获取](</zh-CN/tools/web-fetch>), [Firecrawl](</zh-CN/tools/firecrawl>), [Searxng Search](</zh-CN/tools/searxng-search>)

工具可用性和获取 11 项能力

实验性25%

测试版79%

测试版79%

[配置工具](</zh-CN/gateway/config-tools>), [Web 获取](</zh-CN/tools/web-fetch>), [Web](</zh-CN/tools/web>), [常见问题](</zh-CN/help/faq>)

Anthropic 提供商路径 - M3 测试版 - 5 个领域

一等模型提供商。需要持续的凭证、目录和工具调用场景证明。

覆盖率 实验性 - 0%质量 测试版 - 71%完整性 测试版 - 78%无

提供商凭证和恢复 9 项能力

实验性0%

Alpha66%

Beta78%

[Anthropic](</zh-CN/providers/anthropic>), [Doctor](</zh-CN/gateway/doctor>), [配置示例](</zh-CN/gateway/configuration-examples>), [故障排除](</zh-CN/gateway/troubleshooting>), [提示缓存](</zh-CN/reference/prompt-caching>)

模型和运行时选择 10 项能力

实验性0%

Beta78%

Beta79%

[Anthropic](</zh-CN/providers/anthropic>), [配置智能体](</zh-CN/gateway/config-agents>), [Models](</zh-CN/concepts/models>), [CLI 后端](</zh-CN/gateway/cli-backends>)

请求传输和轮次语义 10 项能力

实验性0%

Beta77%

Beta79%

[Anthropic](</zh-CN/providers/anthropic>), [提示缓存](</zh-CN/reference/prompt-caching>), [故障排除](</zh-CN/gateway/troubleshooting>), [CLI 后端](</zh-CN/gateway/cli-backends>), [模型提供商](</zh-CN/concepts/model-providers>)

提示缓存和上下文 5 项能力

实验性0%

Alpha66%

Beta78%

[Anthropic](</zh-CN/providers/anthropic>), [提示缓存](</zh-CN/reference/prompt-caching>), [故障排除](</zh-CN/gateway/troubleshooting>), [Heartbeat](</zh-CN/gateway/heartbeat>)

媒体输入 4 项能力

实验性0%

Alpha66%

Beta78%

[Anthropic](</zh-CN/providers/anthropic>), [配置智能体](</zh-CN/gateway/config-agents>)

Google 提供商路径 - M3 Beta - 5 个领域

一流提供商，具备模型和实时能力表面。需要单独的 Live/Talk 评分。

覆盖率实验性 - 0%质量 Alpha - 66%完整性 Beta - 78%无

提供商设置和凭证 10 项能力

实验性0%

Alpha 阶段66%

Beta 阶段78%

[Google](</zh-CN/providers/google>), [模型提供商](</zh-CN/concepts/model-providers>)

模型路由和端点 10 项能力

实验性0%

Alpha 阶段66%

Beta 阶段78%

[Google](</zh-CN/providers/google>), [模型提供商](</zh-CN/concepts/model-providers>), [Google](</zh-CN/plugins/reference/google>), [Gemini 搜索](</zh-CN/tools/gemini-search>)

直接 Gemini 运行时 9 项能力

实验性0%

Alpha 阶段66%

Beta 阶段78%

[Google](</zh-CN/providers/google>), [模型提供商](</zh-CN/concepts/model-providers>), [FAQ 模型](</zh-CN/help/faq-models>), [实时测试](</zh-CN/help/testing-live>)

媒体、搜索和实时能力 10 项能力

实验性0%

Alpha 阶段66%

Beta 阶段78%

[Google](</zh-CN/plugins/reference/google>), [Google](</zh-CN/providers/google>)

提示缓存 5 项能力

实验性0%

Alpha 阶段66%

Beta 阶段78%

[提示缓存](</zh-CN/reference/prompt-caching>), [Google](</zh-CN/providers/google>), [模型提供商](</zh-CN/concepts/model-providers>), [Token 用量](</zh-CN/reference/token-use>)

OpenRouter 提供商路径 - M3 Beta 阶段 - 4 个领域

统一的提供商路径已有文档记录且具有价值，但模型特定行为会有所不同。

覆盖率实验性 - 0%质量 Alpha 阶段 - 66%完整性 Beta 阶段 - 78%无

提供商设置和身份验证 14 项能力

实验性0%

Alpha 版66%

Beta 版78%

[Openrouter](</zh-CN/providers/openrouter>), [模型提供商](</zh-CN/concepts/model-providers>), [配置](</zh-CN/cli/configure>), [身份验证](</zh-CN/gateway/authentication>), [环境](</zh-CN/help/environment>), [Models](</zh-CN/cli/models>), [Models](</zh-CN/concepts/models>)

聊天运行时和规范化 15 项能力

实验性0%

Alpha 版66%

Beta 版78%

[Openrouter](</zh-CN/providers/openrouter>), [模型提供商](</zh-CN/concepts/model-providers>), [提示缓存](</zh-CN/reference/prompt-caching>)

提供商恢复和诊断 5 项能力

实验性0%

Alpha 版66%

Beta 版78%

[模型故障转移](</zh-CN/concepts/model-failover>), [Openrouter](</zh-CN/providers/openrouter>), [Models](</zh-CN/cli/models>)

媒体生成和语音 7 项能力

实验性0%

Alpha 版66%

Beta 版78%

[Openrouter](</zh-CN/providers/openrouter>), [图像生成](</zh-CN/tools/image-generation>), [音乐生成](</zh-CN/tools/music-generation>), [媒体概览](</zh-CN/tools/media-overview>), [视频生成](</zh-CN/tools/video-generation>), [TTS](</zh-CN/tools/tts>)

图像、视频和音乐生成工具 - M2 Alpha 版 - 5 个领域

能力已跨提供商存在，但在没有逐提供商证明的情况下，质量、延迟和参数兼容性差异过大，尚不足以达到 Beta 版。

覆盖率实验性 - 0%质量 Alpha 版 - 61%完整性 Alpha 版 - 68%无

媒体路由和设备发现 4 项能力

实验性0%

阿尔法版61%

阿尔法版68%

[配置智能体](</zh-CN/gateway/config-agents>), [图像生成](</zh-CN/tools/image-generation>), [视频生成](</zh-CN/tools/video-generation>), [音乐生成](</zh-CN/tools/music-generation>)

任务生命周期和交付 12 项能力

实验性0%

阿尔法版61%

阿尔法版68%

[媒体概览](</zh-CN/tools/media-overview>), [图像生成](</zh-CN/tools/image-generation>), [视频生成](</zh-CN/tools/video-generation>), [音乐生成](</zh-CN/tools/music-generation>)

图像生成 9 项能力

实验性0%

阿尔法版61%

阿尔法版68%

[图像生成](</zh-CN/tools/image-generation>), [推理](</zh-CN/cli/infer>), [媒体概览](</zh-CN/tools/media-overview>)

视频生成 11 项能力

实验性0%

阿尔法版61%

阿尔法版68%

[视频生成](</zh-CN/tools/video-generation>), [Runway](</zh-CN/providers/runway>), [Pixverse](</zh-CN/providers/pixverse>), [Fal](</zh-CN/providers/fal>), [Openrouter](</zh-CN/providers/openrouter>)

音乐生成 6 项能力

实验性0%

阿尔法版61%

阿尔法版68%

[音乐生成](</zh-CN/tools/music-generation>)

本地模型提供商：Ollama、vLLM、SGLang、LM Studio - M2 阿尔法版 - 5 个领域

实用且有文档说明，但环境差异很大。

覆盖率 实验性 - 0%质量 阿尔法版 - 61%完整度 阿尔法版 - 68%无

提供商设置、生命周期和诊断 12 项能力

实验性0%

Alpha 阶段61%

Alpha 阶段68%

[本地模型](</zh-CN/gateway/local-models>), [Lmstudio](</zh-CN/providers/lmstudio>), [Ollama](</zh-CN/providers/ollama>), [Vllm](</zh-CN/providers/vllm>), [本地模型服务](</zh-CN/gateway/local-model-services>), [配置智能体](</zh-CN/gateway/config-agents>), [故障排除](</zh-CN/gateway/troubleshooting>), [Doctor](</zh-CN/gateway/doctor>)

原生提供商插件 10 项能力

实验性0%

Alpha 阶段61%

Alpha 阶段68%

[Ollama](</zh-CN/providers/ollama>), [Lmstudio](</zh-CN/providers/lmstudio>)

OpenAI 兼容运行时兼容性 8 项能力

实验性0%

Alpha 阶段61%

Alpha 阶段68%

[Vllm](</zh-CN/providers/vllm>), [Sglang](</zh-CN/providers/sglang>), [本地模型](</zh-CN/gateway/local-models>), [Lmstudio](</zh-CN/providers/lmstudio>)

本地记忆和嵌入 5 项能力

实验性0%

Alpha 阶段61%

Alpha 阶段68%

[记忆](</zh-CN/concepts/memory>), [Doctor](</zh-CN/gateway/doctor>)

网络安全和提示词控制 2 项能力

实验性0%

Alpha 阶段61%

Alpha 阶段68%

[索引](</zh-CN/gateway/security>), [配置工具](</zh-CN/gateway/config-tools>), [本地模型](</zh-CN/gateway/local-models>)

长尾托管提供商 - M2 Alpha 阶段 - 3 个领域

许多文档/参考页面已经存在；评分应根据提供商元数据和实时冒烟测试覆盖范围生成。

覆盖率 Experimental - 0%质量 Alpha - 61%完整性 Alpha - 68%无

托管 LLM 提供商 12 项能力

Experimental0%

Alpha61%

Alpha68%

[索引](</zh-CN/providers>), [模型提供商](</zh-CN/concepts/model-providers>), [实时测试](</zh-CN/help/testing-live>), [新手引导](</zh-CN/cli/onboard>)

托管媒体提供商 8 项能力

Experimental0%

Alpha61%

Alpha68%

[清单](</zh-CN/plugins/manifest>), [实时测试](</zh-CN/help/testing-live>), [索引](</zh-CN/providers>)

提供商运维 12 项能力

Experimental0%

Alpha61%

Alpha68%

[索引](</zh-CN/providers>), [模型提供商](</zh-CN/concepts/model-providers>), [清单](</zh-CN/plugins/manifest>), [实时测试](</zh-CN/help/testing-live>), [Models](</zh-CN/cli/models>)