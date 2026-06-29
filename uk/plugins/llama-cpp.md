---
title: Провайдер llama.cpp
source_url: https://docs.openclaw.ai/uk/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp` є офіційним зовнішнім Plugin постачальника для локальних вбудовувань GGUF. Він володіє runtime-залежністю `node-llama-cpp`, яку використовує `memorySearch.provider: "local"`.

Установіть його перед використанням локальних вбудовувань пам’яті:

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

Основний npm-пакет `openclaw` не містить `node-llama-cpp`. Збереження нативної залежності в цьому Plugin запобігає видаленню вручну встановленого runtime у каталозі пакета OpenClaw під час звичайних npm-оновлень OpenClaw.

## Конфігурація

Установіть постачальника пошуку в пам’яті на `local`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

Типова модель — `embeddinggemma-300m-qat-Q8_0.gguf`. Ви також можете вказати `local.modelPath` на локальний файл `.gguf`.

## Нативний runtime

Використовуйте Node 24 для найзручнішого шляху встановлення нативних залежностей. Вихідні checkout’и, що використовують pnpm, можуть потребувати схвалення та повторного складання нативної залежності:

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

Для локальних вбудовувань із меншим тертям використовуйте локального сервісного постачальника, як-от Ollama або LM Studio.

Was this useful?YesNo

Open issue