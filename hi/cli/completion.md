---
title: पूर्णता
source_url: https://docs.openclaw.ai/hi/cli/completion
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw completion`

शेल completion scripts जनरेट करें और वैकल्पिक रूप से उन्हें अपने शेल प्रोफ़ाइल में इंस्टॉल करें।

## उपयोग

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## विकल्प

  * `-s, --shell <shell>`: शेल लक्ष्य (`zsh`, `bash`, `powershell`, `fish`; डिफ़ॉल्ट: `zsh`)
  * `-i, --install`: अपने शेल प्रोफ़ाइल में source लाइन जोड़कर completion इंस्टॉल करें
  * `--write-state`: stdout पर प्रिंट किए बिना completion script(s) को `$OPENCLAW_STATE_DIR/completions` में लिखें
  * `-y, --yes`: इंस्टॉल पुष्टिकरण प्रॉम्प्ट छोड़ें


## नोट्स

  * `--install` आपके शेल प्रोफ़ाइल में एक छोटा "OpenClaw Completion" ब्लॉक लिखता है और उसे कैश किए गए script की ओर इंगित करता है।
  * `--install` या `--write-state` के बिना, कमांड script को stdout पर प्रिंट करता है।
  * Completion जनरेशन कमांड ट्री को उत्सुकता से लोड करता है ताकि नेस्टेड सबकमांड शामिल हों।


## संबंधित

  * [CLI संदर्भ](</hi/cli>)


Was this useful?YesNo

Open issue