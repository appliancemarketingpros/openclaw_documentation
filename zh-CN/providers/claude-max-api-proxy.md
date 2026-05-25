---
title: Claude Max API 代理
source_url: https://docs.openclaw.ai/zh-CN/providers/claude-max-api-proxy
scraped_at: 2026-05-25
---

**claude-max-api-proxy** 是一个社区工具，可将你的 Claude Max/Pro 订阅暴露为兼容 OpenAI 的 API 端点。这样一来，你就可以在任何支持 OpenAI API 格式的工具中使用你的订阅。

## 为什么要使用它？

方式 | 成本 | 最适合  
---|---|---  
Anthropic API | 按 token 付费（Opus 约为输入 $15/M，输出 $75/M） | 生产应用、高流量  
Claude Max 订阅 | 每月固定 $200 | 个人使用、开发、无限量使用  
  
如果你有 Claude Max 订阅，并且希望将其与兼容 OpenAI 的工具一起使用，那么这个代理可能会降低某些工作流的成本。对于生产用途，API key 仍然是更清晰的策略路径。

## 工作原理

textCopy code
[code]
    你的应用 → claude-max-api-proxy → Claude Code CLI → Anthropic（通过订阅）     （OpenAI 格式）              （转换格式）      （使用你的登录）
[/code]

该代理会：

  1. 在 `http://localhost:3456/v1/chat/completions` 接收 OpenAI 格式请求
  2. 将其转换为 Claude Code CLI 命令
  3. 以 OpenAI 格式返回响应（支持流式传输）


## 快速开始

* ### 安装代理

需要 Node.js 20+ 和 Claude Code CLI。

bashCopy code
[code]
    npm install -g claude-max-api-proxy # Verify Claude CLI is authenticatedclaude --version
[/code]

* ### 启动服务器

bashCopy code
[code]
    claude-max-api# Server runs at http://localhost:3456
[/code]

* ### 测试代理

bashCopy code
[code]
    # Health checkcurl http://localhost:3456/health # List modelscurl http://localhost:3456/v1/models # Chat completioncurl http://localhost:3456/v1/chat/completions \  -H "Content-Type: application/json" \  -d '{    "model": "claude-opus-4",    "messages": [{"role": "user", "content": "Hello!"}]  }'
[/code]

* ### 配置 OpenClaw

将 OpenClaw 指向该代理，作为一个自定义的兼容 OpenAI 端点：

json5Copy code
[code]
    {  env: {    OPENAI_API_KEY: "not-needed",    OPENAI_BASE_URL: "http://localhost:3456/v1",  },  agents: {    defaults: {      model: { primary: "openai/claude-opus-4" },    },  },}
[/code]

## 内置目录

模型 ID | 映射到  
---|---  
`claude-opus-4` | Claude Opus 4  
`claude-sonnet-4` | Claude Sonnet 4  
`claude-haiku-4` | Claude Haiku 4  
  
## 高级配置

代理风格的兼容 OpenAI 说明

这条路径与其他自定义 `/v1` 后端一样，使用同一种代理风格的兼容 OpenAI 路由：

  * 不适用原生仅限 OpenAI 的请求塑形
  * 不支持 `service_tier`、不支持 Responses `store`、不支持提示缓存提示，也不支持 OpenAI 推理兼容负载塑形
  * 不会在该代理 URL 上注入隐藏的 OpenClaw 归属 headers（`originator`、`version`、`User-Agent`）

在 macOS 上通过 LaunchAgent 自动启动

创建一个 LaunchAgent 以自动运行该代理：

bashCopy code
[code]
    cat > ~/Library/LaunchAgents/com.claude-max-api.plist << 'EOF'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>Label</key>  <string>com.claude-max-api</string>  <key>RunAtLoad</key>  <true/>  <key>KeepAlive</key>  <true/>  <key>ProgramArguments</key>  <array>    <string>/usr/local/bin/node</string>    <string>/usr/local/lib/node_modules/claude-max-api-proxy/dist/server/standalone.js</string>  </array>  <key>EnvironmentVariables</key>  <dict>    <key>PATH</key>    <string>/usr/local/bin:/opt/homebrew/bin:~/.local/bin:/usr/bin:/bin</string>  </dict></dict></plist>EOF launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.claude-max-api.plist
[/code]

## 链接

  * **npm：** <https://www.npmjs.com/package/claude-max-api-proxy>
  * **GitHub：** <https://github.com/atalovesyou/claude-max-api-proxy>
  * **Issues：** <https://github.com/atalovesyou/claude-max-api-proxy/issues>


## 说明

  * 这是一个**社区工具** ，并未获得 Anthropic 或 OpenClaw 的官方支持
  * 需要已启用的 Claude Max/Pro 订阅，并且 Claude Code CLI 已完成认证
  * 该代理在本地运行，不会将数据发送到任何第三方服务器
  * 完整支持流式响应


## 相关内容

[**Anthropic 提供商** 通过 Claude CLI 或 API key 实现的原生 OpenClaw 集成。 ](</zh-CN/providers/anthropic>) [**OpenAI 提供商** 用于 OpenAI/Codex 订阅。 ](</zh-CN/providers/openai>) [**模型选择** 所有提供商、模型引用和故障转移行为的概览。 ](</zh-CN/concepts/model-providers>) [**配置** 完整配置参考。 ](</zh-CN/gateway/configuration>)

Was this useful?YesNo