---
title: OpenAI
source_url: https://docs.openclaw.ai/hi/providers/openai
scraped_at: 2026-06-29
---

ModelsProviders

OpenAI GPT मॉडलों के लिए डेवलपर API प्रदान करता है, और Codex OpenAI के Codex क्लाइंट के माध्यम से ChatGPT-प्लान कोडिंग एजेंट के रूप में भी उपलब्ध है। OpenClaw दोनों प्रमाणीकरण आकृतियों के लिए एक ही provider id, `openai`, का उपयोग करता है।

OpenClaw कैननिकल OpenAI मॉडल रूट के रूप में `openai/*` का उपयोग करता है। OpenAI मॉडलों पर एम्बेडेड एजेंट टर्न डिफ़ॉल्ट रूप से नेटिव Codex ऐप-सर्वर रनटाइम के माध्यम से चलते हैं; इमेज, एम्बेडिंग, स्पीच और रियलटाइम जैसे गैर-एजेंट OpenAI सतहों के लिए प्रत्यक्ष OpenAI API-key प्रमाणीकरण उपलब्ध रहता है।

  * **एजेंट मॉडल** \- Codex रनटाइम के माध्यम से `openai/*` मॉडल; ChatGPT/Codex सब्सक्रिप्शन उपयोग के लिए Codex प्रमाणीकरण से साइन इन करें, या जब आप जानबूझकर API-key प्रमाणीकरण चाहते हों, तब Codex-संगत OpenAI API-key बैकअप कॉन्फ़िगर करें।
  * **गैर-एजेंट OpenAI API** \- `OPENAI_API_KEY` या OpenAI API-key ऑनबोर्डिंग के माध्यम से उपयोग-आधारित बिलिंग के साथ प्रत्यक्ष OpenAI Platform पहुंच।
  * **लेगेसी कॉन्फ़िग** \- लेगेसी Codex मॉडल संदर्भों को `openclaw doctor --fix` द्वारा `openai/*` और Codex रनटाइम में सुधारा जाता है।


OpenAI स्पष्ट रूप से OpenClaw जैसे बाहरी टूल और वर्कफ़्लो में सब्सक्रिप्शन OAuth उपयोग का समर्थन करता है।

Provider, मॉडल, रनटाइम और चैनल अलग-अलग परतें हैं। यदि ये लेबल आपस में मिल रहे हैं, तो कॉन्फ़िग बदलने से पहले [एजेंट रनटाइम](</hi/concepts/agent-runtimes>) पढ़ें।

## तुरंत चयन

लक्ष्य | उपयोग | नोट्स  
---|---|---  
नेटिव Codex रनटाइम के साथ ChatGPT/Codex सब्सक्रिप्शन | `openai/gpt-5.5` | डिफ़ॉल्ट OpenAI एजेंट सेटअप। Codex प्रमाणीकरण से साइन इन करें।  
एजेंट मॉडलों के लिए प्रत्यक्ष API-key बिलिंग | `openai/gpt-5.5` और Codex-संगत API-key प्रोफ़ाइल | सब्सक्रिप्शन प्रमाणीकरण के बाद बैकअप रखने के लिए `auth.order.openai` का उपयोग करें।  
स्पष्ट OpenClaw के माध्यम से प्रत्यक्ष API-key बिलिंग | `openai/gpt-5.5` और provider/model रनटाइम `openclaw` | सामान्य `openai` API-key प्रोफ़ाइल चुनें।  
नवीनतम ChatGPT Instant API ऐलियस | `openai/chat-latest` | केवल प्रत्यक्ष API-key। प्रयोगों के लिए बदलता ऐलियस, डिफ़ॉल्ट नहीं।  
OpenClaw के माध्यम से ChatGPT/Codex सब्सक्रिप्शन प्रमाणीकरण | `openai/gpt-5.5` और provider/model रनटाइम `openclaw` | संगतता रूट के लिए `openai` OAuth प्रोफ़ाइल चुनें।  
इमेज बनाना या संपादित करना | `openai/gpt-image-2` | `OPENAI_API_KEY` या OpenAI Codex OAuth, दोनों के साथ काम करता है।  
पारदर्शी-बैकग्राउंड इमेज | `openai/gpt-image-1.5` | `outputFormat=png` या `webp` और `openai.background=transparent` का उपयोग करें।  
  
## नामकरण मैप

नाम समान हैं, लेकिन परस्पर बदलने योग्य नहीं हैं:

दिखने वाला नाम | परत | अर्थ  
---|---|---  
`openai` | Provider प्रीफ़िक्स | कैननिकल OpenAI मॉडल रूट; एजेंट टर्न Codex रनटाइम का उपयोग करते हैं।  
लेगेसी OpenAI Codex प्रीफ़िक्स | लेगेसी प्रीफ़िक्स | पुराना मॉडल/प्रोफ़ाइल नेमस्पेस। `openclaw doctor --fix` इसे `openai` में माइग्रेट करता है।  
`codex` Plugin | Plugin | बंडल किया गया OpenClaw Plugin जो नेटिव Codex ऐप-सर्वर रनटाइम और `/codex` चैट नियंत्रण प्रदान करता है।  
provider/model `agentRuntime.id: codex` | एजेंट रनटाइम | मेल खाते एम्बेडेड टर्न के लिए नेटिव Codex ऐप-सर्वर हार्नेस को बाध्य करें।  
`/codex ...` | चैट कमांड सेट | बातचीत से Codex ऐप-सर्वर थ्रेड को बाइंड/नियंत्रित करें।  
`runtime: "acp", agentId: "codex"` | ACP सेशन रूट | स्पष्ट फ़ॉलबैक पथ जो ACP/acpx के माध्यम से Codex चलाता है।  
  
