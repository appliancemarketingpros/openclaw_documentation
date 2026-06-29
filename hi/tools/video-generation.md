---
title: वीडियो निर्माण
source_url: https://docs.openclaw.ai/hi/tools/video-generation
scraped_at: 2026-06-29
---

CapabilitiesTools

OpenClaw एजेंट टेक्स्ट प्रॉम्प्ट, संदर्भ इमेज, या मौजूदा वीडियो से वीडियो बना सकते हैं। सोलह provider बैकएंड समर्थित हैं, जिनमें अलग-अलग मॉडल विकल्प, इनपुट मोड, और फीचर सेट हैं। एजेंट आपके कॉन्फ़िगरेशन और उपलब्ध API कुंजियों के आधार पर सही provider अपने-आप चुनता है।

OpenClaw वीडियो जनरेशन को तीन runtime मोड के रूप में मानता है:

  * `generate` \- बिना संदर्भ मीडिया वाले टेक्स्ट-से-वीडियो अनुरोध।
  * `imageToVideo` \- अनुरोध में एक या अधिक संदर्भ इमेज शामिल होती हैं।
  * `videoToVideo` \- अनुरोध में एक या अधिक संदर्भ वीडियो शामिल होते हैं।


Providers उन मोड के किसी भी उपसमुच्चय का समर्थन कर सकते हैं। टूल सबमिशन से पहले सक्रिय मोड को सत्यापित करता है और `action=list` में समर्थित मोड रिपोर्ट करता है।

## त्वरित शुरुआत

* ### प्रमाणीकरण कॉन्फ़िगर करें

किसी भी समर्थित provider के लिए API कुंजी सेट करें:

bashCopy code
[code]
    export GEMINI_API_KEY="your-key"
[/code]

* ### डिफ़ॉल्ट मॉडल चुनें (वैकल्पिक)

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "google/veo-3.1-fast-generate-preview"
[/code]

* ### एजेंट से पूछें

> सूर्यास्त के समय सर्फिंग करते हुए एक दोस्ताना लॉब्स्टर का 5-सेकंड का सिनेमैटिक वीडियो बनाएं।

एजेंट `video_generate` को अपने-आप कॉल करता है। किसी टूल allowlisting की आवश्यकता नहीं है।

## async जनरेशन कैसे काम करता है

वीडियो जनरेशन asynchronous होता है। जब एजेंट किसी सेशन में `video_generate` कॉल करता है:

  1. OpenClaw अनुरोध provider को सबमिट करता है और तुरंत एक task id लौटाता है।
  2. Provider पृष्ठभूमि में job को प्रोसेस करता है (आमतौर पर provider और resolution के आधार पर 30 सेकंड से कई मिनट; धीमे queue-backed providers कॉन्फ़िगर किए गए timeout तक चल सकते हैं)।
  3. जब वीडियो तैयार हो जाता है, OpenClaw उसी सेशन को एक आंतरिक completion event के साथ जगाता है।
  4. एजेंट सेशन के सामान्य visible-reply मोड के जरिए उपयोगकर्ता को बताता है: automatic होने पर final reply delivery, या जब सेशन को message tool चाहिए हो तब `message(action="send")`। यदि requester सेशन निष्क्रिय है या उसका active wake विफल हो जाता है, और कुछ generated video अभी भी completion reply से गायब है, तो OpenClaw केवल गायब वीडियो के साथ एक idempotent direct fallback भेजता है।


जब कोई job चल रहा हो, उसी सेशन में duplicate `video_generate` कॉल दूसरी generation शुरू करने के बजाय मौजूदा task status लौटाते हैं। CLI से progress जांचने के लिए `openclaw tasks list` या `openclaw tasks show <taskId>` का उपयोग करें।

Session-backed agent runs के बाहर (उदाहरण के लिए, direct tool invocations), टूल inline generation पर fallback करता है और उसी turn में अंतिम media path लौटाता है।

