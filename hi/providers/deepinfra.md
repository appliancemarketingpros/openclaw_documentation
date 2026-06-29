---
title: DeepInfra
source_url: https://docs.openclaw.ai/hi/providers/deepinfra
scraped_at: 2026-06-29
---

ModelsProviders

DeepInfra एक **एकीकृत API** प्रदान करता है, जो अनुरोधों को एक ही endpoint और API key के पीछे सबसे लोकप्रिय open source और अग्रणी मॉडल तक रूट करता है। यह OpenAI-संगत है, इसलिए अधिकांश OpenAI SDKs base URL बदलने से काम करते हैं।

## Plugin इंस्टॉल करें

आधिकारिक Plugin इंस्टॉल करें, फिर Gateway रीस्टार्ट करें:

bashCopy code
[code]
    openclaw plugins install @openclaw/deepinfra-provideropenclaw gateway restart
[/code]

## API key प्राप्त करना

  1. <https://deepinfra.com/> पर जाएं
  2. साइन इन करें या खाता बनाएं
  3. Dashboard / Keys पर जाएं और नई API key जनरेट करें या स्वतः बनाई गई key का उपयोग करें


## CLI सेटअप

bashCopy code
[code]
    openclaw onboard --deepinfra-api-key <key>
[/code]

या environment variable सेट करें:

bashCopy code
[code]
    export DEEPINFRA_API_KEY="<your-deepinfra-api-key>" # pragma: allowlist secret
[/code]

## Config स्निपेट

json5Copy code
[code]
    {  env: { DEEPINFRA_API_KEY: "<your-deepinfra-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "deepinfra/deepseek-ai/DeepSeek-V4-Flash" },    },  },}
[/code]

## समर्थित OpenClaw सतहें

Plugin उन सभी DeepInfra सतहों को पंजीकृत करता है जो मौजूदा OpenClaw प्रदाता contracts से मेल खाती हैं। चैट, image generation, और video generation अपने model catalogues को `/v1/openai/models?sort_by=openclaw&filter=with_meta` से लाइव refresh करते हैं जब `DEEPINFRA_API_KEY` configured होता है; अन्य सतहें नीचे दिए गए curated static defaults का उपयोग करती हैं।

सतह | डिफ़ॉल्ट मॉडल | OpenClaw config/tool  
---|---|---  
चैट / मॉडल प्रदाता | लाइव catalog से पहला chat-tagged entry (manifest fallback `deepseek-ai/DeepSeek-V4-Flash`) | `agents.defaults.model`  
Image generation/editing | लाइव catalog से पहला `image-gen`-tagged entry (static fallback `black-forest-labs/FLUX-1-schnell`) | `image_generate`, `agents.defaults.imageGenerationModel`  
मीडिया समझ | images के लिए `moonshotai/Kimi-K2.5` | incoming image समझ  
Speech-to-text | `openai/whisper-large-v3-turbo` | incoming audio transcription  
Text-to-speech | `hexgrad/Kokoro-82M` | `messages.tts.provider: "deepinfra"`  
Video generation | लाइव catalog से पहला `video-gen`-tagged entry (static fallback `Pixverse/Pixverse-T2V`) | `video_generate`, `agents.defaults.videoGenerationModel`  
Memory embeddings | `BAAI/bge-m3` | `agents.defaults.memorySearch.provider: "deepinfra"`  
  
DeepInfra reranking, classification, object-detection, और अन्य native model types भी उपलब्ध कराता है। OpenClaw में इन श्रेणियों के लिए अभी first-class provider contracts नहीं हैं, इसलिए यह Plugin उन्हें अभी पंजीकृत नहीं करता।

## उपलब्ध मॉडल

OpenClaw startup पर उपलब्ध DeepInfra models को dynamic रूप से discover करता है। उपलब्ध models की पूरी सूची देखने के लिए `/models deepinfra` का उपयोग करें।

[DeepInfra.com](<https://deepinfra.com/>) पर उपलब्ध किसी भी model को `deepinfra/` prefix के साथ उपयोग किया जा सकता है:

CodeCopy code
[code]
    deepinfra/deepseek-ai/DeepSeek-V4-Flashdeepinfra/deepseek-ai/DeepSeek-V3.2deepinfra/MiniMaxAI/MiniMax-M2.5deepinfra/moonshotai/Kimi-K2.5deepinfra/nvidia/NVIDIA-Nemotron-3-Super-120B-A12Bdeepinfra/zai-org/GLM-5.1...and many more
[/code]

## नोट्स

  * Model refs `deepinfra/<provider>/<model>` होते हैं (जैसे, `deepinfra/Qwen/Qwen3-Max`)।
  * डिफ़ॉल्ट मॉडल: `deepinfra/deepseek-ai/DeepSeek-V4-Flash`
  * Base URL: `https://api.deepinfra.com/v1/openai`
  * Native video generation `https://api.deepinfra.com/v1/inference/<model>` का उपयोग करता है।


## संबंधित

  * [Model providers](</hi/concepts/model-providers>)
  * [All providers](</hi/providers>)


Was this useful?YesNo

Open issue