इसका अर्थ है कि कोई कॉन्फ़िग जानबूझकर `openai/*` मॉडल संदर्भ रख सकता है, जबकि प्रमाणीकरण प्रोफ़ाइल API-key या ChatGPT/Codex OAuth क्रेडेंशियल में से किसी पर इंगित कर सकती हैं। कॉन्फ़िग के लिए `auth.order.openai` का उपयोग करें; `openclaw doctor --fix` लेगेसी Codex मॉडल संदर्भों, लेगेसी Codex प्रमाणीकरण प्रोफ़ाइल id और लेगेसी Codex प्रमाणीकरण क्रम को कैननिकल OpenAI रूट में फिर से लिखता है।

## OpenClaw सुविधा कवरेज

OpenAI क्षमता | OpenClaw सतह | स्थिति  
---|---|---  
चैट / Responses | `openai/<model>` मॉडल provider | हाँ  
Codex सब्सक्रिप्शन मॉडल | OpenAI OAuth के साथ `openai/<model>` | हाँ  
लेगेसी Codex मॉडल संदर्भ | लेगेसी Codex मॉडल संदर्भ या `codex-cli/<model>` | doctor द्वारा `openai/<model>` में सुधारा गया  
Codex ऐप-सर्वर हार्नेस | छोड़े गए रनटाइम या provider/model `agentRuntime.id: codex` के साथ `openai/<model>` | हाँ  
सर्वर-साइड वेब खोज | नेटिव OpenAI Responses टूल | हाँ, जब वेब खोज सक्षम हो और कोई provider पिन न हो  
इमेज | `image_generate` | हाँ  
वीडियो | `video_generate` | हाँ  
टेक्स्ट-टू-स्पीच | `messages.tts.provider: "openai"` / `tts` | हाँ  
बैच स्पीच-टू-टेक्स्ट | `tools.media.audio` / मीडिया समझ | हाँ  
स्ट्रीमिंग स्पीच-टू-टेक्स्ट | Voice Call `streaming.provider: "openai"` | हाँ  
रियलटाइम वॉइस | Voice Call `realtime.provider: "openai"` / Control UI Talk `talk.realtime.provider: "openai"` | हाँ (OpenAI Platform क्रेडिट चाहिए, Codex/ChatGPT सब्सक्रिप्शन नहीं)  
एम्बेडिंग | मेमोरी एम्बेडिंग provider | हाँ  
  
## मेमोरी एम्बेडिंग

OpenClaw `memory_search` इंडेक्सिंग और क्वेरी एम्बेडिंग के लिए OpenAI या OpenAI-संगत एम्बेडिंग एंडपॉइंट का उपयोग कर सकता है:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",        model: "text-embedding-3-small",      },    },  },}
[/code]

ऐसे OpenAI-संगत एंडपॉइंट जिनमें असममित एम्बेडिंग लेबल चाहिए, उनके लिए `memorySearch` के अंतर्गत `queryInputType` और `documentInputType` सेट करें। OpenClaw इन्हें provider-विशिष्ट `input_type` अनुरोध फ़ील्ड के रूप में आगे भेजता है: क्वेरी एम्बेडिंग `queryInputType` का उपयोग करती हैं; इंडेक्स किए गए मेमोरी खंड और बैच इंडेक्सिंग `documentInputType` का उपयोग करते हैं। पूरे उदाहरण के लिए [मेमोरी कॉन्फ़िगरेशन संदर्भ](</hi/reference/memory-config#provider-specific-config>) देखें।

## शुरू करना

अपनी पसंदीदा प्रमाणीकरण विधि चुनें और सेटअप चरणों का पालन करें।

### API key (OpenAI Platform)

**सबसे उपयुक्त:** प्रत्यक्ष API पहुंच और उपयोग-आधारित बिलिंग।

* ### अपनी API key प्राप्त करें

[OpenAI Platform dashboard](<https://platform.openai.com/api-keys>) से API key बनाएँ या कॉपी करें।

* ### ऑनबोर्डिंग चलाएँ

bashCopy code
[code]
    openclaw onboard --auth-choice openai-api-key
[/code]

या key सीधे पास करें:

bashCopy code
[code]
    openclaw onboard --openai-api-key "$OPENAI_API_KEY"
[/code]

* ### सत्यापित करें कि मॉडल उपलब्ध है

bashCopy code
[code]
    openclaw models list --provider openai
[/code]

### रूट सारांश

मॉडल संदर्भ | रनटाइम कॉन्फ़िग | रूट | प्रमाणीकरण  
---|---|---|---  
`openai/gpt-5.5` | छोड़ा गया / provider/model `agentRuntime.id: "codex"` | Codex ऐप-सर्वर हार्नेस | Codex-संगत OpenAI प्रोफ़ाइल  
`openai/gpt-5.4-mini` | छोड़ा गया / provider/model `agentRuntime.id: "codex"` | Codex ऐप-सर्वर हार्नेस | Codex-संगत OpenAI प्रोफ़ाइल  
`openai/gpt-5.5` | provider/model `agentRuntime.id: "openclaw"` | OpenClaw एम्बेडेड रनटाइम | चुनी गई `openai` प्रोफ़ाइल  
  
### कॉन्फ़िग उदाहरण

json5Copy code
[code]
    {  env: { OPENAI_API_KEY: "example-openai-key-not-real" },  agents: { defaults: { model: { primary: "openai/gpt-5.5" } } },}
[/code]

OpenAI API से ChatGPT का मौजूदा Instant मॉडल आज़माने के लिए, मॉडल को `openai/chat-latest` पर सेट करें:

json5Copy code
[code]
    {  env: { OPENAI_API_KEY: "example-openai-key-not-real" },  agents: { defaults: { model: { primary: "openai/chat-latest" } } },}
[/code]

`chat-latest` एक बदलता हुआ alias है। OpenAI इसे ChatGPT में उपयोग होने वाले नवीनतम Instant मॉडल के रूप में दस्तावेज़ित करता है और उत्पादन API उपयोग के लिए `gpt-5.5` की अनुशंसा करता है, इसलिए जब तक आपको स्पष्ट रूप से वह alias व्यवहार नहीं चाहिए, `openai/gpt-5.5` को स्थिर default के रूप में रखें। यह alias अभी केवल `medium` text verbosity स्वीकार करता है, इसलिए OpenClaw इस मॉडल के लिए असंगत OpenAI text-verbosity overrides को normalize करता है।

### Codex subscription

**इसके लिए सबसे अच्छा:** अलग API की के बजाय native Codex ऐप-सर्वर execution के साथ अपनी ChatGPT/Codex subscription का उपयोग करना। Codex cloud के लिए ChatGPT sign-in आवश्यक है।

* ### Run Codex OAuth

bashCopy code
[code]
    openclaw onboard --auth-choice openai
[/code]

या सीधे OAuth चलाएं:

bashCopy code
[code]
    openclaw models auth login --provider openai
[/code]

Headless या callback-विरोधी setups के लिए, localhost browser callback के बजाय ChatGPT device-code flow से sign in करने के लिए `--device-code` जोड़ें:

bashCopy code
[code]
    openclaw models auth login --provider openai --device-code
[/code]

* ### Use the canonical OpenAI model route

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary openai/gpt-5.5
[/code]

default path के लिए कोई runtime config आवश्यक नहीं है। OpenAI agent turns native Codex ऐप-सर्वर runtime को अपने आप चुनते हैं, और जब यह route चुना जाता है तो OpenClaw bundled Codex plugin install या repair करता है।

* ### Verify Codex auth is available

bashCopy code
[code]
    openclaw models list --provider openai
[/code]

gateway चलने के बाद, native ऐप-सर्वर runtime सत्यापित करने के लिए chat में `/codex status` या `/codex models` भेजें।

### Route सारांश

मॉडल ref | Runtime config | Route | Auth  
---|---|---|---  
`openai/gpt-5.5` | छोड़ा गया / provider/model `agentRuntime.id: "codex"` | Native Codex ऐप-सर्वर हार्नेस | Codex sign-in या ordered `openai` auth profile  
`openai/gpt-5.5` | provider/model `agentRuntime.id: "openclaw"` | internal Codex-auth transport के साथ OpenClaw embedded runtime | चुनी गई `openai` OAuth profile  
legacy Codex GPT-5.5 ref | doctor द्वारा repaired | Legacy route को `openai/gpt-5.5` में rewritten किया गया | Migrated OpenAI OAuth profile  
`codex-cli/gpt-5.5` | doctor द्वारा repaired | Legacy CLI route को `openai/gpt-5.5` में rewritten किया गया | Codex ऐप-सर्वर auth  
  
### कॉन्फ़िग उदाहरण

json5Copy code
[code]
    {  plugins: { entries: { codex: { enabled: true } } },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },    },  },}
