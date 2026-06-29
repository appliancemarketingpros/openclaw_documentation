---
title: Arcee AI
source_url: https://docs.openclaw.ai/hi/providers/arcee
scraped_at: 2026-06-29
---

ModelsProviders

[Arcee AI](<https://arcee.ai>) OpenAI-संगत API के माध्यम से मिश्रित-विशेषज्ञ मॉडलों के Trinity परिवार तक पहुँच प्रदान करता है। सभी Trinity मॉडल Apache 2.0 लाइसेंस प्राप्त हैं।

Arcee AI मॉडलों तक सीधे Arcee प्लेटफ़ॉर्म के माध्यम से या [OpenRouter](</hi/providers/openrouter>) के ज़रिए पहुँचा जा सकता है।

गुण | मान  
---|---  
प्रदाता | `arcee`  
प्रमाणीकरण | `ARCEEAI_API_KEY` (सीधा) या `OPENROUTER_API_KEY` (OpenRouter के ज़रिए)  
API | OpenAI-संगत  
आधार URL | `https://api.arcee.ai/api/v1` (सीधा) या `https://openrouter.ai/api/v1` (OpenRouter)  
  
## Plugin इंस्टॉल करें

आधिकारिक Plugin इंस्टॉल करें, फिर Gateway पुनः प्रारंभ करें:

bashCopy code
[code]
    openclaw plugins install @openclaw/arcee-provideropenclaw gateway restart
[/code]

## शुरू करना

### सीधा (Arcee प्लेटफ़ॉर्म)

* ### API कुंजी प्राप्त करें

[Arcee AI](<https://chat.arcee.ai/>) पर एक API कुंजी बनाएँ।

* ### ऑनबोर्डिंग चलाएँ

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### डिफ़ॉल्ट मॉडल सेट करें

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### OpenRouter के ज़रिए

* ### API कुंजी प्राप्त करें

[OpenRouter](<https://openrouter.ai/keys>) पर एक API कुंजी बनाएँ।

* ### ऑनबोर्डिंग चलाएँ

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### डिफ़ॉल्ट मॉडल सेट करें

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

वही मॉडल रेफ़रेंस सीधे और OpenRouter, दोनों सेटअप के लिए काम करते हैं (उदाहरण के लिए `arcee/trinity-large-thinking`)।

## गैर-इंटरैक्टिव सेटअप

### सीधा (Arcee प्लेटफ़ॉर्म)

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### OpenRouter के ज़रिए

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## अंतर्निहित कैटलॉग

OpenClaw अभी यह Arcee स्थैतिक कैटलॉग शिप करता है:

मॉडल रेफ़रेंस | नाम | इनपुट | संदर्भ | लागत (प्रति 1M अंदर/बाहर) | नोट्स  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | text | 256K | $0.25 / $0.90 | डिफ़ॉल्ट मॉडल; रीजनिंग सक्षम  
`arcee/trinity-large-preview` | Trinity Large Preview | text | 128K | $0.25 / $1.00 | सामान्य-उद्देश्य; 400B पैरामीटर, 13B सक्रिय  
`arcee/trinity-mini` | Trinity Mini 26B | text | 128K | $0.045 / $0.15 | तेज़ और लागत-किफ़ायती; फ़ंक्शन कॉलिंग  
  
## समर्थित सुविधाएँ

सुविधा | समर्थित  
---|---  
स्ट्रीमिंग | हाँ  
टूल उपयोग / फ़ंक्शन कॉलिंग | हाँ (Trinity Mini, Trinity Large Preview)  
संरचित आउटपुट (JSON मोड और JSON स्कीमा) | हाँ  
विस्तारित सोच | हाँ (Trinity Large Thinking; टूल अक्षम)  
  
पर्यावरण नोट

यदि Gateway डेमन (launchd/systemd) के रूप में चलता है, तो सुनिश्चित करें कि `ARCEEAI_API_KEY` (या `OPENROUTER_API_KEY`) उस प्रक्रिया के लिए उपलब्ध है (उदाहरण के लिए, `~/.openclaw/.env` में या `env.shellEnv` के माध्यम से)।

OpenRouter रूटिंग

OpenRouter के माध्यम से Arcee मॉडल इस्तेमाल करते समय, वही `arcee/*` मॉडल रेफ़रेंस लागू होते हैं। OpenClaw आपके प्रमाणीकरण विकल्प के आधार पर रूटिंग को पारदर्शी रूप से संभालता है। OpenRouter-विशिष्ट कॉन्फ़िगरेशन विवरणों के लिए [OpenRouter provider दस्तावेज़](</hi/providers/openrouter>) देखें।

## संबंधित

[**OpenRouter** एक ही API कुंजी के माध्यम से Arcee मॉडल और कई अन्य तक पहुँचें। ](</hi/providers/openrouter>) [**मॉडल चयन** प्रदाताओं, मॉडल रेफ़रेंस और फ़ेलओवर व्यवहार को चुनना। ](</hi/concepts/model-providers>)

Was this useful?YesNo

Open issue