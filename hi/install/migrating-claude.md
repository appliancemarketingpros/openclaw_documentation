---
title: Claude से माइग्रेट करना
source_url: https://docs.openclaw.ai/hi/install/migrating-claude
scraped_at: 2026-06-29
---

InstallMaintenance

OpenClaw स्थानीय Claude स्थिति को बंडल किए गए Claude माइग्रेशन प्रदाता के माध्यम से आयात करता है। प्रदाता स्थिति बदलने से पहले हर आइटम का पूर्वावलोकन करता है, योजनाओं और रिपोर्टों में सीक्रेट्स को रिडैक्ट करता है, और लागू करने से पहले सत्यापित बैकअप बनाता है।

## आयात करने के दो तरीके

### Onboarding wizard

विज़ार्ड स्थानीय Claude स्थिति का पता लगने पर Claude की पेशकश करता है।

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

या किसी विशिष्ट स्रोत की ओर इंगित करें:

bashCopy code
[code]
    openclaw onboard --import-from claude --import-source ~/.claude
[/code]

### CLI

स्क्रिप्टेड या दोहराए जा सकने वाले रन के लिए `openclaw migrate` का उपयोग करें। पूर्ण संदर्भ के लिए [`openclaw migrate`](</hi/cli/migrate>) देखें।

bashCopy code
[code]
    openclaw migrate claude --dry-runopenclaw migrate apply claude --yes
[/code]

किसी विशिष्ट Claude Code होम या प्रोजेक्ट रूट को आयात करने के लिए `--from <path>` जोड़ें।

## क्या आयात होता है

Instructions and memory

  * प्रोजेक्ट `CLAUDE.md` और `.claude/CLAUDE.md` सामग्री को OpenClaw एजेंट वर्कस्पेस `AGENTS.md` में कॉपी या अपेंड किया जाता है।
  * उपयोगकर्ता `~/.claude/CLAUDE.md` सामग्री को वर्कस्पेस `USER.md` में अपेंड किया जाता है।

MCP servers

MCP सर्वर परिभाषाएँ मौजूद होने पर प्रोजेक्ट `.mcp.json`, Claude Code `~/.claude.json`, और Claude Desktop `claude_desktop_config.json` से आयात की जाती हैं।

Skills and commands

  * `SKILL.md` फ़ाइल वाले Claude skills को OpenClaw वर्कस्पेस Skills डायरेक्टरी में कॉपी किया जाता है।
  * `.claude/commands/` या `~/.claude/commands/` के अंतर्गत Claude कमांड Markdown फ़ाइलों को `disable-model-invocation: true` के साथ OpenClaw Skills में बदला जाता है।


## क्या केवल आर्काइव में रहता है

प्रदाता इन्हें मैन्युअल समीक्षा के लिए माइग्रेशन रिपोर्ट में कॉपी करता है, लेकिन इन्हें लाइव OpenClaw कॉन्फ़िग में लोड **नहीं** करता:

  * Claude hooks
  * Claude अनुमतियाँ और विस्तृत टूल allowlists
  * Claude पर्यावरण डिफ़ॉल्ट्स
  * `CLAUDE.local.md`
  * `.claude/rules/`
  * `.claude/agents/` या `~/.claude/agents/` के अंतर्गत Claude subagents
  * Claude Code कैश, योजनाएँ, और प्रोजेक्ट इतिहास डायरेक्टरियाँ
  * Claude Desktop एक्सटेंशन्स और OS-संग्रहीत क्रेडेंशियल्स


OpenClaw hooks चलाने, अनुमति allowlists पर भरोसा करने, या अपारदर्शी OAuth और Desktop क्रेडेंशियल स्थिति को स्वचालित रूप से डिकोड करने से इनकार करता है। आर्काइव की समीक्षा करने के बाद जो चाहिए उसे हाथ से स्थानांतरित करें।

## स्रोत चयन

`--from` के बिना, OpenClaw `~/.claude` पर डिफ़ॉल्ट Claude Code होम, सैंपल की गई Claude Code `~/.claude.json` स्थिति फ़ाइल, और macOS पर Claude Desktop MCP कॉन्फ़िग की जाँच करता है।