[/code]

API-की backup के साथ, model को `openai/gpt-5.5` पर रखें और auth order को `openai` के अंतर्गत रखें। OpenClaw पहले subscription आज़माएगा, फिर API key, और Codex harness पर ही रहेगा:

json5Copy code
[code]
    {  plugins: { entries: { codex: { enabled: true } } },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },    },  },  auth: {    order: {      openai: [        "openai:user@example.com",        "openai:api-key-backup",      ],    },  },}
[/code]

### Codex OAuth routing जांचें और recover करें

ये commands उपयोग करके देखें कि आपका default agent कौन सा model, runtime, और auth route उपयोग कर रहा है:

bashCopy code
[code]
    openclaw models statusopenclaw models auth list --provider openaiopenclaw config get agents.defaults.model --jsonopenclaw config get models.providers.openai.agentRuntime --json
[/code]

किसी विशिष्ट agent के लिए, `--agent <id>` जोड़ें:

bashCopy code
[code]
    openclaw models status --agent <id>openclaw models auth list --agent <id> --provider openai
[/code]

अगर पुराने config में अब भी legacy Codex GPT refs या explicit runtime config के बिना stale OpenAI runtime session pin है, तो उसे repair करें:

bashCopy code
[code]
    openclaw doctor --fixopenclaw config validate
[/code]

अगर `models auth list --provider openai` कोई usable profile नहीं दिखाता, तो फिर से sign in करें:

bashCopy code
[code]
    openclaw models auth login --provider openaiopenclaw models status --probe --probe-provider openai
[/code]

जब आपको एक ही agent में कई Codex OAuth logins चाहिए और बाद में उन्हें auth ordering या `/model ...@<profileId>` के माध्यम से control करना हो, तो `--profile-id` उपयोग करें:

bashCopy code
[code]
    openclaw models auth login --provider openai --profile-id openai:ritsukoopenclaw models auth login --provider openai --profile-id openai:lain
[/code]

`openai/*`, Codex के माध्यम से OpenAI agent turns के लिए model route है। Profile ordering पर निर्भर होने से पहले पुराने legacy OpenAI Codex prefix profile ids और order entries को migrate करने के लिए `openclaw doctor --fix` चलाएं।

### स्थिति संकेतक

Chat `/status` दिखाता है कि वर्तमान session के लिए कौन सा model runtime active है। Bundled Codex ऐप-सर्वर हार्नेस OpenAI agent model turns के लिए `Runtime: OpenAI Codex` के रूप में दिखाई देता है। Stale OpenAI runtime session pins को Codex में repair किया जाता है, जब तक config स्पष्ट रूप से OpenClaw pin नहीं करता।

### Doctor चेतावनी

