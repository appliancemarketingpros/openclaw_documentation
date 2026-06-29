---
title: llama.cpp प्रदाता
source_url: https://docs.openclaw.ai/hi/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp` स्थानीय GGUF एम्बेडिंग्स के लिए आधिकारिक बाहरी प्रदाता Plugin है। यह `memorySearch.provider: "local"` द्वारा उपयोग की जाने वाली `node-llama-cpp` रनटाइम निर्भरता का स्वामी है।

स्थानीय मेमोरी एम्बेडिंग्स का उपयोग करने से पहले इसे इंस्टॉल करें:

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

मुख्य `openclaw` npm पैकेज में `node-llama-cpp` शामिल नहीं है। नेटिव निर्भरता को इस Plugin में रखने से सामान्य OpenClaw npm अपडेट OpenClaw पैकेज डायरेक्टरी के भीतर मैन्युअल रूप से इंस्टॉल किए गए रनटाइम को हटाने से बचते हैं।

## कॉन्फ़िगरेशन

मेमोरी खोज प्रदाता को `local` पर सेट करें:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

डिफ़ॉल्ट मॉडल `embeddinggemma-300m-qat-Q8_0.gguf` है। आप `local.modelPath` को किसी स्थानीय `.gguf` फ़ाइल की ओर भी इंगित कर सकते हैं।

## नेटिव रनटाइम

सबसे सहज नेटिव इंस्टॉल पथ के लिए Node 24 का उपयोग करें। pnpm का उपयोग करने वाले सोर्स चेकआउट को नेटिव निर्भरता को स्वीकृत और फिर से बिल्ड करने की आवश्यकता हो सकती है:

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

कम झंझट वाली स्थानीय एम्बेडिंग्स के लिए, इसके बजाय Ollama या LM Studio जैसे स्थानीय सेवा प्रदाता का उपयोग करें।

Was this useful?YesNo

Open issue