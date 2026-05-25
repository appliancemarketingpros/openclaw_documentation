---
title: 烟花
source_url: https://docs.openclaw.ai/zh-CN/providers/fireworks
scraped_at: 2026-05-25
---

[Fireworks](<https://fireworks.ai>) 通过 OpenAI 兼容 API 暴露开放权重模型和路由模型。OpenClaw 包含一个内置的 Fireworks provider 插件，随附两个预编目的 Kimi 模型，并在运行时接受任何 Fireworks 模型或路由器 id。

属性 | 值  
---|---  
提供商 id | `fireworks`（别名：`fireworks-ai`）  
插件 | 内置，`enabledByDefault: true`  
凭证环境变量 | `FIREWORKS_API_KEY`  
新手引导标志 | `--auth-choice fireworks-api-key`  
直接 CLI 标志 | `--fireworks-api-key <key>`  
API | OpenAI 兼容（`openai-completions`）  
基础 URL | `https://api.fireworks.ai/inference/v1`  
默认模型 | `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`  
默认别名 | `Kimi K2.5 Turbo`  
  
## 入门指南

* ### 设置 Fireworks API key

OnboardingCopy code
[code]
    openclaw onboard --auth-choice fireworks-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice fireworks-api-key \--fireworks-api-key "$FIREWORKS_API_KEY"
[/code]

Env onlyCopy code
[code]
    export FIREWORKS_API_KEY=fw-...
[/code]

新手引导会将密钥存储到你的凭证配置文件中的 `fireworks` 提供商下，并将 **Fire Pass** Kimi K2.5 Turbo 路由器设为默认模型。

* ### 验证模型可用

bashCopy code
[code]
    openclaw models list --provider fireworks
[/code]

列表应包含 `Kimi K2.6` 和 `Kimi K2.5 Turbo (Fire Pass)`。如果 `FIREWORKS_API_KEY` 未解析，`openclaw models status --json` 会在 `auth.unusableProfiles` 下报告缺失的凭证。

## 非交互式设置

对于脚本化或 CI 安装，请在命令行上传入所有内容：

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice fireworks-api-key \  --fireworks-api-key "$FIREWORKS_API_KEY" \  --skip-health \  --accept-risk
[/code]

## 内置目录

模型引用 | 名称 | 输入 | 上下文 | 最大输出 | 思考  
---|---|---|---|---|---  
`fireworks/accounts/fireworks/models/kimi-k2p6` | Kimi K2.6 | 文本 + 图像 | 262,144 | 262,144 | 强制关闭  
`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo` | Kimi K2.5 Turbo (Fire Pass) | 文本 + 图像 | 256,000 | 256,000 | 强制关闭（默认）  
  
## 自定义 Fireworks 模型 id

OpenClaw 在运行时接受任何 Fireworks 模型或路由器 id。使用 Fireworks 显示的确切 id，并为其加上 `fireworks/` 前缀。动态解析会克隆 Fire Pass 模板（文本 + 图像输入、OpenAI 兼容 API、默认成本为零），并在 id 匹配 Kimi 模式时自动禁用思考。

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "fireworks/accounts/fireworks/models/<your-model-id>",      },    },  },}
[/code]

模型 id 前缀的工作方式

OpenClaw 中的每个 Fireworks 模型引用都以 `fireworks/` 开头，后面跟着 Fireworks 平台中的确切 id 或路由器路径。例如：

  * 路由器模型：`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`
  * 直接模型：`fireworks/accounts/fireworks/models/<model-name>`


OpenClaw 在构造 API 请求时会去掉 `fireworks/` 前缀，并将剩余路径作为 OpenAI 兼容的 `model` 字段发送到 Fireworks 端点。

为什么对 Kimi 强制关闭思考

如果请求携带 `reasoning_*` 参数，即使 Kimi 通过 Moonshot 自有 API 支持思考，Fireworks K2.6 也会返回 400。内置策略（`extensions/fireworks/thinking-policy.ts`）只为 Kimi 模型 id 发布 `off` 思考级别，因此手动 `/think` 切换和提供商策略界面会与运行时契约保持一致。

要端到端使用 Kimi 推理，请配置 [Moonshot provider](</zh-CN/providers/moonshot>)，并通过它路由同一模型。

守护进程的环境可用性

如果 Gateway 网关作为托管服务运行（launchd、systemd、Docker），Fireworks 密钥必须对该进程可见，而不仅仅对你的交互式 shell 可见。

在 macOS 上，`openclaw gateway install` 已经会将 `~/.openclaw/.env` 接入 LaunchAgent 环境文件。轮换密钥后，请重新运行安装（或 `openclaw doctor --fix`）。

## 相关

[**模型提供商** 选择提供商、模型引用和故障转移行为。 ](</zh-CN/concepts/model-providers>) [**思考模式** `/think` 级别、提供商策略，以及路由具备推理能力的模型。 ](</zh-CN/tools/thinking>) [**Moonshot** 通过 Moonshot 自有 API 运行带原生思考输出的 Kimi。 ](</zh-CN/providers/moonshot>) [**故障排除** 常规故障排除和常见问题。 ](</zh-CN/help/troubleshooting>)

Was this useful?YesNo