अगर legacy Codex model refs या stale OpenAI runtime pins config या session state में बने रहते हैं, तो `openclaw doctor --fix` उन्हें Codex runtime के साथ `openai/*` में rewrite करता है, जब तक OpenClaw स्पष्ट रूप से configured न हो।

### Context window cap

OpenClaw model metadata और runtime context cap को अलग-अलग values मानता है।

Codex OAuth catalog के माध्यम से `openai/gpt-5.5` के लिए:

  * Native `contextWindow`: `1000000`
  * Default runtime `contextTokens` cap: `272000`


छोटा default cap व्यवहार में बेहतर latency और quality characteristics देता है। इसे `contextTokens` से override करें:

json5Copy code
[code]
    {  models: {    providers: {      openai: {        models: [{ id: "gpt-5.5", contextTokens: 160000 }],      },    },  },}
[/code]

### Catalog recovery

OpenClaw `gpt-5.5` के लिए upstream Codex catalog metadata का उपयोग करता है, जब वह मौजूद होता है। अगर account authenticated होने पर live Codex discovery `gpt-5.5` row छोड़ देता है, तो OpenClaw उस OAuth model row को synthesize करता है ताकि cron, sub-agent, और configured default-model runs `Unknown model` के साथ fail न हों।

## Native Codex ऐप-सर्वर auth

Native Codex ऐप-सर्वर हार्नेस `openai/*` model refs plus omitted runtime config या provider/model `agentRuntime.id: "codex"` उपयोग करता है, लेकिन इसका auth अब भी account-based है। OpenClaw इस क्रम में auth चुनता है:

  1. Agent के लिए ordered OpenAI auth profiles, बेहतर है `auth.order.openai` के अंतर्गत। पुराने legacy Codex auth profile ids और legacy Codex auth order migrate करने के लिए `openclaw doctor --fix` चलाएं।
  2. ऐप-सर्वर का मौजूदा account, जैसे local Codex CLI ChatGPT sign-in।
  3. केवल local stdio ऐप-सर्वर launches के लिए, `CODEX_API_KEY`, फिर `OPENAI_API_KEY`, जब ऐप-सर्वर कोई account report नहीं करता और फिर भी OpenAI auth मांगता है।


इसका मतलब है कि local ChatGPT/Codex subscription sign-in को सिर्फ इसलिए replace नहीं किया जाता क्योंकि gateway process के पास direct OpenAI models या embeddings के लिए `OPENAI_API_KEY` भी है। Env API-की fallback केवल local stdio no-account path है; इसे WebSocket ऐप-सर्वर connections को नहीं भेजा जाता। जब subscription-style Codex profile चुनी जाती है, OpenClaw spawned stdio ऐप-सर्वर child से `CODEX_API_KEY` और `OPENAI_API_KEY` भी बाहर रखता है और चुने गए credentials को ऐप-सर्वर login RPC के माध्यम से भेजता है। जब वह subscription profile किसी Codex usage limit से blocked होती है, OpenClaw selected model बदले बिना या Codex harness से बाहर निकले बिना अगले ordered `openai:*` API-की profile पर rotate कर सकता है। Subscription reset time बीत जाने के बाद, subscription profile फिर से eligible हो जाती है।

## Image generation

Bundled `openai` plugin `image_generate` tool के माध्यम से image generation register करता है। यह उसी `openai/gpt-image-2` model ref के माध्यम से OpenAI API-की image generation और Codex OAuth image generation दोनों को support करता है।

Capability | OpenAI API key | Codex OAuth  
---|---|---  
Model ref | `openai/gpt-image-2` | `openai/gpt-image-2`  
Auth | `OPENAI_API_KEY` | OpenAI Codex OAuth sign-in  
Transport | OpenAI Images API | Codex Responses backend  
Max images per request | 4 | 4  
Edit mode | Enabled (up to 5 reference images) | Enabled (up to 5 reference images)  
Size overrides | Supported, including 2K/4K sizes | Supported, including 2K/4K sizes  
Aspect ratio / resolution | OpenAI Images API को forward नहीं किया गया | सुरक्षित होने पर supported size से mapped  
  
json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: { primary: "openai/gpt-image-2" },    },  },}
[/code]

`gpt-image-2`, OpenAI text-to-image generation और image editing दोनों के लिए default है। `gpt-image-1.5`, `gpt-image-1`, और `gpt-image-1-mini` explicit model overrides के रूप में usable रहते हैं। Transparent-background PNG/WebP output के लिए `openai/gpt-image-1.5` उपयोग करें; मौजूदा `gpt-image-2` API `background: "transparent"` reject करता है।

पारदर्शी-पृष्ठभूमि अनुरोध के लिए, एजेंटों को `image_generate` को `model: "openai/gpt-image-1.5"`, `outputFormat: "png"` या `"webp"`, और `background: "transparent"` के साथ कॉल करना चाहिए; पुराना `openai.background` प्रदाता विकल्प अब भी स्वीकार किया जाता है। OpenClaw सार्वजनिक OpenAI और OpenAI Codex OAuth रूट्स को भी सुरक्षित रखता है, डिफ़ॉल्ट `openai/gpt-image-2` पारदर्शी अनुरोधों को `gpt-image-1.5` में फिर से लिखकर; Azure और कस्टम OpenAI-संगत एंडपॉइंट अपने कॉन्फ़िगर किए गए डिप्लॉयमेंट/मॉडल नाम बनाए रखते हैं।

यही सेटिंग हेडलेस CLI रन के लिए भी उपलब्ध है:

bashCopy code
[code]
    openclaw infer image generate \  --model openai/gpt-image-1.5 \  --output-format png \  --background transparent \  --prompt "A simple red circle sticker on a transparent background" \  --json
[/code]