जब provider bytes लौटाता है, तो generated video files OpenClaw-managed media storage के अंतर्गत सहेजी जाती हैं। डिफ़ॉल्ट generated-video save cap video media limit का अनुसरण करती है, और `agents.defaults.mediaMaxMb` बड़े renders के लिए इसे बढ़ाता है। जब कोई provider hosted output URL भी लौटाता है, तो OpenClaw local persistence द्वारा oversized file अस्वीकार किए जाने पर task को विफल करने के बजाय वह URL deliver कर सकता है।

### Task lifecycle

State | अर्थ  
---|---  
`queued` | Task बनाया गया है, provider द्वारा स्वीकार किए जाने की प्रतीक्षा में।  
`running` | Provider प्रोसेस कर रहा है (आमतौर पर provider और resolution के आधार पर 30 सेकंड से कई मिनट)।  
`succeeded` | वीडियो तैयार है; एजेंट जागता है और इसे conversation में पोस्ट करता है।  
`failed` | Provider error या timeout; एजेंट error details के साथ जागता है।  
  
CLI से status जांचें:

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

यदि current session के लिए कोई video task पहले से `queued` या `running` है, तो `video_generate` नया task शुरू करने के बजाय मौजूदा task status लौटाता है। नई generation trigger किए बिना स्पष्ट रूप से जांचने के लिए `action: "status"` का उपयोग करें।

## समर्थित providers

Provider | डिफ़ॉल्ट मॉडल | टेक्स्ट | इमेज ref | वीडियो ref | प्रमाणीकरण  
---|---|---|---|---|---  
Alibaba | `wan2.6-t2v` | ✓ | हां (remote URL) | हां (remote URL) | `MODELSTUDIO_API_KEY`  
BytePlus (1.0) | `seedance-1-0-pro-250528` | ✓ | 2 इमेज तक (केवल I2V models; पहला + अंतिम frame) | - | `BYTEPLUS_API_KEY`  
BytePlus Seedance 1.5 | `seedance-1-5-pro-251215` | ✓ | 2 इमेज तक (role के जरिए पहला + अंतिम frame) | - | `BYTEPLUS_API_KEY`  
BytePlus Seedance 2.0 | `dreamina-seedance-2-0-260128` | ✓ | 9 reference images तक | 3 videos तक | `BYTEPLUS_API_KEY`  
ComfyUI | `workflow` | ✓ | 1 इमेज | - | `COMFY_API_KEY` या `COMFY_CLOUD_API_KEY`  
DeepInfra | `Pixverse/Pixverse-T2V` | ✓ | - | - | `DEEPINFRA_API_KEY`  
fal | `fal-ai/minimax/video-01-live` | ✓ | 1 इमेज; Seedance reference-to-video के साथ 9 तक | Seedance reference-to-video के साथ 3 videos तक | `FAL_KEY`  
Google | `veo-3.1-fast-generate-preview` | ✓ | 1 इमेज | 1 वीडियो | `GEMINI_API_KEY`  
MiniMax | `MiniMax-Hailuo-2.3` | ✓ | 1 इमेज | - | `MINIMAX_API_KEY` या MiniMax OAuth  
OpenAI | `sora-2` | ✓ | 1 इमेज | 1 वीडियो | `OPENAI_API_KEY`  
OpenRouter | `google/veo-3.1-fast` | ✓ | 4 इमेज तक (पहला/अंतिम frame या references) | - | `OPENROUTER_API_KEY`  
Qwen | `wan2.6-t2v` | ✓ | हां (remote URL) | हां (remote URL) | `QWEN_API_KEY`  
Runway | `gen4.5` | ✓ | 1 इमेज | 1 वीडियो | `RUNWAYML_API_SECRET`  
Together | `Wan-AI/Wan2.2-T2V-A14B` | ✓ | केवल `Wan-AI/Wan2.2-I2V-A14B` | - | `TOGETHER_API_KEY`  
Vydra | `veo3` | ✓ | 1 इमेज (`kling`) | - | `VYDRA_API_KEY`  
xAI | `grok-imagine-video` | ✓ | 1 first-frame image या 7 `reference_image`s तक | 1 वीडियो | `XAI_API_KEY`  
  
कुछ providers अतिरिक्त या वैकल्पिक API key env vars स्वीकार करते हैं। विवरण के लिए व्यक्तिगत provider pages देखें।

Runtime पर उपलब्ध providers, models, और runtime modes देखने के लिए `video_generate action=list` चलाएं।

### Capability matrix

`video_generate`, contract tests, और shared live sweep द्वारा उपयोग किया गया स्पष्ट mode contract:

Provider | `generate` | `imageToVideo` | `videoToVideo` | आज के shared live lanes  
---|---|---|---|---  
Alibaba | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` छोड़ा गया क्योंकि इस provider को remote `http(s)` video URLs चाहिए  
BytePlus | ✓ | ✓ | - | `generate`, `imageToVideo`  
ComfyUI | ✓ | ✓ | - | Shared sweep में नहीं; workflow-specific coverage Comfy tests के साथ रहती है  
DeepInfra | ✓ | - | - | `generate`; native DeepInfra video schemas plugin contract में text-to-video हैं  
fal | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` केवल Seedance reference-to-video उपयोग करते समय  
Google | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; shared `videoToVideo` छोड़ा गया क्योंकि मौजूदा buffer-backed Gemini/Veo sweep उस input को स्वीकार नहीं करता  
MiniMax | ✓ | ✓ | - | `generate`, `imageToVideo`  
OpenAI | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; shared `videoToVideo` छोड़ा गया क्योंकि इस org/input path को अभी provider-side video edit access चाहिए  
OpenRouter | ✓ | ✓ | - | `generate`, `imageToVideo`  
Qwen | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` छोड़ा गया क्योंकि इस provider को remote `http(s)` video URLs चाहिए  
Runway | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` केवल तब चलता है जब चुना गया model `runway/gen4_aleph` हो  
Together | ✓ | ✓ | - | `generate`, `imageToVideo`  
Vydra | ✓ | ✓ | - | `generate`; shared `imageToVideo` छोड़ा गया क्योंकि bundled `veo3` text-only है और bundled `kling` को remote image URL चाहिए  
xAI | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` छोड़ा गया क्योंकि इस provider को अभी remote MP4 URL चाहिए  
  
## Tool parameters

### आवश्यक

जनरेट किए जाने वाले वीडियो का टेक्स्ट विवरण। `action: "generate"` के लिए आवश्यक।

### सामग्री इनपुट

संयुक्त इमेज सूची के समानांतर वैकल्पिक प्रति-स्थिति भूमिका संकेत। Canonical मान: `first_frame`, `last_frame`, `reference_image`।

संयुक्त वीडियो सूची के समानांतर वैकल्पिक प्रति-स्थिति भूमिका संकेत। Canonical मान: `reference_video`।

एकल संदर्भ ऑडियो (पाथ या URL)। जब प्रदाता ऑडियो इनपुट का समर्थन करता है, तब बैकग्राउंड संगीत या वॉइस संदर्भ के लिए उपयोग किया जाता है।

संयुक्त ऑडियो सूची के समानांतर वैकल्पिक प्रति-स्थिति भूमिका संकेत। Canonical मान: `reference_audio`।

### शैली नियंत्रण

आस्पेक्ट-रेशियो संकेत जैसे `1:1`, `16:9`, `9:16`, `adaptive`, या प्रदाता-विशिष्ट मान। OpenClaw प्रति प्रदाता असमर्थित मानों को सामान्यीकृत करता है या अनदेखा करता है।

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc29sdXRpb24iIHR5cGU9InN0cmluZyI रिज़ॉल्यूशन संकेत जैसे `480P`, `720P`, `768P`, `1080P`, `4K`, या प्रदाता-विशिष्ट मान। OpenClaw प्रति प्रदाता असमर्थित मानों को सामान्यीकृत करता है या अनदेखा करता है। OPENCLAW_DOCS_MARKER:paramClose:

सेकंड में लक्षित अवधि (निकटतम प्रदाता-समर्थित मान तक राउंड की गई)।

समर्थित होने पर आउटपुट में जनरेट किया गया ऑडियो सक्षम करें। `audioRef*` (इनपुट) से अलग।

`adaptive` एक प्रदाता-विशिष्ट सेंटिनल है: इसे उन प्रदाताओं को यथावत भेजा जाता है जो अपनी क्षमताओं में `adaptive` घोषित करते हैं (जैसे BytePlus Seedance इसे इनपुट इमेज आयामों से अनुपात अपने-आप पहचानने के लिए उपयोग करता है)। जो प्रदाता इसे घोषित नहीं करते, वे टूल परिणाम में `details.ignoredOverrides` के माध्यम से मान दिखाते हैं ताकि ड्रॉप दिखाई दे।

### उन्नत

`"status"` वर्तमान सेशन टास्क लौटाता है; `"list"` प्रदाताओं का निरीक्षण करता है।

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci प्रदाता/मॉडल ओवरराइड (जैसे `runway/gen4.5`)। OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg मिलीसेकंड में वैकल्पिक प्रदाता ऑपरेशन टाइमआउट। छोड़े जाने पर, OpenClaw कॉन्फ़िगर होने पर `agents.defaults.videoGenerationModel.timeoutMs` का उपयोग करता है, अन्यथा मौजूद होने पर Plugin-लेखित प्रदाता डिफ़ॉल्ट का उपयोग करता है। OPENCLAW_DOCS_MARKER:paramClose:

JSON ऑब्जेक्ट के रूप में प्रदाता-विशिष्ट विकल्प (जैसे `{"seed": 42, "draft": true}`)। typed स्कीमा घोषित करने वाले प्रदाता कुंजियों और प्रकारों को मान्य करते हैं; अज्ञात कुंजियां या असंगतियां fallback के दौरान उम्मीदवार को छोड़ देती हैं। घोषित स्कीमा के बिना प्रदाता विकल्पों को यथावत प्राप्त करते हैं। हर प्रदाता क्या स्वीकार करता है देखने के लिए `video_generate action=list` चलाएं।

संदर्भ इनपुट रनटाइम मोड चुनते हैं:

  * कोई संदर्भ मीडिया नहीं → `generate`
  * कोई भी इमेज संदर्भ → `imageToVideo`
  * कोई भी वीडियो संदर्भ → `videoToVideo`
  * संदर्भ ऑडियो इनपुट हल किए गए मोड को **नहीं** बदलते; वे इमेज/वीडियो संदर्भों द्वारा चुने गए किसी भी मोड के ऊपर लागू होते हैं, और केवल `maxInputAudios` घोषित करने वाले प्रदाताओं के साथ काम करते हैं।


मिश्रित इमेज और वीडियो संदर्भ स्थिर साझा क्षमता सरफेस नहीं हैं। प्रति अनुरोध एक संदर्भ प्रकार को प्राथमिकता दें।

#### Fallback और typed विकल्प

कुछ क्षमता जांचें टूल सीमा के बजाय fallback लेयर पर लागू की जाती हैं, इसलिए प्राथमिक प्रदाता की सीमाओं से अधिक अनुरोध अभी भी सक्षम fallback पर चल सकता है:

  * कोई `maxInputAudios` (या `0`) घोषित न करने वाला सक्रिय उम्मीदवार तब छोड़ा जाता है जब अनुरोध में ऑडियो संदर्भ हों; अगला उम्मीदवार आज़माया जाता है।
  * सक्रिय उम्मीदवार का `maxDurationSeconds` अनुरोधित `durationSeconds` से कम है और कोई घोषित `supportedDurationSeconds` सूची नहीं है → छोड़ा गया।
  * अनुरोध में `providerOptions` हैं और सक्रिय उम्मीदवार स्पष्ट रूप से typed `providerOptions` स्कीमा घोषित करता है → यदि दी गई कुंजियां स्कीमा में नहीं हैं या मान प्रकार मेल नहीं खाते तो छोड़ा गया। घोषित स्कीमा के बिना प्रदाता विकल्पों को यथावत प्राप्त करते हैं (बैकवर्ड-कम्पैटिबल पास-थ्रू)। कोई प्रदाता खाली स्कीमा (`capabilities.providerOptions: {}`) घोषित करके सभी प्रदाता विकल्पों से बाहर निकल सकता है, जिससे type mismatch जैसा ही skip होता है।


किसी अनुरोध में पहला skip कारण `warn` पर लॉग होता है ताकि ऑपरेटर देख सकें कि उनका प्राथमिक प्रदाता छोड़ा गया था; बाद के skip `debug` पर लॉग होते हैं ताकि लंबी fallback चेन शांत रहें। यदि हर उम्मीदवार छोड़ा जाता है, तो संकलित त्रुटि में प्रत्येक का skip कारण शामिल होता है।

## क्रियाएं

क्रिया | यह क्या करती है  
---|---  
`generate` | डिफ़ॉल्ट। दिए गए prompt और वैकल्पिक संदर्भ इनपुट से वीडियो बनाएं।  
`status` | दूसरी जनरेशन शुरू किए बिना वर्तमान सेशन के लिए चल रहे वीडियो टास्क की स्थिति जांचें।  
`list` | उपलब्ध प्रदाता, मॉडल और उनकी क्षमताएं दिखाएं।  
  
## मॉडल चयन

OpenClaw मॉडल को इस क्रम में हल करता है:

  1. **`model` टूल पैरामीटर** \- यदि एजेंट कॉल में एक निर्दिष्ट करता है।
  2. कॉन्फ़िग से **`videoGenerationModel.primary`** ।
  3. क्रम में **`videoGenerationModel.fallbacks`** ।
  4. **अपने-आप पहचान** \- वे प्रदाता जिनके पास मान्य auth है, वर्तमान डिफ़ॉल्ट प्रदाता से शुरू करके, फिर शेष प्रदाता वर्णानुक्रम में।


यदि कोई प्रदाता विफल होता है, तो अगला उम्मीदवार अपने-आप आज़माया जाता है। यदि सभी उम्मीदवार विफल होते हैं, तो त्रुटि में हर प्रयास के विवरण शामिल होते हैं।

केवल स्पष्ट `model`, `primary`, और `fallbacks` प्रविष्टियों का उपयोग करने के लिए `agents.defaults.mediaGenerationAutoProviderFallback: false` सेट करें।

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",        fallbacks: ["runway/gen4.5", "qwen/wan2.6-t2v"],      },    },  },}
[/code]

## प्रदाता नोट्स

Alibaba

DashScope / Model Studio async endpoint का उपयोग करता है। संदर्भ इमेज और वीडियो remote `http(s)` URLs होने चाहिए।

BytePlus (1.0)

प्रदाता id: `byteplus`।

मॉडल: `seedance-1-0-pro-250528` (डिफ़ॉल्ट), `seedance-1-0-pro-t2v-250528`, `seedance-1-0-pro-fast-251015`, `seedance-1-0-lite-t2v-250428`, `seedance-1-0-lite-i2v-250428`।

T2V मॉडल (`*-t2v-*`) इमेज इनपुट स्वीकार नहीं करते; I2V मॉडल और सामान्य `*-pro-*` मॉडल एकल संदर्भ इमेज (पहला फ्रेम) का समर्थन करते हैं। इमेज को positionally पास करें या `role: "first_frame"` सेट करें। इमेज दिए जाने पर T2V मॉडल IDs अपने-आप संबंधित I2V वैरिएंट में स्विच हो जाते हैं।

समर्थित `providerOptions` कुंजियां: `seed` (number), `draft` (boolean - 480p बाध्य करता है), `camera_fixed` (boolean).

BytePlus Seedance 1.5

[`@openclaw/byteplus-modelark`](<https://www.npmjs.com/package/@openclaw/byteplus-modelark>) Plugin की आवश्यकता है। प्रदाता id: `byteplus-seedance15`। मॉडल: `seedance-1-5-pro-251215`।

एकीकृत `content[]` API का उपयोग करता है। अधिकतम 2 इनपुट इमेज (`first_frame` \+ `last_frame`) का समर्थन करता है। सभी इनपुट remote `https://` URLs होने चाहिए। हर इमेज पर `role: "first_frame"` / `"last_frame"` सेट करें, या इमेज को positionally पास करें।

