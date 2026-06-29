---
title: टेक्स्ट-टू-स्पीच
source_url: https://docs.openclaw.ai/hi/tools/tts
scraped_at: 2026-06-29
---

CapabilitiesTools

OpenClaw आउटबाउंड उत्तरों को **14 स्पीच प्रदाताओं** में ऑडियो में बदल सकता है और Feishu, Matrix, Telegram, और WhatsApp पर नेटिव वॉइस संदेश, बाकी सभी जगह ऑडियो अटैचमेंट, और टेलीफोनी तथा Talk के लिए PCM/Ulaw स्ट्रीम डिलीवर कर सकता है।

TTS, Talk के `stt-tts` मोड का स्पीच-आउटपुट हिस्सा है। प्रदाता-नेटिव `realtime` Talk सत्र इस TTS पथ को कॉल करने के बजाय रियलटाइम प्रदाता के अंदर स्पीच सिंथेसाइज़ करते हैं, जबकि `transcription` सत्र सहायक की वॉइस प्रतिक्रिया सिंथेसाइज़ नहीं करते।

## त्वरित शुरुआत

* ### Pick a provider

OpenAI और ElevenLabs सबसे भरोसेमंद होस्टेड विकल्प हैं। Microsoft और Local CLI बिना API कुंजी के काम करते हैं। पूरी सूची के लिए प्रदाता मैट्रिक्स देखें।

* ### Set the API key

अपने प्रदाता के लिए env var निर्यात करें (उदाहरण के लिए `OPENAI_API_KEY`, `ELEVENLABS_API_KEY`)। Microsoft और Local CLI को किसी कुंजी की ज़रूरत नहीं है।

* ### Enable in config

`messages.tts.auto: "always"` और `messages.tts.provider` सेट करें:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",    },  },}
[/code]

* ### Try it in chat

`/tts status` वर्तमान स्थिति दिखाता है। `/tts audio Hello from OpenClaw` एक बार का ऑडियो उत्तर भेजता है।

## समर्थित प्रदाता

प्रदाता | प्रमाणीकरण | नोट्स  
---|---|---  
**Azure Speech** | `AZURE_SPEECH_KEY` \+ `AZURE_SPEECH_REGION` (साथ ही `AZURE_SPEECH_API_KEY`, `SPEECH_KEY`, `SPEECH_REGION`) | नेटिव Ogg/Opus वॉइस-नोट आउटपुट और टेलीफोनी।  
**DeepInfra** | `DEEPINFRA_API_KEY` | OpenAI-संगत TTS। डिफ़ॉल्ट `hexgrad/Kokoro-82M` है।  
**ElevenLabs** | `ELEVENLABS_API_KEY` या `XI_API_KEY` | वॉइस क्लोनिंग, बहुभाषी, `seed` के माध्यम से निर्धारक; Discord वॉइस प्लेबैक के लिए स्ट्रीम किया गया।  
**Google Gemini** | `GEMINI_API_KEY` या `GOOGLE_API_KEY` | Gemini API बैच TTS; `promptTemplate: "audio-profile-v1"` के माध्यम से persona-aware।  
**Gradium** | `GRADIUM_API_KEY` | वॉइस-नोट और टेलीफोनी आउटपुट।  
**Inworld** | `INWORLD_API_KEY` | स्ट्रीमिंग TTS API। नेटिव Opus वॉइस-नोट और PCM टेलीफोनी।  
**Local CLI** | कोई नहीं | कॉन्फ़िगर किया गया स्थानीय TTS कमांड चलाता है।  
**Microsoft** | कोई नहीं | `node-edge-tts` के माध्यम से सार्वजनिक Edge न्यूरल TTS। सर्वोत्तम-प्रयास, कोई SLA नहीं।  
**MiniMax** | `MINIMAX_API_KEY` (या Token Plan: `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`) | T2A v2 API। डिफ़ॉल्ट `speech-2.8-hd` है।  
**OpenAI** | `OPENAI_API_KEY` | ऑटो-सारांश के लिए भी उपयोग किया जाता है; persona `instructions` का समर्थन करता है।  
**OpenRouter** | `OPENROUTER_API_KEY` (`models.providers.openrouter.apiKey` का पुनः उपयोग कर सकता है) | डिफ़ॉल्ट मॉडल `hexgrad/kokoro-82m`।  
**Volcengine** | `VOLCENGINE_TTS_API_KEY` या `BYTEPLUS_SEED_SPEECH_API_KEY` (लेगेसी AppID/token: `VOLCENGINE_TTS_APPID`/`_TOKEN`) | BytePlus Seed Speech HTTP API।  
**Vydra** | `VYDRA_API_KEY` | साझा इमेज, वीडियो, और स्पीच प्रदाता।  
**xAI** | `XAI_API_KEY` | xAI बैच TTS। नेटिव Opus वॉइस-नोट समर्थित **नहीं** है।  
**Xiaomi MiMo** | `XIAOMI_API_KEY` | Xiaomi चैट completions के माध्यम से MiMo TTS।  
  
यदि कई प्रदाता कॉन्फ़िगर किए गए हैं, तो चयनित प्रदाता पहले उपयोग किया जाता है और बाकी fallback विकल्प होते हैं। ऑटो-सारांश `summaryModel` (या `agents.defaults.model.primary`) का उपयोग करता है, इसलिए यदि आप सारांश सक्षम रखते हैं तो उस प्रदाता का भी प्रमाणीकरण होना चाहिए।

## कॉन्फ़िगरेशन

TTS कॉन्फ़िग `~/.openclaw/openclaw.json` में `messages.tts` के अंतर्गत रहता है। एक preset चुनें और प्रदाता ब्लॉक को अनुकूलित करें:

### Azure Speech

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "azure-speech",  providers: {    "azure-speech": {      apiKey: "${AZURE_SPEECH_KEY}",      region: "eastus",      speakerVoice: "en-US-JennyNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      voiceNoteOutputFormat: "ogg-24khz-16bit-mono-opus",    },  },},},}
[/code]

### ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "elevenlabs",  providers: {    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      speakerVoiceId: "EXAVITQu4vr4xnSDxMaL",    },  },},},}
[/code]

### Google Gemini

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "google",  providers: {    google: {      apiKey: "${GEMINI_API_KEY}",      model: "gemini-3.1-flash-tts-preview",      speakerVoice: "Kore",      // Optional natural-language style prompts:      // audioProfile: "Speak in a calm, podcast-host tone.",      // speakerName: "Alex",    },  },},},}
[/code]

### Gradium

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "gradium",  providers: {    gradium: {      apiKey: "${GRADIUM_API_KEY}",      speakerVoiceId: "YTpq7expH9539ERJ",    },  },},},}
[/code]

### Inworld

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "inworld",  providers: {    inworld: {      apiKey: "${INWORLD_API_KEY}",      modelId: "inworld-tts-1.5-max",      speakerVoiceId: "Sarah",      temperature: 0.7,    },  },},},}
[/code]

