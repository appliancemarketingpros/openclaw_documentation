---
title: Tokenjuice
source_url: https://docs.openclaw.ai/hi/tools/tokenjuice
scraped_at: 2026-06-29
---

CapabilitiesTools

`tokenjuice` एक वैकल्पिक बाहरी Plugin है, जो कमांड पहले ही चल जाने के बाद शोरगुल वाले `exec` और `bash` टूल परिणामों को संकुचित करता है।

यह लौटाए गए `tool_result` को बदलता है, कमांड को नहीं। Tokenjuice शेल इनपुट को दोबारा नहीं लिखता, कमांड दोबारा नहीं चलाता, या निकास कोड नहीं बदलता।

आज यह Codex ऐप-सर्वर हार्नेस में OpenClaw एम्बेडेड रन और OpenClaw डायनामिक टूल पर लागू होता है। Tokenjuice OpenClaw के टूल-रिज़ल्ट मिडलवेयर में हुक करता है और आउटपुट को सक्रिय हार्नेस सत्र में वापस जाने से पहले काट-छांट देता है।

## Plugin सक्षम करें

एक बार इंस्टॉल करें:

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/tokenjuice
[/code]

फिर इसे सक्षम करें:

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled true
[/code]

समतुल्य:

bashCopy code
[code]
    openclaw plugins enable tokenjuice
[/code]

यदि आप सीधे कॉन्फ़िग संपादित करना पसंद करते हैं:

json5Copy code
[code]
    {  plugins: {    entries: {      tokenjuice: {        enabled: true,      },    },  },}
[/code]

## tokenjuice क्या बदलता है

  * शोरगुल वाले `exec` और `bash` परिणामों को सत्र में वापस भेजे जाने से पहले संकुचित करता है।
  * मूल कमांड निष्पादन को अनछुआ रखता है।
  * सटीक फ़ाइल-सामग्री रीड और अन्य कमांड को सुरक्षित रखता है जिन्हें tokenjuice को कच्चा छोड़ना चाहिए।
  * ऑप्ट-इन रहता है: यदि आप हर जगह शब्दशः आउटपुट चाहते हैं, तो Plugin अक्षम करें।


## सत्यापित करें कि यह काम कर रहा है

  1. Plugin सक्षम करें।
  2. ऐसा सत्र शुरू करें जो `exec` कॉल कर सके।
  3. `git status` जैसी शोरगुल वाली कमांड चलाएँ।
  4. जाँचें कि लौटाया गया टूल परिणाम कच्चे शेल आउटपुट से छोटा और अधिक संरचित है।


## Plugin अक्षम करें

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled false
[/code]

या:

bashCopy code
[code]
    openclaw plugins disable tokenjuice
[/code]

## संबंधित

  * [Exec टूल](</hi/tools/exec>)
  * [सोच स्तर](</hi/tools/thinking>)
  * [संदर्भ इंजन](</hi/concepts/context-engine>)


Was this useful?YesNo

Open issue