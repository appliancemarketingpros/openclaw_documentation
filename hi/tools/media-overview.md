---
title: मीडिया अवलोकन
source_url: https://docs.openclaw.ai/hi/tools/media-overview
scraped_at: 2026-06-29
---

CapabilitiesTools

OpenClaw छवियां, वीडियो, और संगीत जनरेट करता है, आने वाले मीडिया (छवियां, ऑडियो, वीडियो) को समझता है, और text-to-speech के साथ उत्तरों को बोलकर सुनाता है। सभी मीडिया क्षमताएं tool-driven हैं: agent बातचीत के आधार पर तय करता है कि उन्हें कब उपयोग करना है, और हर tool तभी दिखाई देता है जब कम से कम एक backing provider configured हो।

Live speech, one-shot media tool path के बजाय Talk session contract का उपयोग करता है। Talk के तीन मोड हैं: provider-native `realtime`, local या streaming `stt-tts`, और observe-only speech capture के लिए `transcription`। ये मोड telephony, meetings, browser realtime, और native push-to-talk clients के साथ provider catalogs, event envelopes, और cancellation semantics साझा करते हैं।

## क्षमताएं

[**छवि जनरेशन** text prompts या reference images से `image_generate` के माध्यम से छवियां बनाएं और edit करें। chat sessions में async — background में चलता है और ready होने पर result post करता है। ](</hi/tools/image-generation>) [**वीडियो जनरेशन** `video_generate` के माध्यम से text-to-video, image-to-video, और video-to-video। Async — background में चलता है और ready होने पर result post करता है। ](</hi/tools/video-generation>) [**संगीत जनरेशन** `music_generate` के माध्यम से music या audio tracks जनरेट करें। chat sessions में shared media-generation task lifecycle पर async। ](</hi/tools/music-generation>) [**Text-to-speech** `tts` tool और `messages.tts` config के माध्यम से outbound replies को spoken audio में बदलें। Synchronous। ](</hi/tools/tts>) [**मीडिया समझ** vision-capable model providers और dedicated media-understanding plugins का उपयोग करके inbound images, audio, और video को summarize करें। ](</hi/nodes/media-understanding>) [**Speech-to-text** batch STT या Voice Call streaming STT providers के माध्यम से inbound voice messages को transcribe करें। ](</hi/nodes/audio>)

## Provider क्षमता मैट्रिक्स

Provider | Image | Video | Music | TTS | STT | Realtime voice | Media understanding  
---|---|---|---|---|---|---|---  
Alibaba |  | ✓ |  |  |  |  |   
BytePlus |  | ✓ |  |  |  |  |   
ComfyUI | ✓ | ✓ | ✓ |  |  |  |   
DeepInfra | ✓ | ✓ |  | ✓ | ✓ |  | ✓  
Deepgram |  |  |  |  | ✓ | ✓ |   
ElevenLabs |  |  |  | ✓ | ✓ |  |   
fal | ✓ | ✓ | ✓ |  |  |  |   
Google | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓  
Gradium |  |  |  | ✓ |  |  |   
Local CLI |  |  |  | ✓ |  |  |   
Microsoft |  |  |  | ✓ |  |  |   
Microsoft Foundry | ✓ |  |  |  |  |  |   
MiniMax | ✓ | ✓ | ✓ | ✓ |  |  |   
Mistral |  |  |  |  | ✓ |  |   
OpenAI | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓  
OpenRouter | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓  
Qwen |  | ✓ |  |  |  |  |   
Runway |  | ✓ |  |  |  |  |   
SenseAudio |  |  |  |  | ✓ |  |   
Together |  | ✓ |  |  |  |  |   
Vydra | ✓ | ✓ |  | ✓ |  |  |   
xAI | ✓ | ✓ |  | ✓ | ✓ |  | ✓  
Xiaomi MiMo | ✓ |  |  | ✓ |  |  | ✓  
  
## Async बनाम synchronous

Capability | Mode | Why  
---|---|---  
Image | Asynchronous | Provider processing chat turn से अधिक समय तक चल सकती है; generated attachments shared completion path का उपयोग करते हैं।  
Text-to-speech | Synchronous | Provider responses कुछ seconds में return होते हैं; reply audio से attached होते हैं।  
Video | Asynchronous | Provider processing में 30 s से कई minutes तक लगते हैं; slow queues configured timeout तक चल सकती हैं।  
Music | Asynchronous | video जैसी ही provider-processing characteristic।  
  
Async tools के लिए, OpenClaw request को provider को submit करता है, तुरंत task id return करता है, और task ledger में job track करता है। job चलते समय agent अन्य messages का जवाब देना जारी रखता है। जब provider finish करता है, OpenClaw generated media paths के साथ agent को wake करता है ताकि वह session के normal visible-reply mode के माध्यम से user को बता सके: configured होने पर automatic final reply delivery, या जब session को message tool की आवश्यकता हो तो `message(action="send")`। यदि requester session inactive है या उसकी active wake fail होती है, और कुछ generated media अभी भी completion reply से missing है, OpenClaw केवल missing media के साथ idempotent direct fallback भेजता है। completion reply द्वारा पहले से delivered media दोबारा post नहीं किया जाता।

## Speech-to-text और Voice Call

Deepgram, DeepInfra, ElevenLabs, Mistral, OpenAI, OpenRouter, SenseAudio, और xAI configured होने पर batch `tools.media.audio` path के माध्यम से सभी inbound audio को transcribe कर सकते हैं। Voice note को mention gating या command parsing के लिए preflight करने वाले channel plugins inbound context पर transcribed attachment mark करते हैं, ताकि shared media-understanding pass उसी audio के लिए दूसरी STT call करने के बजाय उस transcript को reuse करे।

Deepgram, ElevenLabs, Mistral, OpenAI, और xAI Voice Call streaming STT providers भी register करते हैं, ताकि live phone audio को completed recording की प्रतीक्षा किए बिना selected vendor को forward किया जा सके।

Live user conversations के लिए, [Talk mode](</hi/nodes/talk>) को प्राथमिकता दें। Batch audio attachments media path पर रहते हैं; browser realtime, native push-to-talk, telephony, और meeting audio को Talk events और Gateway द्वारा लौटाए गए session-scoped catalogs का उपयोग करना चाहिए।

## Provider mappings (vendors surfaces में कैसे split होते हैं)

Google

Image, video, music, batch TTS, backend realtime voice, और media-understanding surfaces।

OpenAI

Image, video, batch TTS, batch STT, Voice Call streaming STT, backend realtime voice, और memory-embedding surfaces।

DeepInfra

Chat/model routing, image generation/editing, text-to-video, batch TTS, batch STT, image media understanding, और memory-embedding surfaces। DeepInfra-native rerank/classification/object-detection models तब तक registered नहीं होते जब तक OpenClaw के पास उन categories के लिए dedicated provider contracts न हों।

xAI

Image, video, search, code-execution, batch TTS, batch STT, और Voice Call streaming STT। xAI Realtime voice एक upstream capability है लेकिन OpenClaw में तब तक registered नहीं है जब तक shared realtime-voice contract उसे represent नहीं कर सकता।

## संबंधित

  * [छवि जनरेशन](</hi/tools/image-generation>)
  * [वीडियो जनरेशन](</hi/tools/video-generation>)
  * [संगीत जनरेशन](</hi/tools/music-generation>)
  * [Text-to-speech](</hi/tools/tts>)
  * [मीडिया समझ](</hi/nodes/media-understanding>)
  * [Audio nodes](</hi/nodes/audio>)
  * [Talk mode](</hi/nodes/talk>)


Was this useful?YesNo

Open issue