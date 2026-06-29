---
title: रीसेट
source_url: https://docs.openclaw.ai/hi/cli/reset
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw reset`

स्थानीय कॉन्फ़िगरेशन/स्थिति रीसेट करें (CLI इंस्टॉल रहता है)।

विकल्प:

  * `--scope <scope>`: `config`, `config+creds+sessions`, या `full`
  * `--yes`: पुष्टि संकेतों को छोड़ें
  * `--non-interactive`: संकेतों को अक्षम करें; `--scope` और `--yes` आवश्यक हैं
  * `--dry-run`: फ़ाइलें हटाए बिना कार्रवाइयाँ प्रिंट करें


उदाहरण:

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

टिप्पणियाँ:

  * स्थानीय स्थिति हटाने से पहले यदि आप पुनर्स्थापित करने योग्य स्नैपशॉट चाहते हैं, तो पहले `openclaw backup create` चलाएँ।
  * यदि आप `--scope` छोड़ देते हैं, तो `openclaw reset` क्या हटाना है यह चुनने के लिए एक इंटरैक्टिव संकेत का उपयोग करता है।
  * `--non-interactive` केवल तभी मान्य है जब `--scope` और `--yes` दोनों सेट हों।


## संबंधित

  * [CLI संदर्भ](</hi/cli>)


Was this useful?YesNo

Open issue