### Local CLI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "tts-local-cli",  providers: {    "tts-local-cli": {      command: "say",      args: ["-o", "{{OutputPath}}", "{{Text}}"],      outputFormat: "wav",      timeoutMs: 120000,    },  },},},}
[/code]

### Microsoft (no key)

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "microsoft",  providers: {    microsoft: {      enabled: true,      speakerVoice: "en-US-MichelleNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      rate: "+0%",      pitch: "+0%",    },  },},},}
[/code]

### MiniMax

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "minimax",  providers: {    minimax: {      apiKey: "${MINIMAX_API_KEY}",      model: "speech-2.8-hd",      speakerVoiceId: "English_expressive_narrator",      speed: 1.0,      vol: 1.0,      pitch: 0,    },  },},},}
[/code]

### OpenAI + ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openai",  summaryModel: "openai/gpt-4.1-mini",  modelOverrides: { enabled: true },  providers: {    openai: {      apiKey: "${OPENAI_API_KEY}",      model: "gpt-4o-mini-tts",      speakerVoice: "alloy",    },    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      speakerVoiceId: "EXAVITQu4vr4xnSDxMaL",      voiceSettings: { stability: 0.5, similarityBoost: 0.75, style: 0.0, useSpeakerBoost: true, speed: 1.0 },      applyTextNormalization: "auto",      languageCode: "en",    },  },},},}
[/code]

### OpenRouter

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openrouter",  providers: {    openrouter: {      apiKey: "${OPENROUTER_API_KEY}",      model: "hexgrad/kokoro-82m",      speakerVoice: "af_alloy",      responseFormat: "mp3",    },  },},},}
[/code]

### Volcengine

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "volcengine",  providers: {    volcengine: {      apiKey: "${VOLCENGINE_TTS_API_KEY}",      resourceId: "seed-tts-1.0",      speakerVoice: "en_female_anna_mars_bigtts",    },  },},},}
[/code]

### xAI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xai",  providers: {    xai: {      apiKey: "${XAI_API_KEY}",      speakerVoiceId: "eve",      language: "en",      responseFormat: "mp3",    },  },},},}
[/code]

### Xiaomi MiMo

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xiaomi",  providers: {    xiaomi: {      apiKey: "${XIAOMI_API_KEY}",      model: "mimo-v2.5-tts",      speakerVoice: "mimo_default",      format: "mp3",    },  },},},}
[/code]

Xiaomi `mimo-v2.5-tts-voicedesign` के लिए, `speakerVoice` छोड़ दें और `style` को वॉइस-डिज़ाइन prompt पर सेट करें। OpenClaw उस prompt को TTS `user` संदेश के रूप में भेजता है और voicedesign मॉडल के लिए `audio.voice` नहीं भेजता।

### प्रति-एजेंट वॉइस ओवरराइड्स

जब एक एजेंट को अलग प्रदाता, आवाज़, मॉडल, पर्सोना, या ऑटो-TTS मोड के साथ बोलना चाहिए, तो `agents.list[].tts` का उपयोग करें। एजेंट ब्लॉक `messages.tts` के ऊपर डीप-मर्ज होता है, इसलिए प्रदाता क्रेडेंशियल वैश्विक प्रदाता कॉन्फिग में रह सकते हैं:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",      providers: {        elevenlabs: { apiKey: "${ELEVENLABS_API_KEY}", model: "eleven_multilingual_v2" },      },    },  },  agents: {    list: [      {        id: "reader",        tts: {          providers: {            elevenlabs: { speakerVoiceId: "EXAVITQu4vr4xnSDxMaL" },          },        },      },    ],  },}
[/code]

प्रति-एजेंट पर्सोना पिन करने के लिए, प्रदाता कॉन्फिग के साथ `agents.list[].tts.persona` सेट करें — यह केवल उस एजेंट के लिए वैश्विक `messages.tts.persona` को ओवरराइड करता है।

स्वचालित उत्तरों, `/tts audio`, `/tts status`, और `tts` एजेंट टूल के लिए प्राथमिकता क्रम:

  1. `messages.tts`
  2. सक्रिय `agents.list[].tts`
  3. चैनल ओवरराइड, जब चैनल `channels.<channel>.tts` का समर्थन करता है
  4. खाता ओवरराइड, जब चैनल `channels.<channel>.accounts.<id>.tts` पास करता है
  5. इस होस्ट के लिए स्थानीय `/tts` प्राथमिकताएं
  6. इनलाइन `[[tts:...]]` निर्देश, जब मॉडल ओवरराइड सक्षम हों


चैनल और खाता ओवरराइड `messages.tts` जैसी ही संरचना का उपयोग करते हैं और पहले की परतों के ऊपर डीप-मर्ज होते हैं, इसलिए साझा प्रदाता क्रेडेंशियल `messages.tts` में रह सकते हैं, जबकि कोई चैनल या bot खाता केवल स्पीकर आवाज़, मॉडल, पर्सोना, या ऑटो मोड बदलता है:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "openai",      providers: {        openai: { apiKey: "${OPENAI_API_KEY}", model: "gpt-4o-mini-tts" },      },    },  },  channels: {    feishu: {      accounts: {        english: {          tts: {            providers: {              openai: { speakerVoice: "shimmer" },            },          },        },      },    },  },}
[/code]

## पर्सोना

एक **पर्सोना** एक स्थिर बोली जाने वाली पहचान है जिसे प्रदाताओं में नियतात्मक रूप से लागू किया जा सकता है। यह एक प्रदाता को प्राथमिकता दे सकता है, प्रदाता-निरपेक्ष प्रॉम्प्ट आशय परिभाषित कर सकता है, और आवाज़ों, मॉडलों, प्रॉम्प्ट टेम्पलेटों, seeds, और voice settings के लिए प्रदाता-विशिष्ट bindings रख सकता है।

### न्यूनतम पर्सोना

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "narrator",      personas: {        narrator: {          label: "Narrator",          provider: "elevenlabs",          providers: {            elevenlabs: {              speakerVoiceId: "EXAVITQu4vr4xnSDxMaL",              modelId: "eleven_multilingual_v2",            },          },        },      },    },  },}
[/code]