`aspectRatio: "adaptive"` इनपुट इमेज से अनुपात अपने-आप पहचानता है। `audio: true` `generate_audio` पर मैप होता है। `providerOptions.seed` (number) आगे भेजा जाता है।

BytePlus Seedance 2.0

[`@openclaw/byteplus-modelark`](<https://www.npmjs.com/package/@openclaw/byteplus-modelark>) Plugin की आवश्यकता है। प्रदाता id: `byteplus-seedance2`। मॉडल: `dreamina-seedance-2-0-260128`, `dreamina-seedance-2-0-fast-260128`।

एकीकृत `content[]` API का उपयोग करता है। 9 तक संदर्भ इमेज, 3 संदर्भ वीडियो, और 3 संदर्भ ऑडियो का समर्थन करता है। सभी इनपुट remote `https://` URLs होने चाहिए। हर asset पर `role` सेट करें - समर्थित मान: `"first_frame"`, `"last_frame"`, `"reference_image"`, `"reference_video"`, `"reference_audio"`।

`aspectRatio: "adaptive"` इनपुट इमेज से अनुपात अपने-आप पहचानता है। `audio: true` `generate_audio` पर मैप होता है। `providerOptions.seed` (number) आगे भेजा जाता है।

ComfyUI

Workflow-आधारित स्थानीय या cloud execution. कॉन्फ़िगर किए गए graph के माध्यम से text-to-video और image-to-video का समर्थन करता है।

fal

लंबे समय तक चलने वाले jobs के लिए queue-backed flow का उपयोग करता है। OpenClaw चल रहे fal queue job को timed out मानने से पहले default रूप से 20 मिनट तक प्रतीक्षा करता है। अधिकांश fal video models एकल image reference स्वीकार करते हैं। Seedance 2.0 reference-to-video models अधिकतम 9 images, 3 videos, और 3 audio references स्वीकार करते हैं, जिनमें कुल reference files अधिकतम 12 हो सकती हैं।

Google (Gemini / Veo)

एक image या एक video reference का समर्थन करता है। Generated-audio requests को Gemini API path पर warning के साथ अनदेखा किया जाता है क्योंकि वह API वर्तमान Veo video generation के लिए `generateAudio` parameter को reject करती है।

MiniMax

केवल एकल image reference. MiniMax `768P` और `1080P` resolutions स्वीकार करता है; `720P` जैसे requests को submission से पहले सबसे निकटतम समर्थित value में normalize किया जाता है।

OpenAI

केवल `size` override forward किया जाता है। अन्य style overrides (`aspectRatio`, `resolution`, `audio`, `watermark`) warning के साथ अनदेखे किए जाते हैं।

OpenRouter

OpenRouter की asynchronous `/videos` API का उपयोग करता है। OpenClaw job submit करता है, `polling_url` को poll करता है, और या तो `unsigned_urls` या documented job content endpoint डाउनलोड करता है। bundled `google/veo-3.1-fast` default 4/6/8 second durations, `720P`/`1080P` resolutions, और `16:9`/`9:16` aspect ratios विज्ञापित करता है।

Qwen

Alibaba जैसा ही DashScope backend. Reference inputs remote `http(s)` URLs होने चाहिए; local files को पहले ही reject कर दिया जाता है।

Runway

data URIs के माध्यम से local files का समर्थन करता है। Video-to-video के लिए `runway/gen4_aleph` आवश्यक है। Text-only runs `16:9` और `9:16` aspect ratios expose करते हैं।

Together

केवल एकल image reference.

Vydra

auth-dropping redirects से बचने के लिए सीधे `https://www.vydra.ai/api/v1` का उपयोग करता है। `veo3` केवल text-to-video के रूप में bundled है; `kling` को remote image URL चाहिए।

xAI

text-to-video, single first-frame image-to-video, xAI `reference_images` के माध्यम से अधिकतम 7 `reference_image` inputs, और remote video edit/extend flows का समर्थन करता है।

## प्रदाता capability modes

shared video-generation contract केवल flat aggregate limits के बजाय mode-specific capabilities का समर्थन करता है। नए provider implementations को explicit mode blocks को प्राथमिकता देनी चाहिए:

typescriptCopy code
[code]
    capabilities: {  generate: {    maxVideos: 1,    maxDurationSeconds: 10,    supportsResolution: true,  },  imageToVideo: {    enabled: true,    maxVideos: 1,    maxInputImages: 1,    maxInputImagesByModel: { "provider/reference-to-video": 9 },    maxDurationSeconds: 5,  },  videoToVideo: {    enabled: true,    maxVideos: 1,    maxInputVideos: 1,    maxDurationSeconds: 5,  },}
[/code]

`maxInputImages` और `maxInputVideos` जैसे flat aggregate fields transform-mode support विज्ञापित करने के लिए **पर्याप्त नहीं** हैं। Providers को `generate`, `imageToVideo`, और `videoToVideo` स्पष्ट रूप से declare करने चाहिए ताकि live tests, contract tests, और shared `video_generate` tool mode support को deterministically validate कर सकें।

जब किसी provider में एक model के पास बाकी की तुलना में wider reference-input support हो, तो mode-wide limit बढ़ाने के बजाय `maxInputImagesByModel`, `maxInputVideosByModel`, या `maxInputAudiosByModel` का उपयोग करें।

## Live tests

shared bundled providers के लिए opt-in live coverage:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/video-generation-providers.live.test.ts
[/code]

Repo wrapper:

bashCopy code
[code]
    pnpm test:live:media video
[/code]

यह live file default रूप से stored auth profiles से पहले already-exported provider env vars का उपयोग करती है, और default रूप से release-safe smoke चलाती है:

  * sweep में हर non-FAL provider के लिए `generate`.
  * एक-second lobster prompt.
  * प्रति-provider operation cap `OPENCLAW_LIVE_VIDEO_GENERATION_TIMEOUT_MS` से (`180000` default रूप से).


FAL opt-in है क्योंकि provider-side queue latency release time पर हावी हो सकती है:

bashCopy code
[code]
    pnpm test:live:media video --video-providers fal
[/code]

shared sweep जिन declared transform modes को local media के साथ सुरक्षित रूप से exercise कर सकता है, उन्हें भी चलाने के लिए `OPENCLAW_LIVE_VIDEO_GENERATION_FULL_MODES=1` set करें:

  * `capabilities.imageToVideo.enabled` होने पर `imageToVideo`.
  * `capabilities.videoToVideo.enabled` होने पर `videoToVideo` और जब provider/model shared sweep में buffer-backed local video input स्वीकार करता हो।


आज shared `videoToVideo` live lane `runway` को केवल तब cover करता है जब आप `runway/gen4_aleph` select करते हैं।

## Configuration

अपने OpenClaw config में default video-generation model set करें:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "qwen/wan2.6-t2v",        fallbacks: ["qwen/wan2.6-r2v-flash"],      },    },  },}
[/code]

या CLI के माध्यम से:

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "qwen/wan2.6-t2v"
[/code]

## संबंधित

  * [Alibaba Model Studio](</hi/providers/alibaba>)
  * [Background tasks](</hi/automation/tasks>) \- async video generation के लिए task tracking
  * [BytePlus](</hi/concepts/model-providers#byteplus-international>)
  * [ComfyUI](</hi/providers/comfy>)
  * [Configuration reference](</hi/gateway/config-agents#agent-defaults>)
  * [fal](</hi/providers/fal>)
  * [Google (Gemini)](</hi/providers/google>)
  * [MiniMax](</hi/providers/minimax>)
  * [Models](</hi/concepts/models>)
  * [OpenAI](</hi/providers/openai>)
  * [Qwen](</hi/providers/qwen>)
  * [Runway](</hi/providers/runway>)
  * [Together AI](</hi/providers/together>)
  * [Tools overview](</hi/tools>)
  * [Vydra](</hi/providers/vydra>)
  * [xAI](</hi/providers/xai>)


Was this useful?YesNo

Open issue