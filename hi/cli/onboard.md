---
title: आरंभ करें
source_url: https://docs.openclaw.ai/hi/cli/onboard
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw onboard`

स्थानीय या रिमोट Gateway सेटअप के लिए पूरा निर्देशित ऑनबोर्डिंग। इसका उपयोग तब करें जब आप चाहते हैं कि OpenClaw एक ही प्रवाह में मॉडल प्रमाणीकरण, कार्यस्थान, Gateway, चैनल, Skills, और स्वास्थ्य जांच से होकर गुजारे।

## संबंधित गाइड

[**CLI ऑनबोर्डिंग हब** इंटरैक्टिव CLI प्रवाह का वॉकथ्रू। ](</hi/start/wizard>) [**ऑनबोर्डिंग अवलोकन** OpenClaw ऑनबोर्डिंग कैसे एक साथ फिट होती है। ](</hi/start/onboarding-overview>) [**CLI सेटअप संदर्भ** आउटपुट, आंतरिक विवरण, और प्रति-चरण व्यवहार। ](</hi/start/wizard-cli-reference>) [**CLI ऑटोमेशन** गैर-इंटरैक्टिव फ्लैग और स्क्रिप्टेड सेटअप। ](</hi/start/wizard-cli-automation>) [**macOS ऐप ऑनबोर्डिंग** macOS मेनू बार ऐप के लिए ऑनबोर्डिंग प्रवाह। ](</hi/start/onboarding>)

## उदाहरण

bashCopy code
[code]
    openclaw onboardopenclaw onboard --modernopenclaw onboard --flow quickstartopenclaw onboard --flow manualopenclaw onboard --flow importopenclaw onboard --import-from hermes --import-source ~/.hermesopenclaw onboard --skip-bootstrapopenclaw onboard --mode remote --remote-url wss://gateway-host:18789
[/code]

`--flow import` Hermes जैसे Plugin-स्वामित्व वाले माइग्रेशन प्रदाताओं का उपयोग करता है। यह केवल नए OpenClaw सेटअप पर चलता है; यदि मौजूदा कॉन्फिग, क्रेडेंशियल, सेशन, या कार्यस्थान मेमोरी/पहचान फाइलें मौजूद हैं, तो आयात करने से पहले रीसेट करें या नया सेटअप चुनें।

`--modern` Crestodian संवादात्मक ऑनबोर्डिंग पूर्वावलोकन शुरू करता है। `--modern` के बिना, `openclaw onboard` क्लासिक ऑनबोर्डिंग प्रवाह रखता है।

नए इंस्टॉल पर, जहां सक्रिय कॉन्फिग फाइल गायब है या उसमें कोई लिखी गई सेटिंग नहीं है (खाली या केवल मेटाडेटा), केवल `openclaw` भी क्लासिक ऑनबोर्डिंग प्रवाह शुरू करता है। एक बार कॉन्फिग फाइल में लिखी गई सेटिंग हो जाने पर, केवल `openclaw` इसके बजाय Crestodian खोलता है।

Plaintext `ws://` loopback, निजी IP literals, `.local`, और Tailnet `*.ts.net` Gateway URL के लिए स्वीकार किया जाता है। अन्य विश्वसनीय निजी-DNS नामों के लिए, ऑनबोर्डिंग प्रक्रिया वातावरण में `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` सेट करें।

## लोकेल

इंटरैक्टिव ऑनबोर्डिंग स्थिर सेटअप कॉपी के लिए CLI विजार्ड लोकेल का उपयोग करती है। समाधान क्रम है:

  1. `OPENCLAW_LOCALE`
  2. `LC_ALL`
  3. `LC_MESSAGES`
  4. `LANG`
  5. अंग्रेज़ी फॉलबैक


समर्थित विजार्ड लोकेल `en`, `zh-CN`, और `zh-TW` हैं। लोकेल मान अंडरस्कोर या POSIX suffix रूपों जैसे `zh_CN.UTF-8` का उपयोग कर सकते हैं। उत्पाद नाम, कमांड नाम, कॉन्फिग कुंजियां, URL, provider ID, model ID, और plugin/channel लेबल शाब्दिक रहते हैं।

उदाहरण:

bashCopy code
[code]
    OPENCLAW_LOCALE=zh-CN openclaw onboard
[/code]

गैर-इंटरैक्टिव कस्टम प्रदाता:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --secret-input-mode plaintext \  --custom-compatibility openai \  --custom-image-input
[/code]

