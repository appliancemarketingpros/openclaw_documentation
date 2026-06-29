---
title: गोपनीय प्लेसहोल्डर परंपराएँ
source_url: https://docs.openclaw.ai/hi/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# गुप्त प्लेसहोल्डर परंपराएँ

ऐसे प्लेसहोल्डर का उपयोग करें जो मनुष्यों द्वारा पढ़े जा सकें, लेकिन वास्तविक गुप्त मानों जैसे न दिखें।

## अनुशंसित शैली

  * `example-openai-key-not-real` या `example-discord-bot-token` जैसे वर्णनात्मक मानों को प्राथमिकता दें।
  * shell स्निपेट के लिए, inline token-जैसी स्ट्रिंग के बजाय `${OPENAI_API_KEY}` को प्राथमिकता दें।
  * उदाहरणों को स्पष्ट रूप से नकली और उद्देश्य तक सीमित रखें (provider, channel, auth type)।


## docs में इन पैटर्न से बचें

  * शाब्दिक PEM निजी-key header या footer टेक्स्ट।
  * ऐसे prefixes जो live credentials जैसे दिखें, उदाहरण के लिए `sk-...`, `xoxb-...`, `AKIA...`।
  * runtime logs से कॉपी किए गए यथार्थवादी दिखने वाले bearer tokens।


## उदाहरण

bashCopy code
[code]
    # अच्छाexport OPENAI_API_KEY="example-openai-key-not-real" # बेहतर (जब doc env wiring के बारे में हो)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue