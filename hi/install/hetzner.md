---
title: Hetzner
source_url: https://docs.openclaw.ai/hi/install/hetzner
scraped_at: 2026-06-29
---

InstallHosting

## लक्ष्य

टिकाऊ स्थिति, अंतर्निहित बाइनरी और सुरक्षित रीस्टार्ट व्यवहार के साथ Docker का उपयोग करके Hetzner VPS पर एक लगातार चलने वाला OpenClaw Gateway चलाएँ।

यदि आप "~$5 में OpenClaw 24/7" चाहते हैं, तो यह सबसे सरल भरोसेमंद सेटअप है। Hetzner की कीमतें बदलती रहती हैं; सबसे छोटा Debian/Ubuntu VPS चुनें और यदि OOM आने लगें तो स्केल अप करें।

सुरक्षा मॉडल अनुस्मारक:

  * कंपनी-साझा एजेंट ठीक हैं जब सभी एक ही विश्वास सीमा में हों और रनटाइम केवल व्यवसाय के लिए हो।
  * कड़ा पृथक्करण रखें: समर्पित VPS/रनटाइम + समर्पित खाते; उस होस्ट पर कोई व्यक्तिगत Apple/Google/ब्राउज़र/पासवर्ड-मैनेजर प्रोफ़ाइल नहीं।
  * यदि उपयोगकर्ता एक-दूसरे के प्रति प्रतिकूल हैं, तो Gateway/होस्ट/OS उपयोगकर्ता के आधार पर अलग करें।


[सुरक्षा](</hi/gateway/security>) और [VPS होस्टिंग](</hi/vps>) देखें।

## हम क्या कर रहे हैं (सरल शब्दों में)?

  * एक छोटा Linux सर्वर किराए पर लें (Hetzner VPS)
  * Docker इंस्टॉल करें (अलग-थलग ऐप रनटाइम)
  * Docker में OpenClaw Gateway शुरू करें
  * होस्ट पर `~/.openclaw` \+ `~/.openclaw/workspace` को स्थायी रखें (रीस्टार्ट/रीबिल्ड के बाद भी बना रहता है)
  * SSH टनल के माध्यम से अपने लैपटॉप से Control UI एक्सेस करें


माउंट की गई `~/.openclaw` स्थिति में `openclaw.json`, प्रति-एजेंट `agents/<agentId>/agent/auth-profiles.json`, और `.env` शामिल हैं।

Gateway को इनके माध्यम से एक्सेस किया जा सकता है:

  * आपके लैपटॉप से SSH पोर्ट फ़ॉरवर्डिंग
  * यदि आप फ़ायरवॉलिंग और टोकन स्वयं प्रबंधित करते हैं, तो सीधा पोर्ट एक्सपोज़र


यह गाइड Hetzner पर Ubuntu या Debian मानती है।  
यदि आप किसी अन्य Linux VPS पर हैं, तो पैकेजों को उसके अनुसार मैप करें। सामान्य Docker प्रवाह के लिए, [Docker](</hi/install/docker>) देखें।

* * *

## त्वरित मार्ग (अनुभवी ऑपरेटर)

  1. Hetzner VPS प्रोविज़न करें
  2. Docker इंस्टॉल करें
  3. OpenClaw रिपॉज़िटरी क्लोन करें
  4. स्थायी होस्ट डायरेक्टरी बनाएँ
  5. `.env` और `docker-compose.yml` कॉन्फ़िगर करें
  6. आवश्यक बाइनरी को इमेज में बेक करें
  7. `docker compose up -d`
  8. स्थायित्व और Gateway एक्सेस सत्यापित करें


* * *

## आपको क्या चाहिए

  * root एक्सेस वाला Hetzner VPS
  * आपके लैपटॉप से SSH एक्सेस
  * SSH + कॉपी/पेस्ट के साथ बुनियादी सहजता
  * ~20 मिनट
  * Docker और Docker Compose
  * मॉडल ऑथ क्रेडेंशियल
  * वैकल्पिक प्रदाता क्रेडेंशियल 
    * WhatsApp QR
    * Telegram bot token
    * Gmail OAuth


