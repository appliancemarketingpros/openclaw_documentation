---
title: कोड निष्पादन
source_url: https://docs.openclaw.ai/hi/tools/code-execution
scraped_at: 2026-06-29
---

CapabilitiesTools

`code_execution` xAI के Responses API पर सैंडबॉक्स किए गए रिमोट Python विश्लेषण चलाता है। इसे बंडल किए गए `xai` Plugin द्वारा (`tools` अनुबंध के अंतर्गत) पंजीकृत किया जाता है और यह उसी `https://api.x.ai/v1/responses` एंडपॉइंट पर भेजता है जिसका उपयोग `x_search` करता है।

गुण | मान  
---|---  
टूल नाम | `code_execution`  
Provider Plugin | `xai` (बंडल किया गया, `enabledByDefault: true`)  
Auth | xAI auth प्रोफ़ाइल, `XAI_API_KEY`, या `plugins.entries.xai.config.webSearch.apiKey`  
डिफ़ॉल्ट मॉडल | `grok-4-1-fast`  
डिफ़ॉल्ट टाइमआउट | 30 सेकंड  
डिफ़ॉल्ट `maxTurns` | सेट नहीं (xAI अपनी आंतरिक सीमा लागू करता है)  
  
यह स्थानीय [`exec`](</hi/tools/exec>) से अलग है:

  * `exec` आपकी मशीन या paired node पर shell कमांड चलाता है।
  * `code_execution` xAI के रिमोट सैंडबॉक्स में Python चलाता है।


`code_execution` का उपयोग इनके लिए करें:

  * गणनाएं।
  * सारणीकरण।
  * त्वरित सांख्यिकी।
  * चार्ट-शैली विश्लेषण।
  * `x_search` या `web_search` द्वारा लौटाए गए डेटा का विश्लेषण।


जब आपको स्थानीय फ़ाइलों, अपने shell, अपने repo, या paired devices की आवश्यकता हो, तो इसका उपयोग **न करें** । उसके लिए [`exec`](</hi/tools/exec>) का उपयोग करें।

## सेटअप

* ### xAI credentials प्रदान करें

पात्र SuperGrok या X Premium सदस्यता का उपयोग करके Grok OAuth से साइन इन करें, या API key संग्रहीत करें। xAI OAuth device-code verification का उपयोग करता है, इसलिए यह localhost callback के बिना रिमोट hosts से काम करता है। OAuth `code_execution` और `x_search` के लिए काम करता है; `XAI_API_KEY` या Plugin web-search config Grok `web_search` को भी चला सकते हैं।

bashCopy code
[code]
    openclaw models auth login --provider xai --method oauth
[/code]

नए install के दौरान, वही auth विकल्प onboarding के अंदर उपलब्ध होते हैं:

bashCopy code
[code]
    openclaw onboard --install-daemonopenclaw onboard --install-daemon --auth-choice xai-oauth
[/code]

या API key का उपयोग करें:

bashCopy code
[code]
    openclaw models auth login --provider xai --method api-keyexport XAI_API_KEY=xai-...
[/code]

या config के माध्यम से:

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          webSearch: {            apiKey: "xai-...",          },        },      },    },  },}
[/code]

* ### code_execution सक्षम और ट्यून करें

xAI credentials उपलब्ध होने पर `code_execution` उपलब्ध होता है। इसे अक्षम करने के लिए `plugins.entries.xai.config.codeExecution.enabled` को `false` पर सेट करें, या model और timeout को ट्यून करने के लिए उसी block का उपयोग करें।

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast", // override the default xAI code-execution model            maxTurns: 2,            // optional cap on internal tool turns            timeoutSeconds: 30,     // request timeout (default: 30)          },        },      },    },  },}
[/code]

* ### Gateway को restart करें

bashCopy code
[code]
    openclaw gateway restart
[/code]

xAI Plugin के `enabled: true` के साथ फिर से register होने के बाद `code_execution` agent की tool list में दिखाई देता है।

## इसका उपयोग कैसे करें

स्वाभाविक रूप से पूछें और विश्लेषण का उद्देश्य स्पष्ट करें:

textCopy code
[code]
    Use code_execution to calculate the 7-day moving average for these numbers: ...
[/code]

textCopy code
[code]
    Use x_search to find posts mentioning OpenClaw this week, then use code_execution to count them by day.
[/code]

textCopy code
[code]
    Use web_search to gather the latest AI benchmark numbers, then use code_execution to compare percent changes.
[/code]

टूल आंतरिक रूप से एक ही `task` parameter लेता है, इसलिए agent को पूरा analysis request और कोई भी inline data एक prompt में भेजना चाहिए।

## त्रुटियां

जब टूल auth के बिना चलता है, तो यह auth-profile, env var, और config विकल्पों की ओर संकेत करने वाली संरचित `missing_xai_api_key` error लौटाता है। error JSON है, thrown exception नहीं, इसलिए agent स्वयं सुधार कर सकता है:

jsonCopy code
[code]
    {  "error": "missing_xai_api_key",  "message": "code_execution needs xAI credentials. Run `openclaw onboard --auth-choice xai-oauth` to sign in with Grok, run `openclaw onboard --auth-choice xai-api-key`, set `XAI_API_KEY` in the Gateway environment, or configure `plugins.entries.xai.config.webSearch.apiKey`.",  "docs": "https://docs.openclaw.ai/tools/code-execution"}
[/code]

## सीमाएं

  * यह रिमोट xAI execution है, स्थानीय process execution नहीं।
  * परिणामों को ephemeral analysis मानें, persistent notebook session नहीं।
  * स्थानीय फ़ाइलों या अपने workspace तक access मानकर न चलें।
  * ताज़ा X data के लिए, पहले [`x_search`](</hi/tools/web#x_search>) का उपयोग करें और परिणाम को `code_execution` में pipe करें।


## संबंधित

[**Exec tool** आपकी मशीन या paired node पर स्थानीय shell execution। ](</hi/tools/exec>) [**Exec approvals** shell execution के लिए allow/deny policy। ](</hi/tools/exec-approvals>) [**Web tools** `web_search`, `x_search`, और `web_fetch`। ](</hi/tools/web>) [**xAI provider** Grok models, web/x search, और code execution config। ](</hi/providers/xai>)

Was this useful?YesNo

Open issue