---
title: OpenAI coverage and cost
source_url: https://docs.openclaw.ai/providers/openai/coverage-and-cost
scraped_at: 2026-09-14
---

ModelsProviders

## Usage and cost tracking

OpenClaw keeps subscription quota and Platform API billing distinct:

  * ChatGPT/Codex OAuth shows the subscription plan, quota windows, and credit balance.
  * `OPENAI_ADMIN_KEY` shows 30 days of provider-reported organization cost and completions usage in Control UI **Usage** , including daily spend, request/token totals, top models, and cost categories.
  * `OPENAI_PROJECT_ID` optionally scopes Admin API history to one project.
  * OpenClaw never sends `OPENAI_API_KEY` or an `openai` inference profile to organization APIs; those credentials may belong to custom, Azure, or agent-local endpoints.


An explicit Admin key takes precedence over OAuth. Provider-reported history is not merged with OpenClaw's session-derived estimated cost; it can include API activity from other clients and provider-side billing adjustments.

OpenAI's [API Usage Dashboard](<https://help.openai.com/en/articles/10478918>) documentation describes the organization-owner and explicit Usage Dashboard permission requirements for usage data.

Provider, model, runtime, and channel are separate layers. If those labels are getting mixed together, read [Agent runtimes](</concepts/agent-runtimes>) before changing config.

## OpenClaw feature coverage

OpenAI capability | OpenClaw surface | Status  
---|---|---  
Chat / Responses | `openai/<model>` model provider | Yes  
Codex subscription models | `openai/<model>` with OpenAI OAuth | Yes  
Legacy Codex model refs | old Codex model refs, `codex-cli/<model>` | Repaired by doctor to `openai/<model>`  
Codex app-server harness | Codex-compatible HTTPS route with runtime unset/`auto`, or explicit `agentRuntime.id: codex` | Yes  
Server-side web search | Native OpenAI Responses tool | Yes, when web search is enabled and no other provider is pinned  
Images | `image_generate` | Yes  
Videos | `video_generate` | Yes  
Text-to-speech | `tts.provider: "openai"` / `tts` | Yes  
Batch speech-to-text | `tools.media.audio` / media understanding | Yes  
Streaming speech-to-text | Voice Call `streaming.provider: "openai"` | Yes  
Realtime voice | Voice Call `realtime.provider: "openai"` / Control UI Talk `talk.realtime.provider: "openai"` | Yes (auth order depends on the selected Realtime route; see below)  
Embeddings | memory embedding provider | Yes  
  
## Memory embeddings

OpenClaw can use OpenAI, or an OpenAI-compatible embedding endpoint, for `memory_search` indexing and query embeddings:

json5Copy code
[code]
    {  memory: {    search: {      provider: "openai",      model: "text-embedding-3-small",    },  },}
[/code]

For OpenAI-compatible endpoints that require asymmetric embedding labels, set `queryInputType` and `documentInputType` under `memory.search`. OpenClaw forwards these as provider-specific `input_type` request fields: query embeddings use `queryInputType`; indexed memory chunks and batch indexing use `documentInputType`. See the [Memory configuration reference](</reference/memory-config#provider-specific-config>) for the full example.

Was this useful?YesNo

Open issue