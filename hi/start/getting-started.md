---
title: शुरुआत करें
source_url: https://docs.openclaw.ai/hi/start/getting-started
scraped_at: 2026-06-29
---

Get startedFirst steps

OpenClaw इंस्टॉल करें, ऑनबोर्डिंग चलाएँ, और अपने AI सहायक से चैट करें — सब कुछ लगभग 5 मिनट में। अंत तक आपके पास चलता हुआ Gateway, कॉन्फ़िगर किया गया प्रमाणीकरण, और एक काम करता हुआ चैट सत्र होगा।

## आपको क्या चाहिए

  * **Node.js** — Node 24 अनुशंसित है (Node 22.19+ भी समर्थित है)
  * मॉडल प्रदाता (Anthropic, OpenAI, Google, आदि) से **एक API key** — ऑनबोर्डिंग आपसे पूछेगी


## त्वरित सेटअप

* ### Install OpenClaw

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![Install Script Process](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

विज़ार्ड आपको मॉडल प्रदाता चुनने, API key सेट करने, और Gateway कॉन्फ़िगर करने की प्रक्रिया से गुज़ारता है। QuickStart में आम तौर पर केवल कुछ मिनट लगते हैं, लेकिन प्रदाता साइन-इन, चैनल पेयरिंग, daemon इंस्टॉल, नेटवर्क डाउनलोड, Skills, या वैकल्पिक Plugin पूरी ऑनबोर्डिंग को अधिक समय लेवा बना सकते हैं। आप वैकल्पिक चरण छोड़ सकते हैं और बाद में `openclaw configure` के साथ वापस आ सकते हैं।

पूर्ण संदर्भ के लिए [ऑनबोर्डिंग (CLI)](</hi/start/wizard>) देखें।

* ### Verify the Gateway is running

bashCopy code
[code]
    openclaw gateway status
[/code]

आपको Gateway को पोर्ट 18789 पर सुनते हुए दिखना चाहिए।

* ### Open the dashboard

bashCopy code
[code]
    openclaw dashboard
[/code]

यह आपके ब्राउज़र में Control UI खोलता है। यदि यह लोड हो जाता है, तो सब कुछ काम कर रहा है।

* ### Send your first message

Control UI चैट में एक संदेश टाइप करें और आपको AI उत्तर मिलना चाहिए।

इसके बजाय अपने फ़ोन से चैट करना चाहते हैं? सेट अप करने के लिए सबसे तेज़ चैनल [Telegram](</hi/channels/telegram>) है (बस एक bot token)। सभी विकल्पों के लिए [चैनल](</hi/channels>) देखें।

Advanced: mount a custom Control UI build

यदि आप स्थानीयकृत या अनुकूलित डैशबोर्ड बिल्ड बनाए रखते हैं, तो `gateway.controlUi.root` को ऐसी डायरेक्टरी पर इंगित करें जिसमें आपकी बनी हुई static assets और `index.html` हो।

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

फिर सेट करें:

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

Gateway को रीस्टार्ट करें और डैशबोर्ड फिर से खोलें:

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## आगे क्या करें

[**Connect a channel** Discord, Feishu, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, और अन्य। ](</hi/channels>) [**Pairing and safety** नियंत्रित करें कि आपके एजेंट को कौन संदेश भेज सकता है। ](</hi/channels/pairing>) [**Configure the Gateway** मॉडल, टूल, sandbox, और उन्नत सेटिंग्स। ](</hi/gateway/configuration>) [**Browse tools** ब्राउज़र, exec, वेब खोज, Skills, और Plugin। ](</hi/tools>)

Advanced: environment variables

यदि आप OpenClaw को service account के रूप में चलाते हैं या कस्टम पाथ चाहते हैं:

  * `OPENCLAW_HOME` — आंतरिक पाथ रिज़ॉल्यूशन के लिए होम डायरेक्टरी
  * `OPENCLAW_STATE_DIR` — state डायरेक्टरी को ओवरराइड करें
  * `OPENCLAW_CONFIG_PATH` — config file पाथ को ओवरराइड करें


पूर्ण संदर्भ: [Environment variables](</hi/help/environment>)।

## संबंधित

  * [इंस्टॉल अवलोकन](</hi/install>)
  * [चैनल अवलोकन](</hi/channels>)
  * [सेटअप](</hi/start/setup>)


Was this useful?YesNo

Open issue