---
title: Skills
source_url: https://docs.openclaw.ai/hi/cli/skills
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw skills`

स्थानीय Skills का निरीक्षण करें, ClawHub खोजें, ClawHub/Git/स्थानीय डायरेक्टरी से Skills इंस्टॉल करें, ClawHub Skills सत्यापित करें, और ClawHub-ट्रैक किए गए इंस्टॉल अपडेट करें।

संबंधित:

  * Skills सिस्टम: [Skills](</hi/tools/skills>)
  * Skill कार्यशाला: [Skill कार्यशाला](</hi/tools/skill-workshop>)
  * Skills कॉन्फ़िग: [Skills कॉन्फ़िग](</hi/tools/skills-config>)
  * ClawHub इंस्टॉल: [ClawHub](</hi/clawhub/cli>)


## आदेश

bashCopy code
[code]
    openclaw skills search "calendar"openclaw skills search --limit 20 --jsonopenclaw skills install @owner/<slug>openclaw skills install @owner/<slug> --version <version>openclaw skills install git:owner/repoopenclaw skills install git:owner/repo@mainopenclaw skills install ./path/to/skill --as custom-nameopenclaw skills install @owner/<slug> --forceopenclaw skills install @owner/<slug> --acknowledge-clawhub-riskopenclaw skills install @owner/<slug> --agent <id>openclaw skills install @owner/<slug> --globalopenclaw skills update @owner/<slug>openclaw skills update @owner/<slug> --acknowledge-clawhub-riskopenclaw skills update @owner/<slug> --globalopenclaw skills update --allopenclaw skills update --all --agent <id>openclaw skills update --all --globalopenclaw skills verify @owner/<slug>openclaw skills verify @owner/<slug> --version <version>openclaw skills verify @owner/<slug> --tag <tag>openclaw skills verify @owner/<slug> --cardopenclaw skills verify @owner/<slug> --globalopenclaw skills listopenclaw skills list --eligibleopenclaw skills list --jsonopenclaw skills list --verboseopenclaw skills list --agent <id>openclaw skills info <name>openclaw skills info <name> --jsonopenclaw skills info <name> --agent <id>openclaw skills checkopenclaw skills check --agent <id>openclaw skills check --jsonopenclaw skills workshop propose-create --name "qa-check" --description "QA checklist" --proposal ./PROPOSAL.mdopenclaw skills workshop propose-update qa-check --proposal ./PROPOSAL.mdopenclaw skills workshop listopenclaw skills workshop inspect <proposal-id>openclaw skills workshop revise <proposal-id> --proposal ./PROPOSAL.mdopenclaw skills workshop apply <proposal-id>openclaw skills workshop reject <proposal-id> --reason "Not reusable"openclaw skills workshop quarantine <proposal-id> --reason "Needs security review"
[/code]

`search`, `update`, और `verify` सीधे ClawHub का उपयोग करते हैं। `install @owner/<slug>` ClawHub Skill इंस्टॉल करता है, `install git:owner/repo[@ref]` Git Skill क्लोन करता है, और `install ./path` स्थानीय Skill डायरेक्टरी कॉपी करता है। डिफ़ॉल्ट रूप से, `install`, `update`, और `verify` सक्रिय वर्कस्पेस की `skills/` डायरेक्टरी को लक्षित करते हैं; `--global` के साथ, वे साझा मैनेज्ड Skills डायरेक्टरी को लक्षित करते हैं। `list`/`info`/`check` फिर भी वर्तमान वर्कस्पेस और कॉन्फ़िग को दिखाई देने वाले स्थानीय Skills का निरीक्षण करते हैं। वर्कस्पेस-समर्थित आदेश लक्ष्य वर्कस्पेस को `--agent <id>` से हल करते हैं, फिर वर्तमान कार्यशील डायरेक्टरी से जब वह किसी कॉन्फ़िगर किए गए एजेंट वर्कस्पेस के अंदर हो, फिर डिफ़ॉल्ट एजेंट से।

Git और स्थानीय डायरेक्टरी इंस्टॉल स्रोत रूट पर `SKILL.md` की अपेक्षा करते हैं। इंस्टॉल slug `SKILL.md` frontmatter `name` से आता है जब वह मान्य हो, फिर स्रोत डायरेक्टरी या रिपॉज़िटरी नाम से; इसे ओवरराइड करने के लिए `--as <slug>` उपयोग करें। `--version` केवल ClawHub के लिए है। Skill इंस्टॉल npm पैकेज specs या zip/archive पाथ का समर्थन नहीं करते, और `openclaw skills update` केवल ClawHub-ट्रैक किए गए इंस्टॉल अपडेट करता है।

ऑनबोर्डिंग या Skills सेटिंग से ट्रिगर किए गए Gateway-समर्थित Skill dependency इंस्टॉल इसके बजाय अलग `skills.install` अनुरोध पाथ का उपयोग करते हैं।

नोट्स:

  * `search [query...]` वैकल्पिक क्वेरी स्वीकार करता है; डिफ़ॉल्ट ClawHub खोज फ़ीड ब्राउज़ करने के लिए इसे छोड़ दें।
  * `search --limit <n>` लौटाए गए परिणामों की सीमा तय करता है।
  * `install git:owner/repo[@ref]` Git Skill इंस्टॉल करता है। Branch refs में स्लैश हो सकते हैं, जैसे `git:owner/repo@feature/foo`।
  * `install ./path/to/skill` ऐसी स्थानीय डायरेक्टरी इंस्टॉल करता है जिसके रूट में `SKILL.md` होता है।
  * `install --as <slug>` Git और स्थानीय डायरेक्टरी इंस्टॉल के लिए अनुमानित slug को ओवरराइड करता है।
  * `install --version <version>` केवल ClawHub Skill refs पर लागू होता है।
  * `install --force` उसी slug के लिए मौजूदा वर्कस्पेस Skill फ़ोल्डर को ओवरराइट करता है।
  * कम्युनिटी ClawHub Skill इंस्टॉल और अपडेट डाउनलोड करने से पहले trust जांचते हैं। Versioned community archive releases exact-release trust metadata का उपयोग करते हैं। Resolver-backed GitHub Skills ClawHub के install resolver पर निर्भर करते हैं ताकि pinned commit लौटाने से पहले scan और force-install policy लागू हो। दुर्भावनापूर्ण या ब्लॉक किए गए community releases अस्वीकार किए जाते हैं। Risky community releases को समीक्षा और `--acknowledge-clawhub-risk` की आवश्यकता होती है जब कोई non-interactive command उस समीक्षा के बाद जारी रहना चाहिए। आधिकारिक ClawHub Skill publishers और bundled OpenClaw Skill sources इस release-trust prompt को बायपास करते हैं।
  * `--global` साझा मैनेज्ड Skills डायरेक्टरी को लक्षित करता है और इसे `--agent <id>` के साथ जोड़ा नहीं जा सकता।
  * `--agent <id>` एक कॉन्फ़िगर किए गए एजेंट वर्कस्पेस को लक्षित करता है और वर्तमान कार्यशील डायरेक्टरी inference को ओवरराइड करता है।
  * `update @owner/<slug>` एक tracked Skill अपडेट करता है। वर्कस्पेस के बजाय साझा मैनेज्ड Skills डायरेक्टरी को लक्षित करने के लिए `--global` जोड़ें।
  * `update --all` चुने गए वर्कस्पेस में tracked ClawHub installs अपडेट करता है, या `--global` के साथ जोड़े जाने पर साझा मैनेज्ड Skills डायरेक्टरी में।
  * `verify @owner/<slug>` डिफ़ॉल्ट रूप से ClawHub का `clawhub.skill.verify.v1` JSON envelope प्रिंट करता है। कोई `--json` flag नहीं है क्योंकि JSON पहले से ही डिफ़ॉल्ट है। Bare slugs compatibility के लिए तब भी स्वीकार किए जाते हैं जब Skill पहले से इंस्टॉल हो या ambiguous न हो, लेकिन owner-qualified refs publisher ambiguity से बचाते हैं।
  * जब ClawHub server-resolved source provenance लौटाता है, verify JSON में commit-pinned `openclaw.verifiedSourceUrl` भी शामिल होता है। अनुपलब्ध या self-declared source URLs केवल raw provenance envelope में रहते हैं और promote नहीं किए जाते।
  * `verify` इंस्टॉल किए गए ClawHub Skills के लिए `.clawhub/origin.json` उपयोग करता है, इसलिए यह इंस्टॉल किए गए version को उसी registry के विरुद्ध सत्यापित करता है जहां से वह आया था। `--version` और `--tag` version selector को ओवरराइड करते हैं लेकिन origin metadata मौजूद होने पर उस इंस्टॉल registry को बनाए रखते हैं।
  * `verify --card` JSON के बजाय generated Skill Card Markdown प्रिंट करता है। आदेश non-zero के साथ exit करता है जब ClawHub `ok: false` या `decision: "fail"` लौटाता है; unsigned signatures informational हैं जब तक ClawHub policy न बदले।
  * इंस्टॉल किए गए ClawHub bundles में generated `skill-card.md` शामिल हो सकता है। OpenClaw verification को ClawHub server decision मानता है और किसी इंस्टॉल किए गए Skill को केवल इसलिए reject नहीं करता कि वह generated card bundle fingerprint बदलता है।
  * `check --agent <id>` चुने गए एजेंट के वर्कस्पेस को जांचता है और रिपोर्ट करता है कि कौन से ready Skills वास्तव में उस एजेंट के prompt या command surface को दिखाई देते हैं।
  * कोई subcommand नहीं दिए जाने पर `list` डिफ़ॉल्ट action है।
  * `list`, `info`, और `check` अपना rendered output stdout पर लिखते हैं। `--json` के साथ, इसका मतलब है कि machine-readable payload pipes और scripts के लिए stdout पर रहता है।


## Skill कार्यशाला

`openclaw skills workshop` चुने गए वर्कस्पेस में लंबित Skill proposals प्रबंधित करता है। Proposals लागू होने तक सक्रिय Skills नहीं होते। proposal storage, support-file safeguards, Gateway methods, और approval policy के लिए [Skill कार्यशाला](</hi/tools/skill-workshop>) देखें।

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name "qa-check" \  --description "Repeatable QA checklist" \  --proposal ./PROPOSAL.mdopenclaw skills workshop propose-create \  --name "qa-check" \  --description "Repeatable QA checklist" \  --proposal-dir ./qa-check-proposalopenclaw skills workshop propose-update qa-check --proposal ./PROPOSAL.mdopenclaw skills workshop listopenclaw skills workshop inspect <proposal-id>openclaw skills workshop revise <proposal-id> --proposal ./PROPOSAL.mdopenclaw skills workshop apply <proposal-id>openclaw skills workshop reject <proposal-id> --reason "Duplicate"openclaw skills workshop quarantine <proposal-id> --reason "Needs security review"
[/code]

## संबंधित

  * [CLI संदर्भ](</hi/cli>)
  * [Skills](</hi/tools/skills>)


Was this useful?YesNo

Open issue