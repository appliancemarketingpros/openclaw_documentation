---
title: DuckDuckGo खोज
source_url: https://docs.openclaw.ai/hi/tools/duckduckgo-search
scraped_at: 2026-06-29
---

CapabilitiesTools

OpenClaw DuckDuckGo को **कुंजी-मुक्त** `web_search` प्रदाता के रूप में समर्थन करता है। किसी API कुंजी या खाते की आवश्यकता नहीं है।

## सेटअप

किसी API कुंजी की आवश्यकता नहीं - बस DuckDuckGo को अपने प्रदाता के रूप में सेट करें:

* ### कॉन्फ़िगर करें

bashCopy code
[code]
    openclaw configure --section web# Select "duckduckgo" as the provider
[/code]

## कॉन्फ़िग

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

क्षेत्र और SafeSearch के लिए वैकल्पिक Plugin-स्तरीय सेटिंग्स:

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo region code            safeSearch: "moderate", // "strict", "moderate", or "off"          },        },      },    },  },}
[/code]

## टूल पैरामीटर

खोज क्वेरी।

वापस किए जाने वाले परिणाम (1-10)।

DuckDuckGo क्षेत्र कोड (जैसे `us-en`, `uk-en`, `de-de`)।

SafeSearch स्तर।

क्षेत्र और SafeSearch को Plugin कॉन्फ़िग में भी सेट किया जा सकता है (ऊपर देखें) - टूल पैरामीटर प्रति-क्वेरी कॉन्फ़िग मानों को ओवरराइड करते हैं।

## नोट्स

  * **कोई API कुंजी नहीं** \- DuckDuckGo को अपने `web_search` प्रदाता के रूप में चुनने के बाद काम करता है
  * **प्रयोगात्मक** \- परिणाम DuckDuckGo के गैर-JavaScript HTML खोज पेजों से इकट्ठा करता है, किसी आधिकारिक API या SDK से नहीं
  * **बॉट-चैलेंज जोखिम** \- भारी या स्वचालित उपयोग के तहत DuckDuckGo CAPTCHA दिखा सकता है या अनुरोधों को ब्लॉक कर सकता है
  * **HTML पार्सिंग** \- परिणाम पेज संरचना पर निर्भर करते हैं, जो बिना सूचना के बदल सकती है
  * **स्पष्ट चयन** \- जब कोई API-समर्थित प्रदाता कॉन्फ़िग नहीं होता, OpenClaw DuckDuckGo को स्वचालित रूप से नहीं चुनता
  * **कॉन्फ़िग न होने पर SafeSearch डिफ़ॉल्ट रूप से moderate होता है**


## संबंधित

  * [Web Search अवलोकन](</hi/tools/web>) \-- सभी प्रदाता और स्वतः-पहचान
  * [Brave Search](</hi/tools/brave-search>) \-- नि:शुल्क स्तर के साथ संरचित परिणाम
  * [Exa Search](</hi/tools/exa-search>) \-- सामग्री निष्कर्षण के साथ न्यूरल खोज


Was this useful?YesNo

Open issue