इनपुट फ़ाइल से शुरू करते समय `openclaw infer image edit` के साथ वही `--output-format` और `--background` फ़्लैग इस्तेमाल करें। `--openai-background` OpenAI-विशिष्ट उपनाम के रूप में उपलब्ध रहता है। जब आपको OpenAI Images की गुणवत्ता और लागत नियंत्रित करनी हो, तो `--quality low|medium|high|auto` इस्तेमाल करें। `image generate` या `image edit` में से OpenAI का प्रदाता-विशिष्ट मॉडरेशन संकेत पास करने के लिए `--openai-moderation low|auto` इस्तेमाल करें।

ChatGPT/Codex OAuth इंस्टॉल के लिए, वही `openai/gpt-image-2` रेफ़ रखें। जब कोई `openai` OAuth प्रोफ़ाइल कॉन्फ़िगर होती है, OpenClaw उस संग्रहीत OAuth एक्सेस टोकन को रिज़ॉल्व करता है और Codex Responses बैकएंड के ज़रिए इमेज अनुरोध भेजता है। यह उस अनुरोध के लिए पहले `OPENAI_API_KEY` आज़माता नहीं है या चुपचाप API कुंजी पर वापस नहीं जाता। जब आपको इसके बजाय सीधा OpenAI Images API रूट चाहिए, तो `models.providers.openai` को API कुंजी, कस्टम बेस URL, या Azure एंडपॉइंट के साथ स्पष्ट रूप से कॉन्फ़िगर करें। अगर वह कस्टम इमेज एंडपॉइंट किसी भरोसेमंद LAN/निजी पते पर है, तो `browser.ssrfPolicy.dangerouslyAllowPrivateNetwork: true` भी सेट करें; OpenClaw निजी/आंतरिक OpenAI-संगत इमेज एंडपॉइंट को तब तक ब्लॉक रखता है जब तक यह ऑप्ट-इन मौजूद न हो।

जनरेट करें:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2 prompt="A polished launch poster for OpenClaw on macOS" size=3840x2160 count=1
[/code]

एक पारदर्शी PNG जनरेट करें:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-1.5 prompt="A simple red circle sticker on a transparent background" outputFormat=png background=transparent
[/code]

संपादित करें:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2 prompt="Preserve the object shape, change the material to translucent glass" image=/path/to/reference.png size=1024x1536
[/code]

## वीडियो जनरेशन

बंडल किया गया `openai` Plugin `video_generate` टूल के ज़रिए वीडियो जनरेशन पंजीकृत करता है।

क्षमता | मान  
---|---  
डिफ़ॉल्ट मॉडल | `openai/sora-2`  
मोड | टेक्स्ट-से-वीडियो, इमेज-से-वीडियो, एकल-वीडियो संपादन  
संदर्भ इनपुट | 1 इमेज या 1 वीडियो  
आकार ओवरराइड | टेक्स्ट-से-वीडियो और इमेज-से-वीडियो के लिए समर्थित  
अन्य ओवरराइड | `aspectRatio`, `resolution`, `audio`, `watermark` टूल चेतावनी के साथ अनदेखे किए जाते हैं  
  
OpenAI इमेज-से-वीडियो अनुरोध इमेज `input_reference` के साथ `POST /v1/videos` इस्तेमाल करते हैं। एकल-वीडियो संपादन अपलोड किए गए वीडियो को `video` फ़ील्ड में रखकर `POST /v1/videos/edits` इस्तेमाल करते हैं।

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: { primary: "openai/sora-2" },    },  },}
[/code]

## GPT-5 प्रॉम्प्ट योगदान

OpenClaw, OpenClaw-असेंबल किए गए प्रॉम्प्ट सतहों पर GPT-5-परिवार रन के लिए एक साझा GPT-5 प्रॉम्प्ट योगदान जोड़ता है। यह मॉडल id के आधार पर लागू होता है, इसलिए OpenClaw/प्रदाता रूट जैसे लेगेसी प्री-रिपेयर रेफ़ (लेगेसी Codex GPT-5.5 रेफ़), `openrouter/openai/gpt-5.5`, `opencode/gpt-5.5`, और अन्य संगत GPT-5 रेफ़ को वही ओवरले मिलता है। पुराने GPT-4.x मॉडल को नहीं।

बंडल किए गए नेटिव Codex हार्नेस को Codex ऐप-सर्वर डेवलपर निर्देशों के ज़रिए यह OpenClaw GPT-5 ओवरले नहीं मिलता। नेटिव Codex, Codex-स्वामित्व वाले बेस, मॉडल, और प्रोजेक्ट-डॉक व्यवहार को बनाए रखता है, जबकि OpenClaw नेटिव थ्रेड्स के लिए Codex की बिल्ट-इन पर्सनैलिटी अक्षम करता है ताकि एजेंट वर्कस्पेस पर्सनैलिटी फ़ाइलें प्रामाणिक रहें। OpenClaw केवल रनटाइम संदर्भ योगदान करता है, जैसे चैनल डिलीवरी, OpenClaw डायनेमिक टूल्स, ACP डेलिगेशन, वर्कस्पेस संदर्भ, और OpenClaw Skills।

GPT-5 योगदान मेल खाते OpenClaw-असेंबल किए गए प्रॉम्प्ट पर पर्सोना स्थायित्व, निष्पादन सुरक्षा, टूल अनुशासन, आउटपुट आकार, पूर्णता जाँच, और सत्यापन के लिए टैग किया हुआ व्यवहार अनुबंध जोड़ता है। चैनल-विशिष्ट उत्तर और साइलेंट-मैसेज व्यवहार साझा OpenClaw सिस्टम प्रॉम्प्ट और आउटबाउंड डिलीवरी नीति में रहता है। मैत्रीपूर्ण इंटरैक्शन-शैली परत अलग और कॉन्फ़िगर करने योग्य है।

