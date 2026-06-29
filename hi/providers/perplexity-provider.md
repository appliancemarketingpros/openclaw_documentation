---
title: Perplexity
source_url: https://docs.openclaw.ai/hi/providers/perplexity-provider
scraped_at: 2026-06-29
---

ModelsProviders

Perplexity Plugin, Perplexity Search API या OpenRouter के माध्यम से Perplexity Sonar के जरिए वेब खोज क्षमताएं प्रदान करता है।

गुण | मान  
---|---  
प्रकार | वेब खोज प्रदाता (मॉडल प्रदाता नहीं)  
प्रमाणीकरण | `PERPLEXITY_API_KEY` (सीधा) या `OPENROUTER_API_KEY` (OpenRouter के जरिए)  
कॉन्फ़िग पथ | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## Plugin इंस्टॉल करें

आधिकारिक Plugin इंस्टॉल करें, फिर Gateway फिर से शुरू करें:

bashCopy code
[code]
    openclaw plugins install @openclaw/perplexity-pluginopenclaw gateway restart
[/code]

## शुरू करना

* ### API कुंजी सेट करें

इंटरैक्टिव वेब-खोज कॉन्फ़िगरेशन फ़्लो चलाएं:

bashCopy code
[code]
    openclaw configure --section web
[/code]

या कुंजी सीधे सेट करें:

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### खोज शुरू करें

कुंजी कॉन्फ़िगर हो जाने के बाद एजेंट वेब खोजों के लिए अपने-आप Perplexity का उपयोग करेगा। कोई अतिरिक्त चरण आवश्यक नहीं हैं।

## खोज मोड

Plugin API कुंजी प्रीफ़िक्स के आधार पर ट्रांसपोर्ट अपने-आप चुनता है:

### नेटिव Perplexity API (pplx-)

जब आपकी कुंजी `pplx-` से शुरू होती है, OpenClaw नेटिव Perplexity Search API का उपयोग करता है। यह ट्रांसपोर्ट संरचित परिणाम लौटाता है और डोमेन, भाषा, और तारीख फ़िल्टर का समर्थन करता है (नीचे फ़िल्टरिंग विकल्प देखें)।

### OpenRouter / Sonar (sk-or-)

जब आपकी कुंजी `sk-or-` से शुरू होती है, OpenClaw Perplexity Sonar मॉडल का उपयोग करके OpenRouter के जरिए रूट करता है। यह ट्रांसपोर्ट उद्धरणों के साथ AI-संश्लेषित उत्तर लौटाता है।

कुंजी प्रीफ़िक्स | ट्रांसपोर्ट | सुविधाएं  
---|---|---  
`pplx-` | नेटिव Perplexity Search API | संरचित परिणाम, डोमेन/भाषा/तारीख फ़िल्टर  
`sk-or-` | OpenRouter (Sonar) | उद्धरणों के साथ AI-संश्लेषित उत्तर  
  
## नेटिव API फ़िल्टरिंग

नेटिव Perplexity API का उपयोग करते समय, खोजें निम्नलिखित फ़िल्टर का समर्थन करती हैं:

फ़िल्टर | विवरण | उदाहरण  
---|---|---  
देश | 2-अक्षरी देश कोड | `us`, `de`, `jp`  
भाषा | ISO 639-1 भाषा कोड | `en`, `fr`, `zh`  
तारीख सीमा | हालियापन विंडो | `day`, `week`, `month`, `year`  
डोमेन फ़िल्टर | अनुमति-सूची या निषेध-सूची (अधिकतम 20 डोमेन) | `example.com`  
सामग्री बजट | प्रति उत्तर / प्रति पेज टोकन सीमाएं | `max_tokens`, `max_tokens_per_page`  
  
## उन्नत कॉन्फ़िगरेशन

डेमन प्रक्रियाओं के लिए पर्यावरण चर

यदि OpenClaw Gateway डेमन (launchd/systemd) के रूप में चलता है, तो सुनिश्चित करें कि `PERPLEXITY_API_KEY` उस प्रक्रिया के लिए उपलब्ध है।

OpenRouter प्रॉक्सी सेटअप

यदि आप Perplexity खोजों को OpenRouter के जरिए रूट करना पसंद करते हैं, तो नेटिव Perplexity कुंजी के बजाय `OPENROUTER_API_KEY` (प्रीफ़िक्स `sk-or-`) सेट करें। OpenClaw प्रीफ़िक्स का पता लगाएगा और अपने-आप Sonar ट्रांसपोर्ट पर स्विच कर देगा।

## संबंधित

[**Perplexity खोज टूल** एजेंट Perplexity खोजों को कैसे आह्वान करता है और परिणामों की व्याख्या कैसे करता है। ](</hi/tools/perplexity-search>) [**कॉन्फ़िगरेशन संदर्भ** Plugin प्रविष्टियों सहित पूरा कॉन्फ़िगरेशन संदर्भ। ](</hi/gateway/configuration-reference>)

Was this useful?YesNo

Open issue