---
title: Text-to-Speech
source_url: https://docs.openclaw.ai/tools/tts
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Nodes and devices

Text-to-Speech

# 

​

Text-to-speech (TTS)

OpenClaw can convert outbound replies into audio using ElevenLabs, Microsoft, or OpenAI. It works anywhere OpenClaw can send audio; Telegram gets a round voice-note bubble.

## 

​

Supported services

  * **ElevenLabs** (primary or fallback provider)
  * **Microsoft** (primary or fallback provider; current bundled implementation uses `node-edge-tts`, default when no API keys)
  * **OpenAI** (primary or fallback provider; also used for summaries)


### 

​

Microsoft speech notes

The bundled Microsoft speech provider currently uses Microsoft Edge’s online neural TTS service via the `node-edge-tts` library. It’s a hosted service (not local), uses Microsoft endpoints, and does not require an API key. `node-edge-tts` exposes speech configuration options and output formats, but not all options are supported by the service. Legacy config and directive input using `edge` still works and is normalized to `microsoft`. Because this path is a public web service without a published SLA or quota, treat it as best-effort. If you need guaranteed limits and support, use OpenAI or ElevenLabs.

## 

​

Optional keys

If you want OpenAI or ElevenLabs:

  * `ELEVENLABS_API_KEY` (or `XI_API_KEY`)
  * `OPENAI_API_KEY`

Microsoft speech does **not** require an API key. If no API keys are found, OpenClaw defaults to Microsoft (unless disabled via `messages.tts.microsoft.enabled=false` or `messages.tts.edge.enabled=false`). If multiple providers are configured, the selected provider is used first and the others are fallback options. Auto-summary uses the configured `summaryModel` (or `agents.defaults.model.primary`), so that provider must also be authenticated if you enable summaries.

## 

​

