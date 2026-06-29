---
title: Fly.io
source_url: https://docs.openclaw.ai/hi/install/fly
scraped_at: 2026-06-29
---

InstallHosting

**लक्ष्य:** स्थायी स्टोरेज, स्वचालित HTTPS, और Discord/channel एक्सेस के साथ [Fly.io](<https://fly.io>) मशीन पर चल रहा OpenClaw Gateway।

## आपको क्या चाहिए

  * [flyctl CLI](<https://fly.io/docs/hands-on/install-flyctl/>) इंस्टॉल किया हुआ
  * Fly.io खाता (फ्री टियर काम करता है)
  * मॉडल प्रमाणीकरण: आपके चुने हुए मॉडल प्रदाता के लिए API कुंजी
  * Channel क्रेडेंशियल: Discord bot टोकन, Telegram टोकन, आदि।


## शुरुआती त्वरित पथ

  1. रेपो क्लोन करें → `fly.toml` कस्टमाइज़ करें
  2. ऐप + वॉल्यूम बनाएं → सीक्रेट सेट करें
  3. `fly deploy` के साथ डिप्लॉय करें
  4. कॉन्फ़िग बनाने के लिए SSH करें या Control UI का उपयोग करें


* ### Fly ऐप बनाएं

bashCopy code
[code]
    # Clone the repogit clone https://github.com/openclaw/openclaw.gitcd openclaw # Create a new Fly app (pick your own name)fly apps create my-openclaw # Create a persistent volume (1GB is usually enough)fly volumes create openclaw_data --size 1 --region iad
[/code]

**टिप:** अपने पास का क्षेत्र चुनें। सामान्य विकल्प: `lhr` (लंदन), `iad` (वर्जीनिया), `sjc` (सैन होजे)।

* ### fly.toml कॉन्फ़िगर करें

अपने ऐप नाम और आवश्यकताओं से मेल खाने के लिए `fly.toml` संपादित करें।

**सुरक्षा नोट:** डिफ़ॉल्ट कॉन्फ़िग एक सार्वजनिक URL उजागर करता है। बिना सार्वजनिक IP वाले कठोर डिप्लॉयमेंट के लिए, निजी डिप्लॉयमेंट देखें या `deploy/fly.private.toml` का उपयोग करें।

tomlCopy code
[code]
    app = "my-openclaw"  # Your app nameprimary_region = "iad" [build]  dockerfile = "Dockerfile" [env]  NODE_ENV = "production"  OPENCLAW_PREFER_PNPM = "1"  OPENCLAW_STATE_DIR = "/data"  NODE_OPTIONS = "--max-old-space-size=1536" [processes]  app = "node dist/index.js gateway --allow-unconfigured --port 3000 --bind lan" [http_service]  internal_port = 3000  force_https = true  auto_stop_machines = false  auto_start_machines = true  min_machines_running = 1  processes = ["app"] [[vm]]  size = "shared-cpu-2x"  memory = "2048mb" [mounts]  source = "openclaw_data"  destination = "/data"
[/code]

OpenClaw Docker इमेज अपने एंट्रीपॉइंट के रूप में `tini` का उपयोग करती है। Fly प्रोसेस कमांड Docker `CMD` को बदलते हैं, `ENTRYPOINT` को नहीं, इसलिए प्रोसेस फिर भी `tini` के तहत चलता है।

**मुख्य सेटिंग्स:**

सेटिंग | क्यों  
---|---  
`--bind lan` | `0.0.0.0` से बाइंड करता है ताकि Fly का प्रॉक्सी Gateway तक पहुंच सके  
`--allow-unconfigured` | कॉन्फ़िग फ़ाइल के बिना शुरू करता है (आप बाद में एक बनाएंगे)  
`internal_port = 3000` | Fly हेल्थ चेक के लिए `--port 3000` (या `OPENCLAW_GATEWAY_PORT`) से मेल खाना चाहिए  
`memory = "2048mb"` | 512MB बहुत कम है; 2GB अनुशंसित  
`OPENCLAW_STATE_DIR = "/data"` | वॉल्यूम पर स्टेट बनाए रखता है  
  
* ### सीक्रेट सेट करें

bashCopy code
[code]
    # Required: Gateway token (for non-loopback binding)fly secrets set OPENCLAW_GATEWAY_TOKEN=$(openssl rand -hex 32) # Model provider API keysfly secrets set ANTHROPIC_API_KEY=example-anthropic-key-not-real # Optional: Other providersfly secrets set OPENAI_API_KEY=example-openai-key-not-realfly secrets set GOOGLE_API_KEY=... # Channel tokensfly secrets set DISCORD_BOT_TOKEN=example-discord-bot-token
[/code]

**नोट्स:**

  * Non-loopback बाइंड (`--bind lan`) के लिए मान्य Gateway प्रमाणीकरण पथ आवश्यक है। यह Fly.io उदाहरण `OPENCLAW_GATEWAY_TOKEN` का उपयोग करता है, लेकिन `gateway.auth.password` या सही ढंग से कॉन्फ़िगर किया गया non-loopback `trusted-proxy` डिप्लॉयमेंट भी आवश्यकता पूरी करता है।
  * इन टोकन को पासवर्ड की तरह संभालें।
  * **सभी API कुंजियों और टोकन के लिए कॉन्फ़िग फ़ाइल की बजाय env vars को प्राथमिकता दें** । इससे सीक्रेट `openclaw.json` से बाहर रहते हैं, जहां वे गलती से उजागर या लॉग हो सकते हैं।


* ### डिप्लॉय करें

bashCopy code
[code]
    fly deploy
[/code]

पहला डिप्लॉय Docker इमेज बनाता है (~2-3 मिनट)। बाद के डिप्लॉय तेज़ होते हैं।

डिप्लॉयमेंट के बाद, सत्यापित करें:

bashCopy code
[code]
    fly statusfly logs
[/code]

आपको यह दिखना चाहिए:

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:3000 (PID xxx)[discord] logged in to discord as xxx
[/code]

* ### कॉन्फ़िग फ़ाइल बनाएं

उचित कॉन्फ़िग बनाने के लिए मशीन में SSH करें:

bashCopy code
[code]
    fly ssh console
[/code]

कॉन्फ़िग डायरेक्टरी और फ़ाइल बनाएं:

bashCopy code
[code]
    mkdir -p /datacat > /data/openclaw.json << 'EOF'{  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-opus-4-6",        "fallbacks": ["anthropic/claude-sonnet-4-6", "openai/gpt-5.4"]      },      "maxConcurrent": 4    },    "list": [      {        "id": "main",        "default": true      }    ]  },  "auth": {    "profiles": {      "anthropic:default": { "mode": "token", "provider": "anthropic" },      "openai:default": { "mode": "token", "provider": "openai" }    }  },  "bindings": [    {      "agentId": "main",      "match": { "channel": "discord" }    }  ],  "channels": {    "discord": {      "enabled": true,      "groupPolicy": "allowlist",      "guilds": {        "YOUR_GUILD_ID": {          "channels": { "general": { "allow": true } },          "requireMention": false        }      }    }  },  "gateway": {    "mode": "local",    "bind": "auto",    "controlUi": {      "allowedOrigins": [        "https://my-openclaw.fly.dev",        "http://localhost:3000",        "http://127.0.0.1:3000"      ]    }  },  "meta": {}}EOF
[/code]

**नोट:** `OPENCLAW_STATE_DIR=/data` के साथ, कॉन्फ़िग पथ `/data/openclaw.json` है।

**नोट:** `https://my-openclaw.fly.dev` को अपने वास्तविक Fly ऐप origin से बदलें। Gateway स्टार्टअप runtime `--bind` और `--port` मानों से स्थानीय Control UI origins सीड करता है ताकि पहला बूट कॉन्फ़िग मौजूद होने से पहले आगे बढ़ सके, लेकिन Fly के जरिए ब्राउज़र एक्सेस के लिए फिर भी `gateway.controlUi.allowedOrigins` में सूचीबद्ध सटीक HTTPS origin चाहिए।

**नोट:** Discord टोकन इनमें से किसी से आ सकता है:

  * Environment variable: `DISCORD_BOT_TOKEN` (सीक्रेट के लिए अनुशंसित)
  * कॉन्फ़िग फ़ाइल: `channels.discord.token`


यदि env var का उपयोग कर रहे हैं, तो कॉन्फ़िग में टोकन जोड़ने की आवश्यकता नहीं है। Gateway `DISCORD_BOT_TOKEN` को स्वचालित रूप से पढ़ता है।

लागू करने के लिए रीस्टार्ट करें:

bashCopy code
[code]
    exitfly machine restart <machine-id>
[/code]

* ### Gateway एक्सेस करें

### Control UI

ब्राउज़र में खोलें:

bashCopy code
[code]
    fly open
[/code]

या `https://my-openclaw.fly.dev/` पर जाएं

कॉन्फ़िगर किए गए साझा सीक्रेट से प्रमाणीकरण करें। यह गाइड Gateway टोकन `OPENCLAW_GATEWAY_TOKEN` से उपयोग करता है; यदि आपने पासवर्ड प्रमाणीकरण पर स्विच किया है, तो उसके बजाय वह पासवर्ड उपयोग करें।

### लॉग

bashCopy code
[code]
    fly logs              # Live logsfly logs --no-tail    # Recent logs
[/code]

### SSH कंसोल

bashCopy code
[code]
    fly ssh console
[/code]

## समस्या निवारण

### "App is not listening on expected address"

Gateway `0.0.0.0` के बजाय `127.0.0.1` से बाइंड हो रहा है।

**समाधान:** `fly.toml` में अपने प्रोसेस कमांड में `--bind lan` जोड़ें।

### हेल्थ चेक विफल / कनेक्शन अस्वीकार

Fly कॉन्फ़िगर किए गए पोर्ट पर Gateway तक नहीं पहुंच सकता।

**समाधान:** सुनिश्चित करें कि `internal_port` Gateway पोर्ट से मेल खाता है (`--port 3000` या `OPENCLAW_GATEWAY_PORT=3000` सेट करें)।

### OOM / मेमोरी समस्याएं

कंटेनर बार-बार रीस्टार्ट हो रहा है या समाप्त किया जा रहा है। संकेत: `SIGABRT`, `v8::internal::Runtime_AllocateInYoungGeneration`, या बिना संदेश के रीस्टार्ट।

**समाधान:** `fly.toml` में मेमोरी बढ़ाएं:

tomlCopy code
[code]
    [[vm]]  memory = "2048mb"
[/code]

या मौजूदा मशीन अपडेट करें:

bashCopy code
[code]
    fly machine update <machine-id> --vm-memory 2048 -y
[/code]

**नोट:** 512MB बहुत कम है। 1GB काम कर सकता है लेकिन लोड के तहत या विस्तृत लॉगिंग के साथ OOM हो सकता है। **2GB अनुशंसित है।**

### Gateway लॉक समस्याएं

Gateway "already running" त्रुटियों के साथ शुरू होने से इनकार करता है।

यह तब होता है जब कंटेनर रीस्टार्ट होता है लेकिन PID लॉक फ़ाइल वॉल्यूम पर बनी रहती है।

**समाधान:** लॉक फ़ाइल हटाएं:

bashCopy code
[code]
    fly ssh console --command "rm -f /data/gateway.*.lock"fly machine restart <machine-id>
[/code]

लॉक फ़ाइल `/data/gateway.*.lock` पर है (किसी सबडायरेक्टरी में नहीं)।

### कॉन्फ़िग पढ़ा नहीं जा रहा

`--allow-unconfigured` केवल स्टार्टअप गार्ड को बायपास करता है। यह `/data/openclaw.json` बनाता या सुधारता नहीं है, इसलिए सुनिश्चित करें कि आपका वास्तविक कॉन्फ़िग मौजूद है और सामान्य स्थानीय Gateway स्टार्ट चाहने पर उसमें `gateway.mode="local"` शामिल है।

कॉन्फ़िग मौजूद है यह सत्यापित करें:

bashCopy code
[code]
    fly ssh console --command "cat /data/openclaw.json"
[/code]

### SSH के जरिए कॉन्फ़िग लिखना

`fly ssh console -C` कमांड शेल रीडायरेक्शन का समर्थन नहीं करता। कॉन्फ़िग फ़ाइल लिखने के लिए:

bashCopy code
[code]
    # Use echo + tee (pipe from local to remote)echo '{"your":"config"}' | fly ssh console -C "tee /data/openclaw.json" # Or use sftpfly sftp shell> put /local/path/config.json /data/openclaw.json
[/code]

**नोट:** यदि फ़ाइल पहले से मौजूद है तो `fly sftp` विफल हो सकता है। पहले हटाएं:

bashCopy code
[code]
    fly ssh console --command "rm /data/openclaw.json"
[/code]

### स्टेट कायम नहीं रह रहा

यदि रीस्टार्ट के बाद auth profiles, channel/provider स्टेट, या sessions खो जाते हैं, तो स्टेट dir कंटेनर फ़ाइलसिस्टम पर लिख रहा है।

**समाधान:** सुनिश्चित करें कि `fly.toml` में `OPENCLAW_STATE_DIR=/data` सेट है और फिर से डिप्लॉय करें।

## अपडेट

bashCopy code
[code]
    # Pull latest changesgit pull # Redeployfly deploy # Check healthfly statusfly logs
[/code]

### मशीन कमांड अपडेट करना

यदि आपको पूर्ण रीडिप्लॉय के बिना स्टार्टअप कमांड बदलना हो:

bashCopy code
[code]
    # Get machine IDfly machines list # Update commandfly machine update <machine-id> --command "node dist/index.js gateway --port 3000 --bind lan" -y # Or with memory increasefly machine update <machine-id> --vm-memory 2048 --command "node dist/index.js gateway --port 3000 --bind lan" -y
[/code]

**नोट:** `fly deploy` के बाद, मशीन कमांड `fly.toml` में मौजूद कमांड पर रीसेट हो सकता है। यदि आपने मैन्युअल बदलाव किए हैं, तो डिप्लॉय के बाद उन्हें फिर से लागू करें।

## निजी डिप्लॉयमेंट (कठोर)

डिफ़ॉल्ट रूप से, Fly सार्वजनिक IP आवंटित करता है, जिससे आपका Gateway `https://your-app.fly.dev` पर एक्सेस योग्य हो जाता है। यह सुविधाजनक है लेकिन इसका मतलब है कि आपका डिप्लॉयमेंट इंटरनेट स्कैनरों (Shodan, Censys, आदि) द्वारा खोजा जा सकता है।

**कोई सार्वजनिक एक्सपोज़र नहीं** वाले कठोर डिप्लॉयमेंट के लिए, निजी टेम्पलेट का उपयोग करें।

### निजी डिप्लॉयमेंट कब उपयोग करें

  * आप केवल **आउटबाउंड** कॉल/संदेश करते हैं (कोई इनबाउंड Webhook नहीं)
  * आप किसी भी Webhook कॉलबैक के लिए **ngrok या Tailscale** टनल उपयोग करते हैं
  * आप ब्राउज़र के बजाय **SSH, प्रॉक्सी, या WireGuard** के जरिए Gateway एक्सेस करते हैं
  * आप डिप्लॉयमेंट को **इंटरनेट स्कैनरों से छिपा हुआ** रखना चाहते हैं


### सेटअप

मानक कॉन्फ़िग के बजाय `deploy/fly.private.toml` उपयोग करें:

bashCopy code
[code]
    # Deploy with private configfly deploy -c deploy/fly.private.toml
[/code]

या मौजूदा डिप्लॉयमेंट को कन्वर्ट करें:

bashCopy code
[code]
    # List current IPsfly ips list -a my-openclaw # Release public IPsfly ips release <public-ipv4> -a my-openclawfly ips release <public-ipv6> -a my-openclaw # Switch to private config so future deploys don't re-allocate public IPs# (remove [http_service] or deploy with the private template)fly deploy -c deploy/fly.private.toml # Allocate private-only IPv6fly ips allocate-v6 --private -a my-openclaw
[/code]

इसके बाद, `fly ips list` में केवल `private` प्रकार का IP दिखना चाहिए:

CodeCopy code
[code]
    VERSION  IP                   TYPE             REGIONv6       fdaa:x:x:x:x::x      private          global
[/code]

### निजी डिप्लॉयमेंट एक्सेस करना

क्योंकि कोई सार्वजनिक URL नहीं है, इनमें से किसी विधि का उपयोग करें:

**विकल्प 1: स्थानीय प्रॉक्सी (सबसे सरल)**

bashCopy code
[code]
    # Forward local port 3000 to the appfly proxy 3000:3000 -a my-openclaw # Then open http://localhost:3000 in browser
[/code]

**विकल्प 2: WireGuard VPN**

bashCopy code
[code]
    # Create WireGuard config (one-time)fly wireguard create # Import to WireGuard client, then access via internal IPv6# Example: http://[fdaa:x:x:x:x::x]:3000
[/code]

**विकल्प 3: केवल SSH**

bashCopy code
[code]
    fly ssh console -a my-openclaw
[/code]

### निजी डिप्लॉयमेंट के साथ Webhook

अगर आपको सार्वजनिक एक्सपोज़र के बिना Webhook callback (Twilio, Telnyx, आदि) चाहिए:

  1. **ngrok tunnel** \- कंटेनर के अंदर या sidecar के रूप में ngrok चलाएँ
  2. **Tailscale Funnel** \- Tailscale के ज़रिए विशिष्ट पाथ एक्सपोज़ करें
  3. **केवल आउटबाउंड** \- कुछ provider (Twilio) Webhook के बिना आउटबाउंड call के लिए ठीक काम करते हैं


ngrok के साथ voice-call config का उदाहरण:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          provider: "twilio",          tunnel: { provider: "ngrok" },          webhookSecurity: {            allowedHosts: ["example.ngrok.app"],          },        },      },    },  },}
[/code]