मान | प्रभाव  
---|---  
`"friendly"` (डिफ़ॉल्ट) | मैत्रीपूर्ण इंटरैक्शन-शैली परत सक्षम करें  
`"on"` | `"friendly"` का उपनाम  
`"off"` | केवल मैत्रीपूर्ण शैली परत अक्षम करें  
  
### कॉन्फ़िग

json5Copy code
[code]
    {  agents: {    defaults: {      promptOverlays: {        gpt5: { personality: "friendly" },      },    },  },}
[/code]

### CLI

bashCopy code
[code]
    openclaw config set agents.defaults.promptOverlays.gpt5.personality off
[/code]

## आवाज़ और वाणी

वाणी संश्लेषण (TTS)

बंडल किया गया `openai` Plugin `messages.tts` सतह के लिए वाणी संश्लेषण पंजीकृत करता है।

सेटिंग | कॉन्फ़िग पथ | डिफ़ॉल्ट  
---|---|---  
मॉडल | `messages.tts.providers.openai.model` | `gpt-4o-mini-tts`  
आवाज़ | `messages.tts.providers.openai.speakerVoice` | `coral`  
गति | `messages.tts.providers.openai.speed` | (सेट नहीं)  
निर्देश | `messages.tts.providers.openai.instructions` | (सेट नहीं, केवल `gpt-4o-mini-tts`)  
फ़ॉर्मैट | `messages.tts.providers.openai.responseFormat` | वॉइस नोट्स के लिए `opus`, फ़ाइलों के लिए `mp3`  
API कुंजी | `messages.tts.providers.openai.apiKey` | `OPENAI_API_KEY` पर वापस जाता है  
बेस URL | `messages.tts.providers.openai.baseUrl` | `https://api.openai.com/v1`  
अतिरिक्त बॉडी | `messages.tts.providers.openai.extraBody` / `extra_body` | (सेट नहीं)  
  
उपलब्ध मॉडल: `gpt-4o-mini-tts`, `tts-1`, `tts-1-hd`। उपलब्ध आवाज़ें: `alloy`, `ash`, `ballad`, `cedar`, `coral`, `echo`, `fable`, `juniper`, `marin`, `onyx`, `nova`, `sage`, `shimmer`, `verse`।

OpenClaw के जनरेट किए गए फ़ील्ड के बाद `extraBody` को `/audio/speech` अनुरोध JSON में मर्ज किया जाता है, इसलिए इसे उन OpenAI-संगत एंडपॉइंट के लिए इस्तेमाल करें जिन्हें `lang` जैसी अतिरिक्त कुंजियों की आवश्यकता होती है। प्रोटोटाइप कुंजियाँ अनदेखी की जाती हैं।

json5Copy code
[code]
    {  messages: {    tts: {      providers: {        openai: { model: "gpt-4o-mini-tts", speakerVoice: "coral" },      },    },  },}
[/code]

वाणी-से-पाठ

बंडल किया गया `openai` Plugin OpenClaw की मीडिया-अंडरस्टैंडिंग ट्रांसक्रिप्शन सतह के ज़रिए बैच वाणी-से-पाठ पंजीकृत करता है।

  * डिफ़ॉल्ट मॉडल: `gpt-4o-transcribe`
  * एंडपॉइंट: OpenAI REST `/v1/audio/transcriptions`
  * इनपुट पथ: मल्टीपार्ट ऑडियो फ़ाइल अपलोड
  * OpenClaw में जहाँ भी इनबाउंड ऑडियो ट्रांसक्रिप्शन `tools.media.audio` इस्तेमाल करता है, वहाँ समर्थित, जिसमें Discord वॉइस-चैनल सेगमेंट और चैनल ऑडियो अटैचमेंट शामिल हैं


इनबाउंड ऑडियो ट्रांसक्रिप्शन के लिए OpenAI को बाध्य करने हेतु:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [          {            type: "provider",            provider: "openai",            model: "gpt-4o-transcribe",          },        ],      },    },  },}
[/code]

साझा ऑडियो मीडिया कॉन्फ़िग या प्रति-कॉल ट्रांसक्रिप्शन अनुरोध द्वारा दिए जाने पर भाषा और प्रॉम्प्ट संकेत OpenAI को अग्रेषित किए जाते हैं।

Realtime ट्रांसक्रिप्शन

बंडल किया गया `openai` Plugin Voice Call Plugin के लिए Realtime ट्रांसक्रिप्शन पंजीकृत करता है।

सेटिंग | कॉन्फ़िग पथ | डिफ़ॉल्ट  
---|---|---  
मॉडल | `plugins.entries.voice-call.config.streaming.providers.openai.model` | `gpt-4o-transcribe`  
भाषा | `...openai.language` | (सेट नहीं)  
प्रॉम्प्ट | `...openai.prompt` | (सेट नहीं)  
मौन अवधि | `...openai.silenceDurationMs` | `800`  
VAD थ्रेशोल्ड | `...openai.vadThreshold` | `0.5`  
Auth | `...openai.apiKey`, `OPENAI_API_KEY`, या `openai` OAuth | API कुंजियाँ सीधे कनेक्ट करती हैं; OAuth एक Realtime ट्रांसक्रिप्शन क्लाइंट सीक्रेट जारी करता है  
  
Realtime voice

बंडल किया गया `openai` Plugin Voice Call Plugin के लिए Realtime voice पंजीकृत करता है।

