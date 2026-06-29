---
title: Skills (macOS)
source_url: https://docs.openclaw.ai/hi/platforms/mac/skills
scraped_at: 2026-06-29
---

PlatformsmacOS companion app

macOS ऐप Gateway के माध्यम से OpenClaw Skills दिखाता है; यह स्थानीय रूप से Skills को पार्स नहीं करता।

## डेटा स्रोत

  * `skills.status` (Gateway) सभी Skills के साथ पात्रता और अनुपस्थित आवश्यकताएं लौटाता है (बंडल किए गए Skills के लिए allowlist ब्लॉक सहित)।
  * आवश्यकताएं प्रत्येक `SKILL.md` में `metadata.openclaw.requires` से निकाली जाती हैं।


## इंस्टॉल क्रियाएं

  * `metadata.openclaw.install` इंस्टॉल विकल्प (brew/node/go/uv) परिभाषित करता है।
  * ऐप Gateway होस्ट पर इंस्टॉलर चलाने के लिए `skills.install` को कॉल करता है।
  * ऑपरेटर-स्वामित्व वाली `security.installPolicy`, इंस्टॉलर मेटाडेटा चलने से पहले Gateway-समर्थित Skill इंस्टॉल को ब्लॉक कर सकती है। इंस्टॉल-समय पर अंतर्निहित dangerous-code ब्लॉकिंग Skill इंस्टॉल प्रवाह का हिस्सा नहीं है।
  * यदि हर इंस्टॉल विकल्प `download` है, तो Gateway सभी डाउनलोड विकल्प दिखाता है।
  * अन्यथा, Gateway मौजूदा इंस्टॉल प्राथमिकताओं और होस्ट बाइनरी का उपयोग करके एक पसंदीदा इंस्टॉलर चुनता है: पहले Homebrew जब `skills.install.preferBrew` सक्षम हो और `brew` मौजूद हो, फिर `uv`, फिर `skills.install.nodeManager` से कॉन्फ़िगर किया गया node manager, फिर बाद के fallback जैसे `go` या `download`।
  * Node इंस्टॉल लेबल कॉन्फ़िगर किए गए node manager को दर्शाते हैं, जिसमें `yarn` भी शामिल है।


## Env/API कुंजियां

  * ऐप कुंजियों को `~/.openclaw/openclaw.json` में `skills.entries.<skillKey>` के तहत संग्रहीत करता है।
  * `skills.update` `enabled`, `apiKey`, और `env` को पैच करता है।


## रिमोट मोड

  * इंस्टॉल + कॉन्फ़िग अपडेट Gateway होस्ट पर होते हैं (स्थानीय Mac पर नहीं)।


## संबंधित

  * [Skills](</hi/tools/skills>)
  * [macOS ऐप](</hi/platforms/macos>)


Was this useful?YesNo

Open issue