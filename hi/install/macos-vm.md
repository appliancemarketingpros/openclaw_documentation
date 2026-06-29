---
title: macOS वर्चुअल मशीनें
source_url: https://docs.openclaw.ai/hi/install/macos-vm
scraped_at: 2026-06-29
---

InstallHosting

## अनुशंसित डिफ़ॉल्ट (अधिकांश उपयोगकर्ता)

  * हमेशा चालू Gateway और कम लागत के लिए **छोटा Linux VPS** । देखें [VPS होस्टिंग](</hi/vps>)।
  * यदि आप पूरा नियंत्रण और ब्राउज़र ऑटोमेशन के लिए **रेज़िडेंशियल IP** चाहते हैं, तो **समर्पित हार्डवेयर** (Mac mini या Linux बॉक्स)। कई साइटें डेटा सेंटर IPs को ब्लॉक करती हैं, इसलिए स्थानीय ब्राउज़िंग अक्सर बेहतर काम करती है।
  * **हाइब्रिड:** Gateway को सस्ते VPS पर रखें, और जब आपको ब्राउज़र/UI ऑटोमेशन चाहिए तब अपने Mac को **Node** के रूप में कनेक्ट करें। देखें [Nodes](</hi/nodes>) और [Gateway रिमोट](</hi/gateway/remote>)।


macOS VM का उपयोग तब करें जब आपको विशेष रूप से macOS-only क्षमताओं जैसे iMessage की ज़रूरत हो या आप अपने दैनिक Mac से सख्त अलगाव चाहते हों।

## macOS VM विकल्प

### आपके Apple Silicon Mac पर स्थानीय VM (Lume)

