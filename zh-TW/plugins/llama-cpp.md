---
title: llama.cpp 供應商
source_url: https://docs.openclaw.ai/zh-TW/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp` 是本機 GGUF 嵌入的官方外部提供者外掛。 它擁有 `memorySearch.provider: "local"` 使用的 `node-llama-cpp` 執行階段相依套件。

使用本機記憶嵌入前，請先安裝它：

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

主要的 `openclaw` npm 套件不包含 `node-llama-cpp`。將原生相依套件保留在此外掛中，可避免一般 OpenClaw npm 更新刪除 OpenClaw 套件目錄內手動安裝的執行階段。

## 設定

將記憶搜尋提供者設為 `local`：

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

預設模型是 `embeddinggemma-300m-qat-Q8_0.gguf`。你也可以將 `local.modelPath` 指向本機 `.gguf` 檔案。

## 原生執行階段

使用節點 24 可獲得最順暢的原生安裝路徑。使用 pnpm 的原始碼 checkout 可能需要核准並重新建置原生相依套件：

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

若要降低本機嵌入的使用阻力，請改用 Ollama 或 LM Studio 等本機服務提供者。

Was this useful?YesNo

Open issue