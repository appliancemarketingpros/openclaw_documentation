---
title: डिवाइस
source_url: https://docs.openclaw.ai/hi/cli/devices
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw devices`

डिवाइस पेयरिंग अनुरोध और डिवाइस-स्कोप्ड टोकन प्रबंधित करें।

## कमांड

### `openclaw devices list`

लंबित पेयरिंग अनुरोधों और पेयर किए गए डिवाइसों की सूची दिखाएं।

CodeCopy code
[code]
    openclaw devices listopenclaw devices list --json
[/code]

जब डिवाइस पहले से पेयर हो, तो लंबित अनुरोध का आउटपुट डिवाइस की मौजूदा अनुमोदित पहुंच के साथ अनुरोधित पहुंच दिखाता है। इससे स्कोप/भूमिका अपग्रेड स्पष्ट हो जाते हैं, बजाय इसके कि ऐसा लगे कि पेयरिंग खो गई है।

### `openclaw devices remove <deviceId>`

पेयर किए गए एक डिवाइस की प्रविष्टि हटाएं।

जब आप पेयर किए गए डिवाइस टोकन से प्रमाणित हों, तो गैर-एडमिन कॉलर केवल **अपने** डिवाइस की प्रविष्टि हटा सकते हैं। किसी अन्य डिवाइस को हटाने के लिए `operator.admin` आवश्यक है।

CodeCopy code
[code]
    openclaw devices remove <deviceId>openclaw devices remove <deviceId> --json
[/code]

### `openclaw devices clear --yes [--pending]`

पेयर किए गए डिवाइसों को बल्क में साफ करें।

CodeCopy code
[code]
    openclaw devices clear --yesopenclaw devices clear --yes --pendingopenclaw devices clear --yes --pending --json
[/code]

### `openclaw devices approve [requestId] [--latest]`

सटीक `requestId` से लंबित डिवाइस पेयरिंग अनुरोध को अनुमोदित करें। यदि `requestId` छोड़ा गया है या `--latest` पास किया गया है, तो OpenClaw केवल चयनित लंबित अनुरोध प्रिंट करता है और बाहर निकल जाता है; विवरण सत्यापित करने के बाद सटीक अनुरोध ID के साथ अनुमोदन फिर से चलाएं।

यदि डिवाइस पहले से पेयर है और व्यापक स्कोप या व्यापक भूमिका मांगता है, तो OpenClaw मौजूदा अनुमोदन को यथावत रखता है और नया लंबित अपग्रेड अनुरोध बनाता है। `openclaw devices list` में `Requested` बनाम `Approved` कॉलम देखें या अनुमोदन से पहले सटीक अपग्रेड का पूर्वावलोकन करने के लिए `openclaw devices approve --latest` का उपयोग करें।

यदि Gateway को स्पष्ट रूप से `gateway.nodes.pairing.autoApproveCidrs` के साथ कॉन्फिगर किया गया है, तो मिलते-जुलते क्लाइंट IP से पहली बार आने वाले `role: node` अनुरोध इस सूची में दिखने से पहले अनुमोदित हो सकते हैं। यह नीति डिफॉल्ट रूप से अक्षम है और ऑपरेटर/ब्राउजर क्लाइंटों या अपग्रेड अनुरोधों पर कभी लागू नहीं होती।

नोड या अन्य गैर-ऑपरेटर डिवाइस भूमिकाओं को अनुमोदित करने के लिए `operator.admin` आवश्यक है। `operator.pairing` केवल ऑपरेटर-डिवाइस अनुमोदनों के लिए पर्याप्त है, वह भी तब जब अनुरोधित ऑपरेटर स्कोप कॉलर के अपने स्कोप के भीतर रहें। अनुमोदन-समय जांचों के लिए [ऑपरेटर स्कोप](</hi/gateway/operator-scopes>) देखें।

CodeCopy code
[code]
    openclaw devices approveopenclaw devices approve <requestId>openclaw devices approve --latest
[/code]

## Paperclip / `openclaw_gateway` पहली बार चलाने का अनुमोदन

जब कोई नया Paperclip एजेंट पहली बार `openclaw_gateway` एडाप्टर के माध्यम से कनेक्ट करता है, तो Gateway रन सफल होने से पहले एक बार का डिवाइस पेयरिंग अनुमोदन मांग सकता है। यदि Paperclip `openclaw_gateway_pairing_required` रिपोर्ट करता है, तो लंबित डिवाइस को अनुमोदित करें और फिर से प्रयास करें।

स्थानीय गेटवे के लिए, सबसे नए लंबित अनुरोध का पूर्वावलोकन करें:

bashCopy code
[code]
    openclaw devices approve --latest
[/code]

पूर्वावलोकन सटीक `openclaw devices approve <requestId>` कमांड प्रिंट करता है। अनुरोध विवरण सत्यापित करें, फिर उसे अनुमोदित करने के लिए उसी कमांड को अनुरोध ID के साथ फिर से चलाएं।

रिमोट गेटवे या स्पष्ट क्रेडेंशियल के लिए, पूर्वावलोकन और अनुमोदन करते समय वही विकल्प पास करें:

bashCopy code
[code]
    openclaw devices approve --latest --url <gateway-ws-url> --token <gateway-token>
[/code]

रीस्टार्ट के बाद फिर से अनुमोदन से बचने के लिए, हर रन में नई अल्पकालिक पहचान बनाने के बजाय Paperclip एडाप्टर कॉन्फिग में एक स्थायी डिवाइस key रखें:

jsonCopy code
[code]
    {  "adapterConfig": {    "devicePrivateKeyPem": "<ed25519-private-key-pkcs8-pem>"  }}
[/code]

यदि अनुमोदन लगातार विफल होता है, तो पहले `openclaw devices list` चलाकर पुष्टि करें कि कोई लंबित अनुरोध मौजूद है।

### `openclaw devices reject <requestId>`

लंबित डिवाइस पेयरिंग अनुरोध अस्वीकार करें।

CodeCopy code
[code]
    openclaw devices reject <requestId>
[/code]

### `openclaw devices rotate --device <id> --role <role> [--scope <scope...>]`

किसी विशिष्ट भूमिका के लिए डिवाइस टोकन घुमाएं (वैकल्पिक रूप से स्कोप अपडेट करते हुए)। लक्षित भूमिका उस डिवाइस के अनुमोदित पेयरिंग अनुबंध में पहले से मौजूद होनी चाहिए; रोटेशन कोई नई अननुमोदित भूमिका जारी नहीं कर सकता। यदि आप `--scope` छोड़ते हैं, तो संग्रहीत घुमाए गए टोकन के साथ बाद के रीकनेक्ट उस टोकन के कैश किए गए अनुमोदित स्कोप फिर से उपयोग करते हैं। यदि आप स्पष्ट `--scope` मान पास करते हैं, तो वे भविष्य के कैश्ड-टोकन रीकनेक्ट के लिए संग्रहीत स्कोप सेट बन जाते हैं। गैर-एडमिन पेयर्ड-डिवाइस कॉलर केवल अपने **अपने** डिवाइस टोकन को घुमा सकते हैं। लक्षित टोकन स्कोप सेट कॉलर सत्र के अपने ऑपरेटर स्कोप के भीतर रहना चाहिए; रोटेशन कॉलर के पास पहले से मौजूद स्कोप से व्यापक ऑपरेटर टोकन जारी या संरक्षित नहीं कर सकता।

CodeCopy code
[code]
    openclaw devices rotate --device <deviceId> --role operator --scope operator.read --scope operator.write
[/code]

रोटेशन मेटाडेटा JSON के रूप में लौटाता है। यदि कॉलर उस डिवाइस टोकन से प्रमाणित रहते हुए अपना टोकन घुमा रहा है, तो प्रतिक्रिया में प्रतिस्थापन टोकन भी शामिल होता है ताकि क्लाइंट रीकनेक्ट करने से पहले उसे स्थायी कर सके। साझा/एडमिन रोटेशन bearer टोकन वापस नहीं दिखाते।

### `openclaw devices revoke --device <id> --role <role>`

किसी विशिष्ट भूमिका के लिए डिवाइस टोकन रद्द करें।

गैर-एडमिन पेयर्ड-डिवाइस कॉलर केवल अपने **अपने** डिवाइस टोकन को रद्द कर सकते हैं। किसी अन्य डिवाइस का टोकन रद्द करने के लिए `operator.admin` आवश्यक है। लक्षित टोकन स्कोप सेट भी कॉलर सत्र के अपने ऑपरेटर स्कोप के भीतर फिट होना चाहिए; केवल-पेयरिंग कॉलर एडमिन/राइट ऑपरेटर टोकन रद्द नहीं कर सकते।

CodeCopy code
[code]
    openclaw devices revoke --device <deviceId> --role node
[/code]

रद्दीकरण परिणाम JSON के रूप में लौटाता है।

## सामान्य विकल्प

  * `--url <url>`: Gateway WebSocket URL (कॉन्फिगर होने पर डिफॉल्ट `gateway.remote.url` होता है)।
  * `--token <token>`: Gateway टोकन (यदि आवश्यक हो)।
  * `--password <password>`: Gateway पासवर्ड (पासवर्ड auth)।
  * `--timeout <ms>`: RPC टाइमआउट।
  * `--json`: JSON आउटपुट (स्क्रिप्टिंग के लिए अनुशंसित)।


## नोट्स

  * टोकन रोटेशन नया टोकन लौटाता है (संवेदनशील)। इसे secret की तरह संभालें।
  * इन कमांडों के लिए `operator.pairing` (या `operator.admin`) स्कोप आवश्यक है। कुछ अनुमोदनों के लिए कॉलर के पास वे ऑपरेटर स्कोप भी होने चाहिए जिन्हें लक्षित डिवाइस जारी करेगा या विरासत में लेगा। गैर-ऑपरेटर डिवाइस भूमिकाओं के लिए `operator.admin` आवश्यक है; [ऑपरेटर स्कोप](</hi/gateway/operator-scopes>) देखें।
  * `gateway.nodes.pairing.autoApproveCidrs` केवल नई नोड डिवाइस पेयरिंग के लिए एक opt-in Gateway नीति है; यह CLI अनुमोदन अधिकार नहीं बदलती।
  * टोकन रोटेशन और रद्दीकरण उस डिवाइस के अनुमोदित पेयरिंग भूमिका सेट और अनुमोदित स्कोप आधाररेखा के भीतर रहते हैं। कोई भटकी हुई कैश्ड टोकन प्रविष्टि टोकन-प्रबंधन लक्ष्य प्रदान नहीं करती।
  * पेयर्ड-डिवाइस टोकन सत्रों के लिए, क्रॉस-डिवाइस प्रबंधन केवल एडमिन के लिए है: `remove`, `rotate`, और `revoke` केवल स्वयं के लिए हैं, जब तक कॉलर के पास `operator.admin` न हो।
  * टोकन म्यूटेशन भी कॉलर-स्कोप के भीतर सीमित है: केवल-पेयरिंग सत्र ऐसे टोकन को घुमा या रद्द नहीं कर सकता जिसके पास वर्तमान में `operator.admin` या `operator.write` हो।
  * `devices clear` को जानबूझकर `--yes` से गेट किया गया है।
  * यदि पेयरिंग स्कोप local loopback पर उपलब्ध नहीं है (और कोई स्पष्ट `--url` पास नहीं किया गया है), तो list/approve स्थानीय पेयरिंग fallback का उपयोग कर सकता है।
  * `devices approve` को टोकन जारी करने से पहले स्पष्ट अनुरोध ID चाहिए; `requestId` छोड़ना या `--latest` पास करना केवल सबसे नए लंबित अनुरोध का पूर्वावलोकन करता है।


## टोकन ड्रिफ्ट रिकवरी चेकलिस्ट

जब Control UI या अन्य क्लाइंट `AUTH_TOKEN_MISMATCH`, `AUTH_DEVICE_TOKEN_MISMATCH`, या `AUTH_SCOPE_MISMATCH` के साथ लगातार विफल हों, तब इसका उपयोग करें।

  1. मौजूदा गेटवे टोकन स्रोत की पुष्टि करें:

bashCopy code
[code]
    openclaw config get gateway.auth.token
[/code]

  2. पेयर किए गए डिवाइसों की सूची दिखाएं और प्रभावित डिवाइस id पहचानें:

bashCopy code
[code]
    openclaw devices list
[/code]

  3. प्रभावित डिवाइस के लिए ऑपरेटर टोकन घुमाएं:

bashCopy code
[code]
    openclaw devices rotate --device <deviceId> --role operator
[/code]

  4. यदि रोटेशन पर्याप्त नहीं है, तो पुरानी पेयरिंग हटाएं और फिर से अनुमोदित करें:

bashCopy code
[code]
    openclaw devices remove <deviceId>openclaw devices listopenclaw devices approve <requestId>
[/code]

  5. मौजूदा साझा टोकन/पासवर्ड के साथ क्लाइंट कनेक्शन फिर से आजमाएं।


नोट्स:

  * सामान्य रीकनेक्ट auth precedence पहले स्पष्ट साझा टोकन/पासवर्ड है, फिर स्पष्ट `deviceToken`, फिर संग्रहीत डिवाइस टोकन, फिर bootstrap टोकन।
  * विश्वसनीय `AUTH_TOKEN_MISMATCH` रिकवरी एक सीमित पुनर्प्रयास के लिए साझा टोकन और संग्रहीत डिवाइस टोकन दोनों को अस्थायी रूप से साथ भेज सकती है।
  * `AUTH_SCOPE_MISMATCH` का मतलब है कि डिवाइस टोकन पहचाना गया, लेकिन वह अनुरोधित स्कोप सेट नहीं रखता; साझा गेटवे auth बदलने से पहले पेयरिंग/स्कोप अनुमोदन अनुबंध ठीक करें।


संबंधित:

  * [Dashboard auth समस्या-निवारण](</hi/web/dashboard#if-you-see-unauthorized-1008>)
  * [Gateway समस्या-निवारण](</hi/gateway/troubleshooting#dashboard-control-ui-connectivity>)


## संबंधित

  * [CLI संदर्भ](</hi/cli>)
  * [नोड्स](</hi/nodes>)


Was this useful?YesNo

Open issue