---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/hi/cli/commitments
scraped_at: 2026-06-29
---

ReferenceCLI commands

अनुमानित फ़ॉलो-अप प्रतिबद्धताओं को सूचीबद्ध और प्रबंधित करें।

प्रतिबद्धताएँ opt-in, अल्पकालिक फ़ॉलो-अप स्मृतियाँ हैं, जो बातचीत के संदर्भ से बनाई जाती हैं। वैचारिक मार्गदर्शिका के लिए [अनुमानित प्रतिबद्धताएँ](</hi/concepts/commitments>) देखें।

किसी subcommand के बिना, `openclaw commitments` लंबित प्रतिबद्धताओं को सूचीबद्ध करता है।

## उपयोग

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## विकल्प

  * `--all`: केवल लंबित प्रतिबद्धताओं के बजाय सभी स्थितियाँ दिखाएँ।
  * `--agent <id>`: एक एजेंट आईडी तक फ़िल्टर करें।
  * `--status <status>`: स्थिति के आधार पर फ़िल्टर करें। मान: `pending`, `sent`, `dismissed`, `snoozed`, या `expired`।
  * `--json`: मशीन-पठनीय JSON आउटपुट करें।


## उदाहरण

लंबित प्रतिबद्धताओं को सूचीबद्ध करें:

bashCopy code
[code]
    openclaw commitments
[/code]

संग्रहीत हर प्रतिबद्धता को सूचीबद्ध करें:

bashCopy code
[code]
    openclaw commitments --all
[/code]

एक एजेंट तक फ़िल्टर करें:

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

स्नूज़ की गई प्रतिबद्धताएँ खोजें:

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

एक या अधिक प्रतिबद्धताएँ खारिज करें:

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

JSON के रूप में निर्यात करें:

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## आउटपुट

टेक्स्ट आउटपुट में शामिल हैं:

  * प्रतिबद्धता आईडी
  * स्थिति
  * प्रकार
  * सबसे प्रारंभिक नियत समय
  * दायरा
  * सुझाया गया check-in टेक्स्ट


JSON आउटपुट में प्रतिबद्धता स्टोर पथ और पूर्ण संग्रहीत रिकॉर्ड भी शामिल होते हैं।

## संबंधित

  * [अनुमानित प्रतिबद्धताएँ](</hi/concepts/commitments>)
  * [मेमरी अवलोकन](</hi/concepts/memory>)
  * [Heartbeat](</hi/gateway/heartbeat>)
  * [निर्धारित कार्य](</hi/automation/cron-jobs>)


Was this useful?YesNo

Open issue