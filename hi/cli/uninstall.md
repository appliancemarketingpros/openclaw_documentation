---
title: अनइंस्टॉल करें
source_url: https://docs.openclaw.ai/hi/cli/uninstall
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw uninstall`

Gateway सेवा + स्थानीय डेटा अनइंस्टॉल करें (CLI बनी रहती है)।

विकल्प:

  * `--service`: Gateway सेवा हटाएं
  * `--state`: स्थिति और कॉन्फ़िग हटाएं
  * `--workspace`: वर्कस्पेस डायरेक्टरियां हटाएं
  * `--app`: macOS ऐप हटाएं
  * `--all`: सेवा, स्थिति, वर्कस्पेस और ऐप हटाएं
  * `--yes`: पुष्टि प्रॉम्प्ट छोड़ें
  * `--non-interactive`: प्रॉम्प्ट अक्षम करें; `--yes` आवश्यक है
  * `--dry-run`: फ़ाइलें हटाए बिना कार्रवाइयां प्रिंट करें


उदाहरण:

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

नोट्स:

  * यदि आप स्थिति या वर्कस्पेस हटाने से पहले पुनर्स्थापित की जा सकने वाली स्नैपशॉट चाहते हैं, तो पहले `openclaw backup create` चलाएं।
  * जब तक `--workspace` भी चयनित न हो, `--state` कॉन्फ़िगर की गई वर्कस्पेस डायरेक्टरियां सुरक्षित रखता है।
  * `--all` सेवा, स्थिति, वर्कस्पेस और ऐप को साथ में हटाने का संक्षिप्त रूप है।
  * `--non-interactive` के लिए `--yes` आवश्यक है।


## संबंधित

  * [CLI संदर्भ](</hi/cli>)
  * [अनइंस्टॉल](</hi/install/uninstall>)


Was this useful?YesNo

Open issue