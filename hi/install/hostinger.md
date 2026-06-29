---
title: Hostinger
source_url: https://docs.openclaw.ai/hi/install/hostinger
scraped_at: 2026-06-29
---

InstallHosting

[Hostinger](<https://www.hostinger.com/openclaw>) पर **1-Click** managed deployment या **VPS** install के माध्यम से एक persistent OpenClaw Gateway चलाएं।

## आवश्यकताएं

  * Hostinger account ([signup](<https://www.hostinger.com/openclaw>))
  * लगभग 5-10 मिनट


## विकल्प A: 1-Click OpenClaw

शुरू करने का सबसे तेज तरीका। Hostinger infrastructure, Docker, और automatic updates संभालता है।

* ### खरीदें और लॉन्च करें

  1. [Hostinger OpenClaw page](<https://www.hostinger.com/openclaw>) से, Managed OpenClaw plan चुनें और checkout पूरा करें।


* ### Messaging channel चुनें

connect करने के लिए एक या अधिक channels चुनें:

  * **WhatsApp** \-- setup wizard में दिखाया गया QR code scan करें।
  * **Telegram** \-- [BotFather](<https://t.me/BotFather>) से bot token paste करें।


* ### Installation पूरा करें

instance deploy करने के लिए **Finish** पर click करें। Ready होने पर, hPanel में **OpenClaw Overview** से OpenClaw dashboard access करें।

## विकल्प B: VPS पर OpenClaw

अपने server पर अधिक control। Hostinger आपके VPS पर Docker के माध्यम से OpenClaw deploy करता है और आप hPanel में **Docker Manager** के जरिए इसे manage करते हैं।

* ### VPS खरीदें

  1. [Hostinger OpenClaw page](<https://www.hostinger.com/openclaw>) से, OpenClaw on VPS plan चुनें और checkout पूरा करें।


* ### OpenClaw configure करें

VPS provision होने के बाद, configuration fields भरें:

  * **Gateway token** \-- auto-generated; इसे बाद में उपयोग के लिए save करें।
  * **WhatsApp number** \-- country code के साथ आपका number (optional)।
  * **Telegram bot token** \-- [BotFather](<https://t.me/BotFather>) से (optional)।
  * **API keys** \-- केवल तब जरूरी जब आपने checkout के दौरान Ready-to-Use AI credits नहीं चुने हों।


* ### OpenClaw start करें

**Deploy** पर click करें। Running होने पर, **Open** पर click करके hPanel से OpenClaw dashboard खोलें।

Logs, restarts, और updates hPanel में Docker Manager interface से सीधे managed होते हैं। Update करने के लिए, Docker Manager में **Update** दबाएं और वह latest image pull करेगा।

## अपना setup verify करें

जिस channel को आपने connect किया है, उस पर अपने assistant को "Hi" भेजें। OpenClaw reply करेगा और आपको initial preferences के बारे में guide करेगा।

## Troubleshooting

**Dashboard load नहीं हो रहा** \-- Container provisioning पूरा होने के लिए कुछ मिनट प्रतीक्षा करें। hPanel में Docker Manager logs check करें।

**Docker container बार-बार restart हो रहा है** \-- Docker Manager logs खोलें और configuration errors देखें (missing tokens, invalid API keys)।

**Telegram bot respond नहीं कर रहा** \-- Connection पूरा करने के लिए Telegram से अपना pairing code message सीधे अपने OpenClaw chat के अंदर message के रूप में भेजें।

## अगले steps

  * [Channels](</hi/channels>) \-- Telegram, WhatsApp, Discord, और अधिक connect करें
  * [Gateway configuration](</hi/gateway/configuration>) \-- सभी config options


## संबंधित

  * [Install overview](</hi/install>)
  * [VPS hosting](</hi/vps>)
  * [DigitalOcean](</hi/install/digitalocean>)


Was this useful?YesNo

Open issue