### पूर्ण पर्सोना (प्रदाता-निरपेक्ष प्रॉम्प्ट)

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "alfred",      personas: {        alfred: {          label: "Alfred",          description: "Dry, warm British butler narrator.",          provider: "google",          fallbackPolicy: "preserve-persona",          prompt: {            profile: "A brilliant British butler. Dry, witty, warm, charming, emotionally expressive, never generic.",            scene: "A quiet late-night study. Close-mic narration for a trusted operator.",            sampleContext: "The speaker is answering a private technical request with concise confidence and dry warmth.",            style: "Refined, understated, lightly amused.",            accent: "British English.",            pacing: "Measured, with short dramatic pauses.",            constraints: ["Do not read configuration values aloud.", "Do not explain the persona."],          },          providers: {            google: {              model: "gemini-3.1-flash-tts-preview",              speakerVoice: "Algieba",              promptTemplate: "audio-profile-v1",            },            openai: { model: "gpt-4o-mini-tts", speakerVoice: "cedar" },            elevenlabs: {              speakerVoiceId: "voice_id",              modelId: "eleven_multilingual_v2",              seed: 42,              voiceSettings: {                stability: 0.65,                similarityBoost: 0.8,                style: 0.25,                useSpeakerBoost: true,                speed: 0.95,              },            },          },        },      },    },  },}
[/code]

### पर्सोना समाधान

सक्रिय पर्सोना नियतात्मक रूप से चुना जाता है:

  1. `/tts persona <id>` स्थानीय प्राथमिकता, यदि सेट हो।
  2. `messages.tts.persona`, यदि सेट हो।
  3. कोई पर्सोना नहीं।


प्रदाता चयन explicit-first चलता है:

  1. प्रत्यक्ष ओवरराइड (CLI, gateway, Talk, अनुमत TTS निर्देश)।
  2. `/tts provider <id>` स्थानीय प्राथमिकता।
  3. सक्रिय पर्सोना का `provider`।
  4. `messages.tts.provider`।
  5. रजिस्ट्री ऑटो-चयन।


हर प्रदाता प्रयास के लिए, OpenClaw इस क्रम में कॉन्फिग मर्ज करता है:

  1. `messages.tts.providers.<id>`
  2. `messages.tts.personas.<persona>.providers.<id>`
  3. विश्वसनीय अनुरोध ओवरराइड
  4. अनुमत मॉडल-उत्सर्जित TTS निर्देश ओवरराइड


### प्रदाता पर्सोना प्रॉम्प्ट का उपयोग कैसे करते हैं

पर्सोना प्रॉम्प्ट फ़ील्ड (`profile`, `scene`, `sampleContext`, `style`, `accent`, `pacing`, `constraints`) **प्रदाता-निरपेक्ष** हैं। हर प्रदाता तय करता है कि उनका उपयोग कैसे करना है:

Google Gemini

पर्सोना प्रॉम्प्ट फ़ील्ड को Gemini TTS प्रॉम्प्ट संरचना में **केवल तब** लपेटता है जब प्रभावी Google प्रदाता कॉन्फिग `promptTemplate: "audio-profile-v1"` या `personaPrompt` सेट करता है। पुराने `audioProfile` और `speakerName` फ़ील्ड अब भी Google-विशिष्ट प्रॉम्प्ट टेक्स्ट के रूप में आगे जोड़े जाते हैं। `[[tts:text]]` ब्लॉक के अंदर `[whispers]` या `[laughs]` जैसे इनलाइन ऑडियो टैग Gemini transcript के अंदर संरक्षित रहते हैं; OpenClaw ये टैग जनरेट नहीं करता।

OpenAI

पर्सोना प्रॉम्प्ट फ़ील्ड को अनुरोध के `instructions` फ़ील्ड में **केवल तब** मैप करता है जब कोई स्पष्ट OpenAI `instructions` कॉन्फिग न किया गया हो। स्पष्ट `instructions` हमेशा प्राथमिक रहता है।

Other providers

केवल `personas.<id>.providers.<provider>` के अंतर्गत प्रदाता-विशिष्ट पर्सोना bindings का उपयोग करें। पर्सोना प्रॉम्प्ट फ़ील्ड तब तक अनदेखे किए जाते हैं जब तक प्रदाता अपना पर्सोना-प्रॉम्प्ट मैपिंग लागू न करे।

### फ़ॉलबैक नीति

`fallbackPolicy` तब व्यवहार नियंत्रित करता है जब किसी पर्सोना के पास प्रयास किए गए प्रदाता के लिए **कोई binding नहीं** होता:

नीति | व्यवहार  
---|---  
`preserve-persona` | **डिफ़ॉल्ट।** प्रदाता-निरपेक्ष प्रॉम्प्ट फ़ील्ड उपलब्ध रहते हैं; प्रदाता उनका उपयोग कर सकता है या उन्हें अनदेखा कर सकता है।  
`provider-defaults` | उस प्रयास के लिए पर्सोना को प्रॉम्प्ट तैयारी से हटा दिया जाता है; अन्य प्रदाताओं पर फ़ॉलबैक जारी रहते हुए प्रदाता अपने neutral defaults उपयोग करता है।  
`fail` | उस प्रदाता प्रयास को `reasonCode: "not_configured"` और `personaBinding: "missing"` के साथ छोड़ दें। फ़ॉलबैक प्रदाता अब भी आजमाए जाते हैं।  
  
पूरा TTS अनुरोध केवल तब विफल होता है जब **हर** प्रयास किया गया प्रदाता छोड़ा जाता है या विफल होता है।

Talk सत्र प्रदाता चयन सत्र-स्कोप्ड है। Talk क्लाइंट को `talk.catalog` से प्रदाता ids, मॉडल ids, voice ids, और locales चुनने चाहिए और उन्हें Talk सत्र या handoff अनुरोध के माध्यम से पास करना चाहिए। voice सत्र खोलने से `messages.tts` या वैश्विक Talk प्रदाता defaults बदलने नहीं चाहिए।

## मॉडल-संचालित निर्देश

डिफ़ॉल्ट रूप से, सहायक एक ही उत्तर के लिए आवाज़, मॉडल, या गति ओवरराइड करने के लिए `[[tts:...]]` निर्देश उत्सर्जित **कर सकता है** , साथ ही expressive cues के लिए एक वैकल्पिक `[[tts:text]]...[[/tts:text]]` ब्लॉक, जो केवल ऑडियो में दिखाई देना चाहिए:

textCopy code
[code]
    Here you go. [[tts:speakerVoiceId=pMsXgVXv3BLzUgSXRplE model=eleven_v3 speed=1.1]][[tts:text]](laughs) Read the song once more.[[/tts:text]]
[/code]

जब `messages.tts.auto` `"tagged"` होता है, ऑडियो ट्रिगर करने के लिए **निर्देश आवश्यक** होते हैं। Streaming block delivery चैनल के देखने से पहले visible text से निर्देश हटा देता है, भले ही वे adjacent blocks में विभाजित हों।

`provider=...` तब तक अनदेखा किया जाता है जब तक `modelOverrides.allowProvider: true` न हो। जब कोई उत्तर `provider=...` घोषित करता है, तो उस निर्देश की अन्य keys केवल उसी प्रदाता द्वारा parse की जाती हैं; unsupported keys हटा दी जाती हैं और TTS निर्देश warnings के रूप में रिपोर्ट की जाती हैं।

**उपलब्ध निर्देश keys:**

  * `provider` (registered provider id; `allowProvider: true` आवश्यक)
  * `speakerVoice` / `speakerVoiceId` (legacy aliases: `voice`, `voiceName`, `voice_name`, `google_voice`, `voiceId`)
  * `model` / `google_model`
  * `stability`, `similarityBoost`, `style`, `speed`, `useSpeakerBoost`
  * `vol` / `volume` (MiniMax volume, 0–10)
  * `pitch` (MiniMax integer pitch, −12 से 12; fractional values काटे जाते हैं)
  * `emotion` (Volcengine emotion tag)
  * `applyTextNormalization` (`auto|on|off`)
  * `languageCode` (ISO 639-1)
  * `seed`


**मॉडल ओवरराइड पूरी तरह अक्षम करें:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: false } } } }
[/code]

**अन्य knobs configurable रखते हुए प्रदाता switching की अनुमति दें:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: true, allowProvider: true, allowSeed: false } } } }
[/code]

## Slash commands

एकल कमांड `/tts`। Discord पर, OpenClaw `/voice` भी register करता है क्योंकि `/tts` एक built-in Discord कमांड है — text `/tts ...` अब भी काम करता है।

textCopy code
[code]
    /tts off | on | status/tts chat on | off | default/tts latest/tts provider <id>/tts persona <id> | off/tts limit <chars>/tts summary off/tts audio <text>
[/code]

व्यवहार नोट्स:

  * `/tts on` स्थानीय TTS प्राथमिकता को `always` में लिखता है; `/tts off` इसे `off` में लिखता है।
  * `/tts chat on|off|default` वर्तमान chat के लिए session-scoped auto-TTS override लिखता है।
  * `/tts persona <id>` स्थानीय पर्सोना प्राथमिकता लिखता है; `/tts persona off` इसे साफ़ करता है।
  * `/tts latest` वर्तमान session transcript से नवीनतम assistant reply पढ़ता है और उसे एक बार audio के रूप में भेजता है। यह duplicate voice sends दबाने के लिए उस reply का केवल hash session entry पर store करता है।
  * `/tts audio` एक one-off audio reply generate करता है (TTS को on **नहीं** करता)।
  * `limit` और `summary` **local prefs** में store होते हैं, main config में नहीं।
  * `/tts status` में नवीनतम प्रयास के लिए fallback diagnostics शामिल होते हैं — `Fallback: <primary> -> <used>`, `Attempts: ...`, और प्रति-प्रयास detail (`provider:outcome(reasonCode) latency`)।
  * `/status` सक्रिय TTS mode के साथ configured provider, model, voice, और sanitized custom endpoint metadata दिखाता है जब TTS enabled हो।


## प्रति-यूज़र प्राथमिकताएं

Slash commands स्थानीय ओवरराइड `prefsPath` में लिखते हैं। डिफ़ॉल्ट `~/.openclaw/settings/tts.json` है; इसे `OPENCLAW_TTS_PREFS` env var या `messages.tts.prefsPath` से override करें।

Stored field | प्रभाव  
---|---  
`auto` | स्थानीय auto-TTS override (`always`, `off`, …)  
`provider` | स्थानीय primary provider override  
`persona` | स्थानीय persona override  
`maxLength` | Summary threshold (डिफ़ॉल्ट `1500` chars)  
`summarize` | Summary toggle (डिफ़ॉल्ट `true`)  
  
ये उस host के लिए `messages.tts` और सक्रिय `agents.list[].tts` ब्लॉक से प्रभावी config को override करते हैं।

## आउटपुट फ़ॉर्मैट (fixed)

