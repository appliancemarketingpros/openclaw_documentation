---
title: Telegram media and attachments
source_url: https://docs.openclaw.ai/channels/telegram/media
scraped_at: 2026-09-14
---

ChannelsMainstream messaging

What OpenClaw can send to Telegram beyond text, and how inbound media reaches the agent.

## Media and attachments

Photo albums, audio, video, and stickers

### Photo albums

Send multiple image attachments in one `message` tool call. OpenClaw groups consecutive photos into Telegram albums of up to 10 images, in their original order. Automatic replies with multiple photos use the same grouping. A single photo, including a final remainder of one, is sent separately.

json5Copy code
[code]
    {action: "send",channel: "telegram",to: "123456789",message: "Trip photos",attachments: [{ type: "image", media: "https://example.com/photo-1.jpg" },{ type: "image", media: "https://example.com/photo-2.jpg" },],}
[/code]

The caption goes on the first photo. Text that exceeds the caption limit follows the album as a separate message. Photos sent as documents, other media types, and messages with inline buttons keep separate sends so their existing controls and delivery behavior are preserved.

### Audio messages

Telegram distinguishes voice notes from audio files. Default: audio-file behavior; tag `[[audio_as_voice]]` in the agent reply to force a voice-note send. Inbound voice-note transcripts are framed as machine-generated, untrusted text in agent context, but mention detection still uses the raw transcript so mention-gated voice messages keep working.

json5Copy code
[code]
    {action: "send",channel: "telegram",to: "123456789",media: "https://example.com/voice.ogg",asVoice: true,}
[/code]

### Video messages

Telegram distinguishes video files from video notes. Video notes do not support captions; provided message text sends separately.

json5Copy code
[code]
    {action: "send",channel: "telegram",to: "123456789",media: "https://example.com/video.mp4",asVideoNote: true,}
[/code]

### Locations and venues

Use the existing `send` action with one standalone `location` object. Coordinates send a native pin; adding both `name` and `address` sends a native venue card. Location sends cannot be combined with message text or media.

json5Copy code
[code]
    {action: "send",channel: "telegram",to: "123456789",location: {latitude: 48.858844,longitude: 2.294351,accuracy: 12,name: "Eiffel Tower",address: "Champ de Mars, Paris",},}
[/code]

### Stickers

Inbound: static WEBP is downloaded and processed (placeholder `<media:sticker>`); animated TGS and video WEBM are skipped.

Sticker context fields: `Sticker.emoji`, `Sticker.setName`, `Sticker.fileId`, `Sticker.fileUniqueId`, `Sticker.cachedDescription`. Descriptions are cached in OpenClaw SQLite plugin state to reduce repeated vision calls.

Sticker descriptions use the configured `agents.defaults.imageModel` before shared automatic image-model selection, including the provider's MiniMax image routing. The sticker description uses one selected model and does not try the configured fallback list if that model fails. A failed description is not cached; general media analysis can still run separately with its normal fallback handling.

Enable sticker actions:

json5Copy code
[code]
    {channels: {telegram: {  actions: {    sticker: true,  },},},}
[/code]

Send:

json5Copy code
[code]
    {action: "sticker",channel: "telegram",to: "123456789",fileId: "CAACAgIAAxkBAAI...",}
[/code]

Search cached stickers:

json5Copy code
[code]
    {action: "sticker-search",channel: "telegram",query: "cat waving",limit: 5,}
[/code]

Was this useful?YesNo

Open issue