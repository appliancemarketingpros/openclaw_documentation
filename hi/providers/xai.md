---
title: xAI
source_url: https://docs.openclaw.ai/hi/providers/xai
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw Grok मॉडल के लिए एक बंडल किया हुआ `xai` प्रदाता Plugin शिप करता है। अधिकतर उपयोगकर्ताओं के लिए, अनुशंसित पथ पात्र SuperGrok या X Premium सदस्यता के साथ Grok OAuth है। OpenClaw local-first रहता है: Gateway, कॉन्फ़िग, रूटिंग, और टूल आपकी मशीन पर चलते हैं, जबकि Grok मॉडल अनुरोध xAI के माध्यम से प्रमाणित होते हैं और xAI की API को भेजे जाते हैं।

OAuth के लिए xAI API कुंजी की आवश्यकता नहीं होती, और इसके लिए Grok Build ऐप की भी आवश्यकता नहीं होती। xAI सहमति स्क्रीन पर फिर भी Grok Build दिखा सकता है क्योंकि OpenClaw xAI के साझा OAuth क्लाइंट का उपयोग करता है।

## अपना सेटअप पथ चुनें

अपने OpenClaw इंस्टॉल की स्थिति से मेल खाने वाला पथ उपयोग करें:

* ### New OpenClaw install

जब आप नया स्थानीय Gateway सेट अप कर रहे हों, तो डेमन इंस्टॉल के साथ ऑनबोर्डिंग चलाएं, फिर मॉडल/प्रमाणीकरण चरण में xAI/Grok OAuth विकल्प चुनें:

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

VPS पर या SSH के माध्यम से, सीधे xAI OAuth चुनें; OpenClaw device-code सत्यापन का उपयोग करता है और localhost callback की आवश्यकता नहीं होती:

bashCopy code
[code]
    openclaw onboard --install-daemon --auth-choice xai-oauth
[/code]

OAuth के लिए xAI API कुंजी की आवश्यकता नहीं होती। OpenClaw को Grok Build ऐप की आवश्यकता नहीं होती। xAI सहमति ऐप को फिर भी Grok Build के रूप में लेबल कर सकता है क्योंकि OpenClaw xAI के साझा OAuth क्लाइंट का उपयोग करता है।

* ### Existing OpenClaw install

यदि OpenClaw पहले से कॉन्फ़िगर है, तो केवल xAI में साइन इन करें। सिर्फ Grok कनेक्ट करने के लिए पूरी ऑनबोर्डिंग दोबारा न चलाएं या डेमन फिर से इंस्टॉल न करें:

bashCopy code
[code]
    openclaw models auth login --provider xai --method oauth
[/code]

साइन इन करने के बाद Grok को डिफ़ॉल्ट मॉडल बनाने के लिए, इसे अलग से लागू करें:

bashCopy code
[code]
    openclaw models set xai/grok-4.3
[/code]

पूरी ऑनबोर्डिंग केवल तभी दोबारा चलाएं जब आप जानबूझकर Gateway, डेमन, चैनल, वर्कस्पेस, या अन्य सेटअप विकल्प बदलना चाहते हों।

* ### API-key path

API-key सेटअप xAI Console कुंजियों और उन मीडिया सतहों के लिए अभी भी काम करता है जिन्हें key-backed प्रदाता कॉन्फ़िग की आवश्यकता होती है:

bashCopy code
[code]
    openclaw models auth login --provider xai --method api-keyexport XAI_API_KEY=xai-...
[/code]

* ### Pick a model

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "xai/grok-4.3" } } },}
[/code]

## OAuth समस्या निवारण

  * SSH, Docker, VPS, या अन्य remote सेटअप के लिए, `openclaw models auth login --provider xai --method oauth` उपयोग करें; xAI OAuth localhost callback के बजाय device-code सत्यापन का उपयोग करता है।

  * यदि sign-in सफल होता है लेकिन Grok डिफ़ॉल्ट मॉडल नहीं है, तो `openclaw models set xai/grok-4.3` चलाएं।

  * सहेजे गए xAI auth profiles निरीक्षण करने के लिए, चलाएं:

bashCopy code
[code]openclaw models auth list --provider xaiopenclaw models status
[/code]

  * xAI तय करता है कि कौन से खाते OAuth API tokens प्राप्त कर सकते हैं। यदि कोई खाता पात्र नहीं है, तो API-key पथ आज़माएं या xAI की ओर subscription जांचें।


## बिल्ट-इन कैटलॉग