TTS voice delivery channel-capability driven है। Channel plugins विज्ञापित करते हैं कि voice-style TTS को native `voice-note` target के लिए providers से पूछना चाहिए या सामान्य `audio-file` synthesis रखना चाहिए और केवल compatible output को voice delivery के लिए mark करना चाहिए।

  * **वॉइस-नोट सक्षम चैनल** : वॉइस-नोट उत्तर Opus को प्राथमिकता देते हैं (ElevenLabs से `opus_48000_64`, OpenAI से `opus`)। 
    * 48kHz / 64kbps वॉइस संदेश के लिए स्पष्टता और आकार का अच्छा संतुलन है।
  * **Feishu / WhatsApp** : जब कोई वॉइस-नोट उत्तर MP3/WebM/WAV/M4A या किसी अन्य संभावित ऑडियो फ़ाइल के रूप में बनता है, तो channel plugin नेटिव वॉइस संदेश भेजने से पहले `ffmpeg` के साथ उसे 48kHz Ogg/Opus में ट्रांसकोड करता है। WhatsApp परिणाम को Baileys `audio` पेलोड के माध्यम से `ptt: true` और `audio/ogg; codecs=opus` के साथ भेजता है। यदि रूपांतरण विफल होता है, तो Feishu को मूल फ़ाइल अटैचमेंट के रूप में मिलती है; WhatsApp असंगत PTT पेलोड पोस्ट करने के बजाय भेजने में विफल होता है।
  * **अन्य चैनल** : MP3 (ElevenLabs से `mp3_44100_128`, OpenAI से `mp3`)। 
    * 44.1kHz / 128kbps वाणी की स्पष्टता के लिए डिफ़ॉल्ट संतुलन है।
  * **MiniMax** : सामान्य ऑडियो अटैचमेंट के लिए MP3 (`speech-2.8-hd` मॉडल, 32kHz सैंपल दर)। चैनल-द्वारा-घोषित वॉइस-नोट लक्ष्यों के लिए, जब चैनल ट्रांसकोडिंग घोषित करता है, OpenClaw डिलीवरी से पहले `ffmpeg` के साथ MiniMax MP3 को 48kHz Opus में ट्रांसकोड करता है।
  * **Xiaomi MiMo** : डिफ़ॉल्ट रूप से MP3, या कॉन्फ़िगर होने पर WAV। चैनल-द्वारा-घोषित वॉइस-नोट लक्ष्यों के लिए, जब चैनल ट्रांसकोडिंग घोषित करता है, OpenClaw डिलीवरी से पहले `ffmpeg` के साथ Xiaomi आउटपुट को 48kHz Opus में ट्रांसकोड करता है।
  * **स्थानीय CLI** : कॉन्फ़िगर किए गए `outputFormat` का उपयोग करता है। वॉइस-नोट लक्ष्यों को Ogg/Opus में बदला जाता है और टेलीफोनी आउटपुट को `ffmpeg` के साथ कच्चे 16 kHz मोनो PCM में बदला जाता है।
  * **Google Gemini** : Gemini API TTS कच्चा 24kHz PCM लौटाता है। OpenClaw उसे ऑडियो अटैचमेंट के लिए WAV के रूप में लपेटता है, वॉइस-नोट लक्ष्यों के लिए 48kHz Opus में ट्रांसकोड करता है, और Talk/टेलीफोनी के लिए सीधे PCM लौटाता है।
  * **Gradium** : ऑडियो अटैचमेंट के लिए WAV, वॉइस-नोट लक्ष्यों के लिए Opus, और टेलीफोनी के लिए 8 kHz पर `ulaw_8000`।
  * **Inworld** : सामान्य ऑडियो अटैचमेंट के लिए MP3, वॉइस-नोट लक्ष्यों के लिए नेटिव `OGG_OPUS`, और Talk/टेलीफोनी के लिए 22050 Hz पर कच्चा `PCM`।
  * **xAI** : डिफ़ॉल्ट रूप से MP3; `responseFormat` `mp3`, `wav`, `pcm`, `mulaw`, या `alaw` हो सकता है। OpenClaw xAI के बैच REST TTS एंडपॉइंट का उपयोग करता है और पूरा ऑडियो अटैचमेंट लौटाता है; इस प्रदाता पथ द्वारा xAI का स्ट्रीमिंग TTS WebSocket उपयोग नहीं किया जाता। इस पथ द्वारा नेटिव Opus वॉइस-नोट फ़ॉर्मैट समर्थित नहीं है।
  * **Microsoft** : `microsoft.outputFormat` का उपयोग करता है (डिफ़ॉल्ट `audio-24khz-48kbitrate-mono-mp3`)। 
    * बंडल किया गया ट्रांसपोर्ट `outputFormat` स्वीकार करता है, लेकिन सेवा से सभी फ़ॉर्मैट उपलब्ध नहीं होते।
    * आउटपुट फ़ॉर्मैट मान Microsoft Speech आउटपुट फ़ॉर्मैट का पालन करते हैं (Ogg/WebM Opus सहित)।
    * Telegram `sendVoice` OGG/MP3/M4A स्वीकार करता है; यदि आपको सुनिश्चित Opus वॉइस संदेश चाहिए, तो OpenAI/ElevenLabs का उपयोग करें।
    * यदि कॉन्फ़िगर किया गया Microsoft आउटपुट फ़ॉर्मैट विफल होता है, तो OpenClaw MP3 के साथ पुनः प्रयास करता है।


OpenAI/ElevenLabs आउटपुट फ़ॉर्मैट प्रति चैनल निश्चित हैं (ऊपर देखें)।

## ऑटो-TTS व्यवहार

जब `messages.tts.auto` सक्षम होता है, OpenClaw:

  * यदि उत्तर में पहले से संरचित मीडिया है, तो TTS छोड़ देता है।
  * बहुत छोटे उत्तर (10 वर्णों से कम) छोड़ देता है।
  * जब सारांश सक्षम होते हैं, तो लंबे उत्तरों का सारांश बनाता है, `summaryModel` (या `agents.defaults.model.primary`) का उपयोग करके।
  * उत्पन्न ऑडियो को उत्तर से अटैच करता है।
  * `mode: "final"` में, टेक्स्ट स्ट्रीम पूरी होने के बाद भी स्ट्रीम किए गए अंतिम उत्तरों के लिए केवल-ऑडियो TTS भेजता है; उत्पन्न मीडिया सामान्य उत्तर अटैचमेंट की तरह उसी चैनल मीडिया सामान्यीकरण से गुजरता है।


यदि उत्तर `maxLength` से अधिक है और सारांश बंद है (या सारांश मॉडल के लिए कोई API कुंजी नहीं है), तो ऑडियो छोड़ दिया जाता है और सामान्य टेक्स्ट उत्तर भेजा जाता है।

textCopy code
[code]
    Reply -> TTS enabled?  no  -> send text  yes -> has media / short?          yes -> send text          no  -> length > limit?                   no  -> TTS -> attach audio                   yes -> summary enabled?                            no  -> send text                            yes -> summarize -> TTS -> attach audio
[/code]

## चैनल के अनुसार आउटपुट फ़ॉर्मैट

लक्ष्य | फ़ॉर्मैट  
---|---  
Feishu / Matrix / Telegram / WhatsApp | वॉइस-नोट उत्तर **Opus** को प्राथमिकता देते हैं (ElevenLabs से `opus_48000_64`, OpenAI से `opus`)। 48 kHz / 64 kbps स्पष्टता और आकार का संतुलन रखता है।  
अन्य चैनल | **MP3** (ElevenLabs से `mp3_44100_128`, OpenAI से `mp3`)। वाणी के लिए 44.1 kHz / 128 kbps डिफ़ॉल्ट।  
Talk / टेलीफोनी | प्रदाता-नेटिव **PCM** (Inworld 22050 Hz, Google 24 kHz), या टेलीफोनी के लिए Gradium से `ulaw_8000`।  
  
प्रति-प्रदाता नोट्स:

  * **Feishu / WhatsApp ट्रांसकोडिंग:** जब कोई वॉइस-नोट उत्तर MP3/WebM/WAV/M4A के रूप में आता है, तो channel plugin `ffmpeg` के साथ उसे 48 kHz Ogg/Opus में ट्रांसकोड करता है। WhatsApp Baileys के माध्यम से `ptt: true` और `audio/ogg; codecs=opus` के साथ भेजता है। यदि रूपांतरण विफल होता है: Feishu मूल फ़ाइल अटैच करने पर वापस जाता है; WhatsApp असंगत PTT पेलोड पोस्ट करने के बजाय भेजने में विफल होता है।
  * **MiniMax / Xiaomi MiMo:** डिफ़ॉल्ट MP3 (MiniMax `speech-2.8-hd` के लिए 32 kHz); `ffmpeg` के ज़रिए वॉइस-नोट लक्ष्यों के लिए 48 kHz Opus में ट्रांसकोड किया जाता है।
  * **स्थानीय CLI:** कॉन्फ़िगर किए गए `outputFormat` का उपयोग करता है। वॉइस-नोट लक्ष्यों को Ogg/Opus में और टेलीफोनी आउटपुट को कच्चे 16 kHz मोनो PCM में बदला जाता है।
  * **Google Gemini:** कच्चा 24 kHz PCM लौटाता है। OpenClaw अटैचमेंट के लिए WAV के रूप में लपेटता है, वॉइस-नोट लक्ष्यों के लिए 48 kHz Opus में ट्रांसकोड करता है, Talk/टेलीफोनी के लिए सीधे PCM लौटाता है।
  * **Inworld:** MP3 अटैचमेंट, नेटिव `OGG_OPUS` वॉइस-नोट, Talk/टेलीफोनी के लिए कच्चा `PCM` 22050 Hz।
  * **xAI:** डिफ़ॉल्ट रूप से MP3; `responseFormat` `mp3|wav|pcm|mulaw|alaw` हो सकता है। xAI के बैच REST एंडपॉइंट का उपयोग करता है — स्ट्रीमिंग WebSocket TTS का उपयोग **नहीं** किया जाता। नेटिव Opus वॉइस-नोट फ़ॉर्मैट समर्थित **नहीं** है।
  * **Microsoft:** `microsoft.outputFormat` का उपयोग करता है (डिफ़ॉल्ट `audio-24khz-48kbitrate-mono-mp3`)। Telegram `sendVoice` OGG/MP3/M4A स्वीकार करता है; यदि आपको सुनिश्चित Opus वॉइस संदेश चाहिए, तो OpenAI/ElevenLabs का उपयोग करें। यदि कॉन्फ़िगर किया गया Microsoft फ़ॉर्मैट विफल होता है, तो OpenClaw MP3 के साथ पुनः प्रयास करता है।


OpenAI और ElevenLabs आउटपुट फ़ॉर्मैट ऊपर सूचीबद्ध अनुसार प्रति चैनल निश्चित हैं।

## फ़ील्ड संदर्भ

Top-level messages.tts.*

ऑटो-TTS मोड। `inbound` केवल इनबाउंड वॉइस संदेश के बाद ऑडियो भेजता है; `tagged` केवल तब ऑडियो भेजता है जब उत्तर में `[[tts:...]]` निर्देश या `[[tts:text]]` ब्लॉक शामिल हो।

लेगेसी टॉगल। `openclaw doctor --fix` इसे `auto` में माइग्रेट करता है।

`"all"` अंतिम उत्तरों के अतिरिक्त टूल/ब्लॉक उत्तर भी शामिल करता है।

स्पीच प्रदाता id। सेट न होने पर, OpenClaw रजिस्ट्री ऑटो-सेलेक्ट क्रम में पहले कॉन्फ़िगर किए गए प्रदाता का उपयोग करता है। लेगेसी `provider: "edge"` को `openclaw doctor --fix` द्वारा `"microsoft"` में फिर से लिखा जाता है।

`personas` से सक्रिय persona id। लोअरकेस में सामान्यीकृत।

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBlcnNvbmFzLjxpZA " type="object"> स्थिर बोली जाने वाली पहचान। फ़ील्ड: `label`, `description`, `provider`, `fallbackPolicy`, `prompt`, `providers.<provider>`। Personas देखें।

ऑटो-सारांश के लिए सस्ता मॉडल; डिफ़ॉल्ट `agents.defaults.model.primary`। `provider/model` या कॉन्फ़िगर किया गया मॉडल alias स्वीकार करता है।

मॉडल को TTS निर्देश उत्सर्जित करने दें। `enabled` का डिफ़ॉल्ट `true` है; `allowProvider` का डिफ़ॉल्ट `false` है।

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb3ZpZGVycy48aWQ " type="object"> स्पीच प्रदाता id से keyed प्रदाता-स्वामित्व वाली सेटिंग्स। लेगेसी डायरेक्ट ब्लॉक (`messages.tts.openai`, `.elevenlabs`, `.microsoft`, `.edge`) `openclaw doctor --fix` द्वारा फिर से लिखे जाते हैं; केवल `messages.tts.providers.<id>` कमिट करें।

TTS इनपुट वर्णों के लिए कठोर सीमा। अधिक होने पर `/tts audio` विफल होता है।

अनुरोध timeout मिलीसेकंड में।

स्थानीय prefs JSON पथ (प्रदाता/सीमा/सारांश) को override करें। डिफ़ॉल्ट `~/.openclaw/settings/tts.json`।

Azure Speech

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY`, या `SPEECH_KEY`। OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlZ2lvbiIgdHlwZT0ic3RyaW5nIg Azure Speech क्षेत्र (जैसे `eastus`)। Env: `AZURE_SPEECH_REGION` या `SPEECH_REGION`। OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVuZHBvaW50IiB0eXBlPSJzdHJpbmci वैकल्पिक Azure Speech एंडपॉइंट override (alias `baseUrl`)। OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZSIgdHlwZT0ic3RyaW5nIg Azure voice ShortName। डिफ़ॉल्ट `en-US-JennyNeural`। लेगेसी alias: `voice`। OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI SSML भाषा कोड। डिफ़ॉल्ट `en-US`। OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg मानक ऑडियो के लिए Azure `X-Microsoft-OutputFormat`। डिफ़ॉल्ट `audio-24khz-48kbitrate-mono-mp3`। OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTm90ZU91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg वॉइस-नोट आउटपुट के लिए Azure `X-Microsoft-OutputFormat`। डिफ़ॉल्ट `ogg-24khz-16bit-mono-opus`। OPENCLAW_DOCS_MARKER:paramClose:

ElevenLabs

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg `ELEVENLABS_API_KEY` या `XI_API_KEY` पर वापस जाता है। OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci मॉडल id (जैसे `eleven_multilingual_v2`, `eleven_v3`)। OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZUlkIiB0eXBlPSJzdHJpbmci ElevenLabs voice id। लेगेसी alias: `voiceId`। OPENCLAW_DOCS_MARKER:paramClose:

`stability`, `similarityBoost`, `style` (प्रत्येक `0..1`), `useSpeakerBoost` (`true|false`), `speed` (`0.5..2.0`, `1.0` = सामान्य)।

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlQ29kZSIgdHlwZT0ic3RyaW5nIg 2-अक्षर ISO 639-1 (जैसे `en`, `de`)। OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNlZWQiIHR5cGU9Im51bWJlciI best-effort determinism के लिए पूर्णांक `0..4294967295`। OPENCLAW_DOCS_MARKER:paramClose:

Google Gemini

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg `GEMINI_API_KEY` / `GOOGLE_API_KEY` पर वापस जाता है। यदि छोड़ा गया है, तो TTS env fallback से पहले `models.providers.google.apiKey` का पुनः उपयोग कर सकता है। OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Gemini TTS मॉडल। डिफ़ॉल्ट `gemini-3.1-flash-tts-preview`। OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZSIgdHlwZT0ic3RyaW5nIg Gemini prebuilt voice नाम। डिफ़ॉल्ट `Kore`। लेगेसी aliases: `voiceName`, `voice`। OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb21wdFRlbXBsYXRlIiB0eXBlPSciYXVkaW8tcHJvZmlsZS12MSIn सक्रिय persona prompt फ़ील्ड को deterministic Gemini TTS prompt संरचना में लपेटने के लिए `audio-profile-v1` पर सेट करें। OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI केवल `https://generativelanguage.googleapis.com` स्वीकार किया जाता है। OPENCLAW_DOCS_MARKER:paramClose:

