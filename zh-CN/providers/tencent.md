---
title: 腾讯云（TokenHub）
source_url: https://docs.openclaw.ai/zh-CN/providers/tencent
scraped_at: 2026-05-25
---

腾讯云作为 OpenClaw 的内置提供商插件提供。它通过 TokenHub 端点（`tencent-tokenhub`）使用 OpenAI 兼容 API 访问腾讯 Hy3 preview。

属性 | 值  
---|---  
提供商 id | `tencent-tokenhub`  
插件 | 内置，`enabledByDefault: true`  
认证环境变量 | `TOKENHUB_API_KEY`  
新手引导标志 | `--auth-choice tokenhub-api-key`  
直接 CLI 标志 | `--tokenhub-api-key <key>`  
API | OpenAI 兼容（`openai-completions`）  
默认 base URL | `https://tokenhub.tencentmaas.com/v1`  
全球 base URL | `https://tokenhub-intl.tencentmaas.com/v1`（覆盖）  
默认模型 | `tencent-tokenhub/hy3-preview`  
  
## 快速开始

* ### 创建 TokenHub API key

在腾讯云 TokenHub 中创建 API key。如果你为该 key 选择了受限访问范围，请在允许的模型中包含 **Hy3 preview** 。

* ### 运行新手引导

新手引导Copy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

直接标志Copy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

仅环境变量Copy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### 验证模型

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## 非交互式设置

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## 内置目录

模型引用 | 名称 | 输入 | 上下文 | 最大输出 | 备注  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | Hy3 preview（TokenHub） | text | 256,000 | 64,000 | 默认；支持推理  
  
Hy3 preview 是腾讯混元的大型 MoE 语言模型，适用于推理、长上下文指令遵循、代码和智能体工作流。腾讯的 OpenAI 兼容示例使用 `hy3-preview` 作为模型 id，并支持标准 chat-completions 工具调用以及 `reasoning_effort`。

## 分级定价

内置目录带有分级成本元数据，会随输入窗口长度缩放，因此无需手动覆盖也能填充成本估算。

输入 token 范围 | 输入费率 | 输出费率 | 缓存读取  
---|---|---|---  
0 - 16,000 | 0.176 | 0.587 | 0.059  
16,000 - 32,000 | 0.235 | 0.939 | 0.088  
32,000+ | 0.293 | 1.173 | 0.117  
  
费率按腾讯公布的每百万 token 美元价格计算。仅当你需要不同的表面时，才在 `models.providers.tencent-tokenhub` 下覆盖定价。

## 高级配置

端点覆盖

OpenClaw 默认使用腾讯云的 `https://tokenhub.tencentmaas.com/v1` 端点。腾讯还记录了一个国际版 TokenHub 端点：

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

仅在你的 TokenHub 账户或区域要求时覆盖端点。

daemon 的环境可用性

如果 Gateway 网关 作为托管服务（launchd、systemd、Docker）运行，`TOKENHUB_API_KEY` 必须对该进程可见。将它设置在 `~/.openclaw/.env` 中，或通过 `env.shellEnv` 设置，以便 launchd、systemd 或 Docker exec 环境可以读取它。

## 相关内容

[**模型提供商** 选择提供商、模型引用和故障转移行为。 ](</zh-CN/concepts/model-providers>) [**配置参考** 完整配置 schema，包括提供商设置。 ](</zh-CN/gateway/configuration>) [**Tencent TokenHub** 腾讯云 TokenHub 产品页。 ](<https://cloud.tencent.com/product/tokenhub>) [**Hy3 preview 模型卡** 腾讯混元 Hy3 preview 详情和基准测试。 ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo