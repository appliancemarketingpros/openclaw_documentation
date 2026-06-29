---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/hi/providers/kilocode
scraped_at: 2026-06-29
---

ModelsProviders

Kilo Gateway एक ही endpoint और API key के पीछे कई मॉडलों तक अनुरोध रूट करने वाला एक **एकीकृत API** प्रदान करता है। यह OpenAI-संगत है, इसलिए अधिकांश OpenAI SDKs base URL बदलकर काम करते हैं।

प्रॉपर्टी | मान  
---|---  
प्रदाता | `kilocode`  
Auth | `KILOCODE_API_KEY`  
API | OpenAI-संगत  
Base URL | `https://api.kilo.ai/api/gateway/`  
  
## Plugin इंस्टॉल करें

आधिकारिक Plugin इंस्टॉल करें, फिर Gateway को फिर से शुरू करें:

bashCopy code
[code]
    openclaw plugins install @openclaw/kilocode-provideropenclaw gateway restart
[/code]

## शुरू करना

* ### Create an account

[app.kilo.ai](<https://app.kilo.ai>) पर जाएं, साइन इन करें या खाता बनाएं, फिर API Keys पर जाएं और नई key जनरेट करें।

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

या environment variable को सीधे सेट करें:

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## डिफ़ॉल्ट मॉडल

डिफ़ॉल्ट मॉडल `kilocode/kilo/auto` है, जो Kilo Gateway द्वारा प्रबंधित प्रदाता-स्वामित्व वाला smart-routing मॉडल है।

## अंतर्निहित कैटलॉग

OpenClaw startup पर Kilo Gateway से उपलब्ध मॉडलों को dynamic रूप से discover करता है। अपने खाते में उपलब्ध मॉडलों की पूरी सूची देखने के लिए `/models kilocode` का उपयोग करें।

Gateway पर उपलब्ध कोई भी मॉडल `kilocode/` prefix के साथ उपयोग किया जा सकता है:

मॉडल ref | नोट्स  
---|---  
`kilocode/kilo/auto` | डिफ़ॉल्ट — smart routing  
`kilocode/anthropic/claude-sonnet-4` | Kilo के माध्यम से Anthropic  
`kilocode/openai/gpt-5.5` | Kilo के माध्यम से OpenAI  
`kilocode/google/gemini-3.1-pro-preview` | Kilo के माध्यम से Google  
...और भी बहुत सारे | सभी सूचीबद्ध करने के लिए `/models kilocode` का उपयोग करें  
  
## कॉन्फ़िग उदाहरण

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

Transport and compatibility

Kilo Gateway को source में OpenRouter-संगत के रूप में documented किया गया है, इसलिए यह native OpenAI request shaping के बजाय proxy-style OpenAI-संगत path पर रहता है।

  * Gemini-backed Kilo refs proxy-Gemini path पर रहते हैं, इसलिए OpenClaw native Gemini replay validation या bootstrap rewrites सक्षम किए बिना वहां Gemini thought-signature sanitation बनाए रखता है।
  * Kilo Gateway आपके API key के साथ under the hood Bearer token का उपयोग करता है।

Stream wrapper and reasoning

Kilo का साझा stream wrapper provider app header जोड़ता है और समर्थित concrete model refs के लिए proxy reasoning payloads को normalize करता है।

Troubleshooting

  * यदि startup पर model discovery विफल हो जाती है, तो OpenClaw `kilocode/kilo/auto` वाले static catalog पर fallback करता है।
  * पुष्टि करें कि आपकी API key मान्य है और आपके Kilo खाते में वांछित मॉडल enabled हैं।
  * जब Gateway daemon के रूप में चलता है, तो सुनिश्चित करें कि `KILOCODE_API_KEY` उस process के लिए उपलब्ध है (उदाहरण के लिए `~/.openclaw/.env` में या `env.shellEnv` के माध्यम से)।


## संबंधित

[**Model selection** प्रदाताओं, model refs, और failover behavior को चुनना। ](</hi/concepts/model-providers>) [**Configuration reference** पूरा OpenClaw configuration reference। ](</hi/gateway/configuration-reference>) [**Kilo Gateway** Kilo Gateway dashboard, API keys, और account management। ](<https://app.kilo.ai>)

Was this useful?YesNo

Open issue