OpenClaw मौजूदा xAI chat models को out of the box शामिल करता है, model pickers में सबसे नए पहले क्रम में:

Family | Model ids  
---|---  
Grok Build 0.1 | `grok-build-0.1`  
Grok 4.3 | `grok-4.3`  
Grok 4.20 Beta | `grok-4.20-beta-latest-reasoning`, `grok-4.20-beta-latest-non-reasoning`  
  
Plugin मौजूदा configs के लिए पुराने Grok 3, Grok 4, Grok 4 Fast, Grok 4.1 Fast, और Grok Code slugs को अभी भी forward-resolve करता है। Official Grok Code Fast aliases `grok-build-0.1` में normalize होते हैं; OpenClaw selectable catalog में अन्य retired upstream slugs अब नहीं दिखाता।

## OpenClaw फीचर कवरेज

बंडल किया गया Plugin xAI की मौजूदा public API surface को OpenClaw के साझा प्रदाता और tool contracts पर map करता है। साझा contract में फिट न होने वाली capabilities (उदाहरण के लिए streaming TTS और realtime voice) expose नहीं की जातीं - नीचे तालिका देखें।

xAI capability | OpenClaw surface | Status  
---|---|---  
Chat / Responses | `xai/<model>` model provider | हां  
Server-side web search | `web_search` provider `grok` | हां  
Server-side X search | `x_search` tool | हां  
Server-side code execution | `code_execution` tool | हां  
Images | `image_generate` | हां  
Videos | `video_generate` | हां  
Batch text-to-speech | `messages.tts.provider: "xai"` / `tts` | हां  
Streaming TTS | - | Expose नहीं; OpenClaw का TTS contract complete audio buffers लौटाता है  
Batch speech-to-text | `tools.media.audio` / media understanding | हां  
Streaming speech-to-text | Voice Call `streaming.provider: "xai"` | हां  
Realtime voice | - | अभी expose नहीं; अलग session/WebSocket contract  
Files / batches | Generic model API compatibility only | first-class OpenClaw tool नहीं  
  
### Fast-mode mappings

`/fast on` या `agents.defaults.models["xai/<model>"].params.fastMode: true` native xAI requests को इस प्रकार rewrite करता है:

Source model | Fast-mode target  
---|---  
`grok-3` | `grok-3-fast`  
`grok-3-mini` | `grok-3-mini-fast`  
`grok-4` | `grok-4-fast`  
`grok-4-0709` | `grok-4-fast`  
  
### Legacy compatibility aliases

Legacy aliases अभी भी canonical bundled ids में normalize होते हैं:

Legacy alias | Canonical id  
---|---  
`grok-code-fast-1` | `grok-build-0.1`  
`grok-code-fast` | `grok-build-0.1`  
`grok-code-fast-1-0825` | `grok-build-0.1`  
`grok-4-fast-reasoning` | `grok-4-fast`  
`grok-4-1-fast-reasoning` | `grok-4-1-fast`  
`grok-4.20-reasoning` | `grok-4.20-beta-latest-reasoning`  
`grok-4.20-non-reasoning` | `grok-4.20-beta-latest-non-reasoning`  
  
## Features

Web search

बंडल किया गया `grok` web-search provider xAI OAuth को प्राथमिकता देता है, फिर `XAI_API_KEY` या Plugin web-search key पर fallback करता है:

bashCopy code
[code]
    openclaw models auth login --provider xai --method oauthopenclaw config set tools.web.search.provider grok
[/code]

Video generation

