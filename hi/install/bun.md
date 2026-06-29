---
title: Bun (प्रायोगिक)
source_url: https://docs.openclaw.ai/hi/install/bun
scraped_at: 2026-06-29
---

InstallContainers

Bun, TypeScript को सीधे चलाने के लिए एक वैकल्पिक स्थानीय रनटाइम है (`bun run ...`, `bun --watch ...`)। डिफ़ॉल्ट पैकेज मैनेजर `pnpm` ही रहता है, जो पूरी तरह समर्थित है और docs टूलिंग द्वारा उपयोग किया जाता है। Bun `pnpm-lock.yaml` का उपयोग नहीं कर सकता और उसे अनदेखा करेगा।

## इंस्टॉल करें

* ### निर्भरताएँ इंस्टॉल करें

shCopy code
[code]
    bun install
[/code]

`bun.lock` / `bun.lockb` gitignored हैं, इसलिए repo churn नहीं होता। lockfile लिखना पूरी तरह छोड़ने के लिए:

shCopy code
[code]
    bun install --no-save
[/code]

* ### बिल्ड और टेस्ट करें

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## लाइफ़साइकल स्क्रिप्ट

Bun निर्भरता लाइफ़साइकल स्क्रिप्ट को तब तक ब्लॉक करता है जब तक उन पर स्पष्ट रूप से भरोसा न किया जाए। इस repo के लिए, आम तौर पर ब्लॉक होने वाली स्क्रिप्ट आवश्यक नहीं हैं:

  * `baileys` `preinstall` \-- Node major >= 20 की जाँच करता है (OpenClaw डिफ़ॉल्ट रूप से Node 24 पर है और अभी भी Node 22 LTS का समर्थन करता है, वर्तमान में `22.19+`)
  * `protobufjs` `postinstall` \-- असंगत संस्करण योजनाओं के बारे में चेतावनियाँ देता है (कोई बिल्ड आर्टिफ़ैक्ट नहीं)


यदि आपको कोई ऐसी रनटाइम समस्या आती है जिसके लिए ये स्क्रिप्ट आवश्यक हैं, तो उन पर स्पष्ट रूप से भरोसा करें:

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## सावधानियाँ

कुछ स्क्रिप्ट अभी भी pnpm को हार्डकोड करती हैं (उदाहरण के लिए `check:docs`, `ui:*`, `protocol:check`)। अभी के लिए उन्हें pnpm के माध्यम से चलाएँ।

## संबंधित

  * [इंस्टॉल अवलोकन](</hi/install>)
  * [Node.js](</hi/install/node>)
  * [अपडेट करना](</hi/install/updating>)


Was this useful?YesNo

Open issue