Gradium

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg पर्यावरण: `GRADIUM_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI डिफ़ॉल्ट `https://api.gradium.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZUlkIiB0eXBlPSJzdHJpbmci डिफ़ॉल्ट Emma (`YTpq7expH9539ERJ`). पुराना उपनाम: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

Inworld

### Inworld प्राथमिक

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg पर्यावरण: `INWORLD_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI डिफ़ॉल्ट `https://api.inworld.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsSWQiIHR5cGU9InN0cmluZyI डिफ़ॉल्ट `inworld-tts-1.5-max`. यह भी: `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZUlkIiB0eXBlPSJzdHJpbmci डिफ़ॉल्ट `Sarah`. पुराना उपनाम: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRlbXBlcmF0dXJlIiB0eXBlPSJudW1iZXIi सैंपलिंग तापमान `0..2`. OPENCLAW_DOCS_MARKER:paramClose:

Local CLI (tts-local-cli)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFyZ3MiIHR5cGU9InN0cmluZ1tdIg कमांड arguments. `{{Text}}`, `{{OutputPath}}`, `{{OutputDir}}`, `{{OutputBase}}` placeholders का समर्थन करता है. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0nIm1wMyIgfCAib3B1cyIgfCAid2F2Iic अपेक्षित CLI आउटपुट फ़ॉर्मैट. ऑडियो attachments के लिए डिफ़ॉल्ट `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg कमांड timeout मिलीसेकंड में. डिफ़ॉल्ट `120000`. OPENCLAW_DOCS_MARKER:paramClose:

Microsoft (no API key)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZSIgdHlwZT0ic3RyaW5nIg Microsoft neural voice नाम (जैसे `en-US-MichelleNeural`). पुराना उपनाम: `voice`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI भाषा कोड (जैसे `en-US`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Microsoft आउटपुट फ़ॉर्मैट. डिफ़ॉल्ट `audio-24khz-48kbitrate-mono-mp3`. bundled Edge-backed transport सभी फ़ॉर्मैट का समर्थन नहीं करता. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJhdGUgLyBwaXRjaCAvIHZvbHVtZSIgdHlwZT0ic3RyaW5nIg प्रतिशत strings (जैसे `+10%`, `-5%`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVkZ2UuKiIgdHlwZT0ib2JqZWN0IiBkZXByZWNhdGVk पुराना उपनाम. persisted config को `providers.microsoft` में फिर से लिखने के लिए `openclaw doctor --fix` चलाएँ. OPENCLAW_DOCS_MARKER:paramClose:

MiniMax

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg `MINIMAX_API_KEY` पर fallback करता है. Token Plan auth `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, या `MINIMAX_CODING_API_KEY` के ज़रिए. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI डिफ़ॉल्ट `https://api.minimax.io`. पर्यावरण: `MINIMAX_API_HOST`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci डिफ़ॉल्ट `speech-2.8-hd`. पर्यावरण: `MINIMAX_TTS_MODEL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZUlkIiB0eXBlPSJzdHJpbmci डिफ़ॉल्ट `English_expressive_narrator`. पर्यावरण: `MINIMAX_TTS_VOICE_ID`. पुराना उपनाम: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWVkIiB0eXBlPSJudW1iZXIi `0.5..2.0`. डिफ़ॉल्ट `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvbCIgdHlwZT0ibnVtYmVyIg `(0, 10]`. डिफ़ॉल्ट `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBpdGNoIiB0eXBlPSJudW1iZXIi Integer `-12..12`. डिफ़ॉल्ट `0`. अनुरोध से पहले fractional values को truncate किया जाता है. OPENCLAW_DOCS_MARKER:paramClose:

OpenAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg `OPENAI_API_KEY` पर fallback करता है. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci OpenAI TTS model id (जैसे `gpt-4o-mini-tts`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZSIgdHlwZT0ic3RyaW5nIg Voice नाम (जैसे `alloy`, `cedar`). पुराना उपनाम: `voice`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imluc3RydWN0aW9ucyIgdHlwZT0ic3RyaW5nIg स्पष्ट OpenAI `instructions` फ़ील्ड. सेट होने पर, persona prompt फ़ील्ड अपने-आप map **नहीं** किए जाते. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImV4dHJhQm9keSAvIGV4dHJhX2JvZHkiIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 ">Generated OpenAI TTS फ़ील्ड के बाद `/audio/speech` request bodies में merge किए जाने वाले अतिरिक्त JSON फ़ील्ड. इसका उपयोग Kokoro जैसे OpenAI-compatible endpoints के लिए करें जिन्हें `lang` जैसी provider-specific keys चाहिए; unsafe prototype keys को अनदेखा किया जाता है. OPENCLAW_DOCS_MARKER:paramClose:

OpenAI TTS endpoint override करें. Resolution order: config → `OPENAI_TTS_BASE_URL` → `https://api.openai.com/v1`. Non-default values को OpenAI-compatible TTS endpoints माना जाता है, इसलिए custom model और voice names स्वीकार किए जाते हैं.

