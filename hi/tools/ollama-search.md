---
title: Ollama वेब खोज
source_url: https://docs.openclaw.ai/hi/tools/ollama-search
scraped_at: 2026-06-29
---

CapabilitiesTools

OpenClaw बंडल किए गए `web_search` प्रदाता के रूप में **Ollama Web Search** का समर्थन करता है। यह Ollama की वेब-सर्च API का उपयोग करता है और शीर्षकों, URLs, और स्निपेट्स के साथ संरचित परिणाम लौटाता है।

स्थानीय या स्वयं-होस्ट किए गए Ollama के लिए, इस सेटअप को डिफ़ॉल्ट रूप से API key की आवश्यकता नहीं होती। इसके लिए ये आवश्यक हैं:

  * एक Ollama होस्ट जो OpenClaw से पहुंच योग्य हो
  * `ollama signin`


सीधे होस्टेड खोज के लिए, Ollama प्रदाता base URL को `https://ollama.com` पर सेट करें और वास्तविक `OLLAMA_API_KEY` प्रदान करें।

## सेटअप

* ### Ollama शुरू करें

सुनिश्चित करें कि Ollama इंस्टॉल और चल रहा है।

* ### साइन इन करें

चलाएँ:

bashCopy code
[code]
    ollama signin
[/code]

* ### Ollama Web Search चुनें

चलाएँ:

bashCopy code
[code]
    openclaw configure --section web
[/code]

फिर प्रदाता के रूप में **Ollama Web Search** चुनें।

यदि आप पहले से मॉडल्स के लिए Ollama का उपयोग करते हैं, तो Ollama Web Search उसी कॉन्फ़िगर किए गए होस्ट का पुनः उपयोग करता है।

## कॉन्फ़िग

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

वैकल्पिक Ollama होस्ट ओवरराइड:

json5Copy code
[code]
    {  plugins: {    entries: {      ollama: {        config: {          webSearch: {            baseUrl: "http://ollama-host:11434",          },        },      },    },  },}
[/code]

यदि आप Ollama को पहले से मॉडल प्रदाता के रूप में कॉन्फ़िगर करते हैं, तो वेब-सर्च प्रदाता इसके बजाय उस होस्ट का पुनः उपयोग कर सकता है:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434",      },    },  },}
[/code]

Ollama मॉडल प्रदाता canonical key के रूप में `baseUrl` का उपयोग करता है। वेब-सर्च प्रदाता OpenAI SDK-शैली कॉन्फ़िग उदाहरणों के साथ compatibility के लिए `models.providers.ollama` पर `baseURL` का भी सम्मान करता है।

यदि कोई स्पष्ट Ollama base URL सेट नहीं है, तो OpenClaw `http://127.0.0.1:11434` का उपयोग करता है।

यदि आपके Ollama होस्ट को bearer auth अपेक्षित है, तो OpenClaw उस कॉन्फ़िगर किए गए होस्ट को अनुरोधों के लिए `models.providers.ollama.apiKey` (या मिलते-जुलते env-समर्थित प्रदाता auth) का पुनः उपयोग करता है।

सीधा होस्टेड Ollama Web Search:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",      },    },  },  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

## नोट्स

  * इस प्रदाता के लिए कोई वेब-सर्च-विशिष्ट API key फ़ील्ड आवश्यक नहीं है।
  * यदि Ollama होस्ट auth-संरक्षित है, तो OpenClaw मौजूद होने पर सामान्य Ollama प्रदाता API key का पुनः उपयोग करता है।
  * यदि `baseUrl` `https://ollama.com` है, तो OpenClaw सीधे `https://ollama.com/api/web_search` को कॉल करता है और कॉन्फ़िगर की गई Ollama API key को bearer auth के रूप में भेजता है।
  * यदि कॉन्फ़िगर किया गया होस्ट web search उपलब्ध नहीं कराता और `OLLAMA_API_KEY` सेट है, तो OpenClaw उस env key को स्थानीय होस्ट को भेजे बिना `https://ollama.com/api/web_search` पर वापस जा सकता है।
  * यदि Ollama पहुंच योग्य नहीं है या साइन इन नहीं है, तो OpenClaw सेटअप के दौरान चेतावनी देता है, लेकिन चयन को अवरुद्ध नहीं करता।
  * जब कोई उच्च-प्राथमिकता वाला credentialed प्रदाता कॉन्फ़िगर नहीं है, तो OpenClaw Ollama Web Search को स्वतः-चयनित नहीं करता; इसे `tools.web.search.provider: "ollama"` के साथ स्पष्ट रूप से चुनें।
  * स्थानीय Ollama daemon होस्ट स्थानीय proxy endpoint `/api/experimental/web_search` का उपयोग करते हैं, जो साइन करके Ollama Cloud को फ़ॉरवर्ड करता है।
  * `https://ollama.com` होस्ट public hosted endpoint `/api/web_search` का उपयोग सीधे bearer API-key auth के साथ करते हैं।


## संबंधित

  * [Web Search अवलोकन](</hi/tools/web>) \-- सभी प्रदाता और auto-detection
  * [Ollama](</hi/providers/ollama>) \-- Ollama मॉडल सेटअप और cloud/local मोड


Was this useful?YesNo

Open issue