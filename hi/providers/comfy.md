---
title: ComfyUI
source_url: https://docs.openclaw.ai/hi/providers/comfy
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw कार्यप्रवाह-चालित ComfyUI रन के लिए एक बंडल किया गया `comfy` Plugin भेजता है। Plugin पूरी तरह कार्यप्रवाह-चालित है, इसलिए OpenClaw आपके ग्राफ पर सामान्य `size`, `aspectRatio`, `resolution`, `durationSeconds`, या TTS-शैली नियंत्रणों को मैप करने की कोशिश नहीं करता।

गुण | विवरण  
---|---  
प्रदाता | `comfy`  
मॉडल | `comfy/workflow`  
साझा सतहें | `image_generate`, `video_generate`, `music_generate`  
प्रमाणीकरण | स्थानीय ComfyUI के लिए कोई नहीं; Comfy Cloud के लिए `COMFY_API_KEY` या `COMFY_CLOUD_API_KEY`  
API | ComfyUI `/prompt` / `/history` / `/view` और Comfy Cloud `/api/*`  
  
## यह क्या समर्थित करता है

  * कार्यप्रवाह JSON से इमेज जनरेशन
  * 1 अपलोड की गई संदर्भ इमेज के साथ इमेज संपादन
  * कार्यप्रवाह JSON से वीडियो जनरेशन
  * 1 अपलोड की गई संदर्भ इमेज के साथ वीडियो जनरेशन
  * साझा `music_generate` टूल के माध्यम से संगीत या ऑडियो जनरेशन
  * कॉन्फ़िगर किए गए नोड या सभी मेल खाते आउटपुट नोड से आउटपुट डाउनलोड


## शुरू करना

अपनी मशीन पर ComfyUI चलाने या Comfy Cloud का उपयोग करने में से चुनें।

### Local

**इसके लिए सबसे अच्छा:** अपनी मशीन या LAN पर अपना ComfyUI इंस्टेंस चलाना।

* ### Start ComfyUI locally

पक्का करें कि आपका स्थानीय ComfyUI इंस्टेंस चल रहा है (डिफ़ॉल्ट `http://127.0.0.1:8188`)।

* ### Prepare your workflow JSON

ComfyUI कार्यप्रवाह JSON फ़ाइल निर्यात करें या बनाएँ। prompt इनपुट नोड और उस आउटपुट नोड की नोड ID नोट करें जिससे आप OpenClaw को पढ़ाना चाहते हैं।

* ### Configure the provider

`mode: "local"` सेट करें और अपनी कार्यप्रवाह फ़ाइल की ओर संकेत करें। यहाँ एक न्यूनतम इमेज उदाहरण है:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Set the default model

आपके द्वारा कॉन्फ़िगर की गई क्षमता के लिए OpenClaw को `comfy/workflow` मॉडल पर निर्देशित करें:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Verify

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

### Comfy Cloud

**इसके लिए सबसे अच्छा:** स्थानीय GPU संसाधनों को प्रबंधित किए बिना Comfy Cloud पर कार्यप्रवाह चलाना।

* ### Get an API key

[comfy.org](<https://comfy.org>) पर साइन अप करें और अपने खाता डैशबोर्ड से API कुंजी जनरेट करें।

* ### Set the API key

इनमें से किसी एक विधि से अपनी कुंजी दें:

bashCopy code
[code]
    # Environment variable (preferred)export COMFY_API_KEY="your-key" # Alternative environment variableexport COMFY_CLOUD_API_KEY="your-key" # Or inline in configopenclaw config set plugins.entries.comfy.config.apiKey "your-key"
[/code]

* ### Prepare your workflow JSON

ComfyUI कार्यप्रवाह JSON फ़ाइल निर्यात करें या बनाएँ। prompt इनपुट नोड और आउटपुट नोड की नोड ID नोट करें।

* ### Configure the provider

`mode: "cloud"` सेट करें और अपनी कार्यप्रवाह फ़ाइल की ओर संकेत करें:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "cloud",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Set the default model

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Verify

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

## कॉन्फ़िगरेशन

Comfy साझा शीर्ष-स्तरीय कनेक्शन सेटिंग्स के साथ प्रति-क्षमता कार्यप्रवाह सेक्शन (`image`, `video`, `music`) का समर्थन करता है:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },          video: {            workflowPath: "./workflows/video-api.json",            promptNodeId: "12",            outputNodeId: "21",          },          music: {            workflowPath: "./workflows/music-api.json",            promptNodeId: "3",            outputNodeId: "18",          },        },      },    },  },}
[/code]

### साझा कुंजियाँ

कुंजी | प्रकार | विवरण  
---|---|---  
`mode` | `"local"` या `"cloud"` | कनेक्शन मोड।  
`baseUrl` | string | स्थानीय के लिए डिफ़ॉल्ट `http://127.0.0.1:8188` या cloud के लिए `https://cloud.comfy.org`।  
`apiKey` | string | वैकल्पिक inline कुंजी, `COMFY_API_KEY` / `COMFY_CLOUD_API_KEY` env vars का विकल्प।  
`allowPrivateNetwork` | boolean | cloud मोड में private/LAN `baseUrl` की अनुमति दें।  
  
