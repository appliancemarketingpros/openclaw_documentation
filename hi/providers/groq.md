---
title: Groq
source_url: https://docs.openclaw.ai/hi/providers/groq
scraped_at: 2026-06-29
---

ModelsProviders

[Groq](<https://groq.com>) कस्टम LPU हार्डवेयर का उपयोग करके open-weight मॉडल (Llama, Gemma, Kimi, Qwen, GPT OSS, और अधिक) पर अति-तेज़ inference प्रदान करता है। Groq plugin OpenAI-संगत chat provider और audio media-understanding provider, दोनों को register करता है।

गुण | मान  
---|---  
Provider id | `groq`  
Plugin | आधिकारिक बाहरी package  
Auth env var | `GROQ_API_KEY`  
API | OpenAI-संगत (`openai-completions`)  
Base URL | `https://api.groq.com/openai/v1`  
Audio transcription | `whisper-large-v3-turbo` (default)  
Suggested chat default | `groq/llama-3.3-70b-versatile`  
  
## Plugin install करें

आधिकारिक plugin install करें, फिर Gateway restart करें:

bashCopy code
[code]
    openclaw plugins install @openclaw/groq-provideropenclaw gateway restart
[/code]

## शुरू करना

* ### API key प्राप्त करें

[console.groq.com/keys](<https://console.groq.com/keys>) पर API key बनाएँ।

* ### API key सेट करें

bashCopy code
[code]
    export GROQ_API_KEY=gsk_...
[/code]

* ### default model सेट करें

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

* ### catalog पहुँच योग्य है, सत्यापित करें

bashCopy code
[code]
    openclaw models list --provider groq
[/code]

### Config file उदाहरण

json5Copy code
[code]
    {  env: { GROQ_API_KEY: "gsk_..." },  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

## Built-in catalog

OpenClaw reasoning और non-reasoning entries, दोनों के साथ manifest-backed Groq catalog ship करता है। अपने installed version के static rows देखने के लिए `openclaw models list --provider groq` चलाएँ, या Groq की authoritative list के लिए [console.groq.com/docs/models](<https://console.groq.com/docs/models>) देखें।

Model ref | नाम | Reasoning | Input | Context  
---|---|---|---|---  
`groq/llama-3.3-70b-versatile` | Llama 3.3 70B Versatile | नहीं | text | 131,072  
`groq/llama-3.1-8b-instant` | Llama 3.1 8B Instant | नहीं | text | 131,072  
`groq/meta-llama/llama-4-scout-17b-16e-instruct` | Llama 4 Scout 17B | नहीं | text + image | 131,072  
`groq/openai/gpt-oss-120b` | GPT OSS 120B | हाँ | text | 131,072  
`groq/openai/gpt-oss-20b` | GPT OSS 20B | हाँ | text | 131,072  
`groq/openai/gpt-oss-safeguard-20b` | Safety GPT OSS 20B | हाँ | text | 131,072  
`groq/qwen/qwen3-32b` | Qwen3 32B | हाँ | text | 131,072  
`groq/groq/compound` | Compound | हाँ | text | 131,072  
`groq/groq/compound-mini` | Compound Mini | हाँ | text | 131,072  
  
## Reasoning models

OpenClaw अपने साझा `/think` levels को Groq के model-specific `reasoning_effort` values से map करता है:

  * `qwen/qwen3-32b` के लिए, disabled thinking `none` भेजता है और enabled thinking `default` भेजता है।
  * Groq GPT OSS reasoning models (`openai/gpt-oss-*`) के लिए, OpenClaw `/think` level के आधार पर `low`, `medium`, या `high` भेजता है। Disabled thinking `reasoning_effort` को omit करता है क्योंकि ये models disabled value support नहीं करते।
  * DeepSeek R1 Distill, Qwen QwQ, और Compound Groq की native reasoning surface का उपयोग करते हैं; `/think` visibility control करता है लेकिन model हमेशा reason करता है।


साझा `/think` levels और OpenClaw उन्हें प्रत्येक provider के लिए कैसे translate करता है, इसके लिए [Thinking modes](</hi/tools/thinking>) देखें।

## Audio transcription

Groq का plugin एक **audio media-understanding provider** भी register करता है ताकि voice messages को साझा `tools.media.audio` surface के माध्यम से transcribe किया जा सके।

गुण | मान  
---|---  
Shared config path | `tools.media.audio`  
Default base URL | `https://api.groq.com/openai/v1`  
Default model | `whisper-large-v3-turbo`  
Auto priority | 20  
API endpoint | OpenAI-संगत `/audio/transcriptions`  
  
Groq को default audio backend बनाने के लिए:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [{ provider: "groq" }],      },    },  },}
[/code]

daemon के लिए environment availability

यदि Gateway managed service (launchd, systemd, Docker) के रूप में चलता है, तो `GROQ_API_KEY` उस process को visible होना चाहिए — केवल आपके interactive shell को नहीं।

Custom Groq model ids

OpenClaw runtime पर कोई भी Groq model id स्वीकार करता है। Groq द्वारा दिखाए गए exact id का उपयोग करें और उसके आगे `groq/` prefix लगाएँ। static catalog common cases को cover करता है; uncatalogued ids default OpenAI-संगत template पर fall through करते हैं।

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/<your-model-id>" },    },  },}
[/code]

## संबंधित

[**Model providers** providers, model refs, और failover behavior चुनना। ](</hi/concepts/model-providers>) [**Thinking modes** Reasoning effort levels और provider-policy interaction। ](</hi/tools/thinking>) [**Configuration reference** provider और audio settings सहित पूरा config schema। ](</hi/gateway/configuration-reference>) [**Groq Console** Groq dashboard, API docs, और pricing। ](<https://console.groq.com>)

Was this useful?YesNo

Open issue