सेटिंग | कॉन्फ़िग पथ | डिफ़ॉल्ट  
---|---|---  
मॉडल | `plugins.entries.voice-call.config.realtime.providers.openai.model` | `gpt-realtime-2`  
आवाज़ | `...openai.voice` | `alloy`  
तापमान (Azure डिप्लॉयमेंट ब्रिज) | `...openai.temperature` | `0.8`  
VAD थ्रेशोल्ड | `...openai.vadThreshold` | `0.5`  
मौन अवधि | `...openai.silenceDurationMs` | `500`  
प्रीफ़िक्स पैडिंग | `...openai.prefixPaddingMs` | `300`  
रीजनिंग प्रयास | `...openai.reasoningEffort` | (सेट नहीं)  
Auth | `openai` API-कुंजी auth प्रोफ़ाइल, `...openai.apiKey`, या `OPENAI_API_KEY` | OpenAI Platform API कुंजी आवश्यक; OpenAI OAuth Realtime voice कॉन्फ़िगर नहीं करता  
  
`gpt-realtime-2` के लिए उपलब्ध बिल्ट-इन Realtime आवाज़ें: `alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`, `shimmer`, `verse`, `marin`, `cedar`। OpenAI सर्वोत्तम Realtime गुणवत्ता के लिए `marin` और `cedar` की अनुशंसा करता है। यह ऊपर की Text-to-speech आवाज़ों से अलग सेट है; यह न मानें कि `fable`, `nova`, या `onyx` जैसी TTS आवाज़ Realtime सेशन के लिए मान्य है।

## Azure OpenAI endpoints

बंडल किया गया `openai` provider base URL override करके image generation के लिए Azure OpenAI resource को target कर सकता है। image-generation path पर, OpenClaw `models.providers.openai.baseUrl` पर Azure hostnames detect करता है और अपने-आप Azure के request shape पर switch करता है।

Azure OpenAI का उपयोग करें जब:

  * आपके पास पहले से Azure OpenAI subscription, quota, या enterprise agreement हो
  * आपको Azure द्वारा दिए जाने वाले regional data residency या compliance controls चाहिए
  * आप traffic को मौजूदा Azure tenancy के अंदर रखना चाहते हों


### Configuration

बंडल किए गए `openai` provider के माध्यम से Azure image generation के लिए, `models.providers.openai.baseUrl` को अपने Azure resource पर point करें और `apiKey` को Azure OpenAI key पर set करें (OpenAI Platform key नहीं):

json5Copy code
[code]
    {  models: {    providers: {      openai: {        baseUrl: "https://<your-resource>.openai.azure.com",        apiKey: "<azure-openai-api-key>",      },    },  },}
[/code]

OpenClaw Azure image-generation route के लिए ये Azure host suffixes पहचानता है:

  * `*.openai.azure.com`
  * `*.services.ai.azure.com`
  * `*.cognitiveservices.azure.com`


पहचाने गए Azure host पर image-generation requests के लिए, OpenClaw:

  * `Authorization: Bearer` के बजाय `api-key` header भेजता है
  * deployment-scoped paths (`/openai/deployments/{deployment}/...`) का उपयोग करता है
  * हर request में `?api-version=...` जोड़ता है
  * Azure image-generation calls के लिए 600s default request timeout का उपयोग करता है। Per-call `timeoutMs` values अब भी इस default को override करती हैं।


अन्य base URLs (public OpenAI, OpenAI-compatible proxies) standard OpenAI image request shape रखते हैं।

### API version

Azure image-generation path के लिए कोई specific Azure preview या GA version pin करने हेतु `AZURE_OPENAI_API_VERSION` set करें:

bashCopy code
[code]
    export AZURE_OPENAI_API_VERSION="2024-12-01-preview"
[/code]

Variable unset होने पर default `2024-12-01-preview` है।

### Model names are deployment names

Azure OpenAI models को deployments से bind करता है। बंडल किए गए `openai` provider के माध्यम से route की गई Azure image-generation requests के लिए, OpenClaw में `model` field वह **Azure deployment name** होना चाहिए जिसे आपने Azure portal में configured किया है, public OpenAI model id नहीं।

यदि आप `gpt-image-2-prod` नाम का deployment बनाते हैं जो `gpt-image-2` serve करता है:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2-prod prompt="A clean poster" size=1024x1024 count=1
[/code]

यही deployment-name rule बंडल किए गए `openai` provider के माध्यम से route की गई image-generation calls पर लागू होता है।

### Regional availability

Azure image generation अभी केवल regions के subset में उपलब्ध है (उदाहरण के लिए `eastus2`, `swedencentral`, `polandcentral`, `westus3`, `uaenorth`)। Deployment बनाने से पहले Microsoft की current region list देखें, और confirm करें कि specific model आपके region में offered है।

### Parameter differences

Azure OpenAI और public OpenAI हमेशा समान image parameters accept नहीं करते। Azure उन options को reject कर सकता है जिन्हें public OpenAI allow करता है (उदाहरण के लिए `gpt-image-2` पर कुछ `background` values) या उन्हें केवल specific model versions पर expose कर सकता है। ये differences Azure और underlying model से आते हैं, OpenClaw से नहीं। यदि कोई Azure request validation error के साथ fail होती है, तो Azure portal में अपने specific deployment और API version द्वारा supported parameter set देखें।

## Advanced configuration

Transport (WebSocket vs SSE)

OpenClaw `openai/*` के लिए SSE fallback (`"auto"`) के साथ WebSocket-first का उपयोग करता है।

`"auto"` mode में, OpenClaw:

  * SSE पर fallback करने से पहले एक early WebSocket failure retry करता है
  * Failure के बाद, WebSocket को ~60 seconds के लिए degraded mark करता है और cool-down के दौरान SSE उपयोग करता है
  * Retries और reconnects के लिए stable session और turn identity headers attach करता है
  * Transport variants में usage counters (`input_tokens` / `prompt_tokens`) normalize करता है


Value | Behavior  
---|---  
`"auto"` (default) | पहले WebSocket, SSE fallback  
`"sse"` | केवल SSE force करें  
`"websocket"` | केवल WebSocket force करें  
  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: { transport: "auto" },        },      },    },  },}
