---
title: Skills बनाना
source_url: https://docs.openclaw.ai/hi/tools/creating-skills
scraped_at: 2026-06-29
---

CapabilitiesSkills

Skills एजेंट को सिखाते हैं कि टूल्स का उपयोग कैसे और कब करना है। हर skill एक डायरेक्टरी होती है जिसमें YAML frontmatter और markdown निर्देशों वाली `SKILL.md` फ़ाइल होती है। OpenClaw कई roots से skills को एक निर्धारित [precedence order](</hi/tools/skills#loading-order>) में लोड करता है।

## अपनी पहली skill बनाएँ

* ### Create the skill directory

Skills आपके workspace के `skills/` फ़ोल्डर में रहती हैं। अपनी नई skill के लिए एक डायरेक्टरी बनाएँ:

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/hello-world
[/code]

संगठन के लिए आप skills को subfolders में समूहित कर सकते हैं — फिर भी skill का नाम `SKILL.md` frontmatter से तय होता है, फ़ोल्डर path से नहीं:

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/personal/hello-world# skill name is still "hello-world", invoked as /hello-world
[/code]

* ### Write SKILL.md

डायरेक्टरी के अंदर `SKILL.md` बनाएँ। frontmatter metadata परिभाषित करता है; body एजेंट को निर्देश देता है।

markdownCopy code
[code]
    ---name: hello-worlddescription: A simple skill that prints a greeting.--- # Hello World When the user asks for a greeting, use the `exec` tool to run: ```bashecho "Hello from your custom skill!"
[/code]

CodeCopy code
[code]
     नामकरण नियम:- `name` के लिए lowercase अक्षर, अंक और hyphens का उपयोग करें।- डायरेक्टरी नाम और frontmatter `name` को समान रखें।- `description` एजेंट को और slash-command discovery में दिखाया जाता है —  इसे एक पंक्ति में और 160 वर्णों से कम रखें।  OPENCLAW_DOCS_MARKER:stepClose:   OPENCLAW_DOCS_MARKER:stepOpen:IHRpdGxlPSJWZXJpZnkgdGhlIHNraWxsIGxvYWRlZCI ```bashopenclaw skills list
[/code]

OpenClaw डिफ़ॉल्ट रूप से skills roots के अंतर्गत `SKILL.md` फ़ाइलों को देखता है। यदि watcher अक्षम है या आप किसी मौजूदा session को जारी रख रहे हैं, तो एक नया session शुरू करें ताकि एजेंट को refreshed सूची मिल सके:

bashCopy code
[code]
    # From chat — archive current session and start fresh/new # Or restart the gatewayopenclaw gateway restart
[/code]

* ### Test it

ऐसा संदेश भेजें जिससे skill trigger होनी चाहिए:

bashCopy code
[code]
    openclaw agent --message "give me a greeting"
[/code]

या chat खोलें और एजेंट से सीधे पूछें। नाम से स्पष्ट रूप से invoke करने के लिए `/skill hello-world` का उपयोग करें।

## SKILL.md संदर्भ

### आवश्यक fields

Field | Description  
---|---  
`name` | lowercase अक्षरों, अंकों और hyphens वाला unique slug  
`description` | एजेंट और discovery output में दिखाया जाने वाला एक-पंक्ति विवरण  
  
### वैकल्पिक frontmatter keys

Field | Default | Description  
---|---|---  
`user-invocable` | `true` | skill को user slash command के रूप में expose करें  
`disable-model-invocation` | `false` | skill को एजेंट के system prompt से बाहर रखें (`/skill` के ज़रिए फिर भी चलता है)  
`command-dispatch` | — | model को bypass करते हुए slash command को सीधे tool पर route करने के लिए `tool` पर set करें  
`command-tool` | — | `command-dispatch: tool` set होने पर invoke किया जाने वाला tool नाम  
`command-arg-mode` | `raw` | tool dispatch के लिए raw args string को tool तक forward करता है  
`homepage` | — | macOS Skills UI में "Website" के रूप में दिखाया जाने वाला URL  
  
Gating fields (`requires.bins`, `requires.env`, आदि) के लिए देखें [Skills — Gating](</hi/tools/skills#gating>)।

### `{baseDir}` का उपयोग

skill body में `{baseDir}` का उपयोग करके hardcoded paths के बिना skill डायरेक्टरी के अंदर की फ़ाइलों को reference करें:

markdownCopy code
[code]
    Run the helper script at `{baseDir}/scripts/run.sh`.
[/code]

## conditional activation जोड़ना

अपनी skill को gate करें ताकि वह केवल तब load हो जब उसकी dependencies उपलब्ध हों:

markdownCopy code
[code]
    ---name: gemini-searchdescription: Search using Gemini CLI.metadata: { "openclaw": { "requires": { "bins": ["gemini"] }, "primaryEnv": "GEMINI_API_KEY" } }---
[/code]

Gating options

Key | Description  
---|---  
`requires.bins` | सभी binaries `PATH` पर मौजूद होनी चाहिए  
`requires.anyBins` | कम से कम एक binary `PATH` पर मौजूद होनी चाहिए  
`requires.env` | हर env var process या config में मौजूद होना चाहिए  
`requires.config` | हर `openclaw.json` path truthy होना चाहिए  
`os` | Platform filter: `["darwin"]`, `["linux"]`, `["win32"]`  
`always` | सभी gates छोड़ने और skill को हमेशा शामिल करने के लिए `true` set करें  
  
पूरा संदर्भ: [Skills — Gating](</hi/tools/skills#gating>)।

Environment and API keys

`openclaw.json` में किसी skill entry से API key जोड़ें:

json5Copy code
[code]
    {  skills: {    entries: {      "gemini-search": {        enabled: true,        apiKey: { source: "env", provider: "default", id: "GEMINI_API_KEY" },      },    },  },}
[/code]

key केवल उस agent turn के लिए host process में inject की जाती है। यह sandbox तक नहीं पहुँचती — देखें [sandboxed env vars](</hi/tools/skills-config#sandboxed-skills-and-env-vars>)।

## Skill Workshop के ज़रिए प्रस्ताव दें

agent-drafted skills के लिए या जब आप किसी skill के live होने से पहले operator review चाहते हों, `SKILL.md` सीधे लिखने के बजाय [Skill Workshop](</hi/tools/skill-workshop>) proposals का उपयोग करें।

bashCopy code
[code]
    # Propose a brand-new skillopenclaw skills workshop propose-create \  --name "hello-world" \  --description "A simple skill that prints a greeting." \  --proposal ./PROPOSAL.md # Propose an update to an existing skillopenclaw skills workshop propose-update hello-world \  --proposal ./PROPOSAL.md \  --description "Updated greeting skill"
[/code]

जब proposal में support files शामिल हों, तो `--proposal-dir` का उपयोग करें:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name "hello-world" \  --description "A simple skill that prints a greeting." \  --proposal-dir ./hello-world-proposal/
[/code]

डायरेक्टरी में `PROPOSAL.md` होना चाहिए। Support files `assets/`, `examples/`, `references/`, `scripts/`, या `templates/` में जा सकती हैं।

review के बाद:

bashCopy code
[code]
    openclaw skills workshop inspect <proposal-id>openclaw skills workshop apply <proposal-id>
[/code]

पूरे proposal lifecycle के लिए [Skill Workshop](</hi/tools/skill-workshop>) देखें।

## ClawHub पर publish करना

* ### Ensure your SKILL.md is complete

सुनिश्चित करें कि `name`, `description`, और कोई भी `metadata.openclaw` gating fields set हैं। यदि आपके पास project page है तो `homepage` URL जोड़ें।

* ### Install the ClawHub skill

ClawHub skill current publish command shape और आवश्यक metadata को document करती है:

bashCopy code
[code]
    openclaw skills install @openclaw/clawhub-publish
[/code]

* ### Publish

bashCopy code
[code]
    clawhub publish
[/code]

पूरे flow के लिए [ClawHub — Publishing](</hi/clawhub/publishing>) देखें।

## Best practices

## संबंधित

[**Skills reference** Loading order, gating, allowlists, और SKILL.md format। ](</hi/tools/skills>) [**Skill Workshop** agent-drafted skills के लिए proposal queue। ](</hi/tools/skill-workshop>) [**Skills config** पूरा `skills.*` config schema। ](</hi/tools/skills-config>) [**ClawHub** public registry पर skills browse और publish करें। ](</hi/clawhub>) [**Building plugins** Plugins उन tools के साथ skills ship कर सकते हैं जिन्हें वे document करते हैं। ](</hi/plugins/building-plugins>)

Was this useful?YesNo

Open issue