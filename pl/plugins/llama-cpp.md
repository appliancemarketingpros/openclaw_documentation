---
title: Dostawca llama.cpp
source_url: https://docs.openclaw.ai/pl/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp` to oficjalny zewnętrzny Plugin dostawcy dla lokalnych osadzeń GGUF. Jest właścicielem zależności środowiska uruchomieniowego `node-llama-cpp` używanej przez `memorySearch.provider: "local"`.

Zainstaluj go przed użyciem lokalnych osadzeń pamięci:

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

Główny pakiet npm `openclaw` nie zawiera `node-llama-cpp`. Utrzymywanie natywnej zależności w tym Plugin zapobiega usuwaniu ręcznie zainstalowanego środowiska uruchomieniowego w katalogu pakietu OpenClaw przez standardowe aktualizacje npm OpenClaw.

## Konfiguracja

Ustaw dostawcę wyszukiwania pamięci na `local`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

Domyślny model to `embeddinggemma-300m-qat-Q8_0.gguf`. Możesz także wskazać `local.modelPath` na lokalny plik `.gguf`.

## Natywne środowisko uruchomieniowe

Użyj Node 24, aby uzyskać najsprawniejszą ścieżkę instalacji natywnej. Checkouty źródłowe używające pnpm mogą wymagać zatwierdzenia i ponownego zbudowania natywnej zależności:

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

Aby uzyskać lokalne osadzenia z mniejszym tarciem, użyj zamiast tego lokalnego dostawcy usług, takiego jak Ollama lub LM Studio.

Was this useful?YesNo

Open issue