---
title: वेब फ़ेच
source_url: https://docs.openclaw.ai/hi/tools/web-fetch
scraped_at: 2026-06-29
---

CapabilitiesTools

`web_fetch` टूल एक साधारण HTTP GET करता है और पठनीय सामग्री निकालता है (HTML को markdown या text में)। यह JavaScript निष्पादित **नहीं** करता।

JS-प्रधान साइटों या लॉगिन-संरक्षित पेजों के लिए, इसके बजाय [वेब ब्राउज़र](</hi/tools/browser>) का उपयोग करें।

## त्वरित शुरुआत

`web_fetch` **डिफ़ॉल्ट रूप से सक्षम** है -- किसी कॉन्फ़िगरेशन की आवश्यकता नहीं। एजेंट इसे तुरंत कॉल कर सकता है:

javascriptCopy code
[code]
    await web_fetch({ url: "https://example.com/article" });
[/code]

## टूल पैरामीटर

फ़ेच करने के लिए URL। केवल `http(s)`।

मुख्य-सामग्री निष्कर्षण के बाद आउटपुट फ़ॉर्मैट।

आउटपुट को इतने वर्णों तक छोटा करें।

## यह कैसे काम करता है

* ### Fetch

Chrome-जैसे User-Agent और `Accept-Language` header के साथ HTTP GET भेजता है। निजी/आंतरिक hostnames को ब्लॉक करता है और redirects को फिर से जांचता है।

* ### Extract

HTML response पर Readability (मुख्य-सामग्री निष्कर्षण) चलाता है।

* ### Fallback (optional)

अगर Readability विफल हो जाती है और Firecrawl चुना गया है, तो bot-circumvention mode के साथ Firecrawl API के ज़रिए फिर से कोशिश करता है।

* ### Cache

परिणाम 15 मिनट तक cache किए जाते हैं (कॉन्फ़िगर किया जा सकता है), ताकि उसी URL को बार-बार fetch करने की ज़रूरत कम हो।

## प्रगति अपडेट

`web_fetch` केवल तब सार्वजनिक progress line उत्सर्जित करता है जब fetch पांच सेकंड के बाद भी pending हो:

textCopy code
[code]
    Fetching page content...
[/code]

तेज़ cache hits और त्वरित network responses timer चलने से पहले समाप्त हो जाते हैं, इसलिए वे progress line नहीं दिखाते। अगर call canceled हो जाती है, तो timer साफ़ कर दिया जाता है। जब fetch अंततः पूरा होता है, तो agent को सामान्य tool result मिलता है; progress line केवल channel UI state है और उसमें fetch किया गया page content कभी शामिल नहीं होता।

## कॉन्फ़िगरेशन

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        enabled: true, // default: true        provider: "firecrawl", // optional; omit for auto-detect        maxChars: 50000, // max output chars        maxCharsCap: 50000, // hard cap for maxChars param        maxResponseBytes: 2000000, // max download size before truncation        timeoutSeconds: 30,        cacheTtlMinutes: 15,        maxRedirects: 3,        useTrustedEnvProxy: false, // let a trusted HTTP(S) env proxy resolve DNS        readability: true, // use Readability extraction        userAgent: "Mozilla/5.0 ...", // override User-Agent        ssrfPolicy: {          allowRfc2544BenchmarkRange: true, // opt-in for trusted fake-IP proxies using 198.18.0.0/15          allowIpv6UniqueLocalRange: true, // opt-in for trusted fake-IP proxies using fc00::/7        },      },    },  },}
[/code]

## Firecrawl fallback

