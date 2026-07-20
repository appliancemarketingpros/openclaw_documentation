---
title: वॉल्ट SecretRefs
source_url: https://docs.openclaw.ai/hi/plugins/vault
scraped_at: 2026-07-20
---

CapabilitiesPlugin guides

# Vault SecretRefs

बंडल किया गया Vault plugin, Gateway के शुरू होने और रीलोड होने के समय OpenClaw को HashiCorp Vault से `exec` SecretRefs को समाधान करने देता है। OpenClaw, Vault संदर्भों को कॉन्फ़िगरेशन में संग्रहीत करता है, समाधान किए गए मानों को इन-मेमोरी सीक्रेट्स स्नैपशॉट में रखता है और समाधान की गई API कुंजियों को वापस `openclaw.json` में नहीं लिखता।

इसका उपयोग तब करें, जब आप पहले से Vault चला रहे हों या मॉडल प्रदाता कुंजियों को OpenClaw कॉन्फ़िगरेशन फ़ाइलों से बाहर रखना चाहते हों। SecretRef रनटाइम मॉडल के लिए, [सीक्रेट्स प्रबंधन](</hi/gateway/secrets>) देखें।

## शुरू करने से पहले

आपको चाहिए:

  * बंडल किया गया `vault` plugin उपलब्ध रखने वाला OpenClaw
  * पहुँच योग्य Vault सर्वर
  * ऐसा Vault प्रमाणीकरण, जो उन सीक्रेट पथों को पढ़ने की पहुँच वाला क्लाइंट टोकन बना सके, जिन्हें OpenClaw को समाधान करना चाहिए
  * Gateway शुरू करने वाले परिवेश में `VAULT_ADDR` और इनमें से कोई एक शामिल होना चाहिए: `VAULT_TOKEN`, `VAULT_TOKEN_FILE` के साथ `OPENCLAW_VAULT_AUTH_METHOD=token_file`, या कॉन्फ़िगर किया गया JWT/Kubernetes लॉगिन


रिज़ॉल्वर Node से HTTP के माध्यम से Vault से संचार करता है। SecretRefs को समाधान करने के लिए Gateway को Vault CLI की आवश्यकता नहीं होती।

`openclaw vault` कमांड चलाने से पहले बंडल किया गया plugin सक्षम करें:

bashCopy code
[code]
    openclaw plugins enable vault
[/code]

## Vault में प्रदाता कुंजी संग्रहीत करें

OpenClaw डिफ़ॉल्ट रूप से `secret` पर माउंट किए गए KV v2 का उपयोग करता है, जो Vault डेवलपमेंट सर्वर के उदाहरणों के अनुरूप है। प्रोडक्शन Vault के लिए, SecretRef आईडी बनाने से पहले `OPENCLAW_VAULT_KV_MOUNT` को अपने वास्तविक KV माउंट पथ पर सेट करें। OpenClaw के डिफ़ॉल्ट के साथ, यह SecretRef आईडी:

textCopy code
[code]
    providers/openrouter/apiKey
[/code]

इस Vault फ़ील्ड को पढ़ती है:

textCopy code
[code]
    secret/data/providers/openrouter -> apiKey
[/code]

Vault CLI से इसे बनाने का एक तरीका है:

bashCopy code
[code]
    export OPENROUTER_API_KEY=<openrouter-api-key>vault kv put secret/providers/openrouter apiKey="$OPENROUTER_API_KEY"
[/code]

OpenClaw के लिए सीमित दायरे वाला क्लाइंट टोकन उपयोग करें, रूट टोकन नहीं। डिफ़ॉल्ट KV v2 लेआउट के लिए, मॉडल प्रदाता कुंजियों की न्यूनतम नीति इस प्रकार है:

hclCopy code
[code]
    path "secret/data/providers/*" {  capabilities = ["read"]}
[/code]

## Vault को Gateway के लिए दृश्यमान बनाएँ