जब `--from` किसी प्रोजेक्ट रूट की ओर इंगित करता है, तो OpenClaw केवल उस प्रोजेक्ट की Claude फ़ाइलें आयात करता है, जैसे `CLAUDE.md`, `.claude/settings.json`, `.claude/commands/`, `.claude/skills/`, और `.mcp.json`। यह प्रोजेक्ट-रूट आयात के दौरान आपके ग्लोबल Claude होम को नहीं पढ़ता।

## अनुशंसित प्रवाह

* ### Preview the plan

bashCopy code
[code]
    openclaw migrate claude --dry-run
[/code]

योजना उन सभी चीज़ों को सूचीबद्ध करती है जो बदलेंगी, जिनमें conflicts, छोड़े गए आइटम, और नेस्टेड MCP `env` या `headers` फ़ील्ड से रिडैक्ट किए गए संवेदनशील मान शामिल हैं।

* ### Apply with backup

bashCopy code
[code]
    openclaw migrate apply claude --yes
[/code]

OpenClaw लागू करने से पहले बैकअप बनाता और सत्यापित करता है।

* ### Run doctor

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</hi/gateway/doctor>) आयात के बाद कॉन्फ़िग या स्थिति समस्याओं की जाँच करता है।

* ### Restart and verify

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

पुष्टि करें कि Gateway स्वस्थ है और आपके आयातित निर्देश, MCP सर्वर, और skills लोड हैं।

## Conflict प्रबंधन

जब योजना conflicts की रिपोर्ट करती है (लक्ष्य पर फ़ाइल या कॉन्फ़िग मान पहले से मौजूद है), तो लागू करना आगे बढ़ने से इनकार करता है।

नए OpenClaw इंस्टॉल के लिए conflicts असामान्य हैं। वे आम तौर पर तब दिखाई देते हैं जब आप ऐसे सेटअप पर आयात दोबारा चलाते हैं जिसमें पहले से उपयोगकर्ता edits मौजूद हैं।

## ऑटोमेशन के लिए JSON आउटपुट

bashCopy code
[code]
    openclaw migrate claude --dry-run --jsonopenclaw migrate apply claude --json --yes
[/code]

`--json` और बिना `--yes` के, apply योजना प्रिंट करता है और स्थिति को नहीं बदलता। यह CI और साझा scripts के लिए सबसे सुरक्षित मोड है।

## समस्या निवारण

Claude state lives outside ~/.claude

`--from /actual/path` (CLI) या `--import-source /actual/path` (ऑनबोर्डिंग) पास करें।

Onboarding refuses to import on an existing setup

ऑनबोर्डिंग आयातों के लिए नया सेटअप आवश्यक है। या तो स्थिति रीसेट करें और फिर से ऑनबोर्ड करें, या सीधे `openclaw migrate apply claude` का उपयोग करें, जो `--overwrite` और स्पष्ट बैकअप नियंत्रण का समर्थन करता है।

MCP servers from Claude Desktop did not import

Claude Desktop `claude_desktop_config.json` को प्लेटफ़ॉर्म-विशिष्ट पथ से पढ़ता है। अगर OpenClaw ने इसे स्वचालित रूप से नहीं पहचाना, तो `--from` को उस फ़ाइल की डायरेक्टरी पर इंगित करें।

Claude commands became skills with model invocation disabled

यह डिज़ाइन के अनुसार है। Claude कमांड उपयोगकर्ता-द्वारा-ट्रिगर होते हैं, इसलिए OpenClaw उन्हें `disable-model-invocation: true` के साथ skills के रूप में आयात करता है। अगर आप चाहते हैं कि एजेंट उन्हें स्वचालित रूप से invoke करे, तो प्रत्येक skill का frontmatter संपादित करें।

## संबंधित

  * [`openclaw migrate`](</hi/cli/migrate>): पूर्ण CLI संदर्भ, Plugin कॉन्ट्रैक्ट, और JSON shapes।
  * [माइग्रेशन गाइड](</hi/install/migrating>): सभी माइग्रेशन पथ।
  * [Hermes से माइग्रेट करना](</hi/install/migrating-hermes>): दूसरा cross-system आयात पथ।
  * [ऑनबोर्डिंग](</hi/cli/onboard>): विज़ार्ड प्रवाह और non-interactive flags।
  * [Doctor](</hi/gateway/doctor>): माइग्रेशन के बाद स्वास्थ्य जाँच।
  * [एजेंट वर्कस्पेस](</hi/concepts/agent-workspace>): जहाँ `AGENTS.md`, `USER.md`, और skills रहते हैं।


Was this useful?YesNo

Open issue