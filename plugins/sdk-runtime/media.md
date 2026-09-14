---
title: Plugin runtime media helpers
source_url: https://docs.openclaw.ai/plugins/sdk-runtime/media
scraped_at: 2026-09-14
---

ReferencePlugin SDK reference

Speech, media understanding, generation, web search, and the low-level media utilities. Part of the [Plugin runtime helpers](</plugins/sdk-runtime>) reference.

## Media and generation namespaces

api.runtime.tts

Text-to-speech synthesis.

typescriptCopy code
[code]
    // Standard TTSconst clip = await api.runtime.tts.textToSpeech({  text: "Hello from OpenClaw",  cfg: api.config,}); // Telephony-optimized TTSconst telephonyClip = await api.runtime.tts.textToSpeechTelephony({  text: "Hello from OpenClaw",  cfg: api.config,}); // List available voicesconst voices = await api.runtime.tts.listVoices({  provider: "elevenlabs",  cfg: api.config,});
[/code]

Uses core `tts` configuration and provider selection. Returns PCM audio buffer + sample rate. `textToSpeechStream` is also available for streaming synthesis.

api.runtime.mediaUnderstanding

Image, audio, and video analysis.

typescriptCopy code
[code]
    // Describe an imageconst image = await api.runtime.mediaUnderstanding.describeImageFile({  filePath: "/tmp/inbound-photo.jpg",  cfg: api.config,  agentDir: "/tmp/agent",}); // Prepare a capture limit before installing audio receive listeners.const budget = await api.runtime.mediaUnderstanding.resolveAudioInputBudget({  cfg: api.config,});// budget.enabled is false when audio understanding is disabled. Otherwise,// budget.maxBytes includes the container header and covers the largest fallback. // Transcribe audioconst { text } = await api.runtime.mediaUnderstanding.transcribeAudioFile({  filePath: "/tmp/inbound-audio.ogg",  cfg: api.config,  mime: "audio/ogg", // optional, for when MIME cannot be inferred}); // Describe a videoconst video = await api.runtime.mediaUnderstanding.describeVideoFile({  filePath: "/tmp/inbound-video.mp4",  cfg: api.config,}); // Generic file analysisconst result = await api.runtime.mediaUnderstanding.runFile({  filePath: "/tmp/inbound-file.pdf",  cfg: api.config,}); // Structured image extraction through a specific provider/model.// Include at least one image; text inputs are supplemental context.// receiptImageBuffer is your own image bytes, not an SDK-provided value.const evidence = await api.runtime.mediaUnderstanding.extractStructuredWithModel({  provider: "codex",  model: "gpt-6-astra",  input: [    {      type: "image",      buffer: receiptImageBuffer,      fileName: "receipt.png",      mime: "image/png",    },    { type: "text", text: "Prefer the printed total over handwritten notes." },  ],  instructions: "Extract vendor, total, and searchable tags.",  schemaName: "receipt.evidence",  jsonSchema: {    type: "object",    properties: {      vendor: { type: "string" },      total: { type: "number" },      tags: { type: "array", items: { type: "string" } },    },    required: ["vendor", "total"],  },  cfg: api.config,});
[/code]

Returns `{ text: undefined }` when no output is produced (e.g. skipped input).

`describeImageFileWithModel(...)` describes an already-known image through a specific provider/model, bypassing the default active-model resolution that `describeImageFile(...)` uses.

api.runtime.imageGeneration

Image generation.

typescriptCopy code
[code]
    const result = await api.runtime.imageGeneration.generate({  prompt: "A robot painting a sunset",  cfg: api.config,}); const providers = api.runtime.imageGeneration.listProviders({ cfg: api.config });
[/code]

api.runtime.videoGeneration

Video generation, mirroring the image generation shape.

typescriptCopy code
[code]
    const result = await api.runtime.videoGeneration.generate({  prompt: "A drone shot flying over a coastline at sunrise",  cfg: api.config,}); const providers = api.runtime.videoGeneration.listProviders({ cfg: api.config });
[/code]

api.runtime.musicGeneration

Music generation, mirroring the image generation shape.

typescriptCopy code
[code]
    const result = await api.runtime.musicGeneration.generate({  prompt: "An upbeat lo-fi track for a coding session",  cfg: api.config,}); const providers = api.runtime.musicGeneration.listProviders({ cfg: api.config });
[/code]

api.runtime.webSearch

Web search.

typescriptCopy code
[code]
    const providers = api.runtime.webSearch.listProviders({ config: api.config }); const result = await api.runtime.webSearch.search({  config: api.config,  args: { query: "OpenClaw plugin SDK", count: 5 },});
[/code]

api.runtime.media

Low-level media utilities.

typescriptCopy code
[code]
    import { resolvePreferredOpenClawTmpDir } from "openclaw/plugin-sdk/temp-path"; const webMedia = await api.runtime.media.loadWebMedia(url);const mime = await api.runtime.media.detectMime(buffer);const kind = api.runtime.media.mediaKindFromMime("image/jpeg"); // "image"const isVoice = api.runtime.media.isVoiceCompatibleAudio(filePath);const metadata = await api.runtime.media.getImageMetadata(filePath);const resized = await api.runtime.media.resizeToJpeg(buffer, { maxWidth: 800 });const terminalQr = await api.runtime.media.renderQrTerminal("https://openclaw.ai");const pngQr = await api.runtime.media.renderQrPngBase64("https://openclaw.ai", {  scale: 6, // 1-12  marginModules: 4, // 0-16});const pngQrDataUrl = await api.runtime.media.renderQrPngDataUrl("https://openclaw.ai");const tmpRoot = resolvePreferredOpenClawTmpDir();const pngQrFile = await api.runtime.media.writeQrPngTempFile("https://openclaw.ai", {  tmpRoot,  dirPrefix: "my-plugin-qr-",  fileName: "qr.png",});
[/code]

Was this useful?YesNo

Open issue