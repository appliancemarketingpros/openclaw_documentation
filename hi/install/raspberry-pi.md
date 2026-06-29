---
title: Raspberry Pi
source_url: https://docs.openclaw.ai/hi/install/raspberry-pi
scraped_at: 2026-06-29
---

InstallHosting

Raspberry Pi पर एक लगातार चलने वाला, हमेशा-ऑन OpenClaw Gateway चलाएं। चूंकि Pi सिर्फ Gateway है (मॉडल API के जरिए क्लाउड में चलते हैं), इसलिए साधारण Pi भी वर्कलोड अच्छी तरह संभाल लेता है — सामान्य हार्डवेयर लागत **$35–80 एक बार** , कोई मासिक शुल्क नहीं।

## हार्डवेयर संगतता

Pi मॉडल | RAM | काम करता है? | टिप्पणियां  
---|---|---|---  
Pi 5 | 4/8 GB | सबसे अच्छा | सबसे तेज, अनुशंसित।  
Pi 4 | 4 GB | अच्छा | अधिकांश उपयोगकर्ताओं के लिए सही।  
Pi 4 | 2 GB | ठीक | swap जोड़ें।  
Pi 4 | 1 GB | सीमित | swap और न्यूनतम config के साथ संभव।  
Pi 3B+ | 1 GB | धीमा | काम करता है लेकिन सुस्त है।  
Pi Zero 2 W | 512 MB | नहीं | अनुशंसित नहीं।  
  
**न्यूनतम:** 1 GB RAM, 1 core, 500 MB खाली disk, 64-bit OS। **अनुशंसित:** 2 GB+ RAM, 16 GB+ SD card (या USB SSD), Ethernet।

## पूर्वापेक्षाएं

  * 2 GB+ RAM वाला Raspberry Pi 4 या 5 (4 GB अनुशंसित)
  * MicroSD card (16 GB+) या USB SSD (बेहतर प्रदर्शन)
  * आधिकारिक Pi power supply
  * नेटवर्क कनेक्शन (Ethernet या WiFi)
  * 64-bit Raspberry Pi OS (आवश्यक -- 32-bit का उपयोग न करें)
  * लगभग 30 मिनट


## सेटअप

* ### OS फ्लैश करें