[/code]

संबंधित OpenAI docs:

  * [WebSocket के साथ Realtime API](<https://platform.openai.com/docs/guides/realtime-websocket>)
  * [Streaming API responses (SSE)](<https://platform.openai.com/docs/guides/streaming-responses>)

Fast mode

OpenClaw `openai/*` के लिए shared fast-mode toggle expose करता है:

  * **Chat/UI:** `/fast status|auto|on|off`
  * **Config:** `agents.defaults.models["<provider>/<model>"].params.fastMode`


Enabled होने पर, OpenClaw fast mode को OpenAI priority processing (`service_tier = "priority"`) पर map करता है। मौजूदा `service_tier` values preserve रहती हैं, और fast mode `reasoning` या `text.verbosity` को rewrite नहीं करता। `fastMode: "auto"` auto cutoff तक new model calls fast शुरू करता है, फिर बाद की retry, fallback, tool-result, या continuation calls को fast mode के बिना शुरू करता है। Cutoff default 60 seconds है; इसे बदलने के लिए active model पर `params.fastAutoOnSeconds` set करें।

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": { params: { fastMode: "auto", fastAutoOnSeconds: 30 } },      },    },  },}
[/code]

Priority processing (service_tier)

OpenAI की API `service_tier` के माध्यम से priority processing expose करती है। OpenClaw में इसे per model set करें:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": { params: { serviceTier: "priority" } },      },    },  },}
[/code]

Supported values: `auto`, `default`, `flex`, `priority`.

Server-side compaction (Responses API)

Direct OpenAI Responses models (`openai/*` on `api.openai.com`) के लिए, OpenAI plugin का OpenClaw stream wrapper server-side compaction auto-enable करता है:

  * `store: true` force करता है (जब तक model compat `supportsStore: false` set न करे)
  * `context_management: [{ type: "compaction", compact_threshold: ... }]` inject करता है
  * Default `compact_threshold`: `contextWindow` का 70% (या unavailable होने पर `80000`)


यह built-in OpenClaw runtime path और embedded runs द्वारा उपयोग किए गए OpenAI provider hooks पर लागू होता है। Native Codex app-server harness अपना context Codex के माध्यम से खुद manage करता है और OpenAI के default agent route या provider/model runtime policy द्वारा configured होता है।

### Enable explicitly

Azure OpenAI Responses जैसे compatible endpoints के लिए उपयोगी:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "azure-openai-responses/gpt-5.5": {          params: { responsesServerCompaction: true },        },      },    },  },}
[/code]

### Custom threshold

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: {            responsesServerCompaction: true,            responsesCompactThreshold: 120000,          },        },      },    },  },}
[/code]

### Disable

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: { responsesServerCompaction: false },        },      },    },  },}
[/code]

Strict-agentic GPT mode

`openai/*` पर GPT-5-family runs के लिए, OpenClaw एक stricter embedded execution contract का उपयोग कर सकता है:

json5Copy code
[code]
    {  agents: {    defaults: {      embeddedAgent: { executionContract: "strict-agentic" },    },  },}
[/code]

`strict-agentic` के साथ, OpenClaw:

  * substantial work के लिए `update_plan` auto-enable करता है
  * structurally empty या reasoning-only turns को visible-answer continuation के साथ retry करता है
  * selected harness द्वारा provide किए जाने पर explicit harness plan events का उपयोग करता है


OpenClaw यह decide करने के लिए assistant prose classify नहीं करता कि कोई turn plan है, progress update है, या final answer है।

Native vs OpenAI-compatible routes

OpenClaw direct OpenAI, Codex, और Azure OpenAI endpoints को generic OpenAI-compatible `/v1` proxies से अलग तरह से treat करता है:

**Native routes** (`openai/*`, Azure OpenAI):

  * केवल उन models के लिए `reasoning: { effort: "none" }` रखता है जो OpenAI `none` effort support करते हैं
  * उन models या proxies के लिए disabled reasoning omit करता है जो `reasoning.effort: "none"` reject करते हैं
  * Tool schemas को default रूप से strict mode में रखता है
  * केवल verified native hosts पर hidden attribution headers attach करता है
  * OpenAI-only request shaping (`service_tier`, `store`, reasoning-compat, prompt-cache hints) रखता है


**प्रॉक्सी/संगत रूट:**

  * अधिक ढीला संगत व्यवहार उपयोग करें
  * गैर-नेटिव `openai-completions` पेलोड से Completions `store` हटाएं
  * OpenAI-संगत Completions प्रॉक्सी के लिए उन्नत `params.extra_body`/`params.extraBody` पास-थ्रू JSON स्वीकार करें
  * vLLM जैसे OpenAI-संगत Completions प्रॉक्सी के लिए `params.chat_template_kwargs` स्वीकार करें
  * सख्त टूल स्कीमा या केवल-नेटिव हेडर बाध्य न करें


Azure OpenAI नेटिव ट्रांसपोर्ट और संगत व्यवहार का उपयोग करता है, लेकिन उसे छिपे हुए एट्रिब्यूशन हेडर नहीं मिलते।

## संबंधित

[**मॉडल चयन** प्रदाता, मॉडल रेफ़ और फ़ेलओवर व्यवहार चुनना। ](</hi/concepts/model-providers>) [**छवि जनरेशन** साझा छवि टूल पैरामीटर और प्रदाता चयन। ](</hi/tools/image-generation>) [**वीडियो जनरेशन** साझा वीडियो टूल पैरामीटर और प्रदाता चयन। ](</hi/tools/video-generation>) [**OAuth और auth** auth विवरण और क्रेडेंशियल पुन: उपयोग नियम। ](</hi/gateway/authentication>)

Was this useful?YesNo

Open issue