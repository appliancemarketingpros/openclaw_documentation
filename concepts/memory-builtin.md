---
title: Builtin memory engine
source_url: https://docs.openclaw.ai/concepts/memory-builtin
scraped_at: 2026-05-04
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Memory

Builtin memory engine

> ## Documentation Index
> 
> Fetch the complete documentation index at: <https://docs.openclaw.ai/llms.txt>
> 
> Use this file to discover all available pages before exploring further.

The builtin engine is the default memory backend. It stores your memory index in a per-agent SQLite database and needs no extra dependencies to get started.

## 

​

What it provides

  * **Keyword search** via FTS5 full-text indexing (BM25 scoring).
  * **Vector search** via embeddings from any supported provider.
  * **Hybrid search** that combines both for best results.
  * **CJK support** via trigram tokenization for Chinese, Japanese, and Korean.
  * **sqlite-vec acceleration** for in-database vector queries (optional).


## 

​

Getting started

If you have an API key for OpenAI, Gemini, Voyage, Mistral, or DeepInfra, the builtin engine auto-detects it and enables vector search. No config needed. To set a provider explicitly:
[code] 
    {
      agents: {
        defaults: {
          memorySearch: {
            provider: "openai",
          },
        },
      },
    }
    
[/code]

Without an embedding provider, only keyword search is available. To force the built-in local embedding provider, install the optional `node-llama-cpp` runtime package next to OpenClaw, then point `local.modelPath` at a GGUF file:
[code] 
    {
      agents: {
        defaults: {
          memorySearch: {
            provider: "local",
            fallback: "none",
            local: {
              modelPath: "~/.node-llama-cpp/models/embeddinggemma-300m-qat-Q8_0.gguf",
            },
          },
        },
      },
    }
    
[/code]

## 

​

Supported embedding providers

Provider| ID| Auto-detected| Notes  
---|---|---|---  
OpenAI| `openai`| Yes| Default: `text-embedding-3-small`  
Gemini| `gemini`| Yes| Supports multimodal (image + audio)  
Voyage| `voyage`| Yes|   
Mistral| `mistral`| Yes|   
DeepInfra| `deepinfra`| Yes| Default: `BAAI/bge-m3`  
Ollama| `ollama`| No| Local, set explicitly  
Local| `local`| Yes (first)| Optional `node-llama-cpp` runtime  
  
Auto-detection picks the first provider whose API key can be resolved, in the order shown. Set `memorySearch.provider` to override.

## 

​

How indexing works

OpenClaw indexes `MEMORY.md` and `memory/*.md` into chunks (~400 tokens with 80-token overlap) and stores them in a per-agent SQLite database.

  * **Index location:** `~/.openclaw/memory/<agentId>.sqlite`
  * **Storage maintenance:** SQLite WAL sidecars are bounded with periodic and shutdown checkpoints.
  * **File watching:** changes to memory files trigger a debounced reindex (1.5s).
  * **Auto-reindex:** when the embedding provider, model, or chunking config changes, the entire index is rebuilt automatically.
  * **Reindex on demand:** `openclaw memory index --force`


You can also index Markdown files outside the workspace with `memorySearch.extraPaths`. See the [configuration reference](</reference/memory-config#additional-memory-paths>).

## 

​

When to use

The builtin engine is the right choice for most users:

  * Works out of the box with no extra dependencies.
  * Handles keyword and vector search well.
  * Supports all embedding providers.
  * Hybrid search combines the best of both retrieval approaches.

Consider switching to [QMD](</concepts/memory-qmd>) if you need reranking, query expansion, or want to index directories outside the workspace. Consider [Honcho](</concepts/memory-honcho>) if you want cross-session memory with automatic user modeling.

## 

​

Troubleshooting

**Memory search disabled?** Check `openclaw memory status`. If no provider is detected, set one explicitly or add an API key. **Local provider not detected?** Confirm the local path exists and run:
[code] 
    openclaw memory status --deep --agent main
    openclaw memory index --force --agent main
    
[/code]

Both standalone CLI commands and the Gateway use the same `local` provider id. If the provider is set to `auto`, local embeddings are considered first only when `memorySearch.local.modelPath` points to an existing local file. **Stale results?** Run `openclaw memory index --force` to rebuild. The watcher may miss changes in rare edge cases. **sqlite-vec not loading?** OpenClaw falls back to in-process cosine similarity automatically. `openclaw memory status --deep` reports the local vector store separately from the embedding provider, so `Vector store: unavailable` points at sqlite-vec loading while `Embeddings: unavailable` points at provider/auth or model readiness. Check logs for the specific load error.

## 

​

Configuration

For embedding provider setup, hybrid search tuning (weights, MMR, temporal decay), batch indexing, multimodal memory, sqlite-vec, extra paths, and all other config knobs, see the [Memory configuration reference](</reference/memory-config>).

## 

​

Related

  * [Memory overview](</concepts/memory>)
  * [Memory search](</concepts/memory-search>)
  * [Active memory](</concepts/active-memory>)


[Memory overview](</concepts/memory>)[QMD memory engine](</concepts/memory-qmd>)

⌘I