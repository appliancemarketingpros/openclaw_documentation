---
title: चैनल स्थान पार्सिंग
source_url: https://docs.openclaw.ai/hi/channels/location
scraped_at: 2026-06-29
---

ChannelsConfiguration

OpenClaw चैट चैनलों से साझा स्थानों को सामान्यीकृत करके इन्हें बनाता है:

  * इनबाउंड मुख्य भाग में जोड़ा गया संक्षिप्त निर्देशांक टेक्स्ट, और
  * ऑटो-रिप्लाई संदर्भ पेलोड में संरचित फ़ील्ड। चैनल से मिले लेबल, पते, और कैप्शन/टिप्पणियां उपयोगकर्ता के मुख्य भाग में इनलाइन नहीं, बल्कि साझा अविश्वसनीय मेटाडेटा JSON ब्लॉक के माध्यम से प्रॉम्प्ट में रेंडर किए जाते हैं।


वर्तमान में समर्थित:

  * **Telegram** (लोकेशन पिन + स्थल + लाइव लोकेशन)
  * **WhatsApp** (locationMessage + liveLocationMessage)
  * **Matrix** (`m.location` जिसमें `geo_uri` है)


## टेक्स्ट फ़ॉर्मैटिंग

स्थान ब्रैकेट के बिना अनुकूल पंक्तियों के रूप में रेंडर किए जाते हैं:

  * पिन: 
    * `📍 48.858844, 2.294351 ±12m`
  * नामित स्थान: 
    * `📍 48.858844, 2.294351 ±12m`
  * लाइव शेयर: 
    * `🛰 Live location: 48.858844, 2.294351 ±12m`


यदि चैनल में कोई लेबल, पता, या कैप्शन/टिप्पणी शामिल है, तो उसे संदर्भ पेलोड में सुरक्षित रखा जाता है और वह प्रॉम्प्ट में फेंस किए गए अविश्वसनीय JSON के रूप में दिखाई देता है:

textCopy code
[code]
    Location (untrusted metadata):```json{  "latitude": 48.858844,  "longitude": 2.294351,  "name": "Eiffel Tower",  "address": "Champ de Mars, Paris",  "caption": "Meet here"}```
[/code]

## संदर्भ फ़ील्ड

जब कोई स्थान मौजूद होता है, तो ये फ़ील्ड `ctx` में जोड़े जाते हैं:

  * `LocationLat` (number)
  * `LocationLon` (number)
  * `LocationAccuracy` (number, मीटर; वैकल्पिक)
  * `LocationName` (string; वैकल्पिक)
  * `LocationAddress` (string; वैकल्पिक)
  * `LocationSource` (`pin | place | live`)
  * `LocationIsLive` (boolean)
  * `LocationCaption` (string; वैकल्पिक)


प्रॉम्प्ट रेंडरर `LocationName`, `LocationAddress`, और `LocationCaption` को अविश्वसनीय मेटाडेटा मानता है और उन्हें अन्य चैनल संदर्भ के लिए उपयोग किए जाने वाले उसी सीमित JSON पथ के माध्यम से सीरियलाइज़ करता है।

## चैनल नोट्स

  * **Telegram** : स्थल `LocationName/LocationAddress` में मैप होते हैं; लाइव लोकेशन `live_period` का उपयोग करती हैं।
  * **WhatsApp** : `locationMessage.comment` और `liveLocationMessage.caption` `LocationCaption` को भरते हैं।
  * **Matrix** : `geo_uri` को पिन लोकेशन के रूप में पार्स किया जाता है; ऊंचाई को अनदेखा किया जाता है और `LocationIsLive` हमेशा false होता है।


## संबंधित

  * [स्थान कमांड (नोड)](</hi/nodes/location-command>)
  * [कैमरा कैप्चर](</hi/nodes/camera>)
  * [मीडिया समझ](</hi/nodes/media-understanding>)


Was this useful?YesNo

Open issue