Service links

  * [OpenAI Text-to-Speech guide](<https://platform.openai.com/docs/guides/text-to-speech>)
  * [OpenAI Audio API reference](<https://platform.openai.com/docs/api-reference/audio>)
  * [ElevenLabs Text to Speech](<https://elevenlabs.io/docs/api-reference/text-to-speech>)
  * [ElevenLabs Authentication](<https://elevenlabs.io/docs/api-reference/authentication>)
  * [node-edge-tts](<https://github.com/SchneeHertz/node-edge-tts>)
  * [Microsoft Speech output formats](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech#audio-outputs>)


## 

​

Is it enabled by default?

No. Auto‑TTS is **off** by default. Enable it in config with `messages.tts.auto` or per session with `/tts always` (alias: `/tts on`). Microsoft speech **is** enabled by default once TTS is on, and is used automatically when no OpenAI or ElevenLabs API keys are available.

## 

​

Config

TTS config lives under `messages.tts` in `openclaw.json`. Full schema is in [Gateway configuration](</gateway/configuration>).

### 

​

Minimal config (enable + provider)

Copy
[code]
    {
      messages: {
        tts: {
          auto: "always",
          provider: "elevenlabs",
        },
      },
    }
    
[/code]

### 

​

OpenAI primary with ElevenLabs fallback

Copy
[code]
    {
      messages: {
        tts: {
          auto: "always",
          provider: "openai",
          summaryModel: "openai/gpt-4.1-mini",
          modelOverrides: {
            enabled: true,
          },
          openai: {
            apiKey: "openai_api_key",
            baseUrl: "https://api.openai.com/v1",
            model: "gpt-4o-mini-tts",
            voice: "alloy",
          },
          elevenlabs: {
            apiKey: "elevenlabs_api_key",
            baseUrl: "https://api.elevenlabs.io",
            voiceId: "voice_id",
            modelId: "eleven_multilingual_v2",
            seed: 42,
            applyTextNormalization: "auto",
            languageCode: "en",
            voiceSettings: {
              stability: 0.5,
              similarityBoost: 0.75,
              style: 0.0,
              useSpeakerBoost: true,
              speed: 1.0,
            },
          },
        },
      },
    }
    
[/code]

### 

​

Microsoft primary (no API key)

Copy
[code]
    {
      messages: {
        tts: {
          auto: "always",
          provider: "microsoft",
          microsoft: {
            enabled: true,
            voice: "en-US-MichelleNeural",
            lang: "en-US",
            outputFormat: "audio-24khz-48kbitrate-mono-mp3",
            rate: "+10%",
            pitch: "-5%",
          },
        },
      },
    }
    
[/code]

### 

​

Disable Microsoft speech

Copy
[code]
    {
      messages: {
        tts: {
          microsoft: {
            enabled: false,
          },
        },
      },
    }
    
[/code]

### 

​

Custom limits + prefs path

Copy
[code]
    {
      messages: {
        tts: {
          auto: "always",
          maxTextLength: 4000,
          timeoutMs: 30000,
          prefsPath: "~/.openclaw/settings/tts.json",
        },
      },
    }
    
[/code]

### 

​

Only reply with audio after an inbound voice note

Copy
[code]
    {
      messages: {
        tts: {
          auto: "inbound",
        },
      },
    }
    
[/code]

### 

​

Disable auto-summary for long replies

Copy
[code]
    {
      messages: {
        tts: {
          auto: "always",
        },
      },
    }
    
[/code]

Then run:

Copy
[code]
    /tts summary off
    
[/code]

### 

​

Notes on fields

  * `auto`: auto‑TTS mode (`off`, `always`, `inbound`, `tagged`).
    * `inbound` only sends audio after an inbound voice note.
    * `tagged` only sends audio when the reply includes `[[tts]]` tags.
  * `enabled`: legacy toggle (doctor migrates this to `auto`).
  * `mode`: `"final"` (default) or `"all"` (includes tool/block replies).
  * `provider`: speech provider id such as `"elevenlabs"`, `"microsoft"`, or `"openai"` (fallback is automatic).
  * If `provider` is **unset** , OpenClaw prefers `openai` (if key), then `elevenlabs` (if key), otherwise `microsoft`.
  * Legacy `provider: "edge"` still works and is normalized to `microsoft`.
  * `summaryModel`: optional cheap model for auto-summary; defaults to `agents.defaults.model.primary`.
    * Accepts `provider/model` or a configured model alias.
  * `modelOverrides`: allow the model to emit TTS directives (on by default).
    * `allowProvider` defaults to `false` (provider switching is opt-in).
  * `maxTextLength`: hard cap for TTS input (chars). `/tts audio` fails if exceeded.
  * `timeoutMs`: request timeout (ms).
  * `prefsPath`: override the local prefs JSON path (provider/limit/summary).
  * `apiKey` values fall back to env vars (`ELEVENLABS_API_KEY`/`XI_API_KEY`, `OPENAI_API_KEY`).
  * `elevenlabs.baseUrl`: override ElevenLabs API base URL.
  * `openai.baseUrl`: override the OpenAI TTS endpoint.
    * Resolution order: `messages.tts.openai.baseUrl` -> `OPENAI_TTS_BASE_URL` -> `https://api.openai.com/v1`
    * Non-default values are treated as OpenAI-compatible TTS endpoints, so custom model and voice names are accepted.
  * `elevenlabs.voiceSettings`:
    * `stability`, `similarityBoost`, `style`: `0..1`
    * `useSpeakerBoost`: `true|false`
    * `speed`: `0.5..2.0` (1.0 = normal)
  * `elevenlabs.applyTextNormalization`: `auto|on|off`
  * `elevenlabs.languageCode`: 2-letter ISO 639-1 (e.g. `en`, `de`)
  * `elevenlabs.seed`: integer `0..4294967295` (best-effort determinism)
  * `microsoft.enabled`: allow Microsoft speech usage (default `true`; no API key).
  * `microsoft.voice`: Microsoft neural voice name (e.g. `en-US-MichelleNeural`).
  * `microsoft.lang`: language code (e.g. `en-US`).
  * `microsoft.outputFormat`: Microsoft output format (e.g. `audio-24khz-48kbitrate-mono-mp3`).
    * See Microsoft Speech output formats for valid values; not all formats are supported by the bundled Edge-backed transport.
  * `microsoft.rate` / `microsoft.pitch` / `microsoft.volume`: percent strings (e.g. `+10%`, `-5%`).
  * `microsoft.saveSubtitles`: write JSON subtitles alongside the audio file.
  * `microsoft.proxy`: proxy URL for Microsoft speech requests.
  * `microsoft.timeoutMs`: request timeout override (ms).
  * `edge.*`: legacy alias for the same Microsoft settings.


## 

​

Model-driven overrides (default on)

By default, the model **can** emit TTS directives for a single reply. When `messages.tts.auto` is `tagged`, these directives are required to trigger audio. When enabled, the model can emit `[[tts:...]]` directives to override the voice for a single reply, plus an optional `[[tts:text]]...[[/tts:text]]` block to provide expressive tags (laughter, singing cues, etc) that should only appear in the audio. `provider=...` directives are ignored unless `modelOverrides.allowProvider: true`. Example reply payload:

Copy
[code]
    Here you go.
    
    [[tts:voiceId=pMsXgVXv3BLzUgSXRplE model=eleven_v3 speed=1.1]]
    [[tts:text]](laughs) Read the song once more.[[/tts:text]]
    
[/code]

Available directive keys (when enabled):

  * `provider` (registered speech provider id, for example `openai`, `elevenlabs`, or `microsoft`; requires `allowProvider: true`)
  * `voice` (OpenAI voice) or `voiceId` (ElevenLabs)
  * `model` (OpenAI TTS model or ElevenLabs model id)
  * `stability`, `similarityBoost`, `style`, `speed`, `useSpeakerBoost`
  * `applyTextNormalization` (`auto|on|off`)
  * `languageCode` (ISO 639-1)
  * `seed`

Disable all model overrides:

Copy
[code]
    {
      messages: {
        tts: {
          modelOverrides: {
            enabled: false,
          },
        },
      },
    }
    
[/code]

Optional allowlist (enable provider switching while keeping other knobs configurable):

Copy
[code]
    {
      messages: {
        tts: {
          modelOverrides: {
            enabled: true,
            allowProvider: true,
            allowSeed: false,
          },
        },
      },
    }
    
[/code]

## 

​

Per-user preferences

Slash commands write local overrides to `prefsPath` (default: `~/.openclaw/settings/tts.json`, override with `OPENCLAW_TTS_PREFS` or `messages.tts.prefsPath`). Stored fields:

  * `enabled`
  * `provider`
  * `maxLength` (summary threshold; default 1500 chars)
  * `summarize` (default `true`)

These override `messages.tts.*` for that host.

## 

​

Output formats (fixed)

  * **Telegram** : Opus voice note (`opus_48000_64` from ElevenLabs, `opus` from OpenAI).
    * 48kHz / 64kbps is a good voice-note tradeoff and required for the round bubble.
  * **Other channels** : MP3 (`mp3_44100_128` from ElevenLabs, `mp3` from OpenAI).
    * 44.1kHz / 128kbps is the default balance for speech clarity.
  * **Microsoft** : uses `microsoft.outputFormat` (default `audio-24khz-48kbitrate-mono-mp3`).
    * The bundled transport accepts an `outputFormat`, but not all formats are available from the service.
    * Output format values follow Microsoft Speech output formats (including Ogg/WebM Opus).
    * Telegram `sendVoice` accepts OGG/MP3/M4A; use OpenAI/ElevenLabs if you need guaranteed Opus voice notes. citeturn1search1
    * If the configured Microsoft output format fails, OpenClaw retries with MP3.

OpenAI/ElevenLabs formats are fixed; Telegram expects Opus for voice-note UX.

## 

​

Auto-TTS behavior

When enabled, OpenClaw:

  * skips TTS if the reply already contains media or a `MEDIA:` directive.
  * skips very short replies (< 10 chars).
  * summarizes long replies when enabled using `agents.defaults.model.primary` (or `summaryModel`).
  * attaches the generated audio to the reply.

If the reply exceeds `maxLength` and summary is off (or no API key for the summary model), audio is skipped and the normal text reply is sent.

## 

​

Flow diagram

Copy
[code]
    Reply -> TTS enabled?
      no  -> send text
      yes -> has media / MEDIA: / short?
              yes -> send text
              no  -> length > limit?
                       no  -> TTS -> attach audio
                       yes -> summary enabled?
                                no  -> send text
                                yes -> summarize (summaryModel or agents.defaults.model.primary)
                                          -> TTS -> attach audio
    
[/code]

## 

​

Slash command usage

There is a single command: `/tts`. See [Slash commands](</tools/slash-commands>) for enablement details. Discord note: `/tts` is a built-in Discord command, so OpenClaw registers `/voice` as the native command there. Text `/tts ...` still works.

Copy
[code]
    /tts off
    /tts always
    /tts inbound
    /tts tagged
    /tts status
    /tts provider openai
    /tts limit 2000
    /tts summary off
    /tts audio Hello from OpenClaw
    
[/code]

Notes:

  * Commands require an authorized sender (allowlist/owner rules still apply).
  * `commands.text` or native command registration must be enabled.
  * `off|always|inbound|tagged` are per‑session toggles (`/tts on` is an alias for `/tts always`).
  * `limit` and `summary` are stored in local prefs, not the main config.
  * `/tts audio` generates a one-off audio reply (does not toggle TTS on).


## 

​

Agent tool

The `tts` tool converts text to speech and returns a `MEDIA:` path. When the result is Telegram-compatible, the tool includes `[[audio_as_voice]]` so Telegram sends a voice bubble.

## 

​

Gateway RPC

Gateway methods:

  * `tts.status`
  * `tts.enable`
  * `tts.disable`
  * `tts.convert`
  * `tts.setProvider`
  * `tts.providers`


[Location Command](</nodes/location-command>)[Web](</web>)

⌘I