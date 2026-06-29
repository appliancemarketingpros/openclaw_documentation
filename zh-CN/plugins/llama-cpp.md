---
title: llama.cpp 提供商
source_url: https://docs.openclaw.ai/zh-CN/plugins/llama-cpp
scraped_at: 2026-06-29
---

快速开始

`llama-cpp` 是用于本地 GGUF 嵌入的官方外部提供商插件。 它拥有 `memorySearch.provider: "local"` 使用的 `node-llama-cpp` 运行时依赖。

在使用本地记忆嵌入之前安装它：

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

主 `openclaw` npm 包不包含 `node-llama-cpp`。将原生依赖保留在此插件中，可以防止常规 OpenClaw npm 更新删除手动安装在 OpenClaw 包目录内的运行时。

## 配置

将记忆搜索提供商设置为 `local`：

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

默认模型是 `embeddinggemma-300m-qat-Q8_0.gguf`。你也可以将 `local.modelPath` 指向本地 `.gguf` 文件。

## 原生运行时

使用 Node 24 可获得最顺畅的原生安装路径。使用 pnpm 的源码检出可能需要批准并重新构建原生依赖：

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

如果想更轻量地使用本地嵌入，请改用本地服务提供商，例如 Ollama 或 LM Studio。

Was this useful?YesNo

Open issue