अगर Readability extraction विफल हो जाता है, तो `web_fetch` bot-circumvention और बेहतर extraction के लिए [Firecrawl](</hi/tools/firecrawl>) पर fallback कर सकता है:

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        provider: "firecrawl", // optional; omit for auto-detect from available credentials      },    },  },  plugins: {    entries: {      firecrawl: {        enabled: true,        config: {          webFetch: {            // apiKey: "fc-...", // optional; omit for keyless starter access            baseUrl: "https://api.firecrawl.dev",            onlyMainContent: true,            maxAgeMs: 86400000, // cache duration (1 day)            timeoutSeconds: 60,          },        },      },    },  },}
[/code]

`plugins.entries.firecrawl.config.webFetch.apiKey` वैकल्पिक है और SecretRef objects का समर्थन करता है। Legacy `tools.web.fetch.firecrawl.*` config को `openclaw doctor --fix` द्वारा auto-migrate किया जाता है।

वर्तमान runtime behavior:

  * `tools.web.fetch.provider` fetch fallback provider को स्पष्ट रूप से चुनता है।
  * अगर `provider` छोड़ा गया है, तो OpenClaw configured credentials से पहले ready web-fetch provider को auto-detect करता है। Non-sandboxed `web_fetch` ऐसे installed plugins का उपयोग कर सकता है जो `contracts.webFetchProviders` declare करते हैं और runtime पर matching provider register करते हैं। official Firecrawl Plugin यह fallback देता है।
  * Sandboxed `web_fetch` calls bundled providers और ऐसे installed providers की अनुमति देते हैं जिनकी official npm या ClawHub provenance verified है। आज यह official Firecrawl Plugin को permit करता है; third-party external fetch plugins excluded रहते हैं।
  * अगर Readability disabled है, तो `web_fetch` सीधे selected provider fallback पर जाता है। अगर कोई provider available नहीं है, तो यह सुरक्षित रूप से विफल होता है।


## Trusted env proxy

अगर आपके deployment को `web_fetch` को trusted outbound HTTP(S) proxy से गुजारना आवश्यक है, तो `tools.web.fetch.useTrustedEnvProxy: true` set करें।

इस mode में, OpenClaw request भेजने से पहले अब भी hostname-based SSRF checks लागू करता है, लेकिन local DNS pinning करने के बजाय proxy को DNS resolve करने देता है। इसे केवल तब enable करें जब proxy operator-controlled हो और DNS resolution के बाद outbound policy enforce करता हो।

## सीमाएं और सुरक्षा

  * `maxChars` को `tools.web.fetch.maxCharsCap` तक clamp किया जाता है
  * Response body को parsing से पहले `maxResponseBytes` पर cap किया जाता है; oversized responses को warning के साथ truncate किया जाता है
  * Private/internal hostnames blocked हैं
  * `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` और `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` trusted fake-IP proxy stacks के लिए संकरे opt-ins हैं; उन्हें unset छोड़ें जब तक आपका proxy उन synthetic ranges का मालिक न हो और अपनी destination policy enforce न करता हो
  * Redirects check किए जाते हैं और `maxRedirects` द्वारा limited होते हैं
  * `useTrustedEnvProxy` एक explicit opt-in है और इसे केवल operator-controlled proxies के लिए enable करना चाहिए जो DNS resolution के बाद भी outbound policy enforce करते हैं
  * `web_fetch` best-effort है -- कुछ sites को [वेब ब्राउज़र](</hi/tools/browser>) चाहिए


## टूल प्रोफ़ाइल

अगर आप tool profiles या allowlists का उपयोग करते हैं, तो `web_fetch` या `group:web` जोड़ें:

json5Copy code
[code]
    {  tools: {    allow: ["web_fetch"],    // or: allow: ["group:web"]  (includes web_fetch, web_search, and x_search)  },}
[/code]

## संबंधित

  * [वेब खोज](</hi/tools/web>) \-- कई providers के साथ web search करें
  * [वेब ब्राउज़र](</hi/tools/browser>) \-- JS-प्रधान sites के लिए full browser automation
  * [Firecrawl](</hi/tools/firecrawl>) \-- Firecrawl search और scrape tools


Was this useful?YesNo

Open issue