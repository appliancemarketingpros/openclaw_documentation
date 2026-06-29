---
title: डिवाइस मॉडल डेटाबेस
source_url: https://docs.openclaw.ai/hi/reference/device-models
scraped_at: 2026-06-29
---

ReferenceRPC and API

macOS साथी ऐप **इंस्टेंसेस** UI में Apple मॉडल पहचानकर्ताओं (जैसे `iPad16,6`, `Mac16,6`) को मनुष्यों द्वारा पढ़े जा सकने वाले नामों से मैप करके अनुकूल Apple डिवाइस मॉडल नाम दिखाता है।

मैपिंग JSON के रूप में यहां वेंडर की गई है:

  * `apps/macos/Sources/OpenClaw/Resources/DeviceModels/`


## डेटा स्रोत

हम वर्तमान में MIT-लाइसेंस वाले रिपॉज़िटरी से मैपिंग वेंडर करते हैं:

  * `kyle-seongwoo-jun/apple-device-identifiers`


बिल्ड को निर्धारक बनाए रखने के लिए, JSON फ़ाइलों को विशिष्ट upstream कमिट्स पर पिन किया गया है (जो `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md` में दर्ज हैं)।

## डेटाबेस अपडेट करना

  1. वे upstream कमिट्स चुनें जिन्हें आप पिन करना चाहते हैं (एक iOS के लिए, एक macOS के लिए)।
  2. `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md` में कमिट हैश अपडेट करें।
  3. उन कमिट्स पर पिन की गई JSON फ़ाइलें फिर से डाउनलोड करें:

bashCopy code
[code]
    IOS_COMMIT="<commit sha for ios-device-identifiers.json>"MAC_COMMIT="<commit sha for mac-device-identifiers.json>" curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${IOS_COMMIT}/ios-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/ios-device-identifiers.json curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${MAC_COMMIT}/mac-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/mac-device-identifiers.json
[/code]

  4. सुनिश्चित करें कि `apps/macos/Sources/OpenClaw/Resources/DeviceModels/LICENSE.apple-device-identifiers.txt` अब भी upstream से मेल खाता है (यदि upstream लाइसेंस बदलता है तो इसे बदल दें)।
  5. सत्यापित करें कि macOS ऐप साफ़ तौर पर बिल्ड होता है (कोई चेतावनी नहीं):

bashCopy code
[code]
    swift build --package-path apps/macos
[/code]

## संबंधित

  * [Node](</hi/nodes>)
  * [Node समस्या निवारण](</hi/nodes/troubleshooting>)


Was this useful?YesNo

Open issue