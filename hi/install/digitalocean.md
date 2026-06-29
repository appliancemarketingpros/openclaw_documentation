---
title: DigitalOcean
source_url: https://docs.openclaw.ai/hi/install/digitalocean
scraped_at: 2026-06-29
---

InstallHosting

DigitalOcean Droplet पर एक स्थायी OpenClaw Gateway चलाएं (1 GB Basic प्लान के लिए लगभग $6/माह)।

DigitalOcean सबसे सरल सशुल्क VPS रास्ता है। अगर आप सस्ते या मुफ्त विकल्प पसंद करते हैं:

  * [Hetzner](</hi/install/hetzner>) — €3.79/माह, प्रति डॉलर अधिक कोर/RAM।
  * [Oracle Cloud](</hi/install/oracle>) — Always Free ARM (4 OCPU, 24 GB RAM तक), लेकिन साइनअप थोड़ा कठिन हो सकता है और यह केवल ARM है।


## पूर्वापेक्षाएं

  * DigitalOcean खाता ([signup](<https://cloud.digitalocean.com/registrations/new>))
  * SSH कुंजी जोड़ी (या पासवर्ड auth उपयोग करने की इच्छा)
  * लगभग 20 मिनट


## सेटअप

* ### Droplet बनाएं

  1. [DigitalOcean](<https://cloud.digitalocean.com/>) में लॉग इन करें।
  2. **Create > Droplets** पर क्लिक करें।
  3. चुनें: 
     * **Region:** आपके सबसे नज़दीक
     * **Image:** Ubuntu 24.04 LTS
     * **Size:** Basic, Regular, 1 vCPU / 1 GB RAM / 25 GB SSD
     * **Authentication:** SSH कुंजी (अनुशंसित) या पासवर्ड
  4. **Create Droplet** पर क्लिक करें और IP पता नोट करें।


* ### कनेक्ट करें और इंस्टॉल करें

bashCopy code
[code]
    ssh root@YOUR_DROPLET_IP apt update && apt upgrade -y # Install Node.js 24curl -fsSL https://deb.nodesource.com/setup_24.x | bash -apt install -y nodejs # Install OpenClawcurl -fsSL https://openclaw.ai/install.sh | bash # Create the non-root user that will own OpenClaw state and services.adduser openclawusermod -aG sudo openclawloginctl enable-linger openclaw su - openclawopenclaw --version
[/code]

root shell का उपयोग केवल सिस्टम bootstrap के लिए करें। OpenClaw कमांड non-root `openclaw` उपयोगकर्ता के रूप में चलाएं ताकि state `/home/openclaw/.openclaw/` के अंतर्गत रहे और Gateway उस उपयोगकर्ता की systemd सेवा के रूप में इंस्टॉल हो।

* ### ऑनबोर्डिंग चलाएं

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

विज़ार्ड आपको model auth, चैनल सेटअप, gateway token generation, और daemon installation (systemd) से गुज़ारता है।

* ### swap जोड़ें (1 GB Droplets के लिए अनुशंसित)

bashCopy code
[code]
    fallocate -l 2G /swapfilechmod 600 /swapfilemkswap /swapfileswapon /swapfileecho '/swapfile none swap sw 0 0' >> /etc/fstab
[/code]

* ### gateway सत्यापित करें

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Control UI तक पहुंचें

gateway डिफ़ॉल्ट रूप से loopback से bind होता है। इनमें से एक विकल्प चुनें।

**विकल्प A: SSH tunnel (सबसे सरल)**

bashCopy code
[code]
    # From your local machinessh -L 18789:localhost:18789 root@YOUR_DROPLET_IP
[/code]

फिर `http://localhost:18789` खोलें।

**विकल्प B: Tailscale Serve**

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | sudo shsudo tailscale upopenclaw config set gateway.tailscale.mode serveopenclaw gateway restart
[/code]

फिर अपने tailnet पर किसी भी डिवाइस से `https://<magicdns>/` खोलें।

Tailscale Serve, tailnet identity headers के ज़रिए Control UI और WebSocket traffic को authenticate करता है, जो मानता है कि gateway host स्वयं trusted है। HTTP API endpoints, इसके बावजूद, gateway के सामान्य auth mode (token/password) का पालन करते हैं। Serve पर स्पष्ट shared-secret credentials आवश्यक करने के लिए, `gateway.auth.allowTailscale: false` सेट करें और `gateway.auth.mode: "token"` या `"password"` का उपयोग करें।

**विकल्प C: Tailnet bind (Serve नहीं)**

bashCopy code
[code]
    openclaw config set gateway.bind tailnetopenclaw gateway restart
[/code]

फिर `http://<tailscale-ip>:18789` खोलें (token आवश्यक)।

## स्थायित्व और backup

OpenClaw state यहां रहता है:

  * `~/.openclaw/` — `openclaw.json`, per-agent `auth-profiles.json`, channel/provider state, और session data।
  * `~/.openclaw/workspace/` — agent workspace (SOUL.md, memory, artifacts)।


ये Droplet reboot के बाद भी बने रहते हैं। portable snapshot लेने के लिए:

bashCopy code
[code]
    openclaw backup create
[/code]

DigitalOcean snapshots पूरे Droplet का backup लेते हैं; `openclaw backup create` hosts के बीच portable है।

## 1 GB RAM सुझाव

$6 Droplet में केवल 1 GB RAM है। चीज़ों को सुचारु रखने के लिए:

  * सुनिश्चित करें कि ऊपर दिया गया swap step `/etc/fstab` में है, ताकि यह reboots के बाद भी बना रहे।
  * स्थानीय models के बजाय API-based models (Claude, GPT) को प्राथमिकता दें — स्थानीय LLM inference 1 GB में फिट नहीं होता।
  * अगर बड़े prompts पर OOMs आते हैं तो `agents.defaults.model.primary` को छोटे model पर सेट करें।
  * `free -h` और `htop` से monitor करें।


## समस्या निवारण

**Gateway शुरू नहीं होगा** \-- `openclaw doctor --non-interactive` चलाएं और `journalctl --user -u openclaw-gateway.service -n 50` से logs जांचें।

**Port पहले से उपयोग में है** \-- process ढूंढने के लिए `lsof -i :18789` चलाएं, फिर उसे रोकें।

**Memory कम पड़ रही है** \-- `free -h` से सत्यापित करें कि swap active है। अगर फिर भी OOM आ रहा है, तो स्थानीय models के बजाय API-based models (Claude, GPT) का उपयोग करें, या 2 GB Droplet पर upgrade करें।

## अगले कदम

  * [Channels](</hi/channels>) \-- Telegram, WhatsApp, Discord, और अन्य कनेक्ट करें
  * [Gateway configuration](</hi/gateway/configuration>) \-- सभी config options
  * [Updating](</hi/install/updating>) \-- OpenClaw को up to date रखें


## संबंधित

  * [Install overview](</hi/install>)
  * [Fly.io](</hi/install/fly>)
  * [Hetzner](</hi/install/hetzner>)
  * [VPS hosting](</hi/vps>)


Was this useful?YesNo

Open issue