ngrok tunnel कंटेनर के अंदर चलता है और Fly app को स्वयं एक्सपोज़ किए बिना एक सार्वजनिक Webhook URL देता है। `webhookSecurity.allowedHosts` को सार्वजनिक tunnel hostname पर सेट करें ताकि forwarded host header स्वीकार किए जाएँ।

### सुरक्षा लाभ

पहलू | सार्वजनिक | निजी  
---|---|---  
इंटरनेट scanner | खोजे जा सकने योग्य | छिपा हुआ  
सीधे हमले | संभव | अवरुद्ध  
Control UI पहुँच | Browser | Proxy/VPN  
Webhook डिलीवरी | सीधे | tunnel के ज़रिए  
  
## नोट्स

  * Fly.io **x86 architecture** का उपयोग करता है (ARM नहीं)
  * Dockerfile दोनों architecture के साथ संगत है
  * WhatsApp/Telegram onboarding के लिए, `fly ssh console` उपयोग करें
  * स्थायी data `/data` पर volume में रहता है
  * Signal को Java + signal-cli की आवश्यकता होती है; custom image उपयोग करें और memory 2GB+ रखें।


## लागत

अनुशंसित config (`shared-cpu-2x`, 2GB RAM) के साथ:

  * उपयोग के आधार पर लगभग ~$10-15/माह
  * free tier में कुछ allowance शामिल है


विवरण के लिए [Fly.io pricing](<https://fly.io/docs/about/pricing/>) देखें।

## अगले चरण

  * messaging channel सेट करें: [Channels](</hi/channels>)
  * Gateway configure करें: [Gateway configuration](</hi/gateway/configuration>)
  * OpenClaw को up to date रखें: [Updating](</hi/install/updating>)


## संबंधित

  * [Install overview](</hi/install>)
  * [Hetzner](</hi/install/hetzner>)
  * [Docker](</hi/install/docker>)
  * [VPS hosting](</hi/vps>)


Was this useful?YesNo

Open issue