---
title: वेब
source_url: https://docs.openclaw.ai/hi/web
scraped_at: 2026-06-29
---

Gateway & OpsWeb interfaces

Gateway, Gateway WebSocket वाले उसी पोर्ट से एक छोटा **ब्राउज़र नियंत्रण UI** (Vite + Lit) सर्व करता है:

  * डिफ़ॉल्ट: `http://<host>:18789/`
  * `gateway.tls.enabled: true` के साथ: `https://<host>:18789/`
  * वैकल्पिक प्रीफ़िक्स: `gateway.controlUi.basePath` सेट करें (उदा. `/openclaw`)


क्षमताएँ [नियंत्रण UI](</hi/web/control-ui>) में हैं। इस पेज का बाकी भाग बाइंड मोड, सुरक्षा, और वेब-फेसिंग सतहों पर केंद्रित है.

## Webhooks

जब `hooks.enabled=true` हो, Gateway उसी HTTP सर्वर पर एक छोटा Webhook एंडपॉइंट भी एक्सपोज़ करता है। auth + payloads के लिए [Gateway कॉन्फ़िगरेशन](</hi/gateway/configuration>) → `hooks` देखें।

## एडमिन HTTP RPC

एडमिन HTTP RPC, चुनी गई Gateway कंट्रोल-प्लेन विधियों को `POST /api/v1/admin/rpc` पर एक्सपोज़ करता है। यह डिफ़ॉल्ट रूप से बंद होता है और केवल तब रजिस्टर होता है जब `admin-http-rpc` plugin सक्षम हो। auth मॉडल, अनुमत विधियों, और WebSocket तुलना के लिए [एडमिन HTTP RPC](</hi/plugins/admin-http-rpc>) देखें।

## कॉन्फ़िग (डिफ़ॉल्ट रूप से चालू)

एसेट मौजूद होने पर (`dist/control-ui`) नियंत्रण UI **डिफ़ॉल्ट रूप से सक्षम** होता है। आप इसे कॉन्फ़िग के ज़रिए नियंत्रित कर सकते हैं:

json5Copy code
[code]
    {  gateway: {    controlUi: { enabled: true, basePath: "/openclaw" }, // basePath optional  },}
[/code]

## Tailscale एक्सेस

### इंटीग्रेटेड Serve (अनुशंसित)

Gateway को loopback पर रखें और Tailscale Serve को उसे प्रॉक्सी करने दें:

json5Copy code
[code]
    {  gateway: {    bind: "loopback",    tailscale: { mode: "serve" },  },}
[/code]

फिर gateway शुरू करें:

bashCopy code
[code]
    openclaw gateway
[/code]

खोलें:

  * `https://<magicdns>/` (या आपका कॉन्फ़िगर किया गया `gateway.controlUi.basePath`)


### Tailnet बाइंड + टोकन

json5Copy code
[code]
    {  gateway: {    bind: "tailnet",    controlUi: { enabled: true },    auth: { mode: "token", token: "your-token" },  },}
[/code]

फिर gateway शुरू करें (यह गैर-loopback उदाहरण shared-secret टोकन auth का उपयोग करता है):

bashCopy code
[code]
    openclaw gateway
[/code]

खोलें:

  * `http://<tailscale-ip>:18789/` (या आपका कॉन्फ़िगर किया गया `gateway.controlUi.basePath`)


### सार्वजनिक इंटरनेट (Funnel)

json5Copy code
[code]
    {  gateway: {    bind: "loopback",    tailscale: { mode: "funnel" },    auth: { mode: "password" }, // or OPENCLAW_GATEWAY_PASSWORD  },}
[/code]

## सुरक्षा नोट्स

  * Gateway auth डिफ़ॉल्ट रूप से आवश्यक है (टोकन, पासवर्ड, trusted-proxy, या सक्षम होने पर Tailscale Serve पहचान हेडर).
  * गैर-loopback बाइंड में अभी भी gateway auth **आवश्यक** है। व्यवहार में इसका मतलब टोकन/पासवर्ड auth या `gateway.auth.mode: "trusted-proxy"` के साथ पहचान-सचेत रिवर्स प्रॉक्सी है।
  * विज़ार्ड डिफ़ॉल्ट रूप से shared-secret auth बनाता है और आम तौर पर एक gateway टोकन जनरेट करता है (loopback पर भी).
  * shared-secret मोड में, UI `connect.params.auth.token` या `connect.params.auth.password` भेजता है।
  * जब `gateway.tls.enabled: true` हो, तो स्थानीय डैशबोर्ड और स्थिति हेल्पर `https://` डैशबोर्ड URL और `wss://` WebSocket URL रेंडर करते हैं।
  * Tailscale Serve या `trusted-proxy` जैसे पहचान-युक्त मोड में, WebSocket auth जांच इसके बजाय अनुरोध हेडर से पूरी होती है।
  * सार्वजनिक गैर-loopback नियंत्रण UI डिप्लॉयमेंट के लिए, `gateway.controlUi.allowedOrigins` स्पष्ट रूप से सेट करें (पूर्ण origins)। loopback, RFC1918/link-local, `.local`, `.ts.net`, और Tailscale CGNAT होस्ट के लिए निजी same-origin LAN/Tailnet लोड स्वीकार किए जाते हैं।
  * `gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback=true`, Host-header origin fallback मोड सक्षम करता है, लेकिन यह एक खतरनाक सुरक्षा डाउनग्रेड है।
  * Serve के साथ, जब `gateway.auth.allowTailscale` `true` हो, तो Tailscale पहचान हेडर नियंत्रण UI/WebSocket auth पूरा कर सकते हैं (टोकन/पासवर्ड आवश्यक नहीं). HTTP API एंडपॉइंट उन Tailscale पहचान हेडर का उपयोग नहीं करते; वे इसके बजाय gateway के सामान्य HTTP auth मोड का पालन करते हैं। स्पष्ट credentials आवश्यक करने के लिए `gateway.auth.allowTailscale: false` सेट करें। [Tailscale](</hi/gateway/tailscale>) और [सुरक्षा](</hi/gateway/security>) देखें। यह टोकन-रहित प्रवाह मानता है कि gateway होस्ट भरोसेमंद है।
  * `gateway.tailscale.mode: "funnel"` के लिए `gateway.auth.mode: "password"` (shared password) आवश्यक है।


## UI बनाना

Gateway `dist/control-ui` से static फ़ाइलें सर्व करता है। उन्हें इससे बिल्ड करें:

bashCopy code
[code]
    pnpm ui:build
[/code]

Was this useful?YesNo

Open issue