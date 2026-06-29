---
title: OpenClaw
source_url: https://docs.openclaw.ai/hi
scraped_at: 2026-06-29
---

Get started

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _"छिलका उतारो! छिलका उतारो!"_ — शायद एक अंतरिक्ष लॉब्स्टर

**Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, और अन्य पर AI एजेंटों के लिए किसी भी OS का Gateway।**

संदेश भेजें, अपनी जेब से एजेंट प्रतिक्रिया पाएं। बिल्ट-इन चैनलों, बंडल किए गए चैनल Plugin, WebChat, और मोबाइल Node पर एक Gateway चलाएं।

[**शुरू करें** OpenClaw इंस्टॉल करें और कुछ ही मिनटों में Gateway शुरू करें। ](</hi/start/getting-started>) [**Onboarding चलाएं** `openclaw onboard` और पेयरिंग फ़्लो के साथ निर्देशित सेटअप। ](</hi/start/wizard>) [**Control UI खोलें** चैट, कॉन्फ़िग, और सत्रों के लिए ब्राउज़र डैशबोर्ड लॉन्च करें। ](</hi/web/control-ui>)

## OpenClaw क्या है?

OpenClaw एक **स्व-होस्टेड gateway** है जो आपके पसंदीदा चैट ऐप्स और चैनल इंटरफेस — बिल्ट-इन चैनलों तथा Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, और अन्य जैसे बंडल किए गए या बाहरी चैनल Plugin — को AI कोडिंग एजेंटों से जोड़ता है। आप अपनी मशीन (या सर्वर) पर एक ही Gateway प्रक्रिया चलाते हैं, और यह आपके मैसेजिंग ऐप्स और हमेशा उपलब्ध AI सहायक के बीच पुल बन जाता है।

**यह किसके लिए है?** उन डेवलपरों और पावर उपयोगकर्ताओं के लिए जो ऐसा निजी AI सहायक चाहते हैं जिसे वे कहीं से भी संदेश भेज सकें — अपने डेटा पर नियंत्रण छोड़े बिना या किसी होस्टेड सेवा पर निर्भर हुए बिना।

**इसे अलग क्या बनाता है?**

  * **स्व-होस्टेड** : आपके हार्डवेयर पर, आपके नियमों से चलता है
  * **मल्टी-चैनल** : एक Gateway बिल्ट-इन चैनलों और बंडल किए गए या बाहरी चैनल Plugin को एक साथ सेवा देता है
  * **एजेंट-नेटिव** : टूल उपयोग, सत्र, मेमोरी, और मल्टी-एजेंट रूटिंग वाले कोडिंग एजेंटों के लिए बनाया गया
  * **ओपन सोर्स** : MIT लाइसेंस वाला, समुदाय-चालित


**आपको क्या चाहिए?** Node 24 (अनुशंसित), या संगतता के लिए Node 22 LTS (`22.19+`), आपके चुने गए प्रोवाइडर की API कुंजी, और 5 मिनट। सर्वोत्तम गुणवत्ता और सुरक्षा के लिए, उपलब्ध सबसे मजबूत नवीनतम-पीढ़ी का मॉडल उपयोग करें।

