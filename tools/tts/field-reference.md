---
title: Text-to-speech field reference
source_url: https://docs.openclaw.ai/tools/tts/field-reference
scraped_at: 2026-09-14
---

CapabilitiesTools

## Field reference

Provider `apiKey` fields, including `personas.<id>.providers.<provider>.apiKey`, can be raw strings or SecretRefs in global, per-agent, and Discord voice TTS config. During cold Gateway startup, an unavailable TTS SecretRef marks the built-in TTS capability configured-unavailable instead of stopping the Gateway. `tts.speak` then returns `UNAVAILABLE` with reason `SECRET_SURFACE_UNAVAILABLE`, and no provider request is sent. Status and doctor list the degraded TTS owner and its config paths. The explicit refs remain in the runtime snapshot, so environment or profile credentials cannot silently select a different account. Reloads and config-write preflight apply the owner-aware degradation policy: an unchanged eligible TTS owner may keep its last-known-good credentials as stale, while a new or changed failure becomes cold without blocking healthy owners. Structurally invalid refs and resolved values still fail startup or reject the update.

Top-level tts.*

Auto-TTS mode. `inbound` only sends audio after an inbound voice message; `tagged` only sends audio when the reply includes `[[tts:...]]` directives or a `[[tts:text]]` block.

Legacy toggle. `openclaw doctor --fix` migrates this to `auto`.

`"all"` includes tool/block replies in addition to final replies.

Speech provider id. When unset, OpenClaw uses the first configured provider in registry auto-select order. Legacy `provider: "edge"` is rewritten to `"microsoft"` by `openclaw doctor --fix`.

Active persona id from `personas`. Normalized to lowercase.

