---
title: Провайдер llama.cpp
source_url: https://docs.openclaw.ai/ru/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp` — официальный внешний Plugin-провайдер для локальных GGUF-эмбеддингов. Он владеет runtime-зависимостью `node-llama-cpp`, используемой `memorySearch.provider: "local"`.

Установите его перед использованием локальных эмбеддингов памяти:

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

Основной npm-пакет `openclaw` не включает `node-llama-cpp`. Хранение нативной зависимости в этом Plugin предотвращает удаление вручную установленного runtime внутри каталога пакета OpenClaw при обычных npm-обновлениях OpenClaw.

## Конфигурация

Задайте провайдер поиска по памяти как `local`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

Модель по умолчанию — `embeddinggemma-300m-qat-Q8_0.gguf`. Также можно указать в `local.modelPath` локальный файл `.gguf`.

## Нативный Runtime

Используйте Node 24 для наиболее гладкого пути установки нативных зависимостей. Исходные checkout-копии, использующие pnpm, могут потребовать одобрения и пересборки нативной зависимости:

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

Для локальных эмбеддингов с меньшими трудозатратами используйте локальный сервисный провайдер, например Ollama или LM Studio.

Was this useful?YesNo

Open issue