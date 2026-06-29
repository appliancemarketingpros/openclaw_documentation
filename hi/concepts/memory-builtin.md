---
title: अंतर्निहित मेमोरी इंजन
source_url: https://docs.openclaw.ai/hi/concepts/memory-builtin
scraped_at: 2026-06-29
---

AgentsSessions and memory

अंतर्निर्मित इंजन डिफ़ॉल्ट मेमोरी बैकएंड है। यह आपकी मेमोरी इंडेक्स को प्रति-एजेंट SQLite डेटाबेस में संग्रहीत करता है और शुरू करने के लिए किसी अतिरिक्त निर्भरता की आवश्यकता नहीं होती।

## यह क्या प्रदान करता है

  * FTS5 फुल-टेक्स्ट इंडेक्सिंग (BM25 स्कोरिंग) के जरिए **कीवर्ड खोज** ।
  * किसी भी समर्थित प्रदाता से embeddings के जरिए **वेक्टर खोज** ।
  * **हाइब्रिड खोज** , जो सर्वोत्तम परिणामों के लिए दोनों को जोड़ती है।
  * चीनी, जापानी और कोरियाई के लिए ट्राइग्राम टोकनाइज़ेशन के जरिए **CJK समर्थन** ।
  * इन-डेटाबेस वेक्टर क्वेरी के लिए **sqlite-vec त्वरण** (वैकल्पिक)।


## शुरुआत करना

डिफ़ॉल्ट रूप से, अंतर्निर्मित इंजन OpenAI embeddings का उपयोग करता है। यदि आपने पहले से `OPENAI_API_KEY` या `models.providers.openai.apiKey` कॉन्फ़िगर किया है, तो वेक्टर खोज बिना अतिरिक्त मेमोरी कॉन्फ़िगरेशन के काम करती है।

किसी प्रदाता को स्पष्ट रूप से सेट करने के लिए:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",      },    },  },}
[/code]

embedding प्रदाता के बिना, केवल कीवर्ड खोज उपलब्ध होती है।

स्थानीय GGUF embeddings को बाध्य करने के लिए, आधिकारिक llama.cpp प्रदाता Plugin इंस्टॉल करें, फिर `local.modelPath` को किसी GGUF फ़ाइल की ओर इंगित करें:

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        fallback: "none",        local: {          modelPath: "~/.node-llama-cpp/models/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

## समर्थित embedding प्रदाता

प्रदाता | ID | नोट्स  
---|---|---  
Bedrock | `bedrock` | AWS क्रेडेंशियल चेन का उपयोग करता है  
DeepInfra | `deepinfra` | डिफ़ॉल्ट: `BAAI/bge-m3`  
Gemini | `gemini` | मल्टीमॉडल (इमेज + ऑडियो) का समर्थन करता है  
GitHub Copilot | `github-copilot` | Copilot सदस्यता का उपयोग करता है  
Local | `local` | `@openclaw/llama-cpp-provider`  
Mistral | `mistral` |   
Ollama | `ollama` | स्थानीय/स्व-होस्टेड  
OpenAI | `openai` | डिफ़ॉल्ट: `text-embedding-3-small`  
OpenAI-संगत | `openai-compatible` | सामान्य `/v1/embeddings` endpoint  
Voyage | `voyage` |   
  
OpenAI से अलग जाने के लिए `memorySearch.provider` सेट करें।

## इंडेक्सिंग कैसे काम करती है

OpenClaw `MEMORY.md` और `memory/*.md` को खंडों (~400 टोकन, जिनमें 80-टोकन ओवरलैप होता है) में इंडेक्स करता है और उन्हें प्रति-एजेंट SQLite डेटाबेस में संग्रहीत करता है।

  * **इंडेक्स स्थान:** स्वामी एजेंट डेटाबेस `~/.openclaw/agents/<agentId>/agent/openclaw-agent.sqlite`
  * **स्टोरेज रखरखाव:** SQLite WAL sidecars को आवधिक और शटडाउन checkpoints के साथ सीमित रखा जाता है।
  * **फ़ाइल वॉचिंग:** मेमोरी फ़ाइलों में बदलाव debounced reindex (1.5s) को ट्रिगर करते हैं।
  * **स्वचालित रीइंडेक्स:** जब embedding प्रदाता, मॉडल, या chunking कॉन्फ़िगरेशन बदलता है, तो पूरा इंडेक्स अपने आप फिर से बनाया जाता है।
  * **मांग पर रीइंडेक्स:** `openclaw memory index --force`


## कब उपयोग करें

अंतर्निर्मित इंजन अधिकांश उपयोगकर्ताओं के लिए सही विकल्प है:

  * बिना अतिरिक्त निर्भरता के तुरंत काम करता है।
  * कीवर्ड और वेक्टर खोज को अच्छी तरह संभालता है।
  * सभी embedding प्रदाताओं का समर्थन करता है।
  * हाइब्रिड खोज दोनों retrieval तरीकों की सर्वोत्तम खूबियों को जोड़ती है।


यदि आपको reranking, query expansion की आवश्यकता है, या workspace के बाहर directories को इंडेक्स करना चाहते हैं, तो [QMD](</hi/concepts/memory-qmd>) पर स्विच करने पर विचार करें।

यदि आप स्वचालित user modeling के साथ cross-session मेमोरी चाहते हैं, तो [Honcho](</hi/concepts/memory-honcho>) पर विचार करें।

## समस्या निवारण

**मेमोरी खोज अक्षम है?** `openclaw memory status` जांचें। यदि कोई प्रदाता पता नहीं चलता, तो एक को स्पष्ट रूप से सेट करें या API key जोड़ें।

**स्थानीय प्रदाता पता नहीं चला?** पुष्टि करें कि स्थानीय path मौजूद है और चलाएं:

bashCopy code
[code]
    openclaw memory status --deep --agent mainopenclaw memory index --force --agent main
[/code]

Standalone CLI commands और Gateway दोनों समान `local` प्रदाता id का उपयोग करते हैं। जब आप स्थानीय embeddings चाहते हैं, तो `memorySearch.provider: "local"` सेट करें।

**पुराने परिणाम?** फिर से बनाने के लिए `openclaw memory index --force` चलाएं। watcher दुर्लभ edge cases में बदलावों को चूक सकता है।

**sqlite-vec लोड नहीं हो रहा?** OpenClaw अपने आप in-process cosine similarity पर fallback करता है। `openclaw memory status --deep` स्थानीय वेक्टर store को embedding प्रदाता से अलग रिपोर्ट करता है, इसलिए `Vector store: unavailable` sqlite-vec loading की ओर संकेत करता है, जबकि `Embeddings: unavailable` प्रदाता/auth या मॉडल readiness की ओर संकेत करता है। विशिष्ट load error के लिए logs जांचें।

## कॉन्फ़िगरेशन

embedding प्रदाता setup, हाइब्रिड खोज tuning (weights, MMR, temporal decay), batch indexing, multimodal memory, sqlite-vec, extra paths, और अन्य सभी config knobs के लिए [मेमोरी कॉन्फ़िगरेशन संदर्भ](</hi/reference/memory-config>) देखें।

## संबंधित

  * [मेमोरी अवलोकन](</hi/concepts/memory>)
  * [मेमोरी खोज](</hi/concepts/memory-search>)
  * [Active Memory](</hi/concepts/active-memory>)


Was this useful?YesNo

Open issue