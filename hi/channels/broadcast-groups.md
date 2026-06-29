---
title: ब्रॉडकास्ट समूह
source_url: https://docs.openclaw.ai/hi/channels/broadcast-groups
scraped_at: 2026-06-29
---

ChannelsConfiguration

## अवलोकन

Broadcast Groups कई एजेंटों को एक ही संदेश को साथ-साथ प्रोसेस करने और जवाब देने में सक्षम बनाते हैं। इससे आप विशेषीकृत एजेंट टीमें बना सकते हैं जो एक ही WhatsApp समूह या DM में साथ काम करती हैं — सब कुछ एक ही फ़ोन नंबर से।

वर्तमान दायरा: **केवल WhatsApp** (वेब चैनल)।

Broadcast groups का मूल्यांकन चैनल allowlists और समूह सक्रियण नियमों के बाद किया जाता है। WhatsApp समूहों में, इसका मतलब है कि broadcasts तब होते हैं जब OpenClaw सामान्य रूप से जवाब देता (उदाहरण के लिए: mention पर, आपकी समूह सेटिंग्स के अनुसार)।

## उपयोग के मामले

1\. विशेषीकृत एजेंट टीमें

परमाणु, केंद्रित जिम्मेदारियों वाले कई एजेंट तैनात करें:

CodeCopy code
[code]
    Group: "Development Team"Agents:  - CodeReviewer (reviews code snippets)  - DocumentationBot (generates docs)  - SecurityAuditor (checks for vulnerabilities)  - TestGenerator (suggests test cases)
[/code]

प्रत्येक एजेंट उसी संदेश को प्रोसेस करता है और अपना विशेषीकृत दृष्टिकोण देता है।

2\. बहुभाषी सहायता CodeCopy code
[code]
    Group: "International Support"Agents:  - Agent_EN (responds in English)  - Agent_DE (responds in German)  - Agent_ES (responds in Spanish)
[/code]

3\. गुणवत्ता आश्वासन वर्कफ़्लो CodeCopy code
[code]
    Group: "Customer Support"Agents:  - SupportAgent (provides answer)  - QAAgent (reviews quality, only responds if issues found)
[/code]

4\. कार्य ऑटोमेशन CodeCopy code
[code]
    Group: "Project Management"Agents:  - TaskTracker (updates task database)  - TimeLogger (logs time spent)  - ReportGenerator (creates summaries)
[/code]

## कॉन्फ़िगरेशन

### मूल सेटअप

एक शीर्ष-स्तरीय `broadcast` सेक्शन जोड़ें (`bindings` के पास)। कुंजियां WhatsApp peer ids हैं:

  * समूह चैट: समूह JID (जैसे `120363403215116621@g.us`)
  * DMs: E.164 फ़ोन नंबर (जैसे `+15551234567`)

jsonCopy code
[code]
    {  "broadcast": {    "120363403215116621@g.us": ["alfred", "baerbel", "assistant3"]  }}
[/code]

**परिणाम:** जब OpenClaw इस चैट में जवाब देता, तो यह तीनों एजेंट चलाएगा।

### प्रोसेसिंग रणनीति

नियंत्रित करें कि एजेंट संदेशों को कैसे प्रोसेस करें:

### parallel (डिफ़ॉल्ट)

सभी एजेंट साथ-साथ प्रोसेस करते हैं:

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### sequential

एजेंट क्रम में प्रोसेस करते हैं (एक पिछले के पूरा होने की प्रतीक्षा करता है):

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### पूरा उदाहरण

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "code-reviewer",        "name": "Code Reviewer",        "workspace": "/path/to/code-reviewer",        "sandbox": { "mode": "all" }      },      {        "id": "security-auditor",        "name": "Security Auditor",        "workspace": "/path/to/security-auditor",        "sandbox": { "mode": "all" }      },      {        "id": "docs-generator",        "name": "Documentation Generator",        "workspace": "/path/to/docs-generator",        "sandbox": { "mode": "all" }      }    ]  },  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["code-reviewer", "security-auditor", "docs-generator"],    "120363424282127706@g.us": ["support-en", "support-de"],    "+15555550123": ["assistant", "logger"]  }}
[/code]

## यह कैसे काम करता है

### संदेश प्रवाह

* ### आने वाला संदेश पहुंचता है

WhatsApp समूह या DM संदेश पहुंचता है।

* ### रूट और प्रवेश

OpenClaw चैनल allowlists, समूह सक्रियण नियम, और कॉन्फ़िगर की गई ACP binding ownership लागू करता है।

* ### Broadcast जांच

यदि कोई कॉन्फ़िगर की गई ACP binding रूट की मालिक नहीं है, तो OpenClaw जांचता है कि peer ID `broadcast` में है या नहीं।

* ### यदि broadcast लागू होता है

  * सूचीबद्ध सभी एजेंट संदेश प्रोसेस करते हैं।
  * प्रत्येक एजेंट की अपनी session key और isolated context होती है।
  * एजेंट parallel (डिफ़ॉल्ट) या sequentially प्रोसेस करते हैं।


* ### यदि broadcast लागू नहीं होता

OpenClaw सामान्य रूट या routing के दौरान चुने गए कॉन्फ़िगर किए गए ACP session route को dispatch करता है।

### Session isolation

Broadcast group में प्रत्येक एजेंट पूरी तरह अलग रखता है:

  * **Session keys** (`agent:alfred:whatsapp:group:120363...` बनाम `agent:baerbel:whatsapp:group:120363...`)
  * **वार्तालाप इतिहास** (एजेंट दूसरे एजेंटों के संदेश नहीं देखता)
  * **Workspace** (यदि कॉन्फ़िगर हो तो अलग sandboxes)
  * **Tool access** (अलग allow/deny सूचियां)
  * **Memory/context** (अलग IDENTITY.md, SOUL.md, आदि)
  * **Group context buffer** (context के लिए उपयोग किए गए हाल के समूह संदेश) प्रति peer साझा होता है, इसलिए trigger होने पर सभी broadcast agents को वही context दिखता है


इससे प्रत्येक एजेंट के पास हो सकता है:

  * अलग personalities
  * अलग tool access (जैसे, read-only बनाम read-write)
  * अलग models (जैसे, opus बनाम sonnet)
  * अलग Skills इंस्टॉल की गईं


### उदाहरण: isolated sessions

समूह `120363403215116621@g.us` में एजेंट `["alfred", "baerbel"]` के साथ:

### Alfred का context

CodeCopy code
[code]
    Session: agent:alfred:whatsapp:group:120363403215116621@g.usHistory: [user message, alfred's previous responses]Workspace: /Users/user/openclaw-alfred/Tools: read, write, exec
[/code]

### Bärbel का context

CodeCopy code
[code]
    Session: agent:baerbel:whatsapp:group:120363403215116621@g.usHistory: [user message, baerbel's previous responses]Workspace: /Users/user/openclaw-baerbel/Tools: read only
[/code]

## सर्वोत्तम अभ्यास

1\. एजेंटों को केंद्रित रखें

प्रत्येक एजेंट को एक ही, स्पष्ट जिम्मेदारी के साथ डिज़ाइन करें:

jsonCopy code
[code]
    {  "broadcast": {    "DEV_GROUP": ["formatter", "linter", "tester"]  }}
[/code]

✅ **अच्छा:** प्रत्येक एजेंट का एक काम है। ❌ **खराब:** एक generic "dev-helper" एजेंट।

2\. वर्णनात्मक नाम इस्तेमाल करें

यह स्पष्ट करें कि प्रत्येक एजेंट क्या करता है:

jsonCopy code
[code]
    {  "agents": {    "security-scanner": { "name": "Security Scanner" },    "code-formatter": { "name": "Code Formatter" },    "test-generator": { "name": "Test Generator" }  }}
[/code]

3\. अलग tool access कॉन्फ़िगर करें

एजेंटों को केवल वे tools दें जिनकी उन्हें जरूरत है:

jsonCopy code
[code]
    {  "agents": {    "reviewer": {      "tools": { "allow": ["read", "exec"] }    },    "fixer": {      "tools": { "allow": ["read", "write", "edit", "exec"] }    }  }}
[/code]

`reviewer` read-only है। `fixer` पढ़ और लिख सकता है।

4\. प्रदर्शन पर नजर रखें

कई एजेंटों के साथ, विचार करें:

  * गति के लिए `"strategy": "parallel"` (डिफ़ॉल्ट) का उपयोग
  * Broadcast groups को 5-10 एजेंटों तक सीमित करना
  * सरल एजेंटों के लिए तेज models का उपयोग

5\. विफलताओं को सहजता से संभालें

एजेंट स्वतंत्र रूप से विफल होते हैं। एक एजेंट की त्रुटि दूसरों को block नहीं करती:

CodeCopy code
[code]
    Message → [Agent A ✓, Agent B ✗ error, Agent C ✓]Result: Agent A and C respond, Agent B logs error
[/code]

## संगतता

### Providers

Broadcast groups फिलहाल इनके साथ काम करते हैं:

  * ✅ WhatsApp (लागू)
  * 🚧 Telegram (योजनाबद्ध)
  * 🚧 Discord (योजनाबद्ध)
  * 🚧 Slack (योजनाबद्ध)


### Routing

Broadcast groups मौजूदा routing के साथ काम करते हैं:

jsonCopy code
[code]
    {  "bindings": [    {      "match": { "channel": "whatsapp", "peer": { "kind": "group", "id": "GROUP_A" } },      "agentId": "alfred"    }  ],  "broadcast": {    "GROUP_B": ["agent1", "agent2"]  }}
[/code]

  * `GROUP_A`: केवल alfred जवाब देता है (सामान्य routing)।
  * `GROUP_B`: agent1 और agent2 जवाब देते हैं (broadcast)।


## समस्या निवारण

एजेंट जवाब नहीं दे रहे

**जांचें:**

  1. Agent IDs `agents.list` में मौजूद हैं।
  2. Peer ID format सही है (जैसे, `120363403215116621@g.us`)।
  3. एजेंट deny सूचियों में नहीं हैं।


**Debug:**

bashCopy code
[code]
    tail -f ~/.openclaw/logs/gateway.log | grep broadcast
[/code]

केवल एक एजेंट जवाब दे रहा है

**कारण:** Peer ID सामान्य route bindings में हो सकता है लेकिन `broadcast` में नहीं, या यह किसी exclusive configured ACP binding से match हो सकता है।

**समाधान:** सामान्य route-bound peers को broadcast config में जोड़ें, या यदि fan-out broadcast चाहिए तो configured ACP binding को हटाएं/बदलें।

प्रदर्शन समस्याएं

यदि कई एजेंटों के साथ धीमा हो:

  * प्रति समूह एजेंटों की संख्या घटाएं।
  * हल्के models का उपयोग करें (opus के बजाय sonnet)।
  * Sandbox startup time जांचें।


## उदाहरण

उदाहरण 1: Code review team jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": [      "code-formatter",      "security-scanner",      "test-coverage",      "docs-checker"    ]  },  "agents": {    "list": [      {        "id": "code-formatter",        "workspace": "~/agents/formatter",        "tools": { "allow": ["read", "write"] }      },      {        "id": "security-scanner",        "workspace": "~/agents/security",        "tools": { "allow": ["read", "exec"] }      },      {        "id": "test-coverage",        "workspace": "~/agents/testing",        "tools": { "allow": ["read", "exec"] }      },      { "id": "docs-checker", "workspace": "~/agents/docs", "tools": { "allow": ["read"] } }    ]  }}
[/code]

**User भेजता है:** Code snippet।

**जवाब:**

  * code-formatter: "Fixed indentation and added type hints"
  * security-scanner: "⚠️ SQL injection vulnerability in line 12"
  * test-coverage: "Coverage is 45%, missing tests for error cases"
  * docs-checker: "Missing docstring for function `process_data`"

उदाहरण 2: बहुभाषी सहायता jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "+15555550123": ["detect-language", "translator-en", "translator-de"]  },  "agents": {    "list": [      { "id": "detect-language", "workspace": "~/agents/lang-detect" },      { "id": "translator-en", "workspace": "~/agents/translate-en" },      { "id": "translator-de", "workspace": "~/agents/translate-de" }    ]  }}
[/code]

