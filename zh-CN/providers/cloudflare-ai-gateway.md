---
title: Cloudflare AI Gateway
source_url: https://docs.openclaw.ai/zh-CN/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

Cloudflare AI Gateway 位于提供商 API 之前，让你能够添加分析、缓存和控制功能。对于 Anthropic，OpenClaw 会通过你的 Gateway 网关端点使用 Anthropic Messages API。

属性 | 值  
---|---  
提供商 | `cloudflare-ai-gateway`  
Base URL | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
默认模型 | `cloudflare-ai-gateway/claude-sonnet-4-6`  
API key | `CLOUDFLARE_AI_GATEWAY_API_KEY`（你用于通过 Gateway 网关发起请求的提供商 API key）  
  
当为 Anthropic Messages 模型启用 thinking 时，OpenClaw 会在通过 Cloudflare AI Gateway 发送负载之前，去除末尾的 assistant 预填充轮次。Anthropic 会拒绝带有扩展 thinking 的响应预填充，而普通的非 thinking 预填充仍然可用。

## 入门指南

* ### 设置提供商 API key 和 Gateway 网关详细信息

运行新手引导并选择 Cloudflare AI Gateway 凭证选项：

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

系统会提示你输入账户 ID、Gateway 网关 ID 和 API key。

* ### 设置默认模型

将该模型添加到你的 OpenClaw 配置中：

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### 验证该模型可用

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## 非交互式示例

对于脚本化或 CI 设置，请在命令行上传递所有值：

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## 高级配置

需要身份验证的 Gateway 网关

如果你在 Cloudflare 中启用了 Gateway 身份验证，请添加 `cf-aig-authorization` 标头。这是**除了** 你的提供商 API key 之外的额外要求。

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

环境说明

如果 Gateway 网关以守护进程（launchd/systemd）方式运行，请确保 `CLOUDFLARE_AI_GATEWAY_API_KEY` 可供该进程使用。

## 相关内容

[**模型选择** 选择提供商、模型引用和故障切换行为。 ](</zh-CN/concepts/model-providers>) [**故障排除** 常规故障排除和常见问题。 ](</zh-CN/help/troubleshooting>)

Was this useful?YesNo