### प्रति-क्षमता कुंजियाँ

ये कुंजियाँ `image`, `video`, या `music` सेक्शन के अंदर लागू होती हैं:

कुंजी | आवश्यक | डिफ़ॉल्ट | विवरण  
---|---|---|---  
`workflow` या `workflowPath` | हाँ | \-- | ComfyUI कार्यप्रवाह JSON फ़ाइल का पथ।  
`promptNodeId` | हाँ | \-- | वह नोड ID जो टेक्स्ट prompt प्राप्त करती है।  
`promptInputName` | नहीं | `"text"` | prompt नोड पर इनपुट नाम।  
`outputNodeId` | नहीं | \-- | आउटपुट पढ़ने के लिए नोड ID। छोड़े जाने पर, सभी मेल खाते आउटपुट नोड उपयोग किए जाते हैं।  
`pollIntervalMs` | नहीं | \-- | जॉब पूर्णता के लिए milliseconds में polling अंतराल।  
`timeoutMs` | नहीं | \-- | कार्यप्रवाह रन के लिए milliseconds में timeout।  
  
`image` और `video` सेक्शन इसका भी समर्थन करते हैं:

कुंजी | आवश्यक | डिफ़ॉल्ट | विवरण  
---|---|---|---  
`inputImageNodeId` | हाँ (संदर्भ इमेज पास करते समय) | \-- | वह नोड ID जो अपलोड की गई संदर्भ इमेज प्राप्त करती है।  
`inputImageInputName` | नहीं | `"image"` | इमेज नोड पर इनपुट नाम।  
  
## कार्यप्रवाह विवरण

Image workflows

डिफ़ॉल्ट इमेज मॉडल को `comfy/workflow` पर सेट करें:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

**संदर्भ-इमेज संपादन उदाहरण:**

अपलोड की गई संदर्भ इमेज के साथ इमेज संपादन सक्षम करने के लिए, अपने इमेज config में `inputImageNodeId` जोड़ें:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          image: {            workflowPath: "./workflows/edit-api.json",            promptNodeId: "6",            inputImageNodeId: "7",            inputImageInputName: "image",            outputNodeId: "9",          },        },      },    },  },}
[/code]

Video workflows

डिफ़ॉल्ट वीडियो मॉडल को `comfy/workflow` पर सेट करें:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

Comfy वीडियो कार्यप्रवाह कॉन्फ़िगर किए गए ग्राफ के माध्यम से text-to-video और image-to-video का समर्थन करते हैं।

Music workflows

बंडल किया गया Plugin कार्यप्रवाह-परिभाषित ऑडियो या संगीत आउटपुट के लिए music-generation प्रदाता पंजीकृत करता है, जो साझा `music_generate` टूल के माध्यम से प्रस्तुत होता है:

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

अपने ऑडियो कार्यप्रवाह JSON और आउटपुट नोड की ओर संकेत करने के लिए `music` config सेक्शन का उपयोग करें।

Backward compatibility

मौजूदा शीर्ष-स्तरीय इमेज config (nested `image` सेक्शन के बिना) अब भी काम करता है:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          workflowPath: "./workflows/flux-api.json",          promptNodeId: "6",          outputNodeId: "9",        },      },    },  },}
[/code]

OpenClaw उस legacy shape को इमेज कार्यप्रवाह config के रूप में मानता है। आपको तुरंत migrate करने की आवश्यकता नहीं है, लेकिन नए setups के लिए nested `image` / `video` / `music` सेक्शन अनुशंसित हैं।

Live tests

बंडल किए गए Plugin के लिए opt-in live coverage उपलब्ध है:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

जब तक मेल खाता Comfy कार्यप्रवाह सेक्शन कॉन्फ़िगर नहीं होता, live test अलग-अलग इमेज, वीडियो, या संगीत मामलों को छोड़ देता है।

## संबंधित

[**छवि जनरेशन** छवि जनरेशन टूल का कॉन्फ़िगरेशन और उपयोग। ](</hi/tools/image-generation>) [**वीडियो जनरेशन** वीडियो जनरेशन टूल का कॉन्फ़िगरेशन और उपयोग। ](</hi/tools/video-generation>) [**संगीत जनरेशन** संगीत और ऑडियो जनरेशन टूल का सेटअप। ](</hi/tools/music-generation>) [**प्रदाता निर्देशिका** सभी प्रदाताओं और मॉडल refs का अवलोकन। ](</hi/providers>) [**कॉन्फ़िगरेशन संदर्भ** एजेंट डिफ़ॉल्ट सहित पूरा कॉन्फ़िग संदर्भ। ](</hi/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue