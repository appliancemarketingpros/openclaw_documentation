---
title: मॉडल CLI
source_url: https://docs.openclaw.ai/hi/concepts/models
scraped_at: 2026-06-29
---

ModelsConcepts and configuration

[**मॉडल फेलओवर** प्रमाणीकरण प्रोफ़ाइल रोटेशन, कूलडाउन, और यह फॉलबैक के साथ कैसे इंटरैक्ट करता है। ](</hi/concepts/model-failover>) [**मॉडल प्रदाता** त्वरित प्रदाता अवलोकन और उदाहरण। ](</hi/concepts/model-providers>) [**एजेंट रनटाइम** OpenClaw, Codex, और अन्य एजेंट लूप रनटाइम। ](</hi/concepts/agent-runtimes>) [**कॉन्फ़िगरेशन संदर्भ** मॉडल कॉन्फ़िग कुंजियाँ। ](</hi/gateway/config-agents#agent-defaults>)

मॉडल रेफ्स एक प्रदाता और मॉडल चुनते हैं। वे आम तौर पर निम्न-स्तरीय एजेंट रनटाइम नहीं चुनते। OpenAI एजेंट रेफ्स मुख्य अपवाद हैं: `openai/gpt-5.5` आधिकारिक OpenAI प्रदाता पर डिफ़ॉल्ट रूप से Codex ऐप-सर्वर रनटाइम के माध्यम से चलता है। सब्सक्रिप्शन Copilot रेफ्स (`github-copilot/*`) को अतिरिक्त रूप से बाहरी GitHub Copilot एजेंट रनटाइम Plugin में चुना जा सकता है — वह पथ स्पष्ट रहता है (कोई `auto` फॉलबैक नहीं)। स्पष्ट रनटाइम ओवरराइड पूरे एजेंट या सत्र पर नहीं, बल्कि प्रदाता/मॉडल नीति पर होने चाहिए। Codex रनटाइम मोड में, `openai/gpt-*` रेफ API-कुंजी बिलिंग का संकेत नहीं देता; प्रमाणीकरण Codex खाते या `openai` OAuth प्रोफ़ाइल से आ सकता है। [एजेंट रनटाइम](</hi/concepts/agent-runtimes>) और [GitHub Copilot एजेंट रनटाइम](</hi/plugins/copilot>) देखें।

## मॉडल चयन कैसे काम करता है

OpenClaw इस क्रम में मॉडल चुनता है:

* ### प्राथमिक मॉडल

`agents.defaults.model.primary` (या `agents.defaults.model`)।

* ### फॉलबैक

`agents.defaults.model.fallbacks` (क्रम में)।

* ### प्रदाता प्रमाणीकरण फेलओवर

अगले मॉडल पर जाने से पहले प्रमाणीकरण फेलओवर प्रदाता के भीतर होता है।

संबंधित मॉडल सतहें

  * `agents.defaults.models` उन मॉडलों की अनुमति-सूची/कैटलॉग है जिनका OpenClaw उपयोग कर सकता है (साथ में उपनाम)। प्रदाता खोज को डायनेमिक रखते हुए दिखाई देने वाले प्रदाताओं को सीमित करने के लिए `provider/*` प्रविष्टियों का उपयोग करें।
  * `agents.defaults.imageModel` का उपयोग **केवल तब** होता है जब प्राथमिक मॉडल छवियाँ स्वीकार नहीं कर सकता।
  * `agents.defaults.pdfModel` का उपयोग `pdf` टूल द्वारा किया जाता है। यदि छोड़ा गया हो, तो टूल पहले `agents.defaults.imageModel` पर, फिर हल किए गए सत्र/डिफ़ॉल्ट मॉडल पर फॉलबैक करता है।
  * `agents.defaults.imageGenerationModel` का उपयोग साझा इमेज-जनरेशन क्षमता द्वारा किया जाता है। यदि छोड़ा गया हो, तो `image_generate` फिर भी प्रमाणीकरण-समर्थित प्रदाता डिफ़ॉल्ट का अनुमान लगा सकता है। यह पहले मौजूदा डिफ़ॉल्ट प्रदाता को आज़माता है, फिर शेष पंजीकृत इमेज-जनरेशन प्रदाताओं को प्रदाता-ID क्रम में। यदि आप कोई विशिष्ट प्रदाता/मॉडल सेट करते हैं, तो उस प्रदाता का प्रमाणीकरण/API कुंजी भी कॉन्फ़िगर करें।
  * `agents.defaults.musicGenerationModel` का उपयोग साझा म्यूज़िक-जनरेशन क्षमता द्वारा किया जाता है। यदि छोड़ा गया हो, तो `music_generate` फिर भी प्रमाणीकरण-समर्थित प्रदाता डिफ़ॉल्ट का अनुमान लगा सकता है। यह पहले मौजूदा डिफ़ॉल्ट प्रदाता को आज़माता है, फिर शेष पंजीकृत म्यूज़िक-जनरेशन प्रदाताओं को प्रदाता-ID क्रम में। यदि आप कोई विशिष्ट प्रदाता/मॉडल सेट करते हैं, तो उस प्रदाता का प्रमाणीकरण/API कुंजी भी कॉन्फ़िगर करें।
  * `agents.defaults.videoGenerationModel` का उपयोग साझा वीडियो-जनरेशन क्षमता द्वारा किया जाता है। यदि छोड़ा गया हो, तो `video_generate` फिर भी प्रमाणीकरण-समर्थित प्रदाता डिफ़ॉल्ट का अनुमान लगा सकता है। यह पहले मौजूदा डिफ़ॉल्ट प्रदाता को आज़माता है, फिर शेष पंजीकृत वीडियो-जनरेशन प्रदाताओं को प्रदाता-ID क्रम में। यदि आप कोई विशिष्ट प्रदाता/मॉडल सेट करते हैं, तो उस प्रदाता का प्रमाणीकरण/API कुंजी भी कॉन्फ़िगर करें।
  * प्रति-एजेंट डिफ़ॉल्ट, बाइंडिंग्स के साथ `agents.list[].model` के ज़रिए `agents.defaults.model` को ओवरराइड कर सकते हैं ([मल्टी-एजेंट रूटिंग](</hi/concepts/multi-agent>) देखें)।


## चयन स्रोत और फॉलबैक व्यवहार

वही `provider/model` इस पर निर्भर करते हुए अलग-अलग अर्थ रख सकता है कि वह कहाँ से आया है:

  * कॉन्फ़िगर किए गए डिफ़ॉल्ट (`agents.defaults.model.primary` और एजेंट-विशिष्ट प्राथमिक) सामान्य शुरुआती बिंदु हैं और `agents.defaults.model.fallbacks` का उपयोग करते हैं।
  * ऑटो फॉलबैक चयन अस्थायी रिकवरी स्थिति हैं। उन्हें `modelOverrideSource: "auto"` के साथ संग्रहीत किया जाता है ताकि बाद के टर्न हर बार ज्ञात-खराब प्राथमिक की जाँच किए बिना फॉलबैक श्रृंखला का उपयोग जारी रख सकें; OpenClaw समय-समय पर मूल प्राथमिक को फिर से जाँचता है, रिकवर होने पर ऑटो चयन साफ़ करता है, और फॉलबैक/रिकवरी संक्रमणों की घोषणा प्रत्येक स्थिति परिवर्तन पर एक बार करता है।
  * उपयोगकर्ता सत्र चयन सटीक होते हैं। `/model`, मॉडल पिकर, `session_status(model=...)`, और `sessions.patch` `modelOverrideSource: "user"` संग्रहीत करते हैं; यदि वह चुना गया प्रदाता/मॉडल पहुँच योग्य नहीं है, तो OpenClaw किसी अन्य कॉन्फ़िगर किए गए मॉडल पर जाने के बजाय स्पष्ट रूप से विफल होता है।
  * `agents.defaults.model.primary` बदलने से मौजूदा सत्र चयन फिर से नहीं लिखे जाते। यदि स्थिति कहती है `This session is pinned to X; config primary Y will apply to new/unpinned sessions.`, तो मौजूदा सत्र चयन को `/model default` से साफ़ करें ताकि वह फिर से कॉन्फ़िगर किए गए प्राथमिक को विरासत में ले।
  * Cron `--model` / पेलोड `model` प्रति-जॉब प्राथमिक है। यह फिर भी कॉन्फ़िगर किए गए फॉलबैक का उपयोग करता है, जब तक कि जॉब स्पष्ट पेलोड `fallbacks` न दे (`fallbacks: []` का उपयोग सख़्त cron रन के लिए करें)।
  * CLI डिफ़ॉल्ट-मॉडल और अनुमति-सूची पिकर, पूरे बिल्ट-इन कैटलॉग को लोड करने के बजाय स्पष्ट `models.providers.*.models` सूचीबद्ध करके `models.mode: "replace"` का सम्मान करते हैं।
  * Control UI मॉडल पिकर Gateway से उसका कॉन्फ़िगर किया गया मॉडल व्यू पूछता है: मौजूद होने पर `agents.defaults.models`, जिसमें प्रदाता-व्यापी `provider/*` प्रविष्टियाँ शामिल हैं, अन्यथा स्पष्ट `models.providers.*.models` और उपयोगी प्रमाणीकरण वाले प्रदाता। पूरा बिल्ट-इन कैटलॉग स्पष्ट ब्राउज़ व्यू जैसे `models.list` के साथ `view: "all"` या `openclaw models list --all` के लिए आरक्षित है।


## त्वरित मॉडल नीति

  * अपना प्राथमिक मॉडल आपके लिए उपलब्ध सबसे मजबूत नवीनतम-पीढ़ी के मॉडल पर सेट करें।
  * लागत/विलंब-संवेदनशील कार्यों और कम-जोखिम चैट के लिए फॉलबैक का उपयोग करें।
  * टूल-सक्षम एजेंटों या अविश्वसनीय इनपुट के लिए, पुराने/कमज़ोर मॉडल टियर से बचें।


## ऑनबोर्डिंग (अनुशंसित)

यदि आप कॉन्फ़िग हाथ से संपादित नहीं करना चाहते, तो ऑनबोर्डिंग चलाएँ:

bashCopy code
[code]
    openclaw onboard
[/code]

यह सामान्य प्रदाताओं के लिए मॉडल + प्रमाणीकरण सेट कर सकता है, जिसमें **OpenAI Code (Codex) सब्सक्रिप्शन** (OAuth) और **Anthropic** (API कुंजी या Claude CLI) शामिल हैं।

## कॉन्फ़िग कुंजियाँ (अवलोकन)

  * `agents.defaults.model.primary` और `agents.defaults.model.fallbacks`
  * `agents.defaults.imageModel.primary` और `agents.defaults.imageModel.fallbacks`
  * `agents.defaults.pdfModel.primary` और `agents.defaults.pdfModel.fallbacks`
  * `agents.defaults.imageGenerationModel.primary` और `agents.defaults.imageGenerationModel.fallbacks`
  * `agents.defaults.videoGenerationModel.primary` और `agents.defaults.videoGenerationModel.fallbacks`
  * `agents.defaults.models` (अनुमति-सूची + उपनाम + प्रदाता पैरामीटर + `provider/*` डायनेमिक प्रदाता प्रविष्टियाँ)
  * `models.providers` (`models.json` में लिखे गए कस्टम प्रदाता)


### सुरक्षित अनुमति-सूची संपादन

`agents.defaults.models` को हाथ से अपडेट करते समय एडिटिव राइट्स का उपयोग करें:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --merge
[/code]

क्लॉबर सुरक्षा नियम

`openclaw config set` मॉडल/प्रदाता मैप्स को आकस्मिक क्लॉबर से बचाता है। `agents.defaults.models`, `models.providers`, या `models.providers.<id>.models` को साधारण ऑब्जेक्ट असाइनमेंट अस्वीकार किया जाता है जब वह मौजूदा प्रविष्टियाँ हटा देगा। एडिटिव बदलावों के लिए `--merge` का उपयोग करें; `--replace` का उपयोग केवल तब करें जब दिया गया मान पूरा लक्ष्य मान बनना चाहिए।

इंटरैक्टिव प्रदाता सेटअप और `openclaw configure --section model` भी प्रदाता-स्कोप किए गए चयनों को मौजूदा अनुमति-सूची में मर्ज करते हैं, इसलिए Codex, Ollama, या कोई अन्य प्रदाता जोड़ने से असंबंधित मॉडल प्रविष्टियाँ नहीं हटतीं। प्रदाता प्रमाणीकरण फिर से लागू होने पर Configure मौजूदा `agents.defaults.model.primary` को सुरक्षित रखता है। स्पष्ट डिफ़ॉल्ट-सेटिंग कमांड जैसे `openclaw models auth login --provider <id> --set-default` और `openclaw models set <model>` फिर भी `agents.defaults.model.primary` को बदलते हैं।

## "मॉडल की अनुमति नहीं है" (और उत्तर क्यों रुकते हैं)

यदि `agents.defaults.models` सेट है, तो यह `/model` और सत्र ओवरराइड के लिए **अनुमति-सूची** बन जाता है। जब कोई उपयोगकर्ता ऐसा मॉडल चुनता है जो उस अनुमति-सूची में नहीं है, तो OpenClaw लौटाता है:

CodeCopy code
[code]
    Model "provider/model" is not allowed. Use /models to list providers, or /models <provider> to list models.Add it with: openclaw config set agents.defaults.models '{"provider/model":{}}' --strict-json --merge
[/code]

जब अस्वीकृत कमांड में `/model openai/gpt-5.5 --runtime codex` जैसा रनटाइम ओवरराइड शामिल हो, तो पहले अनुमति-सूची ठीक करें, फिर वही `/model ... --runtime ...` कमांड दोबारा चलाएँ। नेटिव Codex निष्पादन के लिए, चुना गया मॉडल फिर भी `openai/gpt-5.5` है; `codex` रनटाइम हार्नेस चुनता है और Codex प्रमाणीकरण को अलग से उपयोग करता है।

स्थानीय/GGUF मॉडलों के लिए, अनुमति-सूची में पूरा प्रदाता-प्रीफ़िक्स वाला रेफ संग्रहीत करें, उदाहरण के लिए `ollama/gemma4:26b`, `lmstudio/Gemma4-26b-a4-it-gguf`, या `openclaw models list --provider <provider>` द्वारा दिखाया गया सटीक प्रदाता/मॉडल। जब अनुमति-सूची सक्रिय हो, तो केवल स्थानीय फ़ाइलनाम या डिस्प्ले नाम पर्याप्त नहीं होते।

यदि आप हर मॉडल को हाथ से सूचीबद्ध किए बिना प्रदाताओं को सीमित करना चाहते हैं, तो `provider/*` प्रविष्टियाँ `agents.defaults.models` में जोड़ें:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/*": {},        "vllm/*": {},      },    },  },}
[/code]

उस नीति के साथ, `/model`, `/models`, और मॉडल पिकर केवल उन प्रदाताओं के लिए खोजा गया कैटलॉग दिखाते हैं। चुने गए प्रदाताओं से नए मॉडल अनुमति-सूची संपादित किए बिना दिखाई दे सकते हैं। जब आपको किसी दूसरे प्रदाता से एक विशिष्ट मॉडल चाहिए, तो सटीक `provider/model` प्रविष्टियों को `provider/*` प्रविष्टियों के साथ मिलाया जा सकता है।

उदाहरण अनुमति-सूची कॉन्फ़िग:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-sonnet-4-6" },      models: {        "anthropic/claude-sonnet-4-6": { alias: "Sonnet" },        "anthropic/claude-opus-4-6": { alias: "Opus" },      },    },  },}
[/code]

## चैट में मॉडल बदलना (`/model`)

आप पुनरारंभ किए बिना मौजूदा सत्र के लिए मॉडल बदल सकते हैं:

CodeCopy code
[code]
    /model/model list/model 3/model openai/gpt-5.4/model default/model status
[/code]

पिकर व्यवहार

  * `/model` (और `/model list`) एक कॉम्पैक्ट, क्रमांकित पिकर है (मॉडल परिवार + उपलब्ध प्रदाता)।
  * Discord पर, `/model` और `/models` प्रदाता और मॉडल ड्रॉपडाउन तथा Submit चरण के साथ एक इंटरैक्टिव पिकर खोलते हैं।
  * Telegram पर, `/models` पिकर चयन सत्र-स्कोप होते हैं; वे `openclaw.json` में एजेंट का स्थायी डिफ़ॉल्ट नहीं बदलते।
  * `/models add` अप्रचलित है और अब चैट से मॉडल पंजीकृत करने के बजाय अप्रचलन संदेश लौटाता है।
  * `/model <#>` उस पिकर से चयन करता है।

स्थायित्व और लाइव स्विचिंग

  * `/model` नया सत्र चयन तुरंत कायम रखता है।
  * यदि agent निष्क्रिय है, तो अगला run नया मॉडल तुरंत उपयोग करता है।
  * यदि कोई run पहले से सक्रिय है, तो OpenClaw लाइव स्विच को pending के रूप में चिह्नित करता है और केवल साफ़ retry point पर नए मॉडल में पुनः आरंभ करता है।
  * यदि tool गतिविधि या reply output पहले ही शुरू हो चुका है, तो pending switch बाद के retry अवसर या अगले user turn तक queued रह सकता है।
  * `/model default` सत्र चयन साफ़ करता है और सत्र को कॉन्फ़िगर किए गए default मॉडल पर वापस ले जाता है।
  * user-selected `/model` ref उस सत्र के लिए strict होता है: यदि चयनित provider/model पहुँच योग्य नहीं है, तो reply `agents.defaults.model.fallbacks` से चुपचाप उत्तर देने के बजाय स्पष्ट रूप से fail होता है। यह configured defaults और cron job primaries से अलग है, जो अभी भी fallback chains उपयोग कर सकते हैं।
  * `/model status` विस्तृत view है (auth candidates और, कॉन्फ़िगर होने पर, provider endpoint `baseUrl` \+ `api` mode).

Ref parsing

  * Model refs को **पहले** `/` पर split करके parse किया जाता है। `/model <ref>` type करते समय `provider/model` उपयोग करें।
  * यदि model ID में स्वयं `/` शामिल है (OpenRouter-style), तो आपको provider prefix शामिल करना होगा (उदाहरण: `/model openrouter/moonshotai/kimi-k2`)।
  * यदि आप provider छोड़ देते हैं, तो OpenClaw input को इस क्रम में resolve करता है: 
    1. alias match
    2. उस exact unprefixed model id के लिए unique configured-provider match
    3. configured default provider पर deprecated fallback — यदि वह provider अब configured default model expose नहीं करता, तो OpenClaw stale removed-provider default दिखाने से बचने के लिए पहले configured provider/model पर fallback करता है।


पूर्ण command behavior/config: [Slash commands](</hi/tools/slash-commands>).

## CLI commands

bashCopy code
[code]
    openclaw models listopenclaw models statusopenclaw models set <provider/model>openclaw models set-image <provider/model> openclaw models aliases listopenclaw models aliases add <alias> <provider/model>openclaw models aliases remove <alias> openclaw models fallbacks listopenclaw models fallbacks add <provider/model>openclaw models fallbacks remove <provider/model>openclaw models fallbacks clear openclaw models image-fallbacks listopenclaw models image-fallbacks add <provider/model>openclaw models image-fallbacks remove <provider/model>openclaw models image-fallbacks clear
[/code]

`openclaw models` (बिना subcommand) `models status` के लिए shortcut है।

### `models list`

Default रूप से configured/auth-available models दिखाता है। उपयोगी flags:

पूरा catalog। Auth configure होने से पहले bundled provider-owned static catalog rows शामिल करता है, इसलिए discovery-only views ऐसे models दिखा सकते हैं जो matching provider credentials जोड़ने तक unavailable होते हैं।

केवल local providers।

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcHJvdmlkZXIgPGlk " type="string"> Provider id से filter करें, उदाहरण के लिए `moonshot`। Interactive pickers से display labels स्वीकार नहीं किए जाते।

प्रति line एक model।

Machine-readable output।

### `models status`

Resolved primary model, fallbacks, image model, और configured providers का auth overview दिखाता है। यह auth store में मिले profiles के लिए OAuth expiry status भी दिखाता है (default रूप से 24h के भीतर चेतावनी देता है)। `--plain` केवल resolved primary model print करता है।

Auth और probe behavior

  * OAuth status हमेशा दिखाया जाता है (और `--json` output में शामिल होता है)। यदि configured provider के पास credentials नहीं हैं, तो `models status` **Missing auth** section print करता है।
  * JSON में `auth.oauth` (warn window + profiles) और `auth.providers` (प्रति provider effective auth, env-backed credentials सहित) शामिल हैं। `auth.oauth` केवल auth-store profile health है; env-only providers वहाँ दिखाई नहीं देते।
  * Automation के लिए `--check` उपयोग करें (missing/expired होने पर exit `1`, expiring होने पर `2`)।
  * Live auth checks के लिए `--probe` उपयोग करें; probe rows auth profiles, env credentials, या `models.json` से आ सकती हैं।
  * यदि explicit `auth.order.<provider>` stored profile को छोड़ देता है, तो probe उसे try करने के बजाय `excluded_by_auth_order` report करता है। यदि auth मौजूद है लेकिन उस provider के लिए कोई probeable model resolve नहीं किया जा सकता, तो probe `status: no_model` report करता है।


उदाहरण (Claude CLI):

bashCopy code
[code]
    claude auth loginopenclaw models status
[/code]

## Scanning (OpenRouter free models)

`openclaw models scan` OpenRouter के **free model catalog** की जाँच करता है और वैकल्पिक रूप से tool और image support के लिए models probe कर सकता है।

Live probes छोड़ें (केवल metadata)।

`agents.defaults.model.primary` को first selection पर set करें।

`agents.defaults.imageModel.primary` को first image selection पर set करें।

Scan results इस आधार पर ranked होते हैं:

  1. Image support
  2. Tool latency
  3. Context size
  4. Parameter count


Input:

  * OpenRouter `/models` list (filter `:free`)
  * Live probes के लिए auth profiles या `OPENROUTER_API_KEY` से OpenRouter API key चाहिए (देखें [Environment variables](</hi/help/environment>))
  * Optional filters: `--max-age-days`, `--min-params`, `--provider`, `--max-candidates`
  * Request/probe controls: `--timeout`, `--concurrency`


जब live probes TTY में चलते हैं, तो आप fallbacks interactively select कर सकते हैं। Non-interactive mode में, defaults स्वीकार करने के लिए `--yes` pass करें। Metadata-only results informational हैं; `--set-default` और `--set-image` के लिए live probes चाहिए ताकि OpenClaw unusable keyless OpenRouter model configure न करे।

## Models registry (`models.json`)

`models.providers` में custom providers agent directory के अंतर्गत `models.json` में लिखे जाते हैं (default `~/.openclaw/agents/<agentId>/agent/models.json`)। Provider-plugin catalogs agent की plugin state के अंतर्गत generated plugin-owned catalog shards के रूप में stored होते हैं और automatically load होते हैं। यह file default रूप से merge होती है जब तक `models.mode` को `replace` पर set न किया गया हो।

Merge mode precedence

Matching provider IDs के लिए merge mode precedence:

  * Agent `models.json` में पहले से मौजूद non-empty `baseUrl` जीतता है।
  * Agent `models.json` में non-empty `apiKey` केवल तब जीतता है जब वह provider current config/auth-profile context में SecretRef-managed नहीं है।
  * SecretRef-managed provider `apiKey` values resolved secrets persist करने के बजाय source markers (env refs के लिए `ENV_VAR_NAME`, file/exec refs के लिए `secretref-managed`) से refresh होती हैं।
  * SecretRef-managed provider header values source markers (env refs के लिए `secretref-env:ENV_VAR_NAME`, file/exec refs के लिए `secretref-managed`) से refresh होती हैं।
  * Empty या missing agent `apiKey`/`baseUrl` config `models.providers` पर fall back करते हैं।
  * अन्य provider fields config और normalized catalog data से refresh होते हैं।


## संबंधित

  * [Agent runtimes](</hi/concepts/agent-runtimes>) — OpenClaw, Codex, और अन्य agent loop runtimes
  * [Configuration reference](</hi/gateway/config-agents#agent-defaults>) — model config keys
  * [Image generation](</hi/tools/image-generation>) — image model configuration
  * [Model failover](</hi/concepts/model-failover>) — fallback chains
  * [Model providers](</hi/concepts/model-providers>) — provider routing और auth
  * [Music generation](</hi/tools/music-generation>) — music model configuration
  * [Video generation](</hi/tools/video-generation>) — video model configuration


Was this useful?YesNo

Open issue