Stable spoken identity. Fields: `label`, `description`, `provider`, `fallbackPolicy`, `providers.<provider>`. See [Personas](</tools/tts/personas#personas>).

Cheap model for auto-summary; defaults to `agents.defaults.model.primary`. Accepts `provider/model` or a configured model alias.

Allow the model to emit TTS directives. `enabled` defaults to `true`; `allowProvider` defaults to `false`.

Provider-owned settings keyed by speech provider id. Legacy direct blocks (`tts.openai`, `.elevenlabs`, `.microsoft`, `.edge`) are rewritten by `openclaw doctor --fix`; commit only `tts.providers.<id>`.

Hard cap for TTS input characters. `/tts audio`, `tts.convert`, and `tts.speak` fail if exceeded.

Request timeout in milliseconds. A per-call `timeoutMs` (agent tool, gateway) wins when set; otherwise an explicitly configured `tts.timeoutMs` wins over any plugin-authored provider default.

Azure Speech

Env: `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY`, or `SPEECH_KEY`.

Azure Speech region (e.g. `eastus`). Env: `AZURE_SPEECH_REGION` or `SPEECH_REGION`.

Optional Azure Speech endpoint override (alias `baseUrl`).

Azure voice ShortName. Default `en-US-JennyNeural`. Legacy alias: `voice`.

SSML language code. Default `en-US`.

Azure `X-Microsoft-OutputFormat` for standard audio. Default `audio-24khz-48kbitrate-mono-mp3`.

Azure `X-Microsoft-OutputFormat` for voice-note output. Default `ogg-24khz-16bit-mono-opus`.

ElevenLabs

Falls back to `ELEVENLABS_API_KEY` or `XI_API_KEY`.

Model id. Default `eleven_multilingual_v2`. Legacy ids `eleven_turbo_v2_5`/`eleven_turbo_v2` are normalized to the matching `flash` model.

ElevenLabs voice id. Default `pMsXgVXv3BLzUgSXRplE`. Legacy alias: `voiceId`.

`stability`, `similarityBoost`, `style` (each `0..1`, defaults `0.5`/`0.75`/`0`), `useSpeakerBoost` (`true|false`, default `true`), `speed` (`0.5..2.0`, default `1.0`).

Text normalization mode.

2-letter ISO 639-1 (e.g. `en`, `de`).

Integer `0..4294967295` for best-effort determinism.

Override ElevenLabs API base URL.

Google Gemini

Falls back to `GEMINI_API_KEY` / `GOOGLE_API_KEY`. If omitted, TTS can reuse `models.providers.google.apiKey` before env fallback.

Gemini TTS model. Default `gemini-3.1-flash-tts-preview`.

Gemini prebuilt voice name. Default `Kore`. Legacy aliases: `voiceName`, `voice`.

Natural-language style prompt prepended before spoken text.

Optional speaker label prepended before spoken text when your prompt uses a named speaker.

Set to `audio-profile-v1` to wrap active persona prompt fields in a deterministic Gemini TTS prompt structure.

Google-specific extra persona prompt text appended to the template's Director's Notes.

Only `https://generativelanguage.googleapis.com` is accepted.

Gradium

Env: `GRADIUM_API_KEY`.

HTTPS Gradium API URL on `api.gradium.ai`. Default `https://api.gradium.ai`.

Default Emma (`YTpq7expH9539ERJ`). Legacy alias: `voiceId`.

Inworld

Env: `INWORLD_API_KEY`.

Default `https://api.inworld.ai`.

Default `inworld-tts-1.5-max`. Also: `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`.

Default `Sarah`. Legacy alias: `voiceId`.

Sampling temperature `0..2` (exclusive of 0).

Local CLI (tts-local-cli)

Local executable or command string for CLI TTS.

Command arguments. Supports `{{Text}}`, `{{OutputPath}}`, `{{OutputDir}}`, `{{OutputBase}}` placeholders.

Expected CLI output format. Default `mp3` for audio attachments.

Command timeout in milliseconds. Overrides the resolved TTS request timeout when set. When omitted, follows the request timeout; the plugin default is `120000`.

Optional command working directory.

Optional environment overrides for the command.

Command stdout and generated or converted audio are limited to 50 MiB. Diagnostic stderr is limited to 1 MiB. OpenClaw terminates the command and fails synthesis when either limit is exceeded.

Microsoft (no API key)

Allow Microsoft speech usage.

Microsoft neural voice name (e.g. `en-US-MichelleNeural`). Legacy alias: `voice`. If the default English voice is in effect and reply text is CJK-dominant, OpenClaw auto-switches to `zh-CN-XiaoxiaoNeural`.

Language code (e.g. `en-US`).

Microsoft output format. Default `audio-24khz-48kbitrate-mono-mp3`. Not all formats are supported by the bundled Edge-backed transport.

Percent strings (e.g. `+10%`, `-5%`).

Write JSON subtitles alongside the audio file.

Proxy URL for Microsoft speech requests.

Request timeout override (ms).

Legacy alias. Run `openclaw doctor --fix` to rewrite persisted config to `providers.microsoft`.

MiniMax

Falls back to `MINIMAX_API_KEY`. Token Plan auth via `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, or `MINIMAX_CODING_API_KEY`.

Default `https://api.minimax.io`. Env: `MINIMAX_API_HOST`.

Default `speech-2.8-hd`. Env: `MINIMAX_TTS_MODEL`.

Default `English_expressive_narrator`. Env: `MINIMAX_TTS_VOICE_ID`. Legacy alias: `voiceId`.

`0.5..2.0`. Default `1.0`.

`(0, 10]`. Default `1.0`.

Integer `-12..12`. Default `0`. Fractional values are truncated before the request.

OpenAI

Falls back to `OPENAI_API_KEY`.

OpenAI TTS model id. Default `gpt-4o-mini-tts`.

Voice name (e.g. `alloy`, `cedar`). Default `coral`. Legacy alias: `voice`.

Explicit OpenAI `instructions` field. When set, persona prompt fields are **not** auto-mapped.

Explicit response format. When omitted, OpenClaw selects Opus for voice-note targets and MP3 otherwise. Use `wav` for compatible local endpoints that do not encode compressed audio.

Extra JSON fields merged into `/audio/speech` request bodies after generated OpenAI TTS fields. Use this for OpenAI-compatible endpoints such as Kokoro that require provider-specific keys like `lang`; unsafe prototype keys are ignored.

Override the OpenAI TTS endpoint. Resolution order: config → `OPENAI_TTS_BASE_URL` → `https://api.openai.com/v1`. Non-default values are treated as OpenAI-compatible TTS endpoints, so custom model and voice names are accepted, and `speed` loses its `0.25..4.0` range check.

OpenRouter

Env: `OPENROUTER_API_KEY`. Can reuse `models.providers.openrouter.apiKey`.

Default `https://openrouter.ai/api/v1`. Legacy `https://openrouter.ai/v1` is normalized.

Default `hexgrad/kokoro-82m`. Alias: `modelId`.

Default `af_alloy`. Legacy aliases: `voice`, `voiceId`.

Default `mp3`.

Provider-native speed override.

Volcengine (BytePlus Seed Speech)

Env: `VOLCENGINE_TTS_API_KEY` or `BYTEPLUS_SEED_SPEECH_API_KEY`.

Default `seed-tts-1.0`. Env: `VOLCENGINE_TTS_RESOURCE_ID`. Use `seed-tts-2.0` when your project has TTS 2.0 entitlement.

App key header. Default `aGjiRDfUWi`. Env: `VOLCENGINE_TTS_APP_KEY`.

Override the Seed Speech TTS HTTP endpoint. Env: `VOLCENGINE_TTS_BASE_URL`.

Voice type. Default `en_female_anna_mars_bigtts`. Env: `VOLCENGINE_TTS_VOICE`. Legacy alias: `voice`.

Provider-native speed ratio, `0.2..3`.

Provider-native emotion tag.

Legacy Volcengine Speech Console fields. Env: `VOLCENGINE_TTS_APPID`, `VOLCENGINE_TTS_TOKEN`, `VOLCENGINE_TTS_CLUSTER` (default `volcano_tts`).

xAI

Env: `XAI_API_KEY`.

Default `https://api.x.ai/v1`. Env: `XAI_BASE_URL`.

Default `eve`. With auth, `openclaw infer tts voices --provider xai` fetches the current built-in catalog; without auth it lists offline fallbacks `ara`, `eve`, `leo`, `rex`, and `sal`. Account custom voice IDs are forwarded even when absent from the built-in list. Legacy alias: `voiceId`.

BCP-47 language code or `auto`. Default `en`.

Default `mp3`.

Provider-native speed override, `0.7..1.5`.

Xiaomi MiMo

Env: `XIAOMI_API_KEY`.

Default `https://api.xiaomimimo.com/v1`. Env: `XIAOMI_BASE_URL`.

Default `mimo-v2.5-tts`. Env: `XIAOMI_TTS_MODEL`. Also supports `mimo-v2.5-tts-voicedesign`.

Default `mimo_default` for preset-voice models. Env: `XIAOMI_TTS_VOICE`. Legacy alias: `voice`. Not sent for `mimo-v2.5-tts-voicedesign`.

Default `mp3`. Env: `XIAOMI_TTS_FORMAT`.

Optional natural-language style instruction sent as the user message; not spoken. For `mimo-v2.5-tts-voicedesign`, this is the voice-design prompt; OpenClaw supplies a default when omitted.

Was this useful?YesNo

Open issue