* * *

* ### Provision the VPS

Hetzner में Ubuntu या Debian VPS बनाएँ।

root के रूप में कनेक्ट करें:

bashCopy code
[code]
    ssh root@YOUR_VPS_IP
[/code]

यह गाइड मानती है कि VPS स्टेटफ़ुल है। इसे डिस्पोज़ेबल इंफ़्रास्ट्रक्चर न मानें।

* ### Install Docker (on the VPS)

bashCopy code
[code]
    apt-get updateapt-get install -y git curl ca-certificatescurl -fsSL https://get.docker.com | sh
[/code]

सत्यापित करें:

bashCopy code
[code]
    docker --versiondocker compose version
[/code]

* ### Clone the OpenClaw repository

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclaw
[/code]

यह गाइड मानती है कि आप बाइनरी स्थायित्व की गारंटी के लिए एक कस्टम इमेज बनाएँगे।

* ### Create persistent host directories

Docker कंटेनर अस्थायी होते हैं। सभी लंबे समय तक रहने वाली स्थिति होस्ट पर ही रहनी चाहिए।

bashCopy code
[code]
    mkdir -p /root/.openclaw/workspace # Set ownership to the container user (uid 1000):chown -R 1000:1000 /root/.openclaw
[/code]

* ### Configure environment variables

रिपॉज़िटरी रूट में `.env` बनाएँ।

bashCopy code
[code]
    OPENCLAW_IMAGE=openclaw:latestOPENCLAW_GATEWAY_TOKEN=OPENCLAW_GATEWAY_BIND=lanOPENCLAW_GATEWAY_PORT=18789 OPENCLAW_CONFIG_DIR=/root/.openclawOPENCLAW_WORKSPACE_DIR=/root/.openclaw/workspace GOG_KEYRING_PASSWORD=XDG_CONFIG_HOME=/home/node/.openclaw
[/code]

जब आप स्थिर Gateway टोकन को `.env` के माध्यम से प्रबंधित करना चाहते हों, तब `OPENCLAW_GATEWAY_TOKEN` सेट करें; अन्यथा पुनः आरंभों के दौरान क्लाइंट पर निर्भर होने से पहले `gateway.auth.token` कॉन्फ़िगर करें। यदि कोई भी स्रोत मौजूद नहीं है, तो OpenClaw उस स्टार्टअप के लिए केवल रनटाइम टोकन का उपयोग करता है। एक कीरिंग पासवर्ड जनरेट करें और उसे `GOG_KEYRING_PASSWORD` में पेस्ट करें:

bashCopy code
[code]
    openssl rand -hex 32
[/code]

**इस फ़ाइल को कमिट न करें।**

यह `.env` फ़ाइल `OPENCLAW_GATEWAY_TOKEN` जैसे कंटेनर/रनटाइम env के लिए है। संग्रहीत प्रोवाइडर OAuth/API-key auth माउंट किए गए `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` में रहता है।

* ### Docker Compose configuration

`docker-compose.yml` बनाएँ या अपडेट करें।

yamlCopy code
[code]
    services:  openclaw-gateway:    image: ${OPENCLAW_IMAGE}    build: .    restart: unless-stopped    env_file:      - .env    environment:      - HOME=/home/node      - NODE_ENV=production      - TERM=xterm-256color      - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}      - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}      - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}      - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}      - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin    volumes:      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace    ports:      # Recommended: keep the Gateway loopback-only on the VPS; access via SSH tunnel.      # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.      - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"    command:      [        "node",        "dist/index.js",        "gateway",        "--bind",        "${OPENCLAW_GATEWAY_BIND}",        "--port",        "${OPENCLAW_GATEWAY_PORT}",        "--allow-unconfigured",      ]
[/code]

`--allow-unconfigured` केवल बूटस्ट्रैप सुविधा के लिए है, यह उचित Gateway कॉन्फ़िगरेशन का विकल्प नहीं है। फिर भी auth (`gateway.auth.token` या पासवर्ड) सेट करें और अपने डिप्लॉयमेंट के लिए सुरक्षित bind सेटिंग्स का उपयोग करें।