कंटेनर के बिना चलने वाले स्थानीय Gateway के लिए, Vault सेटिंग्स को उसी शेल में निर्यात करें जो OpenClaw शुरू करता है। डिफ़ॉल्ट प्रमाणीकरण विधि `VAULT_TOKEN` से Vault क्लाइंट टोकन पढ़ती है:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport VAULT_TOKEN=<vault-client-token>
[/code]

यदि Vault Agent किसी टोकन सिंक फ़ाइल में लिखता है, तो टोकन-फ़ाइल प्रमाणीकरण उपयोग करें:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=token_fileexport VAULT_TOKEN_FILE=/vault/secrets/token
[/code]

निजी CA द्वारा हस्ताक्षरित Vault सर्वर के लिए, या तो उस CA को होस्ट ट्रस्ट स्टोर में इंस्टॉल करें और Node सिस्टम ट्रस्ट सक्षम करें:

bashCopy code
[code]
    export NODE_USE_SYSTEM_CA=1
[/code]

या सीधे PEM बंडल प्रदान करें:

bashCopy code
[code]
    export NODE_EXTRA_CA_CERTS=/path/to/vault-ca.pem
[/code]

OpenClaw शुरू होते समय ये वेरिएबल मौजूद होने चाहिए। Vault plugin इन्हें अपनी रिज़ॉल्वर प्रक्रिया को अग्रेषित करता है।

गैर-इंटरैक्टिव JWT प्रमाणीकरण के लिए, वर्कलोड JWT फ़ाइल और `jwt` प्रकार की Vault भूमिका उपयोग करें:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=jwtexport OPENCLAW_VAULT_AUTH_MOUNT=jwtexport OPENCLAW_VAULT_AUTH_ROLE=openclawexport OPENCLAW_VAULT_JWT_FILE=/var/run/secrets/tokens/vault
[/code]

JWT फ़ाइल एक प्रोजेक्ट किया गया वर्कलोड टोकन होनी चाहिए, जैसे कि Vault भूमिका द्वारा स्वीकार किए जाने वाले ऑडियंस वाला Kubernetes सेवा खाता टोकन। इंटरैक्टिव OIDC ब्राउज़र लॉगिन मनुष्यों के लिए उपयोगी है, लेकिन Gateway रनटाइम को गैर-इंटरैक्टिव JWT लॉगिन या टोकन फ़ाइल की आवश्यकता होती है।

Vault की Kubernetes प्रमाणीकरण विधि के लिए, `kubernetes` उपयोग करें। यह Pods के रूप में चल रहे Gateways के लिए है; डिफ़ॉल्ट माउंट `kubernetes` है और डिफ़ॉल्ट JWT फ़ाइल मानक सेवा खाता टोकन पथ है:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=kubernetesexport OPENCLAW_VAULT_AUTH_ROLE=openclaw
[/code]

`OPENCLAW_VAULT_AUTH_MOUNT` को केवल तब सेट करें, जब Vault ने Kubernetes प्रमाणीकरण को `auth/kubernetes` के अलावा कहीं और माउंट किया हो। `OPENCLAW_VAULT_JWT_FILE` को केवल तब सेट करें, जब सेवा खाता टोकन किसी कस्टम पथ पर प्रोजेक्ट किया गया हो।

वैकल्पिक सेटिंग्स:

bashCopy code
[code]
    export VAULT_NAMESPACE=<namespace-name>export OPENCLAW_VAULT_KV_MOUNT=secretexport OPENCLAW_VAULT_KV_VERSION=2
[/code]

जाँचें कि वर्तमान शेल क्या देख सकता है:

bashCopy code
[code]
    openclaw vault status
[/code]

एक से अधिक Vault-समर्थित सीक्रेट प्रदाता कॉन्फ़िगर होने पर, उपनाम द्वारा किसी एक को चुनें:

bashCopy code
[code]
    openclaw vault status --provider-alias corp-vault
[/code]

`openclaw vault status` कभी भी `VAULT_TOKEN` प्रिंट नहीं करता; यह केवल बताता है कि टोकन, टोकन फ़ाइल और JWT फ़ाइल सेट हैं या नहीं।