## API संदर्भ

### Config schema

typescriptCopy code
[code]
    interface OpenClawConfig {  broadcast?: {    strategy?: "parallel" | "sequential";    [peerId: string]: string[];  };}
[/code]

### फ़ील्ड

एजेंटों को कैसे प्रोसेस करना है। `parallel` सभी एजेंटों को साथ-साथ चलाता है; `sequential` उन्हें array order में चलाता है।

WhatsApp समूह JID, E.164 नंबर, या अन्य peer ID। मान उन agent IDs की array है जिन्हें संदेश प्रोसेस करने चाहिए।

## सीमाएं

  1. **अधिकतम एजेंट:** कोई सख्त सीमा नहीं है, लेकिन 10+ एजेंट धीमे हो सकते हैं।
  2. **साझा संदर्भ:** एजेंट एक-दूसरे की प्रतिक्रियाएँ नहीं देखते (डिज़ाइन के अनुसार)।
  3. **संदेश क्रम:** समानांतर प्रतिक्रियाएँ किसी भी क्रम में आ सकती हैं।
  4. **दर सीमाएँ:** सभी एजेंट WhatsApp दर सीमाओं में गिने जाते हैं।


## भावी सुधार

नियोजित सुविधाएँ:

  * [ ] साझा संदर्भ मोड (एजेंट एक-दूसरे की प्रतिक्रियाएँ देखते हैं)
  * [ ] एजेंट समन्वय (एजेंट एक-दूसरे को संकेत दे सकते हैं)
  * [ ] गतिशील एजेंट चयन (संदेश सामग्री के आधार पर एजेंट चुनें)
  * [ ] एजेंट प्राथमिकताएँ (कुछ एजेंट दूसरों से पहले प्रतिक्रिया देते हैं)


## संबंधित

  * [चैनल रूटिंग](</hi/channels/channel-routing>)
  * [समूह](</hi/channels/groups>)
  * [बहु-एजेंट सैंडबॉक्स टूल्स](</hi/tools/multi-agent-sandbox-tools>)
  * [पेयरिंग](</hi/channels/pairing>)
  * [सत्र प्रबंधन](</hi/concepts/session>)


Was this useful?YesNo

Open issue