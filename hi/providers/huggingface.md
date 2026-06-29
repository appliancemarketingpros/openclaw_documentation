---
title: Hugging Face (इन्फरेंस)
source_url: https://docs.openclaw.ai/hi/providers/huggingface
scraped_at: 2026-06-29
---

ModelsProviders

[Hugging Face Inference Providers](<https://huggingface.co/docs/inference-providers>) एकल router API के माध्यम से OpenAI-संगत चैट completions प्रदान करते हैं। आपको एक token से कई models (DeepSeek, Llama, और अधिक) तक पहुंच मिलती है। OpenClaw **OpenAI-संगत endpoint** (केवल chat completions) का उपयोग करता है; text-to-image, embeddings, या speech के लिए [HF inference clients](<https://huggingface.co/docs/api-inference/quicktour>) का सीधे उपयोग करें।

  * प्रदाता: `huggingface`
  * प्रमाणीकरण: `HUGGINGFACE_HUB_TOKEN` या `HF_TOKEN` (**Make calls to Inference Providers** के साथ fine-grained token)
  * API: OpenAI-संगत (`https://router.huggingface.co/v1`)
  * बिलिंग: एकल HF token; [मूल्य निर्धारण](<https://huggingface.co/docs/inference-providers/pricing>) एक निःशुल्क tier के साथ provider rates का पालन करता है।


## शुरुआत करना

* ### एक fine-grained token बनाएं

[Hugging Face Settings Tokens](<https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained>) पर जाएं और नया fine-grained token बनाएं।

* ### onboarding चलाएं

provider dropdown में **Hugging Face** चुनें, फिर संकेत मिलने पर अपनी API key दर्ज करें:

bashCopy code
[code]
    openclaw onboard --auth-choice huggingface-api-key
[/code]

* ### default model चुनें

**Default Hugging Face model** dropdown में, वह model चुनें जिसे आप चाहते हैं। जब आपके पास valid token होता है, तो सूची Inference API से load होती है; अन्यथा built-in सूची दिखाई जाती है। आपका चयन default model के रूप में save किया जाता है।

आप बाद में config में default model set या change भी कर सकते हैं:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/deepseek-ai/DeepSeek-R1" },    },  },}
[/code]

* ### पुष्टि करें कि model उपलब्ध है

bashCopy code
[code]
    openclaw models list --provider huggingface
[/code]

### Non-interactive setup

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice huggingface-api-key \  --huggingface-api-key "$HF_TOKEN"
[/code]

यह `huggingface/deepseek-ai/DeepSeek-R1` को default model के रूप में set करेगा।

## Model IDs

Model refs `huggingface/<org>/<model>` (Hub-style IDs) form का उपयोग करते हैं। नीचे दी गई सूची **GET** `https://router.huggingface.co/v1/models` से है; आपके catalog में और भी शामिल हो सकते हैं।

Model | Ref (`huggingface/` prefix के साथ)  
---|---  
DeepSeek R1 | `deepseek-ai/DeepSeek-R1`  
DeepSeek V3.2 | `deepseek-ai/DeepSeek-V3.2`  
Qwen3 8B | `Qwen/Qwen3-8B`  
Qwen2.5 7B Instruct | `Qwen/Qwen2.5-7B-Instruct`  
Qwen3 32B | `Qwen/Qwen3-32B`  
Llama 3.3 70B Instruct | `meta-llama/Llama-3.3-70B-Instruct`  
Llama 3.1 8B Instruct | `meta-llama/Llama-3.1-8B-Instruct`  
GPT-OSS 120B | `openai/gpt-oss-120b`  
GLM 4.7 | `zai-org/GLM-4.7`  
Kimi K2.5 | `moonshotai/Kimi-K2.5`  
  
## उन्नत configuration

Model discovery और onboarding dropdown

OpenClaw **Inference endpoint को सीधे** call करके models discover करता है:

bashCopy code
[code]
    GET https://router.huggingface.co/v1/models
[/code]

(वैकल्पिक: पूरी सूची के लिए `Authorization: Bearer $HUGGINGFACE_HUB_TOKEN` या `$HF_TOKEN` भेजें; कुछ endpoints बिना auth के subset लौटाते हैं।) response OpenAI-style `{ "object": "list", "data": [ { "id": "Qwen/Qwen3-8B", "owned_by": "Qwen", ... }, ... ] }` है।

जब आप Hugging Face API key configure करते हैं (onboarding, `HUGGINGFACE_HUB_TOKEN`, या `HF_TOKEN` के माध्यम से), OpenClaw उपलब्ध chat-completion models discover करने के लिए इस GET का उपयोग करता है। **interactive setup** के दौरान, token दर्ज करने के बाद आपको उस सूची से populate किया गया **Default Hugging Face model** dropdown दिखाई देता है (या request fail होने पर built-in catalog)। runtime पर (जैसे Gateway startup), key मौजूद होने पर, OpenClaw catalog refresh करने के लिए फिर से **GET** `https://router.huggingface.co/v1/models` call करता है। सूची को built-in catalog के साथ merge किया जाता है (context window और cost जैसे metadata के लिए)। यदि request fail हो जाता है या कोई key set नहीं है, तो केवल built-in catalog का उपयोग किया जाता है।

Model names, aliases, और policy suffixes

  * **API से नाम:** model display name **GET /v1/models से hydrate** होता है जब API `name`, `title`, या `display_name` लौटाता है; अन्यथा यह model id से derive होता है (जैसे `deepseek-ai/DeepSeek-R1` "DeepSeek R1" बन जाता है)।
  * **display name override करें:** आप config में प्रति model custom label set कर सकते हैं ताकि वह CLI और UI में आपकी इच्छानुसार दिखाई दे:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1 (fast)" },        "huggingface/deepseek-ai/DeepSeek-R1:cheapest": { alias: "DeepSeek R1 (cheap)" },      },    },  },}
[/code]

  * **Policy suffixes:** OpenClaw के bundled Hugging Face docs और helpers अभी इन दो suffixes को built-in policy variants मानते हैं:

    * **`:fastest`** — सबसे अधिक throughput.
    * **`:cheapest`** — प्रति output token सबसे कम cost.

आप इन्हें `models.providers.huggingface.models` में अलग entries के रूप में जोड़ सकते हैं या suffix के साथ `model.primary` set कर सकते हैं। आप अपना default provider order [Inference Provider settings](<https://hf.co/settings/inference-providers>) में भी set कर सकते हैं (कोई suffix नहीं = उस order का उपयोग करें)।

  * **Config merge:** `models.providers.huggingface.models` में मौजूदा entries (जैसे `models.json` में) config merge होने पर रखी जाती हैं। इसलिए आपके द्वारा वहां set किए गए custom `name`, `alias`, या model options सुरक्षित रहते हैं।


Environment और daemon setup

यदि Gateway daemon (launchd/systemd) के रूप में चलता है, तो सुनिश्चित करें कि `HUGGINGFACE_HUB_TOKEN` या `HF_TOKEN` उस process के लिए उपलब्ध है (उदाहरण के लिए, `~/.openclaw/.env` में या `env.shellEnv` के माध्यम से)।

Config: Qwen fallback के साथ DeepSeek R1 json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-R1",        fallbacks: ["huggingface/Qwen/Qwen3-8B"],      },      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1" },        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },      },    },  },}
[/code]