* ### Shared Docker VM runtime steps

सामान्य Docker होस्ट फ़्लो के लिए साझा रनटाइम गाइड का उपयोग करें:

  * [आवश्यक बाइनरी को इमेज में बेक करें](</hi/install/docker-vm-runtime#bake-required-binaries-into-the-image>)
  * [बिल्ड और लॉन्च करें](</hi/install/docker-vm-runtime#build-and-launch>)
  * [कहाँ क्या स्थायी रहता है](</hi/install/docker-vm-runtime#what-persists-where>)
  * [अपडेट](</hi/install/docker-vm-runtime#updates>)


* ### Hetzner-specific access

साझा बिल्ड और लॉन्च चरणों के बाद, टनल खोलने के लिए निम्नलिखित सेटअप पूरा करें:

**पूर्वापेक्षा:** सुनिश्चित करें कि आपका VPS sshd कॉन्फ़िग TCP forwarding की अनुमति देता है। यदि आपने अपना SSH कॉन्फ़िग मजबूत किया है, तो `/etc/ssh/sshd_config` जाँचें और सेट करें:

CodeCopy code
[code]
    AllowTcpForwarding local
[/code]

`local` आपके लैपटॉप से `ssh -L` local forwards की अनुमति देता है, जबकि सर्वर से remote forwards को ब्लॉक करता है। इसे `no` पर सेट करने से टनल इस त्रुटि के साथ विफल होगी: `channel 3: open failed: administratively prohibited: open failed`

TCP forwarding सक्षम होने की पुष्टि करने के बाद, SSH सेवा को पुनः आरंभ करें (`systemctl restart ssh`) और अपने लैपटॉप से टनल चलाएँ:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 root@YOUR_VPS_IP
[/code]

खोलें:

`http://127.0.0.1:18789/`

कॉन्फ़िगर किया गया साझा सीक्रेट पेस्ट करें। यह गाइड डिफ़ॉल्ट रूप से Gateway टोकन का उपयोग करती है; यदि आपने पासवर्ड auth पर स्विच किया है, तो इसके बजाय वह पासवर्ड उपयोग करें।

साझा persistence मानचित्र [Docker VM Runtime](</hi/install/docker-vm-runtime#what-persists-where>) में है।

## Infrastructure as Code (Terraform)

infrastructure-as-code वर्कफ़्लो पसंद करने वाली टीमों के लिए, समुदाय द्वारा अनुरक्षित Terraform सेटअप प्रदान करता है:

  * remote state management के साथ मॉड्यूलर Terraform कॉन्फ़िगरेशन
  * cloud-init के माध्यम से स्वचालित provisioning
  * डिप्लॉयमेंट स्क्रिप्ट (bootstrap, deploy, backup/restore)
  * सुरक्षा hardening (firewall, UFW, केवल-SSH access)
  * Gateway access के लिए SSH tunnel configuration


**रिपॉज़िटरी:**

  * Infrastructure: [openclaw-terraform-hetzner](<https://github.com/andreesg/openclaw-terraform-hetzner>)
  * Docker config: [openclaw-docker-config](<https://github.com/andreesg/openclaw-docker-config>)


यह तरीका ऊपर दिए गए Docker सेटअप को reproducible deployments, version-controlled infrastructure, और automated disaster recovery के साथ पूरक करता है।

## अगले चरण

  * मैसेजिंग चैनल सेट करें: [चैनल](</hi/channels>)
  * Gateway कॉन्फ़िगर करें: [Gateway कॉन्फ़िगरेशन](</hi/gateway/configuration>)
  * OpenClaw को अद्यतित रखें: [अपडेट करना](</hi/install/updating>)


## संबंधित

  * [इंस्टॉल अवलोकन](</hi/install>)
  * [Fly.io](</hi/install/fly>)
  * [Docker](</hi/install/docker>)
  * [VPS होस्टिंग](</hi/vps>)


Was this useful?YesNo

Open issue