[Lume](<https://cua.ai/docs/lume>) का उपयोग करके अपने मौजूदा Apple Silicon Mac पर सैंडबॉक्स किए गए macOS VM में OpenClaw चलाएँ।

इससे आपको मिलता है:

  * अलगाव में पूरा macOS वातावरण (आपका होस्ट साफ़ रहता है)
  * `imsg` के ज़रिए iMessage समर्थन (डिफ़ॉल्ट स्थानीय पथ Linux/Windows पर असंभव है)
  * VMs क्लोन करके तुरंत रीसेट
  * कोई अतिरिक्त हार्डवेयर या क्लाउड लागत नहीं


### होस्टेड Mac प्रदाता (क्लाउड)

यदि आप क्लाउड में macOS चाहते हैं, तो होस्टेड Mac प्रदाता भी काम करते हैं:

  * [MacStadium](<https://www.macstadium.com/>) (होस्टेड Macs)
  * अन्य होस्टेड Mac विक्रेता भी काम करते हैं; उनके VM + SSH दस्तावेज़ों का पालन करें


macOS VM तक SSH पहुँच मिल जाने पर, नीचे चरण 6 पर जारी रखें।

* * *

## त्वरित पथ (Lume, अनुभवी उपयोगकर्ता)

  1. Lume इंस्टॉल करें
  2. `lume create openclaw --os macos --ipsw latest`
  3. Setup Assistant पूरा करें, Remote Login (SSH) सक्षम करें
  4. `lume run openclaw --no-display`
  5. SSH से लॉग इन करें, OpenClaw इंस्टॉल करें, channels कॉन्फ़िगर करें
  6. पूर्ण


* * *

## आपको क्या चाहिए (Lume)

  * Apple Silicon Mac (M1/M2/M3/M4)
  * होस्ट पर macOS Sequoia या बाद का संस्करण
  * प्रति VM ~60 GB खाली डिस्क स्थान
  * ~20 मिनट


* * *

## 1) Lume इंस्टॉल करें

bashCopy code
[code]
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"
[/code]

यदि `~/.local/bin` आपके PATH में नहीं है:

bashCopy code
[code]
    echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.zshrc && source ~/.zshrc
[/code]

सत्यापित करें:

bashCopy code
[code]
    lume --version
[/code]

दस्तावेज़: [Lume इंस्टॉलेशन](<https://cua.ai/docs/lume/guide/getting-started/installation>)

* * *

## 2) macOS VM बनाएँ

bashCopy code
[code]
    lume create openclaw --os macos --ipsw latest
[/code]

यह macOS डाउनलोड करता है और VM बनाता है। VNC विंडो अपने-आप खुलती है।

* * *

## 3) Setup Assistant पूरा करें

VNC विंडो में:

  1. भाषा और क्षेत्र चुनें
  2. Apple ID छोड़ें (या यदि आप बाद में iMessage चाहते हैं तो साइन इन करें)
  3. उपयोगकर्ता खाता बनाएँ (उपयोगकर्ता नाम और पासवर्ड याद रखें)
  4. सभी वैकल्पिक सुविधाएँ छोड़ें


सेटअप पूरा होने के बाद:

  1. SSH सक्षम करें: System Settings -> General -> Sharing खोलें और "Remote Login" सक्षम करें।
  2. हेडलेस VM उपयोग के लिए, ऑटो-लॉगिन सक्षम करें: System Settings -> Users & Groups खोलें, "Automatically log in as:" चुनें, और VM उपयोगकर्ता चुनें।


* * *

## 4) VM IP पता प्राप्त करें

bashCopy code
[code]
    lume get openclaw
[/code]

IP पता देखें (आमतौर पर `192.168.64.x`)।

* * *

## 5) VM में SSH करें

bashCopy code
[code]
    ssh youruser@192.168.64.X
[/code]

`youruser` को आपके बनाए गए खाते से बदलें, और IP को अपने VM के IP से।

* * *

## 6) OpenClaw इंस्टॉल करें

VM के अंदर:

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

अपने मॉडल प्रदाता (Anthropic, OpenAI, आदि) को सेट अप करने के लिए ऑनबोर्डिंग संकेतों का पालन करें।

* * *

## 7) channels कॉन्फ़िगर करें

कॉन्फ़िग फ़ाइल संपादित करें:

bashCopy code
[code]
    nano ~/.openclaw/openclaw.json
[/code]

अपने channels जोड़ें:

json5Copy code
[code]
    {  channels: {    whatsapp: {      dmPolicy: "allowlist",      allowFrom: ["+15551234567"],    },    telegram: {      botToken: "YOUR_BOT_TOKEN",    },  },}
[/code]

फिर WhatsApp में लॉगिन करें (QR स्कैन करें):

bashCopy code
[code]
    openclaw channels login
[/code]

* * *

## 8) VM को हेडलेस चलाएँ

VM रोकें और डिस्प्ले के बिना फिर से शुरू करें:

bashCopy code
[code]
    lume stop openclawlume run openclaw --no-display
[/code]

VM बैकग्राउंड में चलता है। OpenClaw का daemon gateway को चलाए रखता है।

स्थिति जाँचने के लिए:

bashCopy code
[code]
    ssh youruser@192.168.64.X "openclaw status"
[/code]

* * *

## बोनस: iMessage इंटीग्रेशन

यह macOS पर चलाने की सबसे प्रमुख सुविधा है। OpenClaw में Messages जोड़ने के लिए `imsg` के साथ [iMessage](</hi/channels/imessage>) का उपयोग करें।

VM के अंदर:

  1. Messages में साइन इन करें।
  2. `imsg` इंस्टॉल करें।
  3. OpenClaw/`imsg` चलाने वाली प्रक्रिया के लिए Full Disk Access और Automation अनुमति दें।
  4. `imsg rpc --help` के साथ RPC समर्थन सत्यापित करें।


अपने OpenClaw कॉन्फ़िग में जोड़ें:

json5Copy code
[code]
    {  channels: {    imessage: {      enabled: true,      cliPath: "imsg",      dbPath: "~/Library/Messages/chat.db",    },  },}
[/code]

gateway पुनः शुरू करें। अब आपका agent iMessages भेज और प्राप्त कर सकता है।

पूरा सेटअप विवरण: [iMessage channel](</hi/channels/imessage>)

* * *

## गोल्डन इमेज सहेजें

आगे कस्टमाइज़ करने से पहले, अपनी साफ़ स्थिति का snapshot लें:

bashCopy code
[code]
    lume stop openclawlume clone openclaw openclaw-golden
[/code]

कभी भी रीसेट करें:

bashCopy code
[code]
    lume stop openclaw && lume delete openclawlume clone openclaw-golden openclawlume run openclaw --no-display
[/code]

* * *

## 24/7 चलाना

VM को चालू रखने के लिए:

  * अपने Mac को प्लग इन रखें
  * System Settings → Energy Saver में sleep अक्षम करें
  * ज़रूरत पड़ने पर `caffeinate` का उपयोग करें


वास्तव में हमेशा चालू रहने के लिए, समर्पित Mac mini या छोटे VPS पर विचार करें। देखें [VPS होस्टिंग](</hi/vps>)।

* * *

## समस्या निवारण

समस्या | समाधान  
---|---  
VM में SSH नहीं हो पा रहा | जाँचें कि VM की System Settings में "Remote Login" सक्षम है  
VM IP नहीं दिख रहा | VM के पूरी तरह boot होने तक प्रतीक्षा करें, फिर `lume get openclaw` चलाएँ  
Lume कमांड नहीं मिली | अपने PATH में `~/.local/bin` जोड़ें  
WhatsApp QR स्कैन नहीं हो रहा | `openclaw channels login` चलाते समय सुनिश्चित करें कि आप VM में लॉग इन हैं (होस्ट में नहीं)  
  
* * *

## संबंधित दस्तावेज़

  * [VPS होस्टिंग](</hi/vps>)
  * [Nodes](</hi/nodes>)
  * [Gateway रिमोट](</hi/gateway/remote>)
  * [iMessage channel](</hi/channels/imessage>)
  * [Lume Quickstart](<https://cua.ai/docs/lume/guide/getting-started/quickstart>)
  * [Lume CLI Reference](<https://cua.ai/docs/lume/reference/cli-reference>)
  * [Unattended VM Setup](<https://cua.ai/docs/lume/guide/fundamentals/unattended-setup>) (उन्नत)
  * [Docker Sandboxing](</hi/install/docker>) (वैकल्पिक अलगाव तरीका)


Was this useful?YesNo

Open issue