बंडल किया गया `xai` Plugin साझा `video_generate` tool के माध्यम से video generation register करता है।

  * डिफ़ॉल्ट video model: `xai/grok-imagine-video`
  * Modes: text-to-video, image-to-video, reference-image generation, remote video edit, और remote video extension
  * Aspect ratios: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`
  * Resolutions: `480P`, `720P`
  * Duration: generation/image-to-video के लिए 1-15 seconds, `reference_image` roles उपयोग करते समय 1-10 seconds, extension के लिए 2-10 seconds
  * Reference-image generation: हर supplied image के लिए `imageRoles` को `reference_image` पर सेट करें; xAI ऐसी 7 images तक स्वीकार करता है
  * डिफ़ॉल्ट operation timeout: 600 seconds, जब तक `video_generate.timeoutMs` या `agents.defaults.videoGenerationModel.timeoutMs` सेट न हो


xAI को डिफ़ॉल्ट video provider के रूप में उपयोग करने के लिए:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "xai/grok-imagine-video",      },    },  },}
[/code]

Image generation

बंडल किया गया `xai` Plugin साझा `image_generate` tool के माध्यम से image generation register करता है।

  * डिफ़ॉल्ट image model: `xai/grok-imagine-image`
  * अतिरिक्त model: `xai/grok-imagine-image-quality`
  * Modes: text-to-image और reference-image edit
  * Reference inputs: एक `image` या पांच तक `images`
  * Aspect ratios: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `2:3`, `3:2`
  * Resolutions: `1K`, `2K`
  * Count: 4 images तक
  * डिफ़ॉल्ट operation timeout: 600 seconds, जब तक `image_generate.timeoutMs` या `agents.defaults.imageGenerationModel.timeoutMs` सेट न हो


OpenClaw xAI से `b64_json` image responses मांगता है ताकि generated media को सामान्य channel attachment path के माध्यम से stored और delivered किया जा सके। Local reference images data URLs में convert की जाती हैं; remote `http(s)` references pass through की जाती हैं।

xAI को डिफ़ॉल्ट image provider के रूप में उपयोग करने के लिए:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "xai/grok-imagine-image",      },    },  },}
[/code]

टेक्स्ट-से-स्पीच

बंडल किया गया `xai` Plugin साझा `tts` प्रदाता सतह के माध्यम से टेक्स्ट-से-स्पीच पंजीकृत करता है।

  * आवाज़ें: `eve`, `ara`, `rex`, `sal`, `leo`, `una`
  * डिफ़ॉल्ट आवाज़: `eve`
  * फ़ॉर्मैट: `mp3`, `wav`, `pcm`, `mulaw`, `alaw`
  * भाषा: BCP-47 कोड या `auto`
  * गति: प्रदाता-नेटिव गति ओवरराइड
  * नेटिव Opus वॉयस-नोट फ़ॉर्मैट समर्थित नहीं है


xAI को डिफ़ॉल्ट TTS प्रदाता के रूप में उपयोग करने के लिए:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "xai",      providers: {        xai: {          speakerVoiceId: "eve",        },      },    },  },}
[/code]

स्पीच-से-टेक्स्ट

बंडल किया गया `xai` Plugin OpenClaw की मीडिया-अंडरस्टैंडिंग ट्रांसक्रिप्शन सतह के माध्यम से बैच स्पीच-से-टेक्स्ट पंजीकृत करता है।

  * डिफ़ॉल्ट मॉडल: `grok-stt`
  * एंडपॉइंट: xAI REST `/v1/stt`
  * इनपुट पथ: multipart ऑडियो फ़ाइल अपलोड
  * जहाँ भी इनबाउंड ऑडियो ट्रांसक्रिप्शन `tools.media.audio` का उपयोग करता है, वहाँ OpenClaw द्वारा समर्थित, जिसमें Discord वॉइस-चैनल सेगमेंट और चैनल ऑडियो अटैचमेंट शामिल हैं


इनबाउंड ऑडियो ट्रांसक्रिप्शन के लिए xAI को बाध्य करने के लिए:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [          {            type: "provider",            provider: "xai",            model: "grok-stt",          },        ],      },    },  },}
[/code]

भाषा साझा ऑडियो मीडिया कॉन्फ़िग या प्रति-कॉल ट्रांसक्रिप्शन अनुरोध के माध्यम से दी जा सकती है। प्रॉम्प्ट संकेत साझा OpenClaw सतह द्वारा स्वीकार किए जाते हैं, लेकिन xAI REST STT इंटीग्रेशन केवल फ़ाइल, मॉडल, और भाषा को फॉरवर्ड करता है क्योंकि वे वर्तमान सार्वजनिक xAI एंडपॉइंट से साफ़ तौर पर मैप होते हैं।

स्ट्रीमिंग स्पीच-से-टेक्स्ट

बंडल किया गया `xai` Plugin लाइव वॉइस-कॉल ऑडियो के लिए एक रीयलटाइम ट्रांसक्रिप्शन प्रदाता भी पंजीकृत करता है।

  * एंडपॉइंट: xAI WebSocket `wss://api.x.ai/v1/stt`
  * डिफ़ॉल्ट एन्कोडिंग: `mulaw`
  * डिफ़ॉल्ट सैंपल दर: `8000`
  * डिफ़ॉल्ट एंडपॉइंटिंग: `800ms`
  * अंतरिम ट्रांसक्रिप्ट: डिफ़ॉल्ट रूप से सक्षम