## यह कैसे काम करता है
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["OpenClaw agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

Gateway सत्रों, रूटिंग, और चैनल कनेक्शनों के लिए सत्य का एकमात्र स्रोत है।

## मुख्य क्षमताएं

[**मल्टी-चैनल gateway** एक ही Gateway प्रक्रिया के साथ Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat, और अन्य। ](</hi/channels>) [**Plugin चैनल** बंडल किए गए Plugin सामान्य मौजूदा रिलीज़ में Matrix, Nostr, Twitch, Zalo, और अन्य जोड़ते हैं। ](</hi/tools/plugin>) [**मल्टी-एजेंट रूटिंग** प्रति एजेंट, वर्कस्पेस, या प्रेषक अलग-थलग सत्र। ](</hi/concepts/multi-agent>) [**मीडिया समर्थन** इमेज, ऑडियो, और दस्तावेज़ भेजें और प्राप्त करें। ](</hi/nodes/images>) [**Web Control UI** चैट, कॉन्फ़िग, सत्रों, और Node के लिए ब्राउज़र डैशबोर्ड। ](</hi/web/control-ui>) [**मोबाइल Node** Canvas, कैमरा, और वॉइस-सक्षम वर्कफ़्लो के लिए iOS और Android Node पेयर करें। ](</hi/nodes>)

## त्वरित शुरुआत

* ### OpenClaw इंस्टॉल करें

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### Onboard करें और सेवा इंस्टॉल करें

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### चैट करें

अपने ब्राउज़र में Control UI खोलें और संदेश भेजें:

bashCopy code
[code]
    openclaw dashboard
[/code]

या कोई चैनल कनेक्ट करें ([Telegram](</hi/channels/telegram>) सबसे तेज़ है) और अपने फ़ोन से चैट करें।

पूरा इंस्टॉल और dev सेटअप चाहिए? [शुरू करना](</hi/start/getting-started>) देखें।

## डैशबोर्ड

Gateway शुरू होने के बाद ब्राउज़र Control UI खोलें।

  * स्थानीय डिफ़ॉल्ट: <http://127.0.0.1:18789/>
  * रिमोट एक्सेस: [वेब सतहें](</hi/web>) और [Tailscale](</hi/gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## कॉन्फ़िगरेशन (वैकल्पिक)

कॉन्फ़िग `~/.openclaw/openclaw.json` पर रहता है।

  * यदि आप **कुछ नहीं करते** , OpenClaw प्रति-प्रेषक सत्रों के साथ बंडल किए गए OpenClaw एजेंट रनटाइम का उपयोग करता है।
  * यदि आप इसे लॉक डाउन करना चाहते हैं, तो `channels.whatsapp.allowFrom` और (ग्रुप के लिए) मेंशन नियमों से शुरू करें।


उदाहरण:

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## यहां से शुरू करें

[**डॉक्स हब** उपयोग मामले के अनुसार व्यवस्थित सभी डॉक्स और गाइड। ](</hi/start/hubs>) [**कॉन्फ़िगरेशन** मुख्य Gateway सेटिंग्स, टोकन, और प्रोवाइडर कॉन्फ़िग। ](</hi/gateway/configuration>) [**रिमोट एक्सेस** SSH और tailnet एक्सेस पैटर्न। ](</hi/gateway/remote>) [**चैनल** Feishu, Microsoft Teams, WhatsApp, Telegram, Discord, और अन्य के लिए चैनल-विशिष्ट सेटअप। ](</hi/channels/telegram>) [**Node** पेयरिंग, Canvas, कैमरा, और डिवाइस कार्रवाइयों के साथ iOS और Android Node। ](</hi/nodes>) [**सहायता** सामान्य सुधार और ट्रबलशूटिंग प्रवेश बिंदु। ](</hi/help>)

## और जानें

[**पूरी फीचर सूची** पूरी चैनल, रूटिंग, और मीडिया क्षमताएं। ](</hi/concepts/features>) [**मल्टी-एजेंट रूटिंग** वर्कस्पेस आइसोलेशन और प्रति-एजेंट सत्र। ](</hi/concepts/multi-agent>) [**सुरक्षा** टोकन, allowlist, और सुरक्षा नियंत्रण। ](</hi/gateway/security>) [**ट्रबलशूटिंग** Gateway डायग्नोस्टिक्स और सामान्य त्रुटियां। ](</hi/gateway/troubleshooting>) [**परिचय और श्रेय** प्रोजेक्ट की उत्पत्ति, योगदानकर्ता, और लाइसेंस। ](</hi/reference/credits>)

Was this useful?YesNo

Open issue