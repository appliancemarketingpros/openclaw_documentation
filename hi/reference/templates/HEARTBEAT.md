---
title: HEARTBEAT.md टेम्पलेट
source_url: https://docs.openclaw.ai/hi/reference/templates/HEARTBEAT
scraped_at: 2026-06-29
---

ReferenceTemplates

# HEARTBEAT.md टेम्पलेट

`HEARTBEAT.md` एजेंट कार्यक्षेत्र में रहता है। जब आप चाहते हैं कि OpenClaw heartbeat मॉडल कॉल छोड़ दे, तो फ़ाइल को खाली रखें, या केवल Markdown टिप्पणियों और शीर्षकों के साथ रखें।

डिफ़ॉल्ट runtime टेम्पलेट है:

markdownCopy code
[code]
    # Keep this file empty (or with only comments) to skip heartbeat API calls. # Add tasks below when you want the agent to check something periodically.
[/code]

टिप्पणियों के नीचे छोटे कार्य केवल तब जोड़ें जब आप चाहते हैं कि एजेंट समय-समय पर कुछ जांचे। heartbeat निर्देश छोटे रखें क्योंकि वे आवर्ती जागरणों के दौरान पढ़े जाते हैं।

## संबंधित

  * [Heartbeat कॉन्फ़िगरेशन](</hi/gateway/config-agents>)


Was this useful?YesNo

Open issue