Config: cheapest और fastest variants के साथ Qwen json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen3-8B" },      models: {        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },        "huggingface/Qwen/Qwen3-8B:cheapest": { alias: "Qwen3 8B (cheapest)" },        "huggingface/Qwen/Qwen3-8B:fastest": { alias: "Qwen3 8B (fastest)" },      },    },  },}
[/code]

Config: aliases के साथ DeepSeek + Llama + GPT-OSS json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-V3.2",        fallbacks: [          "huggingface/meta-llama/Llama-3.3-70B-Instruct",          "huggingface/openai/gpt-oss-120b",        ],      },      models: {        "huggingface/deepseek-ai/DeepSeek-V3.2": { alias: "DeepSeek V3.2" },        "huggingface/meta-llama/Llama-3.3-70B-Instruct": { alias: "Llama 3.3 70B" },        "huggingface/openai/gpt-oss-120b": { alias: "GPT-OSS 120B" },      },    },  },}
[/code]

Config: policy suffixes के साथ कई Qwen और DeepSeek json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest" },      models: {        "huggingface/Qwen/Qwen2.5-7B-Instruct": { alias: "Qwen2.5 7B" },        "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest": { alias: "Qwen2.5 7B (cheap)" },        "huggingface/deepseek-ai/DeepSeek-R1:fastest": { alias: "DeepSeek R1 (fast)" },        "huggingface/meta-llama/Llama-3.1-8B-Instruct": { alias: "Llama 3.1 8B" },      },    },  },}
[/code]

## संबंधित

[**Model selection** सभी providers, model refs, और failover behavior का overview. ](</hi/concepts/model-providers>) [**Model selection** models कैसे चुनें और configure करें। ](</hi/concepts/models>) [**Inference Providers docs** आधिकारिक Hugging Face Inference Providers documentation. ](<https://huggingface.co/docs/inference-providers>) [**Configuration** पूरा config reference. ](</hi/gateway/configuration>)

Was this useful?YesNo

Open issue