## SecretRef योजना बनाएँ और लागू करें

ऐसी योजना बनाएँ जो OpenRouter की मॉडल प्रदाता API कुंजी को Vault से मैप करे:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openrouter-id providers/openrouter/apiKey
[/code]

योजना लागू और सत्यापित करें:

bashCopy code
[code]
    openclaw secrets apply --from ./vault-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from ./vault-secrets-plan.json --allow-execopenclaw secrets audit --check --allow-execopenclaw secrets reload
[/code]

`--allow-exec` उपयोग करें, क्योंकि Vault plugin OpenClaw द्वारा प्रबंधित exec SecretRef प्रदाता के माध्यम से समाधान करता है।

यदि Gateway अभी नहीं चल रहा है, तो `openclaw secrets reload` चलाने के बजाय योजना लागू करने के बाद इसे सामान्य रूप से शुरू करें।

## अधिक प्रदाता कुंजियाँ कॉन्फ़िगर करें

अंतर्निहित शॉर्टकट:

bashCopy code
[code]
    openclaw vault setup --openai-id providers/openai/apiKeyopenclaw vault setup --anthropic-id providers/anthropic/apiKeyopenclaw vault setup --openrouter-id providers/openrouter/apiKey
[/code]

एक योजना में एकाधिक प्रदाता कुंजियाँ:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openai-id providers/openai/apiKey \  --anthropic-id providers/anthropic/apiKey \  --openrouter-id providers/openrouter/apiKey
[/code]

शॉर्टकट के बिना बंडल किए गए प्रदाता, या पहले से कॉन्फ़िगर किए गए OpenAI-संगत और कस्टम मॉडल प्रदाता, `--provider-key` उपयोग करते हैं:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --provider-key local-openai=providers/local-openai/apiKey \  --provider-key groq=providers/groq/apiKey
[/code]

प्रत्येक `--provider-key <provider=id>`, `models.providers.<provider>.apiKey` में एक SecretRef लिखता है। कस्टम प्रदाताओं के लिए, यह प्रदाता की `baseUrl`, `api` या `models` सेटिंग्स नहीं बनाता; पहले उन्हें कॉन्फ़िगर करें।

किसी भी ज्ञात SecretRef लक्ष्य पथ के लिए `--target <path=id>` उपयोग करें:

bashCopy code
[code]
    openclaw vault setup \  --target channels.telegram.botToken=channels/telegram/botToken \  --target models.providers.openai.headers.x-api-key=providers/openai/proxyKey \  --target auth-profiles:main:profiles.openai.key=providers/openai/apiKey
[/code]

साधारण लक्ष्य पथ `openclaw.json` पर लागू होते हैं। मौजूदा `auth-profiles.json` लक्ष्यों के लिए `auth-profiles:<agentId>:<path>` उपयोग करें। लक्ष्य पथ पंजीकृत OpenClaw SecretRef लक्ष्य होना चाहिए। सेटअप कमांड OpenClaw में मनमाने नाम वाले सीक्रेट नहीं बनाता; Vault सीक्रेट स्टोर बना रहता है और OpenClaw केवल समर्थित कॉन्फ़िगरेशन फ़ील्ड में SecretRefs संग्रहीत करता है।

## SecretRef आईडी प्रारूप

Vault SecretRef आईडी इस परंपरा का उपयोग करती हैं:

textCopy code
[code]
    <vault-secret-path>/<field>
[/code]

उदाहरण:

SecretRef आईडी | डिफ़ॉल्ट KV v2 Vault रीड | लौटाया गया फ़ील्ड  
---|---|---  
`providers/openrouter/apiKey` | `secret/data/providers/openrouter` | `apiKey`  
`providers/openai/apiKey` | `secret/data/providers/openai` | `apiKey`  
`teams/agent-prod/openrouter` | `secret/data/teams/agent-prod` | `openrouter`  
  
लौटाया गया Vault फ़ील्ड स्ट्रिंग होना चाहिए।

KV v1 के लिए, सेट करें:

bashCopy code
[code]
    export OPENCLAW_VAULT_KV_VERSION=1
