---
title: Cohere
source_url: https://docs.openclaw.ai/hi/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>) अपने Compatibility API के माध्यम से OpenAI-संगत inference प्रदान करता है। OpenClaw अपने externalization संक्रमण के दौरान Cohere प्रदाता को शिप करता है और इसे Command A मॉडल कैटलॉग के साथ एक आधिकारिक बाहरी Plugin के रूप में भी प्रकाशित करता है।

गुण | मान  
---|---  
प्रदाता आईडी | `cohere`  
Plugin | संक्रमण के दौरान बंडल; आधिकारिक बाहरी पैकेज  
Auth env var | `COHERE_API_KEY`  
Onboarding फ़्लैग | `--auth-choice cohere-api-key`  
प्रत्यक्ष CLI फ़्लैग | `--cohere-api-key <key>`  
API | OpenAI-संगत (`openai-completions`)  
बेस URL | `https://api.cohere.ai/compatibility/v1`  
डिफ़ॉल्ट मॉडल | `cohere/command-a-03-2025`  
  
## शुरू करें

  1. Cohere मौजूदा OpenClaw पैकेजों में शामिल है। अगर यह उपलब्ध नहीं है, तो बाहरी पैकेज इंस्टॉल करें और Gateway रीस्टार्ट करें:

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. Cohere API कुंजी बनाएं।
  3. onboarding चलाएं:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. पुष्टि करें कि कैटलॉग उपलब्ध है:

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

डिफ़ॉल्ट मॉडल केवल तभी सेट किया जाता है जब कोई प्राथमिक मॉडल पहले से कॉन्फ़िगर न हो।

## केवल-environment सेटअप

`COHERE_API_KEY` को Gateway प्रक्रिया के लिए उपलब्ध कराएं, फिर Cohere मॉडल चुनें:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## संबंधित

  * [मॉडल प्रदाता](</hi/concepts/model-providers>)
  * [मॉडल CLI](</hi/cli/models>)
  * [प्रदाता निर्देशिका](</hi/providers>)


Was this useful?YesNo

Open issue