---
title: Tencent Cloud (TokenHub)
source_url: https://docs.openclaw.ai/hi/providers/tencent
scraped_at: 2026-06-29
---

ModelsProviders

OpenAI-संगत API का उपयोग करके TokenHub endpoint (`tencent-tokenhub`) के माध्यम से Tencent Hy3 preview तक पहुंचने के लिए आधिकारिक Tencent Cloud प्रदाता Plugin इंस्टॉल करें।

प्रॉपर्टी | मान  
---|---  
प्रदाता id | `tencent-tokenhub`  
पैकेज | `@openclaw/tencent-provider`  
Auth env var | `TOKENHUB_API_KEY`  
Onboarding flag | `--auth-choice tokenhub-api-key`  
Direct CLI flag | `--tokenhub-api-key <key>`  
API | OpenAI-संगत (`openai-completions`)  
डिफ़ॉल्ट base URL | `https://tokenhub.tencentmaas.com/v1`  
वैश्विक base URL | `https://tokenhub-intl.tencentmaas.com/v1` (override)  
डिफ़ॉल्ट मॉडल | `tencent-tokenhub/hy3-preview`  
  
## त्वरित शुरुआत

* ### Install the plugin

bashCopy code
[code]
    openclaw plugins install @openclaw/tencent-provider
[/code]

* ### Create a TokenHub API key

Tencent Cloud TokenHub में API key बनाएं। यदि आप key के लिए सीमित access scope चुनते हैं, तो अनुमत मॉडलों में **Hy3 preview** शामिल करें।

* ### Run onboarding

OnboardingCopy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

Env onlyCopy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### Verify the model

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## Non-interactive सेटअप

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## अंतर्निहित कैटलॉग

मॉडल ref | नाम | इनपुट | Context | अधिकतम आउटपुट | नोट्स  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | Hy3 preview (TokenHub) | पाठ | 256,000 | 64,000 | डिफ़ॉल्ट; reasoning-सक्षम  
  
Hy3 preview, Tencent Hunyuan का बड़ा MoE भाषा मॉडल है, जो reasoning, long-context निर्देशों का पालन, code, और agent workflows के लिए है। Tencent के OpenAI-संगत उदाहरण model id के रूप में `hy3-preview` का उपयोग करते हैं और मानक chat-completions tool calling के साथ `reasoning_effort` का समर्थन करते हैं।

## स्तरीकृत मूल्य निर्धारण

प्रदाता कैटलॉग स्तरीकृत लागत metadata के साथ आता है, जो input window length के अनुसार scale होता है, इसलिए लागत अनुमान manual overrides के बिना भर दिए जाते हैं।

Input tokens range | Input rate | Output rate | Cache read  
---|---|---|---  
0 - 16,000 | 0.176 | 0.587 | 0.059  
16,000 - 32,000 | 0.235 | 0.939 | 0.088  
32,000+ | 0.293 | 1.173 | 0.117  
  
दरें Tencent द्वारा विज्ञापित USD में प्रति मिलियन tokens हैं। केवल तभी `models.providers.tencent-tokenhub` के अंतर्गत pricing override करें जब आपको अलग surface की आवश्यकता हो।

## उन्नत कॉन्फ़िगरेशन

Endpoint override

OpenClaw डिफ़ॉल्ट रूप से Tencent Cloud के `https://tokenhub.tencentmaas.com/v1` endpoint का उपयोग करता है। Tencent एक अंतरराष्ट्रीय TokenHub endpoint भी दस्तावेज़ित करता है:

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

endpoint को केवल तभी override करें जब आपके TokenHub खाते या क्षेत्र को इसकी आवश्यकता हो।

Environment availability for the daemon

यदि Gateway managed service (launchd, systemd, Docker) के रूप में चलता है, तो `TOKENHUB_API_KEY` उस process को visible होना चाहिए। इसे `~/.openclaw/.env` में या `env.shellEnv` के माध्यम से सेट करें ताकि launchd, systemd, या Docker exec environments इसे पढ़ सकें।

## संबंधित

[**Model providers** प्रदाताओं, model refs, और failover behavior को चुनना। ](</hi/concepts/model-providers>) [**Configuration reference** प्रदाता settings सहित पूर्ण config schema। ](</hi/gateway/configuration>) [**Tencent TokenHub** Tencent Cloud का TokenHub product page। ](<https://cloud.tencent.com/product/tokenhub>) [**Hy3 preview model card** Tencent Hunyuan Hy3 preview details और benchmarks। ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo

Open issue