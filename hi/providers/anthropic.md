---
title: Anthropic
source_url: https://docs.openclaw.ai/hi/providers/anthropic
scraped_at: 2026-06-29
---

ModelsProviders

Anthropic **Claude** मॉडल परिवार बनाता है। OpenClaw दो auth routes का समर्थन करता है:

  * **API key** — usage-based billing के साथ सीधे Anthropic API access (`anthropic/*` models)
  * **Claude CLI** — उसी host पर मौजूदा Claude Code login का पुनः उपयोग


## शुरू करना

### API key

**इसके लिए सर्वोत्तम:** standard API access और usage-based billing.

* ### अपनी API key प्राप्त करें

[Anthropic Console](<https://console.anthropic.com/>) में API key बनाएं।

* ### onboarding चलाएं

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

या key को सीधे pass करें:

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### सत्यापित करें कि model उपलब्ध है

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Config example

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "example-anthropic-key-not-real" },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-8" } } },}
[/code]

### Claude CLI

**इसके लिए सर्वोत्तम:** अलग API key के बिना मौजूदा Claude CLI login का पुनः उपयोग।

* ### सुनिश्चित करें कि Claude CLI installed है और logged in है

इससे verify करें:

bashCopy code
[code]
    claude --version
[/code]

* ### onboarding चलाएं

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

OpenClaw मौजूदा Claude CLI credentials का पता लगाकर उनका पुनः उपयोग करता है।

* ### सत्यापित करें कि model उपलब्ध है

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Config example

canonical Anthropic model ref और CLI runtime override को प्राथमिकता दें:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-8" },      models: {        "anthropic/claude-opus-4-8": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

Legacy `claude-cli/claude-opus-4-7` model refs अभी भी compatibility के लिए काम करते हैं, लेकिन नए config में provider/model selection को `anthropic/*` के रूप में रखना चाहिए और execution backend को provider/model runtime policy में रखना चाहिए।

### Billing और `claude -p`

OpenClaw Claude CLI runs के लिए Claude Code के non-interactive `claude -p` path का उपयोग करता है। Anthropic वर्तमान में उस path को Agent SDK/programmatic usage मानता है:

  * Anthropic के 15 जून, 2026 support update ने पहले घोषित अलग Agent SDK credit plan को रोक दिया।
  * फिलहाल, subscription-plan Claude Agent SDK, `claude -p`, और third-party app usage अभी भी signed-in subscription की usage limits से draw करते हैं।
  * पहले घोषित monthly Agent SDK credit उपलब्ध नहीं है, जब तक Anthropic उस plan को revise कर रहा है।
  * Console/API-key logins pay-as-you-go API billing का उपयोग करते हैं और उन्हें subscription Agent SDK credit नहीं मिलता।


pause notice के लिए Anthropic का [Agent SDK plan article](<https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan>) देखें, और subscription behavior के लिए Claude Code plan articles [Pro/Max](<https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan>) और [Team/Enterprise](<https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan>) देखें।

Anthropic OpenClaw release के बिना Claude Code billing और rate-limit behavior बदल सकता है। जब billing predictability महत्वपूर्ण हो, तो `claude auth status`, `/status`, और Anthropic के linked docs देखें।

## Thinking defaults (Claude Fable 5, 4.8, और 4.6)

`anthropic/claude-fable-5` हमेशा adaptive thinking का उपयोग करता है और default रूप से `high` effort पर रहता है। क्योंकि Anthropic इस model के लिए thinking को disable करने की अनुमति नहीं देता, `/think off` और `/think minimal` `low` effort का उपयोग करते हैं। OpenClaw Fable 5 requests के लिए custom temperature values भी omit करता है।

Claude Opus 4.8 OpenClaw में default रूप से thinking off रखता है। जब आप `/think high|xhigh|max` से adaptive thinking को स्पष्ट रूप से enable करते हैं, OpenClaw Anthropic के Opus 4.8 effort values भेजता है; Claude 4.6 models default रूप से `adaptive` होते हैं।

Per-message override `/think:<level>` से करें या model params में:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-8": {          params: { thinking: "high" },        },      },    },  },}
[/code]

## Prompt caching

OpenClaw API-key auth के लिए Anthropic की prompt caching feature का समर्थन करता है।

Value | Cache duration | Description  
---|---|---  
`"short"` (default) | 5 minutes | API-key auth के लिए automatically applied  
`"long"` | 1 hour | Extended cache  
`"none"` | No caching | prompt caching disable करें  
  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

Per-agent cache overrides

model-level params को baseline के रूप में उपयोग करें, फिर specific agents को `agents.list[].params` के जरिए override करें:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

