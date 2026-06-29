---
title: Chutes
source_url: https://docs.openclaw.ai/hi/providers/chutes
scraped_at: 2026-06-29
---

ModelsProviders

[Chutes](<https://chutes.ai>) एक OpenAI-संगत API के माध्यम से ओपन-सोर्स मॉडल कैटलॉग उपलब्ध कराता है। OpenClaw `chutes` provider के लिए ब्राउज़र OAuth और प्रत्यक्ष API-key auth, दोनों का समर्थन करता है।

गुण | मान  
---|---  
Provider | `chutes`  
API | OpenAI-संगत  
Base URL | `https://llm.chutes.ai/v1`  
Auth | OAuth या API key (नीचे देखें)  
  
## Plugin इंस्टॉल करें

आधिकारिक Plugin इंस्टॉल करें, फिर Gateway फिर से शुरू करें:

bashCopy code
[code]
    openclaw plugins install @openclaw/chutes-provideropenclaw gateway restart
[/code]

## शुरू करना

### OAuth

* ### OAuth ऑनबोर्डिंग फ़्लो चलाएँ

bashCopy code
[code]
    openclaw onboard --auth-choice chutes
[/code]

OpenClaw ब्राउज़र फ़्लो को स्थानीय रूप से शुरू करता है, या रिमोट/हेडलेस होस्ट पर URL + redirect-paste फ़्लो दिखाता है। OAuth टोकन OpenClaw auth profiles के माध्यम से अपने आप रीफ़्रेश होते हैं।

* ### डिफ़ॉल्ट मॉडल सत्यापित करें

ऑनबोर्डिंग के बाद, डिफ़ॉल्ट मॉडल `chutes/zai-org/GLM-4.7-TEE` पर सेट होता है और Chutes स्थिर कैटलॉग पंजीकृत हो जाता है।

### API key

* ### API key प्राप्त करें

[chutes.ai/settings/api-keys](<https://chutes.ai/settings/api-keys>) पर key बनाएँ।

* ### API key ऑनबोर्डिंग फ़्लो चलाएँ

bashCopy code
[code]
    openclaw onboard --auth-choice chutes-api-key
[/code]

* ### डिफ़ॉल्ट मॉडल सत्यापित करें

ऑनबोर्डिंग के बाद, डिफ़ॉल्ट मॉडल `chutes/zai-org/GLM-4.7-TEE` पर सेट होता है और Chutes स्थिर कैटलॉग पंजीकृत हो जाता है।

## खोज व्यवहार

जब Chutes auth उपलब्ध हो, OpenClaw उस credential के साथ Chutes कैटलॉग को क्वेरी करता है और खोजे गए मॉडलों का उपयोग करता है। यदि discovery विफल हो जाए, तो OpenClaw स्थिर कैटलॉग पर fallback करता है ताकि ऑनबोर्डिंग और startup फिर भी काम करें।

## डिफ़ॉल्ट aliases

OpenClaw Chutes स्थिर कैटलॉग के लिए तीन सुविधा aliases पंजीकृत करता है:

Alias | लक्षित मॉडल  
---|---  
`chutes-fast` | `chutes/zai-org/GLM-4.7-FP8`  
`chutes-pro` | `chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes-vision` | `chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
  
## बिल्ट-इन starter catalog

स्थिर fallback catalog में वर्तमान Chutes refs शामिल हैं:

Model ref  
---  
`chutes/zai-org/GLM-4.7-TEE`  
`chutes/zai-org/GLM-5-TEE`  
`chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes/deepseek-ai/DeepSeek-R1-0528-TEE`  
`chutes/moonshotai/Kimi-K2.5-TEE`  
`chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
`chutes/Qwen/Qwen3-Coder-Next-TEE`  
`chutes/openai/gpt-oss-120b-TEE`  
  
## Config उदाहरण

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "chutes/zai-org/GLM-4.7-TEE" },      models: {        "chutes/zai-org/GLM-4.7-TEE": { alias: "Chutes GLM 4.7" },        "chutes/deepseek-ai/DeepSeek-V3.2-TEE": { alias: "Chutes DeepSeek V3.2" },      },    },  },}
[/code]

OAuth overrides

आप वैकल्पिक environment variables के साथ OAuth फ़्लो को कस्टमाइज़ कर सकते हैं:

Variable | उद्देश्य  
---|---  
`CHUTES_CLIENT_ID` | कस्टम OAuth client ID  
`CHUTES_CLIENT_SECRET` | कस्टम OAuth client secret  
`CHUTES_OAUTH_REDIRECT_URI` | कस्टम redirect URI  
`CHUTES_OAUTH_SCOPES` | कस्टम OAuth scopes  
  
redirect-app आवश्यकताओं और सहायता के लिए [Chutes OAuth docs](<https://chutes.ai/docs/sign-in-with-chutes/overview>) देखें।

नोट्स

  * API-key और OAuth discovery, दोनों समान `chutes` provider id का उपयोग करते हैं।
  * Chutes मॉडल `chutes/<model-id>` के रूप में पंजीकृत होते हैं।
  * यदि startup पर discovery विफल हो जाए, तो स्थिर कैटलॉग अपने आप उपयोग किया जाता है।


## संबंधित

[**मॉडल चयन** Provider नियम, मॉडल refs, और failover व्यवहार। ](</hi/concepts/model-providers>) [**Configuration संदर्भ** provider settings सहित पूरा config schema। ](</hi/gateway/configuration-reference>) [**Chutes** Chutes डैशबोर्ड और API docs। ](<https://chutes.ai>) [**Chutes API keys** Chutes API keys बनाएँ और प्रबंधित करें। ](<https://chutes.ai/settings/api-keys>)

Was this useful?YesNo

Open issue