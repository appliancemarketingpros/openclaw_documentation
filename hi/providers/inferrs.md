---
title: अनुमान लगाता है
source_url: https://docs.openclaw.ai/hi/providers/inferrs
scraped_at: 2026-06-29
---

ModelsProviders

[inferrs](<https://github.com/ericcurtin/inferrs>) स्थानीय मॉडलों को OpenAI-संगत `/v1` API के पीछे सेवा दे सकता है। OpenClaw सामान्य `openai-completions` पथ के ज़रिए `inferrs` के साथ काम करता है।

गुण | मान  
---|---  
प्रदाता id | `inferrs` (कस्टम; `models.providers.inferrs` के अंतर्गत कॉन्फ़िगर करें)  
Plugin | कोई नहीं — `inferrs` बंडल किया गया OpenClaw प्रदाता Plugin नहीं है  
प्रमाणीकरण env var | वैकल्पिक। यदि आपके inferrs सर्वर में प्रमाणीकरण नहीं है, तो कोई भी मान काम करता है  
API | OpenAI-संगत (`openai-completions`)  
सुझाया गया आधार URL | `http://127.0.0.1:8080/v1` (या जहाँ भी आपका inferrs सर्वर चलता हो)  
  
## शुरू करना

* ### Start inferrs with a model

bashCopy code
[code]
    inferrs serve google/gemma-4-E2B-it \  --host 127.0.0.1 \  --port 8080 \  --device metal
[/code]

* ### Verify the server is reachable

bashCopy code
[code]
    curl http://127.0.0.1:8080/healthcurl http://127.0.0.1:8080/v1/models
[/code]

* ### Add an OpenClaw provider entry

स्पष्ट प्रदाता प्रविष्टि जोड़ें और अपने डिफ़ॉल्ट मॉडल को उस पर इंगित करें। नीचे पूरा कॉन्फ़िग उदाहरण देखें।

## पूरा कॉन्फ़िग उदाहरण

यह उदाहरण स्थानीय `inferrs` सर्वर पर Gemma 4 का उपयोग करता है।

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },      models: {        "inferrs/google/gemma-4-E2B-it": {          alias: "Gemma 4 (inferrs)",        },      },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

## माँग पर स्टार्टअप

जब कोई `inferrs/...` मॉडल चुना जाता है, तब ही Inferrs को OpenClaw द्वारा शुरू भी किया जा सकता है। उसी प्रदाता प्रविष्टि में `localService` जोड़ें:

json5Copy code
[code]
    {  models: {    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

`command` निरपेक्ष होना चाहिए। Gateway होस्ट पर `which inferrs` का उपयोग करें और उस पथ को कॉन्फ़िग में रखें। पूरे फ़ील्ड संदर्भ के लिए, [स्थानीय मॉडल सेवाएँ](</hi/gateway/local-model-services>) देखें।

## उन्नत कॉन्फ़िगरेशन

Why requiresStringContent matters

कुछ `inferrs` Chat Completions रूट केवल स्ट्रिंग `messages[].content` स्वीकार करते हैं, संरचित कंटेंट-पार्ट ऐरे नहीं।

json5Copy code
[code]
    compat: {  requiresStringContent: true}
[/code]

अनुरोध भेजने से पहले OpenClaw शुद्ध टेक्स्ट कंटेंट पार्ट्स को सादी स्ट्रिंग में समतल कर देगा।

Gemma and tool-schema caveat

कुछ मौजूदा `inferrs` \+ Gemma संयोजन छोटे सीधे `/v1/chat/completions` अनुरोध स्वीकार करते हैं, लेकिन पूरे OpenClaw एजेंट-रनटाइम टर्न पर फिर भी विफल हो जाते हैं।

यदि ऐसा होता है, तो पहले यह आज़माएँ:

json5Copy code
[code]
    compat: {  requiresStringContent: true,  supportsTools: false}
[/code]

यह मॉडल के लिए OpenClaw की टूल स्कीमा सतह को अक्षम करता है और कड़े स्थानीय बैकएंड पर प्रॉम्प्ट दबाव कम कर सकता है।

यदि छोटे सीधे अनुरोध फिर भी काम करते हैं लेकिन सामान्य OpenClaw एजेंट टर्न `inferrs` के अंदर क्रैश होते रहते हैं, तो बची हुई समस्या आमतौर पर OpenClaw की ट्रांसपोर्ट परत के बजाय अपस्ट्रीम मॉडल/सर्वर व्यवहार होती है।

Manual smoke test

कॉन्फ़िगर होने के बाद, दोनों परतों की जाँच करें:

bashCopy code
[code]
    curl http://127.0.0.1:8080/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"google/gemma-4-E2B-it","messages":[{"role":"user","content":"What is 2 + 2?"}],"stream":false}'
[/code]

bashCopy code
[code]
    openclaw infer model run \  --model inferrs/google/gemma-4-E2B-it \  --prompt "What is 2 + 2? Reply with one short sentence." \  --json
[/code]

यदि पहला कमांड काम करता है लेकिन दूसरा विफल होता है, तो नीचे समस्या-निवारण अनुभाग देखें।

Proxy-style behavior

`inferrs` को नेटिव OpenAI एंडपॉइंट के बजाय प्रॉक्सी-शैली OpenAI-संगत `/v1` बैकएंड माना जाता है।

  * नेटिव केवल-OpenAI अनुरोध आकारण यहाँ लागू नहीं होता
  * कोई `service_tier` नहीं, कोई Responses `store` नहीं, कोई प्रॉम्प्ट-कैश संकेत नहीं, और कोई OpenAI reasoning-compat पेलोड आकारण नहीं
  * छिपे हुए OpenClaw एट्रिब्यूशन हेडर (`originator`, `version`, `User-Agent`) कस्टम `inferrs` आधार URLs पर इंजेक्ट नहीं किए जाते


## समस्या-निवारण

curl /v1/models fails

`inferrs` नहीं चल रहा, पहुँच योग्य नहीं है, या अपेक्षित होस्ट/पोर्ट से बंधा नहीं है। सुनिश्चित करें कि सर्वर शुरू है और आपके कॉन्फ़िगर किए गए पते पर सुन रहा है।

messages[].content expected a string

मॉडल प्रविष्टि में `compat.requiresStringContent: true` सेट करें। विवरण के लिए ऊपर `requiresStringContent` अनुभाग देखें।

Direct /v1/chat/completions calls pass but openclaw infer model run fails

टूल स्कीमा सतह को अक्षम करने के लिए `compat.supportsTools: false` सेट करने का प्रयास करें। ऊपर Gemma टूल-स्कीमा चेतावनी देखें।

inferrs still crashes on larger agent turns

यदि OpenClaw को अब स्कीमा त्रुटियाँ नहीं मिलतीं, लेकिन `inferrs` बड़े एजेंट टर्न पर अब भी क्रैश होता है, तो इसे अपस्ट्रीम `inferrs` या मॉडल सीमा मानें। प्रॉम्प्ट दबाव घटाएँ या किसी अलग स्थानीय बैकएंड या मॉडल पर स्विच करें।

## संबंधित

[**Local models** स्थानीय मॉडल सर्वरों के विरुद्ध OpenClaw चलाना। ](</hi/gateway/local-models>) [**Local model services** कॉन्फ़िगर किए गए प्रदाताओं के लिए माँग पर स्थानीय मॉडल सर्वर शुरू करना। ](</hi/gateway/local-model-services>) [**Gateway troubleshooting** उन स्थानीय OpenAI-संगत बैकएंड को डीबग करना जो प्रोब पास करते हैं लेकिन एजेंट रन में विफल होते हैं। ](</hi/gateway/troubleshooting#local-openai-compatible-backend-passes-direct-probes-but-agent-runs-fail>) [**Model selection** सभी प्रदाताओं, मॉडल refs, और फ़ेलओवर व्यवहार का अवलोकन। ](</hi/concepts/model-providers>)

Was this useful?YesNo

Open issue