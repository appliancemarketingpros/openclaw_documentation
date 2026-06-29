---
title: LiteLLM
source_url: https://docs.openclaw.ai/hi/providers/litellm
scraped_at: 2026-06-29
---

ModelsProviders

[LiteLLM](<https://litellm.ai>) एक ओपन-सोर्स LLM Gateway है जो 100+ मॉडल प्रदाताओं के लिए एक एकीकृत API प्रदान करता है। केंद्रीकृत लागत ट्रैकिंग, लॉगिंग, और अपनी OpenClaw config बदले बिना बैकएंड स्विच करने की लचीलापन पाने के लिए OpenClaw को LiteLLM के माध्यम से रूट करें।

## त्वरित शुरुआत

### Onboarding (recommended)

**इसके लिए सर्वोत्तम:** काम करने वाले LiteLLM सेटअप तक सबसे तेज रास्ता।

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

किसी रिमोट प्रॉक्सी के साथ गैर-इंटरैक्टिव सेटअप के लिए, प्रॉक्सी URL स्पष्ट रूप से पास करें:

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### Manual setup

**इसके लिए सर्वोत्तम:** इंस्टॉलेशन और config पर पूरा नियंत्रण।

* ### Start LiteLLM Proxy

bashCopy code
[code]
    pip install 'litellm[proxy]'litellm --model claude-opus-4-6
[/code]

* ### Point OpenClaw to LiteLLM

bashCopy code
[code]
    export LITELLM_API_KEY="your-litellm-key" openclaw
[/code]

बस इतना ही। OpenClaw अब LiteLLM के माध्यम से रूट करता है।

## कॉन्फ़िगरेशन

### एनवायरनमेंट वेरिएबल

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### Config फ़ाइल

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## उन्नत कॉन्फ़िगरेशन

### इमेज जनरेशन

LiteLLM OpenAI-संगत `/images/generations` और `/images/edits` रूट के माध्यम से `image_generate` टूल का भी समर्थन कर सकता है। `agents.defaults.imageGenerationModel` के तहत LiteLLM इमेज मॉडल कॉन्फ़िगर करें:

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

`http://localhost:4000` जैसे Loopback LiteLLM URL किसी वैश्विक प्राइवेट-नेटवर्क ओवरराइड के बिना काम करते हैं। LAN पर होस्ट किए गए प्रॉक्सी के लिए, `models.providers.litellm.request.allowPrivateNetwork: true` सेट करें क्योंकि API कुंजी कॉन्फ़िगर किए गए प्रॉक्सी होस्ट को भेजी जाएगी।

Virtual keys

OpenClaw के लिए खर्च सीमाओं वाली एक समर्पित कुंजी बनाएं:

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

जनरेट की गई कुंजी को `LITELLM_API_KEY` के रूप में उपयोग करें।

Model routing

LiteLLM मॉडल अनुरोधों को अलग-अलग बैकएंड पर रूट कर सकता है। इसे अपनी LiteLLM `config.yaml` में कॉन्फ़िगर करें:

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

OpenClaw `claude-opus-4-6` का अनुरोध करता रहता है — LiteLLM रूटिंग संभालता है।

Viewing usage

LiteLLM का डैशबोर्ड या API जांचें:

bashCopy code
[code]
    # Key infocurl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # Spend logscurl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

Proxy behavior notes

  * LiteLLM डिफ़ॉल्ट रूप से `http://localhost:4000` पर चलता है
  * OpenClaw LiteLLM के प्रॉक्सी-शैली OpenAI-संगत `/v1` endpoint के माध्यम से कनेक्ट करता है
  * नेटिव केवल-OpenAI अनुरोध शेपिंग LiteLLM के माध्यम से लागू नहीं होती: कोई `service_tier` नहीं, कोई Responses `store` नहीं, कोई prompt-cache संकेत नहीं, और कोई OpenAI reasoning-compat payload शेपिंग नहीं
  * छिपे हुए OpenClaw attribution headers (`originator`, `version`, `User-Agent`) कस्टम LiteLLM base URLs पर inject नहीं किए जाते


## संबंधित

[**LiteLLM Docs** आधिकारिक LiteLLM दस्तावेज़ और API संदर्भ। ](<https://docs.litellm.ai>) [**Model selection** सभी प्रदाताओं, मॉडल refs, और फेलओवर व्यवहार का अवलोकन। ](</hi/concepts/model-providers>) [**Configuration** पूरा config संदर्भ। ](</hi/gateway/configuration>) [**Model selection** मॉडल चुनने और कॉन्फ़िगर करने का तरीका। ](</hi/concepts/models>)

Was this useful?YesNo

Open issue