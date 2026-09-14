---
title: Text-to-speech quickstart
source_url: https://docs.openclaw.ai/tools/tts/quickstart
scraped_at: 2026-09-14
---

CapabilitiesTools

## Quick start

* ### Pick a provider

OpenAI and ElevenLabs are the most reliable hosted options. Microsoft and Local CLI work without an API key. See the provider matrix for the full list.

* ### Set the API key

Export the env var for your provider (for example `OPENAI_API_KEY`, `ELEVENLABS_API_KEY`). Microsoft and Local CLI need no key.

* ### Enable in config

Set `tts.auto: "always"` and `tts.provider`:

json5Copy code
[code]
    {  tts: {    auto: "always",    provider: "elevenlabs",  },}
[/code]

* ### Try it in chat

`/tts status` shows the current state. `/tts audio Hello from OpenClaw` sends a one-off audio reply.

## Supported providers

Provider | Auth | Notes  
---|---|---  
**Azure Speech** | `AZURE_SPEECH_KEY` \+ `AZURE_SPEECH_REGION` (also `AZURE_SPEECH_API_KEY`, `SPEECH_KEY`, `SPEECH_REGION`) | Native Ogg/Opus voice-note output and telephony.  
**DeepInfra** | `DEEPINFRA_API_KEY` | OpenAI-compatible TTS. Defaults to `hexgrad/Kokoro-82M`.  
**ElevenLabs** | `ELEVENLABS_API_KEY` or `XI_API_KEY` | Voice cloning, multilingual, deterministic via `seed`; streamed for Discord voice playback.  
**Fish Audio** | `FISH_API_KEY` or `FISH_AUDIO_API_KEY` | S2.1 hosted TTS, expressive tags, voice discovery, streaming, and telephony.  
**Google Gemini** | `GEMINI_API_KEY` or `GOOGLE_API_KEY` | Gemini API batch TTS; persona-aware via `promptTemplate: "audio-profile-v1"`.  
**Gradium** | `GRADIUM_API_KEY` | Voice-note and telephony output.  
**Inworld** | `INWORLD_API_KEY` | Streaming TTS API. Native Opus voice-note and PCM telephony.  
**Local CLI** | none | Runs a configured local TTS command.  
**Microsoft** | none | Public Edge neural TTS via `node-edge-tts`. Best-effort, no SLA.  
**MiniMax** | `MINIMAX_API_KEY` (or Token Plan: `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`) | T2A v2 API. Defaults to `speech-2.8-hd`.  
**OpenAI** | `OPENAI_API_KEY` | Also used for auto-summary; supports persona `instructions`.  
**OpenRouter** | `OPENROUTER_API_KEY` (can reuse `models.providers.openrouter.apiKey`) | Default model `hexgrad/kokoro-82m`.  
**Volcengine** | `VOLCENGINE_TTS_API_KEY` or `BYTEPLUS_SEED_SPEECH_API_KEY` (legacy AppID/token: `VOLCENGINE_TTS_APPID`/`_TOKEN`) | BytePlus Seed Speech HTTP API.  
**Vydra** | `VYDRA_API_KEY` | Shared image, video, and speech provider.  
**xAI** | `XAI_API_KEY` | xAI batch TTS. Native Opus voice-note is **not** supported.  
**Xiaomi MiMo** | `XIAOMI_API_KEY` | MiMo TTS through Xiaomi chat completions.  
  
If multiple providers are configured, the selected one is used first and the others are fallback options. Auto-summary uses `summaryModel` (or `agents.defaults.model.primary`), so that provider must also be authenticated if you keep summaries enabled.

Was this useful?YesNo

Open issue