[/code]

इसके बाद `providers/openrouter/apiKey` यह पढ़ता है:

textCopy code
[code]
    secret/providers/openrouter -> apiKey
[/code]

## OpenClaw क्या संग्रहीत करता है

Vault सेटअप योजना लागू करने पर plugin द्वारा प्रबंधित प्रदाता संग्रहीत होता है:

jsonCopy code
[code]
    {  "source": "exec",  "pluginIntegration": {    "pluginId": "vault",    "integrationId": "vault"  }}
[/code]

क्रेडेंशियल फ़ील्ड उस प्रदाता की ओर संकेत करते हैं:

jsonCopy code
[code]
    { "source": "exec", "provider": "vault", "id": "providers/openrouter/apiKey" }
[/code]

समाधान किया गया मान केवल सक्रिय रनटाइम सीक्रेट्स स्नैपशॉट में रहता है।

## कंटेनर और प्रबंधित परिनियोजन

कंटेनर में चलने वाले Gateways भी उसी plugin और SecretRef कॉन्फ़िगरेशन का उपयोग करते हैं। कंटेनर को ये मिलने चाहिए:

  * `VAULT_ADDR`
  * एक प्रमाणीकरण स्रोत: 
    * `VAULT_TOKEN`
    * `VAULT_TOKEN_FILE` के साथ `OPENCLAW_VAULT_AUTH_METHOD=token_file`
    * `OPENCLAW_VAULT_AUTH_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` और `OPENCLAW_VAULT_JWT_FILE` के साथ `OPENCLAW_VAULT_AUTH_METHOD=jwt`
    * `OPENCLAW_VAULT_AUTH_ROLE` के साथ `OPENCLAW_VAULT_AUTH_METHOD=kubernetes`; वैकल्पिक रूप से `OPENCLAW_VAULT_AUTH_MOUNT` या `OPENCLAW_VAULT_JWT_FILE` को ओवरराइड करें
  * वैकल्पिक `VAULT_NAMESPACE`, `OPENCLAW_VAULT_KV_MOUNT` और `OPENCLAW_VAULT_KV_VERSION`


Kubernetes का उपयोग करते समय, यदि Vault में क्लस्टर के लिए Kubernetes प्रमाणीकरण कॉन्फ़िगर है, तो `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` को प्राथमिकता दें। `OPENCLAW_VAULT_AUTH_METHOD=jwt` केवल तब उपयोग करें, जब Vault क्लस्टर को सामान्य JWT/OIDC जारीकर्ता मानने के लिए कॉन्फ़िगर हो। दोनों विकल्प Kubernetes Secret में लंबे समय तक सक्रिय रहने वाले Vault टोकन से बेहतर हैं। Vault Agent साइडकार या इंजेक्टर परिनियोजन इसके बजाय `token_file` उपयोग कर सकते हैं।

बहु-किरायेदार Vault सेटअप के लिए, किरायेदार रूटिंग को Vault नीति और परिनियोजन कॉन्फ़िगरेशन में रखें। OpenClaw को निश्चित माउंट, भूमिका या पथ की आवश्यकता नहीं होती: प्रत्येक Gateway परिवेश अपना `OPENCLAW_VAULT_KV_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` और SecretRef आईडी सेट कर सकता है। यदि किसी साझा Gateway को एक ही समय में अलग-अलग Vault उपयोगकर्ताओं का समाधान करना हो, तो अलग-अलग प्रमाणीकरण परिवेशों को रैप करने वाले मैन्युअल रूप से कॉन्फ़िगर किए गए exec प्रदाताओं का उपयोग करें या अलग-अलग Vault परिवेश वेरिएबल वाले Gateway परिवेशों में किरायेदारों को विभाजित करें।

## संबंधित

  * [सीक्रेट्स प्रबंधन](</hi/gateway/secrets>)
  * [`openclaw secrets`](</hi/cli/secrets>)
  * [Plugin सूची](</hi/plugins/plugin-inventory>)


Was this useful?YesNo

Open issue