---
title: Plugin इंस्टॉल ओवरराइड्स
source_url: https://docs.openclaw.ai/hi/plugins/install-overrides
scraped_at: 2026-06-29
---

ReferencePlugin reference

Plugin इंस्टॉल ओवरराइड्स मेंटेनरों को सेटअप-समय Plugin इंस्टॉल को किसी खास npm पैकेज या स्थानीय npm-pack टारबॉल के विरुद्ध टेस्ट करने देते हैं। ये केवल E2E और पैकेज वैलिडेशन के लिए हैं। सामान्य उपयोगकर्ताओं को Plugin इंस्टॉल करने के लिए [`openclaw plugins install`](</hi/cli/plugins>) का उपयोग करना चाहिए।

## परिवेश

जब तक दोनों वेरिएबल सेट न हों, ओवरराइड्स अक्षम रहते हैं:

bashCopy code
[code]
    export OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1export OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{  "codex": "npm-pack:/tmp/openclaw-codex-2026.5.8.tgz",  "openclaw-web-search": "npm:@openclaw/web-search@2026.5.8"}'
[/code]

ओवरराइड मैप JSON है, जिसकी कुंजी Plugin आईडी होती है। मान इनके लिए समर्थन देते हैं:

  * रजिस्ट्री पैकेज और सटीक वर्जन या टैग के लिए `npm:<registry-spec>`
  * `npm pack` से बने स्थानीय टारबॉल के लिए `npm-pack:<path.tgz>`


सापेक्ष `npm-pack:` पाथ वर्तमान कार्यशील डायरेक्टरी से रिज़ॉल्व होते हैं।

## व्यवहार

जब कोई सेटअप-समय फ्लो ऐसे Plugin को इंस्टॉल करने के लिए कहता है जिसकी आईडी मैप में मौजूद है, तो OpenClaw कैटलॉग, बंडल किए गए, या डिफ़ॉल्ट npm स्रोत के बजाय ओवरराइड स्रोत का उपयोग करता है। यह ऑनबोर्डिंग और उन दूसरे फ्लो पर लागू होता है जो साझा सेटअप-समय Plugin इंस्टॉलर का उपयोग करते हैं।

ओवरराइड्स फिर भी अपेक्षित Plugin आईडी लागू करते हैं। `codex` से मैप किया गया टारबॉल ऐसा Plugin इंस्टॉल करना चाहिए जिसकी मेनिफेस्ट आईडी `codex` हो।

ओवरराइड्स आधिकारिक विश्वसनीय-स्रोत स्थिति विरासत में नहीं लेते। भले ही कैटलॉग एंट्री सामान्यतः OpenClaw-स्वामित्व वाले पैकेज को दर्शाती हो, ओवरराइड को ऑपरेटर द्वारा दिया गया टेस्ट इनपुट माना जाता है।

वर्कस्पेस `.env` फाइलें इंस्टॉल ओवरराइड्स सक्षम नहीं कर सकतीं। इन वेरिएबल्स को उस विश्वसनीय शेल, CI जॉब, या रिमोट टेस्ट कमांड में सेट करें जो OpenClaw लॉन्च करता है।

## पैकेज E2E

एक अलग-थलग स्टेट डायरेक्टरी का उपयोग करें ताकि पैकेज इंस्टॉल और इंस्टॉल रिकॉर्ड आपके सामान्य OpenClaw स्टेट को न छुएं:

bashCopy code
[code]
    npm pack extensions/codex --pack-destination /tmp OPENCLAW_STATE_DIR="$(mktemp -d)" \OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1 \OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{"codex":"npm-pack:/tmp/openclaw-codex-2026.5.8.tgz"}' \pnpm openclaw onboard --mode local
[/code]

स्टेट डायरेक्टरी के अंतर्गत इंस्टॉल किए गए पैकेज को सत्यापित करें:

bashCopy code
[code]
    find "$OPENCLAW_STATE_DIR/npm/projects" -path '*/node_modules/@openclaw/codex/package.json' -printgrep -R '"@openclaw/codex"' "$OPENCLAW_STATE_DIR/npm/projects"/*/package-lock.json
[/code]

लाइव प्रोवाइडर E2E के लिए, टेस्ट कमांड लॉन्च करने से पहले वास्तविक API कुंजी को किसी विश्वसनीय शेल या CI सीक्रेट से स्रोत करें। कुंजियां प्रिंट न करें; केवल स्रोत और यह रिपोर्ट करें कि कुंजी मौजूद थी या नहीं।

Was this useful?YesNo

Open issue