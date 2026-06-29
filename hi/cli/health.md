---
title: स्वास्थ्य
source_url: https://docs.openclaw.ai/hi/cli/health
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw health`

चल रहे Gateway से स्वास्थ्य प्राप्त करें।

## विकल्प

फ़्लैग | डिफ़ॉल्ट | विवरण  
---|---|---  
`--json` | `false` | टेक्स्ट के बजाय मशीन-पठनीय JSON प्रिंट करें।  
`--timeout <ms>` | `10000` | कनेक्शन टाइमआउट मिलीसेकंड में।  
`--verbose` | `false` | विस्तृत लॉगिंग। लाइव प्रोब को बाध्य करता है और प्रति-एजेंट आउटपुट को विस्तृत करता है।  
`--debug` | `false` | `--verbose` का उपनाम।  
  
उदाहरण:

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

नोट्स:

  * डिफ़ॉल्ट `openclaw health` चल रहे Gateway से उसका स्वास्थ्य स्नैपशॉट मांगता है। जब Gateway के पास पहले से ताज़ा कैश किया गया स्नैपशॉट होता है, तो वह वह कैश किया गया पेलोड लौटा सकता है और पृष्ठभूमि में रीफ़्रेश कर सकता है।
  * `--verbose` लाइव प्रोब को बाध्य करता है, Gateway कनेक्शन विवरण प्रिंट करता है, और सभी कॉन्फ़िगर किए गए खातों और एजेंटों में मानव-पठनीय आउटपुट को विस्तृत करता है।
  * जब कई एजेंट कॉन्फ़िगर किए गए हों, तो आउटपुट में प्रति-एजेंट सेशन स्टोर शामिल होते हैं।


## संबंधित

  * [CLI संदर्भ](</hi/cli>)
  * [Gateway स्वास्थ्य](</hi/gateway/health>)


Was this useful?YesNo

Open issue