Voice Call की Twilio मीडिया स्ट्रीम G.711 µ-law ऑडियो फ़्रेम भेजती है, इसलिए xAI प्रदाता उन फ़्रेमों को ट्रांसकोडिंग के बिना सीधे फॉरवर्ड कर सकता है:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "xai",            providers: {              xai: {                apiKey: "${XAI_API_KEY}",                endpointingMs: 800,                language: "en",              },            },          },        },      },    },  },}
[/code]

प्रदाता-स्वामित्व वाला कॉन्फ़िग `plugins.entries.voice-call.config.streaming.providers.xai` के अंतर्गत रहता है। समर्थित कुंजियाँ `apiKey`, `baseUrl`, `sampleRate`, `encoding` (`pcm`, `mulaw`, या `alaw`), `interimResults`, `endpointingMs`, और `language` हैं।

x_search कॉन्फ़िगरेशन

बंडल किया गया xAI Plugin Grok के माध्यम से X (पूर्व में Twitter) सामग्री खोजने के लिए `x_search` को OpenClaw टूल के रूप में उजागर करता है।

कॉन्फ़िग पथ: `plugins.entries.xai.config.xSearch`

कुंजी | प्रकार | डिफ़ॉल्ट | विवरण  
---|---|---|---  
`enabled` | boolean | - | x_search सक्षम या अक्षम करें  
`model` | string | `grok-4-1-fast` | x_search अनुरोधों के लिए उपयोग किया गया मॉडल  
`baseUrl` | string | - | xAI Responses बेस URL ओवरराइड  
`inlineCitations` | boolean | - | परिणामों में इनलाइन उद्धरण शामिल करें  
`maxTurns` | number | - | अधिकतम बातचीत टर्न  
`timeoutSeconds` | number | - | सेकंड में अनुरोध टाइमआउट  
`cacheTtlMinutes` | number | - | मिनटों में कैश टाइम-टू-लाइव  
  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast",            baseUrl: "https://api.x.ai/v1",            inlineCitations: true,          },        },      },    },  },}
[/code]

कोड निष्पादन कॉन्फ़िगरेशन

बंडल किया गया xAI Plugin xAI के सैंडबॉक्स वातावरण में दूरस्थ कोड निष्पादन के लिए `code_execution` को OpenClaw टूल के रूप में उजागर करता है।

कॉन्फ़िग पथ: `plugins.entries.xai.config.codeExecution`

कुंजी | प्रकार | डिफ़ॉल्ट | विवरण  
---|---|---|---  
`enabled` | boolean | `true` (यदि कुंजी उपलब्ध हो) | कोड निष्पादन सक्षम या अक्षम करें  
`model` | string | `grok-4-1-fast` | कोड निष्पादन अनुरोधों के लिए उपयोग किया गया मॉडल  
`maxTurns` | number | - | अधिकतम बातचीत टर्न  
`timeoutSeconds` | number | - | सेकंड में अनुरोध टाइमआउट  
  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast",          },        },      },    },  },}
[/code]