`--custom-api-key` गैर-इंटरैक्टिव मोड में वैकल्पिक है। यदि छोड़ा गया है, तो ऑनबोर्डिंग `CUSTOM_API_KEY` जांचती है। OpenClaw सामान्य vision model ID को स्वतः image-capable के रूप में चिह्नित करता है। अज्ञात कस्टम vision ID के लिए `--custom-image-input` पास करें, या केवल-पाठ मेटाडेटा बाध्य करने के लिए `--custom-text-input`। OpenAI-compatible endpoints के लिए `--custom-compatibility openai-responses` उपयोग करें जो `/v1/responses` का समर्थन करते हैं लेकिन `/v1/chat/completions` का नहीं।

LM Studio गैर-इंटरैक्टिव मोड में प्रदाता-विशिष्ट कुंजी फ्लैग का भी समर्थन करता है:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice lmstudio \  --custom-base-url "http://localhost:1234/v1" \  --custom-model-id "qwen/qwen3.5-9b" \  --lmstudio-api-key "$LM_API_TOKEN" \  --accept-risk
[/code]

गैर-इंटरैक्टिव Ollama:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice ollama \  --custom-base-url "http://ollama-host:11434" \  --custom-model-id "qwen3.5:27b" \  --accept-risk
[/code]

`--custom-base-url` का डिफॉल्ट `http://127.0.0.1:11434` है। `--custom-model-id` वैकल्पिक है; यदि छोड़ा गया है, तो ऑनबोर्डिंग Ollama के सुझाए गए डिफॉल्ट का उपयोग करती है। `kimi-k2.5:cloud` जैसे cloud model ID भी यहां काम करते हैं।

प्रदाता कुंजियों को plaintext के बजाय refs के रूप में संग्रहित करें:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

`--secret-input-mode ref` के साथ, ऑनबोर्डिंग plaintext key values के बजाय env-backed refs लिखती है। auth-profile backed providers के लिए यह `keyRef` प्रविष्टियां लिखता है; custom providers के लिए यह `models.providers.<id>.apiKey` को env ref के रूप में लिखता है (उदाहरण के लिए `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`)।

गैर-इंटरैक्टिव `ref` मोड अनुबंध:

  * ऑनबोर्डिंग प्रक्रिया वातावरण में प्रदाता env var सेट करें (उदाहरण के लिए `OPENAI_API_KEY`)।
  * inline key flags पास न करें (उदाहरण के लिए `--openai-api-key`) जब तक कि वह env var भी सेट न हो।
  * यदि आवश्यक env var के बिना inline key flag पास किया जाता है, तो ऑनबोर्डिंग मार्गदर्शन के साथ तुरंत विफल होती है।


गैर-इंटरैक्टिव मोड में Gateway token विकल्प:

  * `--gateway-auth token --gateway-token <token>` plaintext token संग्रहित करता है।
  * `--gateway-auth token --gateway-token-ref-env <name>` `gateway.auth.token` को env SecretRef के रूप में संग्रहित करता है।
  * `--gateway-token` और `--gateway-token-ref-env` परस्पर अनन्य हैं।
  * `--gateway-token-ref-env` को ऑनबोर्डिंग प्रक्रिया वातावरण में non-empty env var की आवश्यकता होती है।
  * `--install-daemon` के साथ, जब token auth को token की आवश्यकता होती है, SecretRef-managed gateway tokens सत्यापित किए जाते हैं लेकिन supervisor service environment metadata में resolved plaintext के रूप में persisted नहीं किए जाते।
  * `--install-daemon` के साथ, यदि token mode को token की आवश्यकता है और कॉन्फिगर किया गया token SecretRef unresolved है, तो ऑनबोर्डिंग remediation guidance के साथ fail closed होती है।
  * `--install-daemon` के साथ, यदि `gateway.auth.token` और `gateway.auth.password` दोनों कॉन्फिगर हैं और `gateway.auth.mode` unset है, तो ऑनबोर्डिंग install को तब तक रोकती है जब तक mode स्पष्ट रूप से सेट न हो।
  * स्थानीय ऑनबोर्डिंग कॉन्फिग में `gateway.mode="local"` लिखती है। यदि बाद की किसी कॉन्फिग फाइल में `gateway.mode` गायब है, तो उसे config damage या incomplete manual edit मानें, valid local-mode shortcut नहीं।
  * स्थानीय ऑनबोर्डिंग चुने गए setup path द्वारा आवश्यक selected downloadable plugins इंस्टॉल करती है।
  * रिमोट ऑनबोर्डिंग केवल रिमोट Gateway के लिए connection info लिखती है और local plugin packages इंस्टॉल नहीं करती।
  * `--allow-unconfigured` एक अलग gateway runtime escape hatch है। इसका मतलब यह नहीं है कि ऑनबोर्डिंग `gateway.mode` छोड़ सकती है।


उदाहरण:

