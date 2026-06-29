---
title: बहु-एजेंट सैंडबॉक्स और टूल्स
source_url: https://docs.openclaw.ai/hi/tools/multi-agent-sandbox-tools
scraped_at: 2026-06-29
---

CapabilitiesAgent coordination

मल्टी-एजेंट सेटअप में हर एजेंट वैश्विक सैंडबॉक्स और टूल नीति को ओवरराइड कर सकता है। यह पेज प्रति-एजेंट कॉन्फ़िगरेशन, प्राथमिकता नियमों और उदाहरणों को कवर करता है।

[**सैंडबॉक्सिंग** बैकएंड और मोड — पूरा सैंडबॉक्स संदर्भ। ](</hi/gateway/sandboxing>) [**सैंडबॉक्स बनाम टूल नीति बनाम उन्नत** डिबग करें कि "यह क्यों ब्लॉक है?" ](</hi/gateway/sandbox-vs-tool-policy-vs-elevated>) [**उन्नत मोड** विश्वसनीय प्रेषकों के लिए उन्नत exec। ](</hi/tools/elevated>)

* * *

## कॉन्फ़िगरेशन उदाहरण

उदाहरण 1: व्यक्तिगत + प्रतिबंधित पारिवारिक एजेंट jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "name": "Personal Assistant",        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      },      {        "id": "family",        "name": "Family Bot",        "workspace": "~/.openclaw/workspace-family",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read", "message"],          "deny": ["exec", "write", "edit", "apply_patch", "process", "browser"],          "message": {            "crossContext": {              "allowWithinProvider": false,              "allowAcrossProviders": false            }          }        }      }    ]  },  "bindings": [    {      "agentId": "family",      "match": {        "provider": "whatsapp",        "accountId": "*",        "peer": {          "kind": "group",          "id": "120363424282127706@g.us"        }      }    }  ]}
[/code]

**परिणाम:**

  * `main` एजेंट: होस्ट पर चलता है, पूरा टूल एक्सेस।
  * `family` एजेंट: Docker में चलता है (प्रति एजेंट एक container), केवल `read` और मौजूदा-बातचीत वाले संदेश भेजना।

उदाहरण 2: साझा सैंडबॉक्स वाला कार्य एजेंट jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "personal",        "workspace": "~/.openclaw/workspace-personal",        "sandbox": { "mode": "off" }      },      {        "id": "work",        "workspace": "~/.openclaw/workspace-work",        "sandbox": {          "mode": "all",          "scope": "shared",          "workspaceRoot": "/tmp/work-sandboxes"        },        "tools": {          "allow": ["read", "write", "apply_patch", "exec"],          "deny": ["browser", "gateway", "discord"]        }      }    ]  }}
[/code]

उदाहरण 2b: वैश्विक coding profile + केवल-संदेश एजेंट jsonCopy code
[code]
    {  "tools": { "profile": "coding" },  "agents": {    "list": [      {        "id": "support",        "tools": { "profile": "messaging", "allow": ["slack"] }      }    ]  }}
[/code]

**परिणाम:**

  * डिफ़ॉल्ट एजेंटों को coding tools मिलते हैं।
  * `support` एजेंट केवल-संदेश है (+ Slack tool)।

