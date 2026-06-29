---
title: उन्नत मोड
source_url: https://docs.openclaw.ai/hi/tools/elevated
scraped_at: 2026-06-29
---

CapabilitiesTools

जब कोई agent sandbox के अंदर चलता है, तो उसके `exec` commands sandbox environment तक सीमित रहते हैं। **एलिवेटेड मोड** agent को इससे बाहर निकलकर sandbox के बाहर commands चलाने देता है, configurable approval gates के साथ।

## Directives

Slash commands से प्रति-session एलिवेटेड मोड नियंत्रित करें:

Directive | यह क्या करता है  
---|---  
`/elevated on` | configured host path पर sandbox के बाहर चलाएं, approvals बनाए रखें  
`/elevated ask` | `on` जैसा ही (alias)  
`/elevated full` | configured host path पर sandbox के बाहर चलाएं और approvals छोड़ दें  
`/elevated off` | sandbox-confined execution पर वापस जाएं  
  
यह `/elev on|off|ask|full` के रूप में भी उपलब्ध है।

वर्तमान level देखने के लिए बिना argument के `/elevated` भेजें।

## यह कैसे काम करता है

* ### उपलब्धता जांचें

Elevated को config में enabled होना चाहिए और sender allowlist पर होना चाहिए:

json5Copy code
[code]
    {  tools: {    elevated: {      enabled: true,      allowFrom: {        discord: ["user-id-123"],        whatsapp: ["+15555550123"],      },    },  },}
[/code]

* ### Level सेट करें

session default सेट करने के लिए directive-only message भेजें:

CodeCopy code
[code]
    /elevated full
[/code]

या इसे inline उपयोग करें (केवल उस message पर लागू होता है):

CodeCopy code
[code]
    /elevated on run the deployment script
[/code]

* ### Commands sandbox के बाहर चलते हैं

Elevated active होने पर, `exec` calls sandbox छोड़ देती हैं। Effective host default रूप से `gateway` होता है, या `node` जब configured/session exec target `node` हो। `full` mode में, exec approvals छोड़ दिए जाते हैं। `on`/`ask` mode में, configured approval rules फिर भी लागू होते हैं।

## Resolution order

  1. message पर **Inline directive** (केवल उस message पर लागू होता है)
  2. **Session override** (directive-only message भेजकर सेट किया गया)
  3. **Global default** (config में `agents.defaults.elevatedDefault`)


## उपलब्धता और allowlists

  * **Global gate** : `tools.elevated.enabled` (`true` होना चाहिए)
  * **Sender allowlist** : per-channel lists के साथ `tools.elevated.allowFrom`
  * **Per-agent gate** : `agents.list[].tools.elevated.enabled` (केवल और restrict कर सकता है)
  * **Per-agent allowlist** : `agents.list[].tools.elevated.allowFrom` (sender को global + per-agent दोनों से match करना होगा)
  * **Discord fallback** : यदि `tools.elevated.allowFrom.discord` omit किया गया है, तो `channels.discord.allowFrom` fallback के रूप में उपयोग होता है
  * **सभी gates pass होने चाहिए** ; अन्यथा elevated को unavailable माना जाता है


Allowlist entry formats:

Prefix | Matches  
---|---  
(none) | Sender ID, E.164, या From field  
`name:` | Sender display name  
`username:` | Sender username  
`tag:` | Sender tag  
`id:`, `from:`, `e164:` | Explicit identity targeting  
  
## Elevated क्या नियंत्रित नहीं करता

  * **Tool policy** : यदि `exec` tool policy द्वारा denied है, तो elevated इसे override नहीं कर सकता।
  * **Host selection policy** : elevated `auto` को free cross-host override में नहीं बदलता। यह configured/session exec target rules का उपयोग करता है, और `node` केवल तब चुनता है जब target पहले से ही `node` हो।
  * **`/exec` से अलग**: `/exec` directive authorized senders के लिए per-session exec defaults adjust करता है और इसके लिए elevated mode की आवश्यकता नहीं होती।


## संबंधित

[**Exec tool** agent से shell command execution। ](</hi/tools/exec>) [**Exec approvals** `exec` के लिए approval और allowlist system। ](</hi/tools/exec-approvals>) [**Sandboxing** Gateway-level sandbox configuration। ](</hi/gateway/sandboxing>) [**Sandbox vs Tool Policy vs Elevated** tool call के दौरान तीनों gates कैसे compose होते हैं। ](</hi/gateway/sandbox-vs-tool-policy-vs-elevated>)

Was this useful?YesNo

Open issue