bashCopy code
[code]
    export OPENCLAW_GATEWAY_TOKEN="your-token"openclaw onboard --non-interactive \  --mode local \  --auth-choice skip \  --gateway-auth token \  --gateway-token-ref-env OPENCLAW_GATEWAY_TOKEN \  --accept-risk
[/code]

गैर-इंटरैक्टिव स्थानीय gateway health:

  * जब तक आप `--skip-health` पास नहीं करते, ऑनबोर्डिंग सफलतापूर्वक बाहर निकलने से पहले reachable local gateway की प्रतीक्षा करती है।
  * `--install-daemon` पहले managed gateway install path शुरू करता है। इसके बिना, आपके पास पहले से local gateway चल रहा होना चाहिए, उदाहरण के लिए `openclaw gateway run`।
  * यदि आप automation में केवल config/workspace/bootstrap writes चाहते हैं, तो `--skip-health` उपयोग करें।
  * यदि आप workspace files स्वयं प्रबंधित करते हैं, तो `agents.defaults.skipBootstrap: true` सेट करने और `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md`, और `BOOTSTRAP.md` बनाना छोड़ने के लिए `--skip-bootstrap` पास करें।
  * native Windows पर, `--install-daemon` पहले Scheduled Tasks आज़माता है और यदि task creation deny हो जाए तो per-user Startup-folder login item पर fallback करता है।


reference mode के साथ इंटरैक्टिव ऑनबोर्डिंग व्यवहार:

  * संकेत मिलने पर **Use secret reference** चुनें।
  * फिर इनमें से कोई एक चुनें: 
    * Environment variable
    * Configured secret provider (`file` या `exec`)
  * ऑनबोर्डिंग ref सहेजने से पहले fast preflight validation करती है। 
    * यदि validation विफल होता है, तो ऑनबोर्डिंग error दिखाती है और आपको retry करने देती है।


### गैर-इंटरैक्टिव Z.AI endpoint विकल्प

bashCopy code
[code]
    # Promptless endpoint selectionopenclaw onboard --non-interactive \  --auth-choice zai-coding-global \  --zai-api-key "$ZAI_API_KEY" # Other Z.AI endpoint choices:# --auth-choice zai-coding-cn# --auth-choice zai-global# --auth-choice zai-cn
[/code]

गैर-इंटरैक्टिव Mistral उदाहरण:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY"
[/code]

## प्रवाह नोट्स

प्रवाह प्रकार

  * `quickstart`: न्यूनतम prompts, gateway token स्वतः generate करता है।
  * `manual`: port, bind, और auth के लिए full prompts (`advanced` का alias)।
  * `import`: detected migration provider चलाता है, plan preview करता है, फिर confirmation के बाद apply करता है।

प्रदाता prefiltering

जब auth choice preferred provider इंगित करता है, तो ऑनबोर्डिंग default-model और allowlist pickers को उस provider तक prefilter करती है। Volcengine और BytePlus के लिए, यह coding-plan variants (`volcengine-plan/*`, `byteplus-plan/*`) से भी match करता है।

यदि preferred-provider filter से अभी तक कोई loaded models नहीं मिलते, तो ऑनबोर्डिंग picker को खाली छोड़ने के बजाय unfiltered catalog पर fallback करती है।

Web-search follow-ups

कुछ web-search providers provider-specific follow-up prompts trigger करते हैं:

  * **Grok** same xAI OAuth profile या API key और `x_search` model choice के साथ optional `x_search` setup offer कर सकता है।
  * **Kimi** Moonshot API region (`api.moonshot.ai` vs `api.moonshot.cn`) और default Kimi web-search model के लिए पूछ सकता है।

अन्य व्यवहार

  * स्थानीय ऑनबोर्डिंग DM scope behavior: [CLI setup reference](</hi/start/wizard-cli-reference#outputs-and-internals>)।
  * सबसे तेज पहला chat: `openclaw dashboard` (Control UI, कोई channel setup नहीं)।
  * कस्टम प्रदाता: hosted providers not listed सहित किसी भी OpenAI या Anthropic compatible endpoint से connect करें। auto-detect के लिए Unknown उपयोग करें।
  * यदि Hermes state detected है, तो ऑनबोर्डिंग migration flow offer करती है। dry-run plans, overwrite mode, reports, और exact mappings के लिए [Migrate](</hi/cli/migrate>) उपयोग करें।


## सामान्य follow-up commands

bashCopy code
[code]
    openclaw channels addopenclaw configureopenclaw agents add <name>
[/code]

जब आपको केवल baseline config/workspace की आवश्यकता हो, तब इसके बजाय `openclaw setup` उपयोग करें। लक्षित परिवर्तनों के लिए बाद में `openclaw configure` और केवल-channel setup के लिए `openclaw channels add` उपयोग करें।

Was this useful?YesNo

Open issue