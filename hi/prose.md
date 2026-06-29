---
title: ओपनप्रोज़
source_url: https://docs.openclaw.ai/hi/prose
scraped_at: 2026-06-29
---

CapabilitiesSkills

OpenProse AI सत्रों को संचालित करने के लिए एक पोर्टेबल, markdown-first वर्कफ़्लो फ़ॉर्मैट है। OpenClaw में यह एक Plugin के रूप में आता है, जो एक OpenProse कौशल पैक और `/prose` slash कमांड इंस्टॉल करता है। प्रोग्राम `.prose` फ़ाइलों में रहते हैं और स्पष्ट नियंत्रण प्रवाह के साथ कई sub-agents शुरू कर सकते हैं।

**Install** OpenProse Plugin सक्षम करें और Gateway फिर से शुरू करें। **Run a program** किसी `.prose` फ़ाइल या रिमोट प्रोग्राम को चलाने के लिए `/prose run` का उपयोग करें। **Write programs** समानांतर और क्रमिक चरणों के साथ multi-agent वर्कफ़्लो लिखें।

## इंस्टॉल करें

* ### Enable the plugin

Bundled plugins डिफ़ॉल्ट रूप से अक्षम होते हैं। OpenProse सक्षम करें:

bashCopy code
[code]
    openclaw plugins enable open-prose
[/code]

* ### Restart the Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

* ### Verify

bashCopy code
[code]
    openclaw plugins list | grep prose
[/code]

आपको `open-prose` सक्षम के रूप में दिखना चाहिए। `/prose` कौशल कमांड अब चैट में उपलब्ध है।

स्थानीय checkout के लिए: `openclaw plugins install ./path/to/local/open-prose-plugin`

## Slash कमांड

OpenProse `/prose` को उपयोगकर्ता द्वारा चलाए जा सकने वाले कौशल कमांड के रूप में पंजीकृत करता है:

textCopy code
[code]
    /prose help/prose run <file.prose>/prose run <handle/slug>/prose run <https://example.com/file.prose>/prose compile <file.prose>/prose examples/prose update
[/code]

`/prose run <handle/slug>` `https://p.prose.md/<handle>/<slug>` पर resolve होता है। सीधे URLs को `web_fetch` टूल का उपयोग करके जैसे हैं वैसे fetch किया जाता है।

Top-level रिमोट runs स्पष्ट होते हैं। `.prose` प्रोग्राम के अंदर रिमोट imports transitive code dependencies हैं: OpenProse किसी भी रिमोट `use` target को fetch करने से पहले, resolved import list दिखाता है और उस run के लिए operator से ठीक `approve remote prose imports` जवाब देने की आवश्यकता होती है।

## यह क्या कर सकता है

  * स्पष्ट parallelism के साथ multi-agent research और synthesis।
  * दोहराए जा सकने वाले, approval-safe वर्कफ़्लो (code review, incident triage, content pipelines)।
  * पुन: उपयोग योग्य `.prose` प्रोग्राम जिन्हें आप समर्थित agent runtimes में चला सकते हैं।


## उदाहरण: समानांतर research और synthesis

proseCopy code
[code]
    # Research + synthesis with two agents running in parallel. input topic: "What should we research?" agent researcher:  model: sonnet  prompt: "You research thoroughly and cite sources." agent writer:  model: opus  prompt: "You write a concise summary." parallel:  findings = session: researcher    prompt: "Research {topic}."  draft = session: writer    prompt: "Summarize {topic}." session "Merge the findings + draft into a final answer."context: { findings, draft }
[/code]

## OpenClaw runtime mapping

OpenProse प्रोग्राम OpenClaw primitives पर map होते हैं:

OpenProse concept | OpenClaw tool  
---|---  
Spawn session / Task tool | `sessions_spawn`  
File read / write | `read` / `write`  
Web fetch | `web_fetch`  
  
## फ़ाइल स्थान

OpenProse आपके workspace में `.prose/` के अंतर्गत state रखता है:

textCopy code
[code]
    .prose/├── .env├── runs/│   └── {YYYYMMDD}-{HHMMSS}-{random}/│       ├── program.prose│       ├── state.md│       ├── bindings/│       └── agents/└── agents/
[/code]

User-level persistent agents यहां रहते हैं:

textCopy code
[code]
    ~/.prose/agents/
[/code]

## State backends

filesystem (default)

State workspace में `.prose/runs/...` पर लिखा जाता है। कोई अतिरिक्त dependencies आवश्यक नहीं हैं।

in-context

Transient state context window में रखा जाता है। छोटे, कम समय तक चलने वाले प्रोग्रामों के लिए उपयुक्त।

sqlite (experimental)

`PATH` पर `sqlite3` binary की आवश्यकता होती है।

postgres (experimental)

`psql` और connection string की आवश्यकता होती है।

## सुरक्षा

`.prose` फ़ाइलों को code की तरह मानें। उन्हें चलाने से पहले review करें, जिसमें रिमोट `use` imports भी शामिल हैं। Top-level `/prose run https://...` अनुरोध स्पष्ट होते हैं, लेकिन transitive remote imports को fetch या execute करने से पहले प्रति-run approval की आवश्यकता होती है। Side effects को नियंत्रित करने के लिए OpenClaw tool allowlists और approval gates का उपयोग करें। Deterministic, approval-gated वर्कफ़्लो के लिए, [Lobster](</hi/tools/lobster>) से तुलना करें।

## संबंधित

[**Skills reference** OpenProse का कौशल पैक कैसे load होता है और कौन-से gates लागू होते हैं। ](</hi/tools/skills>) [**Subagents** OpenClaw की native multi-agent coordination layer। ](</hi/tools/subagents>) [**Text-to-speech** अपने वर्कफ़्लो में audio output जोड़ें। ](</hi/tools/tts>) [**Slash commands** /prose सहित सभी उपलब्ध chat commands। ](</hi/tools/slash-commands>)

आधिकारिक साइट: <https://www.prose.md>

Was this useful?YesNo

Open issue