---
title: डैशबोर्ड
source_url: https://docs.openclaw.ai/hi/cli/dashboard
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw dashboard`

अपने वर्तमान auth का उपयोग करके Control UI खोलें।

bashCopy code
[code]
    openclaw dashboardopenclaw dashboard --no-open
[/code]

नोट्स:

  * `dashboard` संभव होने पर कॉन्फ़िगर किए गए `gateway.auth.token` SecretRefs को resolve करता है।
  * `dashboard` `gateway.tls.enabled` का पालन करता है: TLS-सक्षम gateways `https://` Control UI URLs को print/open करते हैं और `wss://` पर connect करते हैं।
  * यदि token-authenticated dashboard URL के लिए clipboard/browser delivery विफल होती है, तो `dashboard` token value print किए बिना `OPENCLAW_GATEWAY_TOKEN`, `gateway.auth.token`, और fragment key `token` का नाम देते हुए एक सुरक्षित manual-auth hint log करता है।
  * SecretRef-managed tokens (resolved या unresolved) के लिए, `dashboard` terminal output, clipboard history, या browser-launch arguments में external secrets को उजागर करने से बचने के लिए non-tokenized URL print/copy/open करता है।
  * यदि `gateway.auth.token` SecretRef-managed है लेकिन इस command path में unresolved है, तो command invalid token placeholder embed करने के बजाय non-tokenized URL और स्पष्ट remediation guidance print करता है।


## संबंधित

  * [CLI reference](</hi/cli>)
  * [Dashboard](</hi/web/dashboard>)


Was this useful?YesNo

Open issue