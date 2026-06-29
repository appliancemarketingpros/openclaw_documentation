---
title: टूल-लूप पहचान
source_url: https://docs.openclaw.ai/hi/tools/loop-detection
scraped_at: 2026-06-29
---

CapabilitiesTools

OpenClaw में दोहराए जाने वाले टूल-कॉल पैटर्न के लिए दो सहयोगी गार्डरेल हैं:

  1. **लूप पहचान** (`tools.loopDetection.enabled`) — डिफ़ॉल्ट रूप से अक्षम। दोहराए गए पैटर्न और अज्ञात-टूल पुनः प्रयासों के लिए रोलिंग टूल-कॉल इतिहास देखता है।
  2. **पोस्ट-Compaction गार्ड** (`tools.loopDetection.postCompactionGuard`) — डिफ़ॉल्ट रूप से सक्षम, जब तक `tools.loopDetection.enabled` स्पष्ट रूप से `false` न हो। हर compaction-retry के बाद सक्रिय होता है और जब एजेंट विंडो के भीतर वही `(tool, args, result)` ट्रिपल उत्सर्जित करता है, तो रन को रोक देता है।


दोनों एक ही `tools.loopDetection` ब्लॉक के अंतर्गत कॉन्फ़िगर किए जाते हैं, लेकिन पोस्ट-Compaction गार्ड तब चलता है जब भी मास्टर स्विच स्पष्ट रूप से बंद नहीं होता। दोनों सतहों को शांत करने के लिए `tools.loopDetection.enabled: false` सेट करें।

## यह क्यों मौजूद है

  * ऐसी दोहराई जाने वाली अनुक्रमों का पता लगाना जो प्रगति नहीं करते।
  * उच्च-आवृत्ति वाले बिना-परिणाम लूप का पता लगाना (वही टूल, वही इनपुट, दोहराई गई त्रुटियां)।
  * ज्ञात पोलिंग टूल के लिए विशिष्ट दोहराए गए-कॉल पैटर्न का पता लगाना।
  * context-overflow फिर Compaction फिर समान-लूप चक्रों को अनिश्चित काल तक चलने से रोकना।


## कॉन्फ़िगरेशन ब्लॉक

वैश्विक डिफ़ॉल्ट, हर दस्तावेज़ित फ़ील्ड के साथ:

json5Copy code
[code]
    {  tools: {    loopDetection: {      enabled: false, // master switch for the rolling-history detectors      historySize: 30,      warningThreshold: 10,      criticalThreshold: 20,      unknownToolThreshold: 10,      globalCircuitBreakerThreshold: 30,      detectors: {        genericRepeat: true,        knownPollNoProgress: true,        pingPong: true,      },      postCompactionGuard: {        windowSize: 3, // armed after compaction-retry; runs unless enabled is explicitly false      },    },  },}
[/code]

प्रति-एजेंट ओवरराइड (वैकल्पिक):

json5Copy code
[code]
    {  agents: {    list: [      {        id: "safe-runner",        tools: {          loopDetection: {            enabled: true,            warningThreshold: 8,            criticalThreshold: 16,          },        },      },    ],  },}
[/code]

### फ़ील्ड व्यवहार

फ़ील्ड | डिफ़ॉल्ट | प्रभाव  
---|---|---  
`enabled` | `false` | रोलिंग-हिस्ट्री डिटेक्टरों के लिए मास्टर स्विच। `false` सेट करने से पोस्ट-Compaction गार्ड भी अक्षम हो जाता है।  
`historySize` | `30` | विश्लेषण के लिए रखे गए हालिया टूल कॉल की संख्या।  
`warningThreshold` | `10` | वह थ्रेशोल्ड जिसके पहले किसी पैटर्न को केवल-चेतावनी के रूप में वर्गीकृत किया जाता है।  
`criticalThreshold` | `20` | दोहराए जाने वाले बिना-प्रगति लूप पैटर्न को ब्लॉक करने का थ्रेशोल्ड।  
`unknownToolThreshold` | `10` | इतने मिस के बाद उसी अनुपलब्ध टूल पर दोहराई गई कॉल को ब्लॉक करें।  
`globalCircuitBreakerThreshold` | `30` | सभी डिटेक्टरों में वैश्विक बिना-प्रगति ब्रेकर थ्रेशोल्ड।  
`detectors.genericRepeat` | `true` | दोहराए गए समान-टूल + समान-पैरामीटर पैटर्न पर चेतावनी देता है और जब वही कॉल समान परिणाम भी लौटाते हैं, तो ब्लॉक करता है।  
`detectors.knownPollNoProgress` | `true` | बिना अवस्था परिवर्तन वाले ज्ञात पोलिंग-जैसे पैटर्न का पता लगाता है।  
`detectors.pingPong` | `true` | वैकल्पिक पिंग-पॉन्ग पैटर्न का पता लगाता है।  
`postCompactionGuard.windowSize` | `3` | पोस्ट-Compaction टूल कॉल की संख्या जिनके दौरान गार्ड सक्रिय रहता है, और समान ट्रिपल की वह गिनती जो रन को रोकती है।  
  
`exec` के लिए, बिना-प्रगति जांच स्थिर कमांड परिणामों की तुलना करती हैं और अवधि, PID, सेशन ID, और कार्यशील डायरेक्टरी जैसी परिवर्ती रनटाइम मेटाडेटा को अनदेखा करती हैं। जब कोई रन id उपलब्ध होता है, तो हालिया टूल-कॉल इतिहास का मूल्यांकन केवल उसी रन के भीतर किया जाता है ताकि शेड्यूल किए गए Heartbeat चक्र और नए रन पहले के रन से पुराने लूप काउंट विरासत में न लें।

## अनुशंसित सेटअप

  * छोटे मॉडलों के लिए, `enabled: true` सेट करें और थ्रेशोल्ड को उनके डिफ़ॉल्ट पर छोड़ दें। फ्लैगशिप मॉडलों को शायद ही रोलिंग-हिस्ट्री पहचान की आवश्यकता होती है और वे मास्टर स्विच को `false` पर छोड़ सकते हैं, जबकि पोस्ट-Compaction गार्ड से अब भी लाभ ले सकते हैं।
  * थ्रेशोल्ड को `warningThreshold < criticalThreshold < globalCircuitBreakerThreshold` क्रम में रखें।
  * यदि फ़ॉल्स पॉज़िटिव होते हैं: 
    * `warningThreshold` और/या `criticalThreshold` बढ़ाएं।
    * वैकल्पिक रूप से `globalCircuitBreakerThreshold` बढ़ाएं।
    * केवल समस्या पैदा करने वाले विशिष्ट डिटेक्टर को अक्षम करें (`detectors.<name>: false`)।
    * कम सख्त ऐतिहासिक संदर्भ के लिए `historySize` घटाएं।
  * सब कुछ अक्षम करने के लिए (पोस्ट-Compaction गार्ड सहित), `tools.loopDetection.enabled: false` स्पष्ट रूप से सेट करें।


## पोस्ट-Compaction गार्ड

जब रनर context-overflow के बाद compaction-retry पूरा करता है, तो यह एक छोटी-विंडो गार्ड सक्रिय करता है जो अगले कुछ टूल कॉल को देखता है। यदि एजेंट विंडो के भीतर कई बार वही `(toolName, argsHash, resultHash)` ट्रिपल उत्सर्जित करता है, तो गार्ड निष्कर्ष निकालता है कि Compaction ने लूप नहीं तोड़ा और रन को `compaction_loop_persisted` त्रुटि के साथ रोक देता है।

गार्ड मास्टर `tools.loopDetection.enabled` फ़्लैग से नियंत्रित होता है, एक मोड़ के साथ: यह **तब सक्षम रहता है जब फ़्लैग unset या`true` हो** और केवल तब निष्क्रिय होता है जब फ़्लैग स्पष्ट रूप से `false` हो। यह जानबूझकर है। गार्ड उन Compaction लूप से बचने के लिए मौजूद है जो अन्यथा असीमित टोकन खर्च करेंगे, इसलिए बिना-कॉन्फ़िग उपयोगकर्ता को भी सुरक्षा मिलती है।

json5Copy code
[code]
    {  tools: {    loopDetection: {      // master switch; set false to disable the guard along with the rolling detectors      enabled: true,      postCompactionGuard: {        windowSize: 3, // default      },    },  },}
[/code]

  * कम `windowSize` अधिक सख्त है (रोकने से पहले कम प्रयास)।
  * अधिक `windowSize` एजेंट को अधिक रिकवरी प्रयास देता है।
  * परिणाम बदलने पर गार्ड कभी नहीं रोकता, केवल तब जब परिणाम विंडो में बाइट-समान हों।
  * यह जानबूझकर संकीर्ण है: यह केवल compaction-retry के तुरंत बाद सक्रिय होता है।


## लॉग और अपेक्षित व्यवहार

जब कोई लूप पहचाना जाता है, OpenClaw एक लूप इवेंट रिपोर्ट करता है और गंभीरता के आधार पर अगले टूल-चक्र को या तो मंद करता है या ब्लॉक करता है। यह सामान्य टूल एक्सेस को बनाए रखते हुए उपयोगकर्ताओं को अनियंत्रित टोकन खर्च और लॉकअप से बचाता है।

  * चेतावनियां पहले आती हैं।
  * जब पैटर्न चेतावनी थ्रेशोल्ड से आगे बने रहते हैं, तो suppression होता है।
  * गंभीर थ्रेशोल्ड अगले टूल-चक्र को ब्लॉक करते हैं और रन रिकॉर्ड में स्पष्ट लूप-डिटेक्शन कारण सतह पर लाते हैं।
  * पोस्ट-Compaction गार्ड आपत्तिजनक टूल नाम और समान-कॉल गिनती के साथ `compaction_loop_persisted` त्रुटियां उत्सर्जित करता है।


## संबंधित

[**Exec स्वीकृतियां** शेल निष्पादन के लिए अनुमति/इनकार नीति। ](</hi/tools/exec-approvals>) [**Thinking स्तर** तर्क प्रयास स्तर और प्रोवाइडर-नीति अंतःक्रिया। ](</hi/tools/thinking>) [**उप-एजेंट** अनियंत्रित व्यवहार को सीमित करने के लिए अलग-थलग एजेंट शुरू करना। ](</hi/tools/subagents>) [**कॉन्फ़िगरेशन संदर्भ** पूरा `tools.loopDetection` स्कीमा और मर्जिंग सिमैंटिक्स। ](</hi/gateway/configuration-reference>)

Was this useful?YesNo

Open issue