OpenRouter

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg पर्यावरण: `OPENROUTER_API_KEY`. `models.providers.openrouter.apiKey` को फिर से उपयोग कर सकता है. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI डिफ़ॉल्ट `https://openrouter.ai/api/v1`. पुराने `https://openrouter.ai/v1` को normalize किया जाता है. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci डिफ़ॉल्ट `hexgrad/kokoro-82m`. उपनाम: `modelId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZSIgdHlwZT0ic3RyaW5nIg डिफ़ॉल्ट `af_alloy`. पुराने उपनाम: `voice`, `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJwY20iJw डिफ़ॉल्ट `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Volcengine (BytePlus Seed Speech)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg पर्यावरण: `VOLCENGINE_TTS_API_KEY` या `BYTEPLUS_SEED_SPEECH_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc291cmNlSWQiIHR5cGU9InN0cmluZyI डिफ़ॉल्ट `seed-tts-1.0`. पर्यावरण: `VOLCENGINE_TTS_RESOURCE_ID`. जब आपके project के पास TTS 2.0 entitlement हो, तो `seed-tts-2.0` का उपयोग करें. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcEtleSIgdHlwZT0ic3RyaW5nIg App key header. डिफ़ॉल्ट `aGjiRDfUWi`. पर्यावरण: `VOLCENGINE_TTS_APP_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Seed Speech TTS HTTP endpoint override करें. पर्यावरण: `VOLCENGINE_TTS_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZSIgdHlwZT0ic3RyaW5nIg Voice type. डिफ़ॉल्ट `en_female_anna_mars_bigtts`. पर्यावरण: `VOLCENGINE_TTS_VOICE`. पुराना उपनाम: `voice`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcElkIC8gdG9rZW4gLyBjbHVzdGVyIiB0eXBlPSJzdHJpbmciIGRlcHJlY2F0ZWQ पुराने Volcengine Speech Console फ़ील्ड. पर्यावरण: `VOLCENGINE_TTS_APPID`, `VOLCENGINE_TTS_TOKEN`, `VOLCENGINE_TTS_CLUSTER` (डिफ़ॉल्ट `volcano_tts`). OPENCLAW_DOCS_MARKER:paramClose:

xAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg पर्यावरण: `XAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI डिफ़ॉल्ट `https://api.x.ai/v1`. पर्यावरण: `XAI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZUlkIiB0eXBlPSJzdHJpbmci डिफ़ॉल्ट `eve`. Live voices: `ara`, `eve`, `leo`, `rex`, `sal`, `una`. पुराना उपनाम: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlIiB0eXBlPSJzdHJpbmci BCP-47 भाषा कोड या `auto`. डिफ़ॉल्ट `en`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJ3YXYiIHwgInBjbSIgfCAibXVsYXciIHwgImFsYXciJw डिफ़ॉल्ट `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Xiaomi MiMo

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg पर्यावरण: `XIAOMI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI डिफ़ॉल्ट `https://api.xiaomimimo.com/v1`. पर्यावरण: `XIAOMI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci डिफ़ॉल्ट `mimo-v2.5-tts`. पर्यावरण: `XIAOMI_TTS_MODEL`. `mimo-v2-tts` और `mimo-v2.5-tts-voicedesign` का भी समर्थन करता है. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZSIgdHlwZT0ic3RyaW5nIg preset-voice models के लिए डिफ़ॉल्ट `mimo_default`. पर्यावरण: `XIAOMI_TTS_VOICE`. पुराना उपनाम: `voice`. `mimo-v2.5-tts-voicedesign` के लिए नहीं भेजा जाता. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImZvcm1hdCIgdHlwZT0nIm1wMyIgfCAid2F2Iic डिफ़ॉल्ट `mp3`. पर्यावरण: `XIAOMI_TTS_FORMAT`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InN0eWxlIiB0eXBlPSJzdHJpbmci User message के रूप में भेजा गया वैकल्पिक natural-language style instruction; बोला नहीं जाता. `mimo-v2.5-tts-voicedesign` के लिए, यह voice-design prompt है; छूटने पर OpenClaw डिफ़ॉल्ट देता है. OPENCLAW_DOCS_MARKER:paramClose:

## Agent tool

`tts` tool text को speech में बदलता है और reply delivery के लिए audio attachment लौटाता है. Feishu, Matrix, Telegram, और WhatsApp पर, audio को file attachment के बजाय voice message के रूप में deliver किया जाता है. इस path पर `ffmpeg` उपलब्ध होने पर Feishu और WhatsApp non-Opus TTS output को transcode कर सकते हैं.

WhatsApp, Baileys के ज़रिए audio को PTT voice note (`audio` with `ptt: true`) के रूप में भेजता है और visible text को PTT audio से **अलग से** भेजता है, क्योंकि clients voice notes पर captions को consistently render नहीं करते.

Tool वैकल्पिक `channel` और `timeoutMs` फ़ील्ड स्वीकार करता है; `timeoutMs` मिलीसेकंड में per-call provider request timeout है. Per-call values `messages.tts.timeoutMs` को override करती हैं; configured TTS timeouts किसी भी plugin-authored provider default को override करते हैं.

## Gateway RPC

विधि | उद्देश्य  
---|---  
`tts.status` | वर्तमान TTS state और पिछला attempt पढ़ें.  
`tts.enable` | local auto preference को `always` पर सेट करें.  
`tts.disable` | local auto preference को `off` पर सेट करें.  
`tts.convert` | एकबारगी text → audio.  
`tts.setProvider` | local provider preference सेट करें.  
`tts.setPersona` | local persona preference सेट करें.  
`tts.providers` | configured providers और status सूचीबद्ध करें.  
  
## Service links

  * [OpenAI text-to-speech guide](<https://platform.openai.com/docs/guides/text-to-speech>)
  * [OpenAI Audio API reference](<https://platform.openai.com/docs/api-reference/audio>)
  * [Azure Speech REST text-to-speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)
  * [Azure Speech provider](</hi/providers/azure-speech>)
  * [ElevenLabs Text to Speech](<https://elevenlabs.io/docs/api-reference/text-to-speech>)
  * [ElevenLabs Authentication](<https://elevenlabs.io/docs/api-reference/authentication>)
  * [Gradium](</hi/providers/gradium>)
  * [Inworld TTS API](<https://docs.inworld.ai/tts/tts>)
  * [MiniMax T2A v2 API](<https://platform.minimaxi.com/document/T2A%20V2>)
  * [Volcengine TTS HTTP API](</hi/providers/volcengine#text-to-speech>)
  * [Xiaomi MiMo speech synthesis](</hi/providers/xiaomi#text-to-speech>)
  * [node-edge-tts](<https://github.com/SchneeHertz/node-edge-tts>)
  * [Microsoft Speech output formats](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech#audio-outputs>)
  * [xAI text to speech](<https://docs.x.ai/developers/rest-api-reference/inference/voice#text-to-speech-rest>)


## संबंधित

  * [Media overview](</hi/tools/media-overview>)
  * [Music generation](</hi/tools/music-generation>)
  * [Video generation](</hi/tools/video-generation>)
  * [Slash commands](</hi/tools/slash-commands>)
  * [Voice call plugin](</hi/plugins/voice-call>)


Was this useful?YesNo

Open issue