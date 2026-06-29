---
title: Codex पर्यवेक्षक Plugin
source_url: https://docs.openclaw.ai/hi/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Codex Supervisor Plugin

OpenClaw से Codex app-server सत्रों की निगरानी करें।

## वितरण

  * पैकेज: `@openclaw/codex-supervisor`
  * इंस्टॉल मार्ग: OpenClaw में शामिल


## सतह

contracts: tools

## सत्र सूचीकरण

`codex_sessions_list` डिफ़ॉल्ट रूप से केवल लोड किए गए Codex सत्रों तक सीमित रहता है। संग्रहीत इतिहास शामिल करने के लिए `include_stored` सेट करें; Plugin Codex app-server के state-DB-only सूचीकरण पथ का उपयोग करता है और संग्रहीत परिणामों को डिफ़ॉल्ट रूप से 200 तक सीमित करता है। इस सीमा को घटाने या बढ़ाने के लिए, अधिकतम 1000 तक, `max_stored_sessions` पास करें।

Was this useful?YesNo

Open issue