उदाहरण 3: प्रति एजेंट अलग-अलग सैंडबॉक्स मोड jsonCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "non-main",        "scope": "session"      }    },    "list": [      {        "id": "main",        "workspace": "~/.openclaw/workspace",        "sandbox": {          "mode": "off"        }      },      {        "id": "public",        "workspace": "~/.openclaw/workspace-public",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read"],          "deny": ["exec", "write", "edit", "apply_patch"]        }      }    ]  }}
[/code]

* * *

## कॉन्फ़िगरेशन प्राथमिकता

जब वैश्विक (`agents.defaults.*`) और एजेंट-विशिष्ट (`agents.list[].*`) दोनों configs मौजूद हों:

### सैंडबॉक्स config

एजेंट-विशिष्ट सेटिंग्स वैश्विक को ओवरराइड करती हैं:

CodeCopy code
[code]
    agents.list[].sandbox.mode > agents.defaults.sandbox.modeagents.list[].sandbox.scope > agents.defaults.sandbox.scopeagents.list[].sandbox.workspaceRoot > agents.defaults.sandbox.workspaceRootagents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccessagents.list[].sandbox.docker.* > agents.defaults.sandbox.docker.*agents.list[].sandbox.browser.* > agents.defaults.sandbox.browser.*agents.list[].sandbox.prune.* > agents.defaults.sandbox.prune.*
[/code]

### टूल प्रतिबंध

फ़िल्टरिंग क्रम यह है:

* ### टूल profile

`tools.profile` या `agents.list[].tools.profile`।

* ### प्रदाता टूल profile

`tools.byProvider[provider].profile` या `agents.list[].tools.byProvider[provider].profile`।

* ### वैश्विक टूल नीति

`tools.allow` / `tools.deny`।

* ### प्रदाता टूल नीति

`tools.byProvider[provider].allow/deny`।

* ### एजेंट-विशिष्ट टूल नीति

`agents.list[].tools.allow/deny`।

* ### एजेंट प्रदाता नीति

`agents.list[].tools.byProvider[provider].allow/deny`।

* ### सैंडबॉक्स टूल नीति

`tools.sandbox.tools` या `agents.list[].tools.sandbox.tools`।

* ### उप-एजेंट टूल नीति

`tools.subagents.tools`, यदि लागू हो।

प्राथमिकता नियम

  * हर स्तर टूल्स को और प्रतिबंधित कर सकता है, लेकिन पहले के स्तरों से deny किए गए टूल्स को वापस grant नहीं कर सकता।
  * यदि `agents.list[].tools.sandbox.tools` सेट है, तो यह उस एजेंट के लिए `tools.sandbox.tools` को बदल देता है।
  * यदि `agents.list[].tools.profile` सेट है, तो यह उस एजेंट के लिए `tools.profile` को ओवरराइड करता है।
  * प्रदाता टूल keys या तो `provider` (जैसे `google-antigravity`) या `provider/model` (जैसे `openai/gpt-5.4`) स्वीकार करती हैं।

खाली अनुमति-सूची व्यवहार

यदि उस chain में कोई भी स्पष्ट अनुमति-सूची run को बिना callable tools के छोड़ देती है, तो OpenClaw prompt को model पर सबमिट करने से पहले रुक जाता है। यह जानबूझकर है: `agents.list[].tools.allow: ["query_db"]` जैसे missing tool के साथ configure किया गया एजेंट तब तक स्पष्ट रूप से fail होना चाहिए जब तक `query_db` register करने वाला Plugin enabled न हो, न कि text-only एजेंट के रूप में जारी रहे।

टूल नीतियां `group:*` shorthands का समर्थन करती हैं, जो कई टूल्स में expand होते हैं। पूरी सूची के लिए [टूल groups](</hi/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands>) देखें।

प्रति-एजेंट उन्नत overrides (`agents.list[].tools.elevated`) specific agents के लिए उन्नत exec को और प्रतिबंधित कर सकते हैं। विवरण के लिए [उन्नत मोड](</hi/tools/elevated>) देखें।

* * *

## एकल एजेंट से माइग्रेशन

### Before (single agent)

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "workspace": "~/.openclaw/workspace",      "sandbox": {        "mode": "non-main"      }    }  },  "tools": {    "sandbox": {      "tools": {        "allow": ["read", "write", "apply_patch", "exec"],        "deny": []      }    }  }}
[/code]

### After (multi-agent)

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      }    ]  }}
[/code]

* * *

## टूल प्रतिबंध उदाहरण

### Read-only agent

jsonCopy code
[code]
    {  "tools": {    "allow": ["read"],    "deny": ["exec", "write", "edit", "apply_patch", "process"]  }}
