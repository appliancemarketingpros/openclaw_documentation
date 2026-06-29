---
title: Cohere
source_url: https://docs.openclaw.ai/zh-CN/providers/cohere
scraped_at: 2026-06-29
---

快速开始

[Cohere](<https://cohere.com>) 通过其 Compatibility API 提供 OpenAI 兼容推理。OpenClaw 在外部化过渡期间内置 Cohere 提供商，并且也将其作为带有 Command A 模型目录的官方外部插件发布。

属性 | 值  
---|---  
提供商 id | `cohere`  
插件 | 过渡期间内置；官方外部包  
凭证环境变量 | `COHERE_API_KEY`  
新手引导标志 | `--auth-choice cohere-api-key`  
直接 CLI 标志 | `--cohere-api-key <key>`  
API | OpenAI 兼容（`openai-completions`）  
基础 URL | `https://api.cohere.ai/compatibility/v1`  
默认模型 | `cohere/command-a-03-2025`  
  
## 开始使用

  1. 当前 OpenClaw 包已包含 Cohere。如果不可用，请安装外部包并重启 Gateway 网关：

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. 创建 Cohere API key。
  3. 运行新手引导：

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. 确认目录可用：

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

仅当尚未配置主模型时，才会设置默认模型。

## 仅环境变量设置

让 Gateway 网关进程可以使用 `COHERE_API_KEY`，然后选择 Cohere 模型：

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## 相关内容

  * [模型提供商](</zh-CN/concepts/model-providers>)
  * [模型 CLI](</zh-CN/cli/models>)
  * [提供商目录](</zh-CN/providers>)


Was this useful?YesNo

Open issue