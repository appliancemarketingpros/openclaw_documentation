---
title: Zalo व्यक्तिगत Plugin
source_url: https://docs.openclaw.ai/hi/plugins/zalouser
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

OpenClaw के लिए Zalo Personal समर्थन, एक Plugin के माध्यम से, सामान्य Zalo उपयोगकर्ता खाते को स्वचालित करने के लिए नेटिव `zca-js` का उपयोग करते हुए.

## नामकरण

Channel id `zalouser` है ताकि यह स्पष्ट रहे कि यह एक **व्यक्तिगत Zalo उपयोगकर्ता खाते** को स्वचालित करता है (अनौपचारिक)। हम संभावित भविष्य के आधिकारिक Zalo API एकीकरण के लिए `zalo` को आरक्षित रखते हैं।

## यह कहाँ चलता है

यह Plugin **Gateway प्रक्रिया के अंदर** चलता है।

यदि आप रिमोट Gateway का उपयोग करते हैं, तो इसे **Gateway चलाने वाली मशीन** पर इंस्टॉल/कॉन्फ़िगर करें, फिर Gateway को पुनः आरंभ करें।

किसी बाहरी `zca`/`openzca` CLI बाइनरी की आवश्यकता नहीं है।

## इंस्टॉल करें

### विकल्प A: npm से इंस्टॉल करें

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

वर्तमान आधिकारिक रिलीज़ टैग का पालन करने के लिए बेयर पैकेज का उपयोग करें। सटीक संस्करण केवल तब पिन करें जब आपको पुनरुत्पाद्य इंस्टॉल की आवश्यकता हो।

इसके बाद Gateway को पुनः आरंभ करें।

### विकल्प B: स्थानीय फ़ोल्डर से इंस्टॉल करें (dev)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

इसके बाद Gateway को पुनः आरंभ करें।

## कॉन्फ़िगरेशन

Channel कॉन्फ़िगरेशन `channels.zalouser` के अंतर्गत रहता है (`plugins.entries.*` नहीं):

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## Agent टूल

टूल नाम: `zalouser`

क्रियाएँ: `send`, `image`, `link`, `friends`, `groups`, `me`, `status`

Channel संदेश क्रियाएँ संदेश प्रतिक्रियाओं के लिए `react` का भी समर्थन करती हैं।

## संबंधित

  * [Plugins बनाना](</hi/plugins/building-plugins>)
  * [ClawHub](</hi/clawhub>)


Was this useful?YesNo

Open issue