ज्ञात सीमाएँ

  * xAI प्रमाणीकरण API कुंजी, एनवायरनमेंट वैरिएबल, Plugin कॉन्फ़िग फ़ॉलबैक, या पात्र xAI खाते के साथ OAuth का उपयोग कर सकता है। OAuth localhost callback के बिना डिवाइस-कोड सत्यापन का उपयोग करता है। xAI तय करता है कि कौन से खाते OAuth API टोकन प्राप्त कर सकते हैं, और सहमति पृष्ठ Grok Build दिखा सकता है, भले ही OpenClaw को Grok Build ऐप की आवश्यकता नहीं है।
  * OpenClaw वर्तमान में xAI मल्टी-एजेंट मॉडल परिवार को उजागर नहीं करता। xAI इन मॉडलों को Responses API के माध्यम से सर्व करता है, लेकिन वे OpenClaw के साझा एजेंट लूप द्वारा उपयोग किए गए क्लाइंट-साइड या कस्टम टूल स्वीकार नहीं करते। देखें [xAI मल्टी-एजेंट सीमाएँ](<https://docs.x.ai/developers/model-capabilities/text/multi-agent#limitations>).
  * xAI Realtime वॉइस अभी OpenClaw प्रदाता के रूप में पंजीकृत नहीं है। इसे बैच STT या स्ट्रीमिंग ट्रांसक्रिप्शन से अलग द्विदिश वॉइस सत्र अनुबंध चाहिए।
  * xAI इमेज `quality`, इमेज `mask`, और अतिरिक्त केवल-नेटिव आस्पेक्ट रेशियो तब तक उजागर नहीं किए जाते जब तक साझा `image_generate` टूल में संबंधित क्रॉस-प्रदाता नियंत्रण नहीं होते।

उन्नत नोट्स

  * OpenClaw साझा रनर पथ पर xAI-विशिष्ट टूल-स्कीमा और टूल-कॉल संगतता सुधार स्वचालित रूप से लागू करता है।
  * नेटिव xAI अनुरोधों में डिफ़ॉल्ट `tool_stream: true` होता है। इसे अक्षम करने के लिए `agents.defaults.models["xai/<model>"].params.tool_stream` को `false` पर सेट करें।
  * बंडल किया गया xAI रैपर नेटिव xAI अनुरोध भेजने से पहले असमर्थित strict टूल-स्कीमा फ़्लैग और reasoning _effort_ पेलोड कुंजियाँ हटा देता है। केवल `grok-4.3` / `grok-4.3-*` कॉन्फ़िगर करने योग्य reasoning effort घोषित करते हैं; अन्य सभी reasoning-सक्षम xAI मॉडल फिर भी `include: ["reasoning.encrypted_content"]` का अनुरोध करते हैं ताकि पिछली एन्क्रिप्टेड reasoning को फ़ॉलो-अप टर्न पर फिर से चलाया जा सके।
  * `web_search`, `x_search`, और `code_execution` OpenClaw टूल के रूप में उजागर किए जाते हैं। OpenClaw हर चैट टर्न में सभी नेटिव टूल अटैच करने के बजाय प्रत्येक टूल अनुरोध के अंदर उसे चाहिए वह विशिष्ट xAI बिल्ट-इन सक्षम करता है।
  * Grok `web_search` `plugins.entries.xai.config.webSearch.baseUrl` पढ़ता है। `x_search` `plugins.entries.xai.config.xSearch.baseUrl` पढ़ता है, फिर Grok वेब-सर्च बेस URL पर फ़ॉलबैक करता है।
  * `x_search` और `code_execution` कोर मॉडल रनटाइम में हार्डकोड होने के बजाय बंडल किए गए xAI Plugin के स्वामित्व में हैं।
  * `code_execution` दूरस्थ xAI सैंडबॉक्स निष्पादन है, स्थानीय [`exec`](</hi/tools/exec>) नहीं।


## लाइव परीक्षण

xAI मीडिया पथ यूनिट परीक्षणों और ऑप्ट-इन लाइव सूट्स द्वारा कवर किए गए हैं। लाइव प्रोब चलाने से पहले प्रोसेस एनवायरनमेंट में `XAI_API_KEY` एक्सपोर्ट करें।

bashCopy code
[code]
    pnpm test extensions/xaiOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 pnpm test:live -- extensions/xai/xai.live.test.tsOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 OPENCLAW_LIVE_IMAGE_GENERATION_PROVIDERS=xai pnpm test:live -- test/image-generation.runtime.live.test.ts
[/code]

प्रदाता-विशिष्ट लाइव फ़ाइल सामान्य TTS, टेलीफ़ोनी-अनुकूल PCM TTS सिंथेसाइज़ करती है, xAI बैच STT के माध्यम से ऑडियो ट्रांसक्राइब करती है, उसी PCM को xAI रीयलटाइम STT के माध्यम से स्ट्रीम करती है, टेक्स्ट-से-इमेज आउटपुट जनरेट करती है, और संदर्भ इमेज संपादित करती है। साझा इमेज लाइव फ़ाइल OpenClaw के रनटाइम चयन, फ़ॉलबैक, सामान्यीकरण, और मीडिया अटैचमेंट पथ के माध्यम से उसी xAI प्रदाता की पुष्टि करती है।

## संबंधित

[**मॉडल चयन** प्रदाता, मॉडल रेफ़, और फ़ेलओवर व्यवहार चुनना। ](</hi/concepts/model-providers>) [**वीडियो जनरेशन** साझा वीडियो टूल पैरामीटर और प्रदाता चयन। ](</hi/tools/video-generation>) [**सभी प्रदाता** व्यापक प्रदाता अवलोकन। ](</hi/providers>) [**समस्या निवारण** सामान्य समस्याएँ और सुधार। ](</hi/help/troubleshooting>)

Was this useful?YesNo

Open issue