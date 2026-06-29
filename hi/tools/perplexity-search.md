---
title: Perplexity खोज
source_url: https://docs.openclaw.ai/hi/tools/perplexity-search
scraped_at: 2026-06-29
---

CapabilitiesTools

OpenClaw Perplexity Search API को `web_search` प्रदाता के रूप में समर्थन करता है। यह `title`, `url`, और `snippet` फ़ील्ड के साथ संरचित परिणाम लौटाता है।

संगतता के लिए, OpenClaw पुराने Perplexity Sonar/OpenRouter सेटअप का भी समर्थन करता है। यदि आप `OPENROUTER_API_KEY`, `plugins.entries.perplexity.config.webSearch.apiKey` में कोई `sk-or-...` कुंजी उपयोग करते हैं, या `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` सेट करते हैं, तो प्रदाता chat-completions पथ पर स्विच करता है और संरचित Search API परिणामों के बजाय उद्धरणों के साथ AI-संश्लेषित उत्तर लौटाता है।

## Plugin इंस्टॉल करें

आधिकारिक Plugin इंस्टॉल करें, फिर Gateway पुनः आरंभ करें:

bashCopy code
[code]
    openclaw plugins install @openclaw/perplexity-pluginopenclaw gateway restart
[/code]

## Perplexity API कुंजी प्राप्त करना

  1. [perplexity.ai/settings/api](<https://www.perplexity.ai/settings/api>) पर Perplexity खाता बनाएँ
  2. डैशबोर्ड में API कुंजी जनरेट करें
  3. कुंजी को कॉन्फ़िग में संग्रहीत करें या Gateway वातावरण में `PERPLEXITY_API_KEY` सेट करें।


## OpenRouter संगतता

यदि आप Perplexity Sonar के लिए पहले से OpenRouter उपयोग कर रहे थे, तो `provider: "perplexity"` रखें और Gateway वातावरण में `OPENROUTER_API_KEY` सेट करें, या `plugins.entries.perplexity.config.webSearch.apiKey` में कोई `sk-or-...` कुंजी संग्रहीत करें।

वैकल्पिक संगतता नियंत्रण:

  * `plugins.entries.perplexity.config.webSearch.baseUrl`
  * `plugins.entries.perplexity.config.webSearch.model`


## कॉन्फ़िग उदाहरण

### नेटिव Perplexity Search API

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "pplx-...",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

### OpenRouter / Sonar संगतता

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "<openrouter-api-key>",            baseUrl: "https://openrouter.ai/api/v1",            model: "perplexity/sonar-pro",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

## कुंजी कहाँ सेट करें

**कॉन्फ़िग के माध्यम से:** `openclaw configure --section web` चलाएँ। यह कुंजी को `plugins.entries.perplexity.config.webSearch.apiKey` के अंतर्गत `~/.openclaw/openclaw.json` में संग्रहीत करता है। वह फ़ील्ड SecretRef ऑब्जेक्ट भी स्वीकार करता है।

**वातावरण के माध्यम से:** Gateway प्रक्रिया वातावरण में `PERPLEXITY_API_KEY` या `OPENROUTER_API_KEY` सेट करें। Gateway इंस्टॉल के लिए, इसे `~/.openclaw/.env` (या अपने सेवा वातावरण) में रखें। [Env vars](</hi/help/faq#env-vars-and-env-loading>) देखें।

यदि `provider: "perplexity"` कॉन्फ़िगर है और Perplexity कुंजी SecretRef बिना किसी env fallback के अनसुलझी है, तो startup/reload तुरंत विफल हो जाता है।

## टूल पैरामीटर

ये पैरामीटर नेटिव Perplexity Search API पथ पर लागू होते हैं।

खोज क्वेरी।

लौटाए जाने वाले परिणामों की संख्या (1-10)।

2-अक्षरीय ISO देश कोड (जैसे `US`, `DE`)।

ISO 639-1 भाषा कोड (जैसे `en`, `de`, `fr`)।

समय फ़िल्टर - `day` 24 घंटे है।

केवल इस तारीख के बाद प्रकाशित परिणाम (`YYYY-MM-DD`)।

केवल इस तारीख से पहले प्रकाशित परिणाम (`YYYY-MM-DD`)।

डोमेन allowlist/denylist ऐरे (अधिकतम 20)।

कुल सामग्री बजट (अधिकतम 1000000)।

प्रति-पृष्ठ टोकन सीमा।

पुराने Sonar/OpenRouter संगतता पथ के लिए:

  * `query`, `count`, और `freshness` स्वीकार किए जाते हैं
  * वहाँ `count` केवल संगतता के लिए है; प्रतिक्रिया फिर भी N-परिणाम सूची के बजाय उद्धरणों के साथ एक संश्लेषित उत्तर होती है
  * केवल Search API वाले फ़िल्टर जैसे `country`, `language`, `date_after`, `date_before`, `domain_filter`, `max_tokens`, और `max_tokens_per_page` स्पष्ट त्रुटियाँ लौटाते हैं


**उदाहरण:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (allowlist)await web_search({  query: "climate research",  domain_filter: ["nature.com", "science.org", ".edu"],}); // Domain filtering (denylist - prefix with -)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],}); // More content extractionawait web_search({  query: "detailed AI research",  max_tokens: 50000,  max_tokens_per_page: 4096,});
[/code]

### डोमेन फ़िल्टर नियम

  * प्रति फ़िल्टर अधिकतम 20 डोमेन
  * एक ही अनुरोध में allowlist और denylist को मिलाया नहीं जा सकता
  * denylist प्रविष्टियों के लिए `-` उपसर्ग का उपयोग करें (जैसे, `["-reddit.com"]`)


## टिप्पणियाँ

  * Perplexity Search API संरचित वेब खोज परिणाम (`title`, `url`, `snippet`) लौटाता है
  * OpenRouter या स्पष्ट `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` संगतता के लिए Perplexity को वापस Sonar chat completions पर स्विच करता है
  * Sonar/OpenRouter संगतता संरचित परिणाम पंक्तियों के बजाय उद्धरणों के साथ एक संश्लेषित उत्तर लौटाती है
  * परिणाम डिफ़ॉल्ट रूप से 15 मिनट के लिए कैश किए जाते हैं (`cacheTtlMinutes` के माध्यम से कॉन्फ़िगर करने योग्य)


## संबंधित

[**वेब खोज अवलोकन** सभी प्रदाता और ऑटो-डिटेक्शन नियम। ](</hi/tools/web>) [**Brave खोज** देश और भाषा फ़िल्टर के साथ संरचित परिणाम। ](</hi/tools/brave-search>) [**Exa खोज** सामग्री निष्कर्षण के साथ न्यूरल खोज। ](</hi/tools/exa-search>) [**Perplexity Search API दस्तावेज़** आधिकारिक Perplexity Search API क्विकस्टार्ट और संदर्भ। ](<https://docs.perplexity.ai/docs/search/quickstart>)

Was this useful?YesNo

Open issue