Config merge order:

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params` (matching `id`, key द्वारा overrides)


यह एक agent को long-lived cache रखने देता है, जबकि same model पर दूसरा agent bursty/low-reuse traffic के लिए caching disable करता है।

Bedrock Claude notes

  * Bedrock पर Anthropic Claude models (`amazon-bedrock/*anthropic.claude*`) configured होने पर `cacheRetention` pass-through accept करते हैं।
  * Non-Anthropic Bedrock models runtime पर `cacheRetention: "none"` पर forced होते हैं।
  * API-key smart defaults Claude-on-Bedrock refs के लिए भी `cacheRetention: "short"` seed करते हैं, जब explicit value set नहीं है।


## Advanced configuration

Fast mode

OpenClaw का shared `/fast` toggle direct Anthropic traffic (API-key और OAuth to `api.anthropic.com`) का समर्थन करता है।

Command | Maps to  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

Media understanding (image and PDF)

bundled Anthropic plugin image और PDF understanding register करता है। OpenClaw configured Anthropic auth से media capabilities को auto-resolve करता है — कोई अतिरिक्त config आवश्यक नहीं है।

Property | Value  
---|---  
Default model | `claude-opus-4-8`  
Supported input | Images, PDF documents  
  
जब किसी conversation में image या PDF attached होती है, OpenClaw automatically उसे Anthropic media understanding provider के माध्यम से route करता है।

1M context window

Anthropic की 1M context window GA-capable Claude 4.x models पर उपलब्ध है, जैसे Opus 4.8, Opus 4.7, Opus 4.6, और Sonnet 4.6। OpenClaw उन models को automatically 1M पर size करता है:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {},      },    },  },}
[/code]

पुराने configs `params.context1m: true` रख सकते हैं, लेकिन OpenClaw अब retired `context-1m-2025-08-07` beta header नहीं भेजता। उस value वाली पुरानी `anthropicBeta` config entries request header resolution के दौरान ignore की जाती हैं और unsupported पुराने Claude models अपने normal context window पर रहते हैं।

`params.context1m: true` Claude CLI backend (`claude-cli/*`) पर भी eligible GA-capable Opus और Sonnet models के लिए apply होता है, जिससे उन CLI sessions के लिए runtime context window direct-API behavior से match करने के लिए preserve रहता है।

Claude Opus 4.8 1M संदर्भ

`anthropic/claude-opus-4-8` और इसके `claude-cli` वैरिएंट में डिफ़ॉल्ट रूप से 1M संदर्भ विंडो होती है — `params.context1m: true` की आवश्यकता नहीं।

## समस्या निवारण

401 त्रुटियाँ / टोकन अचानक अमान्य

Anthropic टोकन प्रमाणीकरण समाप्त हो जाता है और निरस्त किया जा सकता है। नए सेटअप के लिए, इसके बजाय Anthropic API कुंजी का उपयोग करें।

प्रदाता "anthropic" के लिए कोई API कुंजी नहीं मिली

Anthropic प्रमाणीकरण **प्रति एजेंट** होता है — नए एजेंट मुख्य एजेंट की कुंजियाँ इनहेरिट नहीं करते। उस एजेंट के लिए ऑनबोर्डिंग फिर से चलाएँ (या Gateway होस्ट पर API कुंजी कॉन्फ़िगर करें), फिर `openclaw models status` से सत्यापित करें।

प्रोफ़ाइल "anthropic:default" के लिए कोई क्रेडेंशियल नहीं मिले

कौन-सी प्रमाणीकरण प्रोफ़ाइल सक्रिय है, यह देखने के लिए `openclaw models status` चलाएँ। ऑनबोर्डिंग फिर से चलाएँ, या उस प्रोफ़ाइल पथ के लिए API कुंजी कॉन्फ़िगर करें।

कोई उपलब्ध प्रमाणीकरण प्रोफ़ाइल नहीं (सभी कूलडाउन में)

`auth.unusableProfiles` के लिए `openclaw models status --json` देखें। Anthropic दर-सीमा कूलडाउन मॉडल-स्कोप्ड हो सकते हैं, इसलिए कोई संबद्ध Anthropic मॉडल अभी भी उपयोग योग्य हो सकता है। कोई अन्य Anthropic प्रोफ़ाइल जोड़ें या कूलडाउन की प्रतीक्षा करें।

## संबंधित

[**मॉडल चयन** प्रदाता, मॉडल संदर्भ और फ़ेलओवर व्यवहार चुनना। ](</hi/concepts/model-providers>) [**CLI बैकएंड** Claude CLI बैकएंड सेटअप और रनटाइम विवरण। ](</hi/gateway/cli-backends>) [**प्रॉम्प्ट कैशिंग** प्रदाताओं में प्रॉम्प्ट कैशिंग कैसे काम करती है। ](</hi/reference/prompt-caching>) [**OAuth और प्रमाणीकरण** प्रमाणीकरण विवरण और क्रेडेंशियल पुन: उपयोग नियम। ](</hi/gateway/authentication>)

Was this useful?YesNo

Open issue