[/code]

### Shell execution with filesystem tools disabled

jsonCopy code
[code]
    {  "tools": {    "allow": ["read", "exec", "process"],    "deny": ["write", "edit", "apply_patch", "browser", "gateway"]  }}
[/code]

### Communication-only

jsonCopy code
[code]
    {  "tools": {    "sessions": { "visibility": "tree" },    "allow": ["sessions_list", "sessions_send", "sessions_history", "session_status"],    "deny": ["exec", "write", "edit", "apply_patch", "read", "browser"]  }}
[/code]

इस प्रोफ़ाइल में `sessions_history` अब भी कच्चे ट्रांसक्रिप्ट डंप के बजाय एक सीमित, सैनिटाइज़ किया हुआ रिकॉल दृश्य लौटाता है। Assistant रिकॉल सोच टैग, `<relevant-memories>` स्कैफ़ोल्डिंग, सादे-पाठ टूल-कॉल XML पेलोड (`<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>`, और काटे गए टूल-कॉल ब्लॉक सहित), डाउनग्रेड की गई टूल-कॉल स्कैफ़ोल्डिंग, लीक हुए ASCII/पूर्ण-चौड़ाई मॉडल नियंत्रण टोकन, और विकृत MiniMax टूल-कॉल XML को रिडैक्शन/ट्रंकेशन से पहले हटा देता है।

* * *

## सामान्य गलती: "non-main"

* * *

## परीक्षण

बहु-एजेंट sandbox और टूल कॉन्फ़िगर करने के बाद:

* ### Check agent resolution

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

* ### Verify sandbox containers

bashCopy code
[code]
    docker ps --filter "name=openclaw-sbx-"
[/code]

* ### Test tool restrictions

  * ऐसा संदेश भेजें जिसके लिए प्रतिबंधित टूल चाहिए।
  * सत्यापित करें कि एजेंट अस्वीकृत टूल का उपयोग नहीं कर सकता।


* ### Monitor logs

bashCopy code
[code]
    tail -f "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs/gateway.log" | grep -E "routing|sandbox|tools"
[/code]

* * *

## समस्या निवारण

Agent not sandboxed despite `mode: 'all'`

  * जाँचें कि कहीं कोई वैश्विक `agents.defaults.sandbox.mode` तो नहीं है जो इसे ओवरराइड कर रहा है।
  * एजेंट-विशिष्ट कॉन्फ़िगरेशन को प्राथमिकता मिलती है, इसलिए `agents.list[].sandbox.mode: "all"` सेट करें।

Tools still available despite deny list

  * टूल फ़िल्टरिंग क्रम जाँचें: वैश्विक → एजेंट → sandbox → उप-एजेंट।
  * प्रत्येक स्तर केवल और प्रतिबंधित कर सकता है, अनुमति वापस नहीं दे सकता।
  * लॉग से सत्यापित करें: `[tools] filtering tools for agent:${agentId}`।

Container not isolated per agent

  * एजेंट-विशिष्ट sandbox कॉन्फ़िगरेशन में `scope: "agent"` सेट करें।
  * डिफ़ॉल्ट `"session"` है, जो प्रति सत्र एक कंटेनर बनाता है।


* * *

## संबंधित

  * [Elevated मोड](</hi/tools/elevated>)
  * [Multi-agent रूटिंग](</hi/concepts/multi-agent>)
  * [Sandbox कॉन्फ़िगरेशन](</hi/gateway/config-agents#agentsdefaultssandbox>)
  * [Sandbox बनाम टूल नीति बनाम elevated](</hi/gateway/sandbox-vs-tool-policy-vs-elevated>) — डिबगिंग: "यह अवरुद्ध क्यों है?"
  * [Sandboxing](</hi/gateway/sandboxing>) — पूरा sandbox संदर्भ (मोड, स्कोप, बैकएंड, इमेज)
  * [सेशन प्रबंधन](</hi/concepts/session>)


Was this useful?YesNo

Open issue