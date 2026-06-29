---
title: Brave खोज
source_url: https://docs.openclaw.ai/hi/tools/brave-search
scraped_at: 2026-06-29
---

CapabilitiesTools

OpenClaw Brave Search API को `web_search` provider के रूप में समर्थन करता है।

## API key प्राप्त करें

  1. <https://brave.com/search/api/> पर Brave Search API account बनाएं
  2. dashboard में, **Search** plan चुनें और API key generate करें।
  3. key को config में store करें या Gateway environment में `BRAVE_API_KEY` set करें।


## Config example

json5Copy code
[code]
    {  plugins: {    entries: {      brave: {        config: {          webSearch: {            apiKey: "BRAVE_API_KEY_HERE",            mode: "web", // or "llm-context"            baseUrl: "https://api.search.brave.com", // optional proxy/base URL override          },        },      },    },  },  tools: {    web: {      search: {        provider: "brave",        maxResults: 5,        timeoutSeconds: 30,      },    },  },}
[/code]

Provider-specific Brave search settings अब `plugins.entries.brave.config.webSearch.*` के अंतर्गत रहती हैं। Legacy `tools.web.search.apiKey` अभी भी compatibility shim के ज़रिए load होता है, लेकिन यह अब canonical config path नहीं है।

`webSearch.mode` Brave transport को नियंत्रित करता है:

  * `web` (default): titles, URLs, और snippets के साथ सामान्य Brave web search
  * `llm-context`: grounding के लिए pre-extracted text chunks और sources के साथ Brave LLM Context API


`webSearch.baseUrl` Brave requests को किसी trusted Brave-compatible proxy या gateway की ओर point कर सकता है। OpenClaw configured base URL में `/res/v1/web/search` या `/res/v1/llm/context` append करता है और cache key में base URL रखता है। Public endpoints को `https://` का उपयोग करना चाहिए; `http://` केवल trusted loopback या private-network proxy hosts के लिए accepted है।

## Tool parameters

Search query.

Return करने के लिए results की संख्या (1–10)।

2-letter ISO country code (उदा. `US`, `DE`)।

Search results के लिए ISO 639-1 language code (उदा. `en`, `de`, `fr`)।

Brave search-language code (उदा. `en`, `en-gb`, `zh-hans`)।

UI elements के लिए ISO language code।

Time filter — `day` 24 घंटे है।

केवल इस date (`YYYY-MM-DD`) के बाद published results।

केवल इस date (`YYYY-MM-DD`) से पहले published results।

**Examples:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",});
[/code]

## Notes

  * OpenClaw Brave **Search** plan का उपयोग करता है। यदि आपके पास legacy subscription है (उदा. 2,000 queries/month वाला original Free plan), तो यह valid रहता है लेकिन इसमें LLM Context या higher rate limits जैसी newer features शामिल नहीं हैं।
  * हर Brave plan में **$5/month in free credit** (renewing) शामिल है। Search plan की cost $5 per 1,000 requests है, इसलिए credit 1,000 queries/month cover करता है। unexpected charges से बचने के लिए Brave dashboard में अपनी usage limit set करें। current plans के लिए [Brave API portal](<https://brave.com/search/api/>) देखें।
  * Search plan में LLM Context endpoint और AI inference rights शामिल हैं। models को train या tune करने के लिए results store करने के लिए explicit storage rights वाला plan आवश्यक है। Brave [Terms of Service](<https://api-dashboard.search.brave.com/terms-of-service>) देखें।
  * `llm-context` mode normal web-search snippet shape के बजाय grounded source entries return करता है।
  * `llm-context` mode `freshness` और bounded `date_after` \+ `date_before` ranges support करता है। यह `ui_lang` support नहीं करता; `date_before` बिना `date_after` के reject किया जाता है क्योंकि Brave को custom freshness ranges में start और end dates दोनों शामिल करने की आवश्यकता होती है।
  * `ui_lang` में `en-US` जैसा region subtag शामिल होना चाहिए।
  * Results default रूप से 15 minutes के लिए cached रहते हैं (`cacheTtlMinutes` के ज़रिए configurable)।
  * Custom `webSearch.baseUrl` values Brave cache identity में शामिल होते हैं, इसलिए proxy-specific responses collide नहीं करते।
  * Troubleshooting के दौरान Brave request URLs/query params, response status/timing, और search-cache hit/miss/write events log करने के लिए `brave.http` diagnostics flag enable करें। flag कभी भी API key या response bodies log नहीं करता, लेकिन search queries sensitive हो सकती हैं।


## Related

  * [Web Search overview](</hi/tools/web>) \-- सभी providers और auto-detection
  * [Perplexity Search](</hi/tools/perplexity-search>) \-- domain filtering के साथ structured results
  * [Exa Search](</hi/tools/exa-search>) \-- content extraction के साथ neural search


Was this useful?YesNo

Open issue