headless server के लिए **Raspberry Pi OS Lite (64-bit)** का उपयोग करें -- desktop की जरूरत नहीं।

  1. [Raspberry Pi Imager](<https://www.raspberrypi.com/software/>) डाउनलोड करें।
  2. OS चुनें: **Raspberry Pi OS Lite (64-bit)** ।
  3. settings dialog में, पहले से config करें: 
     * Hostname: `gateway-host`
     * SSH सक्षम करें
     * username और password सेट करें
     * WiFi config करें (यदि Ethernet का उपयोग नहीं कर रहे हैं)
  4. अपने SD card या USB drive पर फ्लैश करें, उसे लगाएं, और Pi को boot करें।


* ### SSH के जरिए connect करें

bashCopy code
[code]
    ssh user@gateway-host
[/code]

* ### system अपडेट करें

bashCopy code
[code]
    sudo apt update && sudo apt upgrade -ysudo apt install -y git curl build-essential # Set timezone (important for cron and reminders)sudo timedatectl set-timezone America/Chicago
[/code]

* ### Node.js 24 install करें

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt install -y nodejsnode --version
[/code]

* ### swap जोड़ें (2 GB या उससे कम के लिए महत्वपूर्ण)

bashCopy code
[code]
    sudo fallocate -l 2G /swapfilesudo chmod 600 /swapfilesudo mkswap /swapfilesudo swapon /swapfileecho '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab # Reduce swappiness for low-RAM devicesecho 'vm.swappiness=10' | sudo tee -a /etc/sysctl.confsudo sysctl -p
[/code]

* ### OpenClaw install करें

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

* ### onboarding चलाएं

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

wizard का पालन करें। headless devices के लिए OAuth की तुलना में API keys अनुशंसित हैं। शुरुआत के लिए Telegram सबसे आसान channel है।

* ### सत्यापित करें

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Control UI तक पहुंचें

अपने computer पर, Pi से dashboard URL प्राप्त करें:

bashCopy code
[code]
    ssh user@gateway-host 'openclaw dashboard --no-open'
[/code]

फिर दूसरे terminal में SSH tunnel बनाएं:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@gateway-host
[/code]

प्रिंट किए गए URL को अपने local browser में खोलें। हमेशा-ऑन remote access के लिए, [Tailscale integration](</hi/gateway/tailscale>) देखें।

## प्रदर्शन टिप्स

**USB SSD का उपयोग करें** \-- SD cards धीमे होते हैं और घिस जाते हैं। USB SSD प्रदर्शन को बहुत बेहतर बनाता है। [Pi USB boot guide](<https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#usb-mass-storage-boot>) देखें।

**module compile cache सक्षम करें** \-- कम-power Pi hosts पर बार-बार CLI चलाने की गति बढ़ाता है:

bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF' # pragma: allowlist secretexport NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

`OPENCLAW_NO_RESPAWN=1` नियमित Gateway restarts को in-process रखता है, जिससे अतिरिक्त process handoffs से बचा जाता है और छोटे hosts पर PID tracking सरल रहती है।

**memory usage घटाएं** \-- headless setups के लिए, GPU memory खाली करें और unused services disable करें:

bashCopy code
[code]
    echo 'gpu_mem=16' | sudo tee -a /boot/config.txtsudo systemctl disable bluetooth
[/code]

**स्थिर restarts के लिए systemd drop-in** \-- यदि यह Pi ज्यादातर OpenClaw चला रहा है, तो service drop-in जोड़ें:

bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

फिर `systemctl --user daemon-reload && systemctl --user restart openclaw-gateway.service`। headless Pi पर, lingering भी एक बार enable करें ताकि user service logout के बाद भी चलती रहे: `sudo loginctl enable-linger "$(whoami)"`।

## अनुशंसित model setup

चूंकि Pi केवल Gateway चलाता है, cloud-hosted API models का उपयोग करें:

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-sonnet-4-6",        "fallbacks": ["openai/gpt-5.4-mini"]      }    }  }}
[/code]

Pi पर local LLMs न चलाएं — छोटे models भी उपयोगी होने के लिए बहुत धीमे हैं। model का काम Claude या GPT को करने दें।

## ARM binary notes

अधिकांश OpenClaw features ARM64 पर बिना बदलाव के काम करते हैं (Node.js, Telegram, WhatsApp/Baileys, Chromium)। जिन binaries में कभी-कभी ARM builds नहीं होते, वे आमतौर पर Skills द्वारा भेजे गए वैकल्पिक Go/Rust CLI tools होते हैं। source से build करने से पहले missing binary के release page पर `linux-arm64` / `aarch64` artifacts सत्यापित करें।

## Persistence और backups

OpenClaw state यहां रहता है:

  * `~/.openclaw/` — `openclaw.json`, per-agent `auth-profiles.json`, channel/provider state, sessions।
  * `~/.openclaw/workspace/` — agent workspace (SOUL.md, memory, artifacts)।


ये reboots के बाद भी बने रहते हैं। portable snapshot लें:

bashCopy code
[code]
    openclaw backup create
[/code]

यदि आप इन्हें SSD पर रखते हैं, तो SD card की तुलना में performance और longevity दोनों बेहतर होते हैं।

## Troubleshooting

**Memory खत्म होना** \-- `free -h` से सत्यापित करें कि swap active है। unused services disable करें (`sudo systemctl disable cups bluetooth avahi-daemon`)। केवल API-based models का उपयोग करें।

**धीमा performance** \-- SD card की जगह USB SSD का उपयोग करें। CPU throttling की जांच `vcgencmd get_throttled` से करें (इसे `0x0` लौटाना चाहिए)।

**Service start नहीं होगी** \-- logs को `journalctl --user -u openclaw-gateway.service --no-pager -n 100` से जांचें और `openclaw doctor --non-interactive` चलाएं। यदि यह headless Pi है, तो यह भी सत्यापित करें कि lingering enabled है: `sudo loginctl enable-linger "$(whoami)"`।

**ARM binary issues** \-- यदि कोई skill "exec format error" के साथ विफल होती है, तो जांचें कि binary का ARM64 build है या नहीं। architecture को `uname -m` से सत्यापित करें (इसे `aarch64` दिखाना चाहिए)।

**WiFi drops** \-- WiFi power management disable करें: `sudo iwconfig wlan0 power off`।

## अगले चरण

  * [Channels](</hi/channels>) \-- Telegram, WhatsApp, Discord और अधिक connect करें
  * [Gateway configuration](</hi/gateway/configuration>) \-- सभी config options
  * [Updating](</hi/install/updating>) \-- OpenClaw को up to date रखें


## संबंधित

  * [Install overview](</hi/install>)
  * [Linux server](</hi/vps>)
  * [Platforms](</hi/platforms>)


Was this useful?YesNo

Open issue