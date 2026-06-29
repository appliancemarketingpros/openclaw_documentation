---
title: दस्तावेज़
source_url: https://docs.openclaw.ai/hi/cli/docs
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw docs`

टर्मिनल से लाइव OpenClaw docs इंडेक्स खोजें। यह कमांड OpenClaw के Cloudflare-होस्टेड docs search API को कॉल करता है और परिणाम आपके टर्मिनल में रेंडर करता है।

## उपयोग

bashCopy code
[code]
    openclaw docs                       # print docs entrypoint and example searchopenclaw docs <query...>            # search the live docs index
[/code]

आर्ग्युमेंट:

आर्ग्युमेंट | विवरण  
---|---  
`[query...]` | मुक्त-रूप खोज क्वेरी। कई शब्दों वाली क्वेरी को रिक्त स्थानों से जोड़ा जाता है और एक के रूप में भेजा जाता है।  
  
## उदाहरण

bashCopy code
[code]
    openclaw docs browser existing-sessionopenclaw docs sandbox allowHostControlopenclaw docs gateway token secretref
[/code]

बिना क्वेरी के, `openclaw docs` खोज चलाने के बजाय docs एंट्रीपॉइंट URL और एक नमूना खोज कमांड प्रिंट करता है।

## यह कैसे काम करता है

`openclaw docs` `https://docs.openclaw.ai/api/search` को कॉल करता है और JSON परिणाम रेंडर करता है। खोज कॉल एक निश्चित 30 सेकंड टाइमआउट का उपयोग करता है।

## आउटपुट

रिच (TTY) टर्मिनल में, परिणाम एक शीर्षक के बाद बुलेट सूची के रूप में रेंडर होते हैं। हर बुलेट पेज शीर्षक, लिंक किया हुआ docs URL, और अगली पंक्ति में एक छोटा स्निपेट दिखाता है। खाली परिणाम "No results." प्रिंट करते हैं।

नॉन-रिच आउटपुट (पाइप किया हुआ, `--no-color`, scripts) में, वही डेटा Markdown के रूप में रेंडर होता है:

markdownCopy code
[code]
    # Docs search: <query> - [Title](https://docs.openclaw.ai/...) - snippet- [Title](https://docs.openclaw.ai/...) - snippet
[/code]

## एग्ज़िट कोड

कोड | अर्थ  
---|---  
`0` | खोज सफल रही (शून्य-परिणाम प्रतिक्रियाओं सहित)।  
`1` | होस्टेड docs search API कॉल विफल हुई; stderr इनलाइन प्रिंट होता है।  
  
## संबंधित

  * [CLI संदर्भ](</hi/cli>)
  * [लाइव docs](<https://docs.openclaw.ai>)


Was this useful?YesNo

Open issue