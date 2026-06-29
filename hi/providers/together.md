---
title: Together AI
source_url: https://docs.openclaw.ai/hi/providers/together
scraped_at: 2026-06-29
---

ModelsProviders

[Together AI](<https://together.ai>) एकीकृत API के माध्यम से Llama, DeepSeek, Kimi और अन्य प्रमुख ओपन-सोर्स मॉडल तक पहुंच प्रदान करता है.

गुण | मान  
---|---  
प्रदाता | `together`  
प्रमाणीकरण | `TOGETHER_API_KEY`  
API | OpenAI-संगत  
आधार URL | `https://api.together.xyz/v1`  
  
## शुरू करना

* ### Get an API key

API कुंजी यहां बनाएं: [api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "together/meta-llama/Llama-3.3-70B-Instruct-Turbo",      },    },  },}
[/code]

### गैर-इंटरैक्टिव उदाहरण

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## अंतर्निहित कैटलॉग

OpenClaw यह बंडल किया गया Together कैटलॉग भेजता है:

मॉडल संदर्भ | नाम | इनपुट | संदर्भ | नोट्स  
---|---|---|---|---  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | पाठ | 131,072 | डिफ़ॉल्ट मॉडल  
`together/moonshotai/Kimi-K2.6` | Kimi K2.6 FP4 | पाठ, छवि | 262,144 | Kimi तर्क मॉडल  
`together/deepseek-ai/DeepSeek-V4-Pro` | DeepSeek V4 Pro | पाठ | 512,000 | तर्क पाठ मॉडल  
`together/Qwen/Qwen2.5-7B-Instruct-Turbo` | Qwen2.5 7B Instruct Turbo | पाठ | 32,768 | तेज़ पाठ मॉडल  
`together/zai-org/GLM-5.1` | GLM 5.1 FP4 | पाठ | 202,752 | तर्क पाठ मॉडल  
  
## वीडियो जनरेशन

बंडल किया गया `together` Plugin साझा `video_generate` टूल के माध्यम से वीडियो जनरेशन भी रजिस्टर करता है.

गुण | मान  
---|---  
डिफ़ॉल्ट वीडियो मॉडल | `together/Wan-AI/Wan2.2-T2V-A14B`  
मोड | टेक्स्ट-से-वीडियो; `Wan-AI/Wan2.2-I2V-A14B` के साथ केवल एकल-छवि संदर्भ  
समर्थित पैरामीटर | `aspectRatio`, `resolution`  
  
Together को डिफ़ॉल्ट वीडियो प्रदाता के रूप में उपयोग करने के लिए:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

Environment note

यदि Gateway डेमन (launchd/systemd) के रूप में चलता है, तो सुनिश्चित करें कि `TOGETHER_API_KEY` उस प्रक्रिया के लिए उपलब्ध है (उदाहरण के लिए, `~/.openclaw/.env` में या `env.shellEnv` के माध्यम से).

Troubleshooting

  * सत्यापित करें कि आपकी कुंजी काम करती है: `openclaw models list --provider together`
  * यदि मॉडल दिखाई नहीं दे रहे हैं, तो पुष्टि करें कि API कुंजी आपके Gateway प्रक्रिया के लिए सही वातावरण में सेट है.
  * मॉडल संदर्भ `together/<model-id>` रूप का उपयोग करते हैं.


## संबंधित

[**Model selection** प्रदाता नियम, मॉडल संदर्भ और फ़ेलओवर व्यवहार. ](</hi/concepts/model-providers>) [**Video generation** साझा वीडियो जनरेशन टूल पैरामीटर और प्रदाता चयन. ](</hi/tools/video-generation>) [**Configuration reference** प्रदाता सेटिंग्स सहित पूरा कॉन्फ़िगरेशन स्कीमा. ](</hi/gateway/configuration-reference>) [**Together AI** Together AI डैशबोर्ड, API दस्तावेज़ और मूल्य निर्धारण. ](<https://together.ai>)

Was this useful?YesNo

Open issue