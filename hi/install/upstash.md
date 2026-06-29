---
title: Upstash बॉक्स
source_url: https://docs.openclaw.ai/hi/install/upstash
scraped_at: 2026-06-29
---

InstallHosting

Upstash Box पर एक स्थायी OpenClaw Gateway चलाएँ, जो जीवित-रखने वाले जीवनचक्र समर्थन वाला एक प्रबंधित Linux वातावरण है।

डैशबोर्ड पहुँच के लिए SSH सुरंग का उपयोग करें। Gateway पोर्ट को सीधे सार्वजनिक इंटरनेट पर उजागर न करें।

## पूर्वापेक्षाएँ

  * Upstash खाता
  * जीवित-रखने वाला Upstash Box
  * आपकी स्थानीय मशीन पर SSH क्लाइंट


## Box बनाएँ

Upstash Console में जीवित-रखने वाला Box बनाएँ। Box ID, जैसे `right-flamingo-14486`, और अपनी Box API कुंजी नोट करें।

Upstash अपना वर्तमान OpenClaw Box मार्गदर्शन यहाँ बनाए रखता है: [OpenClaw सेटअप](<https://upstash.com/docs/box/guides/openclaw-setup>)।

## SSH सुरंग से कनेक्ट करें

OpenClaw डैशबोर्ड पोर्ट को अपनी स्थानीय मशीन पर फ़ॉरवर्ड करें। संकेत मिलने पर SSH पासवर्ड के रूप में अपनी Box API कुंजी का उपयोग करें:

bashCopy code
[code]
    ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

जीवित-रखने वाले विकल्प ऑनबोर्डिंग के दौरान निष्क्रिय सुरंग ड्रॉप को कम करते हैं।

## OpenClaw इंस्टॉल करें

Box के अंदर:

bashCopy code
[code]
    sudo npm install -g openclaw
[/code]

## ऑनबोर्डिंग चलाएँ

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

संकेतों का पालन करें। ऑनबोर्डिंग समाप्त होने पर डैशबोर्ड URL और टोकन कॉपी करें।

## Gateway शुरू करें

Box नेटवर्क के लिए Gateway कॉन्फ़िगर करें और उसे पृष्ठभूमि में शुरू करें:

bashCopy code
[code]
    openclaw config set gateway.bind lannohup openclaw gateway > gateway.log 2>&1 &
[/code]

SSH सुरंग सक्रिय होने पर, डैशबोर्ड URL को स्थानीय रूप से खोलें:

textCopy code
[code]
    http://127.0.0.1:18789/#token=<your-token>
[/code]

## स्वतः पुनःआरंभ

इस कमांड को Box init स्क्रिप्ट के रूप में सेट करें ताकि Box शुरू होने पर Gateway पुनःआरंभ हो:

bashCopy code
[code]
    nohup openclaw gateway > gateway.log 2>&1 &
[/code]

## समस्या निवारण

यदि ऑनबोर्डिंग के दौरान SSH फ़्रीज़ हो जाता है, तो साफ़ SSH कॉन्फ़िग और जीवित-रखने वाले विकल्पों के साथ फिर से कनेक्ट करें:

bashCopy code
[code]
    ssh -F /dev/null -o ControlMaster=no -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

यह पुराने स्थानीय `~/.ssh/config` सेटिंग्स को बायपास करता है और निष्क्रिय नेटवर्क अवधियों के दौरान सुरंग को सक्रिय रखता है।

## संबंधित

  * [दूरस्थ पहुँच](</hi/gateway/remote>)
  * [Gateway सुरक्षा](</hi/gateway/security>)
  * [OpenClaw अपडेट करना](</hi/install/updating>)


Was this useful?YesNo

Open issue