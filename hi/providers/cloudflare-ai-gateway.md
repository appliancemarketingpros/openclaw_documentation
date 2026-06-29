---
title: Cloudflare AI Gateway
source_url: https://docs.openclaw.ai/hi/providers/cloudflare-ai-gateway
scraped_at: 2026-06-29
---

ModelsProviders

Cloudflare AI Gateway प्रदाता APIs के सामने बैठता है और आपको एनालिटिक्स, कैशिंग और नियंत्रण जोड़ने देता है। Anthropic के लिए, OpenClaw आपके Gateway endpoint के माध्यम से Anthropic Messages API का उपयोग करता है।

गुण | मान  
---|---  
प्रदाता | `cloudflare-ai-gateway`  
बेस URL | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
डिफ़ॉल्ट मॉडल | `cloudflare-ai-gateway/claude-sonnet-4-6`  
API कुंजी | `CLOUDFLARE_AI_GATEWAY_API_KEY` (Gateway के माध्यम से अनुरोधों के लिए आपकी प्रदाता API कुंजी)  
  
जब Anthropic Messages मॉडलों के लिए सोच सक्षम होती है, तो OpenClaw Cloudflare AI Gateway के माध्यम से payload भेजने से पहले अंत में आने वाले assistant पूर्व-भरण turns को हटा देता है। Anthropic विस्तारित सोच के साथ response prefilling को अस्वीकार करता है, जबकि साधारण बिना-सोच वाला पूर्व-भरण उपलब्ध रहता है।

## Plugin इंस्टॉल करें

आधिकारिक Plugin इंस्टॉल करें, फिर Gateway पुनः शुरू करें:

bashCopy code
[code]
    openclaw plugins install @openclaw/cloudflare-ai-gateway-provideropenclaw gateway restart
[/code]

## शुरू करना

* ### प्रदाता API कुंजी और Gateway विवरण सेट करें

onboarding चलाएँ और Cloudflare AI Gateway auth विकल्प चुनें:

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

यह आपके account ID, gateway ID, और API कुंजी के लिए पूछता है।

* ### डिफ़ॉल्ट मॉडल सेट करें

मॉडल को अपने OpenClaw config में जोड़ें:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### सत्यापित करें कि मॉडल उपलब्ध है

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## गैर-इंटरैक्टिव उदाहरण

स्क्रिप्टेड या CI setups के लिए, command line पर सभी मान पास करें:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## उन्नत configuration

प्रमाणित gateways

यदि आपने Cloudflare में Gateway authentication सक्षम किया है, तो `cf-aig-authorization` header जोड़ें। यह आपकी प्रदाता API कुंजी के **अतिरिक्त** है।

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

Environment नोट

यदि Gateway daemon (launchd/systemd) के रूप में चलता है, तो सुनिश्चित करें कि `CLOUDFLARE_AI_GATEWAY_API_KEY` उस process के लिए उपलब्ध है।

## संबंधित

[**मॉडल चयन** प्रदाताओं, मॉडल refs, और failover व्यवहार को चुनना। ](</hi/concepts/model-providers>) [**समस्या निवारण** सामान्य समस्या निवारण और FAQ। ](</hi/help/troubleshooting>)

Was this useful?YesNo

Open issue